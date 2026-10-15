# Column views — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/column-views
- Descargado: 2026-10-15
- Sección: components › Layout and organization
- Plataformas: macos
- Última actualización: sin registro de cambios

> Resumen de Apple: A column view — also called a *browser* — lets people view and navigate a data hierarchy using a series of vertical columns.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Each column represents one level of the hierarchy and contains horizontal rows of data items.
> **Note:** If you need to manage the presentation of hierarchical content in your iPadOS or visionOS app, consider using a [split view](https://developer.apple.com/design/human-interface-guidelines/split-views).

### Best practices

- Consider using a column view when you have a deep data hierarchy in which people tend to navigate back and forth frequently between levels, and you don’t need the sorting…
- **Show the root level of your data hierarchy in the first column.**
- **Consider showing information about the selected item when there are no nested items to display.**
- **Let people resize columns.**

### Platform considerations

- *Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.*

## Recursos relacionados

- *Related:*
  - [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)
  - [Outline views](https://developer.apple.com/design/human-interface-guidelines/outline-views)
  - [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views)
- *Developer documentation:*
  - [NSBrowser](https://developer.apple.com/documentation/appkit/nsbrowser) — AppKit
