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
  X-Large (vídeo `2025-356`, 3:27–4:23).
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

1. **Estilo por defecto del scroll edge effect.** Vídeo `2025-356` (9-6-2025, 11:48): «Soft is the default and the
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

## Registro de cambios agregado de todas las páginas de las HIG

Generado a partir de las tablas «Change log» de 172 páginas. Más reciente primero.


### 2026

- **2026-10-13**
  - Live Activities (`hig/components/live-activities.md`): Added guidance for limited width layouts, and updated supported platforms and specifications.
  - Widgets (`hig/components/widgets.md`): Added guidance for Apple HomeView, and updated watchOS specifications.
- **2026-09-17**
  - Apple In-App Purchase (`hig/technologies/apple-in-app-purchase.md`): Rebranded as Apple In-App Purchase and refined guidance to reflect current best practices.
- **2026-09-09**
  - Branding (`hig/foundations/branding.md`): Refined guidance for using brand color.
  - Designing for iPhone Duo (`hig/getting-started/designing-for-iphone-duo.md`): New page. Introduces the fundamental concepts of designing for iPhone Duo, including device poses, dynamic layouts across dual displays, and toolbars and tab bars on the vertical axis.
  - Layout (`hig/foundations/layout.md`): Updated guidance to reflect current best practices.
  - SharePlay (`hig/technologies/shareplay.md`): Reorganized best practices, expanded visionOS guidance, and added a section on custom templates.
- **2026-06-08**
  - App Shortcuts (`hig/components/app-shortcuts.md`): Added guidance for adopting app schemas.
  - App icons (`hig/foundations/app-icons.md`): Refined guidance for Liquid Glass.
  - Apple Pay (`hig/technologies/apple-pay.md`): Refined guidance to reflect the latest Apple Pay appearance and capabilities.
  - Design principles (`hig/getting-started/design-principles.md`): Reintroduced design principles.
  - Generative AI (`hig/technologies/generative-ai.md`): Added guidance for letting people refine results and providing feedback during content generation, and updated guidance for choosing a model type.
  - Machine learning (`hig/technologies/machine-learning.md`): Made minor updates for clarity.
  - Menus (`hig/components/menus.md`): Updated guidance for menu item icons.
  - Scroll views (`hig/components/scroll-views.md`): Updated guidance for scroll edge effects.
  - Search fields (`hig/components/search-fields.md`): Updated terminology and refined guidance for search as a tab in iOS.
  - Searching (`hig/patterns/searching.md`): Updated terminology and refined best practices.
  - Sidebars (`hig/components/sidebars.md`): Updated guidance for sidebar icon colors, and clarified guidance for the adaptable sidebar style.
  - Siri (`hig/technologies/siri.md`): Revised for Siri AI.
  - Snippets (`hig/components/snippets.md`): New page.
  - Tab bars (`hig/components/tab-bars.md`): Updated terminology and art.
  - Wallet (`hig/technologies/wallet.md`): Updated to reflect guidance for iOS 27 and the Pass Designer app.
- **2026-03-24**
  - Scroll views (`hig/components/scroll-views.md`): Added guidance for Look to Scroll in visionOS.
  - Sheets (`hig/components/sheets.md`): Updated guidance for button placement.

### 2025

- **2025-12-16**
  - Apple Pay (`hig/technologies/apple-pay.md`): Clarified supported platforms, including web browsers and Apple Vision Pro.
  - Buttons (`hig/components/buttons.md`): Updated guidance for Liquid Glass.
  - Color (`hig/foundations/color.md`): Updated guidance for Liquid Glass.
  - Images (`hig/foundations/images.md`): Added guidance for spatial photos and spatial scenes in visionOS.
  - Live Activities (`hig/components/live-activities.md`): Updated guidance for all platforms, and added guidance for macOS and CarPlay.
  - Menus (`hig/components/menus.md`): Added guidance for presenting menus with breakthrough effects in visionOS.
  - Tab bars (`hig/components/tab-bars.md`): Updated guidance for Liquid Glass.
  - Toolbars (`hig/components/toolbars.md`): Updated guidance for Liquid Glass.
  - Typography (`hig/foundations/typography.md`): Added emphasized weights to the Dynamic Type style specifications for each platform.
  - Widgets (`hig/components/widgets.md`): Updated guidance for all platforms, and added guidance for visionOS and CarPlay.
  - Writing (`hig/foundations/writing.md`): Clarified guidance on language patterns, and added guidance for possessive pronouns.
- **2025-09-09**
  - Layout (`hig/foundations/layout.md`): Added specifications for iPhone 17, iPhone Air, iPhone 17 Pro, iPhone 17 Pro Max, Apple Watch SE 3, Apple Watch Series 11, and Apple Watch Ultra 3.
  - Materials (`hig/foundations/materials.md`): Updated guidance for Liquid Glass.
  - Motion (`hig/foundations/motion.md`): Added guidance for Liquid Glass.
- **2025-07-28**
  - Menus (`hig/components/menus.md`): Added guidance for representing menu items with icons.
  - SF Symbols (`hig/foundations/sf-symbols.md`): Updated with guidance for Draw animations and gradient rendering in SF Symbols 7.
  - Scroll views (`hig/components/scroll-views.md`): Added guidance for scroll edge effects.
  - Tab bars (`hig/components/tab-bars.md`): Added guidance for Liquid Glass.
- **2025-06-09**
  - Accessibility (`hig/foundations/accessibility.md`): Added guidance and links for Assistive Access, Switch Control, and Accessibility Nutrition Labels.
  - App Clips (`hig/technologies/app-clips.md`): Updated guidance to include demo App Clips.
  - App icons (`hig/foundations/app-icons.md`): Updated guidance to reflect layered icons, consistency across platforms, and best practices for Liquid Glass.
  - Buttons (`hig/components/buttons.md`): Updated guidance for button styles and content.
  - Color (`hig/foundations/color.md`): Updated system color values, and added guidance for Liquid Glass.
  - Designing for games (`hig/getting-started/designing-for-games.md`): Updated guidance for touch-based controls and Game Center.
  - Game Center (`hig/technologies/game-center.md`): Added guidance for new challenges and multiplayer activities, and considerations for the Apple Games app and Game Overlay. Updated guidance and specifications for activity preview images.
  - Game controls (`hig/inputs/game-controls.md`): Updated touch control best practices, updated game controller mapping for UI, and added guidance for spatial game controller support in visionOS.
  - Generative AI (`hig/technologies/generative-ai.md`): New page.
  - Going full screen (`hig/patterns/going-full-screen.md`): Updated guidance for hiding toolbars and navigation controls, and deferring Home Screen indicator gestures in full-screen iOS and iPadOS apps and games.
  - Icons (`hig/foundations/icons.md`): Added a table of SF Symbols that represent common actions.
  - Immersive experiences (`hig/foundations/immersive-experiences.md`): Clarified guidance and noted the availability of portrait-oriented progressive immersion.
  - Keyboards (`hig/inputs/keyboards.md`): Moved game-specific key bindings guidance to the Game controls page.
  - Layout (`hig/foundations/layout.md`): Added guidance for Liquid Glass.
  - Loading (`hig/patterns/loading.md`): Revised guidance for storing downloads to reflect downloading large assets in the background.
  - Materials (`hig/foundations/materials.md`): Added guidance for Liquid Glass.
  - Multitasking (`hig/patterns/multitasking.md`): Reorganized guidance in platform considerations, and added guidance for multitasking with multiple windows in iPadOS.
  - Search fields (`hig/components/search-fields.md`): Updated guidance for search placement in iOS, consolidated iPadOS and macOS platform considerations, and added guidance for tokens.
  - Searching (`hig/patterns/searching.md`): Updated best practices with general guidance from Search fields, and reorganized guidance for systemwide search.
  - Sidebars (`hig/components/sidebars.md`): Added guidance for extending content beneath the sidebar.
  - Split views (`hig/components/split-views.md`): Added iOS and iPadOS platform considerations.
  - The menu bar (`hig/components/the-menu-bar.md`): Added guidance for the menu bar in iPadOS.
  - Toolbars (`hig/components/toolbars.md`): Added guidance for grouping bar items, updated guidance for using symbols, and incorporated navigation bar guidance.
  - Virtual keyboards (`hig/components/virtual-keyboards.md`): Added guidance for displaying custom controls above the keyboard, and updated to reflect virtual keyboard availability in watchOS.
  - Windows (`hig/components/windows.md`): Added best practices, and updated with guidance for resizable windows in iPadOS.
  - iCloud (`hig/technologies/icloud.md`): Added guidance for synchronizing game data through iCloud.
- **2025-03-07**
  - Accessibility (`hig/foundations/accessibility.md`): Expanded and refined all guidance. Moved Dynamic Type guidance to the Typography page, and moved VoiceOver guidance to a new VoiceOver page.
  - Layout (`hig/foundations/layout.md`): Added specifications for iPhone 16e, iPad 11-inch, iPad Air 11-inch, and iPad Air 13-inch.
  - Typography (`hig/foundations/typography.md`): Expanded guidance for Dynamic Type.
  - VoiceOver (`hig/technologies/voiceover.md`): New page.
- **2025-01-17**
  - App Shortcuts (`hig/components/app-shortcuts.md`): Updated and streamlined guidance.
  - Wallet (`hig/technologies/wallet.md`): Added specifications for pass image dimensions.
  - Widgets (`hig/components/widgets.md`): Corrected watchOS widget dimensions.

### 2024

- **2024-12-18**
  - Maps (`hig/technologies/maps.md`): Added guidance for place cards and included additional artwork.
  - Wallet (`hig/technologies/wallet.md`): Added guidance for the poster event ticket style.
- **2024-11-19**
  - Immersive experiences (`hig/foundations/immersive-experiences.md`): Refined immersion style guidance and added artwork.
- **2024-09-09**
  - Camera Control (`hig/inputs/camera-control.md`): New page.
  - Gestures (`hig/inputs/gestures.md`): Added guidance for working with system overlays in visionOS and made organizational updates.
  - Layout (`hig/foundations/layout.md`): Added specifications for iPhone 16, iPhone 16 Plus, iPhone 16 Pro, iPhone 16 Pro Max, and Apple Watch Series 10.
  - Tab bars (`hig/components/tab-bars.md`): Added art representing the tab bar in iPadOS 18.
- **2024-08-06**
  - Dark Mode (`hig/foundations/dark-mode.md`): Added art contrasting the light and dark appearances.
  - Materials (`hig/foundations/materials.md`): Added platform-specific art.
  - Sidebars (`hig/components/sidebars.md`): Updated guidance to include the SwiftUI adaptable sidebar style.
  - Tab bars (`hig/components/tab-bars.md`): Updated with guidance for the tab bar in iPadOS 18.
- **2024-06-10**
  - Accessibility (`hig/foundations/accessibility.md`): Added a link to Apple’s Unity plug-ins for supporting Dynamic Type.
  - App icons (`hig/foundations/app-icons.md`): Added guidance for creating dark and tinted app icon variants for iOS and iPadOS.
  - Apple Pay (`hig/technologies/apple-pay.md`): Updated links to developer guidance for offering Apple Pay on the web.
  - Controls (`hig/components/controls.md`): New page.
  - Designing for games (`hig/getting-started/designing-for-games.md`): New page.
  - Eyes (`hig/inputs/eyes.md`): Added guidance for custom hover effects.
  - File management (`hig/patterns/file-management.md`): Added guidelines for using the document launcher in iOS and iPadOS.
  - Game controls (`hig/inputs/game-controls.md`): Added guidance for supporting touch controls and changed title from Game controllers.
  - Going full screen (`hig/patterns/going-full-screen.md`): Enhanced guidance for playing a game in full-screen mode.
  - Immersive experiences (`hig/foundations/immersive-experiences.md`): Added guidance for tinting passthrough and specifying initial, minimum, and maximum immersion levels.
  - Keyboards (`hig/inputs/keyboards.md`): Added game-specific guidance and made organizational updates.
  - Launching (`hig/patterns/launching.md`): Added guidance on displaying a splash screen.
  - Layout (`hig/foundations/layout.md`): Made minor corrections and organizational updates.
  - Live Activities (`hig/components/live-activities.md`): Added guidance for Live Activities in watchOS.
  - Loading (`hig/patterns/loading.md`): Added guidelines for showing progress and storing downloads, and enhanced guidance for games.
  - Menus (`hig/components/menus.md`): Added guidance for in-game menus and included game-specific examples.
  - Motion (`hig/foundations/motion.md`): Added game-specific examples and enhanced guidance for using motion in games.
  - Onboarding (`hig/patterns/onboarding.md`): Clarified different approaches to onboarding and added a guideline on displaying a splash screen.
  - SF Symbols (`hig/foundations/sf-symbols.md`): Updated with guidance for new animations and features of SF Symbols 6.
  - Settings (`hig/patterns/settings.md`): Reorganized some guidance into new topics and added game-specific examples.
  - Typography (`hig/foundations/typography.md`): Added guidance for using Apple’s Unity plug-ins to support Dynamic Type in a Unity-based game and enhanced guidance on billboarding in a visionOS app or game.
  - Widgets (`hig/components/widgets.md`): Updated to include guidance for accented widgets in iOS 18 and iPadOS 18.
  - Windows (`hig/components/windows.md`): Updated to include guidance for using volumes in visionOS 2 and added game-specific examples.
- **2024-05-07**
  - Apple Pencil and Scribble (`hig/inputs/apple-pencil-and-scribble.md`): Added guidance for handling squeeze and barrel roll on Apple Pencil Pro.
  - Immersive experiences (`hig/foundations/immersive-experiences.md`): Added guidance for creating an environment.
  - Playing haptics (`hig/patterns/playing-haptics.md`): Added guidance for playing haptics on Apple Pencil Pro.
  - Tap to Pay on iPhone (`hig/technologies/tap-to-pay-on-iphone.md`): Updated to include guidance on enabling the feature and educating merchants.
- **2024-03-29**
  - Activity rings (`hig/components/activity-rings.md`): Enhanced guidance for displaying Activity rings and listed specific colors for displaying related content.
  - Eyes (`hig/inputs/eyes.md`): Added artwork showing the visionOS hover effect.
  - Sheets (`hig/components/sheets.md`): Added guidance to use form or page sheet styles in iPadOS apps.
  - Spatial layout (`hig/foundations/spatial-layout.md`): Emphasized the importance of keeping interactive elements from overlapping each other.
  - Toggles (`hig/components/toggles.md`): Enhanced guidance for using switches in macOS apps, clarified when a checkbox has a title, and added artwork for radio buttons.
- **2024-02-02**
  - Alerts (`hig/components/alerts.md`): Enhanced guidance for using default and Cancel buttons.
  - Buttons (`hig/components/buttons.md`): Noted that visionOS buttons don’t support custom hover effects.
  - Color (`hig/foundations/color.md`): Distinguished UIKit and SwiftUI gray colors in iOS and iPadOS, and added guidance for balancing brightness levels in visionOS apps.
  - Designing for visionOS (`hig/getting-started/designing-for-visionos.md`): Included a link to Apple Vision Pro User Guide.
  - Game Center (`hig/technologies/game-center.md`): Added links to developer guidance on using the access point and dashboard in a visionOS game.
  - Immersive experiences (`hig/foundations/immersive-experiences.md`): Clarified guidance for choosing an immersion style that matches the experience your app provides.
  - Layout (`hig/foundations/layout.md`): Enhanced guidance for avoiding system controls in iPadOS app layouts, and added specifications for 10.9-inch iPad Air and 8.3-inch iPad mini.
  - Motion (`hig/foundations/motion.md`): Enhanced guidance for minimizing peripheral motion in visionOS apps.
  - Ornaments (`hig/components/ornaments.md`): Added guidance on using multiple ornaments.
  - Scroll views (`hig/components/scroll-views.md`): Added artwork showing the behavior of the visionOS scroll indicator.
  - Virtual keyboards (`hig/components/virtual-keyboards.md`): Clarified the virtual keyboard’s support for direct and indirect gestures in visionOS.
- **2024-01-31**
  - App icons (`hig/foundations/app-icons.md`): Clarified platform availability for alternate app icons.
- **2024-01-17**
  - Tap to Pay on iPhone (`hig/technologies/tap-to-pay-on-iphone.md`): Updated merchant education guidance.

### 2023

- **2023-12-05**
  - Accessibility (`hig/foundations/accessibility.md`): Updated visionOS Zoom lens artwork.
  - Activity rings (`hig/components/activity-rings.md`): Added artwork representing Activity rings in iOS.
  - Buttons (`hig/components/buttons.md`): Clarified some terminology and guidance for buttons in visionOS.
  - Collaboration and sharing (`hig/patterns/collaboration-and-sharing.md`): Added artwork illustrating button placement and various types of collaboration permissions.
  - Context menus (`hig/components/context-menus.md`): Added guidance on hiding unavailable menu items.
  - Digital Crown (`hig/inputs/digital-crown.md`): Added artwork for Apple Vision Pro and Apple Watch, and clarified that visionOS apps don’t receive direct information from the Digital Crown.
  - Images (`hig/foundations/images.md`): Clarified guidance on choosing a resolution for a rasterized image in a visionOS app.
  - Layout (`hig/foundations/layout.md`): Clarified guidance on centering content in a visionOS window.
  - Materials (`hig/foundations/materials.md`): Updated descriptions of the various material types, and clarified terms related to vibrancy and material thickness.
  - Modality (`hig/patterns/modality.md`): Enhanced guidance for in-depth modal experiences and clarified guidance on multiple modal views.
  - Multitasking (`hig/patterns/multitasking.md`): Added artwork for primary and auxiliary windows in iPadOS.
  - Offering help (`hig/patterns/offering-help.md`): Included visionOS in guidance for creating tooltips.
  - Ornaments (`hig/components/ornaments.md`): Removed a statement about using ornaments to present supplementary items.
  - Scroll views (`hig/components/scroll-views.md`): Described the visionOS scroll indicator and added guidance for integrating it with window layout.
  - SharePlay (`hig/technologies/shareplay.md`): Added artwork for visionOS.
  - Sheets (`hig/components/sheets.md`): Recommended using a split view to offer supplementary items in a visionOS app.
  - Sidebars (`hig/components/sidebars.md`): Added artwork for iPadOS.
  - Split views (`hig/components/split-views.md`): Added guidance for split views in visionOS.
  - Virtual keyboards (`hig/components/virtual-keyboards.md`): Added artwork for visionOS.
- **2023-10-24**
  - Complications (`hig/components/complications.md`): Replaced links to deprecated ClockKit documentation with links to WidgetKit documentation.
  - Drag and drop (`hig/patterns/drag-and-drop.md`): Added artwork.
  - Eyes (`hig/inputs/eyes.md`): Clarified the difference between focus effects and the visionOS hover effect.
  - Focus and selection (`hig/inputs/focus-and-selection.md`): Clarified the difference between focus effects and the visionOS hover effect.
  - Immersive experiences (`hig/foundations/immersive-experiences.md`): Updated artwork.
  - Live Activities (`hig/components/live-activities.md`): Expanded and updated guidance and added new artwork.
  - Machine learning (`hig/technologies/machine-learning.md`): Added art to Corrections section.
  - Notifications (`hig/components/notifications.md`): Updated watchOS platform considerations with guidance for presenting notification responses to double tap.
  - Pop-up buttons (`hig/components/pop-up-buttons.md`): Added artwork.
- **2023-09-15**
  - Gestures (`hig/inputs/gestures.md`): Updated specifications to include double tap in watchOS.
  - Layout (`hig/foundations/layout.md`): Added specifications for iPhone 15 Pro Max, iPhone 15 Pro, iPhone 15 Plus, iPhone 15, Apple Watch Ultra 2, and Apple Watch SE.
- **2023-09-12**
  - Action button (`hig/inputs/action-button.md`): Updated to include guidance for iOS.
  - Alerts (`hig/components/alerts.md`): Added anatomy artwork for visionOS.
  - Always On (`hig/technologies/always-on.md`): Updated intro image artwork.
  - Apple In-App Purchase (`hig/technologies/apple-in-app-purchase.md`): Updated artwork and guidance for redeeming offer codes.
  - Apple Pay (`hig/technologies/apple-pay.md`): Updated artwork.
  - Apple Pencil and Scribble (`hig/inputs/apple-pencil-and-scribble.md`): Updated artwork.
  - Color (`hig/foundations/color.md`): Enhanced guidance for using background color in watchOS views, and added color swatches for tvOS.
  - Designing for visionOS (`hig/getting-started/designing-for-visionos.md`): Updated intro artwork.
  - Game Center (`hig/technologies/game-center.md`): Added artwork for the iOS achievement layout.
  - ID Verifier (`hig/technologies/id-verifier.md`): New page.
  - Maps (`hig/technologies/maps.md`): Added artwork.
  - Offering help (`hig/patterns/offering-help.md`): Added guidance for creating tips.
  - Playing video (`hig/patterns/playing-video.md`): Corrected the recommended width for a thumbnail in visionOS.
  - Progress indicators (`hig/components/progress-indicators.md`): Combined guidance common to all platforms.
  - Ratings and reviews (`hig/patterns/ratings-and-reviews.md`): Added artwork.
  - ResearchKit (`hig/technologies/researchkit.md`): Updated artwork.
  - Search fields (`hig/components/search-fields.md`): Combined guidance common to all platforms.
  - Toggles (`hig/components/toggles.md`): Updated artwork.
  - Typography (`hig/foundations/typography.md`): Added artwork illustrating system font weights, and clarified tvOS specification table descriptions.
  - Wallet (`hig/technologies/wallet.md`): Added guidance for helping people add orders to Wallet.
- **2023-06-21**
  - Accessibility (`hig/foundations/accessibility.md`): Updated to include guidance for visionOS.
  - Alerts (`hig/components/alerts.md`): Updated to include guidance for visionOS.
  - App icons (`hig/foundations/app-icons.md`): Updated to include guidance for visionOS.
  - Buttons (`hig/components/buttons.md`): Updated to include guidance for visionOS.
  - Collaboration and sharing (`hig/patterns/collaboration-and-sharing.md`): Updated to include guidance for visionOS.
  - Color (`hig/foundations/color.md`): Updated to include guidance for visionOS.
  - Context menus (`hig/components/context-menus.md`): Updated to include guidance for visionOS.
  - Designing for visionOS (`hig/getting-started/designing-for-visionos.md`): New page.
  - Digital Crown (`hig/inputs/digital-crown.md`): Updated to include guidance for visionOS.
  - Drag and drop (`hig/patterns/drag-and-drop.md`): Updated to include guidance for visionOS.
  - Edit menus (`hig/components/edit-menus.md`): Updated to include guidance for visionOS.
  - Entering data (`hig/patterns/entering-data.md`): Updated to include guidance for visionOS.
  - Eyes (`hig/inputs/eyes.md`): New page.
  - File management (`hig/patterns/file-management.md`): Updated to include guidance for visionOS.
  - Focus and selection (`hig/inputs/focus-and-selection.md`): Updated to include guidance for visionOS.
  - Gestures (`hig/inputs/gestures.md`): Changed page title from Touchscreen gestures and updated to include guidance for visionOS.
  - Icons (`hig/foundations/icons.md`): Updated to include guidance for visionOS.
  - Image views (`hig/components/image-views.md`): Updated to include guidance for visionOS.
  - Images (`hig/foundations/images.md`): Updated to include guidance for visionOS.
  - Immersive experiences (`hig/foundations/immersive-experiences.md`): New page.
  - Keyboards (`hig/inputs/keyboards.md`): Updated to include guidance for visionOS.
  - Launching (`hig/patterns/launching.md`): Updated to include guidance for visionOS.
  - Layout (`hig/foundations/layout.md`): Updated to include guidance for visionOS.
  - Lists and tables (`hig/components/lists-and-tables.md`): Updated to include guidance for visionOS.
  - Materials (`hig/foundations/materials.md`): Updated to include guidance for visionOS.
  - Menus (`hig/components/menus.md`): Updated to include guidance for visionOS.
  - Modality (`hig/patterns/modality.md`): Updated to include guidance for visionOS.
  - Motion (`hig/foundations/motion.md`): Updated to include guidance for visionOS.
  - Multitasking (`hig/patterns/multitasking.md`): Updated to include guidance for visionOS.
  - Nearby interactions (`hig/inputs/nearby-interactions.md`): Changed page title from Spatial interactions.
  - Onboarding (`hig/patterns/onboarding.md`): Updated to include guidance for visionOS.
  - Ornaments (`hig/components/ornaments.md`): New page.
  - Page controls (`hig/components/page-controls.md`): Updated to include guidance for visionOS.
  - Playing audio (`hig/patterns/playing-audio.md`): Updated to include guidance for visionOS.
  - Playing haptics (`hig/patterns/playing-haptics.md`): Updated to include guidance for visionOS.
  - Playing video (`hig/patterns/playing-video.md`): Updated to include guidance for visionOS.
  - Pointing devices (`hig/inputs/pointing-devices.md`): Updated to include guidance for visionOS.
  - Privacy (`hig/foundations/privacy.md`): Consolidated guidance into new page and updated for visionOS.
  - Segmented controls (`hig/components/segmented-controls.md`): Updated to include guidance for visionOS.
  - SharePlay (`hig/technologies/shareplay.md`): Updated to include guidance for visionOS.
  - Sheets (`hig/components/sheets.md`): Updated to include guidance for visionOS.
  - Sidebars (`hig/components/sidebars.md`): Updated to include guidance for visionOS.
  - Sliders (`hig/components/sliders.md`): Updated to include guidance for visionOS.
  - Spatial layout (`hig/foundations/spatial-layout.md`): New page.
  - Tab bars (`hig/components/tab-bars.md`): Updated to include guidance for visionOS.
  - Toolbars (`hig/components/toolbars.md`): Updated to include guidance for visionOS.
  - Typography (`hig/foundations/typography.md`): Updated to include guidance for visionOS.
  - Virtual keyboards (`hig/components/virtual-keyboards.md`): Changed page title from Onscreen keyboards and updated to include guidance for visionOS.
  - Windows (`hig/components/windows.md`): Updated to include guidance for visionOS.
- **2023-06-05**
  - App Shortcuts (`hig/components/app-shortcuts.md`): New page.
  - Buttons (`hig/components/buttons.md`): Updated guidance for using buttons in watchOS.
  - Color (`hig/foundations/color.md`): Updated guidance for using background color in watchOS.
  - Complications (`hig/components/complications.md`): Updated guidance for rectangular complications to support them as widgets in the Smart Stack.
  - Designing for watchOS (`hig/getting-started/designing-for-watchos.md`): Enhanced guidance for providing a glanceable, focused app experience, and emphasized the importance of the Digital Crown in navigation.
  - Digital Crown (`hig/inputs/digital-crown.md`): Added guidelines emphasizing the central role of the Digital Crown for navigation.
  - Labels (`hig/components/labels.md`): Updated guidance to reflect changes in watchOS 10.
  - Lists and tables (`hig/components/lists-and-tables.md`): Updated guidance to reflect changes in watchOS 10.
  - Live Activities (`hig/components/live-activities.md`): Updated guidance to include features of iOS 17 and iPadOS 17.
  - Materials (`hig/foundations/materials.md`): Added guidance on using materials to provide context and orientation in watchOS apps.
  - Page controls (`hig/components/page-controls.md`): Updated guidance for using page controls in watchOS.
  - Pickers (`hig/components/pickers.md`): Updated guidance for using pickers in watchOS.
  - Progress indicators (`hig/components/progress-indicators.md`): Updated guidance to reflect changes in watchOS 10.
  - SF Symbols (`hig/foundations/sf-symbols.md`): Added a new section on animations. Included animation guidance for custom symbols.
  - Scroll views (`hig/components/scroll-views.md`): Updated guidance for using scroll views in watchOS.
  - Search fields (`hig/components/search-fields.md`): Added guidance for using search fields in watchOS.
  - Sheets (`hig/components/sheets.md`): Updated guidance for using sheets in watchOS.
  - Siri (`hig/technologies/siri.md`): Removed Add to Siri guidance. Added references to the new [App Shortcuts](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts) page.
  - Split views (`hig/components/split-views.md`): Added guidance for split views in watchOS.
  - Tab views (`hig/components/tab-views.md`): Added guidance for using tab views in watchOS.
  - Text fields (`hig/components/text-fields.md`): Updated guidance to reflect changes in watchOS 10.
  - Text views (`hig/components/text-views.md`): Updated guidance to reflect changes in watchOS 10.
  - Toolbars (`hig/components/toolbars.md`): Updated guidance for using toolbars in watchOS.
  - Widgets (`hig/components/widgets.md`): Updated guidance to include widgets in watchOS, widgets on the iPad Lock Screen, and updates for iOS 17, iPadOS 17, and macOS 14.
- **2023-05-02**
  - AirPlay (`hig/technologies/airplay.md`): Consolidated guidance into one page.
  - App Clips (`hig/technologies/app-clips.md`): Consolidated guidance into one page.
  - Apple Pay (`hig/technologies/apple-pay.md`): Consolidated guidance into one page.
  - CarPlay (`hig/technologies/carplay.md`): Consolidated guidance into one page.
  - CareKit (`hig/technologies/carekit.md`): Consolidated guidance into one page.
  - Game Center (`hig/technologies/game-center.md`): Consolidated guidance into one page.
  - HomeKit (`hig/technologies/homekit.md`): Consolidated guidance into one page.
  - Mac Catalyst (`hig/technologies/mac-catalyst.md`): Consolidated guidance into one page.
  - Machine learning (`hig/technologies/machine-learning.md`): Consolidated guidance into one page.
  - Siri (`hig/technologies/siri.md`): Consolidated guidance into one page.
  - iMessage apps and stickers (`hig/technologies/imessage-apps-and-stickers.md`): Consolidated guidance into one page.
- **2023-03-03**
  - Tap to Pay on iPhone (`hig/technologies/tap-to-pay-on-iphone.md`): Enhanced guidance for educating merchants and improving their experience.
- **2023-02-27**
  - Writing (`hig/foundations/writing.md`): New page.
- **2023-02-20**
  - Wallet (`hig/technologies/wallet.md`): Enhanced guidance for presenting order-tracking information and added artwork.

### 2022

- **2022-12-19**
  - Color (`hig/foundations/color.md`): Corrected RGB values for system mint color (Dark Mode) in iOS and iPadOS.
  - SharePlay (`hig/technologies/shareplay.md`): Clarified guidance for helping nonsubscribers join a group activity.
- **2022-11-30**
  - Wallet (`hig/technologies/wallet.md`): Added guidance to include a carrier name in status information for a shipping fulfillment.
- **2022-11-03**
  - Apple In-App Purchase (`hig/technologies/apple-in-app-purchase.md`): Added a guideline for displaying the total billing price for every in-app purchase item and consolidated guidance into one page.
  - Apple Pencil and Scribble (`hig/inputs/apple-pencil-and-scribble.md`): Added guidelines for using hover to enhance your app.
  - Live Activities (`hig/components/live-activities.md`): Updated artwork and specifications.
  - Widgets (`hig/components/widgets.md`): Added guidance for widgets on the iPhone Lock Screen and updated design comprehensives for iPhone 14, iPhone 14 Pro, and iPhone 14 Pro Max.
- **2022-09-23**
  - Always On (`hig/technologies/always-on.md`): Expanded guidance to cover the Always On display on iPhone 14 Pro and iPhone 14 Pro Max.
  - Charting data (`hig/patterns/charting-data.md`): New page.
  - Charts (`hig/components/charts.md`): New page.
  - Gauges (`hig/components/gauges.md`): New page.
  - Live Activities (`hig/components/live-activities.md`): New page.
  - Maps (`hig/technologies/maps.md`): Added guidelines for presenting custom information, refined best practices, and consolidated guidance into one page.
  - Rating indicators (`hig/components/rating-indicators.md`): New page.
- **2022-09-14**
  - Action button (`hig/inputs/action-button.md`): New page.
  - App icons (`hig/foundations/app-icons.md`): Added specifications for Apple Watch Ultra.
  - Collaboration and sharing (`hig/patterns/collaboration-and-sharing.md`): New page.
  - Complications (`hig/components/complications.md`): Added specifications for Apple Watch Ultra.
  - Context menus (`hig/components/context-menus.md`): Refined guidance on including a submenu and added a guideline on using a context menu to support object creation in an iPadOS app.
  - Designing for tvOS (`hig/getting-started/designing-for-tvos.md`): Refined best practices for multiuser support.
  - Edit menus (`hig/components/edit-menus.md`): Added guidance on supporting both edit-menu styles in iPadOS.
  - Images (`hig/foundations/images.md`): Added specifications for Apple Watch Ultra.
  - Layout (`hig/foundations/layout.md`): Added specifications for iPhone 14 Pro Max, iPhone 14 Pro, iPhone 14 Plus, iPhone 14, and Apple Watch Ultra.
  - Menus (`hig/components/menus.md`): Added guidelines for using the small, medium, and large menu layouts in iPadOS.
  - Pop-up buttons (`hig/components/pop-up-buttons.md`): Added a guideline on using a pop-up button in a popover or modal view in iPadOS.
  - Pull-down buttons (`hig/components/pull-down-buttons.md`): Refined guidance on designing a useful menu length.
  - SF Symbols (`hig/foundations/sf-symbols.md`): Added a new section on variable color. Removed instructions on creating custom symbol paths, exporting templates, and layering paths, deferring to developer articles that cover these topics.
  - Sign in with Apple (`hig/technologies/sign-in-with-apple.md`): Refined guidance on supporting existing accounts, helping people set up a new account, and indicating the current sign-in status. Consolidated guidance into one page.
  - Tap to Pay on iPhone (`hig/technologies/tap-to-pay-on-iphone.md`): Refined guidance on preparing Tap to Pay on iPhone and helping merchants learn how to use the feature.
  - Wallet (`hig/technologies/wallet.md`): Added guidelines for using Verify with Wallet, updated guidance on providing shipping status values and descriptions, and consolidated guidance into one page.
