"""Utilidades compartidas por los scripts de descarga de la skill diseno-apple.

- descargar(): 1 petición/segundo como máximo y hasta 3 reintentos.
- Renderizado del formato JSON de las HIG (DocC "RenderNode") a Markdown.
"""
from __future__ import annotations

import datetime as _dt
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE = "https://developer.apple.com"
HIG_DATA = BASE + "/tutorials/data/design/human-interface-guidelines"
UA = "Mozilla/5.0 (diseno-apple skill updater; +local cache)"

_ultimo = [0.0]


def hoy() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def descargar(url: str, intentos: int = 3, pausa: float = 1.0) -> bytes:
    """Descarga respetando 1 petición/segundo; reintenta hasta `intentos` veces."""
    ultimo_error = None
    for i in range(intentos):
        espera = pausa - (time.time() - _ultimo[0])
        if espera > 0:
            time.sleep(espera)
        _ultimo[0] = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            ultimo_error = e
            if e.code == 404:
                break  # no tiene sentido reintentar
        except Exception as e:  # red, timeout…
            ultimo_error = e
        time.sleep(2 ** i)
    raise RuntimeError(f"{url}: {ultimo_error}")


def guardar(ruta: Path, datos: bytes | str) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(datos, str):
        ruta.write_text(datos, encoding="utf-8")
    else:
        ruta.write_bytes(datos)


# ---------------------------------------------------------------------------
# Renderizado DocC JSON -> Markdown
# ---------------------------------------------------------------------------

class Render:
    def __init__(self, doc: dict):
        self.doc = doc
        self.refs = doc.get("references", {})
        self.videos: list[dict] = []  # vídeos enlazados desde la página
        self.enlaces_hig: set[str] = set()

    # -- referencias ------------------------------------------------------
    def url_ref(self, ident: str) -> tuple[str, str]:
        r = self.refs.get(ident, {})
        url = r.get("url") or ident
        if url.startswith("/"):
            url = BASE + url
        titulo = r.get("title") or ident
        if "/videos/play/" in url:
            self.videos.append({"titulo": titulo, "url": url})
        if "/design/human-interface-guidelines/" in url:
            self.enlaces_hig.add(url.split("#")[0].rstrip("/").rsplit("/", 1)[-1])
        return titulo, url

    def img(self, ident: str, meta: dict | None = None) -> str:
        r = self.refs.get(ident, {})
        alt = (r.get("alt") or "").strip()
        url = ""
        for v in r.get("variants", []):
            url = v.get("url", "")
            if url.startswith("/"):
                url = BASE + url
            if "2x" in v.get("traits", []):
                break
        cap = ""
        if meta and meta.get("abstract"):
            cap = self.inline(meta["abstract"])
        if ident in ("checkmark.png",):
            return "✅ (correcto)"
        if ident in ("crossout.png",):
            return "❌ (incorrecto)"
        txt = alt or cap or ident
        extra = f" — {cap}" if cap and cap != alt else ""
        return f"![{txt}]({url}){extra}"

    # -- inline -----------------------------------------------------------
    def inline(self, items) -> str:
        out = []
        for x in items or []:
            t = x.get("type")
            if t == "text":
                out.append(x.get("text", ""))
            elif t == "strong":
                out.append("**" + self.inline(x.get("inlineContent")) + "**")
            elif t == "emphasis":
                out.append("*" + self.inline(x.get("inlineContent")) + "*")
            elif t == "codeVoice":
                out.append("`" + x.get("code", "") + "`")
            elif t == "reference":
                titulo, url = self.url_ref(x.get("identifier", ""))
                out.append(f"[{x.get('overridingTitle') or titulo}]({url})")
            elif t == "link":
                url = x.get("destination", "")
                out.append(f"[{x.get('title') or url}]({url})")
            elif t == "image":
                out.append(self.img(x.get("identifier", ""), x.get("metadata")))
            elif t in ("newTerm", "inlineHead", "superscript", "subscript", "strikethrough"):
                out.append(self.inline(x.get("inlineContent")))
            else:
                if "inlineContent" in x:
                    out.append(self.inline(x["inlineContent"]))
                elif "text" in x:
                    out.append(x["text"])
        return "".join(out)

    # -- bloques ----------------------------------------------------------
    def bloques(self, items, nivel_lista: int = 0) -> list[str]:
        out: list[str] = []
        for b in items or []:
            out.extend(self.bloque(b, nivel_lista))
        return out

    def celda(self, contenido) -> str:
        return " ".join(l.strip() for l in self.bloques(contenido) if l.strip()).replace("|", "\\|")

    def bloque(self, b: dict, nl: int = 0) -> list[str]:
        t = b.get("type")
        if t == "heading":
            return ["", "#" * min(6, b.get("level", 2)) + " " + b.get("text", ""), ""]
        if t == "paragraph":
            return [self.inline(b.get("inlineContent")), ""]
        if t in ("unorderedList", "orderedList"):
            out = []
            for i, it in enumerate(b.get("items", []), 1):
                partes = [l for l in self.bloques(it.get("content"), nl + 1)]
                partes = [p for p in partes if p.strip()]
                marca = "-" if t == "unorderedList" else f"{i}."
                if partes:
                    out.append("  " * nl + f"{marca} {partes[0].strip()}")
                    out.extend("  " * (nl + 1) + p.strip() for p in partes[1:])
            out.append("")
            return out
        if t == "aside":
            nombre = b.get("name") or b.get("style", "Note").capitalize()
            cuerpo = [l for l in self.bloques(b.get("content")) if l.strip()]
            return [f"> **{nombre}:** " + " ".join(cuerpo), ""]
        if t == "table":
            filas = b.get("rows", [])
            if not filas:
                return []
            celdas = [[self.celda(c) for c in f] for f in filas]
            n = max(len(f) for f in celdas)
            celdas = [f + [""] * (n - len(f)) for f in celdas]
            out = ["| " + " | ".join(celdas[0]) + " |", "|" + "---|" * n]
            out += ["| " + " | ".join(f) + " |" for f in celdas[1:]]
            return out + [""]
        if t == "row":
            cols = [[l for l in self.bloques(c.get("content")) if l.strip()] for c in b.get("columns", [])]
            planas = [l for c in cols for l in c]
            if any(l.lstrip().startswith(("|", "#", "**[Pesta")) for l in planas):
                out = []
                for c in cols:
                    out += c + [""]
                return out
            planas = [re.sub(r"^\s*-\s+", "", l) for l in planas]
            return ["- " + " · ".join(planas), ""] if planas else []
        if t == "tabNavigator":
            out = []
            for tab in b.get("tabs", []):
                out += ["", f"**[Pestaña: {tab.get('title')}]**", ""]
                out += self.bloques(tab.get("content"))
            return out
        if t == "links":
            out = []
            for ident in b.get("items", []):
                titulo, url = self.url_ref(ident)
                out.append(f"- [{titulo}]({url})")
            return out + [""]
        if t == "codeListing":
            return ["```" + (b.get("syntax") or ""), *b.get("code", []), "```", ""]
        if t == "termList":
            out = []
            for it in b.get("items", []):
                term = self.inline(it.get("term", {}).get("inlineContent"))
                defi = " ".join(l for l in self.bloques(it.get("definition", {}).get("content")) if l.strip())
                out.append(f"- **{term}:** {defi}")
            return out + [""]
        if t == "small":
            return [self.inline(b.get("inlineContent")), ""]
        if t in ("video",):
            return [f"[vídeo: {b.get('identifier')}]", ""]
        if "content" in b:
            return self.bloques(b["content"])
        if "inlineContent" in b:
            return [self.inline(b["inlineContent"]), ""]
        return [f"<!-- bloque no reconocido: {t} -->"]

    # -- página -----------------------------------------------------------
    def pagina(self, url: str, fecha: str) -> str:
        d = self.doc
        meta = d.get("metadata", {})
        titulo = meta.get("title", "")
        cm = meta.get("customMetadata", {})
        lineas = [f"# {titulo}", "",
                  f"- Fuente: {url}",
                  f"- Descargado: {fecha}"]
        if cm.get("supported-platforms"):
            lineas.append(f"- Plataformas: {cm['supported-platforms']}")
        if cm.get("alert-date"):
            lineas.append(f"- Aviso de la página: {cm.get('alert-date')} — {cm.get('alert-text','')}")
        lineas.append("")
        if d.get("abstract"):
            lineas += ["> " + self.inline(d["abstract"]), ""]
        for s in d.get("primaryContentSections", []):
            lineas += self.bloques(s.get("content"))
        for ts in d.get("topicSections", []) or []:
            lineas += ["", f"## {ts.get('title') or 'Temas'}", ""]
            for ident in ts.get("identifiers", []):
                t, u = self.url_ref(ident)
                lineas.append(f"- [{t}]({u})")
        txt = "\n".join(lineas)
        return re.sub(r"\n{3,}", "\n\n", txt).strip() + "\n"


def changelog(doc: dict) -> list[tuple[str, str]]:
    """Devuelve [(fecha, cambio)] de la tabla «Change log» de una página HIG."""
    r = Render(doc)
    cont = []
    for s in doc.get("primaryContentSections", []):
        cont += s.get("content", [])
    res = []
    dentro = False
    for b in cont:
        if b.get("type") == "heading":
            dentro = b.get("text", "").lower().startswith("change log")
            continue
        if dentro and b.get("type") == "table":
            for fila in b.get("rows", [])[1:]:
                if len(fila) >= 2:
                    res.append((r.celda(fila[0]), r.celda(fila[1])))
    return res


def fecha_iso(f: str) -> str:
    try:
        return _dt.datetime.strptime(f.strip(), "%B %d, %Y").strftime("%Y-%m-%d")
    except ValueError:
        return f.strip()
