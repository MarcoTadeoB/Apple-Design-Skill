#!/usr/bin/env python3
"""Busca una frase en las transcripciones descargadas y devuelve su marca de tiempo exacta.

Uso:
    python3 buscar_cita.py --fuentes ./_fuentes "texto a buscar" [--video wwdc2025-219]
Sirve para verificar citas antes de publicarlas (la skill nunca debe inventar tiempos).
"""
import argparse
import json
import re
from pathlib import Path


def normal(t: str) -> str:
    return re.sub(r"[^a-z0-9 ]", "", t.lower().replace("’", "'").replace("'", ""))


def buscar(fuentes: Path, frase: str, video: str | None = None):
    objetivo = normal(frase)
    res = []
    archivos = [fuentes / "videos" / "json" / f"{video}.json"] if video else sorted((fuentes / "videos" / "json").glob("*.json"))
    for f in archivos:
        d = json.loads(f.read_text())
        tr = d.get("transcripcion", [])
        # ventana deslizante de fragmentos para frases que cruzan cortes
        for i in range(len(tr)):
            ventana = normal(" ".join(x["texto"] for x in tr[i:i + 6]))
            if ventana.startswith(objetivo[: max(20, len(objetivo) // 2)]) or (objetivo in ventana and objetivo[:30] in normal(" ".join(x["texto"] for x in tr[i:i + 2]))):
                t = int(tr[i]["t"])
                res.append((d["clave"], t, f"{t // 60}:{t % 60:02d}", f"{d['url']}?time={t}"))
                break
    return res


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("frase")
    ap.add_argument("--fuentes", default="_fuentes")
    ap.add_argument("--video")
    a = ap.parse_args()
    for r in buscar(Path(a.fuentes), a.frase, a.video):
        print(*r)
