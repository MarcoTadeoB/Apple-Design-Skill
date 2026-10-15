# Windows — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/windows
- Descargado: 2026-10-15
- Sección: components › Presentation
- Plataformas: ipados,macos,visionos
- Última actualización: 2025-06-09 — Added best practices, and updated with guidance for resizable windows in iPadOS.

> Resumen de Apple: A window presents UI views and components in your app or game.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- In iPadOS, macOS, and visionOS, windows help define the visual boundaries of app content and separate it from other areas of the system, and enable multitasking workflows both…
- Conceptually, apps use two types of windows to display content:
  - A *primary* window presents the main navigation and content of an app, and actions associated with them.
  - An *auxiliary* window presents a specific task or area in an app.
- For guidance laying out content within a window on any platform, see [Layout](https://developer.apple.com/design/human-interface-guidelines/layout); for guidance laying out…

### Best practices

- **Make sure that your windows adapt fluidly to different sizes to support multitasking and multiwindow workflows.**
- **Choose the right moment to open a new window.**
  - «Avoid opening new windows as default behavior unless it makes sense for your app.»
- **Consider providing the option to view content in a new window.**
  - «While it’s best to avoid opening new windows as default behavior unless it benefits your user experience, it’s also great to give people the flexibility of viewing content in multiple ways.»
- **Avoid creating custom window UI.**
- **Use the term *window* in user-facing content.**

### Platform considerations

- *Not supported in iOS, tvOS, or watchOS.*

#### iPadOS

- Windows present in one of two ways depending on a person’s choice in Multitasking & Gestures settings.
  - **Full screen.** App windows fill the entire screen, and people switch between them — or between multiple windows of the same app — using the app switcher.
  - **Windowed.** People can freely resize app windows.
- **Make sure window controls don’t overlap toolbar items.**
- **Consider letting people use a gesture to open content in a new window.**
> **Tip:** If you only need to let people view one file, you can present it without creating your own window, but you must support multiple windows in your app.

#### macOS

- In macOS, people typically run several apps at the same time, often viewing windows from multiple apps on one desktop and switching frequently between different windows — moving,…
- To learn about setting up a window to display your game in macOS, see [Managing your game window for Metal in…

##### macOS window anatomy

- A macOS window consists of a frame and a body area.
- The *frame* of a window appears above the body area and can include window controls and a [toolbar](https://developer.apple.com/design/human-interface-guidelines/toolbars).

##### macOS window states

- A macOS window can have one of three states:
  - **Main.** The frontmost window that people view is an app’s main window. There can be only one main window per app.
  - **Key.** Also called the *active window*, the key window accepts people’s input.
  - **Inactive.** A window that’s not in the foreground is an inactive window.
- The system gives main, key, and inactive windows different appearances to help people visually identify them.
> **Note:** Some windows — typically, panels like Colors or Fonts — become the key window only when people click the window’s title bar or a component that requires keyboard input, such as a text field.
- **Make sure custom windows use the system-defined appearances.**
- **Avoid putting critical information or actions in a bottom bar, because people often relocate a window in a way that hides its bottom edge.**

#### visionOS

- visionOS defines two main window styles: default and volumetric.
> **Note:** visionOS also defines the *plain* window style, which is similar to the default style, except that the upright plane doesn’t use the glass background.
- The system defines the initial position of the first window or volume people open in your app or game.

##### visionOS windows

- The default window style consists of an upright plane that uses an unmodifiable background [material](https://developer.apple.com/design/human-interface-guidelines/materials)…
- **Prefer using a window to present a familiar interface and to support familiar tasks.**
- **Retain the window’s glass background.**
- **Choose an initial window size that minimizes empty areas within it.**
- **Aim for an initial shape that suits a window’s content.**
- **Choose a minimum and maximum size for each window to help keep your content looking great.**
- **Minimize the depth of 3D content you display in a window.**

##### visionOS volumes

- You can use a volume to display 2D or 3D content that people can view from any angle.
- **Prefer using a volume to display rich, 3D content.**
- **Place 2D content so it looks good from multiple angles.**
- **In general, use dynamic scaling.**
- **Take advantage of the default baseplate appearance to help people discern the edges of a volume.**
- **Consider offering high-value content in an ornament.**
- **Choose an alignment that supports the way people interact with your volume.**

## Recursos relacionados

- *Related:*
  - [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
  - [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views)
  - [Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking)
- *Developer documentation:*
  - [Windows](https://developer.apple.com/documentation/swiftui/windows) — SwiftUI
  - [WindowGroup](https://developer.apple.com/documentation/swiftui/windowgroup) — SwiftUI
  - [UIWindow](https://developer.apple.com/documentation/uikit/uiwindow) — UIKit
  - [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) — AppKit

## Vídeos que la explican

- [Elevate the design of your iPad app](https://developer.apple.com/videos/play/wwdc2025/208) → `references/videos/2025-208.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 9, 2025 | Added best practices, and updated with guidance for resizable windows in iPadOS. |
| June 10, 2024 | Updated to include guidance for using volumes in visionOS 2 and added game-specific examples. |
| June 21, 2023 | Updated to include guidance for visionOS. |
