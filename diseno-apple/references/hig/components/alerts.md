# Alerts — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/alerts
- Descargado: 2026-10-15
- Sección: components › Presentation
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2024-02-02 — Enhanced guidance for using default and Cancel buttons.

> Resumen de Apple: An alert gives people critical information they need right away.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- For example, an alert can tell people about a problem, warn them when their action might destroy data, and give them an opportunity to confirm a purchase or another important…

### Best practices

- **Use alerts sparingly.**
- **Avoid using an alert merely to provide information.**
- **Avoid displaying alerts for common, undoable actions, even when they’re destructive.**
- **Avoid showing an alert when your app starts.**

### Anatomy

- An alert is a modal view that can look different in different platforms and devices.

### Content

- In all platforms, alerts display a title, optional informative text, and up to three buttons.
  - In iOS, iPadOS, macOS, and visionOS, an alert can include a text field.
  - Alerts in macOS and visionOS can include an icon and an accessory view.
  - macOS alerts can add a suppression [checkbox](https://developer.apple.com/design/human-interface-guidelines/toggles#Checkboxes) and a [Help…
- **In all alert copy, be direct, and use a neutral, approachable tone.**
- **Write a title that clearly and succinctly describes the situation.**
- **Include informative text only if it adds value.**
- **Avoid explaining alert buttons.**
- **If supported, include a text field only if you need people’s input to resolve the situation.**

### Buttons

- **Create succinct, logical button titles.**
- **Avoid using OK as the default button title unless the alert is purely informational.**
- **Place buttons where people expect.**
- **Use the destructive style to identify a button that performs a destructive action people didn’t deliberately choose.**
- **If there’s a destructive action, include a Cancel button to give people a clear, safe way to avoid the action.**
- **Provide alternative ways to cancel an alert when it makes sense.**

| Action | Platform |
|---|---|
| Exit to the Home Screen | iOS, iPadOS |
| Pressing Escape (Esc) or Command-Period (.) on an attached keyboard | iOS, iPadOS, macOS, visionOS |
| Pressing Menu on the remote | tvOS |

### Platform considerations

- *No additional considerations for tvOS or watchOS.*

#### iOS, iPadOS

- **Use an action sheet — not an alert — to offer choices related to an intentional action.**
- **When possible, avoid displaying an alert that scrolls.**

#### macOS

- macOS automatically displays your app icon in an alert, but you can supply an alternative icon or symbol.
  - Configure repeating alerts to let people suppress subsequent occurrences of the same alert.
  - Append a custom view if it’s necessary to provide additional information (for developer guidance, see…
  - Include a Help button that opens your help documentation (see [Help buttons](https://developer.apple.com/design/human-interface-guidelines/buttons#Help-buttons)).
- **Use a caution symbol sparingly.**

#### visionOS

- When your app is running in the Shared Space, visionOS displays an alert in front of the app’s window, slightly forward along the z-axis.
- If someone moves a window without dismissing its alert, the alert remains anchored to the window.
- If you need to display an accessory view in a visionOS alert, create a view that has a maximum height of 154 pt and a 16-pt corner radius.

## Recursos relacionados

- *Related:*
  - [Modality](https://developer.apple.com/design/human-interface-guidelines/modality)
  - [Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets)
  - [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets)
- *Developer documentation:*
  - [alert(_:isPresented:actions:)](https://developer.apple.com/documentation/swiftui/view/alert(_:ispresented:actions:)-1bkka) — SwiftUI
  - [UIAlertController](https://developer.apple.com/documentation/uikit/uialertcontroller) — UIKit
  - [NSAlert](https://developer.apple.com/documentation/appkit/nsalert) — AppKit

## Registro de cambios

| Date | Changes |
|---|---|
| February 2, 2024 | Enhanced guidance for using default and Cancel buttons. |
| September 12, 2023 | Added anatomy artwork for visionOS. |
| June 21, 2023 | Updated to include guidance for visionOS. |
