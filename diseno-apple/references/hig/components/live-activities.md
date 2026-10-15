# Live Activities — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/live-activities
- Descargado: 2026-10-15
- Sección: components › System experiences
- Plataformas: ios,ipados,macos,watchos
- Última actualización: 2026-10-13 — Added guidance for limited width layouts, and updated supported platforms and specifications.

> Resumen de Apple: A Live Activity lets people track the progress of an activity, event, or task at a glance.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Live Activities let people keep track of tasks and events in glanceable locations across devices.
- For example, a Live Activity might show the remaining time until a food delivery order arrives, live in-game information for a soccer match, or real-time fitness metrics and…
- A Live Activity from your app starts on iPad or iPhone and automatically appears in system locations across a person’s devices:

| Platform or system experience | Location |
|---|---|
| iPad and iPhone | Lock Screen, Home Screen, in the Dynamic Island and StandBy on iPhone |
| Mac | The menu bar |
| Apple Watch | Smart Stack |
| CarPlay | CarPlay Dashboard |

### Anatomy

- Live Activities appear across the system in various locations like the Dynamic Island and the Lock Screen.
  - [Compact](https://developer.apple.com/design/human-interface-guidelines/live-activities#Compact)
  - [Minimal](https://developer.apple.com/design/human-interface-guidelines/live-activities#Minimal)
  - [Expanded](https://developer.apple.com/design/human-interface-guidelines/live-activities#Expanded)
  - [Lock Screen](https://developer.apple.com/design/human-interface-guidelines/live-activities#Lock-Screen)
- In iOS and iPadOS, your Live Activity appears throughout the system using these presentations.

#### Compact

- In the Dynamic Island, the system uses the compact presentation when only one Live Activity is active.
- For design guidance, see [Compact presentation](https://developer.apple.com/design/human-interface-guidelines/live-activities#Compact-presentation).

#### Minimal

- When multiple Live Activities are active, the system uses the minimal presentation to display up to three of them in the Dynamic Island.
- For design guidance, see [Minimal presentation](https://developer.apple.com/design/human-interface-guidelines/live-activities#Minimal-presentation).

#### Expanded

- When people touch and hold a Live Activity in compact or minimal presentation, the system displays the expanded presentation.
- For design guidance, see [Expanded presentation](https://developer.apple.com/design/human-interface-guidelines/live-activities#Expanded-presentation).

#### Lock Screen

- The system uses the Lock Screen presentation to display a banner at the bottom of the Lock Screen.
- When you alert people about Live Activity updates on devices that don’t support the Dynamic Island, the Lock Screen presentation briefly appears as a banner that overlays the…
- For design guidance, see [Lock Screen presentation](https://developer.apple.com/design/human-interface-guidelines/live-activities#Lock-Screen-presentation).

#### StandBy

- On iPhone in StandBy, your Live Activity appears in the minimal presentation.
  - «When someone taps it, it transitions to the Lock Screen presentation, scaled up by 2x to fill the screen.»
- (imagen) An image that shows the Lock Screen presentation of a Live Activity in StandBy, scaled up by 2x, with a dotted border to indicate the 2x scaling of the Live Activity.
- For design guidance, see [StandBy presentation](https://developer.apple.com/design/human-interface-guidelines/live-activities#StandBy-presentation).

### Best practices

- **Offer Live Activities for tasks and events that have a defined beginning and end.**
- **Focus on important information that people need to see at a glance.**
- **Don’t use a Live Activity to display ads or promotions**
- **Avoid displaying sensitive information.**
- **Create a Live Activity that matches your app’s visual aesthetic and personality in both dark and light appearances.**
- **If you include a logo mark, display it without a container.**
- **Don’t add elements to your app that draw attention to the Dynamic Island.**
- **Ensure text is easy to read.**
  - ❌ Ejemplo incorrecto: An illustration that shows text in the Dynamic Island that's small and difficult to read.
  - ✅ Ejemplo correcto: An illustration that shows text in the Dynamic Island with heavier weights and legible size.

#### Creating Live Activity layouts

- **Adapt to different screen sizes and presentations.**
- **Adjust element size and placement for efficient use of space.**
- **Support limited width presentations.**
  - «To avoid truncated text in contexts with limited width like the Dynamic Island on iPhone in landscape, adapt your compact and minimal presentations to fit inside a 28pt-diameter circle.»
- **Use familiar layouts for custom views.**
- **Use consistent margins and concentric placement.**
- Keep content compact and snug within a margin that’s concentric to the outer edge of the Live Activity.
  - ❌ Ejemplo incorrecto: An illustration that shows how a Live Activity places an icon too far from the edge of the Dynamic Island.
  - ✅ Ejemplo correcto: An illustration that shows how a Live Activity places an icon close to the edge of the Dynamic Island without poking into the rounded shape of the Dynamic Island.
- **When separating a block of content, place it in an inset container shape or use a thick line.**
  - ❌ Ejemplo incorrecto: An illustration that shows how a Live Activity draws content all the way to the edge of the Dynamic Island to separate content.
  - ✅ Ejemplo correcto: An illustration of a Live Activity with content in an inset, rounded shape to group it together.
  - ✅ Ejemplo correcto: An illustration of a Live Activity that uses a line to separate a block of content.
> **Tip:** To align nonrounded content in the rounded corners of the Live Activity view, it may be helpful to blur the nonrounded content in your drawing tool.
  - ❌ Ejemplo incorrecto: An illustration that shows a Live Activity with blurred text that's too far from the edge of the Dynamic Island.
  - ✅ Ejemplo correcto: An illustration that shows a Live Activity with blurred text that's close to the edge of the Dynamic Island without poking into the rounded shape of the Dynamic Island.
- **Dynamically change the height of your Live Activity on the Lock Screen or in the expanded presentation.**

#### Choosing colors

- **Carefully consider using a custom background color and opacity.**
- **Use color to express the character and identity of your app.**
- **Tint your Live Activity’s key line color so that it matches your content.**

#### Adding transitions and animating content updates

- In addition to extending and contracting transitions, Live Activities use system and custom animations with a maximum duration of two seconds.
- **Use animations to reinforce the information you’re communicating and to bring attention to updates.**
- **Animate layout changes.**
- **Try to avoid overlapping elements.**
- For developer guidance, see [Animating data updates in widgets and Live…

#### Offering interactivity

- **Make sure tapping the Live Activity opens your app at the right location.**
- **Focus on simple, direct actions.**
- **Consider letting people respond to event or progress updates.**

#### Starting, updating, and ending a Live Activity

- **Start Live Activities at appropriate times, and make it easy for people to turn them off in your app.**
- **Offer an App Shortcut that starts your Live Activity.**
- **Update a Live Activity only when new content is available.**
- **Alert people only for essential updates that require their attention.**
- **Let people track multiple events efficiently with a single Live Activity.**
- **Always end a Live Activity immediately when the task or event ends, and consider setting a custom dismissal time.**

### Presentation

- Your Live Activity needs to support all locations, devices, and their corresponding appearances.
- **Start with the iPhone design, then refine it for other contexts.**

#### Compact presentation

- **Focus on the most important information.**
- **Ensure unified information and design of the compact presentations in the Dynamic Island.**
- **Keep content as narrow as possible and ensure it’s snug against the TrueDepth camera.**
  - ❌ Ejemplo incorrecto: An illustration that shows a compact presentation that appears unbalanced and too wide because it uses padding around the TrueDepth camera.
  - ✅ Ejemplo correcto: An illustration that shows a compact presentation that’s snug around the TrueDepth camera.
- **Link to relevant app content.**

#### Minimal presentation

- **Ensure that your Live Activity is recognizable in the minimal presentation.**

#### Expanded presentation

- **Maintain the relative placement of elements to create a coherent layout between presentations.**
- **Wrap content tightly around the TrueDepth camera.**
  - ❌ Ejemplo incorrecto: An illustration that shows an expanded presentation of a Live Activity that leaves empty space next to the TrueDepth camera.
  - ✅ Ejemplo correcto: An illustration that shows an expanded presentation of a Live Activity that uses the space next to the TrueDepth camera.

#### Lock Screen presentation

- **Don’t replicate notification layouts.**
- **Choose colors that work well on a personalized Lock Screen.**
- **Make sure your design, assets, and colors look great and offer enough contrast in Dark Mode and on an Always-On display.**
- **Verify the generated color of the dismiss button.**
- **Use standard margins to align your design with notifications.**
  - «The standard layout margin for Live Activities on the Lock Screen is 14 points.»

#### StandBy presentation

- **Update your layout for StandBy.**
- **Consider using the default background color in StandBy.**
- **Use standard margins and avoid extending graphic elements to the edge of the screen.**
- **Verify your design in Night Mode.**

### CarPlay

- In CarPlay, the system automatically combines the leading and trailing elements of the compact presentation into a single layout that appears on CarPlay Dashboard.
- Your Live Activity design applies to both CarPlay and Apple Watch, so design for both contexts.
- **Consider creating a custom layout if your Live Activity would benefit from larger text or additional information.**
- **Carefully consider including buttons or toggles in your custom layout.**

### Platform considerations

- *No additional considerations for iOS or iPadOS.

#### macOS

- Active Live Activities automatically appear in the Menu bar of a paired Mac using the compact, minimal, and expanded presentations.

#### watchOS

- When a Live Activity begins on iPhone, it appears on a paired Apple Watch at the top of the Smart Stack.
- If you offer a watchOS app and someone taps the Live Activity in the Smart Stack, it opens your watchOS app.
- **Consider creating a custom watchOS layout.**
- **Carefully consider including buttons or toggles in your custom layout.**
- **Focus on essential information and significant updates.**
  - Progress, like the estimated arrival time of a delivery
  - Interactive elements, like stopwatch or timer controls
  - Significant updates, like sports score changes

### Specifications

- When you design your Live Activities, use the following values for guidance.

#### CarPlay dimensions

- The system may scale your Live Activity to best fit a vehicle’s screen size and resolution.

| Live Activity size (pt) |
|---|
| 240x78 |
| 240x100 |
| 170x78 |

- Test your designs with the CarPlay simulator and the following configurations for Smart Display Zoom — available in in Settings > Display in CarPlay:

| Configuration | Resolution (pt) |
|---|---|
| Widescreen | 1920x720 |
| Portrait | 900x1200 |
| Standard | 800x480 |

#### iOS dimensions

| Screen dimensions (portrait) | Compact (leading and trailing) | Minimal (width given as a range) | Expanded (height given as a range) | Lock Screen (height given as a range) | Limited width |
|---|---|---|---|---|---|
| 430x932 | 62.33x36.67 | 36.67–45x36.67 | 408x84–160 | 408x84–160 | 28x28 |
| 393x852 | 52.33x36.67 | 36.67–45x36.67 | 371x84–160 | 371x84–160 | 28x28 |

#### iPadOS dimensions

| Screen dimensions (portrait) | Lock Screen (height given as a range) |
|---|---|
| 1366x1024 | 500x84–160 |
| 1194x834 | 425x84–160 |
| 1012x834 | 425x84–160 |
| 1080x810 | 425x84–160 |
| 1024x768 | 425x84–160 |

#### macOS dimensions

- Use the provided iOS dimensions.

#### watchOS dimensions

- Live Activities in the Smart Stack use the same dimensions as watchOS widgets.

| Apple Watch size | Size of a Live Activity in the Smart Stack (pt) |
|---|---|
| 40mm | 152x69.5 |
| 41mm | 165x72.5 |
| 42mm | 176x72.5 |
| 44mm | 173x76.5 |
| 45mm | 184x80.5 |
| 46mm | 194x80.5 |
| 49mm (Ultra 3, 4) | 198x81.5 |
| 49mm (Ultra 1, 2) | 191x81.5 |

## Recursos relacionados

- *Developer documentation:*
  - [ActivityKit](https://developer.apple.com/documentation/activitykit)
  - [SwiftUI](https://developer.apple.com/documentation/swiftui)
  - [WidgetKit](https://developer.apple.com/documentation/widgetkit)
  - [Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy) — WidgetKit

## Vídeos que la explican

- [Live Activities essentials](https://developer.apple.com/videos/play/wwdc2026/223) → `references/videos/2026-223.md`
- [Turbocharge your app for CarPlay](https://developer.apple.com/videos/play/wwdc2025/216) → `references/videos/2025-216.md`
- [What’s new in widgets](https://developer.apple.com/videos/play/wwdc2025/278) → `references/videos/2025-278.md`

## Registro de cambios

| Date | Changes |
|---|---|
| October 13, 2026 | Added guidance for limited width layouts, and updated supported platforms and specifications. |
| December 16, 2025 | Updated guidance for all platforms, and added guidance for macOS and CarPlay. |
| June 10, 2024 | Added guidance for Live Activities in watchOS. |
| October 24, 2023 | Expanded and updated guidance and added new artwork. |
| June 5, 2023 | Updated guidance to include features of iOS 17 and iPadOS 17. |
| November 3, 2022 | Updated artwork and specifications. |
| September 23, 2022 | New page. |
