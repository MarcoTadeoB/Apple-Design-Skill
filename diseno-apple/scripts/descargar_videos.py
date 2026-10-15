#!/usr/bin/env python3
"""Descarga la lista de vídeos de diseño de Apple y, de cada vídeo, sus
metadatos, capítulos, recursos y transcripción con marcas de tiempo.

Fuentes de la lista:
  1. https://developer.apple.com/videos/design/
  2. vídeos enlazados desde las HIG (_fuentes/hig/indice.json, si existe)
  3. vídeos enlazados desde las páginas de diseño (_fuentes/web/*.html, si existen)
  4. --extra URL …

Uso:
    python3 descargar_videos.py --fuentes ./_fuentes [--solo-nuevos]

Genera (caché local, NO publicar):
    _fuentes/videos/lista.json
    _fuentes/videos/html/<evento>-<id>.html
    _fuentes/videos/json/<evento>-<id>.json
    _fuentes/videos/fallos.json
"""
import argparse
import html as H
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comun import BASE, descargar, guardar, hoy  # noqa: E402

RX_PLAY = re.compile(r"/videos/play/([a-z0-9-]+)/(\d+)")


def limpio(s: str) -> str:
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def parsear_lista(html: str) -> dict:
    vids = {}
    for m in re.finditer(r'<a href="(/videos/play/[^"]+)"[^>]*class="vc-card[^"]*"(.*?)</a>', html, re.S):
        href, cuerpo = m.group(1), m.group(2)
        k = RX_PLAY.search(href)
        if not k:
            continue
        clave = f"{k.group(1)}/{k.group(2)}"
        g = lambda rx: (re.search(rx, cuerpo, re.S) or [None, ""])[1]
        vids[clave] = {
            "clave": clave,
            "titulo": limpio(g(r'vc-card__title">(.*?)</h5>')),
            "duracion": limpio(g(r'vc-card__duration">(.*?)</span>')),
            "evento": limpio(g(r'vc-card__tag--event">(.*?)</span>')),
            "plataformas": g(r'data-filter-platform="([^"]*)"'),
            "temas": g(r'data-filter-topics="([^"]*)"'),
            "origen": ["videos/design"],
        }
    return vids


def parsear_video(html: str, clave: str) -> dict:
    g = lambda rx: (re.search(rx, html, re.S) or [None, ""])[1]
    evento, vid = clave.split("/")
    titulo_pag = limpio(g(r"<title>(.*?)</title>"))
    det = g(r'<li class="supplement details[^"]*"[^>]*>(.*?)<!-- transcript -->') or html
    capitulos = [
        {"inicio": int(float(s)), "titulo": limpio(t)}
        for s, t in re.findall(r'<li class="chapter-item" data-start-time="([\d.]+)">.*?<a[^>]*>(.*?)</a>', det, re.S)
    ]
    recursos = []
    bloque_rec = g(r"<h2>Resources</h2>(.*?)(?:<h2>|<!-- transcript -->)") or ""
    for u, t in re.findall(r'<a href="([^"]+)"[^>]*>(.*?)</a>', bloque_rec, re.S):
        if "devstreaming-cdn" in u:
            continue
        recursos.append({"titulo": limpio(t), "url": u if u.startswith("http") else BASE + u})
    relacionados = []
    bloque_rel = g(r"<h2>Related Videos</h2>(.*?)</li>\s*<!-- transcript -->") or g(r"<h2>Related Videos</h2>(.*)") [:20000]
    for u, t in re.findall(r'<a href="(/videos/play/[^"]+)"[^>]*>(.*?)</a>', bloque_rel, re.S):
        relacionados.append({"titulo": limpio(t), "url": BASE + u.rstrip("/") + "/"})
    trans_html = g(r'<section id="transcript-content">(.*?)</section>')
    transcripcion = [
        {"t": float(s), "texto": limpio(t)}
        for s, t in re.findall(r'data-start="([\d.]+)"[^>]*>(.*?)</span>', trans_html, re.S)
    ]
    transcripcion = [x for x in transcripcion if x["texto"]]
    m_ev = re.match(r"(.*?) - (.*?) - Videos - Apple Developer", titulo_pag)
    return {
        "clave": clave,
        "evento": evento,
        "id": vid,
        "url": f"{BASE}/videos/play/{clave}/",
        "titulo": limpio(g(r'<li class="supplement details[^"]*".*?<h1>(.*?)</h1>')) or (m_ev.group(1) if m_ev else titulo_pag),
        "evento_nombre": m_ev.group(2) if m_ev else evento,
        "fecha": g(r'itemprop="datePublished" content="([^"]+)"'),
        "descripcion": limpio(g(r'<li class="supplement details[^"]*".*?</h1>\s*</div>\s*<p>(.*?)</p>')),
        "capitulos": capitulos,
        "recursos": recursos,
        "relacionados": relacionados,
        "transcripcion": transcripcion,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fuentes", default="_fuentes")
    ap.add_argument("--solo-nuevos", action="store_true", help="no vuelve a bajar vídeos ya guardados")
    ap.add_argument("--extra", nargs="*", default=[])
    a = ap.parse_args()
    base = Path(a.fuentes)
    dv = base / "videos"
    lista_html = descargar(BASE + "/videos/design/").decode("utf-8", "replace")
    guardar(dv / "videos-design.html", lista_html)
    vids = parsear_lista(lista_html)
    print("Lista /videos/design/:", len(vids))

    def anadir(url, origen):
        k = RX_PLAY.search(url)
        if not k:
            return
        clave = f"{k.group(1)}/{k.group(2)}"
        v = vids.setdefault(clave, {"clave": clave, "origen": []})
        if origen not in v["origen"]:
            v["origen"].append(origen)

    ih = base / "hig" / "indice.json"
    if ih.exists():
        for slug, e in json.loads(ih.read_text()).items():
            for v in e.get("videos", []):
                anadir(v["url"], f"hig:{slug}")
    for f in sorted((base / "web").glob("*.html")) if (base / "web").exists() else []:
        for u in set(re.findall(r'/videos/play/[a-z0-9-]+/\d+', f.read_text(errors="replace"))):
            anadir(u, f"web:{f.stem}")
    for u in a.extra:
        anadir(u, "extra")

    fallos = []
    orden = sorted(vids, key=lambda c: (c.split("/")[0], int(c.split("/")[1])), reverse=True)
    for clave in orden:
        nombre = clave.replace("/", "-")
        dest = dv / "json" / f"{nombre}.json"
        if a.solo_nuevos and dest.exists():
            continue
        url = f"{BASE}/videos/play/{clave}/"
        try:
            html = descargar(url).decode("utf-8", "replace")
        except Exception as e:
            fallos.append({"clave": clave, "url": url, "error": str(e)})
            print("FALLO", clave, e, file=sys.stderr)
            continue
        guardar(dv / "html" / f"{nombre}.html", html)
        d = parsear_video(html, clave)
        d.update({k: vids[clave].get(k) for k in ("duracion", "plataformas", "temas", "origen")})
        d["descargado"] = hoy()
        guardar(dest, json.dumps(d, ensure_ascii=False, indent=1))
        print(f"OK {clave} [{len(d['transcripcion'])} frases] {d['titulo']}", flush=True)
    guardar(dv / "lista.json", json.dumps(vids, ensure_ascii=False, indent=1))
    guardar(dv / "fallos.json", json.dumps(fallos, ensure_ascii=False, indent=1))
    print(f"\nVídeos: {len(vids)}  Fallos: {len(fallos)}")


if __name__ == "__main__":
    main()
