# CarPlay — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/carplay
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios
- Última actualización: 2023-05-02 — Consolidated guidance into one page.

> Resumen de Apple: CarPlay lets people get directions, make calls, send and receive messages, listen to music, and more from their car’s built-in display, all while staying focused on the road.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- People download CarPlay apps from the App Store and install them on iPhone like any other app.
- CarPlay is designed for drivers to use while they’re driving.
- To create the interface of your CarPlay app, you use the system-defined templates that are appropriate for the type of app you’re developing, such as audio, communication, or…
- To learn how to create various types of CarPlay apps and use the system-provided templates, see [CarPlay Developer…
> **Note:** CarPlay audio and video apps also work on Apple HomeView without requiring you to make any modifications to your app.

### iPhone interactions

- CarPlay shows compatible apps from the connected iPhone on the car’s built-in display, applying simplified interfaces that are optimized for use while driving.
- **Eliminate app interactions on iPhone when CarPlay is active.**
- **Never lock people out of CarPlay because the connected iPhone requires input.**
- **Make sure your app works without requiring people to unlock iPhone.**

#### Audio

- In CarPlay, keep in mind that your app coexists with other audio sources, such as the car’s own built-in radio and voice prompts from the navigation system.
- **Let people choose when to start playback.**
  - «In general, avoid beginning playback automatically unless your app’s purpose is to play a single source of audio, or your app is resuming previously interrupted audio.»
- **Start playback as soon as audio has sufficiently loaded.**
- **Display the Now Playing screen when audio is ready to play.**
- **Resume audio playback after an interruption only when it’s appropriate.**
- **When necessary, automatically adjust audio levels, but don’t change the overall volume.**

### Layout

- CarPlay supports a wide range of display resolutions with varying pixel densities and aspect ratios.

| Dimensions (pixels) | Aspect ratio |
|---|---|
| 800x480 | 5:3 |
| 960x540 | 16:9 |
| 1280x720 | 16:9 |
| 1920x720 | 8:3 |

- **Provide useful, high-value information in a clean layout that’s easy to scan from the driver’s seat.**
- **Maintain an overall consistent appearance throughout your app.**
- **Ensure that primary content stands out and feels actionable.**

### Color

- Color can indicate interactivity, impart vitality, and provide visual continuity.
- **In general, prefer a limited color palette that coordinates with your app logo.**
- **Avoid using the same color for interactive and noninteractive elements.**
- **Test your app’s color scheme under a variety of lighting conditions in an actual car.**
- **Ensure your app looks great in both dark and light environments.**
- **Choose colors that help you communicate effectively with everyone.**

### Icons and images

- CarPlay supports both landscape and portrait displays and both @2x (low resolution) and @3x (high resolution) scale factors.
- **Supply high-resolution images with scale factors of @2x and @3x for all CarPlay artwork in your app.**
- **Mirror your iPhone app icon.**
- **Don’t use black for your icon’s background.**
- Create your CarPlay app icon in the following sizes:

| @2x (pixels) | @3x (pixels) |
|---|---|
| 120x120 | 180x180 |

### Error handling

- A CarPlay app needs to handle errors gracefully and report them to people only when absolutely necessary.
- **Report errors in CarPlay, not on the connected iPhone.**

### Platform considerations

- *No additional considerations for iOS.

## Recursos relacionados

- *Related:*
  - [CarPlay](http://developer.apple.com/carplay/)
- *Developer documentation:*
  - [CarPlay App Programming Guide](https://developer.apple.com/carplay/documentation/CarPlay-App-Programming-Guide.pdf)

## Vídeos que la explican

- [Rev up your CarPlay app](https://developer.apple.com/videos/play/wwdc2026/212) → `references/videos/2026-212.md`
- [Turbocharge your app for CarPlay](https://developer.apple.com/videos/play/wwdc2025/216) → `references/videos/2025-216.md`

## Registro de cambios

| Date | Changes |
|---|---|
| May 2, 2023 | Consolidated guidance into one page. |
