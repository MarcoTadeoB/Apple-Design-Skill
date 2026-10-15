# Popovers — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/popovers
- Descargado: 2026-10-15
- Sección: components › Presentation
- Plataformas: ios,ipados,macos,visionos
- Última actualización: sin registro de cambios

> Resumen de Apple: A popover is a transient view that appears above other content when people click or tap a control or interactive area.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
### Best practices

- **Use a popover to expose a small amount of information or functionality.**
- **Consider using popovers when you want more room for content.**
- **Position popovers appropriately.**
- **Use a Close button for confirmation and guidance only.**
- **Always save work when automatically closing a nonmodal popover.**
- **Show one popover at a time.**
- **Don’t show another view over a popover.**
  - «Make sure nothing displays on top of a popover, except for an alert.»
- **When possible, let people close one popover and open another with a single click or tap.**
- **Avoid making a popover too big.**
- **Provide a smooth transition when changing the size of a popover.**
- **Avoid using the word *popover* in help documentation.**
- **Avoid using a popover to show a warning.**

### Platform considerations

- *No additional considerations for visionOS.

#### iOS, iPadOS

- **Avoid displaying popovers in compact views.**

#### macOS

- You can make a popover detachable in macOS, which becomes a separate panel when people drag it.
- **Consider letting people detach a popover.**
- **Make minimal appearance changes to a detached popover.**

## Recursos relacionados

- *Related:*
  - [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets)
  - [Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets)
  - [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts)
  - [Modality](https://developer.apple.com/design/human-interface-guidelines/modality)
- *Developer documentation:*
  - [popover(isPresented:attachmentAnchor:arrowEdge:content:)](https://developer.apple.com/documentation/swiftui/view/popover(ispresented:attachmentanchor:arrowedge:content:)) — SwiftUI
  - [UIPopoverPresentationController](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller) — UIKit
  - [NSPopover](https://developer.apple.com/documentation/appkit/nspopover) — AppKit
