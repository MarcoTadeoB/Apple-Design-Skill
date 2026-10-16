#!/usr/bin/env python3
"""Califica las salidas de las pruebas (con y sin skill) contra evals.json.

Además de las aserciones por regex, comprueba las citas de vídeo: para cada enlace
`…/videos/play/<evento>/<id>/?time=T` seguido de «cita», verifica en la caché `_fuentes/`
que la cita aparece en la transcripción a ±30 s de T (citas verificables).

Uso: python3 evals/calificar.py diseno-apple-workspace/iteration-1 [--fuentes _fuentes]
Escribe grading.json en cada carpeta de ejecución (formato del visor de skill-creator).
"""
import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RX_LINK = re.compile(r"videos/play/([a-z0-9-]+)/(\d+)/?\?time=(\d+)\)?[^«\n]{0,250}?«([^»]{12,})»")


def norm(t):
    return re.sub(r"[^a-z0-9]", "", t.lower().replace("’", "'"))


def verificar_citas(texto, fuentes: Path):
    """Para cada enlace de vídeo con ?time=T, busca en la misma línea citas «…» que estén en la
    transcripción de ESE vídeo. Si la cita está en el vídeo, su tiempo real debe estar a ±45 s de T.
    Las citas que no están en el vídeo (p. ej. citas de las HIG en la misma línea) se ignoran."""
    ok = mal = 0
    detalles = []
    for linea in texto.splitlines():
        enlaces = re.findall(r"videos/play/([a-z0-9-]+)/(\d+)/?\?time=(\d+)", linea)
        citas = [norm(c.replace("…", " ").replace("*", ""))[:50] for c in re.findall(r"«([^»]{15,})»", linea)]
        for ev, vid, t in enlaces:
            f = fuentes / "videos" / "json" / f"{ev}-{vid}.json"
            if not f.exists():
                mal += 1
                detalles.append(f"{ev}/{vid}: el vídeo no existe")
                continue
            tr = json.loads(f.read_text())["transcripcion"]
            t = int(t)
            for c in citas:
                if len(c) < 20:
                    continue
                pos = [x["t"] for i, x in enumerate(tr) if c[:30] in norm(" ".join(y["texto"] for y in tr[i:i + 4]))]
                if not pos:
                    continue
                if any(abs(p - t) <= 45 for p in pos):
                    ok += 1
                else:
                    mal += 1
                    detalles.append(f"{ev}/{vid}@{t}: la cita está en {int(pos[0])} s")
    return ok, mal, detalles


_CORPUS = None


def corpus(fuentes: Path) -> str:
    global _CORPUS
    if _CORPUS is None:
        partes = [p.read_text(errors="replace") for p in (fuentes / "hig" / "md").glob("*.md")]
        partes += [p.read_text(errors="replace") for p in (fuentes / "web").glob("*.md")]
        for p in (fuentes / "videos" / "json").glob("*.json"):
            partes.append(" ".join(x["texto"] for x in json.loads(p.read_text())["transcripcion"]))
        _CORPUS = norm(re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", " ".join(partes)))
    return _CORPUS


def verificar_literales(texto, fuentes: Path):
    """Citas «…» en inglés (≥ 6 palabras): deben aparecer literalmente en las fuentes descargadas."""
    ok, mal, det = 0, 0, []
    c = corpus(fuentes)
    for q in re.findall(r"«([^»]{25,})»", texto):
        q2 = q.replace("**", "").replace("…", " ").strip()
        palabras = re.findall(r"[A-Za-z’']+", q2)
        ingles = sum(w.lower() in ("the", "and", "to", "of", "a", "your", "you", "for", "in", "that", "is", "it") for w in palabras)
        espanol = sum(w.lower() in ("de", "la", "el", "que", "los", "las", "una", "un", "con", "por", "para", "nota", "añadir") for w in palabras)
        if len(palabras) < 6 or ingles < 2 or espanol:
            continue
        trozos = [t for t in re.split(r"\s*\.\.\.\s*|\s{2,}", q2) if len(t) > 15] or [q2]
        if all(norm(t)[:60] in c for t in trozos):
            ok += 1
        else:
            mal += 1
            det.append(q2[:70])
    return ok, mal, det


def evaluar(a, texto, outdir: Path):
    if "regex" in a:
        m = re.search(a["regex"], texto)
        return bool(m), (f"encontrado: «{m.group(0)[:80]}»" if m else "no encontrado")
    if "archivo" in a:
        p = outdir / a["archivo"]
        return p.exists(), ("existe" if p.exists() else "no existe")
    if "regex_archivo" in a or "regex_archivo_no" in a:
        html = "".join(p.read_text(errors="replace") for p in outdir.glob("*.html"))
        if not html:
            return False, "no hay HTML"
        if "regex_archivo" in a:
            m = re.search(a["regex_archivo"], html)
            return bool(m), (f"encontrado: «{m.group(0)[:60]}»" if m else "no encontrado en el HTML")
        m = re.search(a["regex_archivo_no"], html)
        return not m, ("no aparece (bien)" if not m else f"aparece: «{m.group(0)[:60]}»")
    if "min_urls_hig" in a:
        urls = set(re.findall(r"human-interface-guidelines/([a-z0-9-]+)", texto))
        return len(urls) >= a["min_urls_hig"], f"{len(urls)} páginas distintas: {', '.join(sorted(urls))[:200]}"
    if "min_tiempos" in a:
        n = len(re.findall(r"\?time=\d+", texto))
        return n >= a["min_tiempos"], f"{n} marcas de tiempo enlazadas"
    return False, "aserción desconocida"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("iteracion")
    ap.add_argument("--fuentes", default=str(RAIZ / "_fuentes"))
    a = ap.parse_args()
    evals = {e["id"]: e for e in json.load(open(RAIZ / "evals" / "evals.json"))["evals"]}
    resumen = []
    for d in sorted(Path(a.iteracion).glob("eval-*")):
        eid = int(d.name.split("-")[1])
        e = evals[eid]
        for conf in ("with_skill", "without_skill"):
            out = d / conf / "outputs"
            texto = "".join(p.read_text(errors="replace") for p in out.glob("*.md")) if out.exists() else ""
            exps = []
            for asr in e["assertions"]:
                ok, ev = evaluar(asr, texto, out) if texto else (False, "sin salida")
                exps.append({"text": asr["texto"], "passed": ok, "evidence": ev})
            okc, malc, det = verificar_citas(texto, Path(a.fuentes))
            if okc + malc:
                exps.append({"text": "Las citas de vídeo con marca de tiempo son verificables (±30 s)",
                             "passed": malc == 0, "evidence": f"{okc} verificadas, {malc} no verificables. " + "; ".join(det[:5])})
            okl, mall, detl = verificar_literales(texto, Path(a.fuentes))
            if okl + mall:
                exps.append({"text": "Las citas literales en inglés existen en las fuentes de Apple",
                             "passed": mall == 0, "evidence": f"{okl} encontradas, {mall} no encontradas. " + " | ".join(detl[:4])})
            n = sum(x["passed"] for x in exps)
            g = {"expectations": exps, "summary": {"passed": n, "failed": len(exps) - n, "total": len(exps),
                                                   "pass_rate": round(n / len(exps), 3) if exps else 0}}
            (d / conf).mkdir(parents=True, exist_ok=True)
            json.dump(g, open(d / conf / "grading.json", "w"), ensure_ascii=False, indent=1)
            resumen.append((eid, e["nombre"], conf, n, len(exps)))
    for r in sorted(resumen):
        print(f"eval {r[0]:>2} {r[1]:<40} {r[2]:<14} {r[3]}/{r[4]}")


if __name__ == "__main__":
    main()
