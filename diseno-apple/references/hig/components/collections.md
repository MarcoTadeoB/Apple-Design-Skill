# Collections — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/collections
- Descargado: 2026-10-15
- Sección: components › Layout and organization
- Plataformas: ios,ipados,macos,tvos,visionos
- Última actualización: sin registro de cambios

> Resumen de Apple: A collection manages an ordered set of content and presents it in a customizable and highly visual layout.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Generally speaking, collections are ideal for showing image-based content.

### Best practices

- **Use the standard row or grid layout whenever possible.**
- **Consider using a table instead of a collection for text.**
- **Make it easy to choose an item.**
- **Add custom interactions when necessary.**
- **Consider using animations to provide feedback when people insert, delete, or reorder items.**

### Platform considerations

- *No additional considerations for macOS, tvOS, or visionOS.

#### iOS, iPadOS

- **Use caution when making dynamic layout changes.**
  - «If possible, try to avoid changing the layout while people are viewing and interacting with it, unless it’s in response to an explicit action.»

## Recursos relacionados

- *Related:*
  - [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)
  - [Image views](https://developer.apple.com/design/human-interface-guidelines/image-views)
  - [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- *Developer documentation:*
  - [UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview) — UIKit
  - [NSCollectionView](https://developer.apple.com/documentation/appkit/nscollectionview) — AppKit
