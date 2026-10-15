# The menu bar — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/the-menu-bar
- Descargado: 2026-10-15
- Sección: components › Menus and actions
- Plataformas: ipados,macos
- Última actualización: 2025-06-09 — Added guidance for the menu bar in iPadOS.

> Resumen de Apple: On a Mac or an iPad, the menu bar at the top of the screen displays the top-level menus in your app or game.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Mac users are very familiar with the macOS menu bar, and they rely on it to help them learn what an app does and find the commands they need.
- Menu bar menus on iPad are similar to those on Mac, appearing in the same order and with familiar sets of menu items.
- Keyboard shortcuts in iPadOS use the same patterns as in macOS.
- Menus in the menu bar share most of the appearance and behavior characteristics that all menu types have.

### Anatomy

- When present in the menu bar, the following menus appear in the order listed below.
  - *YourAppName* (you supply a short version of your app’s name for this menu’s title)
  - File
  - Edit
  - Format
  - View
  - App-specific menus, if any
  - Window
  - Help
- In addition, the macOS menu bar includes the Apple menu on the leading side and menu bar extras on the trailing side.

### Best practices

- **Support the default system-defined menus and their ordering.**
- **Always show the same set of menu items.**
- **Represent menu item actions with familiar icons.**
- **Support the keyboard shortcuts defined for the standard menu items you include.**
- **Prefer short, one-word menu titles.**

### App menu

- The app menu lists items that apply to your app or game as a whole, rather than to a specific task, document, or window.
- The app menu typically contains the following menu items listed in the following order.

| Menu item | Action | Guidance |
|---|---|---|
| About *YourAppName* | Displays the About window for your app, which includes copyright and version information. | Prefer a short name of 16 characters or fewer. Don’t include a version number. |
| Settings… | Opens your [settings](https://developer.apple.com/design/human-interface-guidelines/settings) window, or your app’s page in iPadOS Settings. | Use only for app-level settings. If you also offer document-specific settings, put them in the File menu. |
| Optional app-specific items | Performs custom app-level setting or configuration actions. | List custom app-configuration items after the Settings item and within the same group. |
| Services (macOS only) | Displays a submenu of services from the system and other apps that apply to the current context. |  |
| Hide *YourAppName* (macOS only) | Hides your app and all of its windows, and then activates the most recently used app. | Use the same short app name you supply for the About item. |
| Hide Others (macOS only) | Hides all other open apps and their windows. |  |
| Show All (macOS only) | Shows all other open apps and their windows behind your app’s windows. |  |
| Quit *YourAppName* | Quits your app. Pressing Option changes Quit *YourAppName* to Quit and Keep Windows. | Use the same short app name you supply for the About item. |

- **Display the About menu item first.**

### File menu

- The File menu contains commands that help people manage the files or documents an app supports.
- The File menu typically contains the following menu items listed in the following order.

| Menu item | Action | Guidance |
|---|---|---|
| New *Item* | Creates a new document, file, or window. | For *Item*, use a term that names the type of item your app creates. For example, Calendar uses *Event* and *Calendar*. |
| Open | Can open the selected item or present an interface in which people select an item to open. | If people need to select an item in a separate interface, an ellipsis follows the command to indicate that more input is required. |
| Open Recent | Displays a submenu that lists recently opened documents and files that people can select, and typically includes a *Clear Menu* item. | List document and filenames that people recognize in the submenu; don’t display file paths. List the documents in the order people last opened them, with the most recently opened document first. |
| Close | Closes the current window or document. Pressing Option changes Close to Close All. For a tab-based window, Close Tab replaces Close. | In a tab-based window, consider adding a Close Window item to let people close the entire window with one click or tap. |
| Close Tab | Closes the current tab in a tab-based window. Pressing Option changes Close Tab to Close Other Tabs. |  |
| Close File | Closes the current file and all its associated windows. | Consider supporting this menu item if your app can open multiple views of the same file. |
| Save | Saves the current document or file. | Automatically save changes periodically as people work so they don’t need to keep choosing File > Save. For a new document, prompt people for a name and location. If you need to let people save a file in multiple formats, prefer a pop-up menu that lets people choose a format in the Save sheet. |
| Save All | Saves all open documents. |  |
| Duplicate | Duplicates the current document, leaving both documents open. Pressing Option changes Duplicate to Save As. | Prefer Duplicate to menu items like Save As, Export, Copy To, and Save To because these items don’t clarify the relationship between the original file and the new one. |
| Rename… | Lets people change the name of the current document. |  |
| Move To… | Prompts people to choose a new location for the document. |  |
| Export As… | Prompts people for a name, output location, and export file format. After exporting the file, the current document remains open; the exported file doesn’t open. | Reserve the Export As item for when you need to let people export content in a format your app doesn’t typically handle. |
| Revert To | When people turn on autosaving, displays a submenu that lists recent document versions and an option to display the version browser. After people choose a version to restore, it replaces the current document. |  |
| Page Setup… | Opens a panel for specifying printing parameters like paper size and printing orientation. A document can save the printing parameters that people specify. | Include the Page Setup item if you need to support printing parameters that apply to a specific document. Parameters that are global in nature, like a printer’s name, or that people change frequently, like the number of copies to print, belong in the Print panel. |
| Print… | Opens the standard Print panel, which lets people print to a printer, send a fax, or save as a PDF. |  |

### Edit menu

- The Edit menu lets people make changes to content in the current document or text container, and provides commands for interacting with the Clipboard.
- **Determine whether Find menu items belong in the Edit menu.**
- The Edit menu typically contains the following top-level menu items, listed in the following order.

| Menu item | Action | Guidance |
|---|---|---|
| Undo | Reverses the effect of the previous user operation. | Clarify the target of the undo. For example, if people just selected a menu item, you can append the item’s title, such as Undo Paste and Match Style. For a text entry operation, you might append the word *Typing* to give Undo Typing. |
| Redo | Reverses the effect of the previous Undo operation. | Clarify the target of the redo. For example, if people just reversed a menu item selection, you can append the item’s title, such as Redo Paste and Match Style. For a text entry operation, you might append the word *Typing* to give Redo Typing. |
| Cut | Removes the selected data and stores it on the Clipboard, replacing the previous contents of the Clipboard. |  |
| Copy | Duplicates the selected data and stores it on the Clipboard. |  |
| Paste | Inserts the contents of the Clipboard at the current insertion point. The Clipboard contents remain unchanged, permitting people to choose Paste multiple times. |  |
| Paste and Match Style | Inserts the contents of the Clipboard at the current insertion point, matching the style of the inserted text to the surrounding text. |  |
| Delete | Removes the selected data, but doesn’t place it on the Clipboard. | Provide a Delete menu item instead of an Erase or Clear menu item. Choosing Delete is the equivalent of pressing the Delete key, so it’s important for the naming to be consistent. |
| Select All | Highlights all selectable content in the current document or text container. |  |
| Find | Displays a submenu containing menu items for performing search operations in the current document or text container. Standard submenus include: Find, Find and Replace, Find Next, Find Previous, Use Selection for Find, and Jump to Selection. |  |
| Spelling and Grammar | Displays a submenu containing menu items for checking for and correcting spelling and grammar in the current document or text container. Standard submenus include: Show Spelling and Grammar, Check Document Now, Check Spelling While Typing, Check Grammar With Spelling, and Correct Spelling Automatically. |  |
| Substitutions | Displays a submenu containing items that let people toggle automatic substitutions while they type in a document or text container. Standard submenus include: Show Substitutions, Smart Copy/Paste, Smart Quotes, Smart Dashes, Smart Links, Data Detectors, and Text Replacement. |  |
| Transformations | Displays a submenu containing items that transform selected text. Standard submenus include: Make Uppercase, Make Lowercase, and Capitalize. |  |
| Speech | Displays a submenu containing Start Speaking and Stop Speaking items, which control when the system audibly reads selected text. |  |
| Start Dictation | Opens the dictation window and converts spoken words into text that’s added at the current insertion point. The system automatically adds the Start Dictation menu item at the bottom of the Edit menu. |  |
| Emoji & Symbols | Displays a Character Viewer, which includes emoji, symbols, and other characters people can insert at the current insertion point. The system automatically adds the Emoji & Symbols menu item at the bottom of the Edit menu. |  |

### Format menu

- The Format menu lets people adjust text formatting attributes in the current document or text container.
- The Format menu typically contains the following top-level menu items, listed in the following order.

| Menu item | Action |
|---|---|
| Font | Displays a submenu containing items for adjusting font attributes of the selected text. Standard submenus include: Show Fonts, Bold, Italic, Underline, Bigger, Smaller, Show Colors, Copy Style, and Paste Style. |
| Text | Displays a submenu containing items for adjusting text attributes of the selected text. Standard submenus include: Align Left, Align Center, Justify, Align Right, Writing Direction, Show Ruler, Copy Ruler, and Paste Ruler. |

### View menu

- The View menu lets people customize the appearance of all an app’s windows, regardless of type.
> **Important:** The View menu doesn’t include items for navigating between or managing specific windows; the [Window menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Window-menu) provides these commands.
- **Provide a View menu even if your app supports only a subset of the standard view functions.**
- **Ensure that each show/hide item title reflects the current state of the corresponding view.**
- The View menu typically contains the following top-level menu items, listed in the following order.

| Menu item | Action |
|---|---|
| Show/Hide Tab Bar | Toggles the visibility of the [tab bar](https://developer.apple.com/design/human-interface-guidelines/tab-bars) above the body area in a tab-based window |
| Show All Tabs/Exit Tab Overview | Enters and exits a view (similar to Mission Control) that provides an overview of all open tabs in a tab-based window |
| Show/Hide Toolbar | In a window that includes a [toolbar](https://developer.apple.com/design/human-interface-guidelines/toolbars), toggles the toolbar’s visibility |
| Customize Toolbar | In a window that includes a toolbar, opens a view that lets people customize toolbar items |
| Show/Hide Sidebar | In a window that includes a [sidebar](https://developer.apple.com/design/human-interface-guidelines/sidebars), toggles the sidebar’s visibility |
| Enter/Exit Full Screen | In an app that supports a [full-screen experience](https://developer.apple.com/design/human-interface-guidelines/going-full-screen), opens the window at full-screen size in a new space |

### App-specific menus

- Your app’s custom menus appear in the menu bar between the View menu and the Window menu.
- **Provide app-specific menus for custom commands.**
- **As much as possible, reflect your app’s hierarchy in app-specific menus.**
- **Aim to list app-specific menus in order from most to least general or commonly used.**

### Window menu

- The Window menu lets people navigate, organize, and manage an app’s windows.
> **Important:** The Window menu doesn’t help people customize the appearance of windows or close them.
- **Provide a Window menu even if your app has only one window.**
- **Consider including menu items for showing and hiding panels.**
- The Window menu typically contains the following top-level menu items, listed in the following order.

| Menu item | Action | Guidance |
|---|---|---|
| Minimize | Minimizes the active window to the Dock. Pressing the Option key changes this item to Minimize All. |  |
| Zoom | Toggles between a predefined size appropriate to the window’s content and the window size people set. Pressing the Option key changes this item to Zoom All. | Avoid using Zoom to enter or exit full-screen mode. The [View menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#View-menu) supports these functions. |
| Show Previous Tab | Shows the tab before the current tab in a tab-based window. |  |
| Show Next Tab | Shows the tab after the current tab in a tab-based window. |  |
| Move Tab to New Window | Opens the current tab in a new window. |  |
| Merge All Windows | Combines all open windows into a single tabbed window. |  |
| Enter/Exit Full Screen | In an app that supports a [full-screen experience](https://developer.apple.com/design/human-interface-guidelines/going-full-screen), opens the window at full-screen size in a new space. | Include this item in the Window menu only if your app doesn’t have a View menu. In this scenario, continue to provide separate Minimize and Zoom menu items. |
| Bring All to Front | Brings all an app’s open windows to the front, maintaining their onscreen location, size, and layering order. (Clicking the app icon in the Dock has the same effect.) Pressing the Option key changes this item to Arrange in Front, which brings an app’s windows to the front in a neatly tiled arrangement. |  |
| *Name of an open app-specific window* | Brings the selected window to the front. | List the currently open windows in alphabetical order for easy scanning. Avoid listing panels or other modal views. |

### Help menu

- The Help menu — located at the trailing end of the menu bar — provides access to an app’s help documentation.

| Menu item | Action | Guidance |
|---|---|---|
| Send *YourAppName* Feedback to Apple | Opens the Feedback Assistant, in which people can provide feedback. |  |
| *YourAppName* Help | When the content uses the Help Book format, opens the content in the built-in Help Viewer. |  |
| *Additional Item* |  | Use a separator between your primary help documentation and additional items, which might include registration information or release notes. Keep the total the number of items you list in the Help menu small to avoid overwhelming people with too many choices when they need help. Alternatively, consider linking to additional items from within your help documentation. |

- For guidance, see [Offering help](https://developer.apple.com/design/human-interface-guidelines/offering-help); for developer guidance, see…

### Dynamic menu items

- In rare cases, it can make sense to present a *dynamic menu item*, which is a menu item that changes its behavior when people choose it while pressing a modifier key (Control,…
- **Avoid making a dynamic menu item the only way to accomplish a task.**
- **Use dynamic menu items primarily in menu bar menus.**
- **Require only a single modifier key to reveal a dynamic menu item.**
> **Tip:** macOS automatically sets the width of a menu to hold the widest item, including dynamic menu items.

### Platform considerations

- *Not supported in iOS, tvOS, visionOS, or watchOS.*

#### iPadOS

- The menu bar displays the top-level menus for your app or game, including both system-provided menus and any custom ones you choose to add.
- As with the macOS menu bar, the iPadOS menu bar provides a familiar way for people to learn what an app does, find the commands they need, and discover keyboard shortcuts.

|  | iPadOS | macOS |
|---|---|---|
| Menu bar visibility | Hidden until revealed | Visible by default |
| Horizontal alignment | Centered | Leading side |
| Menu bar extras | Not available | System default and custom |
| Window controls | In the menu bar when the app is full screen | Never in the menu bar |
| Apple menu | Not available | Always available |
| App menu | About, Services, and app visibility-related items not available | Always available |

- **Because the menu bar is often hidden when running an app full screen, ensure that people can access all of your app’s functions through its UI.**
- **Reserve the YourAppName > Settings menu item for opening your app’s page in iPadOS Settings.**
- **For apps with tab-style navigation, consider adding each tab as a menu item in the View menu.**
- **Consider grouping menu items into submenus to conserve vertical space.**

#### macOS

- The menu bar in macOS includes the Apple menu, which is always the first item on the leading side of the menu bar.
- When menu bar space is constrained, the system prioritizes the display of menus and essential menu bar extras.
- When people enter full-screen mode, the menu bar typically hides until they reveal it by moving the pointer to the top of the screen.

##### Menu bar extras

- A menu bar extra exposes app-specific functionality using an icon that appears in the menu bar when your app is running, even when it’s not the frontmost app.
- When necessary, the system hides menu bar extras to make room for app menus.
- **Consider using a symbol to represent your menu bar extra.**
  - «The menu bar’s height is 24 pt.»
- **Display a menu — not a popover — when people click your menu bar extra.**
  - «Unless the app functionality you want to expose is too complex for a menu, avoid presenting it in a [popover](https://developer.apple.com/design/human-interface-guidelines/popovers).»
- **Let people — not your app — decide whether to put your menu bar extra in the menu bar.**
- **Avoid relying on the presence of menu bar extras.**
- **Consider exposing app-specific functionality in other ways, too.**

## Recursos relacionados

- *Related:*
  - [Menus](https://developer.apple.com/design/human-interface-guidelines/menus)
  - [Dock menus](https://developer.apple.com/design/human-interface-guidelines/dock-menus)
  - [Standard keyboard shortcuts](https://developer.apple.com/design/human-interface-guidelines/keyboards#Standard-keyboard-shortcuts)
- *Developer documentation:*
  - [CommandMenu](https://developer.apple.com/documentation/swiftui/commandmenu) — SwiftUI
  - [Adding menus and shortcuts to the menu bar and user interface](https://developer.apple.com/documentation/uikit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface) — UIKit
  - [NSStatusBar](https://developer.apple.com/documentation/appkit/nsstatusbar) — AppKit

## Vídeos que la explican

- [Elevate the design of your iPad app](https://developer.apple.com/videos/play/wwdc2025/208) → `references/videos/2025-208.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 9, 2025 | Added guidance for the menu bar in iPadOS. |
