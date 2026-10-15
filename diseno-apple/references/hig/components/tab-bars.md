# Tab bars — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/tab-bars
- Descargado: 2026-10-15
- Sección: components › Navigation and search
- Plataformas: ios,ipados,macos,tvos,visionos
- Última actualización: 2026-06-08 — Updated terminology and art.

> Resumen de Apple: A tab bar lets people navigate between top-level sections of your app.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Tab bars help people understand the different types of information or functionality that an app provides.

### Best practices

- **Use a tab bar to support navigation, not to provide actions.**
- **Make sure the tab bar is visible when people navigate to different sections of your app.**
  - «The exception is when a modal view covers the tab bar, because a modal is temporary and self-contained.»
- **Use the appropriate number of tabs required to help people navigate your app.**
- **Avoid overflow tabs.**
- **Don’t disable or hide tab bar buttons, even when their content is unavailable.**
- **Include tab labels to help with navigation.**
- **Consider using SF Symbols to provide familiar, scalable tab bar icons.**
- If you’re creating custom tab bar icons, see [Apple Design Resources](https://developer.apple.com/design/resources/) for tab bar icon dimensions.
- **Use a badge to indicate that critical information is available.**
- **Avoid applying a similar color to tab labels and content layer backgrounds.**

### Platform considerations

- *No additional considerations for macOS.

#### iOS

- A tab bar floats above content at the bottom of the screen.
- For tab bars with an attached accessory, like the MiniPlayer in Music, you can choose to minimize the tab bar and move the accessory inline with it when a person scrolls down.
- A tab bar can include a dedicated search tab at the trailing end.

#### iPadOS

- The system displays a tab bar near the top of the screen.
> **Note:** To present a sidebar without the option to convert it to a tab bar, use a [navigation split view](https://developer.apple.com/documentation/swiftui/navigationsplitview) instead of a tab view.
- **Prefer a tab bar for navigation.**
- **Let people customize the tab bar.**

#### tvOS

- A tab bar is highly customizable.
  - Specify a tint, color, or image for the tab bar background
  - Choose a font for tab items, including a different font for the selected item
  - Specify tints for selected and unselected items
  - Add button icons, like settings and search
- By default, a tab bar is translucent, and only the selected tab is opaque.
  - «The height of a tab bar is 68 points, and its top edge is 46 points from the top of the screen; you can’t change either of these values.»
- If there are more items than can fit in the tab bar, the system truncates the rightmost item by applying a fade effect that begins at the right side of the tab bar.
- **Be aware of tab bar scrolling behaviors.**
  - «The exception is when a screen contains a split view, such as the TV app’s Library tab or an app’s Settings screen.»
- **In a live-viewing app, organize tabs in a consistent way.**
  - Live content
  - Cloud DVR or other recorded content
  - Other content
- For additional guidance, see [Live-viewing apps](https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps).

#### visionOS

- In visionOS, a tab bar is always vertical, floating in a position that’s fixed relative to the window’s leading side.
- **Supply a symbol and a text label for each tab.**
- **If it makes sense in your app, consider using a sidebar within a tab.**

## Recursos relacionados

- *Related:*
  - [Tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views)
  - [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars)
  - [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars)
  - [Materials](https://developer.apple.com/design/human-interface-guidelines/materials)
- *Developer documentation:*
  - [TabView](https://developer.apple.com/documentation/swiftui/tabview) — SwiftUI
  - [TabViewBottomAccessoryPlacement](https://developer.apple.com/documentation/swiftui/tabviewbottomaccessoryplacement) — SwiftUI
  - [Enhancing your app’s content with tab navigation](https://developer.apple.com/documentation/swiftui/enhancing-your-app-content-with-tab-navigation) — SwiftUI
  - [UITabBar](https://developer.apple.com/documentation/uikit/uitabbar) — UIKit
  - [Elevating your iPad app with a tab bar and sidebar](https://developer.apple.com/documentation/uikit/elevating-your-ipad-app-with-a-tab-bar-and-sidebar) — UIKit

## Vídeos que la explican

- [Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356) → `references/videos/2025-356.md`
- [Elevate the design of your iPad app](https://developer.apple.com/videos/play/wwdc2025/208) → `references/videos/2025-208.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 8, 2026 | Updated terminology and art. |
| December 16, 2025 | Updated guidance for Liquid Glass. |
| July 28, 2025 | Added guidance for Liquid Glass. |
| September 9, 2024 | Added art representing the tab bar in iPadOS 18. |
| August 6, 2024 | Updated with guidance for the tab bar in iPadOS 18. |
| June 21, 2023 | Updated to include guidance for visionOS. |
