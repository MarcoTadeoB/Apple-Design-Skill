# Disclosure controls — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/disclosure-controls
- Descargado: 2026-10-15
- Sección: components › Layout and organization
- Plataformas: ios,ipados,macos,visionos
- Última actualización: sin registro de cambios

> Resumen de Apple: Disclosure controls reveal and hide information and functionality related to specific controls or views.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
### Best practices

- **Use a disclosure control to hide details until they’re relevant.**

### Disclosure triangles

- A disclosure triangle shows and hides information and functionality associated with a view or a list of items.
- A disclosure triangle points inward from the leading edge when its content is hidden and down when its content is visible.
- **Provide a descriptive label when using a disclosure triangle.**
- For developer guidance, see [NSButton.BezelStyle.disclosure](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/disclosure).

### Disclosure buttons

- A disclosure button shows and hides functionality associated with a specific control.
- A disclosure button points down when its content is hidden and up when its content is visible.
- **Place a disclosure button near the content that it shows and hides.**
- **Use no more than one disclosure button in a single view.**
- For developer guidance, see [NSButton.BezelStyle.pushDisclosure](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/pushdisclosure).

### Platform considerations

- *No additional considerations for macOS.

#### iOS, iPadOS, visionOS

- Disclosure controls are available in iOS, iPadOS, and visionOS with the SwiftUI [DisclosureGroup](https://developer.apple.com/documentation/swiftui/disclosuregroup) view.

## Recursos relacionados

- *Related:*
  - [Outline views](https://developer.apple.com/design/human-interface-guidelines/outline-views)
  - [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)
  - [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)
- *Developer documentation:*
  - [DisclosureGroup](https://developer.apple.com/documentation/swiftui/disclosuregroup) — SwiftUI
  - [NSButton.BezelStyle.disclosure](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/disclosure) — AppKit
  - [NSButton.BezelStyle.pushDisclosure](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/pushdisclosure) — AppKit

## Vídeos que la explican

- [Stacks, Grids, and Outlines in SwiftUI](https://developer.apple.com/videos/play/wwdc2020/10031) → `references/videos/2020-10031.md`
