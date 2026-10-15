# Ornaments — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/ornaments
- Descargado: 2026-10-15
- Sección: components › Menus and actions
- Plataformas: visionos
- Última actualización: 2024-02-02 — Added guidance on using multiple ornaments.

> Resumen de Apple: In visionOS, an ornament presents controls and information related to a window, without crowding or obscuring the window’s contents.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- An ornament floats in a plane that’s parallel to its associated window and slightly in front of it along the z-axis.
- Ornaments can appear on any edge of a window and can contain UI components like buttons, segmented controls, and other views.

### Best practices

- **Consider using an ornament to present frequently needed controls or information in a consistent location that doesn’t clutter the window.**
- **In general, keep an ornament visible.**
- **If you need to display multiple ornaments, prioritize the overall visual balance of the window.**
- **Aim to keep an ornament’s width the same or narrower than the width of the associated window.**
- **Consider using borderless buttons in an ornament.**
- **Use system-provided toolbars and tab bars unless you need to create custom components.**

### Platform considerations

- *Not supported in iOS, iPadOS, macOS, tvOS, or watchOS.*

## Recursos relacionados

- *Related:*
  - [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
  - [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars)
- *Developer documentation:*
  - [ornament(visibility:attachmentAnchor:contentAlignment:ornament:)](https://developer.apple.com/documentation/swiftui/view/ornament(visibility:attachmentanchor:contentalignment:ornament:)) — SwiftUI

## Vídeos que la explican

- [Design for spatial user interfaces](https://developer.apple.com/videos/play/wwdc2023/10076) → `references/videos/2023-10076.md`

## Registro de cambios

| Date | Changes |
|---|---|
| February 2, 2024 | Added guidance on using multiple ornaments. |
| December 5, 2023 | Removed a statement about using ornaments to present supplementary items. |
| June 21, 2023 | New page. |
