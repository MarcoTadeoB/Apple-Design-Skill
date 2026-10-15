# Edit menus — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/edit-menus
- Descargado: 2026-10-15
- Sección: components › Menus and actions
- Plataformas: ios,ipados,macos,visionos
- Última actualización: 2023-06-21 — Updated to include guidance for visionOS.

> Resumen de Apple: An edit menu lets people make changes to selected content in the current view, in addition to offering related commands like Copy, Select, Translate, and Look Up.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- In addition to text, an edit menu’s commands can apply to many types of selectable content, such as images, files, and objects like contact cards, charts, or map locations.
- Edit menus can look and behave slightly differently in different platforms.
  - In iOS, the edit menu displays commands in a compact, horizontal list that appears when people touch and hold or double-tap to select content in a view.
  - In iPadOS, the edit menu looks different depending on how people reveal it.
  - In macOS, people can access editing commands in a context menu they can reveal while in an editing task, as well as through the app’s [Edit…
  - In visionOS, people use the standard [pinch and hold](https://developer.apple.com/design/human-interface-guidelines/gestures#Standard-gestures) gesture to open the edit menu as a…
- Editing content is rare in tvOS and watchOS experiences, so the system doesn’t provide an edit menu in these platforms.

### Best practices

- **Prefer the system-provided edit menu.**
- **Let people reveal an edit menu using the system-defined interactions they already know.**
- **Offer commands that are relevant in the current context, removing or dimming commands that don’t apply.**
- **List custom commands near relevant system-provided ones.**
- **When it makes sense, let people select and copy noneditable text.**
- **Support undo and redo when possible.**
- **In general, avoid implementing other controls that perform the same functions as edit menu items.**
- **Differentiate different types of deletion commands when necessary.**

### Content

- **Create short labels for custom commands.**

### Platform considerations

- *No additional considerations for visionOS.

#### iOS, iPadOS

- **Ensure your edit menu works well in both styles.**
- **Adjust an edit menu’s placement, if necessary.**

#### macOS

- To learn about the order of items in a macOS app’s Edit menu, see [Edit menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Edit-menu).

## Recursos relacionados

- *Related:*
  - [Menus](https://developer.apple.com/design/human-interface-guidelines/menus)
  - [Context menus](https://developer.apple.com/design/human-interface-guidelines/context-menus)
  - [The menu bar](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar)
  - [Undo and redo](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo)
- *Developer documentation:*
  - [UIEditMenuInteraction](https://developer.apple.com/documentation/uikit/uieditmenuinteraction) — UIKit
  - [NSMenu](https://developer.apple.com/documentation/appkit/nsmenu) — AppKit

## Registro de cambios

| Date | Changes |
|---|---|
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | Added guidance on supporting both edit-menu styles in iPadOS. |
