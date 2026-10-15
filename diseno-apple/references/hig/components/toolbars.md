# Toolbars — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/toolbars
- Descargado: 2026-10-15
- Sección: components › Menus and actions
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2025-12-16 — Updated guidance for Liquid Glass.

> Resumen de Apple: A toolbar provides convenient access to frequently used commands, controls, navigation, and search.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- A toolbar consists of one or more sets of controls arranged horizontally along the top or bottom edge of the view, grouped into logical sections.
- Toolbars act on content in the view, facilitate navigation, and help orient people in the app.
  - The title of the current view
  - Navigation controls, like back and forward, and [search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields)
  - Actions, or bar items, like [buttons](https://developer.apple.com/design/human-interface-guidelines/buttons) and…
- In contrast to a toolbar, a [tab bar](https://developer.apple.com/design/human-interface-guidelines/tab-bars) is specifically for navigating between areas of an app.

### Best practices

- **Choose items deliberately to avoid overcrowding.**
> **Note:** The system automatically adds an overflow menu in macOS or iPadOS when items no longer fit.
- **Add a More menu to contain additional actions.**
- **In iPadOS and macOS apps, consider letting people customize the toolbar to include their most common items.**
- **Reduce the use of toolbar backgrounds and tinted controls.**
- **Avoid applying a similar color to toolbar item labels and content layer backgrounds.**
- **Prefer using standard components in a toolbar.**
- **Consider temporarily hiding toolbars for a distraction-free experience.**

### Titles

- **Provide a useful title for each window.**
- **Don’t title windows with your app name.**
- **Write a concise title.**
  - «Aim for a word or short phrase that distills the purpose of the window or view, and keep the title under 15 characters long so you leave enough room for other controls.»

### Navigation

- A toolbar with navigation controls appears at the top of a window, helping people move through a hierarchy of content.
- **Use the standard Back and Close buttons.**
  - ❌ Ejemplo incorrecto: An illustration of a capsule-shape Back button that includes the Back symbol on the leading side, grouped with Back in text on the trailing side.
  - ✅ Ejemplo correcto: An illustration of the standard circular Back button that includes the standard Back symbol.

### Actions

- **Provide actions that support the main tasks people perform.**
- **Make sure the meaning of each control is clear.**
  - «Prefer simple, recognizable symbols for items instead of text, except for actions like *edit* that aren’t well-represented by symbols.»
  - ❌ Ejemplo incorrecto: An illustration of an item group with text button labels for Filter, Delete, and New.
  - ✅ Ejemplo correcto: An illustration of an item group with symbol button labels for Filter, Delete, and New.
- **Prefer system-provided symbols without borders.**
  - ❌ Ejemplo incorrecto: An illustration of an item group with buttons for Filter and More. The buttons are labeled with symbols with circular borders.
  - ✅ Ejemplo correcto: An illustration of an item group with buttons for Filter and More. The buttons are labeled with symbols without borders.
- **Use the `.prominent` style for key actions such as Done or Submit.**

### Item groupings

- You can position toolbar items in three locations: the leading edge, center area, and trailing edge of the toolbar.
  - **Leading edge.** Elements that let people return to the previous document and show or hide a sidebar appear at the far leading edge, followed by the view title.
  - **Center area.** Common, useful controls appear in the center area, and the view title can appear here if it’s not on the leading edge.
  - **Trailing edge.** The trailing edge contains important items that need to remain available, buttons that open nearby inspectors, an optional search field, and the More menu that…
- To position items in the groupings you want, pin them to the leading edge, center, or trailing edge, and insert space between buttons or other items where appropriate.
- **Group toolbar items logically by function and frequency of use.**
- **Group navigation controls and critical actions like Done, Close, or Save in dedicated, familiar, and visually distinct sections.**
  - ❌ Ejemplo incorrecto: An illustration of a top toolbar on iPhone, with controls for back, forward, tool selection, and the More menu grouped in a single section on the trailing edge.
  - ✅ Ejemplo correcto: An illustration of a top toolbar on iPhone, with controls for back and forward grouped on the leading edge, and controls for tool selection and the More menu grouped on the trailing edge.
- **Keep consistent groupings and placement across platforms.**
- **Minimize the number of groups.**
- **Keep actions with text labels separate.**
  - ❌ Ejemplo incorrecto: An illustration of a top toolbar on iPhone, with an Edit control with a text label and a Share control with a symbol grouped together on the trailing edge.
  - ✅ Ejemplo correcto: An illustration of a top toolbar on iPhone, with an Edit control with a text label and a Share control with a symbol grouped into individual sections on the trailing edge.

### Platform considerations

- *No additional considerations for tvOS.*

#### iOS

- **Prioritize only the most important items for inclusion in the main toolbar area.**
- **Use a large title to help people stay oriented as they navigate and scroll.**

#### iPadOS

- **Consider combining a toolbar with a tab bar.**

#### macOS

- In a macOS app, the toolbar resides in the frame at the top of a window, either below or integrated with the title bar.
- **Make every toolbar item available as a command in the menu bar.**

#### visionOS

- In visionOS, the system-provided toolbar appears along the bottom edge of a window, above the window-management controls, and in a parallel plane that’s slightly in front of the…
- To maintain the legibility of toolbar items as content scrolls behind them, visionOS uses a variable blur in the bar background.
- In visionOS, you can supply either a symbol or a text label for each toolbar item.
- **Prefer using a system-provided toolbar.**
- **Avoid creating a vertical toolbar.**
- **Try to prevent windows from resizing below the width of the toolbar.**
- **If your app can enter a modal state, consider offering contextually relevant toolbar controls.**
- **Avoid using a pull-down menu in a toolbar.**

#### watchOS

- A toolbar button lets you offer important app functionality in a view that displays related content.
- For developer guidance, see [topBarLeading](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/topbarleading),…
- You can also place a button in the scrolling view.
- For developer guidance, see [primaryAction](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/primaryaction).
- **Use a scrolling toolbar button for an important action that isn’t a primary app function.**

## Recursos relacionados

- *Related:*
  - [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars)
  - [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars)
  - [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
  - [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)
  - [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields)
  - [Apple Design Resources](https://developer.apple.com/design/resources/)
- *Developer documentation:*
  - [Toolbars](https://developer.apple.com/documentation/swiftui/toolbars) — SwiftUI
  - [UIToolbar](https://developer.apple.com/documentation/uikit/uitoolbar) — UIKit
  - [NSToolbar](https://developer.apple.com/documentation/appkit/nstoolbar) — AppKit

## Vídeos que la explican

- [Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356) → `references/videos/2025-356.md`

## Registro de cambios

| Date | Changes |
|---|---|
| December 16, 2025 | Updated guidance for Liquid Glass. |
| June 9, 2025 | Added guidance for grouping bar items, updated guidance for using symbols, and incorporated navigation bar guidance. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Updated guidance for using toolbars in watchOS. |
