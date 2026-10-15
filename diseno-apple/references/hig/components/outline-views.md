# Outline views — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/outline-views
- Descargado: 2026-10-15
- Sección: components › Layout and organization
- Plataformas: macos
- Última actualización: sin registro de cambios

> Resumen de Apple: An outline view presents hierarchical data in a scrolling list of cells that are organized into columns and rows.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- ![A stylized representation of a list of folders and images, displayed in an outline view containing four columns: [Name], [Date Modified], [Size], and [Kind].
  - «The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://developer.apple.com/images/com.apple.HIG/components-outline-view-intro@2x.png)»
- An outline view includes at least one column that contains primary hierarchical data, such as a set of parent containers and their children.
- Finder windows offer an outline view for navigating the file system.

### Best practices

- Outline views work well to display text-based content and often appear in the leading side of a [split…
- **Use a table instead of an outline view to present data that’s not hierarchical.**
- **Expose data hierarchy in the first column only.**
- **Use descriptive column headings to provide context.**
- **Consider letting people click column headings to sort an outline view.**
- **Let people resize columns.**
- **Make it easy for people to expand or collapse nested containers.**
- **Retain people’s expansion choices.**
- **Consider using alternating row colors in multi-column outline views.**
- **Let people edit data if it makes sense in your app.**
- **Consider using a centered ellipsis to truncate cell text instead of clipping it.**
- **Consider offering a search field to help people find values quickly in a lengthy outline view.**

### Platform considerations

- *Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.*

## Recursos relacionados

- *Related:*
  - [Column views](https://developer.apple.com/design/human-interface-guidelines/column-views)
  - [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)
  - [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views)
- *Developer documentation:*
  - [OutlineGroup](https://developer.apple.com/documentation/swiftui/outlinegroup) — SwiftUI
  - [NSOutlineView](https://developer.apple.com/documentation/appkit/nsoutlineview) — AppKit

## Vídeos que la explican

- [Stacks, Grids, and Outlines in SwiftUI](https://developer.apple.com/videos/play/wwdc2020/10031) → `references/videos/2020-10031.md`
