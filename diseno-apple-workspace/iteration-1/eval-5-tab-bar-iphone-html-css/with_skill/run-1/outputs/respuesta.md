# Tab bar para una app de recetas (iPhone) — diseño + HTML/CSS

**Archivo:** `index.html` (un solo archivo, sin dependencias externas). Ábrelo en el navegador con un ancho de móvil
(o en Safari de iPhone).

**Plataforma asumida:** iPhone con iOS 27 y el lenguaje visual **Liquid Glass**, que llegó con la versión 26
(9-6-2025). La página de Apple [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars)
se actualizó por última vez el 8-6-2026 (terminología e ilustraciones).

> **Si la app es nativa**, no copies esta maqueta: usa `TabView` (SwiftUI) o `UITabBar` (UIKit). Así tienes
> Liquid Glass de verdad, la pestaña de búsqueda, el accesorio, la minimización y la accesibilidad sin escribir
> código. El HTML de abajo es una **aproximación web** de ese comportamiento.

Leyenda del origen de cada decisión:
- **[Apple]**: regla literal de las HIG, citada en inglés.
- **[Vídeo]**: sesión de Apple, con la marca de tiempo enlazada.
- **[Web]**: algo propio de la plataforma web (WebKit/W3C), no de Apple.
- **[Propio]**: decisión mía, en un punto en el que Apple no publica valores.

---

## 1. Arquitectura: 5 destinos, ninguna acción

| # | Pestaña | Icono (propio) | Qué contiene |
|---|---|---|---|
| 1 | **Hoy** | Sol | Sugerencias de temporada y recetas recientes |
| 2 | **Recetas** | Libro abierto | Recetario guardado. El botón **+ Añadir receta** está en su cabecera |
| 3 | **Plan** | Calendario | Planificador semanal. Se ve el estado vacío, con explicación y siguiente paso |
| 4 | **Compra** | Cesta | Lista de la compra compartida. Lleva un badge «2» con artículos nuevos de otra persona |
| 5 | **Buscar** | Lupa | Pestaña de búsqueda, al final, con sugerencias |

Por qué:

- **Solo navegación.** «Use a tab bar to support navigation, not to provide actions.» [Apple, [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars)].
  Lo más tentador habría sido una pestaña «+ Nueva receta». La quité y puse la acción en la cabecera de *Recetas*,
  que es exactamente el ejemplo que corrige Apple en [Design foundations from idea to interface, 6:01](https://developer.apple.com/videos/play/wwdc2025/359/?time=361):
  «tabs are for navigation, not for taking action» [Vídeo].
- **Pocas pestañas.** «Use the appropriate number of tabs required to help people navigate your app.» y «Avoid
  overflow tabs.» [Apple]. Cada pestaña de más es «one more decision for people to make» ([2025-359, 5:22](https://developer.apple.com/videos/play/wwdc2025/359/?time=322)) [Vídeo].
  Por eso funciones como «Favoritos» o «Colecciones» van dentro de *Recetas*, no en pestañas propias.
- **Búsqueda como pestaña al final.** En iOS, «A tab bar can include a dedicated search tab at the trailing end.»
  [Apple, Tab bars › iOS]. Elegí el estilo **standard tab** (igual que las demás pestañas) y no el *button
  appearance*, porque en una app de recetas buscar también sirve para descubrir: «Choose the standard tab style to
  provide suggestions, promote discovery, and encourage exploration.» [Apple, [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields), 8-6-2026].
  Dentro hay un texto de ejemplo y sugerencias: «Use placeholder text…», «Consider showing suggested search terms.» [Apple].
- **La pestaña vacía sigue ahí.** *Plan* está vacía, pero no se oculta ni se desactiva: «Don’t disable or hide tab bar
  buttons, even when their content is unavailable.» y «If a section is empty, explain why its content is unavailable.»
  [Apple, Tab bars]. La pantalla explica por qué está vacía y ofrece el botón «Planificar la semana».
- **Siempre visible.** «Make sure the tab bar is visible when people navigate to different sections of your app.»
  [Apple]. Al cambiar de sección, la barra no desaparece.

## 2. Etiquetas e iconos

- **Todas las pestañas llevan etiqueta.** «Include tab labels to help with navigation.» [Apple]. Los nombres son
  cortos y dicen lo que hay dentro («Compra», no «Lista de la compra»). Eso sigue lo que pide Apple: «make sure
  the tab bar uses clear symbols and labels that match what is inside each tab» ([Design with SwiftUI, 4:50](https://developer.apple.com/videos/play/meet-with-apple/270/?time=290)) [Vídeo].
- **Iconos:**
  - En nativo, usa SF Symbols: «Consider using SF Symbols to provide familiar, scalable tab bar icons.» [Apple]. Para
    la lupa, la tabla de acciones comunes de [Icons](https://developer.apple.com/design/human-interface-guidelines/icons)
    asocia *Search* a `magnifyingglass`.
  - En la web los iconos son **SVG propios**. En las fuentes de Apple no hay permiso para usar SF Symbols en webs, y la
    licencia prohíbe imágenes «confusingly similar» en ciertos usos ([SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols)).
    Los míos usan una rejilla de 24×24, trazo de 1,8 px con extremos redondeados y `currentColor` [Propio, inspirado en SF Symbols].
- **Fuente:** `-apple-system, system-ui…`. En un dispositivo Apple sale San Francisco, que ya está instalada, sin
  incrustar SF Pro. Su licencia prohíbe usarla para «website content» ([Fonts](https://developer.apple.com/fonts/)) [Apple].

## 3. Forma, material y capas (Liquid Glass)

- **Flota abajo, sobre el contenido.** «A tab bar floats above content at the bottom of the screen.» [Apple, Tab bars › iOS].
  El contenido pasa por debajo, igual que en Layout: el contenido a pantalla completa se extiende bajo las barras.
- **Cápsula con margen respecto al borde.** «For phone layouts, use a capsule with extra margin to create space near
  the screen edge.» ([Get to know the new design system, 5:48](https://developer.apple.com/videos/play/wwdc2025/356/?time=348)) [Vídeo].
  El fondo de la pestaña seleccionada también es una cápsula, concéntrica con la barra ([3:42](https://developer.apple.com/videos/play/wwdc2025/356/?time=222)).
  Hay 16 px de margen lateral y 8 px sobre la *safe area* [Propio]: Apple no publica un margen numérico para iOS.
- **Liquid Glass solo en la capa funcional:**
  - Solo la barra y su accesorio llevan cristal. Las tarjetas y las listas no: «Don’t use Liquid Glass in the content
    layer.» [Apple, [Materials](https://developer.apple.com/design/human-interface-guidelines/materials)].
  - Variante *regular*, la de por defecto. *Clear* queda fuera: solo vale sobre medios y con atenuación.
- **Nada de cristal sobre cristal.** El botón de pausa del accesorio no tiene fondo ni cristal propio, y la pestaña
  seleccionada usa un relleno gris, no otra capa de vidrio. Apple dice «always avoid glass on glass» ([Meet Liquid Glass, 13:24](https://developer.apple.com/videos/play/wwdc2025/219/?time=804))
  y «hierarchy should be expressed through layout and grouping» ([2025-356, 8:55](https://developer.apple.com/videos/play/wwdc2025/356/?time=535)) [Vídeo].
- **Cómo se imita en CSS** [Web, según la guía web de la skill]:
  - `backdrop-filter: blur() saturate()`, con un filtro SVG de refracción que solo aplica Chromium. Safari se queda
    con el esmerilado.
  - Un borde especular hecho con sombras `inset`.
  - La sombra exterior va en una **capa hermana**: en el mismo elemento rompe el filtro de refracción.
- **Opacidad del vidrio al 84 %** [Propio]. El Liquid Glass de verdad cambia entre claro y oscuro según el fondo, y
  CSS no puede hacerlo. Subí la opacidad para que las etiquetas sigan siendo legibles aunque pase una foto debajo.
- **Scroll edge effect inferior en vez de un fondo sólido.** Es un degradado con desenfoque bajo la barra. Solo existe
  porque hay UI flotante encima: «Only use a scroll edge effect when a scroll view is behind floating interface
  elements» y «Prefer the automatic scroll edge effect style» [Apple, [Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views), 8-6-2026].
  Hay uno por vista ([2025-356, 11:28](https://developer.apple.com/videos/play/wwdc2025/356/?time=688)).
  En CSS es una aproximación del estilo *automatic*.

## 4. Accesorio de la tab bar: temporizador de cocina

- **Por qué un temporizador.** Encima de la barra va la receta en curso («Risotto de setas · Paso 4 · 12:00»), con
  pausa. Es el equivalente del MiniPlayer de Música para una app de cocina: una función **persistente**, útil en
  cualquier pestaña. Apple pide no poner ahí acciones de una sola pantalla: «Avoid placing screen-specific actions
  here—a checkout button, for example, belongs with the content it supports.» ([2025-356, 10:40](https://developer.apple.com/videos/play/wwdc2025/356/?time=640)) [Vídeo].
- **Minimización.** Al hacer scroll hacia abajo, la barra se reduce a la pestaña activa y el accesorio se coloca a su
  lado. Al subir, o al tocar la barra, vuelve a expandirse. Es lo que Apple prevé para barras con accesorio: «you can
  choose to minimize the tab bar and move the accessory inline with it when a person scrolls down.» [Apple, Tab bars › iOS].
  Si no hay accesorio, no hay motivo para minimizar.

## 5. Color y contraste

**Etiquetas monocromas; color solo en la selección.**

- [Apple, [Color › Liquid Glass color](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color)]:
  - Toolbars y tab bars usan por defecto símbolos y texto monocromos.
  - «Apply color sparingly to the Liquid Glass material, and to symbols or text on the material.»
- La pestaña activa usa el acento porque es un color con significado: la selección
  ([Communicate your brand identity on iOS, 10:01](https://developer.apple.com/videos/play/wwdc2026/251/?time=601)) [Vídeo].

**La marca vive en el contenido.**

- Las fotos de los platos y la tarjeta destacada ponen el color. La barra no lleva fondo de marca: «move color into
  the content area of your app, into the scroll view» ([2026-251, 9:42](https://developer.apple.com/videos/play/wwdc2026/251/?time=582)) [Vídeo].
- Un ejemplo real del mismo vídeo es NYT Cooking ([16:03](https://developer.apple.com/videos/play/wwdc2026/251/?time=963)).

**Acento verde «albahaca» y contenido en tonos cálidos.** Apple dice «Avoid applying a similar color to tab labels
and content layer backgrounds.» [Apple, Tab bars]. Las fotos de comida son rojas, naranjas y ocres, así que el acento
es verde, para que la etiqueta seleccionada no se pierda sobre ellas.

**Por qué un verde propio y no `systemGreen`.**

- Los colores de sistema no llegan al contraste mínimo con texto de 11 pt sobre vidrio claro. Lo calculé con la
  fórmula WCAG:
  - systemGreen #34C759: ≈ 2,2:1 sobre blanco.
  - systemOrange #FF8D28: ≈ 2,3:1.
  - systemBlue #0088FF: ≈ 3,5:1.
- Apple pide 4,5:1 para texto de hasta 17 pt ([Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility))
  y, con colores propios, aspirar a 7:1 en texto pequeño ([Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode)) [Apple].
- Así que el acento es propio, con sus 4 variantes [Propio]:

| Modo | Acento | Contraste de la etiqueta seleccionada (texto 11 px en negrita sobre su fondo) |
|---|---|---|
| Claro | `#0E6B34` | 5,3:1 sobre vidrio claro (≈ 4,1:1 en el peor caso, con una foto muy oscura justo debajo) |
| Oscuro | `#5EDC7B` | 6,6:1 (≈ 4,4:1 en el peor caso, con una foto muy clara debajo) |
| Alto contraste claro | `#0A4F25` | 7,8:1, y el vidrio pasa a opaco |
| Alto contraste oscuro | `#8FF0A4` | 8,4:1, y el vidrio pasa a opaco |

Notas sobre el contraste:

- La etiqueta seleccionada va en **negrita**. Para texto en negrita, el mínimo de Apple es 3:1 («All · Bold · 3:1»
  [Apple, Accessibility]), así que incluso el peor caso lo cumple con margen.
- La negrita y el fondo gris de la cápsula indican la selección además del color: «Convey information with more
  than color alone.» [Apple].
- Las etiquetas sin seleccionar usan el color de etiqueta primario sobre el vidrio, con más de 12:1.

**Badge.**

- «Use a badge to indicate that critical information is available.» [Apple]. Solo hay un badge: avisa de artículos
  nuevos añadidos por otra persona a la lista compartida, y desaparece al abrir *Compra*.
- Es blanco sobre systemRed (#FF383C en claro, #FF4245 en oscuro, valores de [Color › Specifications](https://developer.apple.com/design/human-interface-guidelines/color#Specifications)),
  con el número en negrita: ≈ 3,6:1 y 3,4:1, por encima del 3:1 que pide Apple para texto en negrita.
- No uso un badge para cosas que no son críticas, como el número total de artículos.

**Colores semánticos.** Apple **no publica** los RGB de `label`, `systemBackground`, `separator`, etc. Los valores
CSS que uso para ellos son una aproximación [Propio]. En nativo usa las API (`Color.primary`…): «Avoid hard-coding
system color values in your app.» [Apple].

## 6. Tamaños, tipografía y Dynamic Type

- **Destino táctil.** Cada pestaña mide unos 71×54 px en un iPhone de 393 px, y unos 56×54 px a 320 px. Siempre
  supera los **44×44 pt** que Apple da como tamaño por defecto en iOS [Apple, Accessibility]. Los botones del
  accesorio y de la cabecera también miden 44×44.
- **Etiquetas de 11 px, semibold.** Es el **tamaño mínimo de texto en iOS** (17 por defecto, 11 mínimo) [Apple,
  [Typography](https://developer.apple.com/design/human-interface-guidelines/typography)]. **Apple no publica el
  tamaño de la etiqueta de la tab bar ni la altura de la barra en iOS** (solo da la altura en tvOS, 68 pt). Los
  valores que uso (11 px, barra de unos 62 px) son míos [Propio].
- **Dynamic Type:**
  - El contenido escala con el tamaño de texto del sistema: `html { font: -apple-system-body }` en WebKit, y todo
    en `rem` [Web]. Los estilos son los de la tabla Large de la HIG: Large Title 34/41, Title 3 20/25, Body 17/22,
    Subhead 15/20.
  - La barra **no crece**, como la nativa. En los tamaños de accesibilidad, mantener pulsada una pestaña muestra el
    icono y la etiqueta en grande. Es un equivalente del **Large Content Viewer**: «if you choose to implement
    custom bars or views, consider adopting the large content viewer» ([Get started with Dynamic Type, 13:05](https://developer.apple.com/videos/play/wwdc2024/10074/?time=785)) [Vídeo].
  - Se activa cuando el cuerpo de texto llega a 28 pt, el Body de AX1 en la tabla de la HIG. Para probarlo en un
    ordenador, añade `?ax` a la URL [Propio].

## 7. Accesibilidad y preferencias del sistema

| Preferencia | Qué hace la maqueta | Fuente |
|---|---|---|
| VoiceOver | `<nav aria-label="Secciones">`; los enlaces llevan su etiqueta visible y `aria-current="page"`; el badge se anuncia como «2 artículos nuevos»; los SVG son `aria-hidden` | «Describe your app’s interface and content for VoiceOver.» [Apple, Accessibility] |
| Dark Mode | Variantes oscuras de todos los tokens | [Apple, Color / Dark Mode] |
| Increase Contrast (`prefers-contrast: more`) | Colores de alto contraste de la HIG; vidrio opaco con borde de 2 px | «makes elements predominantly black or white and highlights them with a contrasting border» ([2025-219, 18:22](https://developer.apple.com/videos/play/wwdc2025/219/?time=1102)) |
| Reduce Transparency | Sin desenfoque; vidrio opaco | «makes Liquid Glass frostier…» (mismo vídeo) |
| Reduce Motion | Sin transiciones ni animación de aparición; el scroll a la parte superior es instantáneo | «…disables any elastic properties» (mismo vídeo) |
| Teclado | Foco visible de 3 px en el color de acento | [Web] |
| Windows, contraste alto (`forced-colors`) | Bordes de sistema visibles | [Web] |
| Safe areas | `viewport-fit=cover` + `env(safe-area-inset-bottom)` | [Apple, Layout › Guides and safe areas] + [Web] |

## 8. Comportamientos de la maqueta que son decisión mía

Ninguno de estos comportamientos aparece en las fuentes; son decisiones mías [Propio]:

- Cada pestaña guarda su posición de scroll.
- Tocar la pestaña activa vuelve arriba.
- La barra minimizada se expande al tocarla.

## 9. Checklist de revisión

| Punto | Estado |
|---|---|
| La tab bar solo navega; la acción «Añadir» está en la cabecera de su pantalla | ✅ |
| Ninguna pestaña oculta o desactivada; la vacía explica por qué | ✅ |
| Etiquetas en todas las pestañas e iconos claros; búsqueda al final | ✅ |
| Liquid Glass solo en la capa funcional, sin cristal sobre cristal, sin fondos extra en los botones de la barra | ✅ |
| Color solo en la selección y en el badge; la marca está en el contenido | ✅ |
| Contraste ≥ 4,5:1 en el caso normal y ≥ 3:1 (negrita) en el peor caso | ✅ |
| Destinos ≥ 44×44 pt; texto ≥ 11 pt | ✅ |
| Reduce Transparency, Increase Contrast, Reduce Motion y Dark Mode atendidos | ✅ (probado en Chromium sin cabeza a 393 y 320 px, en claro y oscuro; Safari/WebKit no estaba disponible para probar) |
| Sin SF Pro incrustada, sin SF Symbols en la web, sin logotipos de Apple | ✅ |

## 10. Lo que Apple no publica

| Dato | Qué hice |
|---|---|
| Altura de la tab bar en iOS y tamaño de su etiqueta | 54 px por pestaña y 11 px de etiqueta [Propio] |
| Radios de esquina numéricos | Cápsulas (radio = mitad de la altura) y formas concéntricas, la regla publicada |
| RGB de los colores semánticos (`label`, `systemBackground`…) | Aproximación marcada como tal |
| Márgenes numéricos de iOS | 16 px laterales [Propio] |
| Liquid Glass para la web | Apple no publica nada; el CSS es una imitación y no tiene el *lensing* adaptativo real |
