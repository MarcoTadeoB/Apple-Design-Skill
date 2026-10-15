# Split views — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/split-views
- Descargado: 2026-10-15
- Sección: components › Layout and organization
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2025-06-09 — Added iOS and iPadOS platform considerations.

> Resumen de Apple: A split view manages the presentation of multiple adjacent panes of content, each of which can contain a variety of components, including tables, collections, images, and custom views.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Typically, you use a split view to show multiple levels of your app’s hierarchy at once and support navigation between them.
- It’s common to use a split view to display a [sidebar](https://developer.apple.com/design/human-interface-guidelines/sidebars) for navigation, where the leading pane lists the…

### Best practices

- **To support navigation, persistently highlight the current selection in each pane that leads to the detail view.**
- **Consider letting people drag and drop content between panes.**

### Platform considerations

#### iOS

- **Prefer using a split view in a regular — not a compact — environment.**

#### iPadOS

- In iPadOS, a split view can include either two vertical panes, like Mail, or three vertical panes, like Keynote.
- **Account for narrow, compact, and intermediate window widths.**

#### macOS

- In macOS, you can arrange the panes of a split view vertically, horizontally, or both.
- **Set reasonable defaults for minimum and maximum pane sizes.**
- **Consider letting people hide a pane when it makes sense.**
- **Provide multiple ways to reveal hidden panes.**
- **Prefer the thin divider style.**
  - «Avoid using thicker divider styles unless you have a specific need.»

#### tvOS

- In tvOS, a split view can work well to help people filter content.
- **Choose a split view layout that keeps the panes looking balanced.**
- **Display a single title above a split view, helping people understand the content as a whole.**
- **Choose the title’s alignment based on the type of content the secondary pane contains.**

#### visionOS

- **To display supplementary information, prefer a split view instead of a new window.**

#### watchOS

- In watchOS, the split view displays either the list view or a detail view as a full-screen view.
- **Automatically display the most relevant detail view.**
- **If your app displays multiple detail pages, place the detail views in a vertical [tab view](https://developer.apple.com/design/human-interface-guidelines/tab-views).**

## Recursos relacionados

- *Related:*
  - [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars)
  - [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars)
  - [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- *Developer documentation:*
  - [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) — SwiftUI
  - [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller) — UIKit
  - [NSSplitViewController](https://developer.apple.com/documentation/appkit/nssplitviewcontroller) — AppKit

## Vídeos que la explican

- [Make your UIKit app more flexible](https://developer.apple.com/videos/play/wwdc2025/282) → `references/videos/2025-282.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 9, 2025 | Added iOS and iPadOS platform considerations. |
| December 5, 2023 | Added guidance for split views in visionOS. |
| June 5, 2023 | Added guidance for split views in watchOS. |
