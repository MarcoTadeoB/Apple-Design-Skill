#!/usr/bin/env python3
"""Descarga recursivamente las Human Interface Guidelines en su formato JSON
y las convierte a Markdown completo (caché local, NO publicar).

Uso:
    python3 descargar_hig.py --fuentes ./_fuentes

Genera:
    _fuentes/hig/json/<slug>.json   JSON original
    _fuentes/hig/md/<slug>.md       Markdown completo con URL y fecha
    _fuentes/hig/indice.json        slug, título, sección, grupo, URL, fecha, changelog, vídeos
    _fuentes/hig/fallos.json        URLs que no se pudieron descargar
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comun import HIG_DATA, BASE, Render, changelog, descargar, guardar, hoy  # noqa: E402

SECCIONES = ["getting-started", "foundations", "patterns", "components", "inputs", "technologies"]


def slug_de(ident_o_url: str) -> str:
    return ident_o_url.split("#")[0].rstrip("/").rsplit("/", 1)[-1].lower()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fuentes", default="_fuentes")
    ap.add_argument("--solo", nargs="*", help="slugs concretos (para pruebas)")
    ap.add_argument("--rerender", action="store_true",
                    help="no descarga: regenera los .md desde los JSON ya guardados")
    a = ap.parse_args()
    base = Path(a.fuentes) / "hig"
    indice: dict[str, dict] = {}
    fallos = []

    def bajar(slug: str):
        url_json = HIG_DATA + ".json" if slug == "_raiz" else f"{HIG_DATA}/{slug}.json"
        url_web = BASE + "/design/human-interface-guidelines" + ("" if slug == "_raiz" else f"/{slug}")
        try:
            datos = descargar(url_json)
        except Exception as e:
            fallos.append({"slug": slug, "url": url_json, "error": str(e)})
            print("FALLO", slug, e, file=sys.stderr)
            return None
        guardar(base / "json" / f"{slug}.json", datos)
        doc = json.loads(datos)
        fecha = hoy()
        r = Render(doc)
        md = r.pagina(url_web, fecha)
        guardar(base / "md" / f"{slug}.md", md)
        meta = doc.get("metadata", {})
        indice[slug] = {
            "slug": slug, "titulo": meta.get("title"), "rol": meta.get("role"),
            "url": url_web, "url_json": url_json, "descargado": fecha,
            "plataformas": meta.get("customMetadata", {}).get("supported-platforms"),
            "aviso": [meta.get("customMetadata", {}).get("alert-date"), meta.get("customMetadata", {}).get("alert-text")],
            "changelog": changelog(doc),
            "videos": r.videos,
            "enlaces_hig": sorted(r.enlaces_hig),
        }
        print("OK", slug, meta.get("title"), flush=True)
        return doc

    if a.rerender:
        indice = json.loads((base / "indice.json").read_text())
        for slug, e in indice.items():
            doc = json.loads((base / "json" / f"{slug}.json").read_text())
            guardar(base / "md" / f"{slug}.md", Render(doc).pagina(e["url"], e["descargado"]))
        print("Regenerados", len(indice))
        return
    if a.solo:
        for s in a.solo:
            bajar(s)
    else:
        raiz = bajar("_raiz")
        cola = []  # (slug, seccion, grupo)
        vistos = {"_raiz"}
        for s in SECCIONES:
            cola.append((s, s, None))
        # recorrido del árbol de temas
        while cola:
            slug, seccion, grupo = cola.pop(0)
            if slug in vistos:
                continue
            vistos.add(slug)
            doc = bajar(slug)
            if doc is None:
                continue
            indice[slug].update({"seccion": seccion, "grupo": grupo, "en_arbol": True})
            for ts in doc.get("topicSections", []) or []:
                for ident in ts.get("identifiers", []):
                    ref = doc.get("references", {}).get(ident, {})
                    url = ref.get("url", "")
                    if url.startswith("/design/human-interface-guidelines/"):
                        hijo = slug_de(url)
                        if hijo not in vistos:
                            cola.append((hijo, seccion, ts.get("title") or grupo))
        # páginas HIG enlazadas pero fuera del árbol
        pendientes = set()
        for e in list(indice.values()):
            pendientes |= set(e.get("enlaces_hig", []))
        while pendientes - vistos:
            slug = sorted(pendientes - vistos)[0]
            vistos.add(slug)
            doc = bajar(slug)
            if doc is not None:
                indice[slug].update({"seccion": "_fuera-del-arbol", "grupo": None, "en_arbol": False})
                pendientes |= set(indice[slug]["enlaces_hig"])
    guardar(base / "indice.json", json.dumps(indice, ensure_ascii=False, indent=1))
    guardar(base / "fallos.json", json.dumps(fallos, ensure_ascii=False, indent=1))
    print(f"\nPáginas: {len(indice)}  Fallos: {len(fallos)}")


if __name__ == "__main__":
    main()
