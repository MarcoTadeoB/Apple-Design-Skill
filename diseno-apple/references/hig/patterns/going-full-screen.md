# Going full screen — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/going-full-screen
- Descargado: 2026-10-15
- Sección: patterns
- Plataformas: ios,ipados,macos
- Última actualización: 2025-06-09 — Updated guidance for hiding toolbars and navigation controls, and deferring Home Screen indicator gestures in full-screen iOS and iPadOS apps and games.

> Resumen de Apple: iPhone, iPad, and Mac offer full-screen modes that let people expand a window to fill the screen, hiding system controls and providing a distraction-free environment.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Apple TV and Apple Watch don’t offer full-screen modes because apps and games already fill the screen by default.

### Best practices

- **Support full-screen mode when it makes sense for your experience.**
- **If necessary, adjust your layout in full-screen mode, but don’t programmatically resize your window.**
- **Continue to provide access to essential features and controls so people can complete their task without exiting full-screen mode.**
- **Except in games, let people reveal the Dock while your iPadOS or macOS app is in full-screen mode.**
- **After people switch away from your full-screen experience, help them resume where they left off when they return.**
- **Let people choose when to exit full-screen mode.**
- **Prioritize content by temporarily hiding toolbars and navigation controls.**

### Platform considerations

- *Not supported in tvOS, visionOS, or watchOS.*

#### iOS, iPadOS

- **Consider deferring system gestures to prevent accidental exits in a full-screen app or game.**

#### macOS

- **Use the system-provided full-screen experience.**
- **In a game, don’t change the display mode when players go full screen.**
- For additional developer guidance, see [Managing your game window for Metal in macOS](https://developer.apple.com/documentation/metal/managing-your-game-window-for-metal-in-macos).
- **Always let people choose when to enter full-screen mode.**

## Recursos relacionados

- *Related:*
  - [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
  - [Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking)
  - [Windows](https://developer.apple.com/design/human-interface-guidelines/windows)
  - [The menu bar](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar)
- *Developer documentation:*
  - [fullScreenCover(item:onDismiss:content:)](https://developer.apple.com/documentation/swiftui/view/fullscreencover(item:ondismiss:content:)) — SwiftUI
  - [NSScreen](https://developer.apple.com/documentation/appkit/nsscreen) — AppKit
  - [NSWindow.CollectionBehavior](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct) — AppKit
  - [Managing your game window for Metal in macOS](https://developer.apple.com/documentation/metal/managing-your-game-window-for-metal-in-macos) — Swift, Objective-C

## Vídeos que la explican

- [Elevate the design of your iPad app](https://developer.apple.com/videos/play/wwdc2025/208) → `references/videos/2025-208.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 9, 2025 | Updated guidance for hiding toolbars and navigation controls, and deferring Home Screen indicator gestures in full-screen iOS and iPadOS apps and games. |
| June 10, 2024 | Enhanced guidance for playing a game in full-screen mode. |
