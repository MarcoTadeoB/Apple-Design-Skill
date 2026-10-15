# Action sheets — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/action-sheets
- Descargado: 2026-10-15
- Sección: components › Presentation
- Plataformas: ios,ipados,macos,tvos,watchos
- Última actualización: sin registro de cambios

> Resumen de Apple: An action sheet is a modal view that presents choices related to an action people initiate.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
> **Developer note:** When you use SwiftUI, you can offer action sheet functionality in all platforms by specifying a [presentation modifier](https://developer.apple.com/documentation/swiftui/view-presentation) for a confirmation dialog.

### Best practices

- **Use an action sheet — not an alert — to offer choices related to an intentional action.**
- **Use action sheets sparingly.**
- **Aim to keep titles short enough to display on a single line.**
- **Provide a message only if necessary.**
- **If necessary, provide a Cancel button that lets people reject an action that might destroy data.**
- **Make destructive choices visually prominent.**

### Platform considerations

- *No additional considerations for macOS or tvOS.

#### iOS, iPadOS

- **Use an action sheet — not a menu — to provide choices related to an action.**
- **Avoid letting an action sheet scroll.**

#### watchOS

- The system-defined style for action sheets includes a title, an optional message, a Cancel button, and one or more additional buttons.
- Each button has an associated style that conveys information about the button’s effect.

| Style | Meaning |
|---|---|
| Default | The button has no special meaning. |
| Destructive | The button destroys user data or performs a destructive action in the app. |
| Cancel | The button dismisses the view without taking any action. |

- **Avoid displaying more than four buttons in an action sheet, including the Cancel button.**

## Recursos relacionados

- *Related:*
  - [Modality](https://developer.apple.com/design/human-interface-guidelines/modality)
  - [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets)
  - [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts)
- *Developer documentation:*
  - [confirmationDialog(_:isPresented:titleVisibility:actions:)](https://developer.apple.com/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:actions:)-46zbb) — SwiftUI
  - [UIAlertController.Style.actionSheet](https://developer.apple.com/documentation/uikit/uialertcontroller/style/actionsheet) — UIKit
