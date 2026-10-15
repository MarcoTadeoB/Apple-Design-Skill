# diseno-apple — Skill de diseño de Apple para Claude

Skill que convierte a Claude en experto en aplicar el contenido de
[developer.apple.com/design](https://developer.apple.com/design/): Human Interface Guidelines completas
(172 páginas), Liquid Glass, SF Symbols, fuentes, Icon Composer, Design Resources, What's New, Design Pathway,
289 vídeos de diseño (271 con transcripción), Apple Design Awards e historias de desarrolladores.
Da valores exactos y cita la página o el vídeo (con marca de tiempo) de cada dato.

- `diseno-apple/` — la skill (SKILL.md + `references/` + `scripts/`).
- `_fuentes/` — caché local con el texto completo de Apple (HIG, HTML, transcripciones). **No se publica**
  (está en `.gitignore`): se regenera con los scripts.
- `evals/` — pruebas de la skill (con y sin skill) y resultados.

## Instalar

Copia la carpeta `diseno-apple/` a `~/.claude/skills/` (Claude Code) o empaquétala como `.skill`.

## Actualizar cuando Apple cambie algo

```bash
cd diseno-apple
python3 scripts/comprobar_novedades.py                       # informe de cambios
python3 scripts/descargar_hig.py --fuentes ../_fuentes        # 1 petición/s, 3 reintentos
python3 scripts/descargar_paginas.py --fuentes ../_fuentes
python3 scripts/descargar_videos.py --fuentes ../_fuentes --solo-nuevos
python3 scripts/generar_referencias.py --fuentes ../_fuentes
python3 scripts/inventario.py --fuentes ../_fuentes
python3 scripts/comprobar_novedades.py --guardar-estado --fuentes ../_fuentes
```

El contenido de las referencias son resúmenes, valores, tablas de especificaciones y citas cortas de Apple, con su
URL. Apple, iPhone, iPad, Mac, Liquid Glass, SF Symbols y demás son marcas de Apple Inc.; este proyecto no está
afiliado a Apple.
