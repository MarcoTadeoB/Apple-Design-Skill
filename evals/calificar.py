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
RX_LINK = re.compile(r"videos/play/([a-z0-9-]+)/(\d+)/?\?time=(\d+)\)?\s*[«\"“]([^»\"”]{12,})[»\"”]")


def norm(t):
    return re.sub(r"[^a-z0-9]", "", t.lower().replace("’", "'"))


def verificar_citas(texto, fuentes: Path):
    ok = mal = 0
    detalles = []
    for ev, vid, t, cita in RX_LINK.findall(texto):
        f = fuentes / "videos" / "json" / f"{ev}-{vid}.json"
        if not f.exists():
            mal += 1
            detalles.append(f"{ev}/{vid}@{t}: vídeo no existe")
            continue
        tr = json.loads(f.read_text())["transcripcion"]
        t = int(t)
        ventana = norm(" ".join(x["texto"] for x in tr if t - 30 <= x["t"] <= t + 45))
        frag = norm(cita.replace("…", " "))[:60]
        if frag and frag[:40] in ventana:
            ok += 1
        else:
            mal += 1
            detalles.append(f"{ev}/{vid}@{t}: «{cita[:50]}…» no está en ±30 s")
    return ok, mal, detalles


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
