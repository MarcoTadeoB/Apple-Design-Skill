# Buttons — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/buttons
- Descargado: 2026-10-15
- Sección: components › Menus and actions
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2025-12-16 — Updated guidance for Liquid Glass.

> Resumen de Apple: A button initiates an instantaneous action.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Versatile and highly customizable, buttons give people simple, familiar ways to do tasks in your app.
  - **Style.** A visual style based on size, color, and shape.
  - **Content.** A symbol (or icon), text label, or both that a button displays to convey its purpose.
  - **Role.** A system-defined role that identifies a button’s semantic meaning and can affect its appearance.
- There are also many button-like components that have distinct appearances and behaviors for specific use cases, like…

### Best practices

- When buttons are instantly recognizable and easy to understand, an app tends to feel intuitive and well designed.
- **Make buttons easy for people to use.**
  - «As a general rule, a button needs a hit region of at least 44x44 pt — in visionOS, 60x60 pt — to ensure that people can select it easily, whether they use a fingertip, a pointer, their eyes, or a remote.»
- **Always include a press state for a custom button.**

### Style

- System buttons offer a range of styles that support customization while providing built-in interaction states, accessibility support, and appearance adaptation.
- **In general, use a button that has a prominent visual style for the most likely action in a view.**
- **Use style — not size — to visually distinguish the preferred choice among multiple options.**
- **Avoid applying a similar color to button labels and content layer backgrounds.**

### Content

- **Ensure that each button clearly communicates its purpose.**
> **Note:** In macOS and visionOS, the system displays a tooltip after people hover over a button for a moment.
- **Try to associate familiar actions with familiar icons.**
- **Consider using text when a short label communicates more clearly than an icon.**

### Role

- A system button can have one of the following roles:
  - **Normal.** No specific meaning.
  - **Primary.** The button is the default button — the button people are most likely to choose.
  - **Cancel.** The button cancels the current action.
  - **Destructive.** The button performs an action that can result in data destruction.
- A button’s role can have additional effects on its appearance.
- **Assign the primary role to the button people are most likely to choose.**
- **Don’t assign the primary role to a button that performs a destructive action, even if that action is the most likely choice.**

### Platform considerations

- *No additional considerations for tvOS.*

#### iOS, iPadOS

- **Configure a button to display an activity indicator when you need to provide feedback about an action that doesn’t instantly complete.**

#### macOS

- Several specific button types are unique to macOS.

##### Push buttons

- The standard button type in macOS is known as a *push button*.
- **Use a flexible-height push button only when you need to display tall or variable height content.**
- **Append a trailing ellipsis to the title when a push button opens another window, view, or app.**
- **Consider supporting spring loading.**

##### Square buttons

- A *square button* (also known as a *gradient button*) initiates an action related to a view, like adding or removing rows in a table.
- Square buttons contain symbols or icons — not text — and you can configure them to behave like push buttons, toggles, or pop-up buttons.
- **Use square buttons in a view, not in the window frame.**
- **Prefer using a symbol in a square button.**
- **Avoid using labels to introduce square buttons.**
- For developer guidance, see [NSButton.BezelStyle.smallSquare](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/smallsquare).

##### Help buttons

- A *help button* appears within a view and opens app-specific help documentation.
- Help buttons are circular, consistently sized buttons that contain a question mark.
- **Use the system-provided help button to display your help documentation.**
- **When possible, open the help topic that’s related to the current context.**
- **Include no more than one help button per window.**
- **Position help buttons where people expect to find them.**

| View style | Help button location |
|---|---|
| Dialog with dismissal buttons (like OK and Cancel) | Lower corner, opposite to the dismissal buttons and vertically aligned with them |
| Dialog without dismissal buttons | Lower-left or lower-right corner |
| Settings window or pane | Lower-left or lower-right corner |

- **Use a help button within a view, not in the window frame.**
- **Avoid displaying text that introduces a help button.**

##### Image buttons

- An *image button* appears in a view and displays an image, symbol, or icon.
- **Use an image button in a view, not in the window frame.**
- **Include about 10 pixels of padding between the edges of the image and the button edges.**
- **If you need to include a label, position it below the image button.**

#### visionOS

- A visionOS button typically includes a visible background that can help people see it, and the button plays sound to provide feedback when people interact with it.
- There are three standard button shapes in visionOS.
- visionOS buttons use different visual styles to communicate four different interaction states.
> **Note:** In visionOS, buttons don’t support custom hover effects.
- In addition to the four states shown above, a button can also reveal a tooltip when people look at it for a brief time.
- In visionOS, buttons can have the following sizes.

| Shape | Mini (28 pt) | Small (32 pt) | Regular (44 pt) | Large (52 pt) | Extra large (64 pt) |
|---|---|---|---|---|---|
| Circular | ![A checkmark denoting availability.](https://developer.apple.com/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](https://developer.apple.com/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](https://developer.apple.com/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](https://developer.apple.com/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](https://developer.apple.com/images/com.apple.HIG/table-availability-checkmark@2x.png) |
| Capsule (text only) |  | ![A checkmark denoting availability.](https://developer.apple.com/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](https://developer.apple.com/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](https://developer.apple.com/images/com.apple.HIG/table-availability-checkmark@2x.png) |  |
| Capsule (text and icon) |  |  | ![A checkmark denoting availability.](https://developer.apple.com/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](https://developer.apple.com/images/com.apple.HIG/table-availability-checkmark@2x.png) |  |
| Rounded rectangle |  | ![A checkmark denoting availability.](https://developer.apple.com/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](https://developer.apple.com/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](https://developer.apple.com/images/com.apple.HIG/table-availability-checkmark@2x.png) |  |

- **Prefer buttons that have a discernible background shape and fill.**
  - «The exception is a button in a toolbar, context menu, alert, or [ornament](https://developer.apple.com/design/human-interface-guidelines/ornaments) where the shape and material of the larger component make the button comfortably visible.»
  - When a button appears on top of a glass [window](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS), use the…
  - When a button appears floating in space, use the [glass material](https://developer.apple.com/design/human-interface-guidelines/materials#visionOS) for its background.
- **Avoid creating a custom button that uses a white background fill and black text or icons.**
- **In general, prefer circular or capsule-shape buttons.**
- **Provide enough space around a button to make it easy for people to look at it.**
  - «Aim to place buttons so their centers are always at least 60 pts apart.»
- **Choose the right shape if you need to display text-labeled buttons in a stack or row.**
- **Use standard controls to take advantage of the audible feedback sounds people already know.**

#### watchOS

- watchOS displays all inline buttons using the [capsule](https://developer.apple.com/documentation/swiftui/buttonbordershape/capsule) button shape.
- **Use a toolbar to place buttons in the corners.**
- **Prefer buttons that span the width of the screen for primary actions in your app.**
- **Use toolbar buttons to provide either navigation to related areas or contextual actions for the view’s content.**
- **Use the same height for vertical stacks of one- and two-line text buttons.**

## Recursos relacionados

- *Related:*
  - [Pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons)
  - [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons)
  - [Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles)
  - [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)
  - [Location button](https://developer.apple.com/design/human-interface-guidelines/privacy#Location-button)
- *Developer documentation:*
  - [Button](https://developer.apple.com/documentation/swiftui/button) — SwiftUI
  - [UIButton](https://developer.apple.com/documentation/uikit/uibutton) — UIKit
  - [NSButton](https://developer.apple.com/documentation/appkit/nsbutton) — AppKit

## Registro de cambios

| Date | Changes |
|---|---|
| December 16, 2025 | Updated guidance for Liquid Glass. |
| June 9, 2025 | Updated guidance for button styles and content. |
| February 2, 2024 | Noted that visionOS buttons don’t support custom hover effects. |
| December 5, 2023 | Clarified some terminology and guidance for buttons in visionOS. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Updated guidance for using buttons in watchOS. |
