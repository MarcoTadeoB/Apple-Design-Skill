# Immersive experiences — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/immersive-experiences
- Descargado: 2026-10-15
- Sección: foundations
- Plataformas: visionos
- Última actualización: 2025-06-09 — Clarified guidance and noted the availability of portrait-oriented progressive immersion.

> Resumen de Apple: In visionOS, you can design apps and games that extend beyond windows and volumes, immersing people in your content.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- You can choose whether your visionOS app or game launches in the Shared Space or in a Full Space.

### Immersion and passthrough

- In visionOS, people use passthrough to see their physical surroundings.
- People can also use the [Digital Crown](https://developer.apple.com/design/human-interface-guidelines/digital-crown) at any time to manage app or game content or adjust…
- The system also helps people remain comfortable by automatically changing the opacity of content in certain situations.
  - «In more immersive experiences — such as in the `progressive` and `full` styles described below — the system defines a boundary that extends about 1.5 meters from the initial position of the wearer’s head.»

#### Immersion styles

- When your app or game transitions to a Full Space, the system hides other apps so people can focus on yours.
- visionOS offers several ways to immerse people in your content in the Shared Space as well as when you transition to a Full Space.
  - **Use dimmed passthrough to bring attention to your content.** You can subtly dim or tint passthrough and other visible content to bring attention to your app in the Shared Space…
  - **Create unbounded 3D experiences.** Use the `mixed` immersion style in a Full Space to blend your content with passthrough.
  - **Use `progressive` immersion to blend your custom environment with a person’s surroundings.** You can use the `progressive` style in a Full Space to display a custom environment…
  - **Use `full` immersion to create a fully immersive experience.** You can use the `full` style in a Full Space to display a 360-degree custom environment that completely replaces…

### Best practices

- **Offer multiple ways to use your app or game.**
- **Prefer launching your app or game in the Shared Space or using the `mixed` immersion style.**
- **Reserve immersion for meaningful moments and content.**
- **Help people engage with key moments in your app or game, regardless of the level of immersion.**
- **Prefer subtle tint colors for passthrough.**

### Promoting comfort

- **Be mindful of people’s visual comfort.**
- **Choose a style of immersion that supports the movements people might make while they’re in your app or game.**
- **Avoid encouraging people to move while they’re in a progressive or fully immersive experience.**
- **If you use the `mixed` immersion style, avoid obscuring passthrough too much.**
- **Adopt ARKit if you want to blend custom content with someone’s surroundings.**

### Transitioning between immersive styles

- **Design smooth, predictable transitions when changing immersion.**
- **Let people choose when to enter or exit a more immersive experience.**
- **Indicate the purpose of an exit control.**

### Displaying virtual hands

- When your immersive app or game transitions to a Full Space, it can ask permission to hide a person’s hands and instead show virtual hands that represent them.
- **Prefer virtual hands that match familiar characteristics.**
- **Use caution if you create virtual hands that are larger than the viewer’s hands.**
- **If there’s an interruption in hand-tracking data, fade out virtual hands and reveal the viewer’s own hands.**

### Creating an environment

- When your app or game transitions to a Full Space, you can replace passthrough with a custom environment that partially or completely surrounds a person, transporting them to a…
- **Minimize distracting content.**
- **Help people distinguish interactive objects in your environment.**
- **Keep animation subtle.**
- **Create an expansive environment, regardless of the place it depicts.**
- **Use Spatial Audio to create atmosphere.**
- **In general, avoid using a flat 360-degree image to create your environment.**
- **Help people feel grounded.**
- **Minimize asset redundancy.**

### Platform considerations

- *Not supported in iOS, iPadOS, macOS, tvOS, or watchOS.*

## Recursos relacionados

- *Related:*
  - [Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout)
  - [Motion](https://developer.apple.com/design/human-interface-guidelines/motion)
- *Developer documentation:*
  - [Creating fully immersive experiences in your app](https://developer.apple.com/documentation/visionos/creating-fully-immersive-experiences) — visionOS
  - [Incorporating real-world surroundings in an immersive experience](https://developer.apple.com/documentation/visionos/incorporating-real-world-surroundings-in-an-immersive-experience) — visionOS
  - [ImmersionStyle](https://developer.apple.com/documentation/swiftui/immersionstyle) — visionOS
  - [Immersive spaces](https://developer.apple.com/documentation/swiftui/immersive-spaces) — SwiftUI

## Vídeos que la explican

- [Design immersive environments for visionOS apps and the spatial web](https://developer.apple.com/videos/play/wwdc2026/234) → `references/videos/2026-234.md`
- [Principles of spatial design](https://developer.apple.com/videos/play/wwdc2023/10072) → `references/videos/2023-10072.md`
- [Design spatial SharePlay experiences](https://developer.apple.com/videos/play/wwdc2023/10075) → `references/videos/2023-10075.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 9, 2025 | Clarified guidance and noted the availability of portrait-oriented progressive immersion. |
| November 19, 2024 | Refined immersion style guidance and added artwork. |
| June 10, 2024 | Added guidance for tinting passthrough and specifying initial, minimum, and maximum immersion levels. |
| May 7, 2024 | Added guidance for creating an environment. |
| February 2, 2024 | Clarified guidance for choosing an immersion style that matches the experience your app provides. |
| October 24, 2023 | Updated artwork. |
| June 21, 2023 | New page. |
