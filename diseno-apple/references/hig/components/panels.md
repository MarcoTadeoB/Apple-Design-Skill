# Panels — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/panels
- Descargado: 2026-10-15
- Sección: components › Presentation
- Plataformas: macos
- Última actualización: sin registro de cambios

> Resumen de Apple: In a macOS app, a panel typically floats above other open windows providing supplementary controls, options, or information related to the active window or current selection.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- In general, a panel has a less prominent appearance than an app’s [main window](https://developer.apple.com/design/human-interface-guidelines/windows#macOS-window-states).
- When your app runs in other platforms, consider using a modal view to present supplementary content that’s relevant to the current task or selection.

### Best practices

- **Use a panel to give people quick access to important controls or information related to the content they’re working with.**
- **Consider using a panel to present inspector functionality.**
- **Prefer simple adjustment controls in a panel.**
- **Write a brief title that describes the panel’s purpose.**
- **Show and hide panels appropriately.**
- **Avoid including panels in the Window menu’s documents list.**
- **In general, avoid making a panel’s minimize button available.**
- **Refer to panels by title in your interface and in help documentation.**

### HUD-style panels

- A HUD-style panel serves the same function as a standard panel, but its appearance is darker and translucent.
- **Prefer standard panels.**
  - In a media-oriented app that presents movies, photos, or slides
  - When a standard panel would obscure essential content
  - When you don’t need to include controls — with the exception of the disclosure triangle, most system-provided controls don’t match a HUD’s appearance.
- **Maintain one panel style when your app switches modes.**
- **Use color sparingly in HUDs.**
- **Keep HUDs small.**
- For developer guidance, see [hudWindow](https://developer.apple.com/documentation/appkit/nswindow/stylemask-swift.struct/hudwindow).

### Platform considerations

- *Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.*

## Recursos relacionados

- *Related:*
  - [Windows](https://developer.apple.com/design/human-interface-guidelines/windows)
  - [Modality](https://developer.apple.com/design/human-interface-guidelines/modality)
- *Developer documentation:*
  - [NSPanel](https://developer.apple.com/documentation/appkit/nspanel) — AppKit
  - [hudWindow](https://developer.apple.com/documentation/appkit/nswindow/stylemask-swift.struct/hudwindow) — AppKit
