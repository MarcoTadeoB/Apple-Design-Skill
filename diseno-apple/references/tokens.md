# Tokens de diseño de Apple — valores exactos

Generado desde la caché de las HIG (HIG descargadas el 2026-10-15). Cada tabla indica la página de origen. Los colores
aparecen como `R,G,B · #HEX` (Apple los publica en el texto alternativo de cada muestra).

**Antes de usar estos valores**

- En apps nativas, **no copies los valores**: usa las API (`Color.blue`, `UIColor.systemBlue`, `.font(.body)`…).
  Apple: «Avoid hard-coding system color values in your app… The actual color values may fluctuate from release to
  release» ([Color](https://developer.apple.com/design/human-interface-guidelines/color#System-colors)).
- En web o en maquetas, son la mejor referencia disponible; indica siempre la fecha de la HIG de la que salen.
- Si un valor no está aquí ni en `references/hig/`, **no está publicado en las HIG**: dilo, no lo inventes.

## Índice

1. Colores de sistema (claro, oscuro y alto contraste)
2. Grises de sistema de iOS/iPadOS
3. Colores dinámicos (semánticos) de iOS/iPadOS y macOS — nombres y uso (Apple no publica sus RGB)
4. Contraste mínimo
5. Tipografía: tamaños por defecto y mínimos, Dynamic Type por plataforma, interlineado y tracking
6. Tamaños mínimos de controles y espaciado
7. Márgenes y zonas seguras publicadas
8. Radios y formas (concentricidad)
9. Materiales
10. Iconos de app
11. Huecos: lo que las HIG no publican

---

## 1. Colores de sistema

Fuente: [Color › Specifications](https://developer.apple.com/design/human-interface-guidelines/color#Specifications).
Apple: «visionOS system colors use the default dark color values.» En la versión 26 (9-6-2025) se
actualizaron los valores («Updated system color values»).

_Fuente: [color](https://developer.apple.com/design/human-interface-guidelines/color)_

| Name | SwiftUI API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
|---|---|---|---|---|---|
| Red | [red](https://developer.apple.com/documentation/swiftui/color/red) | 255,56,60 · #FF383C | 255,66,69 · #FF4245 | 233,21,45 · #E9152D | 255,97,101 · #FF6165 |
| Orange | [orange](https://developer.apple.com/documentation/swiftui/color/orange) | 255,141,40 · #FF8D28 | 255,146,48 · #FF9230 | 197,83,0 · #C55300 | 255,160,86 · #FFA056 |
| Yellow | [yellow](https://developer.apple.com/documentation/swiftui/color/yellow) | 255,204,0 · #FFCC00 | 255,214,0 · #FFD600 | 161,106,0 · #A16A00 | 254,223,67 · #FEDF43 |
| Green | [green](https://developer.apple.com/documentation/swiftui/color/green) | 52,199,89 · #34C759 | 48,209,88 · #30D158 | 0,137,50 · #008932 | 74,217,104 · #4AD968 |
| Mint | [mint](https://developer.apple.com/documentation/swiftui/color/mint) | 0,200,179 · #00C8B3 | 0,218,195 · #00DAC3 | 0,133,117 · #008575 | 84,223,203 · #54DFCB |
| Teal | [teal](https://developer.apple.com/documentation/swiftui/color/teal) | 0,195,208 · #00C3D0 | 0,210,224 · #00D2E0 | 0,129,152 · #008198 | 59,221,236 · #3BDDEC |
| Cyan | [cyan](https://developer.apple.com/documentation/swiftui/color/cyan) | 0,192,232 · #00C0E8 | 60,211,254 · #3CD3FE | 0,126,174 · #007EAE | 109,217,255 · #6DD9FF |
| Blue | [blue](https://developer.apple.com/documentation/swiftui/color/blue) | 0,136,255 · #0088FF | 0,145,255 · #0091FF | 30,110,244 · #1E6EF4 | 92,184,255 · #5CB8FF |
| Indigo | [indigo](https://developer.apple.com/documentation/swiftui/color/indigo) | 97,85,245 · #6155F5 | 109,124,255 · #6D7CFF | 86,74,222 · #564ADE | 167,170,255 · #A7AAFF |
| Purple | [purple](https://developer.apple.com/documentation/swiftui/color/purple) | 203,48,224 · #CB30E0 | 219,52,242 · #DB34F2 | 176,47,194 · #B02FC2 | 234,141,255 · #EA8DFF |
| Pink | [pink](https://developer.apple.com/documentation/swiftui/color/pink) | 255,45,85 · #FF2D55 | 255,55,95 · #FF375F | 231,18,77 · #E7124D | 255,138,196 · #FF8AC4 |
| Brown | [brown](https://developer.apple.com/documentation/swiftui/color/brown) | 172,127,94 · #AC7F5E | 183,138,102 · #B78A66 | 149,109,81 · #956D51 | 219,166,121 · #DBA679 |


## 2. Grises de sistema de iOS y iPadOS

_Fuente: [color](https://developer.apple.com/design/human-interface-guidelines/color)_

| Name | UIKit API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
|---|---|---|---|---|---|
| Gray | [systemGray](https://developer.apple.com/documentation/uikit/uicolor/systemgray) | 142,142,147 · #8E8E93 | 142,142,147 · #8E8E93 | 108,108,112 · #6C6C70 | 174,174,178 · #AEAEB2 |
| Gray (2) | [systemGray2](https://developer.apple.com/documentation/uikit/uicolor/systemgray2) | 174,174,178 · #AEAEB2 | 99,99,102 · #636366 | 142,142,147 · #8E8E93 | 124,124,128 · #7C7C80 |
| Gray (3) | [systemGray3](https://developer.apple.com/documentation/uikit/uicolor/systemgray3) | 199,199,204 · #C7C7CC | 72,72,74 · #48484A | 174,174,178 · #AEAEB2 | 84,84,86 · #545456 |
| Gray (4) | [systemGray4](https://developer.apple.com/documentation/uikit/uicolor/systemgray4) | 209,209,214 · #D1D1D6 | 58,58,60 · #3A3A3C | 188,188,192 · #BCBCC0 | 68,68,70 · #444446 |
| Gray (5) | [systemGray5](https://developer.apple.com/documentation/uikit/uicolor/systemgray5) | 229,229,234 · #E5E5EA | 44,44,46 · #2C2C2E | 216,216,220 · #D8D8DC | 54,54,56 · #363638 |
| Gray (6) | [systemGray6](https://developer.apple.com/documentation/uikit/uicolor/systemgray6) | 242,242,247 · #F2F2F7 | 28,28,30 · #1C1C1E | 235,235,240 · #EBEBF0 | 36,36,38 · #242426 |


La HIG añade: «In SwiftUI, the equivalent of `systemGray` is [gray](https://developer.apple.com/documentation/swiftui/color/gray).»

## 3. Colores dinámicos (semánticos)

Se definen por su **propósito**, no por su aspecto, y se adaptan solos a claro/oscuro/contraste. Las HIG
listan nombres y usos, **pero no publican sus valores RGB**.

### iOS, iPadOS

iOS define dos juegos de fondos dinámicos, *system* y *grouped* (`systemBackground`, `systemGroupedBackground`…),
cada uno con variantes primaria (vista general), secundaria (agrupar dentro de la vista) y terciaria (agrupar
dentro de elementos secundarios). Colores de primer plano:

_Fuente: [color](https://developer.apple.com/design/human-interface-guidelines/color)_

| Color | Use for… | UIKit API |
|---|---|---|
| Label | A text label that contains primary content. | [label](https://developer.apple.com/documentation/uikit/uicolor/label) |
| Secondary label | A text label that contains secondary content. | [secondaryLabel](https://developer.apple.com/documentation/uikit/uicolor/secondarylabel) |
| Tertiary label | A text label that contains tertiary content. | [tertiaryLabel](https://developer.apple.com/documentation/uikit/uicolor/tertiarylabel) |
| Quaternary label | A text label that contains quaternary content. | [quaternaryLabel](https://developer.apple.com/documentation/uikit/uicolor/quaternarylabel) |
| Placeholder text | Placeholder text in controls or text views. | [placeholderText](https://developer.apple.com/documentation/uikit/uicolor/placeholdertext) |
| Separator | A separator that allows some underlying content to be visible. | [separator](https://developer.apple.com/documentation/uikit/uicolor/separator) |
| Opaque separator | A separator that doesn’t allow any underlying content to be visible. | [opaqueSeparator](https://developer.apple.com/documentation/uikit/uicolor/opaqueseparator) |
| Link | Text that functions as a link. | [link](https://developer.apple.com/documentation/uikit/uicolor/link) |


### macOS

_Fuente: [color](https://developer.apple.com/design/human-interface-guidelines/color)_

| Color | Use for… | AppKit API |
|---|---|---|
| Alternate selected control text color | The text on a selected surface in a list or table. | [alternateSelectedControlTextColor](https://developer.apple.com/documentation/appkit/nscolor/alternateselectedcontroltextcolor) |
| Alternating content background colors | The backgrounds of alternating rows or columns in a list, table, or collection view. | [alternatingContentBackgroundColors](https://developer.apple.com/documentation/appkit/nscolor/alternatingcontentbackgroundcolors) |
| Control accent | The accent color people select in System Settings. | [controlAccentColor](https://developer.apple.com/documentation/appkit/nscolor/controlaccentcolor) |
| Control background color | The background of a large interface element, such as a browser or table. | [controlBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/controlbackgroundcolor) |
| Control color | The surface of a control. | [controlColor](https://developer.apple.com/documentation/appkit/nscolor/controlcolor) |
| Control text color | The text of a control that is available. | [controlTextColor](https://developer.apple.com/documentation/appkit/nscolor/controltextcolor) |
| Current control tint | The system-defined control tint. | [currentControlTint](https://developer.apple.com/documentation/appkit/nscolor/currentcontroltint) |
| Unavailable control text color | The text of a control that’s unavailable. | [disabledControlTextColor](https://developer.apple.com/documentation/appkit/nscolor/disabledcontroltextcolor) |
| Find highlight color | The color of a find indicator. | [findHighlightColor](https://developer.apple.com/documentation/appkit/nscolor/findhighlightcolor) |
| Grid color | The gridlines of an interface element, such as a table. | [gridColor](https://developer.apple.com/documentation/appkit/nscolor/gridcolor) |
| Header text color | The text of a header cell in a table. | [headerTextColor](https://developer.apple.com/documentation/appkit/nscolor/headertextcolor) |
| Highlight color | The virtual light source onscreen. | [highlightColor](https://developer.apple.com/documentation/appkit/nscolor/highlightcolor) |
| Keyboard focus indicator color | The ring that appears around the currently focused control when using the keyboard for interface navigation. | [keyboardFocusIndicatorColor](https://developer.apple.com/documentation/appkit/nscolor/keyboardfocusindicatorcolor) |
| Label color | The text of a label containing primary content. | [labelColor](https://developer.apple.com/documentation/appkit/nscolor/labelcolor) |
| Link color | A link to other content. | [linkColor](https://developer.apple.com/documentation/appkit/nscolor/linkcolor) |
| Placeholder text color | A placeholder string in a control or text view. | [placeholderTextColor](https://developer.apple.com/documentation/appkit/nscolor/placeholdertextcolor) |
| Quaternary label color | The text of a label of lesser importance than a tertiary label, such as watermark text. | [quaternaryLabelColor](https://developer.apple.com/documentation/appkit/nscolor/quaternarylabelcolor) |
| Secondary label color | The text of a label of lesser importance than a primary label, such as a label used to represent a subheading or additional information. | [secondaryLabelColor](https://developer.apple.com/documentation/appkit/nscolor/secondarylabelcolor) |
| Selected content background color | The background for selected content in a key window or view. | [selectedContentBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/selectedcontentbackgroundcolor) |
| Selected control color | The surface of a selected control. | [selectedControlColor](https://developer.apple.com/documentation/appkit/nscolor/selectedcontrolcolor) |
| Selected control text color | The text of a selected control. | [selectedControlTextColor](https://developer.apple.com/documentation/appkit/nscolor/selectedcontroltextcolor) |
| Selected menu item text color | The text of a selected menu. | [selectedMenuItemTextColor](https://developer.apple.com/documentation/appkit/nscolor/selectedmenuitemtextcolor) |
| Selected text background color | The background of selected text. | [selectedTextBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/selectedtextbackgroundcolor) |
| Selected text color | The color for selected text. | [selectedTextColor](https://developer.apple.com/documentation/appkit/nscolor/selectedtextcolor) |
| Separator color | A separator between different sections of content. | [separatorColor](https://developer.apple.com/documentation/appkit/nscolor/separatorcolor) |
| Shadow color | The virtual shadow cast by a raised object onscreen. | [shadowColor](https://developer.apple.com/documentation/appkit/nscolor/shadowcolor) |
| Tertiary label color | The text of a label of lesser importance than a secondary label. | [tertiaryLabelColor](https://developer.apple.com/documentation/appkit/nscolor/tertiarylabelcolor) |
| Text background color | The background color behind text. | [textBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/textbackgroundcolor) |
| Text color | The text in a document. | [textColor](https://developer.apple.com/documentation/appkit/nscolor/textcolor) |
| Under page background color | The background behind a document’s content. | [underPageBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/underpagebackgroundcolor) |
| Unemphasized selected content background color | The selected content in a non-key window or view. | [unemphasizedSelectedContentBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/unemphasizedselectedcontentbackgroundcolor) |
| Unemphasized selected text background color | A background for selected text in a non-key window or view. | [unemphasizedSelectedTextBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/unemphasizedselectedtextbackgroundcolor) |
| Unemphasized selected text color | Selected text in a non-key window or view. | [unemphasizedSelectedTextColor](https://developer.apple.com/documentation/appkit/nscolor/unemphasizedselectedtextcolor) |
| Window background color | The background of a window. | [windowBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/windowbackgroundcolor) |
| Window frame text color | The text in the window’s title bar area. | [windowFrameTextColor](https://developer.apple.com/documentation/appkit/nscolor/windowframetextcolor) |


Dark Mode en iOS/iPadOS usa dos juegos de fondos, *base* (más tenue) y *elevated* (más brillante, para
popovers y sheets en primer plano) — [Dark Mode › iOS, iPadOS](https://developer.apple.com/design/human-interface-guidelines/dark-mode#iOS-iPadOS).
Dark Mode no existe en visionOS ni watchOS.

## 4. Contraste mínimo

Fuente: [Accessibility › Vision](https://developer.apple.com/design/human-interface-guidelines/accessibility#Vision).

_Fuente: [accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)_

| Text size | Text weight | Minimum contrast ratio |
|---|---|---|
| Up to 17 pts | All | 4.5:1 |
| 18 pts | All | 3:1 |
| All | Bold | 3:1 |


Además ([Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Dark-Mode-colors)):
«make sure the contrast ratio between colors is no lower than 4.5:1. For custom foreground and background colors,
strive for a contrast ratio of 7:1, especially in small text.»

## 5. Tipografía

Fuentes del sistema: SF Pro (iOS, iPadOS, macOS, tvOS, visionOS), SF Compact (watchOS; SF Compact Rounded
en complicaciones), New York (NY) como serif — [Typography › Platform considerations](https://developer.apple.com/design/human-interface-guidelines/typography#Platform-considerations).
macOS no admite Dynamic Type. Pesos enfatizados: medium, semibold, bold o heavy (`bold()` en SwiftUI,
`traitBold` en UIKit).

### 5.1 Tamaño por defecto y mínimo por plataforma

_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Platform | Default size | Minimum size |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |


### 5.2 iOS y iPadOS — Dynamic Type (tamaño por defecto: Large)

«Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.»

#### Large (por defecto)
_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 34 | 41 | Bold |
| Title 1 | Regular | 28 | 34 | Bold |
| Title 2 | Regular | 22 | 28 | Bold |
| Title 3 | Regular | 20 | 25 | Semibold |
| Headline | Semibold | 17 | 22 | Semibold |
| Body | Regular | 17 | 22 | Semibold |
| Callout | Regular | 16 | 21 | Semibold |
| Subhead | Regular | 15 | 20 | Semibold |
| Footnote | Regular | 13 | 18 | Semibold |
| Caption 1 | Regular | 12 | 16 | Semibold |
| Caption 2 | Regular | 11 | 13 | Semibold |


#### xSmall
_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 31 | 38 | Bold |
| Title 1 | Regular | 25 | 31 | Bold |
| Title 2 | Regular | 19 | 24 | Bold |
| Title 3 | Regular | 17 | 22 | Semibold |
| Headline | Semibold | 14 | 19 | Semibold |
| Body | Regular | 14 | 19 | Semibold |
| Callout | Regular | 13 | 18 | Semibold |
| Subhead | Regular | 12 | 16 | Semibold |
| Footnote | Regular | 12 | 16 | Semibold |
| Caption 1 | Regular | 11 | 13 | Semibold |
| Caption 2 | Regular | 11 | 13 | Semibold |


#### Small
_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 32 | 39 | Bold |
| Title 1 | Regular | 26 | 32 | Bold |
| Title 2 | Regular | 20 | 25 | Bold |
| Title 3 | Regular | 18 | 23 | Semibold |
| Headline | Semibold | 15 | 20 | Semibold |
| Body | Regular | 15 | 20 | Semibold |
| Callout | Regular | 14 | 19 | Semibold |
| Subhead | Regular | 13 | 18 | Semibold |
| Footnote | Regular | 12 | 16 | Semibold |
| Caption 1 | Regular | 11 | 13 | Semibold |
| Caption 2 | Regular | 11 | 13 | Semibold |


#### Medium
_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 33 | 40 | Bold |
| Title 1 | Regular | 27 | 33 | Bold |
| Title 2 | Regular | 21 | 26 | Bold |
| Title 3 | Regular | 19 | 24 | Semibold |
| Headline | Semibold | 16 | 21 | Semibold |
| Body | Regular | 16 | 21 | Semibold |
| Callout | Regular | 15 | 20 | Semibold |
| Subhead | Regular | 14 | 19 | Semibold |
| Footnote | Regular | 12 | 16 | Semibold |
| Caption 1 | Regular | 11 | 13 | Semibold |
| Caption 2 | Regular | 11 | 13 | Semibold |


#### xLarge
_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 36 | 43 | Bold |
| Title 1 | Regular | 30 | 37 | Bold |
| Title 2 | Regular | 24 | 30 | Bold |
| Title 3 | Regular | 22 | 28 | Semibold |
| Headline | Semibold | 19 | 24 | Semibold |
| Body | Regular | 19 | 24 | Semibold |
| Callout | Regular | 18 | 23 | Semibold |
| Subhead | Regular | 17 | 22 | Semibold |
| Footnote | Regular | 15 | 20 | Semibold |
| Caption 1 | Regular | 14 | 19 | Semibold |
| Caption 2 | Regular | 13 | 18 | Semibold |


#### xxLarge
_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 38 | 46 | Bold |
| Title 1 | Regular | 32 | 39 | Bold |
| Title 2 | Regular | 26 | 32 | Bold |
| Title 3 | Regular | 24 | 30 | Semibold |
| Headline | Semibold | 21 | 26 | Semibold |
| Body | Regular | 21 | 26 | Semibold |
| Callout | Regular | 20 | 25 | Semibold |
| Subhead | Regular | 19 | 24 | Semibold |
| Footnote | Regular | 17 | 22 | Semibold |
| Caption 1 | Regular | 16 | 21 | Semibold |
| Caption 2 | Regular | 15 | 20 | Semibold |


#### xxxLarge
_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 40 | 48 | Bold |
| Title 1 | Regular | 34 | 41 | Bold |
| Title 2 | Regular | 28 | 34 | Bold |
| Title 3 | Regular | 26 | 32 | Semibold |
| Headline | Semibold | 23 | 29 | Semibold |
| Body | Regular | 23 | 29 | Semibold |
| Callout | Regular | 22 | 28 | Semibold |
| Subhead | Regular | 21 | 28 | Semibold |
| Footnote | Regular | 19 | 24 | Semibold |
| Caption 1 | Regular | 18 | 23 | Semibold |
| Caption 2 | Regular | 17 | 22 | Semibold |


#### Tamaños de accesibilidad AX1–AX5
_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 44 | 52 | Bold |
| Title 1 | Regular | 38 | 46 | Bold |
| Title 2 | Regular | 34 | 41 | Bold |
| Title 3 | Regular | 31 | 38 | Semibold |
| Headline | Semibold | 28 | 34 | Semibold |
| Body | Regular | 28 | 34 | Semibold |
| Callout | Regular | 26 | 32 | Semibold |
| Subhead | Regular | 25 | 31 | Semibold |
| Footnote | Regular | 23 | 29 | Semibold |
| Caption 1 | Regular | 22 | 28 | Semibold |
| Caption 2 | Regular | 20 | 25 | Semibold |

_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 48 | 57 | Bold |
| Title 1 | Regular | 43 | 51 | Bold |
| Title 2 | Regular | 39 | 47 | Bold |
| Title 3 | Regular | 37 | 44 | Semibold |
| Headline | Semibold | 33 | 40 | Semibold |
| Body | Regular | 33 | 40 | Semibold |
| Callout | Regular | 32 | 39 | Semibold |
| Subhead | Regular | 30 | 37 | Semibold |
| Footnote | Regular | 27 | 33 | Semibold |
| Caption 1 | Regular | 26 | 32 | Semibold |
| Caption 2 | Regular | 24 | 30 | Semibold |

_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 52 | 61 | Bold |
| Title 1 | Regular | 48 | 57 | Bold |
| Title 2 | Regular | 44 | 52 | Bold |
| Title 3 | Regular | 43 | 51 | Semibold |
| Headline | Semibold | 40 | 48 | Semibold |
| Body | Regular | 40 | 48 | Semibold |
| Callout | Regular | 38 | 46 | Semibold |
| Subhead | Regular | 36 | 43 | Semibold |
| Footnote | Regular | 33 | 40 | Semibold |
| Caption 1 | Regular | 32 | 39 | Semibold |
| Caption 2 | Regular | 29 | 35 | Semibold |

_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 56 | 66 | Bold |
| Title 1 | Regular | 53 | 62 | Bold |
| Title 2 | Regular | 50 | 59 | Bold |
| Title 3 | Regular | 49 | 58 | Semibold |
| Headline | Semibold | 47 | 56 | Semibold |
| Body | Regular | 47 | 56 | Semibold |
| Callout | Regular | 44 | 52 | Semibold |
| Subhead | Regular | 42 | 50 | Semibold |
| Footnote | Regular | 38 | 46 | Semibold |
| Caption 1 | Regular | 37 | 44 | Semibold |
| Caption 2 | Regular | 34 | 41 | Semibold |

_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 60 | 70 | Bold |
| Title 1 | Regular | 58 | 68 | Bold |
| Title 2 | Regular | 56 | 66 | Bold |
| Title 3 | Regular | 55 | 65 | Semibold |
| Headline | Semibold | 53 | 62 | Semibold |
| Body | Regular | 53 | 62 | Semibold |
| Callout | Regular | 51 | 60 | Semibold |
| Subhead | Regular | 49 | 58 | Semibold |
| Footnote | Regular | 44 | 52 | Semibold |
| Caption 1 | Regular | 43 | 51 | Semibold |
| Caption 2 | Regular | 40 | 48 | Semibold |


### 5.3 macOS — estilos de texto integrados

_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Text style | Weight | Size (points) | Line height (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 26 | 32 | Bold |
| Title 1 | Regular | 22 | 26 | Bold |
| Title 2 | Regular | 17 | 22 | Bold |
| Title 3 | Regular | 15 | 20 | Semibold |
| Headline | Bold | 13 | 16 | Heavy |
| Body | Regular | 13 | 16 | Semibold |
| Callout | Regular | 12 | 15 | Semibold |
| Subheadline | Regular | 11 | 14 | Semibold |
| Footnote | Regular | 10 | 13 | Semibold |
| Caption 1 | Regular | 10 | 13 | Medium |
| Caption 2 | Medium | 10 | 13 | Semibold |


### 5.4 tvOS — estilos de texto integrados

_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Text style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Title 1 | Medium | 76 | 96 | Bold |
| Title 2 | Medium | 57 | 66 | Bold |
| Title 3 | Medium | 48 | 56 | Bold |
| Headline | Medium | 38 | 46 | Bold |
| Subtitle 1 | Regular | 38 | 46 | Medium |
| Callout | Medium | 31 | 38 | Bold |
| Body | Medium | 29 | 36 | Bold |
| Caption 1 | Medium | 25 | 32 | Bold |
| Caption 2 | Medium | 23 | 30 | Bold |


### 5.5 watchOS — Dynamic Type

#### Large (por defecto en 40/41/42 mm)
_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 36 | 38.5 | Bold |
| Title 1 | Regular | 34 | 36.5 | Semibold |
| Title 2 | Regular | 28 | 30.5 | Semibold |
| Title 3 | Regular | 19 | 21.5 | Semibold |
| Headline | Semibold | 16 | 18.5 | Semibold |
| Body | Regular | 16 | 18.5 | Semibold |
| Caption 1 | Regular | 15 | 17.5 | Semibold |
| Caption 2 | Regular | 14 | 16.5 | Semibold |
| Footnote 1 | Regular | 13 | 15.5 | Semibold |
| Footnote 2 | Regular | 12 | 14.5 | Semibold |


#### xLarge (por defecto en 44/45/49 mm)
_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 40 | 42.5 | Bold |
| Title 1 | Regular | 38 | 40.5 | Semibold |
| Title 2 | Regular | 30 | 32.5 | Semibold |
| Title 3 | Regular | 20 | 22.5 | Semibold |
| Headline | Semibold | 17 | 19.5 | Semibold |
| Body | Regular | 17 | 19.5 | Semibold |
| Caption 1 | Regular | 16 | 18.5 | Semibold |
| Caption 2 | Regular | 15 | 17.5 | Semibold |
| Footnote 1 | Regular | 14 | 16.5 | Semibold |
| Footnote 2 | Regular | 13 | 15.5 | Semibold |


#### Small (por defecto en 38 mm)
_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 32 | 34.5 | Bold |
| Title 1 | Regular | 30 | 32.5 | Semibold |
| Title 2 | Regular | 26 | 28.5 | Semibold |
| Title 3 | Regular | 18 | 20.5 | Semibold |
| Headline | Semibold | 15 | 17.5 | Semibold |
| Body | Regular | 15 | 17.5 | Semibold |
| Caption 1 | Regular | 14 | 16.5 | Semibold |
| Caption 2 | Regular | 13 | 15.5 | Semibold |
| Footnote 1 | Regular | 12 | 14.5 | Semibold |
| Footnote 2 | Regular | 11 | 13.5 | Semibold |


El resto (xSmall, xxLarge, xxxLarge, AX1–AX3) está en `references/hig/foundations/typography.md`.

### 5.6 visionOS

Las HIG no publican una tabla propia de Dynamic Type para visionOS. Dicen: «visionOS uses bolder versions of
the Dynamic Type body and title styles and it introduces Extra Large Title 1 and Extra Large Title 2» y que
el tracking de SF Pro es el mismo que en iOS («iOS, iPadOS, visionOS tracking values»).

### 5.7 Tracking (espaciado entre letras) de SF Pro — iOS, iPadOS y visionOS

Unidades: milésimas de em y puntos. Para CSS: `letter-spacing: <milésimas>/1000 em` (p. ej. +6 → `0.006em`).

_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Size (points) | Tracking (1/1000 em) | Tracking (points) |
|---|---|---|
| 6 | +41 | +0.24 |
| 7 | +34 | +0.23 |
| 8 | +26 | +0.21 |
| 9 | +19 | +0.17 |
| 10 | +12 | +0.12 |
| 11 | +6 | +0.06 |
| 12 | 0 | 0.0 |
| 13 | -6 | -0.08 |
| 14 | -11 | -0.15 |
| 15 | -16 | -0.23 |
| 16 | -20 | -0.31 |
| 17 | -26 | -0.43 |
| 18 | -25 | -0.44 |
| 19 | -24 | -0.45 |
| 20 | -23 | -0.45 |
| 21 | -18 | -0.36 |
| 22 | -12 | -0.26 |
| 23 | -4 | -0.10 |
| 24 | +3 | +0.07 |
| 25 | +6 | +0.15 |
| 26 | +8 | +0.22 |
| 27 | +11 | +0.29 |
| 28 | +14 | +0.38 |
| 29 | +14 | +0.40 |
| 30 | +14 | +0.40 |
| 31 | +13 | +0.39 |
| 32 | +13 | +0.41 |
| 33 | +12 | +0.40 |
| 34 | +12 | +0.40 |
| 35 | +11 | +0.38 |
| 36 | +10 | +0.37 |
| 37 | +10 | +0.36 |
| 38 | +10 | +0.37 |
| 39 | +10 | +0.38 |
| 40 | +10 | +0.37 |
| 41 | +9 | +0.36 |
| 42 | +9 | +0.37 |
| 43 | +9 | +0.38 |
| 44 | +8 | +0.37 |
| 45 | +8 | +0.35 |
| 46 | +8 | +0.36 |
| 47 | +8 | +0.37 |
| 48 | +8 | +0.35 |
| 49 | +7 | +0.33 |
| 50 | +7 | +0.34 |
| 51 | +7 | +0.35 |
| 52 | +6 | +0.33 |
| 53 | +6 | +0.31 |
| 54 | +6 | +0.32 |
| 56 | +6 | +0.30 |
| 58 | +5 | +0.28 |
| 60 | +4 | +0.26 |
| 62 | +4 | +0.24 |
| 64 | +4 | +0.22 |
| 66 | +3 | +0.19 |
| 68 | +2 | +0.17 |
| 70 | +2 | +0.14 |
| 72 | +2 | +0.14 |
| 76 | +1 | +0.07 |
| 80 | 0 | 0 |
| 84 | 0 | 0 |
| 88 | 0 | 0 |
| 92 | 0 | 0 |
| 96 | 0 | 0 |


### 5.8 Tracking de SF Pro — macOS

_Fuente: [typography](https://developer.apple.com/design/human-interface-guidelines/typography)_

| Size (points) | Tracking (1/1000 em) | Tracking (points) |
|---|---|---|
| 6 | +41 | +0.24 |
| 7 | +34 | +0.23 |
| 8 | +26 | +0.21 |
| 9 | +19 | +0.17 |
| 10 | +12 | +0.12 |
| 11 | +6 | +0.06 |
| 12 | 0 | 0.0 |
| 13 | -6 | -0.08 |
| 14 | -11 | -0.15 |
| 15 | -16 | -0.23 |
| 16 | -20 | -0.31 |
| 17 | -26 | -0.43 |
| 18 | -25 | -0.44 |
| 19 | -24 | -0.45 |
| 20 | -23 | -0.45 |
| 21 | -18 | -0.36 |
| 22 | -12 | -0.26 |
| 23 | -4 | -0.10 |
| 24 | +3 | +0.07 |
| 25 | +6 | +0.15 |
| 26 | +8 | +0.22 |
| 27 | +11 | +0.29 |
| 28 | +14 | +0.38 |
| 29 | +14 | +0.40 |
| 30 | +14 | +0.40 |
| 31 | +13 | +0.39 |
| 32 | +13 | +0.41 |
| 33 | +12 | +0.40 |
| 34 | +12 | +0.40 |
| 35 | +11 | +0.38 |
| 36 | +10 | +0.37 |
| 37 | +10 | +0.36 |
| 38 | +10 | +0.37 |
| 39 | +10 | +0.38 |
| 40 | +10 | +0.37 |
| 41 | +9 | +0.36 |
| 42 | +9 | +0.37 |
| 43 | +9 | +0.38 |
| 44 | +8 | +0.37 |
| 45 | +8 | +0.35 |
| 46 | +8 | +0.36 |
| 47 | +8 | +0.37 |
| 48 | +8 | +0.35 |
| 49 | +7 | +0.33 |
| 50 | +7 | +0.34 |
| 51 | +7 | +0.35 |
| 52 | +6 | +0.31 |
| 53 | +6 | +0.33 |
| 54 | +6 | +0.32 |
| 56 | +6 | +0.30 |
| 58 | +5 | +0.28 |
| 60 | +4 | +0.26 |
| 62 | +4 | +0.24 |
| 64 | +4 | +0.22 |
| 66 | +3 | +0.19 |
| 68 | +2 | +0.17 |
| 70 | +2 | +0.14 |
| 72 | +2 | +0.14 |
| 76 | +1 | +0.07 |
| 80 | 0 | 0 |
| 84 | 0 | 0 |
| 88 | 0 | 0 |
| 92 | 0 | 0 |
| 96 | 0 | 0 |


Tracking de SF Pro Rounded, New York, tvOS, SF Compact y SF Compact Rounded: en
`references/hig/foundations/typography.md` (sección Tracking values).

## 6. Tamaños mínimos de controles y espaciado

Fuente: [Accessibility › Mobility](https://developer.apple.com/design/human-interface-guidelines/accessibility#Mobility).

_Fuente: [accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)_

| Platform | Default control size | Minimum control size |
|---|---|---|
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |
| tvOS | 66x66 pt | 56x56 pt |
| visionOS | 60x60 pt | 28x28 pt |
| watchOS | 44x44 pt | 28x28 pt |


- Espaciado: «add about 12 points of padding around elements that include a bezel; for elements without a
  bezel, it works well to add about 24 points of padding around the element’s visible edges» (Accessibility).
- visionOS: «place buttons so their centers are at least 60 points apart» ([Layout › visionOS](https://developer.apple.com/design/human-interface-guidelines/layout#visionOS));
  y «a margin of at least 16 points around the bounds of each item» ([Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes)).
- watchOS: no más de tres botones con glifo o dos con texto en una fila ([Layout › watchOS](https://developer.apple.com/design/human-interface-guidelines/layout#watchOS)).

### Botones de visionOS — tamaños disponibles

_Fuente: [buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)_

| Shape | Mini (28 pt) | Small (32 pt) | Regular (44 pt) | Large (52 pt) | Extra large (64 pt) |
|---|---|---|---|---|---|
| Circular | ✓ | ✓ | ✓ | ✓ | ✓ |
| Capsule (text only) |  | ✓ | ✓ | ✓ |  |
| Capsule (text and icon) |  |  | ✓ | ✓ |  |
| Rounded rectangle |  | ✓ | ✓ | ✓ |  |


### macOS — tamaños de control (vídeo)

«On macOS, Mini, Small, and Medium controls will continue using rounded rectangles… Large controls will now use
capsule shapes, alongside with the new X-Large size» — [Get to know the new design system, 4:23](https://developer.apple.com/videos/play/wwdc2025/356/?time=263).

## 7. Márgenes y zonas seguras publicadas

- tvOS: «Inset primary content 60 points from the top and bottom of the screen, and 80 points from the sides»
  ([Layout › tvOS](https://developer.apple.com/design/human-interface-guidelines/layout#tvOS)).
- Widgets: «Use the standard margin width for widgets — 16 points for most widgets» ([Widgets](https://developer.apple.com/design/human-interface-guidelines/widgets)).
- Live Activities: «The standard layout margin for Live Activities on the Lock Screen is 14 points» ([Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities)).
- iOS/iPadOS: las HIG no publican un margen numérico; piden respetar *layout margins* y *safe areas* del sistema
  ([Layout › Guides and safe areas](https://developer.apple.com/design/human-interface-guidelines/layout#Guides-and-safe-areas)).
- iPhone Duo: diseña para *compact width* (pantalla exterior) y *regular width* (interior); usa márgenes de layout
  e insets horizontales de safe area ([Design for iPhone Duo, 3:42](https://developer.apple.com/videos/play/tech-talks/111466/?time=222)).

### Rejillas de tvOS

_Fuente: [layout](https://developer.apple.com/design/human-interface-guidelines/layout)_

**Two-column grid**

| Attribute | Value |
|---|---|
| Unfocused content width | 860 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Three-column grid**

| Attribute | Value |
|---|---|
| Unfocused content width | 560 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Four-column grid**

| Attribute | Value |
|---|---|
| Unfocused content width | 410 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Five-column grid**

| Attribute | Value |
|---|---|
| Unfocused content width | 320 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Six-column grid**

| Attribute | Value |
|---|---|
| Unfocused content width | 260 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Seven-column grid**

| Attribute | Value |
|---|---|
| Unfocused content width | 217 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Eight-column grid**

| Attribute | Value |
|---|---|
| Unfocused content width | 184 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Nine-column grid**

| Attribute | Value |
|---|---|
| Unfocused content width | 160 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |


## 8. Radios y formas

Las HIG **no publican radios de esquina numéricos** para componentes. La regla vigente es la
concentricidad ([Get to know the new design system, 3:42](https://developer.apple.com/videos/play/wwdc2025/356/?time=222)):

- **Fija**: radio constante.
- **Cápsula**: radio = mitad de la altura.
- **Concéntrica**: radio = radio del contenedor − padding.
- En iPhone, junto al borde de la pantalla, cápsula con margen extra; en iPad y Mac, forma concéntrica con el borde de la ventana.

## 9. Materiales

- Liquid Glass: variantes `regular` (por defecto, desenfoca y ajusta la luminosidad) y `clear` (muy translúcida, solo
  sobre fondos ricos en medios). Con `clear` sobre contenido brillante: «consider adding a dark dimming layer of 35% opacity»
  ([Materials](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass)).
- Materiales estándar de iOS/iPadOS: `ultraThin`, `thin`, `regular` (por defecto) y `thick`; evita
  `quaternaryLabel` sobre `thin` y `ultraThin` (contraste demasiado bajo).

_Fuente: [materials](https://developer.apple.com/design/human-interface-guidelines/materials)_

| Material | Recommended for |
|---|---|
| [ultraThin](https://developer.apple.com/documentation/swiftui/material/ultrathin) | Full-screen views that require a light color scheme |
| [thin](https://developer.apple.com/documentation/swiftui/material/thin) | Overlay views that partially obscure onscreen content and require a light color scheme |
| [regular](https://developer.apple.com/documentation/swiftui/material/regular) | Overlay views that partially obscure onscreen content |
| [thick](https://developer.apple.com/documentation/swiftui/material/thick) | Overlay views that partially obscure onscreen content and require a dark color scheme |


## 10. Iconos de app

_Fuente: [app-icons](https://developer.apple.com/design/human-interface-guidelines/app-icons)_

| Platform | Layout shape | Icon shape after system masking | Layout size | Style | Appearances |
|---|---|---|---|---|---|
| iOS, iPadOS, macOS | Square | Rounded rectangle (square) | 1024x1024 px | Layered | Default, dark, clear light, clear dark, tinted light, tinted dark |
| tvOS | Rectangle (landscape) | Rounded rectangle (rectangular) | 800x480 px | Layered (Parallax) | N/A |
| visionOS | Square | Circular | 1024x1024 px | Layered (3D) | N/A |
| watchOS | Square | Circular | 1088x1088 px | Layered | N/A |


Más detalle (capas, apariencias, Icon Composer) en `references/hig/foundations/app-icons.md` y en los vídeos
`references/videos/2025-220.md` y `2025-361.md`.

## 11. Huecos (no publicados en las HIG vigentes)

- RGB de los colores semánticos (label, systemBackground, separator…): no se publican.
- Radios de esquina numéricos de componentes: no se publican (usa concentricidad).
- Tablas de tamaño de pantalla por dispositivo: retiradas de *Layout* en la actualización del 9-9-2026.
- Tabla de Dynamic Type de visionOS: no se publica.
