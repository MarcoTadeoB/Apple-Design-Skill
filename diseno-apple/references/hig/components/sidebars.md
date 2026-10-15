# Sidebars — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/sidebars
- Descargado: 2026-10-15
- Sección: components › Navigation and search
- Plataformas: ios,ipados,macos,tvos,visionos
- Última actualización: 2026-06-08 — Updated guidance for sidebar icon colors, and clarified guidance for the adaptable sidebar style.

> Resumen de Apple: A sidebar appears on the leading side of a view and lets people navigate between areas of your app or top-level collections of content, like folders and playlists.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- A sidebar requires a large amount of vertical and horizontal space.

### Best practices

- **Extend visually rich content beneath the sidebar.**
  - ❌ Ejemplo incorrecto: A screenshot of the leading side of an app on iPad. An image spans the upper part of the window, stopping at the edge of the sidebar.
  - ✅ Ejemplo correcto: A screenshot of the leading side of an app on iPad. An image spans the upper part of the window, and uses a background extension effect to flip, blur, and extend the image beneath the sidebar to the…
- **When possible, let people customize the contents of a sidebar.**
- **Group hierarchy with disclosure controls if your app has a lot of content.**
- **Consider using familiar symbols to represent items in the sidebar.**
- **Consider letting people hide the sidebar.**
- **In general, show no more than two levels of hierarchy in a sidebar.**
- **If you need to include two levels of hierarchy in a sidebar, use succinct, descriptive labels to title each group.**
- **Make sure any sidebar icon colors you choose serve a clear purpose.**

### Platform considerations

- *No additional considerations for tvOS.

#### iOS, iPadOS

- When you use the [sidebarAdaptable](https://developer.apple.com/documentation/swiftui/tabviewstyle/sidebaradaptable) style of tab view to present a sidebar, you choose whether to…
> **Developer note:** To display a sidebar only, use [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) to present a sidebar in the primary pane of a split view, or use…
- **Consider using a tab bar first.**
- **If necessary, apply the correct appearance to a sidebar.**

#### macOS

- A sidebar’s row height, text, and glyph size depend on its overall size, which can be small, medium, or large.
- **Consider automatically hiding and revealing a sidebar when its container window resizes.**
- **Avoid putting critical information or actions at the bottom of a sidebar.**

#### visionOS

- **If your app’s hierarchy is deep, consider using a sidebar within a tab in a tab bar.**

## Recursos relacionados

- *Related:*
  - [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views)
  - [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars)
  - [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- *Developer documentation:*
  - [sidebarAdaptable](https://developer.apple.com/documentation/swiftui/tabviewstyle/sidebaradaptable) — SwiftUI
  - [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) — SwiftUI
  - [sidebar](https://developer.apple.com/documentation/swiftui/liststyle/sidebar) — SwiftUI
  - [UICollectionLayoutListConfiguration](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct) — UIKit
  - [NSSplitViewController](https://developer.apple.com/documentation/appkit/nssplitviewcontroller) — AppKit

## Vídeos que la explican

- [Elevate the design of your iPad app](https://developer.apple.com/videos/play/wwdc2025/208) → `references/videos/2025-208.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 8, 2026 | Updated guidance for sidebar icon colors, and clarified guidance for the adaptable sidebar style. |
| June 9, 2025 | Added guidance for extending content beneath the sidebar. |
| August 6, 2024 | Updated guidance to include the SwiftUI adaptable sidebar style. |
| December 5, 2023 | Added artwork for iPadOS. |
| June 21, 2023 | Updated to include guidance for visionOS. |
