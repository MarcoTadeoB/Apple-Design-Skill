#!/usr/bin/env python3
"""Inventario de lo descargado en `_fuentes/` (páginas HIG, páginas web, vídeos,
transcripciones) con la lista de fallos y huecos. Escribe:
  _fuentes/inventario.md  y  <skill>/references/_inventario.md

Uso: python3 inventario.py --fuentes ./_fuentes --skill ./diseno-apple
"""
import argparse
import collections
import json
from pathlib import Path

# Explicación de huecos conocidos (se revisa a mano al actualizar)
EXPLICACIONES = {
    "spatial-interactions": "Enlace roto en «Designing for iOS»: la página no existe (404 en JSON). No hay contenido que recuperar.",
    "www.apple.com": "Dominio bloqueado por la política de red del entorno (403 del proxy). Hay que permitir www.apple.com y volver a ejecutar descargar_paginas.py.",
    "awards/2019": "Apple devuelve 403 Forbidden: la página de ganadores de 2019 ya no está publicada.",
    "augmented-reality/reality-composer-pro": "URL antigua (404); sustituida por https://developer.apple.com/reality-composer-pro/ (descargada).",
    "sin_transcripcion": "Apple no publica transcripción para estas sesiones (Q&A, «Meet the Presenter», laboratorios en grupo y dos sesiones antiguas): el bloque de transcripción de la página está vacío (comprobado en el HTML).",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fuentes", default="_fuentes")
    ap.add_argument("--skill", default=str(Path(__file__).resolve().parent.parent))
    a = ap.parse_args()
    f = Path(a.fuentes)
    hig = json.loads((f / "hig/indice.json").read_text())
    hig_f = json.loads((f / "hig/fallos.json").read_text())
    web = json.loads((f / "web/indice.json").read_text())
    web_f = json.loads((f / "web/fallos.json").read_text())
    vids = [json.loads(p.read_text()) for p in sorted((f / "videos/json").glob("*.json"))]
    vid_f = json.loads((f / "videos/fallos.json").read_text())
    lista = json.loads((f / "videos/lista.json").read_text())

    sec = collections.Counter(e.get("seccion") or "raíz" for e in hig.values())
    con_t = [v for v in vids if v["transcripcion"]]
    sin_t = [v for v in vids if not v["transcripcion"]]
    por_origen = collections.Counter()
    for v in vids:
        o = v.get("origen") or []
        por_origen["videos/design" if "videos/design" in o else ("solo HIG" if all(x.startswith("hig:") for x in o) else "páginas de diseño / otros")] += 1
    por_evento = collections.Counter(v["evento"] for v in vids)
    fechas = sorted({e["descargado"][:10] for e in hig.values()} | {v["descargado"][:10] for v in vids})

    L = ["# Inventario de fuentes descargadas", "",
         f"Fechas de descarga: {', '.join(fechas)}", "",
         "## Human Interface Guidelines", "",
         f"- Páginas descargadas: **{len(hig) - 1}** + la raíz ({len(hig)} archivos JSON)."]
    for s, n in sorted(sec.items()):
        L.append(f"  - {s}: {n} (incluye la página índice de la sección)" if s != "raíz" else f"  - raíz: {n}")
    L.append(f"- Fallos: {len(hig_f)}")
    for x in hig_f:
        L.append(f"  - `{x['slug']}` — {x['error']} → {EXPLICACIONES.get(x['slug'], 'sin explicar')}")
    L += ["", "## Páginas web de diseño (no HIG)", "", f"- Descargadas: **{len(web)}**"]
    tipos = collections.Counter("historias/noticias (news, articles)" if ("news-" in k or "articles" in k) else "páginas de diseño, herramientas, premios y marcas" for k in web)
    for t, n in tipos.items():
        L.append(f"  - {t}: {n}")
    L.append(f"- Fallos: {len(web_f)}")
    for x in web_f:
        clave = next((k for k in EXPLICACIONES if k in x["url"]), None)
        L.append(f"  - {x['url']} — {x['error'][:80]} → {EXPLICACIONES.get(clave, 'sin explicar')}")
    L += ["", "## Vídeos", "",
          f"- En la lista oficial https://developer.apple.com/videos/design/: **{sum(1 for v in lista.values() if 'videos/design' in v.get('origen', []))}**",
          f"- Total procesados (lista + enlazados desde HIG y páginas de diseño): **{len(vids)}**"]
    for o, n in por_origen.items():
        L.append(f"  - {o}: {n}")
    L.append("- Por evento: " + ", ".join(f"{k} {n}" for k, n in sorted(por_evento.items(), reverse=True)))
    L += [f"- Con transcripción: **{len(con_t)}** · Sin transcripción: **{len(sin_t)}** → {EXPLICACIONES['sin_transcripcion']}"]
    for v in sin_t:
        L.append(f"  - {v['clave']} — {v['titulo']}")
    L += [f"- Fallos de descarga: {len(vid_f)}"]
    for x in vid_f:
        L.append(f"  - {x['clave']} — {x['error']}")
    L += ["", "## Design Resources", "",
          "- Inventario de kits y plantillas en `references/recursos-diseno.md` (no se descargan los .dmg).", "",
          "## Huecos conocidos que no dependen de la descarga", "",
          "- Las licencias completas de New York y de SF Symbols solo vienen dentro de los .dmg (no descargados por indicación). Se documenta lo que dicen la página /fonts/ (licencias de SF y SF Compact), la HIG de SF Symbols y las guías de marcas de developer.apple.com.",
          "- La página Layout (actualizada el 9-9-2026) ya no incluye las tablas de tamaños de pantalla por dispositivo; los valores de dispositivos antiguos que citen vídeos anteriores no se pueden verificar en la HIG vigente.",
          ""]
    txt = "\n".join(L)
    (f / "inventario.md").write_text(txt, encoding="utf-8")
    Path(a.skill, "references", "_inventario.md").write_text(txt, encoding="utf-8")
    print(txt)


if __name__ == "__main__":
    main()
