# Gestures — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/gestures
- Descargado: 2026-10-15
- Sección: inputs
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2024-09-09 — Added guidance for working with system overlays in visionOS and made organizational updates.

> Resumen de Apple: A gesture is a physical motion that a person uses to directly affect an object in an app or game on their device.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Depending on the device they’re using, people can make gestures on a touchscreen, in the air, or on a range of input devices such as a trackpad, mouse, remote, or game controller…
- Every platform supports basic gestures like tap, swipe, and drag.

### Best practices

- **Give people more than one way to interact with your app.**
- **In general, respond to gestures in ways that are consistent with people’s expectations.**
- **Handle gestures as responsively as possible.**
- **Indicate when a gesture isn’t available.**

### Custom gestures

- **Add custom gestures only when necessary.**
  - Discoverable
  - Straightforward to perform
  - Distinct from other gestures
  - Not the only way to perform an important action in your app or game
- **Make custom gestures easy to learn.**
- **Use shortcut gestures to supplement standard gestures, not replace them.**
- **Avoid conflicting with gestures that access system UI.**

### Platform considerations

#### iOS, iPadOS

- In addition to the [standard gestures](https://developer.apple.com/design/human-interface-guidelines/gestures#Standard-gestures) supported in all platforms, iOS and iPadOS…

| Gesture | Common action |
|---|---|
| Three-finger swipe | Initiate undo (left swipe); initiate redo (right swipe). |
| Three-finger pinch | Copy selected text (pinch in); paste copied text (pinch out). |
| Four-finger swipe (iPadOS only) | Switch between apps. |
| Shake | Initiate undo; initiate redo. |

- **Consider allowing simultaneous recognition of multiple gestures if it enhances the experience.**

#### macOS

- People primarily interact with macOS using a [keyboard](https://developer.apple.com/design/human-interface-guidelines/keyboards) and mouse.

#### tvOS

- People expect to use [standard gestures](https://developer.apple.com/design/human-interface-guidelines/gestures#Standard-gestures) to navigate tvOS apps and games with a…

#### visionOS

- visionOS supports two categories of gestures: indirect and direct.
- People use an *indirect* gesture by looking at an object to target it, and then manipulating that object from a distance — indirectly — with their hands.
- People use a *direct* gesture to physically touch an interactive object.
- Here are the standard direct gestures people use in visionOS; see [Specifications](https://developer.apple.com/design/human-interface-guidelines/gestures#Specifications) for a…

| Direct gesture | Common use |
|---|---|
| Touch | Directly select or activate an object. |
| Touch and hold | Open a contextual menu. |
| Touch and drag | Move an object to a new location. |
| Double touch | Preview an object or file; select a word in an editing context. |
| Swipe | Reveal actions and controls; dismiss views; scroll. |
| With two hands, pinch and drag together or apart | Zoom in or out. |
| With two hands, pinch and drag in a circular motion | Rotate an object. |

- **Support standard gestures everywhere you can.**
- **Offer both indirect and direct interactions when possible.**
- **Avoid requiring specific body movements or positions for input.**

##### Designing custom gestures in visionOS

- If you want to offer a specific interaction for your experience that people can’t perform using an existing system gesture, consider designing a custom gesture.
- **Prioritize comfort.**
- **Carefully consider complex custom gestures that involve multiple fingers or both hands.**
- **Avoid custom gestures that require using a specific hand.**

##### Working with system overlays in visionOS

- In visionOS 2 and later, people can look at the palm of one hand and use gestures to quickly access system overlays for Home and Control Center.
> **Note:** The system overlay is the default method of accessing Control Center in visionOS 2 and later.
- When designing apps and games that use custom gestures or anchor content to a person’s hands, it’s important to take interactions with the system overlays into consideration.
- **Reserve the area around a person’s hand for system overlays and their related gestures.**
- **Consider deferring the system overlay behavior when designing an immersive app or game.**
> **Note:** Apps and games that you built for visionOS 1 defer the system overlay behavior by default.
- **Use caution when designing custom gestures that involve a rolling motion of the hand, wrist, and forearm.**

#### watchOS

##### Double tap

- In watchOS 11 and later, people can use the double-tap gesture to scroll through lists and scroll views, and to advance between vertical tab views.
- **Avoid setting a primary action in views with lists, scroll views, or vertical tabs.**
- **Choose the button that people use most commonly as the primary action in a view.**

### Specifications

#### Standard gestures

- The system provides APIs that support the familiar gestures people use with their devices, whether they use a touchscreen, an indirect gesture in visionOS, or an input device…

| Gesture | Supported in | Common action |
|---|---|---|
| Tap | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Activate a control; select an item. |
| Swipe | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Reveal actions and controls; dismiss views; scroll. |
| Drag | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Move a UI element. |
| Touch (or pinch) and hold | iOS, iPadOS, tvOS, visionOS, watchOS | Reveal additional controls or functionality. |
| Double tap | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Zoom in; zoom out if already zoomed in; perform a primary action on Apple Watch Series 9 and Apple Watch Ultra 2. |
| Zoom | iOS, iPadOS, macOS, tvOS, visionOS | Zoom a view; magnify content. |
| Rotate | iOS, iPadOS, macOS, tvOS, visionOS | Rotate a selected item. |

- For guidance on supporting additional gestures and button presses on specific input devices, see [Pointing…

## Recursos relacionados

- *Related:*
  - [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback)
  - [Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes)
  - [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics)
- *Developer documentation:*
  - [Gestures](https://developer.apple.com/documentation/swiftui/gestures) — SwiftUI
  - [UITouch](https://developer.apple.com/documentation/uikit/uitouch) — UIKit

## Vídeos que la explican

- [Enhance your UI animations and transitions](https://developer.apple.com/videos/play/wwdc2024/10145) → `references/videos/2024-10145.md`
- [Design for spatial input](https://developer.apple.com/videos/play/wwdc2023/10073) → `references/videos/2023-10073.md`

## Registro de cambios

| Date | Changes |
|---|---|
| September 9, 2024 | Added guidance for working with system overlays in visionOS and made organizational updates. |
| September 15, 2023 | Updated specifications to include double tap in watchOS. |
| June 21, 2023 | Changed page title from Touchscreen gestures and updated to include guidance for visionOS. |
