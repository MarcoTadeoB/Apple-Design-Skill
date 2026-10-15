# Pop-up buttons — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons
- Descargado: 2026-10-15
- Sección: components › Menus and actions
- Plataformas: ios,ipados,macos,visionos
- Última actualización: 2023-10-24 — Added artwork.

> Resumen de Apple: A pop-up button displays a menu of mutually exclusive options.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- After people choose an item from a pop-up button’s menu, the menu closes, and the button can update its content to indicate the current selection.

### Best practices

- **Use a pop-up button to present a flat list of mutually exclusive options or states.**
  - Offer a list of actions
  - Let people select multiple items
  - Include a submenu
- **Provide a useful default selection.**
- **Give people a way to predict a pop-up button’s options without opening it.**
- **Consider using a pop-up button when space is limited and you don’t need to display all options all the time.**
- **If necessary, include a Custom option in a pop-up button’s menu to provide additional items that are useful in some situations.**

### Platform considerations

- *No additional considerations for iOS, macOS, or visionOS.

#### iPadOS

- **Within a popover or modal view, consider using a pop-up button instead of a disclosure indicator to present multiple options for a list item.**

## Recursos relacionados

- *Related:*
  - [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons)
  - [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)
  - [Menus](https://developer.apple.com/design/human-interface-guidelines/menus)
- *Developer documentation:*
  - [MenuPickerStyle](https://developer.apple.com/documentation/swiftui/menupickerstyle)  — SwiftUI
  - [changesSelectionAsPrimaryAction](https://developer.apple.com/documentation/uikit/uibutton/changesselectionasprimaryaction) — UIKit
  - [NSPopUpButton](https://developer.apple.com/documentation/appkit/nspopupbutton) — AppKit

## Registro de cambios

| Date | Changes |
|---|---|
| October 24, 2023 | Added artwork. |
| September 14, 2022 | Added a guideline on using a pop-up button in a popover or modal view in iPadOS. |
