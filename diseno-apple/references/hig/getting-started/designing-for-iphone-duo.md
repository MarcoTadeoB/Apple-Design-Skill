# Designing for iPhone Duo — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo
- Descargado: 2026-10-15
- Sección: getting-started
- Plataformas: n/d
- Última actualización: 2026-09-09 — New page. Introduces the fundamental concepts of designing for iPhone Duo, including device poses, dynamic layouts across dual displays, and toolbars and tab bars on the vertical axis.

> Resumen de Apple: An app designed for iPhone Duo adapts seamlessly to both displays, providing a continuous experience as the device opens and closes.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- iPhone Duo has two displays, each with its own front-facing camera.
- Although iPhone Duo is a new form factor, keep in mind that you’re still designing for iPhone, and [Designing for…

### Anatomy

- iPhone Duo has an inner and an outer display.
- A center hinge supports a range of ways to hold and position the device.
- The outer front-facing camera is in the corner and is always visible, vertically aligned with controls on the side.

#### Device poses

- People hold iPhone Duo and set it down in a number of ways: partially folded like a book, placed down on a surface, or standing on its edges.
- Supporting the device’s various poses doesn’t mean designing a custom layout for each one: instead, use [size…
- You can use [Device Hub](https://developer.apple.com/documentation/xcode/device-hub) in Xcode to preview your app on iPhone Duo and test how your app appears in its various poses.

### Best practices

- **Build your app to resize.**
- **Create a consistent experience across displays.**
- **Maintain the same functionality across device poses.**
- **Follow the system’s vertical layout for toolbars, tab bars, and navigation controls.**
- **Make your game playable in every device pose.**

### Dynamic layouts

- Designing for iPhone Duo means accounting for a variety of hardware and software configurations.
- For guidance, see [Layout](https://developer.apple.com/design/human-interface-guidelines/layout).

#### Reserved regions

- In addition to standard considerations for safe areas, available space on iPhone Duo is shaped by *reserved regions*.
- The reserved regions on iPhone Duo include:
  - **The outer front-facing camera.** This region is always present, and expands into the Dynamic Island for Live Activities.
  - **The inner front-facing camera.** This region is only present when the camera is active.
  - **The folding region.** This region is conditional based on how a person uses the device.
- Many system components automatically adapt to reserved regions.
- **Adapt your layout when the device folds.**
- **Avoid extreme layout changes as people fold the device.**

#### Split views

- On iPhone Duo, a split view expands on the inner display and collapses to a single pane on the outer display, the same way it adapts between regular and compact environments on…
- For general guidance, see [split views](https://developer.apple.com/design/human-interface-guidelines/split-views).

#### Arrangement views

- An *arrangement view* is a layout container that holds two views inside it — a primary view and a secondary view — and dynamically organizes them based on display size,…
- There are two types of arrangement view: split and overlay.
  - A *split* arrangement divides its area between its primary and secondary views.
  - An *overlay* arrangement positions the primary and secondary views on top of one another.
- You can limit which axes a split arrangement uses, and collapse the secondary view in an overlay arrangement when you don’t want it to appear.
- For developer guidance, see [ArrangementView](https://developer.apple.com/documentation/swiftui/arrangementview) (SwiftUI) and…
- **Consider an arrangement view when your layout already resembles one.**
- **Keep navigation outside of arrangement views.**

### Vertical controls

- On iPhone Duo, toolbars, tab bars, and navigation controls that are typically at the top and bottom of the display move to the side, preserving vertical space for content and…
- Controls on the side include both system and app elements: the Dynamic Island, the status bar, the toolbar (including navigation buttons), and the tab bar.
- When two apps share the inner display with Split View multitasking, each one places controls along its outer edge, so the left app has controls on the left.
- Because controls on the vertical axis stay aligned with the hardware, they hold the same position relative to the camera on the outer display, and stay on the same side in…
- **Account for asymmetry in your layouts.**
- **Keep controls consistent across device poses.**
- **Follow the standard placement order for toolbar items.**
- **Prioritize frequently used toolbar items to keep them easily available.**
- Preserve frequently used actions first, like Compose in Mail or New Note in Notes, and keep controls that convey important status, like items with badges, visible longer so…
- **In general, don’t override the default bar placement.**
- **Consider using the full display width for interfaces where bars aren’t necessary.**
- **Group related toolbar items instead of spacing them manually.**
- **Locate controls near the content they affect.**
- **Provide both a title and a symbol for each toolbar item that isn’t text-only.**
- **Keep text-based buttons to a minimum.**
- **When space is limited, preserve either the toolbar or tab bar based on the experience that the view provides.**
- In task-oriented experiences, minimize the tab bar to preserve the toolbar actions that are central to completing the task.
- **Use the system overflow menu.**

## Recursos relacionados

- *Related:*
  - [Apple Design Resources](https://developer.apple.com/design/resources/#ios-apps)
  - [Screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications)
  - [Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios)
  - [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- *Developer documentation:*
  - [Preparing your app for iPhone Duo](https://developer.apple.com/documentation/technologyoverviews/preparing-your-app-for-iphone-duo)
  - [ReservedRegion](https://developer.apple.com/documentation/swiftui/reservedregion) — SwiftUI
  - [UIView.ReservedRegion](https://developer.apple.com/documentation/uikit/uiview/reservedregion) — UIKit
  - [ArrangementView](https://developer.apple.com/documentation/swiftui/arrangementview) — SwiftUI
  - [UIArrangementViewController](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller) — UIKit

## Vídeos que la explican

- [Design for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111466) → `references/videos/2026-tech-talks-111466.md`
- [Raise the bar with iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111462) → `references/videos/2026-tech-talks-111462.md`
- [Strike a pose with adaptive layouts on iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111463) → `references/videos/2026-tech-talks-111463.md`

## Registro de cambios

| Date | Changes |
|---|---|
| September 9, 2026 | New page. Introduces the fundamental concepts of designing for iPhone Duo, including device poses, dynamic layouts across dual displays, and toolbars and tab bars on the vertical axis. |
