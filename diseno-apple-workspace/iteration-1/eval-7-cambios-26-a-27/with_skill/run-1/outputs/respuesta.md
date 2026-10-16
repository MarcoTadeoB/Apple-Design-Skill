# Qué cambió en el diseño de Apple entre la versión 26 y la 27

## Respuesta corta

La 27 **no es un rediseño**. El gran cambio visual fue la **26** (9-6-2025), que introdujo **Liquid Glass**. Las
plataformas 27 (iOS, iPadOS, macOS, watchOS, tvOS y visionOS 27, presentadas el **8-6-2026**) mantienen ese
lenguaje visual y hacen tres cosas:

1. **Pulen la guía de Liquid Glass**: iconos de app (Icon Composer 2), scroll edge effects (ahora se recomienda
   `automatic`), búsqueda como pestaña en iOS, sidebars, iconos en menús y botones de las sheets.
2. **Añaden contenido nuevo**: vuelven los **Design principles** (8 principios), nueva página **Snippets**, Siri
   revisado para **Siri AI** y una guía completa para **iPhone Duo**, el primer iPhone plegable (9-9-2026).
3. **Actualizan las herramientas**: Icon Composer 2, SF Symbols 8 beta / «SF Symbols 27», Pass Designer (nuevo),
   Reality Composer Pro 3 y kits de diseño de iOS/iPadOS 27 y macOS 27.

> Cómo se ha hecho la comparación: a partir de los registros de cambios («Change log») de cada página de las HIG,
> de [What's new](https://developer.apple.com/design/whats-new/) y de los vídeos de la WWDC26. No tengo el texto
> anterior de cada página, así que comparo **lo que Apple declara haber cambiado** con **la guía vigente**
> (descarga del 15-10-2026). Si Apple no dice qué cambió en concreto, lo indico.

---

## 1. Punto de partida: qué trajo la versión 26 (9-6-2025)

Así se entiende mejor qué se ha refinado después:

| Área | Novedad de la 26 |
|---|---|
| Material | **Liquid Glass** para la capa funcional (controles y navigación) que flota sobre el contenido; variantes *regular* y *clear* |
| Color | «Updated system color values» en claro, oscuro y alto contraste ([Color](https://developer.apple.com/design/human-interface-guidelines/color), 9-6-2025) |
| Iconos de app | Iconos por capas; apariencias default, dark, clear y tinted; nueva app Icon Composer |
| Forma | Formas concéntricas (fija, cápsula, concéntrica) |
| Barras | Elementos de barra agrupados, pestaña de búsqueda en iOS, accesorio de la tab bar, *scroll edge effects* en lugar de separadores |
| iPadOS | Nuevo sistema de ventanas y barra de menús en todas las apps |
| SF Symbols 7 | Draw On/Off, Variable Draw, degradados |

Después hubo ajustes dentro del ciclo 26: Materials y Motion (9-9-2025) y, el 16-12-2025, guía de Liquid Glass
revisada en Color, Buttons, Toolbars y Tab bars, más pesos *emphasized* en las tablas de Dynamic Type.

---

## 2. Qué cambió con la versión 27

### 2.1 Cambios publicados antes de la WWDC26 (24-3-2026, todavía en el ciclo 26)

| Página | Qué dice ahora |
|---|---|
| [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets): «Updated guidance for button placement» | En iOS/iPadOS, en una sheet con una sola vista, **Cancel va en el borde inicial (leading) de la toolbar superior** y Done en el final. Regla: **«Provide an alternative to the Done button.»** Además, «Avoid showing all three buttons — Cancel, Done, and Back — together». En flujos de varios pasos, Back sustituye a Cancel, y Back «isn’t intended to dismiss a sheet». |
| [Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views): Look to Scroll (visionOS) | Guía nueva para el desplazamiento con la mirada: actívalo en vistas de lectura o exploración, no en contenido secundario. |

### 2.2 WWDC26: 8-6-2026 (llegada de las plataformas 27)

**Fundamentos**

- **Design principles: vuelven a las HIG** («Reintroduced design principles»). Son ocho:
  **Purpose** («Make something meaningful.»), **Agency** («Let people do things their own way.»),
  **Responsibility** («Act in people’s best interest.»), **Familiarity** («Build on what people know.»),
  **Flexibility** («Adapt to diverse contexts and needs.»), **Simplicity** («Be clear and direct.»),
  **Craft** («Care about every detail.») y **Delight** («Make it human.») —
  [Design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles).
  Los explica el vídeo *Principles of great design* (WWDC26-250). Dos ideas útiles:
  «When we say simple, we don't mean minimal.» ([11:20](https://developer.apple.com/videos/play/wwdc2026/250/?time=680))
  y, sobre la IA, «Think about what it means to responsibly add AI capabilities to your product.»
  ([5:10](https://developer.apple.com/videos/play/wwdc2026/250/?time=310)).

**Liquid Glass refinado (componentes y materiales)**

| Página | Cambio declarado por Apple | Guía vigente (resumen o cita) |
|---|---|---|
| [App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons) | «Refined guidance for Liquid Glass» | Aparece con **Icon Composer 2**: **refracción** por capa, nuevos **specular highlights** (dentro, fuera o automático; luz vertical desde arriba) y anotación por modo **Default, Dark y Mono** ([Icon Composer](https://developer.apple.com/icon-composer/)). Regla de la HIG: «Prefer vector graphics when bringing layers into Icon Composer.» |
| [Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views) | «Updated guidance for scroll edge effects» | **«Prefer the automatic scroll edge effect style.»** Si usas *soft*, prueba la legibilidad a fondo. Se mantienen «Only use a scroll edge effect when a scroll view is behind floating interface elements» y «Apply one scroll edge effect per view». **Este es el cambio de criterio más claro respecto a la 26** (ver §3). |
| [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields) y [Searching](https://developer.apple.com/design/human-interface-guidelines/searching) | «Updated terminology and refined guidance for search as a tab in iOS» | Hay dos estilos de pestaña Search: **Standard tab** («Choose the standard tab style to provide suggestions, promote discovery, and encourage exploration.») y **Button appearance** («Choose the button appearance to help people quickly find what they need.»). Fuera de la tab bar: «Place search at the bottom if there’s room.» Vídeo *Design intuitive search experiences* (WWDC26-292): la toolbar inferior es la posición preferida en iOS ([3:22](https://developer.apple.com/videos/play/wwdc2026/292/?time=202)) y en apps con pestañas conviene una pestaña Search como entrada principal ([5:32](https://developer.apple.com/videos/play/wwdc2026/292/?time=332)). |
| [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) | «Updated terminology and art» | Apple no detalla nada más; el cambio de nombres coincide con el de la búsqueda como pestaña. |
| [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars) | «Updated guidance for sidebar icon colors, and clarified guidance for the adaptable sidebar style» | **«Make sure any sidebar icon colors you choose serve a clear purpose.»** En resumen: por defecto, los iconos usan el color de acento; en macOS deben respetar el acento que elija la persona; los colores fijos se usan con moderación (p. ej., el VIP amarillo de Mail). Para el estilo adaptable (`sidebarAdaptable`): «Consider using a tab bar first.» |
| [Menus](https://developer.apple.com/design/human-interface-guidelines/menus) | «Updated guidance for menu item icons» | **«Use menu item icons sparingly and with purpose.»** y «Represent common actions consistently.» Es un cambio de tono: en la 26 (28-7-2025) se añadió la guía para poner iconos en los menús y en la 27 se pide moderación (el contraejemplo de Apple es un menú de días de la semana con un símbolo distinto en cada uno). |

**Inteligencia y sistema**

- [Siri](https://developer.apple.com/design/human-interface-guidelines/siri): «Revised for Siri AI». Siri AI es
  «a version of Siri powered by Apple Intelligence».
- [Snippets](https://developer.apple.com/design/human-interface-guidelines/snippets) (**página nueva**): vistas
  compactas con el resultado o la confirmación de una acción hecha con Siri, Spotlight o App Shortcuts. Hay
  dos tipos (confirmation y result) y la vista propia mide como máximo **400 pt** de alto. Reglas: «Ensure
  legibility.» y «Keep content concise.»
- [App Shortcuts](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts): guía para adoptar
  *app schemas*.
- [Generative AI](https://developer.apple.com/design/human-interface-guidelines/generative-ai): guía nueva para
  que la gente refine los resultados y dé su opinión durante la generación. También se actualiza cómo elegir el
  tipo de modelo. [Machine learning](https://developer.apple.com/design/human-interface-guidelines/machine-learning)
  solo recibe aclaraciones menores.

**Pagos y Wallet**

- [Wallet](https://developer.apple.com/design/human-interface-guidelines/wallet): «Updated to reflect guidance
  for iOS 27 and the Pass Designer app».
- [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay): «Refined guidance to
  reflect the latest Apple Pay appearance and capabilities».

### 2.3 Después de la WWDC26

| Fecha | Página | Cambio |
|---|---|---|
| 9-9-2026 | [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo) (**página nueva**) | Primer iPhone plegable, con dos pantallas. Trae *device poses*, *reserved regions* (cámara exterior, cámara interior y zona de pliegue), *arrangement views* (split y overlay) y **controles en el eje vertical**: toolbars, tab bars y navegación pasan al lateral. Reglas: «Build your app to resize.», «Follow the system’s vertical layout for toolbars, tab bars, and navigation controls.», «Avoid extreme layout changes as people fold the device.», «In general, don’t override the default bar placement.» |
| 9-9-2026 | [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) | «Updated guidance to reflect current best practices». **Desaparecen las tablas de tamaños de pantalla por dispositivo**, que estaban en la página hasta la 26 (la última se añadió el 9-9-2025 con el iPhone 17). |
| 9-9-2026 | [Branding](https://developer.apple.com/design/human-interface-guidelines/branding) | «Refined guidance for using brand color». Regla: «Apply your app’s accent color judiciously.» En el ejemplo correcto de Apple, el color de marca está **en la capa de contenido** y no en todos los controles. El vídeo WWDC26-251 recomienda «move color into the content area of your app, into the scroll view» ([9:42](https://developer.apple.com/videos/play/wwdc2026/251/?time=582)). |
| 9-9-2026 | [SharePlay](https://developer.apple.com/design/human-interface-guidelines/shareplay) | Buenas prácticas reorganizadas, más guía de visionOS y nueva sección sobre plantillas propias. |
| 17-9-2026 | [Apple In-App Purchase](https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase) | Cambio de nombre («Rebranded as Apple In-App Purchase») y guía actualizada. |
| 18-9-2026 | Design Resources | Marcos de dispositivo para iPhone Duo y los iPhone 18. |
| 13-10-2026 | [Widgets](https://developer.apple.com/design/human-interface-guidelines/widgets) | Guía para **Apple HomeView** (Home Screen y esfera Modular) y especificaciones de watchOS actualizadas. |
| 13-10-2026 | [Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities) | **«Support limited width presentations.»** Las presentaciones compact y minimal deben caber «inside a 28pt-diameter circle» (p. ej., la Dynamic Island con el iPhone en horizontal). |

### 2.4 Herramientas

| Herramienta | 26 | 27 |
|---|---|---|
| SF Symbols | SF Symbols 7 (Draw, Variable Draw, degradados) | What's new la anunció como «SF Symbols 8 beta», pero la página y Design Resources descargan `SF-Symbols-27.dmg`. Trae **Enhanced Search** (búsqueda semántica), **Annotation** y símbolos nuevos para las plataformas 27. Más de 7.000 símbolos. |
| Icon Composer | 1.ª versión | **Icon Composer 2 (beta)**: refracción, nuevos specular highlights, Default/Dark/Mono. Requiere **macOS Tahoe 26.4** o posterior. |
| Pass Designer | — | **Nueva** app del Mac para crear y previsualizar pases de Wallet (beta, macOS 27). |
| Reality Composer Pro | — | **Reality Composer Pro 3** (beta, macOS 26.5), con juegos sin código y scripting visual. |
| Kits de diseño | iOS/iPadOS 26, macOS 26 | Sketch de iOS/iPadOS 27 y macOS 27 el 8-6-2026; Figma el 23-6 y el 17-9-2026. |

---

## 3. Contradicciones entre la 26 y la 27 (cuál prevalece)

1. **Estilo por defecto del scroll edge effect.** En el vídeo *Get to know the new design system* (WWDC25-356,
   9-6-2025, hacia el [11:48](https://developer.apple.com/videos/play/wwdc2025/356/?time=708)) Apple decía: «Soft
   is the default and the one you'll use in most cases». La HIG del 8-6-2026 dice «Prefer the automatic scroll edge
   effect style». **Prevalece la de 2026: usa `automatic`.**
2. **Tamaños de pantalla por dispositivo.** Los vídeos antiguos y Layout hasta 2025 los daban; la página vigente
   ya no. **No los cites como guía actual.**
3. **Barras en iPhone Duo.** Todo lo de la 26 da por hecho que las barras van arriba o abajo. En iPhone Duo van al
   lateral, salvo en la pantalla interior en vertical. **Aplica esta guía solo a ese dispositivo.**
4. **Nombre de SF Symbols** («8 beta» frente a «27»): cita los dos.
5. **Requisito de Icon Composer**: Design Resources aún dice «macOS Sequoia or later»; la página de Icon
   Composer 2 dice **macOS Tahoe 26.4**. Prevalece la página de la herramienta.

## 4. Lo que no consta que haya cambiado en la 27

En los registros de cambios desde el 8-6-2026 **no aparecen** las páginas de Color, Typography, Materials,
Motion, Buttons ni Toolbars. Por tanto, los **valores RGB de los colores de sistema** (actualizados en la 26), las
**tablas de Dynamic Type** (con pesos *emphasized* desde el 16-12-2025), los tamaños mínimos de control y las
reglas básicas de Liquid Glass (regular por defecto, nada de cristal sobre cristal, color solo en lo primario)
**siguen siendo los de la 26**.

## 5. Qué revisar si tu app está diseñada para la 26 (interpretación propia)

Esta lista es mía y sale de los cambios anteriores. No es una checklist oficial de Apple.

- [ ] Cambiar los scroll edge effects *soft* por `automatic`, salvo que hayas comprobado la legibilidad.
- [ ] Revisar las sheets: Cancel a la izquierda y Done a la derecha, nunca Done solo, y nunca Cancel + Done + Back juntos.
- [ ] Si la app tiene pestañas, decidir si la pestaña Search usa el estilo *standard tab* (para explorar) o *button appearance* (para buscar rápido).
- [ ] Quitar de los menús los iconos que no aporten significado.
- [ ] Sidebars: que los iconos usen el color de acento (en macOS, el que elija la persona) y que los colores fijos tengan un motivo.
- [ ] Sacar el color de marca de las barras y llevarlo al contenido.
- [ ] Rehacer el icono en Icon Composer 2 para aprovechar la refracción y los nuevos brillos.
- [ ] Preparar la app para iPhone Duo: redimensionable, controles verticales del sistema y arrangement views si encajan.
- [ ] Live Activities: que compact y minimal quepan en un círculo de 28 pt.
- [ ] Si usas Siri o App Shortcuts, diseñar Snippets (vista de 400 pt de alto como máximo).

---

**Fuentes principales:** registros de cambios de las HIG enlazadas arriba;
[What's new](https://developer.apple.com/design/whats-new/); vídeos WWDC26
[250](https://developer.apple.com/videos/play/wwdc2026/250/), [251](https://developer.apple.com/videos/play/wwdc2026/251/)
y [292](https://developer.apple.com/videos/play/wwdc2026/292/); WWDC25
[356](https://developer.apple.com/videos/play/wwdc2025/356/); páginas de
[SF Symbols](https://developer.apple.com/sf-symbols/), [Icon Composer](https://developer.apple.com/icon-composer/),
[Pass Designer](https://developer.apple.com/pass-designer/) y
[Reality Composer Pro](https://developer.apple.com/reality-composer-pro/). Datos descargados el 15-10-2026; último
cambio registrado en las HIG: 13-10-2026.
