# Multitasking — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/multitasking
- Descargado: 2026-10-15
- Sección: patterns
- Plataformas: ios,ipados,macos,tvos,visionos
- Última actualización: 2025-06-09 — Reorganized guidance in platform considerations, and added guidance for multitasking with multiple windows in iPadOS.

> Resumen de Apple: Multitasking lets people switch quickly from one app to another, performing tasks in each.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- People expect to use multitasking on their devices, and they may think something is wrong if your app doesn’t allow it.
- In addition to app switching, multitasking can present different experiences on different devices; see [Platform…

### Best practices

- A great multitasking experience helps people accomplish tasks in multiple apps by managing content in a variety of simultaneous contexts.
- **Pause activities that require people’s attention or active participation when they switch away.**
- **Respond smoothly to audio interruptions.**
  - Pause audio indefinitely for primary audio interruptions, such as playing music, podcasts, or audiobooks.
  - Temporarily lower the volume or pause the audio for shorter interruptions, such as GPS directional notifications, and resume the original volume or playback when the interruption…
- For guidance, see [Playing audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio).
- **Finish user-initiated tasks in the background.**
- **Use notifications sparingly.**

### Platform considerations

- *Not supported in watchOS.*

#### iOS

- On iPhone, multitasking lets people use FaceTime or watch a video in Picture in Picture while they also use a different app.

#### iPadOS

- On iPad, people can view and interact with the [windows](https://developer.apple.com/design/human-interface-guidelines/windows) of several different apps at the same time.
- People can use iPad with either full-screen or windowed apps.
- When using windowed apps, app windows are resizable, and people can arrange them to suit their needs with behavior similar to macOS.
- Additionally, videos and FaceTime calls can also play in a Picture in Picture overlay above other content regardless of whether apps are full screen or windowed.
> **Note:** Apps don’t control multitasking configurations or receive any indication of the ones that people choose.
- To help your app respond correctly when people open it while windowed, make sure it adapts gracefully to different screen sizes.

#### macOS

- On Mac, multitasking is the default experience because people typically run more than one app at a time, switching between windows and tasks as they work.

#### tvOS

- On Apple TV, people can play or browse content while also playing movies or TV shows in Picture in Picture (where supported).

#### visionOS

- On Apple Vision Pro, people can run multiple apps at the same time in the Shared Space, viewing and switching between windows and volumes throughout the space.
- Only one window is active at a time in the Shared Space.
> **Note:** When an app is the Now Playing app, closing its window automatically pauses audio playback; if people want to resume playback, they can do so in Control Center without opening the window.
- **Avoid interfering with the system-provided multitasking behavior.**
- **Don’t pause a window’s video playback when people look away from it.**
- **Be prepared for situations where your audio can duck.**
  - «Unless an app is currently the Now Playing app, its audio can duck when people look away from it to another app.»

## Recursos relacionados

- *Related:*
  - [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
  - [Windows](https://developer.apple.com/design/human-interface-guidelines/windows)
  - [Playing video](https://developer.apple.com/design/human-interface-guidelines/playing-video)
- *Developer documentation:*
  - [Responding to the launch of your app](https://developer.apple.com/documentation/uikit/responding-to-the-launch-of-your-app) — UIKit
  - [Multitasking on iPad, Mac, and Apple Vision Pro](https://developer.apple.com/documentation/uikit/multitasking-on-ipad-mac-and-apple-vision-pro) — UIKit

## Vídeos que la explican

- [Elevate the design of your iPad app](https://developer.apple.com/videos/play/wwdc2025/208) → `references/videos/2025-208.md`
- [Make your UIKit app more flexible](https://developer.apple.com/videos/play/wwdc2025/282) → `references/videos/2025-282.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 9, 2025 | Reorganized guidance in platform considerations, and added guidance for multitasking with multiple windows in iPadOS. |
| December 5, 2023 | Added artwork for primary and auxiliary windows in iPadOS. |
| June 21, 2023 | Updated to include guidance for visionOS. |
