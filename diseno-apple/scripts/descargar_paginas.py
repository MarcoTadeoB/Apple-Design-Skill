#!/usr/bin/env python3
"""Descarga las páginas web de la sección de diseño de Apple (no HIG) y las
convierte a texto Markdown aproximado (caché local, NO publicar).

Uso:
    python3 descargar_paginas.py --fuentes ./_fuentes [--extra URL ...]

Genera _fuentes/web/<nombre>.html, _fuentes/web/<nombre>.md y _fuentes/web/indice.json
"""
import argparse
import html as H
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comun import descargar, guardar, hoy  # noqa: E402

SEMILLAS = [
    "https://developer.apple.com/design/",
    "https://developer.apple.com/design/whats-new/",
    "https://developer.apple.com/design/get-started/",
    "https://developer.apple.com/design/resources/",
    "https://developer.apple.com/design/awards/",
    "https://developer.apple.com/fonts/",
    "https://developer.apple.com/sf-symbols/",
    "https://developer.apple.com/icon-composer/",
    "https://developer.apple.com/pass-designer/",
    "https://developer.apple.com/reality-composer-pro/",
    "https://developer.apple.com/licensing-trademarks/",
    "https://developer.apple.com/articles/capwords/",
    "https://developer.apple.com/app-store/marketing/guidelines/",
    "https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html",
    "https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html",
]
# enlaces que también se siguen (un nivel) desde las semillas
SEGUIR = [
    r"^https://developer\.apple\.com/design/awards/\d{4}/?$",
    r"^https://developer\.apple\.com/design/(?!human-interface-guidelines)[a-z0-9-]+/?$",
    r"^https://developer\.apple\.com/news/\?id=[a-z0-9]+$",
    r"^https://developer\.apple\.com/articles/[a-z0-9-]+/?$",
    r"^https://developer\.apple\.com/licensing-trademarks/[a-z0-9-]+/?$",
    r"^https://developer\.apple\.com/(fonts|sf-symbols|icon-composer)/[a-z0-9-]+/?$",
    r"^https://developer\.apple\.com/(support|terms)/.*(font|symbol|licen)[^#]*$",
]


def nombre_de(url: str) -> str:
    p = urlparse(url)
    s = (p.netloc.replace("developer.apple.com", "dev").replace("www.apple.com", "apple") + p.path).strip("/")
    if p.query:
        s += "-" + p.query
    return re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower() or "raiz"


class AMarkdown(HTMLParser):
    BLOQUE = {"p", "div", "section", "article", "ul", "ol", "table", "tr", "br", "header", "footer", "figure"}
    IGNORAR = {"script", "style", "noscript", "svg", "nav", "template", "head"}

    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base, self.out, self.ign, self.href, self.enlaces = base, [], 0, None, []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in self.IGNORAR:
            self.ign += 1
            return
        if self.ign:
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.out.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "li":
            self.out.append("\n- ")
        elif tag in ("td", "th"):
            self.out.append(" | ")
        elif tag in self.BLOQUE:
            self.out.append("\n")
        elif tag == "a" and a.get("href"):
            self.href = urljoin(self.base, a["href"])
            self.enlaces.append(self.href)
            self.out.append("[")
        elif tag == "img" and a.get("alt"):
            self.out.append(f"[imagen: {a['alt']}]")

    def handle_endtag(self, tag):
        if tag in self.IGNORAR:
            self.ign = max(0, self.ign - 1)
            return
        if self.ign:
            return
        if tag == "a" and self.href:
            self.out.append(f"]({self.href})")
            self.href = None
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6", "p"):
            self.out.append("\n")

    def handle_data(self, data):
        if not self.ign:
            self.out.append(re.sub(r"\s+", " ", data))

    def texto(self):
        t = "".join(self.out)
        t = re.sub(r"\[\s*\]\([^)]*\)", "", t)
        t = re.sub(r"[ \t]+\n", "\n", t)
        return re.sub(r"\n{3,}", "\n\n", t).strip() + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fuentes", default="_fuentes")
    ap.add_argument("--extra", nargs="*", default=[])
    ap.add_argument("--sin-seguir", action="store_true")
    ap.add_argument("--solo-extra", action="store_true", help="descarga solo las URL de --extra y añade al índice")
    a = ap.parse_args()
    dw = Path(a.fuentes) / "web"
    indice, fallos, vistos = {}, [], set()
    if a.solo_extra and (dw / "indice.json").exists():
        indice = json.loads((dw / "indice.json").read_text())
        vistos = {e["url"] for e in indice.values()}
        fallos = [f for f in json.loads((dw / "fallos.json").read_text()) if f["url"] not in a.extra]
    cola = [(u, 0) for u in (a.extra if a.solo_extra else SEMILLAS + a.extra)]
    while cola:
        url, nivel = cola.pop(0)
        if url in vistos:
            continue
        vistos.add(url)
        try:
            raw = descargar(url).decode("utf-8", "replace")
        except Exception as e:
            fallos.append({"url": url, "error": str(e)})
            print("FALLO", url, e, file=sys.stderr)
            continue
        n = nombre_de(url)
        guardar(dw / f"{n}.html", raw)
        p = AMarkdown(url)
        p.feed(raw)
        titulo = H.unescape((re.search(r"<title>(.*?)</title>", raw, re.S) or [None, ""])[1]).strip()
        fecha = hoy()
        guardar(dw / f"{n}.md", f"# {titulo}\n\n- Fuente: {url}\n- Descargado: {fecha}\n\n" + p.texto())
        indice[n] = {"url": url, "titulo": titulo, "descargado": fecha, "nivel": nivel}
        print("OK", n, titulo, flush=True)
        if nivel == 0 and not a.sin_seguir:
            for e in sorted(set(x.split("#")[0] for x in p.enlaces)):
                if any(re.match(rx, e) for rx in SEGUIR) and e not in vistos:
                    cola.append((e, 1))
    guardar(dw / "indice.json", json.dumps(indice, ensure_ascii=False, indent=1))
    guardar(dw / "fallos.json", json.dumps(fallos, ensure_ascii=False, indent=1))
    print(f"\nPáginas: {len(indice)}  Fallos: {len(fallos)}")


if __name__ == "__main__":
    main()
