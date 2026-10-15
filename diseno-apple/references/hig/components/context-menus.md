# Context menus — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/context-menus
- Descargado: 2026-10-15
- Sección: components › Menus and actions
- Plataformas: ios,ipados,macos,tvos,visionos
- Última actualización: 2023-12-05 — Added guidance on hiding unavailable menu items.

> Resumen de Apple: A context menu provides access to functionality that’s directly related to an item, without cluttering the interface.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Although a context menu provides convenient access to frequently used items, it’s hidden by default, so people might not know it’s there.
  - The system-defined touch or pinch and hold gesture in visionOS, iOS, and iPadOS
  - Pressing the Control key while clicking a pointing device in macOS and iPadOS
  - Using a secondary click on a Magic Trackpad in macOS or iPadOS

### Best practices

- **Prioritize relevancy when choosing items to include in a context menu.**
- **Aim for a small number of menu items.**
- **Support context menus consistently throughout your app.**
- **Always make context menu items available in the main interface, too.**
- **If you need to use submenus to manage a menu’s complexity, keep them to one level.**
- **Hide unavailable menu items, don’t dim them.**
- **Aim to place the most frequently used menu items where people are likely to encounter them first.**
- **Show keyboard shortcuts in your app’s main menus, not in context menus.**
- **Follow best practices for using separators.**
- **In iOS, iPadOS, and visionOS, warn people about context menu items that can destroy data.**

### Content

- A context menu seldom displays a title.
- **Include a title in a context menu only if doing so clarifies the menu’s effect.**
- **Represent menu item actions with familiar icons.**

### Platform considerations

- *No additional considerations for tvOS.

#### iOS, iPadOS

- **Provide either a context menu or an edit menu for an item, but not both.**
- **In iPadOS, consider using a context menu to let people create a new object in your app.**
- In iOS and iPadOS, a context menu can display a preview of the current content near the list of commands.
- **Prefer a graphical preview that clarifies the target of a context menu’s commands.**
- **Ensure that your preview looks good as it animates.**

#### macOS

- On a Mac, a context menu is sometimes called a *contextual* menu.

#### visionOS

- **Consider using a context menu instead of a panel or inspector window to present frequently used functionality.**
- **In general, avoid letting a context menu’s height exceed the height of the window.**

## Recursos relacionados

- *Related:*
  - [Menus](https://developer.apple.com/design/human-interface-guidelines/menus)
  - [Edit menus](https://developer.apple.com/design/human-interface-guidelines/edit-menus)
  - [Pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons)
  - [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons)
- *Developer documentation:*
  - [contextMenu(menuItems:)](https://developer.apple.com/documentation/swiftui/view/contextmenu(menuitems:)) — SwiftUI
  - [UIContextMenuInteraction](https://developer.apple.com/documentation/uikit/uicontextmenuinteraction) — UIKit
  - [popUpContextMenu(_:with:for:)](https://developer.apple.com/documentation/appkit/nsmenu/popupcontextmenu(_:with:for:)) — AppKit

## Registro de cambios

| Date | Changes |
|---|---|
| December 5, 2023 | Added guidance on hiding unavailable menu items. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | Refined guidance on including a submenu and added a guideline on using a context menu to support object creation in an iPadOS app. |
