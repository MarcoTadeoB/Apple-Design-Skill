# Novedades del diseño de Apple — versiones 26 y 27

Fuentes: [What's new](https://developer.apple.com/design/whats-new/), los registros de cambios de cada página de
las HIG (tabla al final de este archivo), las páginas de herramientas (SF Symbols, Icon Composer, Pass Designer,
Reality Composer Pro, Design Resources) y los vídeos. Descarga: ver `references/_inventario.md`.

## Versión vigente

- **Plataformas 27** (iOS 27, iPadOS 27, macOS 27, watchOS 27, tvOS 27, visionOS 27). Evidencias: la página
  [SF Symbols](https://developer.apple.com/sf-symbols/) («available in apps running iOS 27, iPadOS 27, macOS 27,
  watchOS 27, tvOS 27, and visionOS 27»), el cambio de *Wallet* del 8-6-2026 («Updated to reflect guidance for
  iOS 27…») y los kits *iOS and iPadOS 27* y *macOS 27* de Design Resources.
- **El lenguaje visual sigue siendo Liquid Glass**, introducido con las plataformas 26 el 9-6-2025. La versión 27
  no lo sustituye: refina guías (iconos, búsqueda, barras, sidebars, scroll edge effects, menús) y añade
  contenido nuevo (principios de diseño, Snippets, Siri AI, iPhone Duo).
- Último cambio registrado en las HIG: **13-10-2026** (Widgets y Live Activities).

## Qué trajo la versión 26 (9-6-2025) — el gran rediseño

- **Liquid Glass**: nuevo material para la capa funcional (controles y navigación) que flota sobre el contenido;
  variantes *regular* y *clear*; tintado nuevo; adaptaciones automáticas de accesibilidad.
  `references/liquid-glass.md`, vídeos `2025-219`, `2025-356`.
- **Colores de sistema actualizados** en claro, oscuro y alto contraste («Updated system color values», Color,
  9-6-2025). Tabla en `references/tokens.md`.
- **Iconos de app por capas** con apariencias default, dark, clear (light/dark) y tinted (light/dark); rejilla
  nueva; lienzo de 1024 px (iOS, iPadOS, macOS) y 1088 px (watchOS); nueva app **Icon Composer**. Vídeos
  `2025-220` y `2025-361`.
- **Formas concéntricas** (fija, cápsula, concéntrica); controles grandes de macOS en cápsula y nuevo tamaño
  X-Large (vídeo `2025-356`, [3:42](https://developer.apple.com/videos/play/wwdc2025/356/?time=222) y [4:23](https://developer.apple.com/videos/play/wwdc2025/356/?time=263)).
- **Barras**: los elementos de barra se agrupan y comparten fondo; pestaña de búsqueda dedicada en iOS;
  accesorio de la tab bar para funciones persistentes; *scroll edge effects* en lugar de separadores
  (vídeo `2025-356`; HIG Tab bars, Toolbars, Scroll views — 28-7-2025).
- **iPadOS 26**: nuevo sistema de ventanas, nuevo puntero, barra de menús en todas las apps (vídeo `2025-208`).
- **SF Symbols 7**: animaciones Draw On/Off, Variable Draw, degradados, Magic Replace mejorado (vídeo `2025-337`;
  HIG SF Symbols, 28-7-2025).
- Ajustes posteriores: Materials y Motion (9-9-2025), y el 16-12-2025 guía de Liquid Glass revisada en Color,
  Buttons, Toolbars y Tab bars; pesos enfatizados en las tablas de Dynamic Type (Typography).

## Qué cambió en la versión 27 (desde el 8-6-2026)

Lo que sigue resume los registros de cambios de Apple; el texto anterior de cada página no está en la caché,
así que la comparación es por lo que Apple declara haber cambiado y por la guía vigente.

| Fecha | Cambio | Qué dice ahora la guía (resumen) |
|---|---|---|
| 24-3-2026 | Sheets: colocación de botones | En iOS/iPadOS, Cancel en el borde inicial de la toolbar superior y Done en el final; si hay Done, ofrece siempre Cancel o Back; no muestres Cancel, Done y Back a la vez; en flujos de varios pasos Back sustituye a Cancel. |
| 24-3-2026 | Scroll views: Look to Scroll (visionOS) | Admitirlo en vistas de lectura o exploración; no en contenido secundario. |
| 8-6-2026 | **Design principles** (reintroducidos) | Ocho principios: Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft, Delight (vídeo `2026-250`). |
| 8-6-2026 | App icons: guía de Liquid Glass refinada | Icon Composer 2 (beta): refracción por capa, nuevos brillos especulares con ángulo de luz vertical, anotación Default/Dark/Mono ([Icon Composer](https://developer.apple.com/icon-composer/)). |
| 8-6-2026 | Searching y Search fields: terminología y búsqueda como pestaña en iOS | Pestaña Search estándar o prominente; toolbar inferior preferida (vídeo `2026-292`). |
| 8-6-2026 | Tab bars: terminología y arte | — |
| 8-6-2026 | Sidebars: colores de iconos y estilo adaptable | Por defecto los iconos usan el color de acento; en macOS deben respetar el acento elegido por la persona; colores fijos solo con moderación (p. ej. VIP de Mail en amarillo). |
| 8-6-2026 | Scroll views: scroll edge effects | «Prefer the automatic scroll edge effect style»; si usas *soft*, prueba la legibilidad a fondo. |
| 8-6-2026 | Menus: iconos en elementos de menú | «Use menu item icons sparingly and with purpose.» |
| 8-6-2026 | Siri (Siri AI), App Shortcuts (app schemas), **Snippets** (página nueva), Generative AI, Machine learning | Ver páginas en `hig/technologies/` y `hig/components/snippets.md`. |
| 8-6-2026 | Apple Pay, Wallet (iOS 27 y **Pass Designer**) | Pass Designer: app para crear y previsualizar pases de Wallet en el Mac. |
| 8-6-2026 | Herramientas | SF Symbols «8 beta» en What's new; Icon Composer 2 beta; Reality Composer Pro 3; kits de Sketch de iOS/iPadOS 27 y macOS 27 (Figma el 23-6 y el 17-9-2026). |
| 9-9-2026 | **Designing for iPhone Duo** (página nueva) | Primer iPhone plegable: posturas, regiones reservadas, controles en el eje vertical, *arrangement views* (vídeos `2026-tech-talks-111466`, `-111463`, `-111462`). |
| 9-9-2026 | Layout | «Updated guidance to reflect current best practices»; desaparecen las tablas de tamaños por dispositivo. |
| 9-9-2026 | Branding (color de marca), SharePlay | Vídeo `2026-251`: el color de marca va a la capa de contenido. |
| 17-9-2026 | Apple In-App Purchase (nuevo nombre) | — |
| 18-9-2026 | Design Resources | Marcos de iPhone Duo y de los iPhone 18. |
| 13-10-2026 | Widgets (Apple HomeView, watchOS), Live Activities (anchos limitados) | Ver `hig/components/widgets.md` y `live-activities.md`. |

## Contradicciones entre fuentes (y cuál prevalece)

Regla: prevalece la fuente más reciente; en empate, la HIG frente al vídeo.

1. **Estilo por defecto del scroll edge effect.** Vídeo `2025-356` (9-6-2025, [11:56](https://developer.apple.com/videos/play/wwdc2025/356/?time=716)): «Soft is the default and the
   one you'll use in most cases». HIG *Scroll views* (8-6-2026): «Prefer the automatic scroll edge effect style».
   → **Prevalece la HIG de 2026: usa `automatic`.**
2. **Nombre de la versión de SF Symbols.** What's new (8-6-2026): «Download SF Symbols 8 beta». Design Resources
   y la página SF Symbols (octubre de 2026) enlazan `SF-Symbols-27.dmg` («Download SF Symbols 27»). → La
   numeración actual parece alinearse con las plataformas (27); cita ambos nombres si hace falta.
3. **Número de símbolos.** What's new (9-6-2025): «over 6,900». Página SF Symbols y Design Resources (2026):
   «over 7,000». → **Más de 7.000.**
4. **Requisitos de Icon Composer.** Design Resources: «Requires macOS Sequoia or later». Página Icon Composer
   (Icon Composer 2): «Requires macOS Tahoe 26.4 or later». → Para la versión actual, **macOS Tahoe 26.4**.
5. **Tamaños de pantalla por dispositivo.** Vídeos antiguos y versiones previas de *Layout* los daban; la página
   vigente (9-9-2026) ya no. → No los cites como guía vigente.
6. **Barras en iPhone Duo.** Todo lo anterior a septiembre de 2026 asume barras arriba/abajo; en iPhone Duo pasan
   al lateral salvo en la pantalla interior en vertical (HIG *Designing for iPhone Duo*). → Aplica la guía de
   iPhone Duo solo a ese dispositivo.
