# Checklist para revisar un diseño según las HIG

Cómo usarla: recorre las secciones que apliquen, marca cada punto como ✅ / ⚠️ / ❌ y, para cada problema,
**cita la regla literal y su página** (las frases en inglés entre «» son de Apple). Al final de este archivo hay
un apéndice generado con **todas las reglas negativas** («Avoid…», «Don’t…», «Never…») de cada página, para
buscar con Ctrl+F.

## Formato de informe recomendado

| # | Severidad | Dónde | Problema | Regla de Apple (cita) | Fuente | Arreglo |
|---|---|---|---|---|---|---|
| 1 | Alta | Tab bar | La pestaña «Añadir» ejecuta una acción | «Use a tab bar to support navigation, not to provide actions.» | [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) | Mover «Añadir» a la toolbar de la pantalla |

Severidad: **Alta** = rompe accesibilidad, navegación o una regla explícita «Don’t/Never»; **Media** = contradice una
recomendación («Prefer…», «Consider…»); **Baja** = pulido. Si una observación no está respaldada por una fuente,
márcala como «opinión» o no la incluyas.

## 1. Plataforma y estructura

- [ ] ¿Responde cada pantalla a «¿dónde estoy?, ¿qué puedo hacer?, ¿adónde puedo ir?» — vídeo `2025-359`.
- [ ] ¿Se usan los patrones de la plataforma de destino (iOS, iPadOS, macOS, watchOS, tvOS, visionOS)? —
  `hig/getting-started/designing-for-*.md`.
- [ ] ¿La navegación principal usa tab bar (iPhone) o sidebar (iPad/Mac con jerarquía profunda)? — Tab bars, Sidebars.
- [ ] ¿La tab bar solo navega? «Use a tab bar to support navigation, not to provide actions.» — Tab bars.
- [ ] ¿Ninguna pestaña está oculta o desactivada? «Don’t disable or hide tab bar buttons, even when their content is
  unavailable.» — Tab bars.
- [ ] ¿Cada pestaña tiene etiqueta? «Include tab labels to help with navigation.» — Tab bars.
- [ ] ¿La pantalla tiene título y solo las acciones esenciales en la toolbar? — vídeo `2025-359`.
- [ ] ¿Se usa progressive disclosure en lugar de mostrarlo todo? — Layout.
- [ ] ¿Funcionalidad igual en todos los tamaños? «Keep functionality the same as size classes change» — Layout.
- [ ] iPhone Duo (si aplica): controles en el lateral, nada interactivo en el pliegue, mismas funciones en todas las
  posturas — `hig/getting-started/designing-for-iphone-duo.md`.

## 2. Componentes estándar

- [ ] ¿Se usan componentes del sistema en vez de réplicas propias de tareas convencionales? — vídeo `2026-251`.
- [ ] Botones: destino ≥ 44×44 pt (60×60 en visionOS); estilo, no tamaño, para distinguir la opción preferida; rol
  primario nunca en una acción destructiva — Buttons.
- [ ] Alerts: solo información crítica y, a ser posible, accionable — Feedback, Alerts.
- [ ] Sheets (iOS/iPadOS): Cancel en el borde inicial, Done en el final; si hay Done, hay Cancel o Back; nunca
  Cancel, Done y Back juntos — Sheets (24-3-2026).
- [ ] Modales: solo con beneficio claro, cortos y con forma obvia de cerrarlos — Modality.
- [ ] Menús: no se ocultan elementos según el contexto (se atenúan); iconos con moderación — Menus; vídeo `2025-208`.
- [ ] Búsqueda en el sitio adecuado (toolbar inferior / pestaña Search en iOS; toolbar o sidebar en iPad/Mac),
  recientes, sugerencias y estado vacío — Search fields, Searching; vídeo `2026-292`.

## 3. Liquid Glass y materiales

- [ ] Liquid Glass solo en la capa funcional; nunca en contenido («Don’t use Liquid Glass in the content layer»).
- [ ] Sin cristal sobre cristal; sin fondos/bordes extra en botones de barra; elementos agrupados por función.
- [ ] Regular por defecto; clear solo sobre medios, con atenuación del 35 % si el fondo es brillante.
- [ ] Color solo en acciones primarias o estados, en el fondo del control; no en todos los controles.
- [ ] Scroll edge effect *automatic*, uno por vista y solo bajo UI flotante; nada de fondos sólidos bajo las barras.
- [ ] Detalle: `liquid-glass.md` §10.

## 4. Color

- [ ] ¿Colores de sistema o colores propios con variantes claro, oscuro y alto contraste? — Color.
- [ ] ¿Ningún dato depende solo del color? «Convey information with more than color alone.» — Accessibility.
- [ ] ¿Contraste ≥ 4.5:1 (≤ 17 pt) / 3:1 (≥ 18 pt o negrita)? — Accessibility; `tokens.md` §4.
- [ ] ¿No se redefine el significado de los colores semánticos (p. ej. separator como texto)? — Color.
- [ ] ¿El color de marca vive en el contenido, no en las barras? — Branding; vídeo `2026-251`.

## 5. Tipografía

- [ ] ¿Estilos de texto del sistema / Dynamic Type? «Consider using the built-in text styles.» — Typography.
- [ ] ¿Tamaños ≥ mínimos (iOS 17 pt por defecto, 11 pt mínimo; macOS 13/10; tvOS 29/23; visionOS 17/12;
  watchOS 16/12)? — Typography; `tokens.md` §5.1.
- [ ] ¿Se evitan pesos finos? «In general, avoid light font weights.» — Typography.
- [ ] ¿Pocas familias tipográficas? «Minimize the number of typefaces you use» — Typography.
- [ ] ¿El diseño aguanta los tamaños de accesibilidad sin cortar texto? — Typography › Supporting Dynamic Type.
- [ ] ¿Las fuentes propias implementan Dynamic Type? — Typography; vídeo `2026-251`.

## 6. Layout y adaptabilidad

- [ ] ¿Se respetan safe areas y márgenes del sistema? — Layout › Guides and safe areas.
- [ ] ¿Contenido ordenado por importancia, alineado y agrupado? — Layout › Visual hierarchy.
- [ ] ¿Decisiones por size class, no por dispositivo u orientación? — Layout.
- [ ] ¿El fondo a pantalla completa se extiende bajo barras y sidebars? — Layout.
- [ ] macOS: nada crítico en la parte inferior de la ventana — Layout › macOS.
- [ ] tvOS: margen de 60 pt arriba/abajo y 80 pt a los lados — Layout › tvOS.

## 7. Accesibilidad

- [ ] Controles ≥ tamaño por defecto (iOS 44×44 pt; mínimo 28×28) y separación (~12 pt con bisel, ~24 sin) —
  Accessibility; `tokens.md` §6.
- [ ] Etiquetas de VoiceOver en todo elemento interactivo; controles propios con valor, acciones y respuesta —
  Accessibility; vídeo `2026-220`.
- [ ] Alternativas a gestos complejos; navegación con teclado; Switch Control y Voice Control.
- [ ] Respeta Reduce Motion, Reduce Transparency e Increase Contrast; prueba Dark Mode + Increase Contrast.
- [ ] Subtítulos/transcripciones para audio y vídeo; sin destellos rápidos.

## 8. Iconos y símbolos

- [ ] Icono de app por capas, simple, sin texto salvo esencial, sin réplicas de hardware de Apple, con apariencias
  dark/clear/tinted coherentes — App icons; vídeos `2025-220`, `2025-361`.
- [ ] Mismos símbolos para las mismas acciones; texto si no hay un símbolo inequívoco — vídeo `2025-356`.
- [ ] Metáforas estándar (papelera = borrar…) — vídeo `2026-250`; `hig/foundations/icons.md`.
- [ ] SF Symbols no usados en logotipos ni iconos de app — SF Symbols.

## 9. Escritura

- [ ] Sin relleno («simply», «quickly», «Oops»), sin repeticiones, beneficio delante — vídeo `2025-404`.
- [ ] Mismo nombre para la misma cosa en toda la app (lista de palabras) — vídeo `2025-404`; Writing.
- [ ] Mensajes de error claros y con siguiente paso; pantallas vacías con siguiente paso — Writing.
- [ ] Nombres de funciones claros para la persona, no para la tecnología — vídeo `2026-290`.

## 10. Privacidad, permisos y responsabilidad

- [ ] Permisos solo cuando hacen falta, no al abrir la app, con texto que explique el uso — Privacy.
- [ ] Nada de pantallas propias engañosas antes de la alerta del sistema — Privacy.
- [ ] Funciones de IA con salvaguardas (vista previa, confirmación, avisos) — vídeo `2026-250`; Generative AI.

## 11. Movimiento

- [ ] Movimiento con propósito, breve y opcional; nada de animar interacciones muy frecuentes — Motion.

## 12. Marcas y licencias (sobre todo en webs y marketing)

- [ ] Sin SF Pro incrustada ni SF Symbols en webs; sin logotipo de Apple; marcas sin traducir — `licencias-y-marcas.md`.

---

## Apéndice — reglas negativas de cada página (literales)

Generado automáticamente: frases en negrita que empiezan por Avoid / Don’t / Never / Refrain / Do not,
con su apartado entre paréntesis. Úsalo para encontrar la regla exacta que respalda un problema.


### foundations

- **App icons** (`hig/foundations/app-icons.md`): «Don’t use replicas of Apple hardware products. _(Design)_» · «Avoid adding a shape that’s intended to look like a hole or concave area to the background layer. _(visionOS)_» · «Avoid using black for your icon’s background. _(watchOS)_»
- **Branding** (`hig/foundations/branding.md`): «Avoid using a launch screen as a branding opportunity.»
- **Color** (`hig/foundations/color.md`): «Avoid using the same color to mean different things.» · «Avoid relying solely on color to differentiate between objects, indicate interactivity, or communicate essential information. _(Inclusive color)_» · «Avoid using colors that make it hard to perceive content in your app. _(Inclusive color)_» · «Avoid hard-coding system color values in your app. _(System colors)_» · «Avoid redefining the semantic meanings of dynamic system colors. _(System colors)_» · «Avoid using similar colors in control labels if your app has a colorful background. _(Liquid Glass color)_» · «Avoid using only color to indicate focus. _(tvOS)_»
- **Dark Mode** (`hig/foundations/dark-mode.md`): «Avoid offering an app-specific appearance setting.»
- **Icons** (`hig/foundations/icons.md`): «Avoid using replicas of Apple hardware products.» · «Avoid placing important content in the top-right corner of your background fill. _(macOS)_»
- **Immersive experiences** (`hig/foundations/immersive-experiences.md`): «Avoid encouraging people to move while they’re in a progressive or fully immersive experience. _(Promoting comfort)_»
- **Inclusion** (`hig/foundations/inclusion.md`): «Avoid using specialized or technical terms without defining them. _(Welcoming language)_» · «Avoid images and language that exclude people with disabilities. _(Accessibility)_»
- **Layout** (`hig/foundations/layout.md`): «Avoid placing controls or critical information at the bottom of a window. _(macOS)_» · «Avoid displaying content behind the camera housing at the top edge of the window. _(macOS)_» · «Avoid placing more than two or three controls side by side in your interface. _(watchOS)_»
- **Materials** (`hig/foundations/materials.md`): «Don’t use Liquid Glass in the content layer. _(Liquid Glass)_»
- **Motion** (`hig/foundations/motion.md`): «Avoid showing objects that oscillate in a sustained way. _(visionOS)_»
- **Privacy** (`hig/foundations/privacy.md`): «Avoid requesting permission at launch unless the data or resource is required for your app to function. _(Requesting permission)_» · «Don’t include additional actions in your custom screen or window, unless needed to obtain a legal consent. _(Requesting permission)_» · «Never precede the system-provided alert with a custom screen or window that could confuse or mislead people. _(Requesting permission)_» · «Avoid relying solely on passwords for authentication. _(Protecting data)_» · «Never store passwords or other secure content in plain-text files. _(Protecting data)_» · «Avoid inventing custom authentication schemes. _(Protecting data)_» · «Avoid making assumptions about who is signed in. _(macOS)_»
- **Right to left** (`hig/foundations/right-to-left.md`): «Don’t reverse the order of numerals in a specific number. _(Numbers and characters)_» · «Avoid flipping images like photographs, illustrations, and general artwork. _(Images)_» · «Don’t flip logos or universal signs and marks. _(Interface icons)_»
- **SF Symbols** (`hig/foundations/sf-symbols.md`): «Avoid making custom symbols that include common variants, such as enclosures or badges. _(Custom symbols)_» · «Don’t design replicas of Apple products. _(Custom symbols)_»
- **Spatial layout** (`hig/foundations/spatial-layout.md`): «Avoid anchoring content to the wearer’s head. _(Field of view)_» · «Avoid displaying too many windows.»

### patterns

- **Entering data** (`hig/patterns/entering-data.md`): «Never prepopulate a password field.»
- **Feedback** (`hig/patterns/feedback.md`): «Avoid displaying an indeterminate progress indicator — such as a loading indicator — in a watchOS app. _(watchOS)_»
- **File management** (`hig/patterns/file-management.md`): «Avoid including a custom top toolbar. _(iOS, iPadOS)_»
- **Launching** (`hig/patterns/launching.md`): «Avoid including text on your launch screen, even if your first screen displays text. _(Launch screens)_» · «Don’t advertise. _(Launch screens)_»
- **Managing accounts** (`hig/patterns/managing-accounts.md`): «Avoid using the term *passcode* to refer to account authentication.» · «Avoid displaying a sign-out option when people are signed in at the system level. _(TV provider accounts)_» · «Never instruct people to sign out by adjusting privacy controls. _(TV provider accounts)_»
- **Managing notifications** (`hig/patterns/managing-notifications.md`): «Never use the Time Sensitive interruption level to send a marketing notification. _(Sending marketing notifications)_»
- **Multitasking** (`hig/patterns/multitasking.md`): «Avoid interfering with the system-provided multitasking behavior. _(visionOS)_» · «Don’t pause a window’s video playback when people look away from it. _(visionOS)_»
- **Offering help** (`hig/patterns/offering-help.md`): «Avoid bloating your help content by explaining how standard components or patterns work.»
- **Onboarding** (`hig/patterns/onboarding.md`): «Don’t let large downloads hinder onboarding. _(Additional content)_» · «Avoid displaying licensing details within your onboarding flow. _(Additional content)_»
- **Playing audio** (`hig/patterns/playing-audio.md`): «Avoid repurposing audio controls.»
- **Playing haptics** (`hig/patterns/playing-haptics.md`): «Avoid overusing haptics.»
- **Playing video** (`hig/patterns/playing-video.md`): «Avoid allowing audio from different sources to mix as viewers switch between modes.» · «Avoid asking people if they want to resume playback. _(Integrating with the TV app)_» · «Avoid displaying loading screens when possible. _(Integrating with the TV app)_» · «Avoid automatically starting a fully immersive video playback experience. _(visionOS)_» · «Avoid expanding an inline video player to fill a window. _(visionOS)_» · «Avoid creating a poster image that looks like a system control. _(watchOS)_»
- **Ratings and reviews** (`hig/patterns/ratings-and-reviews.md`): «Avoid interrupting people while they’re performing a task or playing a game.» · «Avoid pestering people.»
- **Settings** (`hig/patterns/settings.md`): «Avoid using settings to ask for setup information you can get in other ways.»
- **Undo and redo** (`hig/patterns/undo-and-redo.md`): «Avoid redefining standard gestures for undo and redo. _(iOS, iPadOS)_»
- **Workouts** (`hig/patterns/workouts.md`): «Avoid distracting people from a workout with information that’s not relevant.»

### components

- **Action sheets** (`hig/components/action-sheets.md`): «Avoid letting an action sheet scroll. _(iOS, iPadOS)_» · «Avoid displaying more than four buttons in an action sheet, including the Cancel button. _(watchOS)_»
- **Activity rings** (`hig/components/activity-rings.md`): «Don’t send notifications that repeat the same information the Activity app sends.» · «Don’t use Activity rings for decoration.» · «Don’t use Activity rings for branding.»
- **Activity views** (`hig/components/activity-views.md`): «Avoid creating duplicate versions of common actions that are already available in the activity view.» · «Avoid placing a modal view above your extension. _(Share and action extensions)_»
- **Alerts** (`hig/components/alerts.md`): «Avoid using an alert merely to provide information.» · «Avoid displaying alerts for common, undoable actions, even when they’re destructive.» · «Avoid showing an alert when your app starts.» · «Avoid explaining alert buttons. _(Content)_» · «Avoid using OK as the default button title unless the alert is purely informational. _(Buttons)_»
- **Buttons** (`hig/components/buttons.md`): «Avoid applying a similar color to button labels and content layer backgrounds. _(Style)_» · «Don’t assign the primary role to a button that performs a destructive action, even if that action is the most likely choice. _(Role)_» · «Avoid using labels to introduce square buttons. _(macOS)_» · «Avoid displaying text that introduces a help button. _(macOS)_» · «Avoid creating a custom button that uses a white background fill and black text or icons. _(visionOS)_»
- **Charts** (`hig/components/charts.md`): «Avoid relying solely on color to differentiate between different pieces of data or communicate essential information in a chart. _(Color)_»
- **Home Screen quick actions** (`hig/components/home-screen-quick-actions.md`): «Avoid making unpredictable changes to quick actions.» · «Don’t use an emoji in place of a symbol or interface icon.»
- **Lists and tables** (`hig/components/lists-and-tables.md`): «Avoid adding an index to a table that displays controls — like disclosure indicators — in the trailing ends of its rows. _(iOS, iPadOS, visionOS)_»
- **Live Activities** (`hig/components/live-activities.md`): «Don’t use a Live Activity to display ads or promotions» · «Avoid displaying sensitive information.» · «Don’t add elements to your app that draw attention to the Dynamic Island.» · «Don’t replicate notification layouts. _(Presentation)_»
- **Notifications** (`hig/components/notifications.md`): «Avoid sending multiple notifications for the same thing, even if someone hasn’t responded.» · «Avoid sending a notification that tells people to perform specific tasks within your app.» · «Avoid including sensitive, personal, or confidential information in a notification.» · «Avoid including your app name or icon. _(Content)_» · «Avoid providing an action that merely opens your app. _(Notification actions)_» · «Avoid creating a custom image or component that mimics the appearance or behavior of a badge. _(Badging)_» · «Avoid using a short look as the only way to communicate important information. _(watchOS)_»
- **Page controls** (`hig/components/page-controls.md`): «Avoid using more than two different indicator images in a page control. _(Customizing indicators)_» · «Avoid coloring indicator images. _(Customizing indicators)_» · «Avoid animating page transitions during scrubbing. _(iOS, iPadOS)_» · «Avoid supporting the scrubber when you use the minimal background style. _(iOS, iPadOS)_»
- **Panels** (`hig/components/panels.md`): «Avoid including panels in the Window menu’s documents list.»
- **Pickers** (`hig/components/pickers.md`): «Avoid switching views to show a picker.»
- **Popovers** (`hig/components/popovers.md`): «Don’t show another view over a popover.» · «Avoid making a popover too big.» · «Avoid using the word *popover* in help documentation.» · «Avoid using a popover to show a warning.» · «Avoid displaying popovers in compact views. _(iOS, iPadOS)_»
- **Progress indicators** (`hig/components/progress-indicators.md`): «Don’t switch from the circular style to the bar style.» · «Avoid labeling a spinning progress indicator. _(macOS)_»
- **Pull-down buttons** (`hig/components/pull-down-buttons.md`): «Avoid putting all of a view’s actions in one pull-down button.»
- **Scroll views** (`hig/components/scroll-views.md`): «Avoid putting a scroll view inside another scroll view with the same orientation.» · «Avoid using Look to Scroll for secondary content. _(visionOS)_»
- **Segmented controls** (`hig/components/segmented-controls.md`): «Avoid putting other focusable elements close to segmented controls. _(tvOS)_»
- **Sheets** (`hig/components/sheets.md`): «Avoid displaying a sheet that emerges from the bottom edge of a window. _(visionOS)_»
- **Sidebars** (`hig/components/sidebars.md`): «Avoid putting critical information or actions at the bottom of a sidebar. _(macOS)_»
- **Sliders** (`hig/components/sliders.md`): «Don’t use a slider to adjust audio volume. _(iOS, iPadOS)_»
- **Status bars** (`hig/components/status-bars.md`): «Avoid permanently hiding the status bar.»
- **Tab bars** (`hig/components/tab-bars.md`): «Avoid overflow tabs.» · «Don’t disable or hide tab bar buttons, even when their content is unavailable.» · «Avoid applying a similar color to tab labels and content layer backgrounds.»
- **Tab views** (`hig/components/tab-views.md`): «Avoid using a pop-up button to switch between tabs.» · «Avoid providing more than six tabs in a tab view.»
- **The menu bar** (`hig/components/the-menu-bar.md`): «Avoid making a dynamic menu item the only way to accomplish a task. _(Dynamic menu items)_» · «Avoid relying on the presence of menu bar extras. _(macOS)_»
- **Toggles** (`hig/components/toggles.md`): «Avoid supplying a label that explains the button’s purpose. _(iOS, iPadOS)_» · «Avoid listing too many radio buttons in a set. _(macOS)_»
- **Toolbars** (`hig/components/toolbars.md`): «Avoid applying a similar color to toolbar item labels and content layer backgrounds.» · «Don’t title windows with your app name. _(Titles)_» · «Avoid creating a vertical toolbar. _(visionOS)_» · «Avoid using a pull-down menu in a toolbar. _(visionOS)_»
- **Top Shelf** (`hig/components/top-shelf.md`): «Avoid showing advertisements or prices.» · «Avoid implying interactivity in a static image.»
- **Virtual keyboards** (`hig/components/virtual-keyboards.md`): «Avoid duplicating system-provided keyboard features. _(Custom keyboards)_»
- **Web views** (`hig/components/web-views.md`): «Avoid using a web view to build a web browser.»
- **Widgets** (`hig/components/widgets.md`): «Avoid mirroring your widget’s appearance within your app.» · «Avoid very small font sizes.» · «Avoid rasterizing text.»
- **Windows** (`hig/components/windows.md`): «Avoid creating custom window UI.» · «Avoid putting critical information or actions in a bottom bar, because people often relocate a window in a way that hides its bottom edge. _(macOS)_»

### inputs

- **Apple Pencil and Scribble** (`hig/inputs/apple-pencil-and-scribble.md`): «Avoid using hover to initiate an action. _(Hover)_» · «Avoid using the double-tap gesture to perform an action that modifies content. _(Double tap)_» · «Avoid distracting people while they write. _(Scribble)_»
- **Eyes** (`hig/inputs/eyes.md`): «Avoid using a repeating pattern or texture that fills the field of view. _(Making items easy to see)_»
- **Focus and selection** (`hig/inputs/focus-and-selection.md`): «Avoid changing focus without people’s interaction.» · «Avoid displaying a pointer. _(tvOS)_»
- **Gestures** (`hig/inputs/gestures.md`): «Avoid conflicting with gestures that access system UI. _(Custom gestures)_» · «Avoid requiring specific body movements or positions for input. _(visionOS)_» · «Avoid custom gestures that require using a specific hand. _(visionOS)_» · «Avoid setting a primary action in views with lists, scroll views, or vertical tabs. _(watchOS)_»
- **Keyboards** (`hig/inputs/keyboards.md`): «Avoid adding Shift to a shortcut that uses the upper character of a two-character key. _(Custom keyboard shortcuts)_» · «Avoid creating a new shortcut by adding a modifier to an existing shortcut for an unrelated command. _(Custom keyboard shortcuts)_»
- **Nearby interactions** (`hig/inputs/nearby-interactions.md`): «Avoid using a nearby interaction as the only way to perform a task.»
- **Pointing devices** (`hig/inputs/pointing-devices.md`): «Avoid redefining systemwide trackpad gestures.» · «Avoid creating gratuitous pointer and content effects. _(iPadOS)_» · «Avoid displaying instructional text with a pointer. _(iPadOS)_»

### technologies

- **AirPlay** (`hig/technologies/airplay.md`): «Don’t stop playback when your app enters the background or when the device locks.» · «Don’t interrupt another app’s playback unless your app is starting to play immersive content.» · «Don’t use the AirPlay icon or name in custom buttons or interactive elements. _(Using AirPlay icons)_»
- **App Clips** (`hig/technologies/app-clips.md`): «Don’t use App Clips solely for marketing purposes. _(Designing your App Clip)_» · «Avoid using web views in your App Clip. _(Designing your App Clip)_» · «Avoid requiring people to create an account before they can benefit from your App Clip. _(Designing your App Clip)_» · «Don’t compromise the user experience by asking people to install the full app. _(Designing your App Clip)_» · «Avoid using text. _(Creating content for an App Clip card)_» · «Don’t create App Clip Codes that are too small. _(App Clip Codes)_»
- **Apple In-App Purchase** (`hig/technologies/apple-in-app-purchase.md`): «Avoid characterizing or providing guidance on Apple’s refund policies.»
- **Apple Pay** (`hig/technologies/apple-pay.md`): «Don’t hide an Apple Pay button or make it appear unavailable. _(Offering Apple Pay)_» · «Avoid requiring account creation before purchase. _(Streamlining checkout)_» · «Avoid forcing compliance with your business logic. _(Handling problems)_» · «Never use the Apple logo to represent the name *Apple* in text. _(Referring to Apple Pay)_» · «Don’t translate *Apple Pay* or any other Apple trademark. _(Referring to Apple Pay)_»
- **Augmented reality** (`hig/technologies/augmented-reality.md`): «Avoid trying to precisely align objects with the edges of detected surfaces. _(Helping people place objects)_»
- **CarPlay** (`hig/technologies/carplay.md`): «Never lock people out of CarPlay because the connected iPhone requires input. _(iPhone interactions)_» · «Avoid using the same color for interactive and noninteractive elements. _(Color)_» · «Don’t use black for your icon’s background. _(Icons and images)_»
- **Game Center** (`hig/technologies/game-center.md`): «Avoid placing controls near the access point. _(Accessing Game Center)_» · «Avoid creating challenges that track overall progress or personal best scores. _(Challenges)_»
- **HealthKit** (`hig/technologies/healthkit.md`): «Don’t use Activity rings for ornamentation. _(Activity rings)_» · «Don’t use Activity rings for branding. _(Activity rings)_» · «Don’t use the Apple Health icon as a button. _(Apple Health icon)_» · «Don’t alter the appearance of the Apple Health icon. _(Apple Health icon)_» · «Don’t use the Apple Health icon within text or as a replacement for the terms *Health*, *Apple Health*, or *HealthKit*. _(Apple Health icon)_» · «Don’t display Health app images or screenshots. _(Apple Health icon)_» · «Don’t use the term *HealthKit*. _(Editorial guidelines)_»
- **HomeKit** (`hig/technologies/homekit.md`): «Don’t present duplicate home settings. _(Terminology and layout)_» · «Don’t require people to create an account or supply personal information. _(Setup)_» · «Don’t block camera images. _(Custom functionality)_» · «Don’t use the HomeKit icon within text or as a replacement for the word HomeKit. _(Using HomeKit icons)_» · «Don’t use the name *HomeKit* as a descriptor. _(Referring to HomeKit)_» · «Don’t suggest that HomeKit is performing an action or function. _(Referring to HomeKit)_»
- **Machine learning** (`hig/technologies/machine-learning.md`): «Don’t let implicit feedback decrease people’s opportunities to explore. _(Implicit feedback)_» · «Avoid asking people to participate in calibration more than once. _(Calibration)_» · «Never rely on corrections to make up for low-quality results. _(Corrections)_» · «Avoid being too specific or too general. _(Attribution)_»
- **Maps** (`hig/technologies/maps.md`): «Avoid duplicating information. _(Place cards)_»
- **NFC** (`hig/technologies/nfc.md`): «Don’t encourage people to make contact with physical objects. _(In-app tag reading)_»
- **Photo editing** (`hig/technologies/photo-editing.md`): «Don’t provide a custom top toolbar.»
- **Sign in with Apple** (`hig/technologies/sign-in-with-apple.md`): «Don’t ask people to supply a password. _(Collecting data)_» · «Avoid asking for a personal email address when people supply a private relay address. _(Collecting data)_» · «Don’t add horizontal padding to a logo-only image. _(Displaying buttons)_»
- **Siri** (`hig/technologies/siri.md`): «Don’t advertise.»
- **Tap to Pay on iPhone** (`hig/technologies/tap-to-pay-on-iphone.md`): «Avoid making merchants wait to use Tap to Pay on iPhone. _(Checking out)_»
- **Wallet** (`hig/technologies/wallet.md`): «Avoid inner drop shadows on logo artwork. _(Pass images)_» · «Avoid sending duplicate notifications. _(Order tracking)_»
- **iCloud** (`hig/technologies/icloud.md`): «Avoid asking which documents to keep in iCloud.»

### getting-started

- **Design principles** (`hig/getting-started/design-principles.md`): «Don’t mistake delight for decoration. _(Delight)_»
- **Designing for games** (`hig/getting-started/designing-for-games.md`): «Avoid stereotypes in your stories and characters. _(Welcome everyone)_»
- **Designing for iPhone Duo** (`hig/getting-started/designing-for-iphone-duo.md`): «Avoid extreme layout changes as people fold the device. _(Dynamic layouts)_»
