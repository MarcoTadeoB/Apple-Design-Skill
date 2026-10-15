# Scroll views — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/scroll-views
- Descargado: 2026-10-15
- Sección: components › Presentation
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2026-06-08 — Updated guidance for scroll edge effects.

> Resumen de Apple: A scroll view lets people view content that’s larger than the view’s boundaries by moving the content vertically or horizontally.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- The scroll view itself has no appearance, but it can display a translucent *scroll indicator* that typically appears after people begin scrolling the view’s content.

### Best practices

- **Support default scrolling gestures and keyboard shortcuts.**
- **Make it apparent when content is scrollable.**
- **Avoid putting a scroll view inside another scroll view with the same orientation.**
- **Consider supporting page-by-page scrolling if it makes sense for your content.**
- **In some cases, scroll automatically to help people find their place.**
  - Your app performs an operation that selects content or places the insertion point in an area that’s currently hidden.
  - People start entering information in a location that’s not currently visible.
  - The pointer moves past the edge of the view while people are making a selection. In this case, follow the pointer by scrolling in the direction it moves.
  - People select something and scroll to a new location before acting on the selection. In this case, scroll until the selection is in view before performing the operation.
- In all cases, automatically scroll the content only as much as necessary to help people retain context.
- **If you support zoom, set appropriate maximum and minimum scale values.**

### Scroll edge effects

- In iOS, iPadOS, and macOS, a *scroll edge effect* provides a visual separation between certain interface elements, such as…
- **Prefer the automatic scroll edge effect style.**
- **Only use a scroll edge effect when a scroll view is behind floating interface elements.**
- **Apply one scroll edge effect per view.**
- For developer guidance, see [ScrollEdgeEffectStyle](https://developer.apple.com/documentation/swiftui/scrolledgeeffectstyle),…

### Platform considerations

#### iOS, iPadOS

- **Consider showing a page control when a scroll view is in page-by-page mode.**

#### macOS

- In macOS, a *scroll indicator* is commonly called a *scroll bar*.
- **If necessary, use small or mini scroll bars in a panel.**

#### tvOS

- Views in tvOS can scroll, but they aren’t treated as distinct objects with scroll indicators.

#### visionOS

- In visionOS, the scroll indicator has a small, fixed size to help communicate that people can scroll efficiently without making large movements.
- When people begin swiping content in the direction they want it to scroll, the scroll indicator appears at the window’s edge, visually reinforcing the effect of their gesture and…
- **If necessary, account for the size of the scroll indicator.**

##### Look to Scroll

- In views that support Look to Scroll, people can scroll using only their eyes.
- **Support Look to Scroll for reading or browsing views.**
- **Avoid using Look to Scroll for secondary content.**
- **Maintain consistency across content.**
- **Define clear scroll areas within your app.**
- **If your app uses custom scroll effects or animations, remove them before supporting Look to Scroll.**

#### watchOS

- **Prefer vertically scrolling content.**
- **Use tab views to provide page-by-page scrolling.**
- **When displaying paged content, consider limiting the content of an individual page to a single screen height.**

## Recursos relacionados

- *Related:*
  - [Page controls](https://developer.apple.com/design/human-interface-guidelines/page-controls)
  - [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures)
  - [Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)
- *Developer documentation:*
  - [ScrollView](https://developer.apple.com/documentation/swiftui/scrollview) — SwiftUI
  - [UIScrollView](https://developer.apple.com/documentation/uikit/uiscrollview) — UIKit
  - [NSScrollView](https://developer.apple.com/documentation/appkit/nsscrollview) — AppKit
  - [WKPageOrientation](https://developer.apple.com/documentation/watchkit/wkpageorientation) — WatchKit
  - [look](https://developer.apple.com/documentation/swiftui/scrollinputkind/look) — SwiftUI

## Registro de cambios

| Date | Changes |
|---|---|
| June 8, 2026 | Updated guidance for scroll edge effects. |
| March 24, 2026 | Added guidance for Look to Scroll in visionOS. |
| July 28, 2025 | Added guidance for scroll edge effects. |
| February 2, 2024 | Added artwork showing the behavior of the visionOS scroll indicator. |
| December 5, 2023 | Described the visionOS scroll indicator and added guidance for integrating it with window layout. |
| June 5, 2023 | Updated guidance for using scroll views in watchOS. |
