#!/usr/bin/env python3
"""Genera las referencias condensadas de la skill a partir de la caché `_fuentes/`.

Las referencias guardan SOLO resúmenes, valores exactos, tablas de especificaciones
y citas cortas (con URL y fecha). El texto completo y las transcripciones se
quedan en `_fuentes/` (caché local, no publicar).

Uso:
    python3 generar_referencias.py --fuentes ./_fuentes --skill ./diseno-apple [hig videos componentes novedades]
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comun import BASE, Render, fecha_iso, guardar  # noqa: E402

RX_VALOR = re.compile(
    r"(\b\d+(?:[.,]\d+)?\s?(?:pt|px|points?|pixels?|%|ms|milliseconds?|seconds?|mm|inch(?:es)?|x\b|×|:1|fps|Hz|degrees|°|meters?|cm|characters|words|lines|percent)\b"
    r"|R-\d+,G-\d+,B-\d+|#[0-9A-Fa-f]{6}\b"
    r"|\b(?:at least|minimum|maximum|no more than|no larger than|no smaller than|up to)\b[^.]*\d)",
    re.I,
)
RX_MATIZ = re.compile(r"\b(exception|except|unless)\b", re.I)
RX_FRASE = re.compile(r"(?<=[.!?])\s+(?=[A-Z“\"(*])")
MAX_CITA = 240


def frases(t: str) -> list[str]:
    return [f.strip() for f in RX_FRASE.split(t.strip()) if f.strip()]


def corta(t: str, n: int = MAX_CITA) -> str:
    t = re.sub(r"\s+", " ", t).strip()
    return t if len(t) <= n else t[: n - 1].rsplit(" ", 1)[0] + "…"


def sin_imagenes(t: str) -> str:
    return re.sub(r"!\[[^\]]*\]\([^)]*\)( — [^·]*)?", "", t).strip(" ·")


def alt_con_valores(t: str) -> list[str]:
    return [a for a in re.findall(r"!\[([^\]]*)\]", t) if RX_VALOR.search(a)]


# ---------------------------------------------------------------------------
# HIG
# ---------------------------------------------------------------------------

class Digest:
    """Condensa una página HIG: reglas (frases en negrita), valores, tablas."""

    def __init__(self, doc: dict):
        self.doc = doc
        self.r = Render(doc)
        self.out: list[str] = []
        self.recursos: list[str] = []
        self.changelog: list[str] = []
        self.zona = "cuerpo"

    def valores(self, texto: str, excluir: str = "") -> list[str]:
        return [corta(f) for f in frases(texto) if RX_VALOR.search(f) and f.strip() not in excluir]

    def parrafo(self, b: dict, prefijo: str = "") -> None:
        ic = b.get("inlineContent") or []
        txt = self.r.inline(ic)
        if not txt.strip():
            return
        alts = alt_con_valores(txt)
        limpio = sin_imagenes(txt)
        if not limpio:
            for a in alts:
                self.out.append(f"{prefijo}- (imagen) {a}")
            return
        if ic and ic[0].get("type") == "strong":
            regla = self.r.inline(ic[0].get("inlineContent")).strip()
            resto = limpio[len(regla) + 4:] if limpio.startswith("**") else limpio
            fs = frases(resto)
            self.out.append(f"{prefijo}- **{regla}**")
            for v in [corta(f) for f in fs if RX_VALOR.search(f) or RX_MATIZ.search(f)]:
                self.out.append(f"{prefijo}  - «{v}»")
        else:
            fs = frases(limpio)
            prim = corta(fs[0], 180) if fs else ""
            if prim:
                self.out.append(f"{prefijo}- {prim}")
            for v in self.valores(" ".join(fs[1:])):
                self.out.append(f"{prefijo}  - «{v}»")
        for a in alts:
            self.out.append(f"{prefijo}  - (imagen) {a}")

    def bloque(self, b: dict, prefijo: str = "") -> None:
        t = b.get("type")
        if t == "heading":
            texto = b.get("text", "")
            if b.get("level", 2) == 2:
                low = texto.lower()
                self.zona = "recursos" if low == "resources" else "changelog" if low.startswith("change log") else "cuerpo"
            if self.zona == "cuerpo":
                self.out += ["", "#" * min(6, b.get("level", 2) + 1) + " " + texto, ""]
            elif self.zona == "recursos" and b.get("level", 2) > 2:
                self.recursos.append(f"- *{texto}:*")
            return
        if self.zona == "changelog":
            if t == "table":
                self.changelog += self.r.bloque(b)
            return
        if self.zona == "recursos":
            if t == "paragraph":
                l = sin_imagenes(self.r.inline(b.get("inlineContent")))
                if l:
                    self.recursos.append(f"  - {l}")
            elif t in ("unorderedList", "links"):
                for l in self.r.bloque(b):
                    if l.strip():
                        self.recursos.append("  " + l.strip())
            return
        if t == "paragraph":
            self.parrafo(b, prefijo)
        elif t in ("unorderedList", "orderedList"):
            for it in b.get("items", []):
                lineas = [l for l in self.r.bloques(it.get("content")) if l.strip()]
                if not lineas:
                    continue
                txt = sin_imagenes(" ".join(lineas))
                if txt:
                    fs = frases(txt)
                    # en listas cortas se conserva el elemento entero si es breve
                    self.out.append(f"{prefijo}  - {corta(txt if len(txt) <= 180 else fs[0], 180)}")
        elif t == "aside":
            cuerpo = " ".join(l for l in self.r.bloques(b.get("content")) if l.strip())
            fs = frases(sin_imagenes(cuerpo))
            if fs:
                nombre = b.get("name") or b.get("style", "note").capitalize()
                self.out.append(f"{prefijo}> **{nombre}:** {corta(fs[0])}")
                for v in self.valores(" ".join(fs[1:])):
                    self.out.append(f"{prefijo}>   «{v}»")
        elif t == "table":
            self.out.append("")
            self.out += self.r.bloque(b)
        elif t == "row":
            for col in b.get("columns", []):
                txt = " ".join(self.r.bloques(col.get("content")))
                if "✅" in txt or "❌" in txt:
                    cap = re.findall(r"!\[([^\]]*)\]\([^)]*\)(?: — ([^·✅❌]*))?", txt)
                    desc = (cap[0][1].strip() or cap[0][0]) if cap else ""
                    marca = "✅ Ejemplo correcto" if "✅" in txt else "❌ Ejemplo incorrecto"
                    self.out.append(f"{prefijo}  - {marca}: {corta(desc, 200)}")
                    continue
                for x in col.get("content", []):
                    self.bloque(x, prefijo)
        elif t == "tabNavigator":
            for tab in b.get("tabs", []):
                antes = len(self.out)
                self.out += ["", f"**Pestaña «{tab.get('title')}»**", ""]
                for x in tab.get("content", []):
                    self.bloque(x, prefijo)
                if not any(l.strip() for l in self.out[antes + 3:]):
                    del self.out[antes:]
        elif t == "termList":
            for it in b.get("items", []):
                term = self.r.inline(it.get("term", {}).get("inlineContent"))
                defi = " ".join(l for l in self.r.bloques(it.get("definition", {}).get("content")) if l.strip())
                fs = frases(sin_imagenes(defi))
                self.out.append(f"{prefijo}- **{term}:** {corta(fs[0]) if fs else ''}")
        elif t == "links":
            return
        elif "content" in b:
            for x in b["content"]:
                self.bloque(x, prefijo)

    def generar(self) -> str:
        for s in self.doc.get("primaryContentSections", []):
            for b in s.get("content", []):
                self.bloque(b)
        txt = "\n".join(self.out)
        return re.sub(r"\n{3,}", "\n\n", txt).strip()


def mapa_secciones(base: Path, indice: dict) -> dict:
    """slug -> (sección, grupo) usando las páginas de grupo de Components, etc."""
    padres = {}
    for slug, e in indice.items():
        doc = json.loads((base / "json" / f"{slug}.json").read_text())
        for ts in doc.get("topicSections", []) or []:
            for ident in ts.get("identifiers", []):
                u = doc["references"].get(ident, {}).get("url", "")
                if u.startswith("/design/human-interface-guidelines/"):
                    h = u.rstrip("/").rsplit("/", 1)[-1].lower()
                    padres.setdefault(h, slug)
    return padres


def nombre_video(url: str, fechas: dict) -> str | None:
    m = re.search(r"/videos/play/([a-z0-9-]+)/(\d+)", url)
    if not m:
        return None
    ev, vid = m.groups()
    if ev.startswith("wwdc"):
        return f"{ev[4:]}-{vid}"
    anio = (fechas.get(f"{ev}/{vid}", "") or "")[:4] or "s-f"
    return f"{anio}-{ev}-{vid}"


def cargar_fechas_videos(fuentes: Path) -> dict:
    res = {}
    for f in (fuentes / "videos" / "json").glob("*.json"):
        d = json.loads(f.read_text())
        res[d["clave"]] = d.get("fecha", "")
    return res


def generar_hig(fuentes: Path, skill: Path) -> dict:
    base = fuentes / "hig"
    indice = json.loads((base / "indice.json").read_text())
    padres = mapa_secciones(base, indice)
    fechas_v = cargar_fechas_videos(fuentes)
    destino = skill / "references" / "hig"
    filas = collections.defaultdict(list)
    rutas = {}
    for slug, e in sorted(indice.items()):
        if slug == "_raiz":
            continue
        seccion = e.get("seccion") or "otros"
        grupo = padres.get(slug)
        grupo_tit = indice.get(grupo, {}).get("titulo") if grupo and grupo != seccion else None
        doc = json.loads((base / "json" / f"{slug}.json").read_text())
        d = Digest(doc)
        cuerpo = d.generar()
        cl = e.get("changelog") or []
        ultima = f"{fecha_iso(cl[0][0])} — {cl[0][1]}" if cl else "sin registro de cambios"
        abstract = Render(doc).inline(doc.get("abstract"))
        rel = f"{seccion}/{slug}.md"
        rutas[slug] = rel
        cab = [
            f"# {e['titulo']} — HIG (condensado)",
            "",
            f"- URL: {e['url']}",
            f"- Descargado: {e['descargado'][:10]}",
            f"- Sección: {seccion}" + (f" › {grupo_tit}" if grupo_tit else ""),
            f"- Plataformas: {e.get('plataformas') or 'n/d'}",
            f"- Última actualización: {ultima}",
            "",
            "> Resumen de Apple: " + abstract if abstract else "",
            "",
            "_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);",
            "«…» son frases literales con valores numéricos; las tablas son las especificaciones",
            "originales. Para el texto completo, abre la URL._",
            "",
        ]
        vids = []
        for v in e.get("videos", []):
            n = nombre_video(v["url"], fechas_v)
            linea = f"- [{v['titulo']}]({v['url']})" + (f" → `references/videos/{n}.md`" if n else "")
            if linea not in vids:
                vids.append(linea)
        pie = []
        d.recursos = [l for i, l in enumerate(d.recursos)
                      if not (l.startswith("- *") and (i + 1 == len(d.recursos) or d.recursos[i + 1].startswith("- *")
                              or "/videos/play/" in d.recursos[i + 1]))]
        if d.recursos:
            pie += ["", "## Recursos relacionados", ""] + [l for l in d.recursos if "/videos/play/" not in l]
        if vids:
            pie += ["", "## Vídeos que la explican", ""] + vids
        if d.changelog:
            pie += ["", "## Registro de cambios", ""] + d.changelog
        guardar(destino / rel, "\n".join(cab) + cuerpo + "\n" + "\n".join(pie).rstrip() + "\n")
        filas[seccion].append((grupo_tit or "", e["titulo"], rel, fecha_iso(cl[0][0]) if cl else "", e.get("plataformas") or "", abstract))
    # índice general
    orden = ["getting-started", "foundations", "patterns", "components", "inputs", "technologies"]
    lineas = ["# Índice de las HIG (páginas condensadas)", "",
              f"Total: {sum(len(v) for v in filas.values())} páginas. Fuente: {BASE}/design/human-interface-guidelines",
              "Columnas: página → archivo · última actualización · plataformas · resumen de Apple.", ""]
    for s in orden + sorted(set(filas) - set(orden)):
        if s not in filas:
            continue
        lineas += ["", f"## {s}", ""]
        for g, t, rel, f, p, ab in sorted(filas[s]):
            pref = f"{g} › " if g else ""
            lineas.append(f"- {pref}**{t}** → `hig/{rel}` · {f or '—'} · {p.replace(',', ' ') or '—'} · {corta(ab, 160)}")
    guardar(destino / "_indice.md", "\n".join(lineas) + "\n")
    guardar(fuentes / "rutas_hig.json", json.dumps(rutas, indent=1))
    print("HIG condensadas:", len(rutas))
    return rutas


# ---------------------------------------------------------------------------
# Vídeos
# ---------------------------------------------------------------------------

RX_REGLA = re.compile(
    r"\b(should(?:n't)?|avoid|don't|do not|never|always|make sure|recommend|prefer|best practice|instead of|"
    r"keep in mind|it's important|important to|consider|remember|try to|aim for|be sure)\b", re.I)


def mmss(s: float) -> str:
    s = int(s)
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}" if s >= 3600 else f"{s // 60}:{s % 60:02d}"


def frases_transcripcion(tr: list[dict]) -> list[tuple[float, str]]:
    res, buf, ini = [], [], None
    for x in tr:
        if ini is None:
            ini = x["t"]
        buf.append(x["texto"])
        if re.search(r"[.!?][”\"']?$", x["texto"]):
            res.append((ini, " ".join(buf)))
            buf, ini = [], None
    if buf:
        res.append((ini, " ".join(buf)))
    return res


def citas_video(d: dict, maximo: int = 24) -> list[tuple[float, str, str]]:
    fr = frases_transcripcion(d.get("transcripcion", []))
    caps = d.get("capitulos") or [{"inicio": 0, "titulo": ""}]
    def cap_de(t):
        c = caps[0]["titulo"]
        for k in caps:
            if t >= k["inicio"]:
                c = k["titulo"]
        return c
    cand = []
    for t, f in fr:
        if len(f) < 40:
            continue
        p = 0
        if RX_REGLA.search(f):
            p += 2
        if RX_VALOR.search(f):
            p += 2
        if p:
            cand.append((p, t, corta(f, 260), cap_de(t)))
    por_cap = collections.defaultdict(list)
    for c in cand:
        por_cap[c[3]].append(c)
    cupo = max(2, maximo // max(1, len(por_cap)))
    elegidas = []
    for cap, lista in por_cap.items():
        lista.sort(key=lambda c: (-c[0], c[1]))
        elegidas += lista[:cupo]
    elegidas.sort(key=lambda c: c[1])
    return [(c[1], c[2], c[3]) for c in elegidas[:maximo]]


AVISOS: list[str] = []


def _norm(t: str) -> str:
    return re.sub(r"[^a-z0-9]", "", t.lower().replace("’", "'"))


def localizar(tr: list[dict], ancla: str):
    """Devuelve (segundo, frase literal) donde empieza `ancla` en la transcripción."""
    obj = _norm(ancla)
    for i in range(len(tr)):
        ventana = "".join(_norm(x["texto"]) for x in tr[i:i + 8])
        pos = ventana.find(obj)
        if pos != -1 and pos < len(_norm(tr[i]["texto"])):
            # frase completa a partir del fragmento i
            for t0, f in frases_transcripcion(tr[i:]):
                return tr[i]["t"], corta(f, 200)
    return None, None


def generar_videos(fuentes: Path, skill: Path, rutas_hig: dict) -> None:
    dv = fuentes / "videos" / "json"
    indice_hig = json.loads((fuentes / "hig" / "indice.json").read_text())
    enlazado = collections.defaultdict(list)
    for slug, e in indice_hig.items():
        for v in e.get("videos", []):
            m = re.search(r"/videos/play/([a-z0-9-]+)/(\d+)", v["url"])
            if m and slug in rutas_hig:
                enlazado[f"{m.group(1)}/{m.group(2)}"].append(slug)
    manual_p = skill / "scripts" / "resumenes_videos.json"
    manual = json.loads(manual_p.read_text()) if manual_p.exists() else {}
    fechas = cargar_fechas_videos(fuentes)
    filas = []
    destino = skill / "references" / "videos"
    for f in sorted(dv.glob("*.json")):
        d = json.loads(f.read_text())
        nombre = nombre_video(d["url"], fechas)
        url = d["url"]
        tr = d.get("transcripcion", [])
        dur = d.get("duracion") or (mmss(tr[-1]["t"]) + " (aprox., última frase)" if tr else "n/d")
        L = [f"# {d['titulo']} — {d.get('evento_nombre') or d['evento']}", "",
             f"- URL: {url}",
             f"- Evento: {d.get('evento_nombre') or d['evento']} · Publicado: {d.get('fecha') or 'n/d'} · Duración: {dur}",
             f"- Descargado: {d.get('descargado', '')[:10]} · Transcripción: {'sí, ' + str(len(tr)) + ' fragmentos' if tr else 'NO disponible'}",
             f"- Temas: {d.get('temas') or 'n/d'} · Plataformas: {d.get('plataformas') or 'n/d'}",
             f"- Origen en la lista: {', '.join(d.get('origen') or [])}", ""]
        if d.get("descripcion"):
            L += [f"> Descripción de Apple: {d['descripcion']}", ""]
        m = manual.get(d["clave"])
        if m:
            L += ["## Resumen (redactado a partir de la transcripción)", "", m.get("resumen", ""), ""]
            if m.get("reglas"):
                L += ["## Reglas prácticas", "", "_Cada regla enlaza el momento exacto del vídeo y cita la frase literal que la respalda._", ""]
                for r in m["reglas"]:
                    t, cita = localizar(tr, r["ancla"])
                    if t is None:
                        AVISOS.append(f"{d['clave']}: ancla no encontrada «{r['ancla']}»")
                        L.append(f"- {r['texto']} — ⚠️ cita sin verificar")
                    else:
                        L.append(f"- {r['texto']} — [{mmss(t)}]({url}?time={int(t)}) «{cita}»")
                L.append("")
        if d.get("capitulos"):
            L += ["## Capítulos", ""] + [f"- [{mmss(c['inicio'])}]({url}?time={c['inicio']}) {c['titulo']}" for c in d["capitulos"]] + [""]
        if tr:
            cit = citas_video(d)
            if cit:
                L += ["## Citas clave (literales, con marca de tiempo)", "",
                      "_Selección automática de frases con recomendaciones o valores; verifica el contexto en el vídeo._", ""]
                cap_ant = None
                for t, txt, cap in cit:
                    if cap != cap_ant and cap:
                        L.append(f"- *{cap}*")
                        cap_ant = cap
                    L.append(f"  - [{mmss(t)}]({url}?time={int(t)}) «{txt}»")
                L.append("")
        hig = enlazado.get(d["clave"], [])
        if hig:
            L += ["## Páginas de las HIG que enlazan este vídeo", ""] + [f"- `references/hig/{rutas_hig[s]}`" for s in sorted(set(hig))] + [""]
        if d.get("recursos"):
            L += ["## Recursos enlazados", ""] + [f"- [{r['titulo']}]({r['url']})" for r in d["recursos"]] + [""]
        if d.get("relacionados"):
            L += ["## Vídeos relacionados", ""] + [f"- [{r['titulo']}]({r['url']})" + (f" → `{nombre_video(r['url'], fechas)}.md`" if nombre_video(r['url'], fechas) else "") for r in d["relacionados"]] + [""]
        guardar(destino / f"{nombre}.md", "\n".join(L))
        filas.append((d.get("fecha") or "", nombre, d["titulo"], d.get("evento_nombre") or d["evento"], dur, bool(tr), "videos/design" in (d.get("origen") or []), sorted(set(hig))))
    filas.sort(reverse=True)
    L = ["# Índice de vídeos de diseño", "",
         f"Total: {len(filas)} vídeos ({sum(1 for f in filas if f[5])} con transcripción). Ordenados del más reciente al más antiguo.",
         "D = aparece en developer.apple.com/videos/design/; si no, está enlazado desde las HIG o desde las páginas de diseño.", "",
         "| Fecha | Archivo | Título | Evento | Duración | Transcr. | D | HIG que lo enlazan |", "|---|---|---|---|---|---|---|---|"]
    for fe, n, t, ev, du, tr, de, hig in filas:
        L.append(f"| {fe} | `videos/{n}.md` | {t.replace('|', '/')} | {ev} | {du} | {'sí' if tr else 'no'} | {'D' if de else ''} | {', '.join(hig[:6])}{'…' if len(hig) > 6 else ''} |")
    guardar(destino / "_indice.md", "\n".join(L) + "\n")
    print("Vídeos condensados:", len(filas))
    for a_ in AVISOS:
        print("⚠️", a_)


# ---------------------------------------------------------------------------



# ---------------------------------------------------------------------------
# Plantillas con tablas extraídas (tokens.md)
# ---------------------------------------------------------------------------

def rgb_legible(celda: str) -> str:
    def rep(m):
        r, g, b = (int(x) for x in m.groups())
        return f"{r},{g},{b} · #{r:02X}{g:02X}{b:02X}"
    celda = re.sub(r"!\[R-(\d+),G-(\d+),B-(\d+)\]\([^)]*\)", rep, celda)
    celda = re.sub(r"!\[A checkmark denoting availability\.\]\([^)]*\)", "✓", celda)
    return re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", celda)


def extraer_tablas(md: str, tras: str, seccion: str | None, contiene: str | None, n: int, cruzar: bool = False) -> list[str]:
    lineas = md.splitlines()
    i = 0
    if seccion:
        i = next((k for k, l in enumerate(lineas) if re.match(r"#+ " + re.escape(seccion) + r"\s*$", l)), None)
        if i is None:
            return [f"> ⚠️ No se encontró la sección «{seccion}»"]
    k = next((k for k in range(i, len(lineas)) if re.match(r"#+ " + re.escape(tras) + r"\s*$", lineas[k])), None)
    if k is None:
        return [f"> ⚠️ No se encontró el encabezado «{tras}»"]
    nivel = len(lineas[k]) - len(lineas[k].lstrip("#"))
    tablas, actual, actual_titulo = [], [], ""
    for l in lineas[k + 1:]:
        m = re.match(r"(#+) ", l)
        if m and (len(m.group(1)) < nivel or (len(m.group(1)) == nivel and not cruzar)):
            break
        if m and cruzar:
            actual_titulo = l.lstrip("# ").strip()
            continue
        if l.startswith("|"):
            if not actual and cruzar and actual_titulo:
                actual.append(f"**{actual_titulo}**")
                actual.append("")
            actual.append(rgb_legible(l))
        elif actual:
            if not contiene or contiene in "".join(actual[:3]):
                tablas.append(actual)
            actual = []
            if len(tablas) >= n:
                break
    if actual and len(tablas) < n and (not contiene or contiene in actual[0]):
        tablas.append(actual)
    out = []
    for t in tablas[:n]:
        out += t + [""]
    return out or [f"> ⚠️ Sin tablas tras «{tras}»"]


# ---------------------------------------------------------------------------
# CSS generado desde las tablas (para web.md)
# ---------------------------------------------------------------------------

def _tabla(md: str, tras: str, seccion: str | None = None) -> list[list[str]]:
    filas = [l for l in extraer_tablas(md, tras, seccion, None, 1) if l.startswith("|")]
    return [[c.strip() for c in l.strip("|").split("|")] for l in filas[2:]]


def css_colores(fuentes: Path) -> str:
    md = (fuentes / "hig" / "md" / "color.md").read_text(encoding="utf-8")
    sis = _tabla(md, "System colors", "Specifications")
    gris = _tabla(md, "iOS, iPadOS system gray colors")
    def hexs(c):
        m = re.search(r"#([0-9A-F]{6})", c)
        return "#" + m.group(1) if m else "?"
    modos = {"claro": 2, "oscuro": 3, "ac_claro": 4, "ac_oscuro": 5}
    def bloque(col):
        out = []
        for f in sis:
            out.append(f"  --{f[0].lower()}: {hexs(f[col])};")
        for f in gris:
            n = f[0].lower().replace(" (", "").replace(")", "")
            out.append(f"  --{n}: {hexs(f[col])};")
        return "\n".join(out)
    return f"""```css
/* Colores de sistema — HIG Color › Specifications (valores de referencia, no API). */
:root {{
  color-scheme: light dark;
{bloque(modos['claro'])}
}}
@media (prefers-color-scheme: dark) {{
  :root {{
{bloque(modos['oscuro'])}
  }}
}}
@media (prefers-contrast: more) {{
  :root {{
{bloque(modos['ac_claro'])}
  }}
}}
@media (prefers-contrast: more) and (prefers-color-scheme: dark) {{
  :root {{
{bloque(modos['ac_oscuro'])}
  }}
}}
```"""


def css_tipo(fuentes: Path) -> str:
    md = (fuentes / "hig" / "md" / "typography.md").read_text(encoding="utf-8")
    estilos = _tabla(md, "Large (default)", "iOS, iPadOS Dynamic Type sizes")
    track = {int(f[0]): f[1] for f in _tabla(md, "SF Pro", "iOS, iPadOS, visionOS tracking values") if f[0].isdigit()}
    pesos = {"Regular": 400, "Medium": 500, "Semibold": 600, "Bold": 700, "Heavy": 800}
    out = ["```css", "/* Escala tipográfica iOS (Dynamic Type «Large», tamaño por defecto) — HIG Typography.",
           "   tamaño y leading en pt → px (1 pt = 1 px CSS en Safari de iOS); tracking de la tabla SF Pro (1/1000 em). */"]
    for f in estilos:
        nombre, peso, tam, lead, enf = f[:5]
        cls = nombre.lower().replace(" ", "-")
        t = int(tam)
        tr = track.get(t, "0")
        em = int(tr.replace("+", "")) / 1000 if tr not in ("0", "") else 0
        out.append(f".{cls} {{ font-size: {t}px; line-height: {lead}px; font-weight: {pesos.get(peso, 400)}; "
                   f"letter-spacing: {em:g}em; }} /* {nombre}: {peso} {t}/{lead}, enfatizado {enf}, tracking {tr} */")
    out.append("```")
    return "\n".join(out)


def generar_plantillas(fuentes: Path, skill: Path) -> None:
    for plantilla in sorted((skill / "scripts" / "plantillas").glob("*.md")):
        txt = plantilla.read_text(encoding="utf-8")
        fecha = ""
        def rep(m):
            nonlocal fecha
            attrs = dict(re.findall(r'(\w+)="([^"]*)"', m.group(1)))
            pag = attrs["pagina"]
            md = (fuentes / "hig" / "md" / f"{pag}.md").read_text(encoding="utf-8")
            fecha = re.search(r"Descargado: (\S+)", md).group(1)[:10]
            fuente = f"_Fuente: [{pag}]({BASE}/design/human-interface-guidelines/{pag})_\n\n"
            return fuente + "\n".join(extraer_tablas(md, attrs["tras"], attrs.get("seccion"), attrs.get("contiene"), int(attrs.get("n", 1)), attrs.get("cruzar") == "si"))
        txt = re.sub(r"<<tabla ([^>]*)>>", rep, txt)
        txt = txt.replace("<<css_colores>>", css_colores(fuentes)).replace("<<css_tipo>>", css_tipo(fuentes))
        txt = txt.replace("{{fecha}}", f"HIG descargadas el {fecha}")
        guardar(skill / "references" / plantilla.name, txt)
        print("Plantilla:", plantilla.name, "⚠️" in txt and "CON AVISOS" or "ok")


# ---------------------------------------------------------------------------
# componentes.md
# ---------------------------------------------------------------------------

RX_ESTADO = re.compile(r"\b(selected|unselected|disabled|unavailable|dimmed|highlighted|pressed|focus(?:ed)?|hover|on state|off state|mixed state|loading|expanded|collapsed)\b", re.I)
RX_ERROR = re.compile(r"^(avoid|don’t|don't|never|refrain|do not)\b", re.I)
RX_USO = re.compile(r"^(use|prefer|consider using|in general, use|reserve)\b", re.I)
SECCIONES_NO_ANATOMIA = {"best practices", "platform considerations", "resources", "change log", "specifications"}


def analizar_componente(doc: dict) -> dict:
    r = Render(doc)
    res = {"uso": [], "errores": [], "otras": [], "valores": [], "estados": [], "secciones": [], "plataformas": [], "tablas": 0}
    h2 = h3 = ""
    def ctx():
        if h2.lower() == "platform considerations" and h3:
            return h3
        return "" if h2.lower() in ("best practices", "") else h2
    def visitar(b):
        nonlocal h2, h3
        t = b.get("type")
        if t == "heading":
            if b.get("level") == 3:
                h3 = b["text"]
            if b.get("level") == 2:
                h2, h3 = b["text"], ""
                if b["text"].lower() not in SECCIONES_NO_ANATOMIA:
                    res["secciones"].append(b["text"])
            elif b.get("level") == 3 and h2.lower() == "platform considerations":
                res["plataformas"].append(b["text"])
            return
        if h2.lower() in ("resources", "change log"):
            return
        if t == "table":
            res["tablas"] += 1
            return
        if t == "paragraph":
            ic = b.get("inlineContent") or []
            txt = sin_imagenes(r.inline(ic))
            if not txt:
                return
            if ic and ic[0].get("type") == "strong":
                regla = r.inline(ic[0].get("inlineContent")).strip()
                etiqueta = f"{regla}" + (f" _({ctx()})_" if ctx() else "")
                if RX_ERROR.match(regla):
                    res["errores"].append(etiqueta)
                elif RX_USO.match(regla):
                    res["uso"].append(etiqueta)
                else:
                    res["otras"].append(etiqueta)
            c = f" _({ctx()})_" if ctx() else ""
            for f in frases(txt.replace("**", "")):
                if RX_VALOR.search(f) and len(res["valores"]) < 8:
                    res["valores"].append(corta(f, 220) + c)
                elif RX_ESTADO.search(f) and len(res["estados"]) < 4 and len(f) < 260:
                    res["estados"].append(corta(f, 200) + c)
            return
        for k in ("content",):
            for x in b.get(k, []) or []:
                visitar(x)
        if t == "row":
            for c in b.get("columns", []):
                for x in c.get("content", []):
                    visitar(x)
        if t == "tabNavigator":
            for tab in b.get("tabs", []):
                for x in tab.get("content", []):
                    visitar(x)
    for s_ in doc.get("primaryContentSections", []):
        for b in s_.get("content", []):
            visitar(b)
    return res


def generar_componentes(fuentes: Path, skill: Path, rutas: dict) -> None:
    base = fuentes / "hig"
    indice = json.loads((base / "indice.json").read_text())
    padres = mapa_secciones(base, indice)
    grupos = collections.OrderedDict()
    raiz = json.loads((base / "json" / "components.json").read_text())
    for ts in raiz.get("topicSections", []):
        for ident in ts.get("identifiers", []):
            g = raiz["references"][ident]["url"].rstrip("/").rsplit("/", 1)[-1]
            grupos[g] = []
    for slug, e in indice.items():
        if e.get("seccion") == "components" and padres.get(slug) in grupos:
            grupos[padres[slug]].append(slug)
    plantilla = (skill / "scripts" / "plantillas_fijas" / "componentes_intro.md").read_text(encoding="utf-8")
    L = [plantilla.rstrip(), ""]
    total = 0
    for g, slugs in grupos.items():
        L += ["", f"## {indice[g]['titulo']}", ""]
        for slug in sorted(slugs, key=lambda x: indice[x]["titulo"]):
            e = indice[slug]
            doc = json.loads((base / "json" / f"{slug}.json").read_text())
            a = analizar_componente(doc)
            cl = e.get("changelog") or []
            total += 1
            L += [f"### {e['titulo']}", "",
                  f"`hig/{rutas[slug]}` · {e['url']} · plataformas: {(e.get('plataformas') or 'n/d').replace(',', ', ')}"
                  + (f" · actualizado {fecha_iso(cl[0][0])}" if cl else ""), "",
                  f"- **Qué es:** {Render(doc).inline(doc.get('abstract'))}"]
            if a["uso"]:
                L.append("- **Cuándo y cómo usarlo:** " + " · ".join(f"«{x}»" for x in a["uso"][:6]))
            if a["secciones"]:
                L.append("- **Anatomía / apartados de la página:** " + ", ".join(a["secciones"]))
            if a["valores"] or a["tablas"]:
                vals = " · ".join(f"«{v}»" for v in a["valores"][:6])
                extra = f" (+{a['tablas']} tabla(s) de especificaciones en la página condensada)" if a["tablas"] else ""
                L.append(f"- **Tamaños y valores:** {vals or '—'}{extra}")
            if a["estados"]:
                L.append("- **Estados:** " + " · ".join(f"«{x}»" for x in a["estados"]))
            if a["errores"]:
                L.append("- **Errores habituales (lo que Apple pide evitar):** " + " · ".join(f"«{x}»" for x in a["errores"]))
            if a["otras"]:
                L.append("- **Otras reglas:** " + " · ".join(f"«{x}»" for x in a["otras"][:8]) + (" …" if len(a["otras"]) > 8 else ""))
            if a["plataformas"]:
                L.append("- **Consideraciones por plataforma:** " + ", ".join(a["plataformas"]))
            L.append("")
    guardar(skill / "references" / "componentes.md", "\n".join(L).replace("{{total}}", str(total)))
    print("Componentes:", total)


# ---------------------------------------------------------------------------
# novedades.md
# ---------------------------------------------------------------------------

def generar_novedades(fuentes: Path, skill: Path, rutas: dict) -> None:
    indice = json.loads((fuentes / "hig" / "indice.json").read_text())
    por_fecha = collections.defaultdict(list)
    for slug, e in indice.items():
        for f, t in e.get("changelog") or []:
            por_fecha[fecha_iso(f)].append((e["titulo"], slug, t))
    intro = (skill / "scripts" / "plantillas_fijas" / "novedades_intro.md").read_text(encoding="utf-8")
    L = [intro.rstrip(), "", "## Registro de cambios agregado de todas las páginas de las HIG", "",
         f"Generado a partir de las tablas «Change log» de {len(indice) - 1} páginas. Más reciente primero.", ""]
    anio = None
    for f in sorted(por_fecha, reverse=True):
        if f[:4] != anio:
            anio = f[:4]
            L += ["", f"### {anio}", ""]
        L.append(f"- **{f}**")
        for tit, slug, t in sorted(por_fecha[f]):
            ruta = rutas.get(slug, "")
            L.append(f"  - {tit} (`hig/{ruta}`): {t}")
    guardar(skill / "references" / "novedades.md", "\n".join(L) + "\n")
    print("Novedades: fechas", len(por_fecha))


# ---------------------------------------------------------------------------
# recursos-diseno.md (inventario de Apple Design Resources; no descarga .dmg)
# ---------------------------------------------------------------------------

def generar_recursos(fuentes: Path, skill: Path) -> None:
    md = (fuentes / "web" / "dev-design-resources.md").read_text(encoding="utf-8")
    fecha = re.search(r"Descargado: (\S+)", md).group(1)[:10]
    filas, sec, ver, item = [], "", "", ""
    for l in md.splitlines():
        if l.startswith("## "):
            sec, ver, item = l[3:].strip(), "", ""
            if sec.startswith("Developer Footer"):
                break
        elif l.startswith("#### "):
            ver, item = l[5:].strip(), ""
        elif l.startswith("##### "):
            item = l[6:].strip()
        else:
            for txt, url in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", l):
                if "View in English" in txt or "Learn more" in txt:
                    continue
                filas.append([sec, ver, item, txt, url, ""])
        m = re.match(r"^\s*(\d+(?:\.\d+)? [KM]B)\s*$", l) or re.match(r"^(Requires .*|Note: .*)$", l.strip())
        if m and filas:
            filas[-1][5] = (filas[-1][5] + " " + m.group(1)).strip()
    L = ["# Apple Design Resources — inventario", "",
         f"Fuente: https://developer.apple.com/design/resources/ (descargada el {fecha}). **No se descargan los .dmg**;",
         "solo se listan. Las versiones son las que figuran en la página en esa fecha.", "",
         "Resumen: UI kits de iOS/iPadOS 27 y macOS 27 (Figma y Sketch); watchOS 26 y visionOS 26 (Figma y Sketch);",
         "tvOS 18 (Sketch); plantillas de iconos de app; plantillas de tecnologías; fuentes; SF Symbols; Icon Composer;",
         "Parallax Previewer; marcos de producto (*product bezels*); insignias y logotipos (en Licensing and Trademarks).", "",
         "Uso legal: ver `references/licencias-y-marcas.md` (fuentes solo para maquetas de software de plataformas Apple;",
         "marcos de producto según las *Marketing Resources and Identity Guidelines*).", "",
         "| Sección | Versión / grupo | Recurso | Formato / acción | Enlace | Notas |", "|---|---|---|---|---|---|"]
    for f in filas:
        L.append("| " + " | ".join(x.replace("|", "/") for x in f) + " |")
    L += ["", "Vídeo de introducción: `references/videos/2026-tech-talks-111427.md` (*Discover the Apple Design Resources*)."]
    guardar(skill / "references" / "recursos-diseno.md", "\n".join(L) + "\n")
    print("Recursos:", len(filas))


# ---------------------------------------------------------------------------
# premios-e-historias.md (Apple Design Awards + historias de desarrolladores)
# ---------------------------------------------------------------------------

def parsear_premios(md: str) -> list[dict]:
    lineas = [re.sub(r"\(https?:[^)]*\)", "", l).rstrip() for l in md.splitlines()]
    res, cat, sub, ganador_sig, modo = [], "", "", False, ""
    for i, l in enumerate(lineas):
        t = l.strip()
        if "Developer Footer" in t or "View last year" in t:
            break
        if not t or t.startswith("[View") or t.startswith("Streaming"):
            continue
        m = re.match(r"^#{1,2} (.+?)(?: Winners)?$", t)
        if m and not t.startswith("### ") and i > 6 and not re.match(r"^## .+", t) or (t.startswith("# ") and i > 6):
            if t.startswith("# ") and not t.startswith("# Introducing"):
                cat = re.sub(r"^# ", "", t).replace(" Winners", "").replace(" Finalists", "")
                modo = "finalistas" if "Finalists" in t else ""
                continue
        if t.startswith("## ") and cat == "" and "Winners" in t:
            cat = t[3:].replace(" Winners", "")
            continue
        if re.match(r"^### (Apps|Games|Winners|Finalists)$", t):
            sub = t[4:]
            continue
        if t.startswith("Winner [") or t == "Winner":
            ganador_sig = True
            continue
        nombre, rol = None, None
        if t.startswith("#### ") and t[5:] not in ("Finalists",):
            nombre = t[5:]
            rol = "ganador" if (ganador_sig or sub == "Winners") else "finalista"
        elif t.startswith("##### "):
            nombre, rol = t[6:], "finalista"
        elif t.startswith("## ") and cat and not t.endswith("Winners"):
            nombre, rol = t[3:], "ganador"
        if nombre and cat:
            sig = [x.strip() for x in lineas[i + 1:i + 8] if x.strip() and x.strip() not in ("]", "[")]
            res.append({"categoria": cat, "tipo": sub if sub in ("Apps", "Games") else "", "nombre": nombre.strip(),
                        "rol": rol, "detalle": sig[:4]})
            ganador_sig = False
    return res


def generar_premios(fuentes: Path, skill: Path) -> None:
    web = fuentes / "web"
    indice = json.loads((web / "indice.json").read_text())
    L = ["# Apple Design Awards e historias de desarrolladores", "",
         "Fuentes: https://developer.apple.com/design/awards/ (2026) y las páginas de años anteriores; historias",
         "*Behind the Design*, *ADA Q&A* y artículos enlazados desde las páginas de diseño. Útil para buscar",
         "**ejemplos reales** de buenas prácticas (cita la categoría y el año). Descripciones: primera frase, literal.", ""]
    for nombre in ["dev-design-awards"] + [f"dev-design-awards-{y}" for y in range(2025, 2019, -1)]:
        f = web / f"{nombre}.md"
        if not f.exists():
            continue
        md = f.read_text(encoding="utf-8")
        anio = re.search(r"(\d{4})", indice.get(nombre, {}).get("titulo", "")) or re.search(r"(\d{4})", nombre)
        url = indice.get(nombre, {}).get("url", "")
        L += ["", f"## {anio.group(1) if anio else nombre} — {url}", ""]
        premios = parsear_premios(md)
        cat_ant = None
        for p_ in premios:
            if p_["categoria"] != cat_ant:
                L.append(f"- **{p_['categoria']}**")
                cat_ant = p_["categoria"]
            det = [d for d in p_["detalle"] if not d.startswith("[Read") and not d.startswith("#")]
            desc = next((d for d in det if len(d) > 60), "")
            meta = " · ".join(d for d in det if len(d) <= 60)[:120]
            prim = corta(frases(desc)[0], 200) if desc else ""
            L.append(f"  - {'🏆 ' if p_['rol'] == 'ganador' else ''}{p_['nombre']}"
                     + (f" ({p_['tipo']})" if p_["tipo"] else "") + (f" — {meta}" if meta else "")
                     + (f" — «{prim}»" if prim else ""))
    L += ["", "## Historias de desarrolladores y artículos", ""]
    for k, e in sorted(indice.items(), key=lambda x: x[1]["titulo"]):
        if k.startswith("dev-news-") or k.startswith("dev-articles-"):
            tit = e["titulo"].replace(" - Discover - Apple Developer", "").replace(" - Articles - Apple Developer", "")
            L.append(f"- [{tit}]({e['url']})")
    guardar(skill / "references" / "premios-e-historias.md", "\n".join(L) + "\n")
    print("Premios: ok")


# ---------------------------------------------------------------------------
# checklist-revision.md
# ---------------------------------------------------------------------------

def generar_checklist(fuentes: Path, skill: Path, rutas: dict) -> None:
    base = fuentes / "hig"
    indice = json.loads((base / "indice.json").read_text())
    intro = (skill / "scripts" / "plantillas_fijas" / "checklist_intro.md").read_text(encoding="utf-8")
    L = [intro.rstrip(), "", "## Apéndice — reglas negativas de cada página (literales)", "",
         "Generado automáticamente: frases en negrita que empiezan por Avoid / Don’t / Never / Refrain / Do not,",
         "con su apartado entre paréntesis. Úsalo para encontrar la regla exacta que respalda un problema.", ""]
    total = 0
    for seccion in ["foundations", "patterns", "components", "inputs", "technologies", "getting-started"]:
        L += ["", f"### {seccion}", ""]
        for slug in sorted((k for k, e in indice.items() if e.get("seccion") == seccion), key=lambda k: indice[k]["titulo"]):
            doc = json.loads((base / "json" / f"{slug}.json").read_text())
            a = analizar_componente(doc)
            if a["errores"]:
                total += len(a["errores"])
                L.append(f"- **{indice[slug]['titulo']}** (`hig/{rutas[slug]}`): " + " · ".join(f"«{x}»" for x in a["errores"]))
    guardar(skill / "references" / "checklist-revision.md", "\n".join(L) + "\n")
    print("Checklist: reglas negativas", total)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fuentes", default="_fuentes")
    ap.add_argument("--skill", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("partes", nargs="*", default=["hig", "videos", "componentes", "novedades", "plantillas", "recursos", "premios", "checklist"])
    a = ap.parse_args()
    fuentes, skill = Path(a.fuentes), Path(a.skill)
    rutas = generar_hig(fuentes, skill) if "hig" in a.partes else json.loads((fuentes / "rutas_hig.json").read_text())
    if "videos" in a.partes:
        generar_videos(fuentes, skill, rutas)
    if "novedades" in a.partes:
        generar_novedades(fuentes, skill, rutas)
    if "componentes" in a.partes:
        generar_componentes(fuentes, skill, rutas)
    if "plantillas" in a.partes:
        generar_plantillas(fuentes, skill)
    if "recursos" in a.partes:
        generar_recursos(fuentes, skill)
    if "checklist" in a.partes:
        generar_checklist(fuentes, skill, rutas)
    if "premios" in a.partes:
        generar_premios(fuentes, skill)


if __name__ == "__main__":
    main()
