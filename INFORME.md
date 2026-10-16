# Informe final — skill `diseno-apple`

Fecha: 16-10-2026 (descarga de fuentes: 15-10-2026). Rama: `claude/wonderful-planck-gex0i5`.

## 1. Qué se ha procesado

| Fuente | Procesado | Huecos |
|---|---|---|
| Human Interface Guidelines (formato JSON) | **172 páginas + raíz** (getting-started 10, foundations 19, patterns 26, components 73, inputs 14, technologies 30; incluye las páginas índice). Convertidas a Markdown con tablas, pestañas por plataforma, recursos, registro de cambios y **valores de las imágenes** (colores de sistema en sus 4 variantes, desde el texto alternativo). | 1 enlace roto en *Designing for iOS* (`spatial-interactions`, 404: la página no existe). |
| Páginas de diseño (no HIG) | **84**: /design, What's new, Get started (Design Pathway), Resources, Apple Design Awards 2020–2026, /fonts (con las licencias de SF y SF Compact), /sf-symbols, /icon-composer, /pass-designer, /reality-composer-pro, Licensing and Trademarks (+ Mac logo), Marketing Guidelines del App Store y **65 historias de desarrolladores/artículos**. | www.apple.com bloqueado por la política de red del entorno (guía de marcas para terceros y lista de marcas); ADA 2019 devuelve 403; la URL antigua de Reality Composer Pro da 404 (se usó la nueva). |
| Vídeos | **289 procesados**: los **192** de /videos/design/ + **97** enlazados desde las HIG o las páginas de diseño. **271 con transcripción** (con marca de tiempo por frase), capítulos, recursos y vídeos relacionados. | **18 sin transcripción**: Apple no la publica (Q&A, «Meet the Presenter», laboratorios de iPhone Duo y dos sesiones antiguas); comprobado en el HTML. 0 fallos de descarga. |
| Design Resources | Inventario de **83 enlaces** (kits de Figma/Sketch por plataforma y versión, plantillas de iconos, plantillas de tecnologías, fuentes, SF Symbols 27, Icon Composer, Parallax Previewer, marcos de producto, insignias). **No se descargó ningún .dmg.** | Licencias completas de New York y SF Symbols: solo dentro de los .dmg. |

Todo se descargó con un máximo de 1 petición/segundo y hasta 3 reintentos. El contenido íntegro está en `_fuentes/`
(caché local, en `.gitignore`, **no publicada**).

## 2. Qué contiene la skill

- `SKILL.md` (157 líneas): reglas (citar siempre, no inventar, origen de cada dato, prevalece lo más reciente,
  licencias), flujo de 5 pasos, mapa de referencias y lectura mínima por tipo de tarea.
- `references/`: 172 páginas HIG condensadas (reglas literales en negrita, frases con valores, tablas completas,
  vídeos que las explican, registro de cambios) + `tokens.md`, `componentes.md` (64 componentes),
  `liquid-glass.md`, `novedades.md`, `licencias-y-marcas.md`, `web.md`, `checklist-revision.md` (con 206 reglas
  «Avoid/Don’t/Never»), `herramientas.md`, `recursos-diseno.md`, `premios-e-historias.md`, `_inventario.md` y
  289 fichas de vídeo (**19 con resumen y reglas redactadas**, 177 reglas con marca de tiempo **verificada
  automáticamente** contra la transcripción; el resto con capítulos y citas literales seleccionadas).
- `scripts/`: `descargar_hig.py`, `descargar_paginas.py`, `descargar_videos.py`, `generar_referencias.py`,
  `inventario.py`, `comprobar_novedades.py`, `buscar_cita.py`.

**Versión vigente identificada**: plataformas **27** (8-6-2026) sobre el lenguaje **Liquid Glass** de la 26
(9-6-2025); último cambio en las HIG el 13-10-2026; iPhone Duo desde el 9-9-2026. `novedades.md` recoge qué
cambió de la 26 a la 27 y **6 contradicciones** entre fuentes (p. ej. scroll edge effect: el vídeo de 2025 dice
*soft* por defecto y la HIG de junio de 2026 pide *automatic* → prevalece la HIG).

**Comprobación web (Chromium 141)**: la refracción con `feDisplacementMap` en `backdrop-filter` funciona; una
sombra exterior en el mismo elemento la desplaza y recorta (no siempre la anula del todo); las sombras `inset`
no la afectan; la sombra en una capa hermana se ve bien. Safari no se pudo probar (no hay WebKit en el entorno).

## 3. Pruebas (14 casos, con y sin skill)

Condiciones: subagentes sin acceso a la web; con skill solo podían leer la carpeta de la skill (sin `_fuentes/`,
como una skill publicada); sin skill, solo su conocimiento. 1 ejecución por caso y configuración.

| # | Prueba | Con skill | Sin skill |
|---|---|---|---|
| 1 | RGB de systemBlue oscuro + alto contraste | 4/4 | 2/3 |
| 2 | Liquid Glass clear vs regular | 6/6 | 3/5 |
| 3 | Tamaño mínimo de control iOS/visionOS | 5/5 | 3/4 |
| 4 | SF Symbols / SF Pro en una web | 7/7 | 4/5 |
| 5 | Tab bar de iPhone en HTML/CSS | 9/9 | 7/7 |
| 6 | Revisión de una pantalla según las HIG | 9/10 → **10/10** tras la corrección | 6/8 |
| 7 | Cambios de la 26 a la 27 | 8/8 | 3/6 |
| 8 | Vídeo más reciente sobre iconos, con tiempos | 5/5 | 1/4 |
| 9 | Escala de Dynamic Type de iOS | 7/7 | 4/5 |
| 10 | Cancel y Done en una sheet | 6/6 | 3/4 |
| 11 | iPhone Duo: barras y pliegue | 7/7 | 3/5 |
| 12 | Lienzo de icono watchOS y apariencias | 5/5 | 2/3 |
| 13 | Marca naranja → Liquid Glass | 6/6 | 1/4 |
| 14 | Contraste mínimo 15 pt / 20 pt negrita | 4/4 | 2/3 |

- Media por prueba: **99 % con skill frente a 65 % sin skill** (+35 puntos). Coste: +11 s y +16.6k tokens de media.
- Verificación de veracidad (solo aplicable con skill): **59 citas de vídeo con marca de tiempo** comprobadas contra
  la transcripción (0 errores) y **183 citas literales en inglés** encontradas en las fuentes de Apple.
- Sin skill, los errores son de actualidad: valores de color anteriores a la versión 26 (systemBlue
  64,156,255 en vez de 92,184,255), desconocimiento de iPhone Duo, de los principios de 2026 y del vídeo de
  iconos de la WWDC26, y casi nunca da URL ni marcas de tiempo.
- Fallos encontrados y corregidos: (1) una paráfrasis entre comillas en la prueba 6 → regla de citas literales
  en SKILL.md y repetición de la prueba (10/10, 26/26 citas encontradas); (2) la prueba de HTML fue la más cara
  (433 s) → «lectura mínima según la tarea» en SKILL.md; (3) faltaba el resumen del vídeo de iconos más reciente
  (WWDC26, laboratorio de Icon Composer) → añadido antes de las pruebas.
- Limitación: la prueba 5 no discrimina con comprobaciones automáticas; se revisó visualmente (la versión con
  skill sigue la guía de 2026 —barra neutra, color solo en la pestaña seleccionada— pero dejó sin margen
  izquierdo un carrusel).

Resultados completos: `diseno-apple-workspace/iteration-1/` (`benchmark.md`, `revision.html`, salidas y
`grading.json` de cada prueba) e `iteration-2/` (repetición de la prueba 6). Calificador: `evals/calificar.py`.

## 4. Cómo actualizar la skill

```bash
cd diseno-apple
python3 scripts/comprobar_novedades.py            # dice si cambió algo (HIG, What's new, vídeos)
python3 scripts/descargar_hig.py --fuentes ../_fuentes
python3 scripts/descargar_paginas.py --fuentes ../_fuentes
python3 scripts/descargar_videos.py --fuentes ../_fuentes --solo-nuevos
python3 scripts/generar_referencias.py --fuentes ../_fuentes
python3 scripts/inventario.py --fuentes ../_fuentes
python3 scripts/comprobar_novedades.py --guardar-estado --fuentes ../_fuentes
```

Después, revisar a mano `scripts/plantillas_fijas/*.md`, `references/liquid-glass.md`,
`licencias-y-marcas.md` y `herramientas.md`, y añadir resúmenes de vídeos nuevos en
`scripts/resumenes_videos.json` (cada regla con una «ancla» literal; el generador calcula la marca de tiempo y
avisa si no la encuentra). Para cubrir los huecos de www.apple.com, permitir ese dominio en la configuración de
red del entorno y volver a ejecutar `descargar_paginas.py`.
