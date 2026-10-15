# Playing haptics — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/playing-haptics
- Descargado: 2026-10-15
- Sección: patterns
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2024-05-07 — Added guidance for playing haptics on Apple Pencil Pro.

> Resumen de Apple: Playing haptics can engage people’s sense of touch and bring their familiarity with the physical world into your app or game.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Depending on the platform and the device people are using, the system can play haptics in addition to visual and auditory feedback.
- In addition to built-in haptic capabilities, some external input devices can also play haptics.
  - In an iPadOS, macOS, tvOS, or visionOS app or game, [game controllers](https://developer.apple.com/design/human-interface-guidelines/game-controls) can provide haptic feedback…
  - [Apple Pencil Pro](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble) and some trackpads can provide haptic feedback when connected to…

### Best practices

- **Use system-provided haptic patterns according to their documented meanings.**
- **Use haptics consistently throughout your app or game.**
- **Prefer using haptics to complement other feedback in your app or game.**
- **Avoid overusing haptics.**
- **In most apps, prefer playing short haptics that complement discrete events.**
- **Make haptics optional.**
- **Be aware that playing haptics might impact other user experiences.**

### Custom haptics

- Games often use custom haptics to enhance gameplay.
- You can design custom haptic patterns that vary dynamically, based on user input or context.
- There are two basic building blocks you can use to generate custom haptic patterns.
  - *Transient* events are brief and compact, often feeling like taps or impulses.
  - *Continuous* events feel like sustained vibrations, such as the experience of the lasers effect in a message.
- Regardless of the type of haptic event you use to generate a custom haptic, you can also control its *sharpness* and *intensity*.
- By combining transient and continuous events, varying sharpness and intensity, and including optional audio content, you can create a wide range of different haptic experiences.

### Platform considerations

#### iOS

- On supported iPhone models, you can add haptics to your experience in the following ways:
  - Use standard UI components — like [toggles](https://developer.apple.com/design/human-interface-guidelines/toggles),…
  - When it makes sense, use a feedback generator to play one of several predefined haptic patterns in the categories of…

##### Notification

- Notification haptics provide feedback about the outcome of a task or action, such as depositing a check or unlocking a vehicle.

##### Impact

- Impact haptics provide a physical metaphor you can use to complement a visual experience.

##### Selection

- Selection haptics provide feedback while the values of a UI element are changing.

#### macOS

- When a Magic Trackpad is available, your app can provide one of the three following haptic patterns in response to a drag operation or force click.

| Haptic feedback pattern | Description |
|---|---|
| Alignment | Indicates the alignment of a dragged item. For example, this pattern could be used in a drawing app when the people drag a shape into alignment with another shape. Other scenarios where this type of feedback could be used might include scaling an object to fit within specific dimensions, positioning an object at a preferred location, or reaching the beginning/end or minimum/maximum of something like a scrubber in a video app. |
| Level change | Indicates movement between discrete levels of pressure. For example, as people press a fast-forward button on a video player, playback could increase or decrease and haptic feedback could be provided as different levels of pressure are reached. |
| Generic | Intended for providing general feedback when the other patterns don’t apply. |

- For developer guidance, see [NSHapticFeedbackPerformer](https://developer.apple.com/documentation/appkit/nshapticfeedbackperformer).

#### watchOS

- Apple Watch Series 4 and later provides haptic feedback for the Digital Crown, which gives people a more tactile experience as they scroll through content.
- watchOS defines the following set of haptics, each of which conveys a specific meaning to people.

**Pestaña «Notification»**

- **Notification.**

**Pestaña «Up»**

- **Up.**

**Pestaña «Down»**

- **Down.**

**Pestaña «Success»**

- **Success.**

**Pestaña «Failure»**

- **Failure.**

**Pestaña «Retry»**

- **Retry.**

**Pestaña «Start»**

- **Start.**

**Pestaña «Stop»**

- **Stop.**

**Pestaña «Click»**

- **Click.**

## Recursos relacionados

- *Related:*
  - [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback)
  - [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures)
- *Developer documentation:*
  - [Core Haptics](https://developer.apple.com/documentation/corehaptics)

## Vídeos que la explican

- [Practice audio haptic design](https://developer.apple.com/videos/play/wwdc2021/10278) → `references/videos/2021-10278.md`
- [Introducing Core Haptics](https://developer.apple.com/videos/play/wwdc2019/520) → `references/videos/2019-520.md`

## Registro de cambios

| Date | Changes |
|---|---|
| May 7, 2024 | Added guidance for playing haptics on Apple Pencil Pro. |
| June 21, 2023 | Updated to include guidance for visionOS. |
