# Pull-down buttons — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons
- Descargado: 2026-10-15
- Sección: components › Menus and actions
- Plataformas: ios,ipados,macos,visionos
- Última actualización: 2022-09-14 — Refined guidance on designing a useful menu length.

> Resumen de Apple: A pull-down button displays a menu of items or actions that directly relate to the button’s purpose.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- After people choose an item in a pull-down button’s menu, the menu closes, and the app performs the chosen action.

### Best practices

- **Use a pull-down button to present commands or items that are directly related to the button’s action.**
  - An Add button could present a menu that lets people specify the item they want to add.
  - A Sort button could use a menu to let people select an attribute on which to sort.
  - A Back button could let people choose a specific location to revisit instead of opening the previous one.
- If you need to provide a list of mutually exclusive choices that aren’t commands, use a [pop-up…
- **Avoid putting all of a view’s actions in one pull-down button.**
- **Balance menu length with ease of use.**
- **Display a succinct menu title only if it adds meaning.**
- **Let people know when a pull-down button’s menu item is destructive, and ask them to confirm their intent.**
- **Include an interface icon with a menu item when it provides value.**

### Platform considerations

- *No additional considerations for macOS or visionOS.

#### iOS, iPadOS

> **Note:** You can also let people reveal a pull-down menu by performing a specific gesture on a button.
- **Consider using a More pull-down button to present items that don’t need prominent positions in the main interface.**

## Recursos relacionados

- *Related:*
  - [Pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons)
  - [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)
  - [Menus](https://developer.apple.com/design/human-interface-guidelines/menus)
- *Developer documentation:*
  - [MenuPickerStyle](https://developer.apple.com/documentation/swiftui/menupickerstyle) — SwiftUI
  - [showsMenuAsPrimaryAction](https://developer.apple.com/documentation/uikit/uicontrol/showsmenuasprimaryaction) — UIKit
  - [pullsDown](https://developer.apple.com/documentation/appkit/nspopupbutton/pullsdown) — AppKit

## Registro de cambios

| Date | Changes |
|---|---|
| September 14, 2022 | Refined guidance on designing a useful menu length. |
