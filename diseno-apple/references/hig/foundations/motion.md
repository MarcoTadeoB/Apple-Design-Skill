# Motion — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/motion
- Descargado: 2026-10-15
- Sección: foundations
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2025-09-09 — Added guidance for Liquid Glass.

> Resumen de Apple: Beautiful, fluid motions bring the interface to life, conveying status, providing feedback and instruction, and enriching the visual experience of your app or game.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Many system components automatically include motion, letting you offer familiar and consistent experiences throughout your app or game.
- If you design custom motion, follow the guidelines below.

### Best practices

- **Add motion purposefully, supporting the experience without overshadowing it.**
- **Make motion optional.**

### Providing feedback

- **Strive for realistic feedback motion that follows people’s gestures and expectations.**
- **Aim for brevity and precision in feedback animations.**
- **In apps, generally avoid adding motion to UI interactions that occur frequently.**
- **Let people cancel motion.**
- **Consider using animated symbols where it makes sense.**

### Leveraging platform capabilities

- **Make sure your game’s motion looks great by default on each platform you support.**
  - «In most games, maintaining a consistent frame rate of 30 to 60 fps typically results in a smooth, visually appealing experience.»
- **Let people customize the visual experience of your game to optimize performance or battery life.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, or tvOS.*

#### visionOS

- In addition to subtly communicating context, drawing attention to information, and enriching immersive experiences, motion in visionOS can combine with…
- **As much as possible, avoid displaying motion at the edges of a person’s field of view.**
- **Help people remain comfortable when showing the movement of large virtual objects.**
> **Note:** People can experience discomfort even when they’re the ones moving a large virtual object, such as a window.
- **Consider using fades when you need to relocate an object.**
- **In general, avoid letting people rotate a virtual world.**
- **Consider giving people a stationary frame of reference.**
- **Avoid showing objects that oscillate in a sustained way.**
  - «In particular, you want to avoid showing an oscillation that has a frequency of around 0.2 Hz because people can be very sensitive to this frequency.»

#### watchOS

- SwiftUI provides a powerful and streamlined way to add motion to your app.
> **Note:** All layout- and appearance-based animations automatically include built-in easing that plays at the start and end of the animation.

## Recursos relacionados

- *Related:*
  - [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback)
  - [Accessibility](https://www.apple.com/accessibility/)
  - [Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout)
  - [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences)
- *Developer documentation:*
  - [Animating views and transitions](https://developer.apple.com/tutorials/swiftui/animating-views-and-transitions) — SwiftUI

## Vídeos que la explican

- [Enhance your UI animations and transitions](https://developer.apple.com/videos/play/wwdc2024/10145) → `references/videos/2024-10145.md`
- [Create custom visual effects with SwiftUI](https://developer.apple.com/videos/play/wwdc2024/10151) → `references/videos/2024-10151.md`
- [Design considerations for vision and motion](https://developer.apple.com/videos/play/wwdc2023/10078) → `references/videos/2023-10078.md`

## Registro de cambios

| Date | Changes |
|---|---|
| September 9, 2025 | Added guidance for Liquid Glass. |
| June 10, 2024 | Added game-specific examples and enhanced guidance for using motion in games. |
| February 2, 2024 | Enhanced guidance for minimizing peripheral motion in visionOS apps. |
| June 21, 2023 | Updated to include guidance for visionOS. |
