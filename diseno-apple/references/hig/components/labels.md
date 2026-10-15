# Labels — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/labels
- Descargado: 2026-10-15
- Sección: components › Layout and organization
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2023-06-05 — Updated guidance to reflect changes in watchOS 10.

> Resumen de Apple: A label is a static piece of text that people can read and often copy, but not edit.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Labels display text throughout the interface, in buttons, menu items, and views, helping people understand the current context and what they can do next.
- The term *label* refers to uneditable text that can appear in various places.
  - Within a button, a label generally conveys what the button does, such as Edit, Cancel, or Send.
  - Within many lists, a label can describe each item, often accompanied by a symbol or an image.
  - Within a view, a label might provide additional context by introducing a control or describing a common action or task that people can perform in the view.
> **Developer note:** To display uneditable text, SwiftUI defines two components: [Label](https://developer.apple.com/documentation/swiftui/label) and [Text](https://developer.apple.com/documentation/swiftui/text).
- The guidance below can help you use a label to display text.

### Best practices

- **Use a label to display a small amount of text that people don’t need to edit.**
- **Prefer system fonts.**
- **Use system-provided label colors to communicate relative importance.**

| System color | Example usage | iOS, iPadOS, tvOS, visionOS | macOS |
|---|---|---|---|
| Label | Primary information | [label](https://developer.apple.com/documentation/uikit/uicolor/label) | [labelColor](https://developer.apple.com/documentation/appkit/nscolor/labelcolor) |
| Secondary label | A subheading or supplemental text | [secondaryLabel](https://developer.apple.com/documentation/uikit/uicolor/secondarylabel) | [secondaryLabelColor](https://developer.apple.com/documentation/appkit/nscolor/secondarylabelcolor) |
| Tertiary label | Text that describes an unavailable item or behavior | [tertiaryLabel](https://developer.apple.com/documentation/uikit/uicolor/tertiarylabel) | [tertiaryLabelColor](https://developer.apple.com/documentation/appkit/nscolor/tertiarylabelcolor) |
| Quaternary label | Watermark text | [quaternaryLabel](https://developer.apple.com/documentation/uikit/uicolor/quaternarylabel) | [quaternaryLabelColor](https://developer.apple.com/documentation/appkit/nscolor/quaternarylabelcolor) |

- **Make useful label text selectable.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, tvOS, or visionOS.*

#### macOS

> **Developer note:** To display uneditable text in a label, use the [isEditable](https://developer.apple.com/documentation/appkit/nstextfield/iseditable) property of [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield).

#### watchOS

- Date and time text components (shown below on the left) display the current date, the current time, or a combination of both.
- When you use the system-provided date and timer text components, watchOS automatically adjusts the label’s presentation to fit the available space.
- Consider using date and timer components in complications.

## Recursos relacionados

- *Related:*
  - [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields)
  - [Text views](https://developer.apple.com/design/human-interface-guidelines/text-views)
- *Developer documentation:*
  - [Label](https://developer.apple.com/documentation/swiftui/label) — SwiftUI
  - [Text](https://developer.apple.com/documentation/swiftui/text) — SwiftUI
  - [UILabel](https://developer.apple.com/documentation/uikit/uilabel) — UIKit
  - [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield) — AppKit

## Registro de cambios

| Date | Changes |
|---|---|
| June 5, 2023 | Updated guidance to reflect changes in watchOS 10. |
