# Text fields — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/text-fields
- Descargado: 2026-10-15
- Sección: components › Selection and input
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2023-06-05 — Updated guidance to reflect changes in watchOS 10.

> Resumen de Apple: A text field is a rectangular area in which people enter or edit small, specific pieces of text.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
### Best practices

- **Use a text field to request a small amount of information, such as a name or an email address.**
- **Show a hint in a text field to help communicate its purpose.**
- **Use secure text fields to hide private data.**
- **To the extent possible, match the size of a text field to the quantity of anticipated text.**
- **Evenly space multiple text fields.**
- **Ensure that tabbing between multiple fields flows as people expect.**
- **Validate fields when it makes sense.**
- **Use a number formatter to help with numeric data.**
- **Adjust line breaks according to the needs of the field.**
- **Consider using an expansion tooltip to show the full version of clipped or truncated text.**
- **In iOS, iPadOS, tvOS, and visionOS apps, show the appropriate keyboard type.**
- **Minimize text entry in your tvOS and watchOS apps.**

### Platform considerations

- *No additional considerations for tvOS or visionOS.*

#### iOS, iPadOS

- **Display a Clear button in the trailing end of a text field to help people erase their input.**
- **Use images and buttons to provide clarity and functionality in text fields.**

#### macOS

- **Consider using a combo box if you need to pair text input with a list of choices.**

#### watchOS

- **Present a text field only when necessary.**

## Recursos relacionados

- *Related:*
  - [Text views](https://developer.apple.com/design/human-interface-guidelines/text-views)
  - [Combo boxes](https://developer.apple.com/design/human-interface-guidelines/combo-boxes)
  - [Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data)
- *Developer documentation:*
  - [TextField](https://developer.apple.com/documentation/swiftui/textfield) — SwiftUI
  - [SecureField](https://developer.apple.com/documentation/swiftui/securefield) — SwiftUI
  - [UITextField](https://developer.apple.com/documentation/uikit/uitextfield) — UIKit
  - [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield) — AppKit

## Registro de cambios

| Date | Changes |
|---|---|
| June 5, 2023 | Updated guidance to reflect changes in watchOS 10. |
