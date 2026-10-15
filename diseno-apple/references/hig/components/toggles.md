# Toggles — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/toggles
- Descargado: 2026-10-15
- Sección: components › Selection and input
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2024-03-29 — Enhanced guidance for using switches in macOS apps, clarified when a checkbox has a title, and added artwork for radio buttons.

> Resumen de Apple: A toggle lets people choose between a pair of opposing states, like on and off, using a different appearance to indicate each state.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- A toggle can have various styles, such as switch and checkbox, and different platforms can use these styles in different ways.
- In addition to toggles, all platforms also support buttons that behave like toggles by using a different appearance for each state.

### Best practices

- **Use a toggle to help people choose between two opposing values that affect the state of content or a view.**
- **Clearly identify the setting, view, or content the toggle affects.**
- **Make sure the visual differences in a toggle’s state are obvious.**

### Platform considerations

- *No additional considerations for tvOS, visionOS, or watchOS.*

#### iOS, iPadOS

- **Use the switch toggle style only in a list row.**
- **Change the default color of a switch only if necessary.**
- **Outside of a list, use a button that behaves like a toggle, not a switch.**
- **Avoid supplying a label that explains the button’s purpose.**

#### macOS

- In addition to the switch toggle style, macOS supports the checkbox style and also defines radio buttons that can provide similar behaviors.
- **Use switches, checkboxes, and radio buttons in the window body, not the window frame.**

##### Switches

- **Prefer a switch for settings that you want to emphasize.**
- **Within a grouped form, consider using a mini switch to control the setting in a single row.**
- **In general, don’t replace a checkbox with a switch.**

##### Checkboxes

- A checkbox is a small, square button that’s empty when the button is off, contains a checkmark when the button is on, and can contain a dash when the button’s state is mixed.
- **Use a checkbox instead of a switch if you need to present a hierarchy of settings.**
- **Consider using radio buttons if you need to present a set of more than two mutually exclusive options.**
- **Consider using a label to introduce a group of checkboxes if their relationship isn’t clear.**
- **Accurately reflect a checkbox’s state in its appearance.**

##### Radio buttons

- A radio button is a small, circular button followed by a label.
- A radio button’s state is either selected (a filled circle) or deselected (an empty circle).
- **Prefer a set of radio buttons to present mutually exclusive options.**
- **Avoid listing too many radio buttons in a set.**
- **To present a single setting that can be on or off, prefer a checkbox.**
- **Use consistent spacing when you display radio buttons horizontally.**

## Recursos relacionados

- *Related:*
  - [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- *Developer documentation:*
  - [Toggle](https://developer.apple.com/documentation/swiftui/toggle) — SwiftUI
  - [UISwitch](https://developer.apple.com/documentation/uikit/uiswitch) — UIKit
  - [NSButton.ButtonType.toggle](https://developer.apple.com/documentation/appkit/nsbutton/buttontype/toggle) — AppKit
  - [NSSwitch](https://developer.apple.com/documentation/appkit/nsswitch) — AppKit

## Registro de cambios

| Date | Changes |
|---|---|
| March 29, 2024 | Enhanced guidance for using switches in macOS apps, clarified when a checkbox has a title, and added artwork for radio buttons. |
| September 12, 2023 | Updated artwork. |
