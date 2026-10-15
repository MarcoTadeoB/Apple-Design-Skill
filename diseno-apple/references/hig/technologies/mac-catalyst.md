# Mac Catalyst — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/mac-catalyst
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ipados,macos
- Última actualización: 2023-05-02 — Consolidated guidance into one page.

> Resumen de Apple: When you use Mac Catalyst to create a Mac version of your iPad app, you give people the opportunity to enjoy the experience in a new environment.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
### Before you start

- Many iPad apps are great candidates for creating a Mac app built with Mac Catalyst.
- **Drag and drop.**
- **Keyboard navigation and shortcuts.**
- **Multitasking.**
- **Multiple windows**
- Although great iPad apps can provide a solid foundation for creating a Mac app built with Mac Catalyst, some apps rely on frameworks or features that don’t exist on a Mac.
- Creating a Mac version of your iPad app with Mac Catalyst gives the app automatic support for fundamental macOS features such as:
  - Pointer interactions and keyboard-based focus and navigation
  - Window management
  - Toolbars
  - Rich text interaction, including copy and paste as well as contextual menus for editing
  - File management
  - Menu bar menus
  - App-specific settings in the system-provided Settings app
- System-provided UI elements take on a more Mac-like appearance, too; for example:
  - Split view
  - File browser
  - Activity view
  - Form sheet
  - Contextual actions
  - Color picker
- To learn more about the characteristics that distinguish the Mac experience, see [Designing for…
> **Developer note:** To discover how views and controls can change when you create a Mac app using Mac Catalyst, download [UIKit Catalog: Creating and customizing views and…

### Choose an idiom

- When you first create your Mac app using Mac Catalyst, Xcode defaults to the “Scale Interface to Match iPad” setting, or *iPad idiom*.
  - «For example, the system scales text that uses the iPadOS baseline font size of 17pt down to 13pt in macOS.»
- When your app feels at home on the Mac using the iPad idiom, consider switching to the *Mac idiom*.
- You’re most likely to benefit from the Mac idiom if your app displays a lot of text, detailed artwork, or animations, but choosing this idiom can also mean that you need to spend…
- **When you adopt the Mac idiom, thoroughly audit your app’s layout, and plan to make changes to it.**
- **Adjust font sizes as needed.**
- **Make sure views and images look good in the Mac version of your app.**
> **Developer note:** When you adopt the Mac idiom, the unscaled views and interface elements report different metrics, often resulting in a significant amount of additional work.
- **Limit your appearance customizations to standard macOS appearance customizations that are the same or similar to those available in iPadOS.**

### Integrate the Mac experience

- When you use Mac Catalyst to create a Mac version of your iPad app, you need to ensure that your Mac app gives people a rich Mac experience.
- iPadOS and macOS each define patterns and conventions that are rooted in the different ways people use their devices.

#### Navigation

- Many iPad and Mac apps organize data in similar ways, but they use different controls and visual indicators to help people understand and navigate through the data.
- Typically, iPad apps use the following components to organize their content and features:
  - [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views).
  - [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars).
  - [Page controls](https://developer.apple.com/design/human-interface-guidelines/page-controls).
- If you use a tab bar in your iPad app, consider using a split view with a sidebar or a segmented control.
  - A split view with a sidebar displays a list of top-level items, each of which can disclose a list of child items.
  - A segmented control and a tab bar both accommodate similar interactions, such as mutually exclusive selection.
- **Make sure people retain access to important tab-bar items in the Mac version of your app.**
- **Offer multiple ways to move between pages.**

#### Inputs

- Although both iPad and Mac accept user input from a range of devices — such as keyboard, mouse, and trackpad — touch interactions are the basis for iPadOS conventions.
- Most iPadOS gestures convert automatically when you create your Mac app using Mac Catalyst; for example:

| iPadOS gesture… | Translates to mouse interaction |
|---|---|
| Tap | Left or right click |
| Touch and hold | Click and hold |
| Pan | Left click and drag |

| iPadOS gesture… | Translates to trackpad gesture |
|---|---|
| Tap | Click |
| Touch and hold | Click and hold |
| Pan | Click and drag |
| Pinch | Pinch |
| Rotate | Rotate |

> **Developer note:** The system sends the two touches in the pinch and rotate gestures to the view under the pointer, not the view under each touch.

#### App icons

- **Create a macOS version of your app icon.**

#### Layout

- To take advantage of the wider Mac screen in ways that give Mac users a great experience, consider updating your layout in the following ways:
  - Divide a single column of content and actions into multiple columns.
  - Use the regular-width and regular-height size classes, and consider reflowing elements in the content area to a side-by-side arrangement as people resize the window.
  - Present an inspector UI next to the main content instead of using a popover.
- **Consider moving controls from the main UI of your iPad app to your Mac app’s toolbar.**
- **As much as possible, adopt a top-down flow.**
- **Relocate buttons from the side and bottom edges of the screen.**

#### Menus

- Mac users are familiar with the persistent menu bar and expect to find all of an app’s commands in it.
> **Developer note:** To support keyboard shortcuts for menu commands, use [UIKeyCommand](https://developer.apple.com/documentation/uikit/uikeycommand).
- If you provide [pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons) or [pull-down…
> **Developer note:** To add and remove custom app menus, use [UIMenuBuilder](https://developer.apple.com/documentation/uikit/uimenubuilder) and add menu items that represent your iPad app’s commands as menu items with…
- The system automatically converts the context menus in your iPad app to context menus in the macOS version of your app.

### Platform considerations

- *No additional considerations for iPadOS or macOS.

## Recursos relacionados

- *Related:*
  - [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos)
- *Developer documentation:*
  - [Mac Catalyst](https://developer.apple.com/documentation/uikit/mac-catalyst) — UIKit

## Vídeos que la explican

- [Designing iPad Apps for Mac](https://developer.apple.com/videos/play/wwdc2019/809) → `references/videos/2019-809.md`

## Registro de cambios

| Date | Changes |
|---|---|
| May 2, 2023 | Consolidated guidance into one page. |
