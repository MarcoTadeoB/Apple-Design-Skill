# Focus and selection — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/focus-and-selection
- Descargado: 2026-10-15
- Sección: inputs
- Plataformas: ipados,macos,tvos,visionos
- Última actualización: 2023-10-24 — Clarified the difference between focus effects and the visionOS hover effect.

> Resumen de Apple: Focus helps people visually confirm the object that their interaction targets.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Focus supports simplified, component-based navigation.
- In many cases, focusing an item also selects it.
- Different platforms communicate focus in different ways.

### Best practices

- **Rely on system-provided focus effects.**
- **Avoid changing focus without people’s interaction.**
  - «The exception is when people are moving focus using an input device that lets them make discrete, directional movements — like a keyboard, remote, or game controller — and a previously focused item disappears.»
- **Be consistent with the platform as you help people bring focus to items in your app.**
- **Indicate focus using visual appearances that are consistent with the platform.**
- **In general, use a focus ring for a text or search field, but use a highlight in a list or collection.**

### Platform considerations

- *Not supported in iOS or watchOS.*

#### iPadOS

- iPadOS 15 and later defines a focus system that supports keyboard interactions for navigating text fields, text views, and sidebars, in addition to various types of collection…
- The iPadOS and tvOS focus systems are similar.
  - Pressing the Tab key moves focus among focus groups, letting people navigate to sidebars, grids, and other app areas.
  - Pressing an arrow key supports a directional focus interaction that’s similar to tvOS, but limited to navigation among items in the same focus group.
- Onscreen components can indicate focus by using the halo effect or the highlighted appearance.
- The *halo* focus effect — also known as the *focus ring* — displays a customizable outline around the component.
- **Customize the halo focus effect when necessary.**
- The *highlighted* appearance — in which the component’s text uses the app’s accent color — also indicates focus, but it’s not a focus effect.
- **Ensure that focus moves through your custom views in ways that make sense.**
- **Adjust the priority of an item to reflect its importance within a focus group.**

#### tvOS

- **In a full-screen experience, let people use gestures to interact with the content, not to move focus.**
- **Avoid displaying a pointer.**
- **Design your interface to accommodate components in various focus states.**

| State | Description |
|---|---|
| ![An image of an unfocused button on top of a photograph. A small drop shadow makes it appear very close to the content behind it, with a translucent background infused by the colors of the content, and a high-contrast text color.](https://developer.apple.com/images/com.apple.HIG/focus-and-selection-state-unfocused@2x.png) | The viewer hasn’t brought focus to the item. Unfocused items appear less prominent than focused items. |
| ![An image of a focused button on top of a photograph. It’s larger than an unfocused button, and a drop shadow makes it appear farther away from the content behind it, with an opaque white background and a black text label.](https://developer.apple.com/images/com.apple.HIG/focus-and-selection-state-focused@2x.png) | The viewer brings focus to the item. A focused item visually stands out from the other onscreen content through elevation to the foreground, illumination, and animation. |
| ![An image of a highlighted button on top of a photograph. It’s the same size as an unfocused button, and a drop shadow makes it appear a little farther away from the surface of the content behind it, with an opaque white background and a black text label.](https://developer.apple.com/images/com.apple.HIG/focus-and-selection-state-highlighted@2x.png) | The viewer chooses the focused item. A focused item provides instant visual feedback when people choose it. For example, a button might briefly invert its colors and animate before it transitions to its selected appearance. |
| ![An image of a selected button on top of a photograph. It’s the same size as an unfocused button, and a small drop shadow makes it appear very close to the content behind it, with an opaque white background and a black text label.](https://developer.apple.com/images/com.apple.HIG/focus-and-selection-state-selected@2x.png) | The viewer has chosen or activated the item in some way. For example, a heart-shaped button that people can use to favorite a photo might appear filled in the selected state and empty in the deselected state. |
| ![An image of an unavailable button on top of a photograph. It’s the same size as an unfocused button. It lacks a drop shadow and appears to rest directly on the content behind it, with a translucent background tinted by the the colors of nearby content, and a low-contrast text color.](https://developer.apple.com/images/com.apple.HIG/focus-and-selection-state-unavailable@2x.png) | The viewer can’t bring focus to the item or choose it. An unavailable item appears inactive. |

- For developer guidance, see [Adding user-focusable elements to a tvOS app](https://developer.apple.com/documentation/uikit/adding-user-focusable-elements-to-a-tvos-app).

#### visionOS

- visionOS supports the same focus system as in iPadOS and tvOS, letting people use a connected input device like a keyboard or game controller to interact with apps and the system.
> **Note:** When people look at a virtual object to identify it as the object they want to interact with, the system uses the *hover effect*, not a focus effect, to provide visual feedback (for guidance, see…

## Recursos relacionados

- *Related:*
  - [Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes)
  - [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards)
- *Developer documentation:*
  - [Focus Attributes](https://developer.apple.com/documentation/tvml/focus-attributes) — TVML
  - [Focus-based navigation](https://developer.apple.com/documentation/uikit/focus-based-navigation) — UIKit
  - [About focus interactions for Apple TV](https://developer.apple.com/documentation/uikit/about-focus-interactions-for-apple-tv) — UIKit

## Vídeos que la explican

- [Design for spatial input](https://developer.apple.com/videos/play/wwdc2023/10073) → `references/videos/2023-10073.md`
- [Design for spatial user interfaces](https://developer.apple.com/videos/play/wwdc2023/10076) → `references/videos/2023-10076.md`
- [Design for the iPadOS pointer](https://developer.apple.com/videos/play/wwdc2020/10640) → `references/videos/2020-10640.md`

## Registro de cambios

| Date | Changes |
|---|---|
| October 24, 2023 | Clarified the difference between focus effects and the visionOS hover effect. |
| June 21, 2023 | Updated to include guidance for visionOS. |
