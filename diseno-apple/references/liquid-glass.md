# Liquid Glass — guía completa

Fuentes principales: HIG [Materials](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass)
(9-9-2025), [Color › Liquid Glass color](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color)
(16-12-2025), [Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views) (8-6-2026),
[Layout](https://developer.apple.com/design/human-interface-guidelines/layout), y los vídeos *Meet Liquid Glass*
(`videos/2025-219.md`) y *Get to know the new design system* (`videos/2025-356.md`). Para HTML/CSS ver `web.md`.

## 1. Qué es

- Material dinámico que **unifica el lenguaje de diseño** de todas las plataformas desde la versión 26 (9-6-2025)
  y sigue vigente en la 27.
- Forma una **capa funcional** para controles y navigación (tab bars, toolbars, sidebars…) que **flota sobre la
  capa de contenido**: «Liquid Glass forms a distinct functional layer for controls and navigation elements… that
  floats above the content layer» (Materials).
- Óptica: no dispersa la luz como los materiales anteriores, la **dobla y concentra** (*lensing*). Movimiento:
  se comporta como un líquido ligero; «Instead of fading, Liquid Glass objects materialize in and out by gradually
  modulating the light bending and lensing» ([2025-219, 2:55](https://developer.apple.com/videos/play/wwdc2025/219/?time=175)).
- Capas del material: reflejos (luces que se mueven con la interacción y, a veces, con el movimiento del dispositivo),
  sombra que se adapta (más opaca sobre texto, menos sobre fondo claro liso), brillo interior al tocar
  ([2025-219, 11:04](https://developer.apple.com/videos/play/wwdc2025/219/?time=664)).
- Tamaño: al crecer (p. ej. un menú que sale de un botón) simula un material más grueso: sombras más profundas,
  lensing más marcado, dispersión más suave ([2025-219, 7:02](https://developer.apple.com/videos/play/wwdc2025/219/?time=422)).
- Elementos pequeños (nav bars, tab bars) **alternan entre claro y oscuro** según el fondo; los grandes (menús,
  sidebars) se adaptan pero **no cambian** de claro a oscuro ([2025-219, 15:16](https://developer.apple.com/videos/play/wwdc2025/219/?time=916)).
  En sidebars el material es más opaco para preservar la legibilidad (Color › Liquid Glass color).

## 2. Cuándo SÍ y cuándo NO

| ✅ Sí | ❌ No |
|---|---|
| Controles y navigation de la capa funcional (lo hacen solos los componentes estándar) | «Don’t use Liquid Glass in the content layer» (Materials) — p. ej. una table view o el fondo de la app |
| Controles propios **muy importantes**, con moderación: «Limit these effects to the most important functional elements in your app» | Muchos controles propios con cristal: «overusing this material in multiple custom controls can provide a subpar user experience» |
| Controles transitorios en la capa de contenido **mientras se interactúa** (sliders, toggles): «the element takes on a Liquid Glass appearance… when a person activates it» | **Cristal sobre cristal**: «always avoid glass on glass» ([2025-219, 13:24](https://developer.apple.com/videos/play/wwdc2025/219/?time=804)); encima usa rellenos, transparencia y vibrancy |
| Vistas de controles sobre el teclado si el resto de la app usa Liquid Glass (Virtual keyboards) | Fondos o bordes añadidos a botones de barra: «hierarchy should be expressed through layout and grouping» ([2025-356, 8:55](https://developer.apple.com/videos/play/wwdc2025/356/?time=535)) |
| | En reposo, contenido cruzándose con el cristal: reposiciónalo o escálalo ([2025-219, 17:54](https://developer.apple.com/videos/play/wwdc2025/219/?time=1074)) |

En controles propios, aplica el material **al control, no a sus vistas internas** ([2025-356, 7:18](https://developer.apple.com/videos/play/wwdc2025/356/?time=438)).

## 3. Variantes: regular y clear

| | Regular | Clear |
|---|---|---|
| Qué hace | «blurs and adjusts the luminosity of background content to maintain legibility» | «highly translucent», prioriza ver el contenido de debajo |
| Comportamiento | Todos los efectos adaptativos | **Sin** comportamientos adaptativos; permanentemente más transparente ([2025-219, 14:16](https://developer.apple.com/videos/play/wwdc2025/219/?time=856)) |
| Uso | Por defecto; la mayoría de componentes del sistema; cuando el fondo puede dar problemas de legibilidad o hay mucho texto (alerts, sidebars, popovers) | Solo componentes que flotan sobre **medios** (fotos, vídeo) |
| Atenuación | No necesita | Si el contenido es brillante: «consider adding a dark dimming layer of 35% opacity»; no hace falta si el contenido es oscuro o usas controles de AVKit con su propia atenuación |
| API SwiftUI | [`Glass.regular`](https://developer.apple.com/documentation/swiftui/glass/regular) | [`Glass.clear`](https://developer.apple.com/documentation/swiftui/glass/clear) |

**Regla de las 3 condiciones para clear** ([2025-219, 14:50](https://developer.apple.com/videos/play/wwdc2025/219/?time=890)):
1) el elemento está sobre contenido rico en medios; 2) la capa de contenido tolera una capa de atenuación;
3) el contenido encima del cristal es llamativo y brillante. Si falta una, usa **regular**.
Nunca mezcles regular y clear: «They should never be mixed».
Con elementos pequeños puedes usar **atenuación localizada** para conservar la viveza del contenido.

Las variantes cambian con los ajustes del sistema: el aspecto preferido de Liquid Glass elegido por la persona,
Reduce Transparency e Increase Contrast (Materials).

## 4. Color y tintado

Fuente: [Color › Liquid Glass color](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color).

- Por defecto el cristal **no tiene color**: toma el del contenido de detrás.
- Puedes tintar algunos elementos (aspecto de vidrio de color): útil para la llamada a la acción principal; es lo
  que hace el estilo de botón prominente (p. ej. **Done**, con el color de acento de la app de fondo).
- «**Apply color sparingly to the Liquid Glass material, and to symbols or text on the material.**» Resérvalo para
  indicadores de estado o acciones primarias; para enfatizar una acción primaria, colorea el **fondo**, no el
  símbolo o el texto. «Refrain from adding color to the background of multiple controls.»
- Toolbars y tab bars: por defecto, símbolos y texto **monocromos** (más oscuros sobre contenido claro, más claros
  sobre oscuro). Evita un color de etiquetas parecido al del contenido (Buttons, Toolbars, Tab bars).
- El tintado nativo genera una gama de tonos según el brillo de lo que hay detrás, como un vidrio de color real;
  un relleno sólido «breaks the visual character of Liquid Glass» ([2025-219, 16:31](https://developer.apple.com/videos/play/wwdc2025/219/?time=991) y [17:03](https://developer.apple.com/videos/play/wwdc2025/219/?time=1023)).
- Marca: lleva el color al **contenido**, que pasa bajo los controles y estos lo recogen dinámicamente
  (Branding, 9-9-2026; vídeo `2026-251`, [9:42](https://developer.apple.com/videos/play/wwdc2026/251/?time=582)).
- Aunque tu app tenga una sola apariencia, define colores claro y oscuro: «provide both light and dark colors to
  support Liquid Glass adaptivity» (Color).

## 5. Separación del contenido: scroll edge effects y extensión de fondo

- Usa un **scroll edge effect** en vez de un fondo sólido o semiopaco bajo los controles (Layout).
- «Prefer the automatic scroll edge effect style» (Scroll views, 8-6-2026). *Automatic* da una separación más
  opaca para toolbars superiores con muchos controles, texto fuera de controles de cristal y cabeceras de tabla
  fijadas. Si usas *soft*, prueba la legibilidad a fondo. (Esto **sustituye** lo dicho en el vídeo de 2025 de que
  *soft* era el estilo por defecto; ver `novedades.md`.)
- «Only use a scroll edge effect when a scroll view is behind floating interface elements» — no es decorativo.
- Un scroll edge effect **por vista**; en Split View, uno por panel con la misma altura ([2025-356, 12:25](https://developer.apple.com/videos/play/wwdc2025/356/?time=745)).
- Sidebars: flotan en la capa de cristal; extiende el contenido rico por debajo con scroll horizontal o con
  **background extension effect** (`backgroundExtensionEffect()`, `UIBackgroundExtensionView`), que refleja y
  desenfoca el contenido adyacente. Texto y controles van por encima (Sidebars; Layout).
- Contenido a pantalla completa: extiéndelo bajo sidebars, toolbars y tab bars (Layout).

## 6. Formas

- Controles en formas redondeadas y flotantes que anidan con las esquinas del hardware; concentricidad:
  fija, cápsula (radio = mitad de la altura), concéntrica (radio = radio padre − padding) ([2025-356, 3:42](https://developer.apple.com/videos/play/wwdc2025/356/?time=222)).
- Las HIG no publican radios numéricos (ver `tokens.md` §8).

## 7. Accesibilidad

Con el material del sistema, las adaptaciones son **automáticas** ([2025-219, 18:22](https://developer.apple.com/videos/play/wwdc2025/219/?time=1102)):

| Ajuste | Efecto en Liquid Glass |
|---|---|
| Reduce Transparency | «makes Liquid Glass frostier and obscures more of the content behind it» |
| Increase Contrast | «makes elements predominantly black or white and highlights them with a contrasting border» |
| Reduce Motion | «decreases the intensity of some effects and disables any elastic properties» |

- En iPhone Duo, con Reduce Transparency la barra vertical tiene fondo ([2026-tech-talks-111462, 10:57](https://developer.apple.com/videos/play/tech-talks/111462/?time=657)).
- Comprueba Dark Mode con Increase Contrast y Reduce Transparency, juntos y por separado: puede haber texto oscuro
  poco legible sobre fondo oscuro ([Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)).
- Contraste mínimo y tamaños: `tokens.md` §4 y §6.

## 8. Por plataforma

- **iOS/iPadOS**: tab bar flotante abajo (iPadOS: arriba); accesorio de la tab bar para funciones persistentes;
  pestaña Search al final. Además de Liquid Glass, siguen los materiales estándar `ultraThin`, `thin`,
  `regular` y `thick` para la capa de contenido.
- **macOS**: controles Mini/Small/Medium en rectángulo redondeado; Large y X-Large en cápsula (vídeo `2025-356`, [4:23](https://developer.apple.com/videos/play/wwdc2025/356/?time=263)).
  Al perder el foco una ventana, el cristal se atenúa ([2025-219, 12:37](https://developer.apple.com/videos/play/wwdc2025/219/?time=757)).
- **tvOS**: Liquid Glass en la navegación y en experiencias del sistema (Top Shelf, Control Center); imágenes y
  botones lo adoptan al recibir el foco (Materials › tvOS).
- **visionOS**: las ventanas usan el material *glass* del sistema, no modificable; no hay Dark Mode; prefiere
  translucidez a colores opacos (Materials › visionOS).
- **Iconos de app**: material de cristal propio con reflejos especulares, refracción y translucidez; se diseña en
  Icon Composer (`references/hig/foundations/app-icons.md`, vídeos `2025-220`, `2025-361`).
- **Widgets**: apariencias *clear* (desatura y añade el material) y *tinted* (`hig/components/widgets.md`).

## 9. API (para desarrolladores)

- SwiftUI: [`glassEffect(_:in:)`](https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)),
  [Applying Liquid Glass to custom views](https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views),
  `backgroundExtensionEffect()`.
- UIKit: `UIVisualEffectView`, `UIBackgroundExtensionView`. AppKit: `NSVisualEffectView`.
- Guía general: [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass).

## 10. Checklist rápida de Liquid Glass

- [ ] ¿Solo la capa funcional usa cristal? ¿Nada de cristal en listas, tarjetas o fondos?
- [ ] ¿Sin cristal sobre cristal?
- [ ] ¿Regular por defecto; clear solo sobre medios y con atenuación (35 % si el fondo es brillante)?
- [ ] ¿Color solo en la acción primaria o en estados, y aplicado al fondo del control?
- [ ] ¿Sin fondos/bordes propios en botones de barra; elementos agrupados por función?
- [ ] ¿Scroll edge effect *automatic*, uno por vista, solo bajo UI flotante?
- [ ] ¿Probado con Reduce Transparency, Increase Contrast, Reduce Motion y Dark Mode?
