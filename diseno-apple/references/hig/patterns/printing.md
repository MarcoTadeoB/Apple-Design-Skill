# Printing — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/printing
- Descargado: 2026-10-15
- Sección: patterns
- Plataformas: ios,ipados,macos,visionos
- Última actualización: sin registro de cambios

> Resumen de Apple: An iOS, iPadOS, macOS, or visionOS app can integrate system-provided print functionality when it makes sense, presenting custom printer- and document-specific options if necessary.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
### Best practices

- **Make printing discoverable.**
- **Present a printing option only when it’s possible.**
- **Present relevant printing options.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, or visionOS.

#### macOS

- **If your macOS app offers app-specific print options that the system doesn’t offer, consider creating a custom category for the print panel.**
- **If your app supports document-specific page settings, consider presenting a page setup dialog.**
- **Make sure interdependencies between options are clear.**
- **Separate advanced features from frequently used features.**
- **Consider letting people preview the effect of a setting.**
- **Consider storing modified settings with the document.**

## Recursos relacionados

- *Related:*
  - [File management](https://developer.apple.com/design/human-interface-guidelines/file-management)
  - [File menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#File-menu)
- *Developer documentation:*
  - [UIPrintInteractionController](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller) — UIKit
  - [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) — AppKit
