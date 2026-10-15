#!/usr/bin/env python3
"""Comprueba si Apple ha cambiado algo desde la última actualización de la skill.

Compara con `scripts/estado_fuentes.json` (solo fechas y listas, sin contenido de Apple):
  - la fecha más reciente del «Change log» de cada página de las HIG (y páginas nuevas o retiradas);
  - las entradas de https://developer.apple.com/design/whats-new/;
  - la lista de vídeos de https://developer.apple.com/videos/design/.

Uso:
    python3 comprobar_novedades.py                 # informe (1 petición/s; ~3 min)
    python3 comprobar_novedades.py --rapido        # solo What's new + lista de vídeos + índice de las HIG
    python3 comprobar_novedades.py --guardar-estado --fuentes ./_fuentes   # regenera el estado desde la caché

Si hay cambios, sigue los pasos que imprime (descargar → generar referencias → revisar resúmenes).
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comun import BASE, HIG_DATA, changelog, descargar, fecha_iso, hoy  # noqa: E402

ESTADO = Path(__file__).resolve().parent / "estado_fuentes.json"
RX_VID = re.compile(r'href="/videos/play/([a-z0-9-]+/\d+)/?"')


def entradas_whats_new(html: str) -> list[str]:
    txt = re.sub(r"<[^>]+>", " ", html)
    txt = re.sub(r"\s+", " ", txt)
    fechas = re.findall(r"((?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4})", txt)
    return sorted({fecha_iso(f) for f in fechas}, reverse=True)


def estado_desde_cache(fuentes: Path) -> dict:
    ix = json.loads((fuentes / "hig" / "indice.json").read_text())
    lista = json.loads((fuentes / "videos" / "lista.json").read_text())
    wn = (fuentes / "web" / "dev-design-whats-new.html").read_text(errors="replace")
    return {
        "generado": hoy(),
        "hig": {s: (fecha_iso(e["changelog"][0][0]) if e.get("changelog") else None) for s, e in ix.items() if s != "_raiz"},
        "whats_new_fechas": entradas_whats_new(wn)[:40],
        "videos_design": sorted(k for k, v in lista.items() if "videos/design" in v.get("origen", [])),
    }


def slugs_del_arbol() -> set:
    """Recorre el árbol de secciones (7 peticiones) para detectar páginas nuevas."""
    slugs = set()
    for sec in ["getting-started", "foundations", "patterns", "components", "inputs", "technologies"]:
        cola = [sec]
        while cola:
            s = cola.pop()
            slugs.add(s)
            d = json.loads(descargar(f"{HIG_DATA}/{s}.json"))
            if d.get("metadata", {}).get("role") in ("collectionGroup", "collection"):
                for ts in d.get("topicSections", []) or []:
                    for ident in ts.get("identifiers", []):
                        u = d["references"].get(ident, {}).get("url", "")
                        if u.startswith("/design/human-interface-guidelines/"):
                            h = u.rstrip("/").rsplit("/", 1)[-1].lower()
                            r = d["references"][ident].get("role")
                            if r in ("collectionGroup", "collection") and h not in slugs:
                                cola.append(h)
                            slugs.add(h)
    return slugs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fuentes", default="_fuentes")
    ap.add_argument("--rapido", action="store_true")
    ap.add_argument("--guardar-estado", action="store_true")
    a = ap.parse_args()
    if a.guardar_estado:
        est = estado_desde_cache(Path(a.fuentes))
        ESTADO.write_text(json.dumps(est, ensure_ascii=False, indent=1), encoding="utf-8")
        print("Estado guardado en", ESTADO)
        return
    est = json.loads(ESTADO.read_text())
    cambios = []

    wn = entradas_whats_new(descargar(BASE + "/design/whats-new/").decode("utf-8", "replace"))
    nuevas = [f for f in wn if f > (est["whats_new_fechas"] or ["0"])[0]]
    if nuevas:
        cambios.append(f"What's new tiene entradas nuevas: {', '.join(nuevas)}")

    html = descargar(BASE + "/videos/design/").decode("utf-8", "replace")
    vids = set(RX_VID.findall(html))
    nuevos_v = sorted(vids - set(est["videos_design"]))
    quitados_v = sorted(set(est["videos_design"]) - vids)
    if nuevos_v:
        cambios.append(f"Vídeos nuevos en /videos/design/: {', '.join(nuevos_v)}")
    if quitados_v:
        cambios.append(f"Vídeos retirados de /videos/design/: {', '.join(quitados_v)}")

    arbol = slugs_del_arbol()
    nuevas_p = sorted(arbol - set(est["hig"]))
    if nuevas_p:
        cambios.append(f"Páginas HIG nuevas: {', '.join(nuevas_p)}")
    retiradas = sorted(s for s in est["hig"] if s not in arbol and s not in ("_raiz",))
    if retiradas:
        cambios.append(f"Páginas HIG que ya no están en el árbol (comprobar): {', '.join(retiradas)}")

    if not a.rapido:
        for slug, fecha in sorted(est["hig"].items()):
            try:
                d = json.loads(descargar(f"{HIG_DATA}/{slug}.json"))
            except Exception as e:  # noqa: BLE001
                cambios.append(f"{slug}: no se pudo descargar ({e})")
                continue
            cl = changelog(d)
            actual = fecha_iso(cl[0][0]) if cl else None
            if actual != fecha:
                cambios.append(f"{slug}: cambio {fecha} → {actual}: {cl[0][1] if cl else ''}")

    print(f"Comprobación {hoy()} — estado de referencia {est['generado']}")
    if not cambios:
        print("Sin cambios: la skill está al día.")
        return
    print("\nCAMBIOS DETECTADOS:")
    for c in cambios:
        print(" -", c)
    print("""
Para actualizar:
  1. python3 scripts/descargar_hig.py --fuentes ./_fuentes
  2. python3 scripts/descargar_paginas.py --fuentes ./_fuentes
  3. python3 scripts/descargar_videos.py --fuentes ./_fuentes --solo-nuevos
  4. python3 scripts/generar_referencias.py --fuentes ./_fuentes
  5. python3 scripts/inventario.py --fuentes ./_fuentes
  6. Revisa a mano: novedades (plantillas_fijas/novedades_intro.md), liquid-glass.md, web.md y los
     resúmenes de vídeos nuevos (scripts/resumenes_videos.json, con «ancla» literal para cada regla).
  7. python3 scripts/comprobar_novedades.py --guardar-estado --fuentes ./_fuentes""")
    sys.exit(1)


if __name__ == "__main__":
    main()
