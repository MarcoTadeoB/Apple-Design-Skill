# Lists and tables — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/lists-and-tables
- Descargado: 2026-10-15
- Sección: components › Layout and organization
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2023-06-21 — Updated to include guidance for visionOS.

> Resumen de Apple: Lists and tables present data in one or more columns of rows.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- A table or list can represent data that’s organized in groups or hierarchies, and it can support user interactions like selecting, adding, deleting, and reordering.
- Sometimes, people need to work with complex data in a multicolumn table or a spreadsheet.

### Best practices

- **Prefer displaying text in a list or table.**
- **Let people edit a table when it makes sense.**
- **Provide appropriate feedback when people select a list item.**

### Content

- **Keep item text succinct so row content is comfortable to read.**
- **Consider ways to preserve readability of text that might otherwise get clipped or truncated.**
- **Use descriptive column headings in a multicolumn table.**

### Style

- **Choose a table or list style that coordinates with your data and platform.**
- **Choose a row style that fits the information you need to display.**

### Platform considerations

#### iOS, iPadOS, visionOS

- **Use an info button only to reveal more information about a row’s content.**
- **Avoid adding an index to a table that displays controls — like disclosure indicators — in the trailing ends of its rows.**

#### macOS

- **When it provides value, let people click a column heading to sort a table view based on that column**
- **Let people resize columns.**
- **Consider using alternating row colors in a multicolumn table.**
- **Use an outline view instead of a table view to present hierarchical data.**

#### tvOS

- **Confirm that images near a table still look good as each row highlights and slightly increases in size when it becomes focused.**

#### watchOS

- **When possible, limit the number of rows.**
- **Constrain the length of detail views if you want to support vertical page-based navigation.**

## Recursos relacionados

- *Related:*
  - [Collections](https://developer.apple.com/design/human-interface-guidelines/collections)
  - [Outline views](https://developer.apple.com/design/human-interface-guidelines/outline-views)
  - [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- *Developer documentation:*
  - [List](https://developer.apple.com/documentation/swiftui/list) — SwiftUI
  - [Tables](https://developer.apple.com/documentation/swiftui/tables) — SwiftUI
  - [UITableView](https://developer.apple.com/documentation/uikit/uitableview) — UIKit
  - [NSTableView](https://developer.apple.com/documentation/appkit/nstableview) — AppKit

## Vídeos que la explican

- [Stacks, Grids, and Outlines in SwiftUI](https://developer.apple.com/videos/play/wwdc2020/10031) → `references/videos/2020-10031.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Updated guidance to reflect changes in watchOS 10. |
