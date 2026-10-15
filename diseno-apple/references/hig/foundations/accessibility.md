# Accessibility — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/accessibility
- Descargado: 2026-10-15
- Sección: foundations
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2025-06-09 — Added guidance and links for Assistive Access, Switch Control, and Accessibility Nutrition Labels.

> Resumen de Apple: Accessible user interfaces empower everyone to have a great experience with your app or game.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- When you design for accessibility, you reach a larger audience and create a more inclusive experience.
  - **Intuitive.** Your interface uses familiar and consistent interactions that make tasks straightforward to perform.
  - **Perceivable.** Your interface doesn’t rely on any single method to convey information.
  - **Adaptable.** Your interface adapts to how people want to use their device, whether by supporting system accessibility features or letting people personalize settings.
- As you design your app, audit the accessibility of your interface.

### Vision

- The people who use your interface may be blind, color blind, or have low vision or light sensitivity.
- **Support larger text sizes.**
  - «Ideally, give people the option to enlarge text by at least 200 percent (or 140 percent in watchOS apps).»
- **Use recommended defaults for custom type sizes.**

| Platform | Default size | Minimum size |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

- **Bear in mind that font weight can also impact how easy text is to read.**
- **Strive to meet color contrast minimum standards.**

| Text size | Text weight | Minimum contrast ratio |
|---|---|---|
| Up to 17 pts | All | 4.5:1 |
| 18 pts | All | 3:1 |
| All | Bold | 3:1 |

- If your app doesn’t provide this minimum contrast by default, ensure it at least provides a higher contrast color scheme when the system setting Increase Contrast is turned on.
  - ❌ Ejemplo incorrecto: A button with insufficient color contrast
  - ✅ Ejemplo correcto: A button with sufficient color contrast
- **Prefer system-defined colors.**
- **Convey information with more than color alone.**
  - ❌ Ejemplo incorrecto: For someone with red-green color blindness, these indicators might appear the same.
  - ✅ Ejemplo correcto: Both visual indicators and color help differentiate between indicators.
- **Describe your app’s interface and content for VoiceOver.**

### Hearing

- The people who use your interface may be deaf or hard of hearing.
- **Support text-based ways to enjoy audio and video.**
  - **Captions** give people the textual equivalent of audible information in video or audio-only content.
  - **Subtitles** allow people to read live onscreen dialogue in their preferred language. Subtitles are great for TV shows and movies.
  - **Audio descriptions** are interspersed between natural pauses in the main audio of a video and supply spoken narration of important information that’s presented only visually.
  - **Transcripts** provide a complete textual description of a video, covering both audible and visual information.
- For developer guidance, see [Selecting subtitles and alternative audio…
- **Use haptics in addition to audio cues.**
- **Augment audio cues with visual cues.**

### Mobility

- Ensure your interface offers a comfortable experience for people with limited dexterity or mobility.
- **Offer sufficiently sized controls.**

| Platform | Default control size | Minimum control size |
|---|---|---|
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |
| tvOS | 66x66 pt | 56x56 pt |
| visionOS | 60x60 pt | 28x28 pt |
| watchOS | 44x44 pt | 28x28 pt |

- **Consider spacing between controls as important as size.**
  - «In general, it works well to add about 12 points of padding around elements that include a bezel.»
  - «For elements without a bezel, about 24 points of padding works well around the element’s visible edges.»
  - ❌ Ejemplo incorrecto: Elements with insufficient padding
  - ✅ Ejemplo correcto: Elements with sufficient padding
- **Support simple gestures for common interactions.**
- **Offer alternatives to gestures.**
- **Let people use Voice Control to give guidance and enter information verbally.**
- **Integrate with Siri and Shortcuts to let people perform tasks using voice alone.**
- **Support mobility-related assistive technologies.**

### Speech

- Apple’s accessibility features help people with speech disabilities and people who prefer text-based interactions to communicate effectively using their devices.
- **Let people use the keyboard alone to navigate and interact with your app.**
- **Support Switch Control.**

### Cognitive

- When you minimize complexity in your app or game, all people benefit.
- **Keep actions simple and intuitive.**
- **Minimize use of time-boxed interface elements.**
- **Consider offering difficulty accommodations in games.**
- **Let people control audio and video playback.**
- **Allow people to opt out of flashing lights in video playback.**
- **Be cautious with fast-moving and blinking animations.**
  - Tightening animation springs to reduce bounce effects
  - Tracking animations directly with people’s gestures
  - Avoiding animating depth changes in z-axis layers
  - Replacing transitions in x-, y-, and z-axes with fades to avoid motion
  - Avoiding animating into and out of blurs
- **Optimize your app’s UI for Assistive Access.**
- To optimize your app for this mode, use the following guidelines when Assistive Access is turned on:
  - Identify the core functionality of your app and consider removing noncritical workflows and UI elements.
  - Break up multistep workflows so people can focus on a single interaction per screen.
  - Always ask for confirmation twice whenever people perform an action that’s difficult to recover from, such a deleting a file.
- For developer guidance, see [Assistive Access](https://developer.apple.com/documentation/accessibility/assistive-access).

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS.*

#### visionOS

- visionOS offers a variety of accessibility features people can use to interact with their surroundings in ways that are comfortable and work best for them, including head and…
- **Prioritize comfort.**
  - Keep interface elements within a person’s field of view.
  - Reduce the speed and intensity of animated objects, particularly in someone’s peripheral vision.
  - Be gentle with camera and video motion, and avoid situations where someone may feel like the world around them is moving without their control.
  - Avoid anchoring content to the wearer’s head, which may make them feel stuck and confined, and also prevent them from using assistive technologies like Pointer Control.
  - Minimize the need for large and repetitive gestures, as these can become tiresome and may be difficult depending on a person’s surroundings.
- For additional guidance, see [Create accessible spatial experiences](https://developer.apple.com/videos/play/wwdc2023/10034) and [Design considerations for vision and…

## Recursos relacionados

- *Related:*
  - [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion)
  - [Typography](https://developer.apple.com/design/human-interface-guidelines/typography)
  - [VoiceOver](https://developer.apple.com/design/human-interface-guidelines/voiceover)
- *Developer documentation:*
  - [Building accessible apps](https://developer.apple.com/accessibility/)
  - [Accessibility framework](https://developer.apple.com/documentation/accessibility)
  - [Overview of Accessibility Nutrition Labels](https://devcms.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels)

## Vídeos que la explican

- [Support Full Keyboard Access in your iOS app](https://developer.apple.com/videos/play/wwdc2021/10120) → `references/videos/2021-10120.md`
- [Create accessible spatial experiences](https://developer.apple.com/videos/play/wwdc2023/10034) → `references/videos/2023-10034.md`
- [Design considerations for vision and motion](https://developer.apple.com/videos/play/wwdc2023/10078) → `references/videos/2023-10078.md`
- [Refine accessibility for custom controls](https://developer.apple.com/videos/play/wwdc2026/220) → `references/videos/2026-220.md`
- [Principles of inclusive app design](https://developer.apple.com/videos/play/wwdc2025/316) → `references/videos/2025-316.md`
- [Evaluate your app for Accessibility Nutrition Labels](https://developer.apple.com/videos/play/wwdc2025/224) → `references/videos/2025-224.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 9, 2025 | Added guidance and links for Assistive Access, Switch Control, and Accessibility Nutrition Labels. |
| March 7, 2025 | Expanded and refined all guidance. Moved Dynamic Type guidance to the Typography page, and moved VoiceOver guidance to a new VoiceOver page. |
| June 10, 2024 | Added a link to Apple’s Unity plug-ins for supporting Dynamic Type. |
| December 5, 2023 | Updated visionOS Zoom lens artwork. |
| June 21, 2023 | Updated to include guidance for visionOS. |
