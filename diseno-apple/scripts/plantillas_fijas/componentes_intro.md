# Componentes de Apple — guía rápida

{{total}} componentes de la sección *Components* de las HIG, agrupados como en Apple. Para cada uno:
qué es (resumen literal de Apple), cuándo usarlo, apartados de la página (anatomía), valores exactos, estados,
errores habituales y plataformas. Las frases entre «» son citas literales de las HIG; abre la página condensada
(`references/hig/components/…`) para las tablas completas y el contexto, y la URL para el texto íntegro.

## Cómo elegir el componente (resumen con fuentes)

| Necesidad | Componente | Fuente |
|---|---|---|
| Navegar entre secciones principales (iPhone) | Tab bar (flota sobre el contenido, abajo; puede tener pestaña de búsqueda al final) | [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) |
| Navegar en iPad/Mac con jerarquía profunda | Sidebar (en iPad la tab bar puede convertirse en sidebar) | [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars), vídeo `2025-208` [2:52](https://developer.apple.com/videos/play/wwdc2025/208/?time=172) |
| Acciones sobre la vista actual | Toolbar, **nunca** la tab bar («Use a tab bar to support navigation, not to provide actions») | [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars), [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars) |
| Elegir entre pocas opciones exclusivas | Segmented control | [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls) |
| Activar/desactivar | Toggle | [Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles) |
| Valor continuo dentro de un rango | Slider | [Sliders](https://developer.apple.com/design/human-interface-guidelines/sliders) |
| Tarea acotada que interrumpe el flujo | Sheet (con atenuación si interrumpe) | [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets), vídeo `2025-356` [7:43](https://developer.apple.com/videos/play/wwdc2025/356/?time=463) |
| Información crítica que exige respuesta | Alert (úsalo con moderación) | [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) |
| Acciones contextuales sobre un elemento | Context menu / menú | [Context menus](https://developer.apple.com/design/human-interface-guidelines/context-menus), [Menus](https://developer.apple.com/design/human-interface-guidelines/menus) |
| Buscar | Search field (toolbar inferior preferida en iOS, pestaña Search en apps con pestañas) | [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields), vídeo `2026-292` |
| Datos estructurados escaneables | Lists and tables | [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables) |
| Muchos elementos visuales | Collections | [Collections](https://developer.apple.com/design/human-interface-guidelines/collections) |

Reglas transversales del sistema de diseño vigente (Liquid Glass): los componentes estándar adoptan el material
automáticamente; no añadas fondos ni bordes propios a los botones de barra (vídeo `2025-356`, [8:55](https://developer.apple.com/videos/play/wwdc2025/356/?time=535)); agrupa
elementos de barra por función y frecuencia; el botón primario (Done) va separado y tintado. Detalle en
`references/liquid-glass.md`.

---
