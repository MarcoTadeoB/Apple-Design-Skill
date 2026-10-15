# Tokens de diseño de Apple — valores exactos

Generado desde la caché de las HIG ({{fecha}}). Cada tabla indica la página de origen. Los colores
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

<<tabla pagina="color" tras="System colors" seccion="Specifications" n="1">>

## 2. Grises de sistema de iOS y iPadOS

<<tabla pagina="color" tras="iOS, iPadOS system gray colors" n="1">>

La HIG añade: «In SwiftUI, the equivalent of `systemGray` is [gray](https://developer.apple.com/documentation/swiftui/color/gray).»

## 3. Colores dinámicos (semánticos)

Se definen por su **propósito**, no por su aspecto, y se adaptan solos a claro/oscuro/contraste. Las HIG
listan nombres y usos, **pero no publican sus valores RGB**.

### iOS, iPadOS

iOS define dos juegos de fondos dinámicos, *system* y *grouped* (`systemBackground`, `systemGroupedBackground`…),
cada uno con variantes primaria (vista general), secundaria (agrupar dentro de la vista) y terciaria (agrupar
dentro de elementos secundarios). Colores de primer plano:

<<tabla pagina="color" tras="iOS, iPadOS" seccion="Platform considerations" n="1">>

### macOS

<<tabla pagina="color" tras="macOS" seccion="Platform considerations" n="1">>

Dark Mode en iOS/iPadOS usa dos juegos de fondos, *base* (más tenue) y *elevated* (más brillante, para
popovers y sheets en primer plano) — [Dark Mode › iOS, iPadOS](https://developer.apple.com/design/human-interface-guidelines/dark-mode#iOS-iPadOS).
Dark Mode no existe en visionOS ni watchOS.

## 4. Contraste mínimo

Fuente: [Accessibility › Vision](https://developer.apple.com/design/human-interface-guidelines/accessibility#Vision).

<<tabla pagina="accessibility" tras="Vision" contiene="Minimum contrast ratio" n="1">>

Además ([Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Dark-Mode-colors)):
«make sure the contrast ratio between colors is no lower than 4.5:1. For custom foreground and background colors,
strive for a contrast ratio of 7:1, especially in small text.»

## 5. Tipografía

Fuentes del sistema: SF Pro (iOS, iPadOS, macOS, tvOS, visionOS), SF Compact (watchOS; SF Compact Rounded
en complicaciones), New York (NY) como serif — [Typography › Platform considerations](https://developer.apple.com/design/human-interface-guidelines/typography#Platform-considerations).
macOS no admite Dynamic Type. Pesos enfatizados: medium, semibold, bold o heavy (`bold()` en SwiftUI,
`traitBold` en UIKit).

### 5.1 Tamaño por defecto y mínimo por plataforma

<<tabla pagina="typography" tras="Ensuring legibility" contiene="Minimum size" n="1">>

### 5.2 iOS y iPadOS — Dynamic Type (tamaño por defecto: Large)

«Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.»

#### Large (por defecto)
<<tabla pagina="typography" tras="Large (default)" seccion="iOS, iPadOS Dynamic Type sizes" n="1">>

#### xSmall
<<tabla pagina="typography" tras="xSmall" seccion="iOS, iPadOS Dynamic Type sizes" n="1">>

#### Small
<<tabla pagina="typography" tras="Small" seccion="iOS, iPadOS Dynamic Type sizes" n="1">>

#### Medium
<<tabla pagina="typography" tras="Medium" seccion="iOS, iPadOS Dynamic Type sizes" n="1">>

#### xLarge
<<tabla pagina="typography" tras="xLarge" seccion="iOS, iPadOS Dynamic Type sizes" n="1">>

#### xxLarge
<<tabla pagina="typography" tras="xxLarge" seccion="iOS, iPadOS Dynamic Type sizes" n="1">>

#### xxxLarge
<<tabla pagina="typography" tras="xxxLarge" seccion="iOS, iPadOS Dynamic Type sizes" n="1">>

#### Tamaños de accesibilidad AX1–AX5
<<tabla pagina="typography" tras="AX1" seccion="iOS, iPadOS larger accessibility type sizes" n="1">>
<<tabla pagina="typography" tras="AX2" seccion="iOS, iPadOS larger accessibility type sizes" n="1">>
<<tabla pagina="typography" tras="AX3" seccion="iOS, iPadOS larger accessibility type sizes" n="1">>
<<tabla pagina="typography" tras="AX4" seccion="iOS, iPadOS larger accessibility type sizes" n="1">>
<<tabla pagina="typography" tras="AX5" seccion="iOS, iPadOS larger accessibility type sizes" n="1">>

### 5.3 macOS — estilos de texto integrados

<<tabla pagina="typography" tras="macOS built-in text styles" n="1">>

### 5.4 tvOS — estilos de texto integrados

<<tabla pagina="typography" tras="tvOS built-in text styles" n="1">>

### 5.5 watchOS — Dynamic Type

#### Large (por defecto en 40/41/42 mm)
<<tabla pagina="typography" tras="Large (default 40mm/41mm/42mm)" n="1">>

#### xLarge (por defecto en 44/45/49 mm)
<<tabla pagina="typography" tras="xLarge (default 44mm/45mm/49mm)" n="1">>

#### Small (por defecto en 38 mm)
<<tabla pagina="typography" tras="Small (default 38mm)" n="1">>

El resto (xSmall, xxLarge, xxxLarge, AX1–AX3) está en `references/hig/foundations/typography.md`.

### 5.6 visionOS

Las HIG no publican una tabla propia de Dynamic Type para visionOS. Dicen: «visionOS uses bolder versions of
the Dynamic Type body and title styles and it introduces Extra Large Title 1 and Extra Large Title 2» y que
el tracking de SF Pro es el mismo que en iOS («iOS, iPadOS, visionOS tracking values»).

### 5.7 Tracking (espaciado entre letras) de SF Pro — iOS, iPadOS y visionOS

Unidades: milésimas de em y puntos. Para CSS: `letter-spacing: <milésimas>/1000 em` (p. ej. +6 → `0.006em`).

<<tabla pagina="typography" tras="SF Pro" seccion="iOS, iPadOS, visionOS tracking values" n="1">>

### 5.8 Tracking de SF Pro — macOS

<<tabla pagina="typography" tras="macOS tracking values" n="1">>

Tracking de SF Pro Rounded, New York, tvOS, SF Compact y SF Compact Rounded: en
`references/hig/foundations/typography.md` (sección Tracking values).

## 6. Tamaños mínimos de controles y espaciado

Fuente: [Accessibility › Mobility](https://developer.apple.com/design/human-interface-guidelines/accessibility#Mobility).

<<tabla pagina="accessibility" tras="Mobility" contiene="Minimum control size" n="1">>

- Espaciado: «add about 12 points of padding around elements that include a bezel; for elements without a
  bezel, it works well to add about 24 points of padding around the element’s visible edges» (Accessibility).
- visionOS: «place buttons so their centers are at least 60 points apart» ([Layout › visionOS](https://developer.apple.com/design/human-interface-guidelines/layout#visionOS));
  y «a margin of at least 16 points around the bounds of each item» ([Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes)).
- watchOS: no más de tres botones con glifo o dos con texto en una fila ([Layout › watchOS](https://developer.apple.com/design/human-interface-guidelines/layout#watchOS)).

### Botones de visionOS — tamaños disponibles

<<tabla pagina="buttons" tras="visionOS" contiene="Mini (28 pt)" n="1">>

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

<<tabla pagina="layout" tras="Grids" n="8" cruzar="si">>

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

<<tabla pagina="materials" tras="tvOS" n="1">>

## 10. Iconos de app

<<tabla pagina="app-icons" tras="Specifications" n="1">>

Más detalle (capas, apariencias, Icon Composer) en `references/hig/foundations/app-icons.md` y en los vídeos
`references/videos/2025-220.md` y `2025-361.md`.

## 11. Huecos (no publicados en las HIG vigentes)

- RGB de los colores semánticos (label, systemBackground, separator…): no se publican.
- Radios de esquina numéricos de componentes: no se publican (usa concentricidad).
- Tablas de tamaño de pantalla por dispositivo: retiradas de *Layout* en la actualización del 9-9-2026.
- Tabla de Dynamic Type de visionOS: no se publica.
