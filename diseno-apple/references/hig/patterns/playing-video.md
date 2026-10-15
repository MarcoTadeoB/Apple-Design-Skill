# Playing video — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/playing-video
- Descargado: 2026-10-15
- Sección: patterns
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2023-09-12 — Corrected the recommended width for a thumbnail in visionOS.

> Resumen de Apple: People expect to enjoy rich video experiences on their devices, regardless of the app or game they’re using.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- The system provides video players designed for you to use to embed playback experiences within your app or game in iOS, iPadOS, macOS, tvOS, and visionOS.
- The system-provided video players support different aspect-ratio playback modes and in most platforms, Picture in Picture (PiP) viewing mode.
  - In full-screen — or *aspect-fill* — mode, the video scales to fill the display, and some edge cropping may occur.
  - In fit-to-screen — or *aspect* — mode, the entire video is visible onscreen, and letterboxing or pillarboxing occurs as needed.
- In visionOS and tvOS, the built-in video player also provides *transport controls,* which let people perform playback tasks, like turning on subtitles or changing the audio…

### Best practices

- **Use the system video player to give people a familiar and convenient experience.**
- **Always display video content at its original aspect ratio.**
- Here are some examples that show how padding can affect video display on iPhone Xs.

**Pestaña «Result of padding a 4:3 video»**

  - ✅ Ejemplo correcto: An illustration of iPhone in landscape orientation. A blue rectangle shows the AVKit safe area within the screen. Overlaying the safe area and extending beyond it on all sides is a purple rectangle…
  - ❌ Ejemplo incorrecto: An illustration of iPhone in landscape orientation. A blue rectangle shows the AVKit safe area within the screen. Overlaying the safe area and extending beyond its top and bottom edges is a purple…

**Pestaña «Result of padding a 21:9 video»**

  - ✅ Ejemplo correcto: An illustration of iPhone in landscape orientation. A blue rectangle shows the AVKit safe area within the screen. Overlaying the safe area and extending to the top and bottom edges of the device is…
  - ❌ Ejemplo incorrecto: An illustration of iPhone in landscape orientation. A blue rectangle shows the AVKit safe area within the screen. Overlaying the safe area is a purple rectangle representing the 21:9 video area plus…
- **Provide additional information when it adds value.**
- **Support the interactions people expect, regardless of the input device they’re using to control playback.**
- **If people need to access playback options or content-specific information in your tvOS app, consider adding a transport control or a custom content tab.**
- **Avoid allowing audio from different sources to mix as viewers switch between modes.**

### Integrating with the TV app

- The TV app provides global access to favorite, recently played, and recommended video content from across the system.
- **Ensure a smooth transition to your app.**
- **Show the expected content immediately.**
- **Avoid asking people if they want to resume playback.**
- **Play or pause playback when people press Space on a connected Bluetooth keyboard.**
- **Make sure content plays for the correct viewer.**
- **Use the previous end time when resuming playback of a long video clip.**

#### Loading content

- **Avoid displaying loading screens when possible.**
- **Start playback immediately.**
- **Minimize loading screen content.**

#### Exiting playback

- After exiting playback, people remain in your app rather than returning to the TV app, so it’s a good idea to help them avoid becoming disoriented.
- **Show a contextually relevant screen.**
- **Be prepared for an immediate exit.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, or macOS.*

#### tvOS

- **Defer to content when displaying logos or noninteractive overlays above video.**
- **Show interactive overlays gracefully.**
  - «For the best user experience, implement a minimum delay of 0.5 seconds to pause playing media, and display an interactive overlay.»

#### visionOS

- **Help people stay comfortable when playing video in your app.**
  - Letting them choose when to start playing a video
  - Using a small window for playback, letting people resize it if they want
  - Making sure people can see their surroundings during playback
- **In a fully immersive experience, avoid letting virtual content obscure playback or transport controls.**
- **Avoid automatically starting a fully immersive video playback experience.**
- **Create a thumbnail track if you want to support scrubbing.**
  - «To improve performance, supply a set of thumbnails that each measure 160 px in width.»
- **Avoid expanding an inline video player to fill a window.**
- **Use a RealityKit video player if you need to play video in a view like a splash screen or a transitional view.**

#### watchOS

- In watchOS, the system manages video playback.
- **Keep video clips short.**
  - «Prefer shorter clips of no longer than 30 seconds.»
- **Use the recommended sizes and encoding values for media assets.**

| Attribute | Value |
|---|---|
| Video codec | H.264 High Profile |
| Video bit rate | 160 kbps at up to 30 fps |
| Resolution (full screen) | 208x260 px (portrait orientation) |
| Resolution (16:9) | 320x180 px (landscape orientation) |
| Audio | 64 kbps HE-AAC |

- **Avoid creating a poster image that looks like a system control.**
- **Consider creating a poster image that represents a video clip’s contents.**

## Recursos relacionados

- *Related:*
  - [Playing audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio)
  - [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback)
- *Developer documentation:*
  - [Configuring your app for media playback](https://developer.apple.com/documentation/avfoundation/configuring-your-app-for-media-playback) — AVFoundation
  - [AVKit](https://developer.apple.com/documentation/avkit)
  - [HTTP Live Streaming](https://developer.apple.com/streaming/)

## Vídeos que la explican

- [Create a great video playback experience](https://developer.apple.com/videos/play/wwdc2022/10147) → `references/videos/2022-10147.md`
- [Explore video experiences for visionOS](https://developer.apple.com/videos/play/wwdc2025/304) → `references/videos/2025-304.md`
- [Deliver a great playback experience on tvOS](https://developer.apple.com/videos/play/wwdc2021/10191) → `references/videos/2021-10191.md`

## Registro de cambios

| Date | Changes |
|---|---|
| September 12, 2023 | Corrected the recommended width for a thumbnail in visionOS. |
| June 21, 2023 | Updated to include guidance for visionOS. |
