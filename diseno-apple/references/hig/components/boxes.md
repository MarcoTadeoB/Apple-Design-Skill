# Boxes — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/boxes
- Descargado: 2026-10-15
- Sección: components › Layout and organization
- Plataformas: ios,ipados,macos,visionos
- Última actualización: sin registro de cambios

> Resumen de Apple: A box creates a visually distinct group of logically related information and components.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- By default, a box uses a visible border or background color to separate its contents from the rest of the interface.

### Best practices

- **Prefer keeping a box relatively small in comparison with its containing view.**
- **Consider using padding and alignment to communicate additional grouping within a box.**

### Content

- **Provide a succinct introductory title if it helps clarify the box’s contents.**
- **If you need a title, write a brief phrase that describes the contents.**
  - «Avoid ending punctuation unless you use a box in a settings pane, where you append a colon to the title.»

### Platform considerations

- *No additional considerations for visionOS.

#### iOS, iPadOS

- By default, iOS and iPadOS use the secondary and tertiary background [colors](https://developer.apple.com/design/human-interface-guidelines/color) in boxes.

#### macOS

- By default, macOS displays a box’s title above it.

## Recursos relacionados

- *Related:*
  - [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- *Developer documentation:*
  - [GroupBox](https://developer.apple.com/documentation/swiftui/groupbox) — SwiftUI
  - [NSBox](https://developer.apple.com/documentation/appkit/nsbox) — AppKit
