# Componentes de Apple — guía rápida

64 componentes de la sección *Components* de las HIG, agrupados como en Apple. Para cada uno:
qué es (resumen literal de Apple), cuándo usarlo, apartados de la página (anatomía), valores exactos, estados,
errores habituales y plataformas. Las frases entre «» son citas literales de las HIG; abre la página condensada
(`references/hig/components/…`) para las tablas completas y el contexto, y la URL para el texto íntegro.

## Cómo elegir el componente (resumen con fuentes)

| Necesidad | Componente | Fuente |
|---|---|---|
| Navegar entre secciones principales (iPhone) | Tab bar (flota sobre el contenido, abajo; puede tener pestaña de búsqueda al final) | [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) |
| Navegar en iPad/Mac con jerarquía profunda | Sidebar (en iPad la tab bar puede convertirse en sidebar) | [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars), vídeo `2025-208` 1:25 |
| Acciones sobre la vista actual | Toolbar, **nunca** la tab bar («Use a tab bar to support navigation, not to provide actions») | [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars), [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars) |
| Elegir entre pocas opciones exclusivas | Segmented control | [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls) |
| Activar/desactivar | Toggle | [Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles) |
| Valor continuo dentro de un rango | Slider | [Sliders](https://developer.apple.com/design/human-interface-guidelines/sliders) |
| Tarea acotada que interrumpe el flujo | Sheet (con atenuación si interrumpe) | [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets), vídeo `2025-356` 7:43 |
| Información crítica que exige respuesta | Alert (úsalo con moderación) | [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) |
| Acciones contextuales sobre un elemento | Context menu / menú | [Context menus](https://developer.apple.com/design/human-interface-guidelines/context-menus), [Menus](https://developer.apple.com/design/human-interface-guidelines/menus) |
| Buscar | Search field (toolbar inferior preferida en iOS, pestaña Search en apps con pestañas) | [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields), vídeo `2026-292` |
| Datos estructurados escaneables | Lists and tables | [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables) |
| Muchos elementos visuales | Collections | [Collections](https://developer.apple.com/design/human-interface-guidelines/collections) |

Reglas transversales del sistema de diseño vigente (Liquid Glass): los componentes estándar adoptan el material
automáticamente; no añadas fondos ni bordes propios a los botones de barra (vídeo `2025-356`, 8:33); agrupa
elementos de barra por función y frecuencia; el botón primario (Done) va separado y tintado. Detalle en
`references/liquid-glass.md`.

---


## Content

### Charts

`hig/components/charts.md` · https://developer.apple.com/design/human-interface-guidelines/charts · plataformas: ios, ipados, macos, tvos, visionos, watchos · actualizado 2022-09-23

- **Qué es:** Organize data in a chart to communicate information with clarity and visual appeal.
- **Cuándo y cómo usarlo:** «Use a fixed or dynamic axis range depending on the meaning of your chart. _(Axes)_» · «Prefer familiar sequences of values in the tick and grid-line labels for an axis. _(Axes)_» · «Consider using Audio Graphs to give VoiceOver users more information about your chart. _(Enhancing the accessibility of a chart)_»
- **Anatomía / apartados de la página:** Anatomy, Marks, Axes, Descriptive content, Color, Enhancing the accessibility of a chart
- **Tamaños y valores:** «For example, people expect a chart that shows a battery’s current charge to have a minimum value of 0% (completely empty) and a maximum value of 100% (completely full). _(Axes)_»
- **Estados:** «If people want to explore additional details, they can drag a vertical indicator through the line graph, revealing the value at the selected time.» · «The second way — which is particularly useful if you need to present a very large dataset — is to let people move focus among subsets of values instead of navigating through all individual data…»
- **Errores habituales (lo que Apple pide evitar):** «Avoid relying solely on color to differentiate between different pieces of data or communicate essential information in a chart. _(Color)_»
- **Otras reglas:** «Choose a mark type based on the information you want to communicate about the data. _(Marks)_» · «Consider combining mark types when it adds clarity to your chart. _(Marks)_» · «Define the value of the lower bound based on mark type and chart usage. _(Axes)_» · «Tailor the appearance of grid lines and labels to a chart’s use cases. _(Axes)_» · «Write descriptions that help people understand what a chart does before they view it. _(Descriptive content)_» · «Summarize the main message of your chart to help make it approachable and useful for everyone. _(Descriptive content)_» · «Establish a consistent visual hierarchy that helps communicate the relative importance of various chart elements.» · «In a compact environment, maximize the width of the plot area to give people enough space to comfortably examine a chart.» …
- **Consideraciones por plataforma:** watchOS

### Image views

`hig/components/image-views.md` · https://developer.apple.com/design/human-interface-guidelines/image-views · plataformas: ios, ipados, macos, tvos, visionos, watchos · actualizado 2023-06-21

- **Qué es:** An image view displays a single image — or in some cases, an animated sequence of images — on a transparent or opaque background.
- **Cuándo y cómo usarlo:** «Use an image view when the primary purpose of the view is simply to display an image.» · «Use an image button instead of an image view to make a clickable image. _(macOS)_» · «Use SwiftUI to create animations when possible. _(watchOS)_»
- **Anatomía / apartados de la página:** Content
- **Otras reglas:** «If you want to display an icon in your interface, consider using a symbol or interface icon instead of an image view.» · «Take care when overlaying text on images. _(Content)_» · «Aim to use a consistent size for all images in an animated sequence. _(Content)_» · «If your app needs an editable image view, use an image well. _(macOS)_»
- **Consideraciones por plataforma:** macOS, tvOS, visionOS, watchOS

### Text views

`hig/components/text-views.md` · https://developer.apple.com/design/human-interface-guidelines/text-views · plataformas: ios, ipados, macos, tvos, visionos, watchos · actualizado 2023-06-05

- **Qué es:** A text view displays multiline, styled text content, which can optionally be editable.
- **Cuándo y cómo usarlo:** «Use a text view when you need to display text that’s long, editable, or in a special format.»
- **Otras reglas:** «Keep text legible.» · «Make useful text selectable.» · «Show the appropriate keyboard type. _(iOS, iPadOS)_»
- **Consideraciones por plataforma:** iOS, iPadOS, tvOS

### Web views

`hig/components/web-views.md` · https://developer.apple.com/design/human-interface-guidelines/web-views · plataformas: ios, ipados, macos, visionos

- **Qué es:** A web view loads and displays rich web content, such as embedded HTML and websites, directly within your app.
- **Errores habituales (lo que Apple pide evitar):** «Avoid using a web view to build a web browser.»
- **Otras reglas:** «Support forward and back navigation when appropriate.»


## Layout and organization

### Boxes

`hig/components/boxes.md` · https://developer.apple.com/design/human-interface-guidelines/boxes · plataformas: ios, ipados, macos, visionos

- **Qué es:** A box creates a visually distinct group of logically related information and components.
- **Cuándo y cómo usarlo:** «Prefer keeping a box relatively small in comparison with its containing view.» · «Consider using padding and alignment to communicate additional grouping within a box.»
- **Anatomía / apartados de la página:** Content
- **Otras reglas:** «Provide a succinct introductory title if it helps clarify the box’s contents. _(Content)_» · «If you need a title, write a brief phrase that describes the contents. _(Content)_»
- **Consideraciones por plataforma:** iOS, iPadOS, macOS

### Collections

`hig/components/collections.md` · https://developer.apple.com/design/human-interface-guidelines/collections · plataformas: ios, ipados, macos, tvos, visionos

- **Qué es:** A collection manages an ordered set of content and presents it in a customizable and highly visual layout.
- **Cuándo y cómo usarlo:** «Use the standard row or grid layout whenever possible.» · «Consider using a table instead of a collection for text.» · «Consider using animations to provide feedback when people insert, delete, or reorder items.» · «Use caution when making dynamic layout changes. _(iOS, iPadOS)_»
- **Estados:** «Use adequate padding around images to keep focus or hover effects easy to see and prevent content from overlapping.»
- **Otras reglas:** «Make it easy to choose an item.» · «Add custom interactions when necessary.»
- **Consideraciones por plataforma:** iOS, iPadOS

### Column views

`hig/components/column-views.md` · https://developer.apple.com/design/human-interface-guidelines/column-views · plataformas: macos

- **Qué es:** A column view — also called a *browser* — lets people view and navigate a data hierarchy using a series of vertical columns.
- **Estados:** «Consider showing information about the selected item when there are no nested items to display.» · «The Finder, for example, shows a preview of the selected item and information like the creation date, modification date, file type, and size.»
- **Otras reglas:** «Show the root level of your data hierarchy in the first column.» · «Consider showing information about the selected item when there are no nested items to display.» · «Let people resize columns.»

### Disclosure controls

`hig/components/disclosure-controls.md` · https://developer.apple.com/design/human-interface-guidelines/disclosure-controls · plataformas: ios, ipados, macos, visionos

- **Qué es:** Disclosure controls reveal and hide information and functionality related to specific controls or views.
- **Cuándo y cómo usarlo:** «Use a disclosure control to hide details until they’re relevant.» · «Use no more than one disclosure button in a single view. _(Disclosure buttons)_»
- **Anatomía / apartados de la página:** Disclosure triangles, Disclosure buttons
- **Estados:** «Establish a clear relationship between the control and the expanded choices that appear when a person clicks or taps a button. _(Disclosure buttons)_»
- **Otras reglas:** «Provide a descriptive label when using a disclosure triangle. _(Disclosure triangles)_» · «Place a disclosure button near the content that it shows and hides. _(Disclosure buttons)_»
- **Consideraciones por plataforma:** iOS, iPadOS, visionOS

### Labels

`hig/components/labels.md` · https://developer.apple.com/design/human-interface-guidelines/labels · plataformas: ios, ipados, macos, tvos, visionos, watchos · actualizado 2023-06-05

- **Qué es:** A label is a static piece of text that people can read and often copy, but not edit.
- **Cuándo y cómo usarlo:** «Use a label to display a small amount of text that people don’t need to edit.» · «Prefer system fonts.» · «Use system-provided label colors to communicate relative importance.»
- **Tamaños y valores:** — (+1 tabla(s) de especificaciones en la página condensada)
- **Otras reglas:** «Make useful label text selectable.»
- **Consideraciones por plataforma:** macOS, watchOS

### Lists and tables

`hig/components/lists-and-tables.md` · https://developer.apple.com/design/human-interface-guidelines/lists-and-tables · plataformas: ios, ipados, macos, tvos, visionos, watchos · actualizado 2023-06-21

- **Qué es:** Lists and tables present data in one or more columns of rows.
- **Cuándo y cómo usarlo:** «Prefer displaying text in a list or table.» · «Use descriptive column headings in a multicolumn table. _(Content)_» · «Use an info button only to reveal more information about a row’s content. _(iOS, iPadOS, visionOS)_» · «Consider using alternating row colors in a multicolumn table. _(macOS)_» · «Use an outline view instead of a table view to present hierarchical data. _(macOS)_»
- **Anatomía / apartados de la página:** Content, Style
- **Estados:** «In general, a table that helps people navigate through a hierarchy persistently highlights the selected row to clarify the path people are taking.» · «In contrast, a table that lists options often highlights a row only briefly before adding an image — such as a checkmark — indicating that the item is selected.» · «Confirm that images near a table still look good as each row highlights and slightly increases in size when it becomes focused. _(tvOS)_» · «A focused row’s corners can also become rounded, which may affect the appearance of images on either side of it. _(tvOS)_»
- **Errores habituales (lo que Apple pide evitar):** «Avoid adding an index to a table that displays controls — like disclosure indicators — in the trailing ends of its rows. _(iOS, iPadOS, visionOS)_»
- **Otras reglas:** «Let people edit a table when it makes sense.» · «Provide appropriate feedback when people select a list item.» · «Keep item text succinct so row content is comfortable to read. _(Content)_» · «Consider ways to preserve readability of text that might otherwise get clipped or truncated. _(Content)_» · «Choose a table or list style that coordinates with your data and platform. _(Style)_» · «Choose a row style that fits the information you need to display. _(Style)_» · «When it provides value, let people click a column heading to sort a table view based on that column _(macOS)_» · «Let people resize columns. _(macOS)_» …
- **Consideraciones por plataforma:** iOS, iPadOS, visionOS, macOS, tvOS, watchOS

### Lockups

`hig/components/lockups.md` · https://developer.apple.com/design/human-interface-guidelines/lockups · plataformas: tvos

- **Qué es:** Lockups combine multiple separate views into a single, interactive unit.
- **Cuándo y cómo usarlo:** «Use consistent lockup sizes within a row or group.» · «Prefer images over initials. _(Monograms)_»
- **Anatomía / apartados de la página:** Cards, Caption buttons, Monograms, Posters
- **Estados:** «All three views expand and contract together as the lockup gets focus.» · «A focused lockup expands in size, so leave enough room between lockups to avoid overlapping or displacing other lockups.» · «Make sure that when people focus on them, caption buttons tilt with the motion that they swipe. _(Caption buttons)_» · «Posters consist of an image and an optional title and subtitle, which are hidden until the poster comes into focus. _(Posters)_»
- **Otras reglas:** «Allow adequate space between lockups.»

### Outline views

`hig/components/outline-views.md` · https://developer.apple.com/design/human-interface-guidelines/outline-views · plataformas: macos

- **Qué es:** An outline view presents hierarchical data in a scrolling list of cells that are organized into columns and rows.
- **Cuándo y cómo usarlo:** «Use a table instead of an outline view to present data that’s not hierarchical.» · «Use descriptive column headings to provide context.» · «Consider using alternating row colors in multi-column outline views.» · «Consider using a centered ellipsis to truncate cell text instead of clipping it.»
- **Tamaños y valores:** «The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://developer.apple.com/images/com.apple.HIG/components-outline-view-intro@2x.png)»
- **Otras reglas:** «Expose data hierarchy in the first column only.» · «Consider letting people click column headings to sort an outline view.» · «Let people resize columns.» · «Make it easy for people to expand or collapse nested containers.» · «Retain people’s expansion choices.» · «Let people edit data if it makes sense in your app.» · «Consider offering a search field to help people find values quickly in a lengthy outline view.»

### Split views

`hig/components/split-views.md` · https://developer.apple.com/design/human-interface-guidelines/split-views · plataformas: ios, ipados, macos, tvos, visionos, watchos · actualizado 2025-06-09

- **Qué es:** A split view manages the presentation of multiple adjacent panes of content, each of which can contain a variety of components, including tables, collections, images, and custom views.
- **Cuándo y cómo usarlo:** «Prefer using a split view in a regular — not a compact — environment. _(iOS)_» · «Prefer the thin divider style. _(macOS)_»
- **Estados:** «The selected appearance clarifies the relationship between the content in various panes and helps people stay oriented.» · «People can then use the Digital Crown to scroll between the detail view’s tabs. watchOS also displays a page indicator next to the Digital Crown, indicating the number of tabs and the currently… _(watchOS)_»
- **Otras reglas:** «To support navigation, persistently highlight the current selection in each pane that leads to the detail view.» · «Consider letting people drag and drop content between panes.» · «Account for narrow, compact, and intermediate window widths. _(iPadOS)_» · «Set reasonable defaults for minimum and maximum pane sizes. _(macOS)_» · «Consider letting people hide a pane when it makes sense. _(macOS)_» · «Provide multiple ways to reveal hidden panes. _(macOS)_» · «Choose a split view layout that keeps the panes looking balanced. _(tvOS)_» · «Display a single title above a split view, helping people understand the content as a whole. _(tvOS)_» …
- **Consideraciones por plataforma:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

### Tab views

`hig/components/tab-views.md` · https://developer.apple.com/design/human-interface-guidelines/tab-views · plataformas: macos, watchos · actualizado 2023-06-05

- **Qué es:** A tab view presents multiple mutually exclusive panes of content in the same area, which people can switch between using a tabbed control.
- **Cuándo y cómo usarlo:** «Use a tab view to present closely related areas of content.»
- **Anatomía / apartados de la página:** Anatomy
- **Errores habituales (lo que Apple pide evitar):** «Avoid using a pop-up button to switch between tabs.» · «Avoid providing more than six tabs in a tab view.»
- **Otras reglas:** «Make sure the controls within a pane affect content only in the same pane.» · «Provide a label for each tab that describes the contents of its pane.» · «In general, inset a tab view by leaving a margin of window-body area on all sides of a tab view. _(Anatomy)_»
- **Consideraciones por plataforma:** iOS, iPadOS, watchOS


## Menus and actions

### Activity views

`hig/components/activity-views.md` · https://developer.apple.com/design/human-interface-guidelines/activity-views · plataformas: ios, ipados, visionos

- **Qué es:** An activity view — often called a *share sheet* — presents a range of tasks that people can perform in the current context.
- **Cuándo y cómo usarlo:** «Consider using a symbol to represent your custom activity.» · «Use the Share button to display an activity view.» · «Use your main app to denote the progress of a lengthy operation. _(Share and action extensions)_»
- **Anatomía / apartados de la página:** Share and action extensions
- **Estados:** «People typically reveal a share sheet by choosing an Action button while viewing a page or document, or after they’ve selected an item.» · «Action extensions let people initiate content-specific tasks — like adding a bookmark, copying a link, editing an inline image, or displaying selected text in another language — without leaving the… _(Share and action extensions)_»
- **Errores habituales (lo que Apple pide evitar):** «Avoid creating duplicate versions of common actions that are already available in the activity view.» · «Avoid placing a modal view above your extension. _(Share and action extensions)_»
- **Otras reglas:** «Write a succinct, descriptive title for each custom action you provide.» · «Make sure activities are appropriate for the current context.» · «If necessary, create a custom interface that feels familiar to people. _(Share and action extensions)_» · «Streamline and limit interaction. _(Share and action extensions)_» · «If necessary, provide an image that communicates the purpose of your extension. _(Share and action extensions)_»

### Buttons

`hig/components/buttons.md` · https://developer.apple.com/design/human-interface-guidelines/buttons · plataformas: ios, ipados, macos, tvos, visionos, watchos · actualizado 2025-12-16

- **Qué es:** A button initiates an instantaneous action.
- **Cuándo y cómo usarlo:** «In general, use a button that has a prominent visual style for the most likely action in a view. _(Style)_» · «Use style — not size — to visually distinguish the preferred choice among multiple options. _(Style)_» · «Consider using text when a short label communicates more clearly than an icon. _(Content)_» · «Use a flexible-height push button only when you need to display tall or variable height content. _(macOS)_» · «Use square buttons in a view, not in the window frame. _(macOS)_» · «Prefer using a symbol in a square button. _(macOS)_»
- **Anatomía / apartados de la página:** Style, Content, Role
- **Tamaños y valores:** «As a general rule, a button needs a hit region of at least 44x44 pt — in visionOS, 60x60 pt — to ensure that people can select it easily, whether they use a fingertip, a pointer, their eyes, or a remote.» · «Include about 10 pixels of padding between the edges of the image and the button edges. _(macOS)_» · «Aim to place buttons so their centers are always at least 60 pts apart. _(visionOS)_» (+2 tabla(s) de especificaciones en la página condensada)
- **Estados:** «In macOS and visionOS, the system displays a tooltip after people hover over a button for a moment. _(Content)_» · «Consider supporting spring loading. _(macOS)_» · «On systems with a Magic Trackpad, *spring loading* lets people activate a button by dragging selected items over it and force clicking — that is, pressing harder — without dropping the selected items. _(macOS)_» · «In visionOS, buttons don’t support custom hover effects. _(visionOS)_»
- **Errores habituales (lo que Apple pide evitar):** «Avoid applying a similar color to button labels and content layer backgrounds. _(Style)_» · «Don’t assign the primary role to a button that performs a destructive action, even if that action is the most likely choice. _(Role)_» · «Avoid using labels to introduce square buttons. _(macOS)_» · «Avoid displaying text that introduces a help button. _(macOS)_» · «Avoid creating a custom button that uses a white background fill and black text or icons. _(visionOS)_»
- **Otras reglas:** «Make buttons easy for people to use.» · «Always include a press state for a custom button.» · «Ensure that each button clearly communicates its purpose. _(Content)_» · «Try to associate familiar actions with familiar icons. _(Content)_» · «Assign the primary role to the button people are most likely to choose. _(Role)_» · «Configure a button to display an activity indicator when you need to provide feedback about an action that doesn’t instantly complete. _(iOS, iPadOS)_» · «Append a trailing ellipsis to the title when a push button opens another window, view, or app. _(macOS)_» · «Consider supporting spring loading. _(macOS)_» …
- **Consideraciones por plataforma:** iOS, iPadOS, macOS, visionOS, watchOS

### Context menus

`hig/components/context-menus.md` · https://developer.apple.com/design/human-interface-guidelines/context-menus · plataformas: ios, ipados, macos, tvos, visionos · actualizado 2023-12-05

- **Qué es:** A context menu provides access to functionality that’s directly related to an item, without cluttering the interface.
- **Cuándo y cómo usarlo:** «Prefer a graphical preview that clarifies the target of a context menu’s commands. _(iOS, iPadOS)_» · «Consider using a context menu instead of a panel or inspector window to present frequently used functionality. _(visionOS)_»
- **Anatomía / apartados de la página:** Content
- **Estados:** «Hide unavailable menu items, don’t dim them.» · «Unlike a regular menu, which helps people discover actions they can perform even when the action isn’t available, a context menu displays only the actions that are relevant to the currently selected…» · «In macOS, the exceptions are the Cut, Copy, and Paste menu items, which may appear unavailable if they don’t apply to the current context.» · «Depending on the location of the selected content, a context menu might open above or below it, so you might also need to reverse the order of items to match the position of the menu.»
- **Otras reglas:** «Prioritize relevancy when choosing items to include in a context menu.» · «Aim for a small number of menu items.» · «Support context menus consistently throughout your app.» · «Always make context menu items available in the main interface, too.» · «If you need to use submenus to manage a menu’s complexity, keep them to one level.» · «Hide unavailable menu items, don’t dim them.» · «Aim to place the most frequently used menu items where people are likely to encounter them first.» · «Show keyboard shortcuts in your app’s main menus, not in context menus.» …
- **Consideraciones por plataforma:** iOS, iPadOS, macOS, visionOS

### Dock menus

`hig/components/dock-menus.md` · https://developer.apple.com/design/human-interface-guidelines/dock-menus · plataformas: macos

- **Qué es:** On a Mac, people can secondary click an app’s or game’s icon in the Dock to reveal a Dock menu, which presents both system-provided and custom items.
- **Cuándo y cómo usarlo:** «Prefer high-value custom items for your Dock menu.»
- **Otras reglas:** «Make custom Dock menu items available in other places, too.»

### Edit menus

`hig/components/edit-menus.md` · https://developer.apple.com/design/human-interface-guidelines/edit-menus · plataformas: ios, ipados, macos, visionos · actualizado 2023-06-21

- **Qué es:** An edit menu lets people make changes to selected content in the current view, in addition to offering related commands like Copy, Select, Translate, and Look Up.
- **Cuándo y cómo usarlo:** «Prefer the system-provided edit menu.»
- **Anatomía / apartados de la página:** Content
- **Estados:** «In iOS, iPadOS, and visionOS, the system automatically detects the data type of a selected item, which can result in the addition of a related action to the edit menu.» · «For example, if nothing is selected, avoid showing options that require a selection, such as Copy or Cut.» · «For example, a Delete menu item behaves the same as pressing a Delete key, but a Cut menu item copies the selected content to the system pasteboard before deleting it.»
- **Otras reglas:** «Let people reveal an edit menu using the system-defined interactions they already know.» · «Offer commands that are relevant in the current context, removing or dimming commands that don’t apply.» · «List custom commands near relevant system-provided ones.» · «When it makes sense, let people select and copy noneditable text.» · «Support undo and redo when possible.» · «In general, avoid implementing other controls that perform the same functions as edit menu items.» · «Differentiate different types of deletion commands when necessary.» · «Create short labels for custom commands. _(Content)_» …
- **Consideraciones por plataforma:** iOS, iPadOS, macOS

### Home Screen quick actions

`hig/components/home-screen-quick-actions.md` · https://developer.apple.com/design/human-interface-guidelines/home-screen-quick-actions · plataformas: ios, ipados

- **Qué es:** Home Screen quick actions give people a way to perform app-specific actions from the Home Screen.
- **Errores habituales (lo que Apple pide evitar):** «Avoid making unpredictable changes to quick actions.» · «Don’t use an emoji in place of a symbol or interface icon.»
- **Otras reglas:** «Create quick actions for compelling, high-value tasks.» · «For each quick action, provide a succinct title that instantly communicates the results of the action.» · «Provide a familiar interface icon for each quick action.»

### Menus

`hig/components/menus.md` · https://developer.apple.com/design/human-interface-guidelines/menus · plataformas: ios, ipados, macos, tvos, visionos, watchos · actualizado 2026-06-08

- **Qué es:** A menu reveals its options when people interact with it, making it a space-efficient way to present commands in your app or game.
- **Cuándo y cómo usarlo:** «Use menu item icons sparingly and with purpose. _(Icons)_» · «Prefer listing important or frequently used menu items first. _(Organization)_» · «Prefer keeping all logically related commands in the same group, even if the commands don’t all have the same importance. _(Organization)_» · «Use submenus sparingly. _(Submenus)_» · «Prefer using a submenu to indenting menu items. _(Submenus)_» · «Consider using a changeable label that describes an item’s current state. _(Toggled items)_»
- **Anatomía / apartados de la página:** Labels, Icons, Organization, Submenus, Toggled items, In-game menus
- **Estados:** «For guidance labeling menu items that show and hide something in the interface or show the currently selected state of something, see [Toggled… _(Labels)_» · «Show people when a menu item is unavailable. _(Labels)_» · «An unavailable menu item often appears dimmed and doesn’t respond to interactions. _(Labels)_» · «If all of a menu’s items are unavailable, the menu itself needs to remain available so people can open it and learn about the commands it contains. _(Labels)_»
- **Otras reglas:** «For each menu item, write a label that clearly and succinctly describes it. _(Labels)_» · «To be consistent with platform experiences, use title-style capitalization. _(Labels)_» · «Remove articles like *a*, *an*, and *the* from menu-item labels to save space. _(Labels)_» · «Show people when a menu item is unavailable. _(Labels)_» · «Append an ellipsis to a menu item’s label when the action requires more information before it can complete. _(Labels)_» · «Represent common actions consistently. _(Icons)_» · «Apply a uniform visual treatment across menu items in the same group. _(Icons)_» · «Consider grouping logically related items. _(Organization)_» …
- **Consideraciones por plataforma:** iOS, iPadOS, visionOS

### Ornaments

`hig/components/ornaments.md` · https://developer.apple.com/design/human-interface-guidelines/ornaments · plataformas: visionos · actualizado 2024-02-02

- **Qué es:** In visionOS, an ornament presents controls and information related to a window, without crowding or obscuring the window’s contents.
- **Cuándo y cómo usarlo:** «Consider using an ornament to present frequently needed controls or information in a consistent location that doesn’t clutter the window.» · «Consider using borderless buttons in an ornament.» · «Use system-provided toolbars and tab bars unless you need to create custom components.»
- **Estados:** «When people look at a borderless button in an ornament, the system automatically applies the hover effect to it (for guidance, see…»
- **Otras reglas:** «In general, keep an ornament visible.» · «If you need to display multiple ornaments, prioritize the overall visual balance of the window.» · «Aim to keep an ornament’s width the same or narrower than the width of the associated window.»

### Pop-up buttons

`hig/components/pop-up-buttons.md` · https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons · plataformas: ios, ipados, macos, visionos · actualizado 2023-10-24

- **Qué es:** A pop-up button displays a menu of mutually exclusive options.
- **Cuándo y cómo usarlo:** «Use a pop-up button to present a flat list of mutually exclusive options or states.» · «Consider using a pop-up button when space is limited and you don’t need to display all options all the time.»
- **Otras reglas:** «Provide a useful default selection.» · «Give people a way to predict a pop-up button’s options without opening it.» · «If necessary, include a Custom option in a pop-up button’s menu to provide additional items that are useful in some situations.» · «Within a popover or modal view, consider using a pop-up button instead of a disclosure indicator to present multiple options for a list item. _(iPadOS)_»
- **Consideraciones por plataforma:** iPadOS

### Pull-down buttons

`hig/components/pull-down-buttons.md` · https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons · plataformas: ios, ipados, macos, visionos · actualizado 2022-09-14

- **Qué es:** A pull-down button displays a menu of items or actions that directly relate to the button’s purpose.
- **Cuándo y cómo usarlo:** «Use a pull-down button to present commands or items that are directly related to the button’s action.» · «Consider using a More pull-down button to present items that don’t need prominent positions in the main interface. _(iOS, iPadOS)_»
- **Errores habituales (lo que Apple pide evitar):** «Avoid putting all of a view’s actions in one pull-down button.»
- **Otras reglas:** «Balance menu length with ease of use.» · «Display a succinct menu title only if it adds meaning.» · «Let people know when a pull-down button’s menu item is destructive, and ask them to confirm their intent.» · «Include an interface icon with a menu item when it provides value.»
- **Consideraciones por plataforma:** iOS, iPadOS

### The menu bar

`hig/components/the-menu-bar.md` · https://developer.apple.com/design/human-interface-guidelines/the-menu-bar · plataformas: ipados, macos · actualizado 2025-06-09

- **Qué es:** On a Mac or an iPad, the menu bar at the top of the screen displays the top-level menus in your app or game.
- **Cuándo y cómo usarlo:** «Prefer short, one-word menu titles.» · «Use dynamic menu items primarily in menu bar menus. _(Dynamic menu items)_» · «Reserve the YourAppName > Settings menu item for opening your app’s page in iPadOS Settings. _(iPadOS)_» · «Consider using a symbol to represent your menu bar extra. _(macOS)_»
- **Anatomía / apartados de la página:** Anatomy, App menu, File menu, Edit menu, Format menu, View menu, App-specific menus, Window menu, Help menu, Dynamic menu items
- **Tamaños y valores:** «The menu bar’s height is 24 pt. _(macOS)_» (+8 tabla(s) de especificaciones en la página condensada)
- **Estados:** «Keeping menu items visible helps people learn what actions your app supports, even if they’re unavailable in the current context.» · «Both interface icons and symbols use black and clear colors to define their shapes; the system can apply other colors to the black areas in each image so it looks good on both dark and light menu… _(macOS)_»
- **Errores habituales (lo que Apple pide evitar):** «Avoid making a dynamic menu item the only way to accomplish a task. _(Dynamic menu items)_» · «Avoid relying on the presence of menu bar extras. _(macOS)_»
- **Otras reglas:** «Support the default system-defined menus and their ordering.» · «Always show the same set of menu items.» · «Represent menu item actions with familiar icons.» · «Support the keyboard shortcuts defined for the standard menu items you include.» · «Display the About menu item first. _(App menu)_» · «Determine whether Find menu items belong in the Edit menu. _(Edit menu)_» · «Provide a View menu even if your app supports only a subset of the standard view functions. _(View menu)_» · «Ensure that each show/hide item title reflects the current state of the corresponding view. _(View menu)_» …
- **Consideraciones por plataforma:** iPadOS, macOS

### Toolbars

`hig/components/toolbars.md` · https://developer.apple.com/design/human-interface-guidelines/toolbars · plataformas: ios, ipados, macos, tvos, visionos, watchos · actualizado 2025-12-16

- **Qué es:** A toolbar provides convenient access to frequently used commands, controls, navigation, and search.
- **Cuándo y cómo usarlo:** «Prefer using standard components in a toolbar.» · «Use the standard Back and Close buttons. _(Navigation)_» · «Prefer system-provided symbols without borders. _(Actions)_» · «Use the `.prominent` style for key actions such as Done or Submit. _(Actions)_» · «Use a large title to help people stay oriented as they navigate and scroll. _(iOS)_» · «Prefer using a system-provided toolbar. _(visionOS)_»
- **Anatomía / apartados de la página:** Titles, Navigation, Actions, Item groupings
- **Tamaños y valores:** «Aim for a word or short phrase that distills the purpose of the window or view, and keep the title under 15 characters long so you leave enough room for other controls. _(Titles)_»
- **Estados:** «Borders (like outlined circle symbols) aren’t necessary because the section provides a visible container, and the system defines hover and selection state appearances automatically. _(Actions)_»
- **Errores habituales (lo que Apple pide evitar):** «Avoid applying a similar color to toolbar item labels and content layer backgrounds.» · «Don’t title windows with your app name. _(Titles)_» · «Avoid creating a vertical toolbar. _(visionOS)_» · «Avoid using a pull-down menu in a toolbar. _(visionOS)_»
- **Otras reglas:** «Choose items deliberately to avoid overcrowding.» · «Add a More menu to contain additional actions.» · «In iPadOS and macOS apps, consider letting people customize the toolbar to include their most common items.» · «Reduce the use of toolbar backgrounds and tinted controls.» · «Consider temporarily hiding toolbars for a distraction-free experience.» · «Provide a useful title for each window. _(Titles)_» · «Write a concise title. _(Titles)_» · «Provide actions that support the main tasks people perform. _(Actions)_» …
- **Consideraciones por plataforma:** iOS, iPadOS, macOS, visionOS, watchOS


## Navigation and search

### Path controls

`hig/components/path-controls.md` · https://developer.apple.com/design/human-interface-guidelines/path-controls · plataformas: macos

- **Qué es:** A path control shows the file system path of a selected file or folder.
- **Cuándo y cómo usarlo:** «Use a path control in the window body, not the window frame.»
- **Estados:** «It shows the path of the selected item, or the path of the window’s folder if nothing is selected.» · «A linear list that includes the root disk, parent folders, and selected item.» · «A control similar to a [pop-up button](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons) that shows the icon and name of the selected item.» · «People can click the item to open a menu containing the root disk, parent folders, and selected item.»
- **Otras reglas:** «Standard.» · «Pop up.»

### Search fields

`hig/components/search-fields.md` · https://developer.apple.com/design/human-interface-guidelines/search-fields · plataformas: ios, ipados, macos, tvos, visionos, watchos · actualizado 2026-06-08

- **Qué es:** A search field lets people search a collection of content for specific terms they enter.
- **Cuándo y cómo usarlo:** «Use placeholder text to help people know what they can search for.» · «Use a scope bar to filter among clearly defined search categories. _(Scope bars and tokens)_» · «Use tokens to filter by common search terms or items. _(Scope bars and tokens)_»
- **Anatomía / apartados de la página:** Scope bars and tokens
- **Estados:** «Tokens can clarify a search term, like filtering by a specific contact in Mail, or focus a search to a specific set of attributes, like filtering by photos in Messages. _(Scope bars and tokens)_»
- **Otras reglas:** «If possible, start search immediately when a person types.» · «Consider showing suggested search terms.» · «Simplify search results.» · «Consider letting people filter search results.» · «Default to a broader scope and let people refine it as they need. _(Scope bars and tokens)_» · «Consider pairing tokens with search suggestions. _(Scope bars and tokens)_» · «Choose the standard tab style to provide suggestions, promote discovery, and encourage exploration. _(iOS)_» · «Choose the button appearance to help people quickly find what they need. _(iOS)_» …
- **Consideraciones por plataforma:** iOS, iPadOS, macOS, tvOS, watchOS

### Sidebars

`hig/components/sidebars.md` · https://developer.apple.com/design/human-interface-guidelines/sidebars · plataformas: ios, ipados, macos, tvos, visionos · actualizado 2026-06-08

- **Qué es:** A sidebar appears on the leading side of a view and lets people navigate between areas of your app or top-level collections of content, like folders and playlists.
- **Cuándo y cómo usarlo:** «Consider using familiar symbols to represent items in the sidebar.» · «Consider using a tab bar first. _(iOS, iPadOS)_»
- **Errores habituales (lo que Apple pide evitar):** «Avoid putting critical information or actions at the bottom of a sidebar. _(macOS)_»
- **Otras reglas:** «Extend visually rich content beneath the sidebar.» · «When possible, let people customize the contents of a sidebar.» · «Group hierarchy with disclosure controls if your app has a lot of content.» · «Consider letting people hide the sidebar.» · «In general, show no more than two levels of hierarchy in a sidebar.» · «If you need to include two levels of hierarchy in a sidebar, use succinct, descriptive labels to title each group.» · «Make sure any sidebar icon colors you choose serve a clear purpose.» · «If necessary, apply the correct appearance to a sidebar. _(iOS, iPadOS)_» …
- **Consideraciones por plataforma:** iOS, iPadOS, macOS, visionOS

### Tab bars

`hig/components/tab-bars.md` · https://developer.apple.com/design/human-interface-guidelines/tab-bars · plataformas: ios, ipados, macos, tvos, visionos · actualizado 2026-06-08

- **Qué es:** A tab bar lets people navigate between top-level sections of your app.
- **Cuándo y cómo usarlo:** «Use a tab bar to support navigation, not to provide actions.» · «Use the appropriate number of tabs required to help people navigate your app.» · «Consider using SF Symbols to provide familiar, scalable tab bar icons.» · «Use a badge to indicate that critical information is available.» · «Prefer a tab bar for navigation. _(iPadOS)_»
- **Tamaños y valores:** «The height of a tab bar is 68 points, and its top edge is 46 points from the top of the screen; you can’t change either of these values. _(tvOS)_»
- **Estados:** «Don’t disable or hide tab bar buttons, even when their content is unavailable.» · «If a section is empty, explain why its content is unavailable.» · «By default, a tab bar is translucent, and only the selected tab is opaque. _(tvOS)_» · «When people use the remote to focus on the tab bar, the selected tab includes a drop shadow that emphasizes its selected state. _(tvOS)_»
- **Errores habituales (lo que Apple pide evitar):** «Avoid overflow tabs.» · «Don’t disable or hide tab bar buttons, even when their content is unavailable.» · «Avoid applying a similar color to tab labels and content layer backgrounds.»
- **Otras reglas:** «Make sure the tab bar is visible when people navigate to different sections of your app.» · «Include tab labels to help with navigation.» · «Let people customize the tab bar. _(iPadOS)_» · «Be aware of tab bar scrolling behaviors. _(tvOS)_» · «In a live-viewing app, organize tabs in a consistent way. _(tvOS)_» · «Supply a symbol and a text label for each tab. _(visionOS)_» · «If it makes sense in your app, consider using a sidebar within a tab. _(visionOS)_»
- **Consideraciones por plataforma:** iOS, iPadOS, tvOS, visionOS

### Token fields

`hig/components/token-fields.md` · https://developer.apple.com/design/human-interface-guidelines/token-fields · plataformas: macos

- **Qué es:** A token field is a type of text field that can convert text into *tokens* that are easy to select and manipulate.
- **Otras reglas:** «Add value with a context menu.» · «Consider providing additional ways to convert text into tokens.» · «Consider customizing the delay the system uses before showing suggested tokens.»


## Presentation

### Action sheets

`hig/components/action-sheets.md` · https://developer.apple.com/design/human-interface-guidelines/action-sheets · plataformas: ios, ipados, macos, tvos, watchos

- **Qué es:** An action sheet is a modal view that presents choices related to an action people initiate.
- **Cuándo y cómo usarlo:** «Use an action sheet — not an alert — to offer choices related to an intentional action.» · «Use action sheets sparingly.» · «Use an action sheet — not a menu — to provide choices related to an action. _(iOS, iPadOS)_»
- **Tamaños y valores:** — (+1 tabla(s) de especificaciones en la página condensada)
- **Errores habituales (lo que Apple pide evitar):** «Avoid letting an action sheet scroll. _(iOS, iPadOS)_» · «Avoid displaying more than four buttons in an action sheet, including the Cancel button. _(watchOS)_»
- **Otras reglas:** «Aim to keep titles short enough to display on a single line.» · «Provide a message only if necessary.» · «If necessary, provide a Cancel button that lets people reject an action that might destroy data.» · «Make destructive choices visually prominent.»
- **Consideraciones por plataforma:** iOS, iPadOS, watchOS

### Alerts

`hig/components/alerts.md` · https://developer.apple.com/design/human-interface-guidelines/alerts · plataformas: ios, ipados, macos, tvos, visionos, watchos · actualizado 2024-02-02

- **Qué es:** An alert gives people critical information they need right away.
- **Cuándo y cómo usarlo:** «Use alerts sparingly.» · «Use the destructive style to identify a button that performs a destructive action people didn’t deliberately choose. _(Buttons)_» · «Use an action sheet — not an alert — to offer choices related to an intentional action. _(iOS, iPadOS)_» · «Use a caution symbol sparingly. _(macOS)_»
- **Anatomía / apartados de la página:** Anatomy, Content, Buttons
- **Tamaños y valores:** «If you need to display an accessory view in a visionOS alert, create a view that has a maximum height of 154 pt and a 16-pt corner radius. _(visionOS)_» (+1 tabla(s) de especificaciones en la página condensada)
- **Estados:** «For example, when a server connection is unavailable, Mail displays an indicator that people can choose to learn more.»
- **Errores habituales (lo que Apple pide evitar):** «Avoid using an alert merely to provide information.» · «Avoid displaying alerts for common, undoable actions, even when they’re destructive.» · «Avoid showing an alert when your app starts.» · «Avoid explaining alert buttons. _(Content)_» · «Avoid using OK as the default button title unless the alert is purely informational. _(Buttons)_»
- **Otras reglas:** «In all alert copy, be direct, and use a neutral, approachable tone. _(Content)_» · «Write a title that clearly and succinctly describes the situation. _(Content)_» · «Include informative text only if it adds value. _(Content)_» · «If supported, include a text field only if you need people’s input to resolve the situation. _(Content)_» · «Create succinct, logical button titles. _(Buttons)_» · «Place buttons where people expect. _(Buttons)_» · «If there’s a destructive action, include a Cancel button to give people a clear, safe way to avoid the action. _(Buttons)_» · «Provide alternative ways to cancel an alert when it makes sense. _(Buttons)_» …
- **Consideraciones por plataforma:** iOS, iPadOS, macOS, visionOS

### Page controls

`hig/components/page-controls.md` · https://developer.apple.com/design/human-interface-guidelines/page-controls · plataformas: ios, ipados, tvos, visionos, watchos · actualizado 2023-06-21

- **Qué es:** A page control displays a row of indicator images, each of which represents a page in a flat list.
- **Cuándo y cómo usarlo:** «Use page controls to represent movement between an ordered list of pages.» · «Use page controls on collections of full-screen pages. _(tvOS)_» · «Use vertical pagination to separate multiple views into distinct, purposeful pages. _(watchOS)_»
- **Anatomía / apartados de la página:** Customizing indicators
- **Estados:** «Inclusion of additional controls makes it difficult to maintain focus while moving between pages. _(tvOS)_»
- **Errores habituales (lo que Apple pide evitar):** «Avoid using more than two different indicator images in a page control. _(Customizing indicators)_» · «Avoid coloring indicator images. _(Customizing indicators)_» · «Avoid animating page transitions during scrubbing. _(iOS, iPadOS)_» · «Avoid supporting the scrubber when you use the minimal background style. _(iOS, iPadOS)_»
- **Otras reglas:** «Center a page control at the bottom of the view or window.» · «Although page controls can handle any number of pages, don’t display too many» · «Make sure custom indicator images are simple and clear. _(Customizing indicators)_» · «Customize the default indicator image only when it enhances the page control’s overall meaning. _(Customizing indicators)_» · «Consider limiting the content of an individual page to a single screen height. _(watchOS)_»
- **Consideraciones por plataforma:** iOS, iPadOS, tvOS, visionOS, watchOS

### Panels

`hig/components/panels.md` · https://developer.apple.com/design/human-interface-guidelines/panels · plataformas: macos

- **Qué es:** In a macOS app, a panel typically floats above other open windows providing supplementary controls, options, or information related to the active window or current selection.
- **Cuándo y cómo usarlo:** «Use a panel to give people quick access to important controls or information related to the content they’re working with.» · «Consider using a panel to present inspector functionality.» · «Prefer simple adjustment controls in a panel.» · «Prefer standard panels. _(HUD-style panels)_» · «Use color sparingly in HUDs. _(HUD-style panels)_»
- **Anatomía / apartados de la página:** HUD-style panels
- **Estados:** «For example, you might use a panel to provide controls or settings that affect the selected item in the active document or window.» · «An *inspector* displays the details of the currently selected item, automatically updating its contents when the item changes or when people select a new item.» · «In contrast, if you need to present an *Info* window — which always maintains the same contents, even when the selected item changes — use a regular window, not a panel.»
- **Errores habituales (lo que Apple pide evitar):** «Avoid including panels in the Window menu’s documents list.»
- **Otras reglas:** «Write a brief title that describes the panel’s purpose.» · «Show and hide panels appropriately.» · «In general, avoid making a panel’s minimize button available.» · «Refer to panels by title in your interface and in help documentation.» · «Maintain one panel style when your app switches modes. _(HUD-style panels)_» · «Keep HUDs small. _(HUD-style panels)_»

### Popovers

`hig/components/popovers.md` · https://developer.apple.com/design/human-interface-guidelines/popovers · plataformas: ios, ipados, macos, visionos

- **Qué es:** A popover is a transient view that appears above other content when people click or tap a control or interactive area.
- **Cuándo y cómo usarlo:** «Use a popover to expose a small amount of information or functionality.» · «Consider using popovers when you want more room for content.» · «Use a Close button for confirmation and guidance only.»
- **Estados:** «Some popovers provide both condensed and expanded views of the same information.»
- **Errores habituales (lo que Apple pide evitar):** «Don’t show another view over a popover.» · «Avoid making a popover too big.» · «Avoid using the word *popover* in help documentation.» · «Avoid using a popover to show a warning.» · «Avoid displaying popovers in compact views. _(iOS, iPadOS)_»
- **Otras reglas:** «Position popovers appropriately.» · «Always save work when automatically closing a nonmodal popover.» · «Show one popover at a time.» · «When possible, let people close one popover and open another with a single click or tap.» · «Provide a smooth transition when changing the size of a popover.» · «Consider letting people detach a popover. _(macOS)_» · «Make minimal appearance changes to a detached popover. _(macOS)_»
- **Consideraciones por plataforma:** iOS, iPadOS, macOS

### Scroll views

`hig/components/scroll-views.md` · https://developer.apple.com/design/human-interface-guidelines/scroll-views · plataformas: ios, ipados, macos, tvos, visionos, watchos · actualizado 2026-06-08

- **Qué es:** A scroll view lets people view content that’s larger than the view’s boundaries by moving the content vertically or horizontally.
- **Cuándo y cómo usarlo:** «Prefer the automatic scroll edge effect style. _(Scroll edge effects)_» · «Prefer vertically scrolling content. _(watchOS)_» · «Use tab views to provide page-by-page scrolling. _(watchOS)_»
- **Anatomía / apartados de la página:** Scroll edge effects
- **Estados:** «Instead, when content exceeds the size of the screen, the system automatically scrolls the interface to keep focused items visible. _(tvOS)_»
- **Errores habituales (lo que Apple pide evitar):** «Avoid putting a scroll view inside another scroll view with the same orientation.» · «Avoid using Look to Scroll for secondary content. _(visionOS)_»
- **Otras reglas:** «Support default scrolling gestures and keyboard shortcuts.» · «Make it apparent when content is scrollable.» · «Consider supporting page-by-page scrolling if it makes sense for your content.» · «In some cases, scroll automatically to help people find their place.» · «If you support zoom, set appropriate maximum and minimum scale values.» · «Only use a scroll edge effect when a scroll view is behind floating interface elements. _(Scroll edge effects)_» · «Apply one scroll edge effect per view. _(Scroll edge effects)_» · «Consider showing a page control when a scroll view is in page-by-page mode. _(iOS, iPadOS)_» …
- **Consideraciones por plataforma:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS

### Sheets

`hig/components/sheets.md` · https://developer.apple.com/design/human-interface-guidelines/sheets · plataformas: ios, ipados, macos, tvos, visionos, watchos · actualizado 2026-03-24

- **Qué es:** A sheet helps people perform a scoped task that’s closely related to their current context.
- **Cuándo y cómo usarlo:** «Use a nonmodal view when you want to present supplementary items that affect the main task in the parent view.» · «Prefer using the page or form sheet presentation styles in an iPadOS app. _(iOS, iPadOS)_» · «Use a panel instead of a sheet if people need to repeatedly provide input and observe results. _(macOS)_» · «Use a sheet only when your modal task requires a custom title or custom content presentation. _(watchOS)_»
- **Anatomía / apartados de la página:** Anatomy
- **Estados:** «The system defines two detents: *large* is the height of a fully expanded sheet and *medium* is about half of the fully expanded height. _(iOS, iPadOS)_» · «Each style uses a default size for the sheet, centering its content on top of a dimmed background view and providing a consistent experience. _(iOS, iPadOS)_» · «The parent window is dimmed while the sheet is onscreen, signaling that people can’t interact with it until they dismiss the sheet. _(macOS)_»
- **Errores habituales (lo que Apple pide evitar):** «Avoid displaying a sheet that emerges from the bottom edge of a window. _(visionOS)_»
- **Otras reglas:** «For complex or prolonged user flows, consider alternatives to sheets.» · «Display only one sheet at a time from the main interface.» · «Provide an alternative to the Done button.» · «In an iPhone app, consider supporting the medium detent to allow progressive disclosure of the sheet’s content. _(iOS, iPadOS)_» · «Include a grabber in a resizable sheet. _(iOS, iPadOS)_» · «Support swiping to dismiss a sheet. _(iOS, iPadOS)_» · «Present a sheet in a reasonable default size. _(macOS)_» · «Let people interact with other app windows without first dismissing a sheet. _(macOS)_» …
- **Consideraciones por plataforma:** iOS, iPadOS, macOS, visionOS, watchOS

### Windows

`hig/components/windows.md` · https://developer.apple.com/design/human-interface-guidelines/windows · plataformas: ipados, macos, visionos · actualizado 2025-06-09

- **Qué es:** A window presents UI views and components in your app or game.
- **Cuándo y cómo usarlo:** «Use the term *window* in user-facing content.» · «Prefer using a window to present a familiar interface and to support familiar tasks. _(visionOS)_» · «Prefer using a volume to display rich, 3D content. _(visionOS)_» · «In general, use dynamic scaling. _(visionOS)_»
- **Estados:** «If you must include one, use it only to display a small amount of information directly related to a window’s contents or to a selected item within it. _(macOS)_» · «For example, Finder uses a bottom bar (called the status bar) to display the total number of items in a window, the number of selected items, and how much space is available on the disk. _(macOS)_»
- **Errores habituales (lo que Apple pide evitar):** «Avoid creating custom window UI.» · «Avoid putting critical information or actions in a bottom bar, because people often relocate a window in a way that hides its bottom edge. _(macOS)_»
- **Otras reglas:** «Make sure that your windows adapt fluidly to different sizes to support multitasking and multiwindow workflows.» · «Choose the right moment to open a new window.» · «Consider providing the option to view content in a new window.» · «Make sure window controls don’t overlap toolbar items. _(iPadOS)_» · «Consider letting people use a gesture to open content in a new window. _(iPadOS)_» · «Make sure custom windows use the system-defined appearances. _(macOS)_» · «Retain the window’s glass background. _(visionOS)_» · «Choose an initial window size that minimizes empty areas within it. _(visionOS)_» …
- **Consideraciones por plataforma:** iPadOS, macOS, visionOS


## Selection and input

### Color wells

`hig/components/color-wells.md` · https://developer.apple.com/design/human-interface-guidelines/color-wells · plataformas: ios, ipados, macos, visionos

- **Qué es:** A color well lets people adjust the color of text, shapes, guides, and other onscreen elements.
- **Otras reglas:** «Consider the system-provided color picker for a familiar experience.»
- **Consideraciones por plataforma:** macOS

### Combo boxes

`hig/components/combo-boxes.md` · https://developer.apple.com/design/human-interface-guidelines/combo-boxes · plataformas: macos

- **Qué es:** A combo box combines a text field with a pull-down button in a single control.
- **Cuándo y cómo usarlo:** «Use an introductory label to let people know what types of items to expect.»
- **Otras reglas:** «Populate the field with a meaningful default value from the list.» · «Provide relevant choices.» · «Make sure list items aren’t wider than the text field.»

### Digit entry views

`hig/components/digit-entry-views.md` · https://developer.apple.com/design/human-interface-guidelines/digit-entry-views · plataformas: tvos

- **Qué es:** A digit entry view fills the entire screen and prompts people to enter a series of digits, like a PIN, using a digit-specific keyboard.
- **Cuándo y cómo usarlo:** «Use secure digit fields.»
- **Otras reglas:** «Clearly state the purpose of the digit entry view.»

### Image wells

`hig/components/image-wells.md` · https://developer.apple.com/design/human-interface-guidelines/image-wells · plataformas: macos

- **Qué es:** An image well is an editable version of an image view.
- **Otras reglas:** «Revert to a default image when necessary.» · «If your image well supports copy and paste, make sure the standard copy and paste menu items are available.»

### Pickers

`hig/components/pickers.md` · https://developer.apple.com/design/human-interface-guidelines/pickers · plataformas: ios, ipados, macos, tvos, visionos, watchos · actualizado 2023-06-05

- **Qué es:** A picker displays one or more scrollable lists of distinct values that people can choose from.
- **Cuándo y cómo usarlo:** «Consider using a picker to offer medium-to-long lists of items.» · «Use predictable and logically ordered values.» · «Use a compact date picker when space is constrained. _(iOS, iPadOS)_»
- **Errores habituales (lo que Apple pide evitar):** «Avoid switching views to show a picker.»
- **Otras reglas:** «Consider providing less granularity when specifying minutes in a date picker.» · «Choose a date picker style that suits your app. _(macOS)_»
- **Consideraciones por plataforma:** iOS, iPadOS, macOS, tvOS, watchOS

### Segmented controls

`hig/components/segmented-controls.md` · https://developer.apple.com/design/human-interface-guidelines/segmented-controls · plataformas: ios, ipados, macos, tvos, visionos · actualizado 2023-06-21

- **Qué es:** A segmented control is a linear set of two or more segments, each of which functions as a button.
- **Cuándo y cómo usarlo:** «Use a segmented control to provide closely related choices that affect an object, state, or view.» · «Prefer using either text or images — not a mix of both — in a single segmented control. _(Content)_» · «Use nouns or noun phrases for segment labels. _(Content)_» · «Consider using introductory text to clarify the purpose of a segmented control. _(macOS)_» · «Use a tab view in the main window area — instead of a segmented control — for view switching. _(macOS)_» · «Consider using a split view instead of a segmented control on screens that perform content filtering. _(tvOS)_»
- **Anatomía / apartados de la página:** Content
- **Estados:** «For example, in macOS Keynote people can select only one segment in the alignment options control to align selected text.» · «This grouping can also help people understand at a glance which controls are currently selected.» · «Consider supporting spring loading. _(macOS)_» · «On a Mac equipped with a Magic Trackpad, spring loading lets people activate a segment by dragging selected items over it and force clicking without dropping the selected items. _(macOS)_»
- **Errores habituales (lo que Apple pide evitar):** «Avoid putting other focusable elements close to segmented controls. _(tvOS)_»
- **Otras reglas:** «Consider a segmented control when it’s important to group functions together, or to clearly show their selection state.» · «Keep control types consistent within a single segmented control.» · «Limit the number of segments in a control.» · «In general, keep segment size consistent.» · «As much as possible, use content with a similar size in each segment. _(Content)_» · «Consider a segmented control to switch between closely related subviews. _(iOS, iPadOS)_» · «Consider supporting spring loading. _(macOS)_»
- **Consideraciones por plataforma:** iOS, iPadOS, macOS, tvOS, visionOS

### Sliders

`hig/components/sliders.md` · https://developer.apple.com/design/human-interface-guidelines/sliders · plataformas: ios, ipados, macos, visionos, watchos · actualizado 2023-06-21

- **Qué es:** A slider is a horizontal track with a control, called a thumb, that people can adjust between a minimum and maximum value.
- **Cuándo y cómo usarlo:** «Use familiar slider directions.» · «Consider using a label to introduce a slider. _(macOS)_» · «Use tick marks to increase clarity and accuracy. _(macOS)_» · «Prefer horizontal sliders. _(visionOS)_»
- **Tamaños y valores:** «For example, people expect to be able to move a horizontal slider that represents a percentage from 0 percent on the leading side to 100 percent on the trailing side.» · «For example, a graphics app might offer a horizontal slider for setting the opacity level of an object between 0 and 100 percent. _(macOS)_» · «For example, a graphics app might use a circular slider to adjust the rotation of an object between 0 and 360 degrees. _(macOS)_» · «An animation app might use a circular slider to adjust how many times an object spins when animated — four complete rotations equals four spins, or 1440 degrees of rotation. _(macOS)_»
- **Errores habituales (lo que Apple pide evitar):** «Don’t use a slider to adjust audio volume. _(iOS, iPadOS)_»
- **Otras reglas:** «Customize a slider’s appearance if it adds value.» · «Consider supplementing a slider with a corresponding text field and stepper.» · «Consider giving live feedback as the value of a slider changes. _(macOS)_» · «Choose a slider style that matches peoples’ expectations. _(macOS)_» · «Consider adding labels to tick marks for even greater clarity. _(macOS)_» · «If necessary, create custom glyphs to communicate what the slider does. _(watchOS)_»
- **Consideraciones por plataforma:** iOS, iPadOS, macOS, visionOS, watchOS

### Steppers

`hig/components/steppers.md` · https://developer.apple.com/design/human-interface-guidelines/steppers · plataformas: ios, ipados, macos, visionos

- **Qué es:** A stepper is a two-segment control that people use to increase or decrease an incremental value.
- **Otras reglas:** «Make the value that a stepper affects obvious.» · «Consider pairing a stepper with a text field when large value changes are likely.» · «For large value ranges, consider supporting Shift-click to change the value quickly. _(macOS)_»
- **Consideraciones por plataforma:** macOS

### Text fields

`hig/components/text-fields.md` · https://developer.apple.com/design/human-interface-guidelines/text-fields · plataformas: ios, ipados, macos, tvos, visionos, watchos · actualizado 2023-06-05

- **Qué es:** A text field is a rectangular area in which people enter or edit small, specific pieces of text.
- **Cuándo y cómo usarlo:** «Use a text field to request a small amount of information, such as a name or an email address.» · «Use secure text fields to hide private data.» · «Use a number formatter to help with numeric data.» · «Consider using an expansion tooltip to show the full version of clipped or truncated text.» · «Use images and buttons to provide clarity and functionality in text fields. _(iOS, iPadOS)_» · «Consider using a combo box if you need to pair text input with a list of choices. _(macOS)_»
- **Estados:** «When tabbing between fields, move focus in a logical sequence.»
- **Otras reglas:** «Show a hint in a text field to help communicate its purpose.» · «To the extent possible, match the size of a text field to the quantity of anticipated text.» · «Evenly space multiple text fields.» · «Ensure that tabbing between multiple fields flows as people expect.» · «Validate fields when it makes sense.» · «Adjust line breaks according to the needs of the field.» · «In iOS, iPadOS, tvOS, and visionOS apps, show the appropriate keyboard type.» · «Minimize text entry in your tvOS and watchOS apps.» …
- **Consideraciones por plataforma:** iOS, iPadOS, macOS, watchOS

### Toggles

`hig/components/toggles.md` · https://developer.apple.com/design/human-interface-guidelines/toggles · plataformas: ios, ipados, macos, tvos, visionos, watchos · actualizado 2024-03-29

- **Qué es:** A toggle lets people choose between a pair of opposing states, like on and off, using a different appearance to indicate each state.
- **Cuándo y cómo usarlo:** «Use a toggle to help people choose between two opposing values that affect the state of content or a view.» · «Use the switch toggle style only in a list row. _(iOS, iPadOS)_» · «Use switches, checkboxes, and radio buttons in the window body, not the window frame. _(macOS)_» · «Prefer a switch for settings that you want to emphasize. _(macOS)_» · «Use a checkbox instead of a switch if you need to present a hierarchy of settings. _(macOS)_» · «Consider using radio buttons if you need to present a set of more than two mutually exclusive options. _(macOS)_»
- **Estados:** «If you use a checkbox to globally turn on and off multiple subordinate checkboxes, show a mixed state when the subordinate checkboxes have different states. _(macOS)_» · «A radio button’s state is either selected (a filled circle) or deselected (an empty circle). _(macOS)_» · «Although a radio button can also display a mixed state (indicated by a dash), this state is rarely useful because you can communicate multiple states by using additional radio buttons. _(macOS)_» · «If you need to show that a setting or item has a mixed state, consider using a checkbox instead. _(macOS)_»
- **Errores habituales (lo que Apple pide evitar):** «Avoid supplying a label that explains the button’s purpose. _(iOS, iPadOS)_» · «Avoid listing too many radio buttons in a set. _(macOS)_»
- **Otras reglas:** «Clearly identify the setting, view, or content the toggle affects.» · «Make sure the visual differences in a toggle’s state are obvious.» · «Change the default color of a switch only if necessary. _(iOS, iPadOS)_» · «Outside of a list, use a button that behaves like a toggle, not a switch. _(iOS, iPadOS)_» · «Within a grouped form, consider using a mini switch to control the setting in a single row. _(macOS)_» · «In general, don’t replace a checkbox with a switch. _(macOS)_» · «Accurately reflect a checkbox’s state in its appearance. _(macOS)_» · «To present a single setting that can be on or off, prefer a checkbox. _(macOS)_»
- **Consideraciones por plataforma:** iOS, iPadOS, macOS

### Virtual keyboards

`hig/components/virtual-keyboards.md` · https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards · plataformas: ios, ipados, tvos, visionos, watchos · actualizado 2025-06-09

- **Qué es:** On devices without physical keyboards, the system offers various types of virtual keyboards people can use to enter data.
- **Cuándo y cómo usarlo:** «Use the keyboard layout guide to make the keyboard feel like an integrated part of your interface. _(iOS, iPadOS)_»
- **Anatomía / apartados de la página:** Custom input views, Custom keyboards
- **Errores habituales (lo que Apple pide evitar):** «Avoid duplicating system-provided keyboard features. _(Custom keyboards)_»
- **Otras reglas:** «Choose a keyboard that matches the type of content people are editing.» · «Consider customizing the Return key type if it helps clarify the text-entry experience.» · «Make sure your custom input view makes sense in the context of your app. _(Custom input views)_» · «Play the standard keyboard sound while people type. _(Custom input views)_» · «Provide an obvious and easy way to switch between keyboards. _(Custom keyboards)_» · «Consider providing a keyboard tutorial in your app. _(Custom keyboards)_» · «Place custom controls above the keyboard thoughtfully. _(iOS, iPadOS)_»
- **Consideraciones por plataforma:** iOS, iPadOS, tvOS, visionOS, watchOS


## Status

### Activity rings

`hig/components/activity-rings.md` · https://developer.apple.com/design/human-interface-guidelines/activity-rings · plataformas: ios, ipados, watchos · actualizado 2024-03-29

- **Qué es:** Activity rings show an individual’s daily progress toward Move, Exercise, and Stand goals.
- **Cuándo y cómo usarlo:** «Use Activity rings only to show Move, Exercise, and Stand information.» · «Use Activity rings to show progress for a single person.»
- **Tamaños y valores:** — (+1 tabla(s) de especificaciones en la página condensada)
- **Errores habituales (lo que Apple pide evitar):** «Don’t send notifications that repeat the same information the Activity app sends.» · «Don’t use Activity rings for decoration.» · «Don’t use Activity rings for branding.»
- **Otras reglas:** «Display Activity rings when they’re relevant to the purpose of your app.» · «Always keep the visual appearance of Activity rings the same, regardless of where you display them.» · «To display a label or value that’s directly associated with an Activity ring, use the colors that match it.» · «Maintain Activity ring margins.» · «Differentiate other ring-like elements from Activity rings.»
- **Consideraciones por plataforma:** iOS

### Gauges

`hig/components/gauges.md` · https://developer.apple.com/design/human-interface-guidelines/gauges · plataformas: ios, ipados, macos, visionos, watchos · actualizado 2022-09-23

- **Qué es:** A gauge displays a specific numerical value within a range of values.
- **Cuándo y cómo usarlo:** «Consider using the continuous style for large ranges. _(macOS)_»
- **Anatomía / apartados de la página:** Anatomy
- **Otras reglas:** «Write succinct labels that describe the current value and both endpoints of the range.» · «Consider filling the path with a gradient to help communicate the purpose of the gauge.» · «Continuous. _(macOS)_» · «Discrete. _(macOS)_» · «Consider changing the fill color to inform people about significant parts of the range. _(macOS)_»
- **Consideraciones por plataforma:** macOS

### Progress indicators

`hig/components/progress-indicators.md` · https://developer.apple.com/design/human-interface-guidelines/progress-indicators · plataformas: ios, ipados, macos, tvos, visionos, watchos · actualizado 2023-09-12

- **Qué es:** Progress indicators let people know that your app isn’t stalled while it loads content or performs lengthy operations.
- **Cuándo y cómo usarlo:** «Prefer an activity indicator (spinner) to communicate the status of a background operation or when space is constrained. _(macOS)_»
- **Tamaños y valores:** «Showing 90 percent completion in five seconds and the last 10 percent in 5 minutes can make people wonder if your app is still working and can even feel deceptive.»
- **Estados:** «Avoid vague terms like *loading* or *authenticating* because they seldom add value.» · «In most cases, this is unnecessary, as the animation of the control indicates that content is loading. _(iOS, iPadOS)_»
- **Errores habituales (lo que Apple pide evitar):** «Don’t switch from the circular style to the bar style.» · «Avoid labeling a spinning progress indicator. _(macOS)_»
- **Otras reglas:** «When possible, use a determinate progress indicator.» · «Be as accurate as possible when reporting advancement in a determinate progress indicator.» · «Keep progress indicators moving so people know something is continuing to happen.» · «When possible, switch a progress bar from indeterminate to determinate.» · «If it’s helpful, display a description that provides additional context for the task.» · «Display a progress indicator in a consistent location.» · «When it’s feasible, let people halt processing.» · «Let people know when halting a process has a negative consequence.» …
- **Consideraciones por plataforma:** iOS, iPadOS, macOS, watchOS

### Rating indicators

`hig/components/rating-indicators.md` · https://developer.apple.com/design/human-interface-guidelines/rating-indicators · plataformas: macos · actualizado 2022-09-23

- **Qué es:** A rating indicator uses a series of horizontally arranged graphical symbols — by default, stars — to communicate a ranking level.
- **Otras reglas:** «Make it easy to change rankings.» · «If you replace the star with a custom symbol, make sure that its purpose is clear.»


## System experiences

### App Shortcuts

`hig/components/app-shortcuts.md` · https://developer.apple.com/design/human-interface-guidelines/app-shortcuts · plataformas: ios, ipados, visionos, watchos · actualizado 2026-06-08

- **Qué es:** An App Shortcut gives people access to your app’s key functions or content throughout the system.
- **Anatomía / apartados de la página:** Editorial guidelines
- **Tamaños y valores:** «Each app can include up to 10 App Shortcuts.»
- **Otras reglas:** «To surface common types of app functionality throughout the system, consider adopting app schemas instead.» · «Offer App Shortcuts for your app’s most common and important tasks.» · «Add flexibility by letting people choose from a set of options.» · «Ask for clarification in response to a request that’s missing optional information.» · «Keep voice interactions simple.» · «Make App Shortcuts discoverable in your app.» · «Provide enough detail for interaction on audio-only devices.» · «Provide brief, memorable activation phrases and natural variants. _(Editorial guidelines)_» …
- **Consideraciones por plataforma:** iOS, iPadOS, macOS

### Complications

`hig/components/complications.md` · https://developer.apple.com/design/human-interface-guidelines/complications · plataformas: watchos · actualizado 2023-10-24

- **Qué es:** A complication displays timely, relevant information on the watch face, where people can view it each time they raise their wrist.
- **Anatomía / apartados de la página:** Visual design, Circular, Corner, Inline, Rectangular, Legacy templates
- **Tamaños y valores:** «The text can fill nearly 180 degrees of the bezel before truncating. _(Circular)_» (+12 tabla(s) de especificaciones en la página condensada)
- **Estados:** «When people choose tinted mode, the system automatically desaturates your complication, converting it to grayscale and tinting its images, gauges, and text using a single color that’s based on the… _(Visual design)_»
- **Otras reglas:** «Identify essential, dynamic content that people want to view at a glance.» · «Support all complication families when possible.» · «Consider creating multiple complications for each family.» · «Define a different deep link for each complication you support.» · «Keep privacy in mind.» · «Carefully consider when to update data.» · «Choose a ring or gauge style based on the data you need to display. _(Visual design)_» · «Make sure images look good in tinted mode. _(Visual design)_» …

### Controls

`hig/components/controls.md` · https://developer.apple.com/design/human-interface-guidelines/controls · plataformas: ios, ipados, macos · actualizado 2024-06-10

- **Qué es:** A control provides quick access to a feature of your app from Control Center, the Lock Screen, or the Action button.
- **Cuándo y cómo usarlo:** «Use symbol animations to highlight state changes.» · «Use the same camera UI in your app and your camera experience. _(Camera experiences on a locked device)_»
- **Anatomía / apartados de la página:** Anatomy, Camera experiences on a locked device
- **Estados:** «The system applies this tint color to a control toggle’s symbol in its on state.» · «If specified, the system redacts the title and value, and displays the symbol in its off state.»
- **Otras reglas:** «Offer controls for actions that provide the most benefit without having to launch your app.» · «Update controls when someone interacts with them, when an action completes, or remotely with a push notification.» · «Choose a descriptive symbol that suggests the behavior of the control.» · «Select a tint color that works with your app’s brand.» · «Help people provide additional information the system needs to perform an action.» · «Provide hint text for the Action button.» · «If your control title or value can vary, include a placeholder.» · «Hide sensitive information when the device is locked.» …

### Live Activities

`hig/components/live-activities.md` · https://developer.apple.com/design/human-interface-guidelines/live-activities · plataformas: ios, ipados, macos, watchos · actualizado 2026-10-13

- **Qué es:** A Live Activity lets people track the progress of an activity, event, or task at a glance.
- **Cuándo y cómo usarlo:** «Use familiar layouts for custom views.» · «Use consistent margins and concentric placement.» · «Use color to express the character and identity of your app.» · «Use animations to reinforce the information you’re communicating and to bring attention to updates.» · «Use standard margins to align your design with notifications. _(Presentation)_» · «Consider using the default background color in StandBy. _(Presentation)_»
- **Anatomía / apartados de la página:** Anatomy, Presentation, CarPlay
- **Tamaños y valores:** «When someone taps it, it transitions to the Lock Screen presentation, scaled up by 2x to fill the screen. _(Anatomy)_» · «To avoid truncated text in contexts with limited width like the Dynamic Island on iPhone in landscape, adapt your compact and minimal presentations to fit inside a 28pt-diameter circle.» · «The standard layout margin for Live Activities on the Lock Screen is 14 points. _(Presentation)_» (+6 tabla(s) de especificaciones en la página condensada)
- **Estados:** «As with the compact presentation, people tap the minimal presentation to open its app or touch and hold it to see the expanded presentation. _(Anatomy)_» · «When people touch and hold a Live Activity in compact or minimal presentation, the system displays the expanded presentation. _(Anatomy)_» · «For design guidance, see [Expanded presentation](https://developer.apple.com/design/human-interface-guidelines/live-activities#Expanded-presentation). _(Anatomy)_» · «In this presentation, use a layout similar to the expanded presentation. _(Anatomy)_»
- **Errores habituales (lo que Apple pide evitar):** «Don’t use a Live Activity to display ads or promotions» · «Avoid displaying sensitive information.» · «Don’t add elements to your app that draw attention to the Dynamic Island.» · «Don’t replicate notification layouts. _(Presentation)_»
- **Otras reglas:** «Offer Live Activities for tasks and events that have a defined beginning and end.» · «Focus on important information that people need to see at a glance.» · «Create a Live Activity that matches your app’s visual aesthetic and personality in both dark and light appearances.» · «If you include a logo mark, display it without a container.» · «Ensure text is easy to read.» · «Adapt to different screen sizes and presentations.» · «Adjust element size and placement for efficient use of space.» · «Support limited width presentations.» …
- **Consideraciones por plataforma:** macOS, watchOS

### Notifications

`hig/components/notifications.md` · https://developer.apple.com/design/human-interface-guidelines/notifications · plataformas: ios, ipados, macos, tvos, visionos, watchos · actualizado 2023-10-24

- **Qué es:** A notification gives people timely, high-value information they can understand at a glance.
- **Cuándo y cómo usarlo:** «Use an alert — not a notification — to display an error message.» · «Prefer nondestructive actions. _(Notification actions)_» · «Use a badge only to show people how many unread notifications they have. _(Badging)_» · «Consider using a rich, custom long-look notification to let people get the information they need without launching your app. _(watchOS)_»
- **Anatomía / apartados de la página:** Anatomy, Content, Notification actions, Badging
- **Estados:** «The system defaults to the static interface when the dynamic interface is unavailable, such as when there is no network or the iPhone companion app is unreachable. _(watchOS)_»
- **Errores habituales (lo que Apple pide evitar):** «Avoid sending multiple notifications for the same thing, even if someone hasn’t responded.» · «Avoid sending a notification that tells people to perform specific tasks within your app.» · «Avoid including sensitive, personal, or confidential information in a notification.» · «Avoid including your app name or icon. _(Content)_» · «Avoid providing an action that merely opens your app. _(Notification actions)_» · «Avoid creating a custom image or component that mimics the appearance or behavior of a badge. _(Badging)_» · «Avoid using a short look as the only way to communicate important information. _(watchOS)_»
- **Otras reglas:** «Provide concise, informative notifications.» · «Handle notifications gracefully when your app is in the foreground.» · «Create a short title if it provides context for the notification content. _(Content)_» · «Write succinct, easy-to-read notification content. _(Content)_» · «Provide generically descriptive text to display when notification previews aren’t available. _(Content)_» · «Consider providing a sound to supplement your notifications. _(Content)_» · «Provide beneficial actions that make sense in the context of your notification. _(Notification actions)_» · «Provide a simple, recognizable interface icon for each notification action. _(Notification actions)_» …
- **Consideraciones por plataforma:** watchOS

### Snippets

`hig/components/snippets.md` · https://developer.apple.com/design/human-interface-guidelines/snippets · plataformas: ios, ipados, macos · actualizado 2026-06-08

- **Qué es:** When someone performs a task with Siri or an App Shortcut, a snippet shows the result or asks for confirmation.
- **Anatomía / apartados de la página:** Anatomy
- **Otras reglas:** «Ensure legibility.» · «Keep content concise.» · «Choose a descriptive label for a confirmation snippet’s primary button.» · «Communicate a snippet’s purpose visually.»

### Status bars

`hig/components/status-bars.md` · https://developer.apple.com/design/human-interface-guidelines/status-bars · plataformas: ios, ipados

- **Qué es:** A status bar appears along the upper edge of the screen and displays information about the device’s current state, like the time, cellular carrier, and battery level.
- **Errores habituales (lo que Apple pide evitar):** «Avoid permanently hiding the status bar.»
- **Otras reglas:** «Obscure content under the status bar.» · «Consider temporarily hiding the status bar when displaying full-screen media.»

### Top Shelf

`hig/components/top-shelf.md` · https://developer.apple.com/design/human-interface-guidelines/top-shelf · plataformas: tvos

- **Qué es:** The Apple TV Home Screen provides an area called Top Shelf, which showcases your content in a rich, engaging way while also giving people access to their favorite apps in the Dock.
- **Anatomía / apartados de la página:** Dynamic layouts
- **Tamaños y valores:** «The system displays a static image when your app is in the Dock and in focus and full-screen content is unavailable. tvOS flips and blurs the image, ensuring that it fits into a width of 1920 pixels at the 16:9 aspect…» · «For example, a 16:9 image scales to 500 pixels high if included in a row with a poster or square image. _(Dynamic layouts)_» (+5 tabla(s) de especificaciones en la página condensada)
- **Estados:** «Showing purchasable content in the Top Shelf is fine, but prefer putting the focus on new and exciting content, and consider displaying prices only when people show interest.» · «A label appears when an individual piece of content comes into focus, and small movements on the remote’s Touch surface bring the focused image to life. _(Dynamic layouts)_» · «Apple TV automatically scrolls through these banners on a preset timer until people bring one into focus. _(Dynamic layouts)_» · «When a banner is in focus, a small, circular gesture on the remote’s Touch surface enacts the system focus effect, animating the item, applying lighting effects, and, if the banner contains layered… _(Dynamic layouts)_»
- **Errores habituales (lo que Apple pide evitar):** «Avoid showing advertisements or prices.» · «Avoid implying interactivity in a static image.»
- **Otras reglas:** «Help people jump right into your content.» · «Feature new content.» · «Personalize people’s favorite content.» · «Showcase compelling dynamic content that can help draw people in and encourage them to view more.» · «If you don’t provide the recommended full-screen content, supply at least one static image as a fallback.» · «Provide a title. _(Dynamic layouts)_» · «Provide a title that identifies the currently playing content. _(Dynamic layouts)_» · «Provide enough content to constitute a complete row. _(Dynamic layouts)_» …

### Watch faces

`hig/components/watch-faces.md` · https://developer.apple.com/design/human-interface-guidelines/watch-faces · plataformas: watchos

- **Qué es:** A watch face is a view that people choose as their primary view in watchOS.
- **Otras reglas:** «Help people discover your app by sharing watch faces that feature your complications.» · «Display a preview of each watch face you share.» · «Aim to offer shareable watch faces for all Apple Watch devices.» · «Respond gracefully if people choose an incompatible watch face.»

### Widgets

`hig/components/widgets.md` · https://developer.apple.com/design/human-interface-guidelines/widgets · plataformas: ios, ipados, macos, watchos, visionos · actualizado 2026-10-13

- **Qué es:** A widget provides quick access to essential information and focused interactions from your app or game in additional contexts.
- **Cuándo y cómo usarlo:** «Prefer dynamic information that changes throughout the day.» · «Use brand elements thoughtfully.» · «Use system functionality to refresh dates and times in your widget.» · «Use animated transitions to bring attention to data updates.» · «In general, use standard margins to ensure legibility.» · «Prefer using the system font, text styles, and SF Symbols.»
- **Anatomía / apartados de la página:** Anatomy, Rendering modes, Previews and placeholders
- **Tamaños y valores:** «Use the standard margin width for widgets — 16 points for most widgets — to avoid crowding their edges and creating a cluttered appearance.» · «If you need to use tighter margins — for example, to create content groupings for graphics, buttons, or background shapes — setting margins of 11 points can work well.» · «In general, display text using fonts at 11 points or larger.» · «Text in a font that’s smaller than 11 points can be too hard for many people to read.» · «To make a widget feel intentional and proportionate to where they place it, people can scale a widget from 75 to 125 percent in size. _(visionOS)_» (+7 tabla(s) de especificaciones en la página condensada)
- **Errores habituales (lo que Apple pide evitar):** «Avoid mirroring your widget’s appearance within your app.» · «Avoid very small font sizes.» · «Avoid rasterizing text.»
- **Otras reglas:** «Choose simple ideas that relate to your app’s main purpose.» · «Aim to create a widget that gives people quick access to the content they want.» · «Look for opportunities to surprise and delight.» · «Offer widgets in multiple sizes when doing so adds value.» · «Balance information density.» · «Display only the information that’s directly related to the widget’s main purpose.» · «Choose between automatically displaying content and letting people customize displayed information.» · «Let people know when authentication adds value.» …
- **Consideraciones por plataforma:** iOS, iPadOS, visionOS, watchOS
