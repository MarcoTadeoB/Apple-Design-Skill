# Menus — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/menus
- Descargado: 2026-10-15
- Sección: components › Menus and actions
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2026-06-08 — Updated guidance for menu item icons.

> Resumen de Apple: A menu reveals its options when people interact with it, making it a space-efficient way to present commands in your app or game.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Menus are ubiquitous in apps and games, so most people already know how to use them.
> **Note:** Several system-provided components also include menus that support specific use cases.

### Labels

- A menu item’s label describes what it does and may include a symbol if it helps to clarify meaning.
> **Note:** Depending on menu layout, an iOS, iPadOS, or visionOS app can display a few unlabeled menu items that use only symbols or icons to identify them.
- **For each menu item, write a label that clearly and succinctly describes it.**
- **To be consistent with platform experiences, use title-style capitalization.**
  - «Although a game might have a different writing style, generally prefer using title-style capitalization, which capitalizes every word except articles, coordinating conjunctions, and short prepositions, and capitalizes the last word in the…»
- **Remove articles like *a*, *an*, and *the* from menu-item labels to save space.**
- **Show people when a menu item is unavailable.**
- **Append an ellipsis to a menu item’s label when the action requires more information before it can complete.**

### Icons

- **Represent common actions consistently.**
- **Use menu item icons sparingly and with purpose.**
  - ❌ Ejemplo incorrecto: An illustration of a menu containing the days of the week. Each menu item is represented by a different symbol with no relation to the corresponding day.
  - ✅ Ejemplo correcto: An illustration of a menu containing the days of the week with no accompanying symbols.
- **Apply a uniform visual treatment across menu items in the same group.**

### Organization

- Organizing menu items in ways that reflect how people use your app or game can make your experience feel straightforward and easy to use.
- **Prefer listing important or frequently used menu items first.**
- **Consider grouping logically related items.**
- **Prefer keeping all logically related commands in the same group, even if the commands don’t all have the same importance.**
- **Be mindful of menu length.**
  - «The exception is when a menu contains user-defined or dynamically generated content, like the History and Bookmarks menus in Safari.»

### Submenus

- Sometimes, a menu item can reveal a set of closely related items in a subordinate list called a *submenu*.
- **Use submenus sparingly.**
- **Limit the depth and length of submenus.**
- **Make sure a submenu remains available even when its nested menu items are unavailable.**
- **Prefer using a submenu to indenting menu items.**

### Toggled items

- Menu items often represent attributes or objects that people can turn on or off.
- **Consider using a changeable label that describes an item’s current state.**
- **Include a verb if a changeable label isn’t clear enough.**
- **If necessary, display both menu items instead of one toggled item.**
- **Consider using a checkmark to show that an attribute is currently in effect.**
- **Consider offering a menu item that makes it easy to remove multiple toggled attributes.**

### In-game menus

- In-game menus give players ways to control gameplay as well as determine [settings](https://developer.apple.com/design/human-interface-guidelines/settings) for the game as a whole.
- **Let players navigate in-game menus using the platform’s default interaction method.**
- **Make sure your menus remain easy to open and read on all platforms you support.**

### Platform considerations

- *No additional considerations for macOS, tvOS, or watchOS.*

#### iOS, iPadOS

- In iOS and iPadOS, a menu can display items in one of the following three layouts.
  - **Small.** A row of four items appears at the top of the menu, above a list that contains the remaining items.
  - **Medium.** A row of three items appears at the top of the menu, above a list that contains the remaining items.
  - **Large (the default).** The menu displays all items in a list.
- For developer guidance, see [preferredElementSize](https://developer.apple.com/documentation/uikit/uimenu/preferredelementsize).
- **Choose a small or medium menu layout when it can help streamline people’s choices.**

#### visionOS

- In visionOS, a menu can display items using the small or large layout styles that iOS and iPadOS define (for guidance, see [iOS,…
- **Prefer displaying a menu near the content it controls.**
- **Prefer the subtle breakthrough effect in most cases.**

## Recursos relacionados

- *Related:*
  - [Pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons)
  - [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons)
  - [Context menus](https://developer.apple.com/design/human-interface-guidelines/context-menus)
  - [The menu bar](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar)
- *Developer documentation:*
  - [Menu](https://developer.apple.com/documentation/swiftui/menu) — SwiftUI
  - [Menus and shortcuts](https://developer.apple.com/documentation/uikit/menus-and-shortcuts) — UIKit
  - [Menus](https://developer.apple.com/documentation/appkit/menus) — AppKit

## Registro de cambios

| Date | Changes |
|---|---|
| June 8, 2026 | Updated guidance for menu item icons. |
| December 16, 2025 | Added guidance for presenting menus with breakthrough effects in visionOS. |
| July 28, 2025 | Added guidance for representing menu items with icons. |
| June 10, 2024 | Added guidance for in-game menus and included game-specific examples. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | Added guidelines for using the small, medium, and large menu layouts in iPadOS. |
