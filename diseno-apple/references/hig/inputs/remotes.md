# Remotes — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/remotes
- Descargado: 2026-10-15
- Sección: inputs
- Plataformas: tvos
- Última actualización: sin registro de cambios

> Resumen de Apple: The Siri Remote is the primary input method for Apple TV, helping people feel connected to onscreen content from across the room.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- In addition to several specific buttons, the Siri Remote combines a clickpad and touch surface to support familiar gestures like swipe and press that people use to navigate tvOS…

### Best practices

- **Prefer using standard gestures to perform standard actions.**
  - «Unless people are actively playing a game, they expect the remote to behave in standard ways in every app they use.»
- **Be consistent with the tvOS focus experience.**
- **Provide clear feedback that shows people what happens when they make gestures in your app.**
- **Define new gestures only when it makes sense in your app.**
- **Differentiate between press and tap, and avoid responding to an inadvertent tap.**
- **Consider using the position of a tap to aid with navigation or gameplay.**
- **In almost all cases, open the parent of the current screen when people press the Back button.**
  - «The exception to this standard behavior is when people are actively playing a game, where it can be easy to accidentally press the Back button repeatedly.»
- **Respond correctly to the Play/Pause button during media playback.**

### Gestures

- The clickpad’s touch surface detects swipes and presses.
- **Swipe.**
- **Press.**

### Buttons

- Ensure that your app or game responds to specific presses in the following ways.

| Button or area | Expected behavior in an app | Expected behavior in a game |
|---|---|---|
| Touch surface (swipe) | Navigates. Changes focus. | Performs directional pad behavior. |
| Touch surface (press) | Activates a control or an item. Navigates deeper. | Performs primary button behavior. |
| Back | Returns to previous screen. Exits to Apple TV Home Screen. | Pauses/resumes gameplay. Returns to previous screen, exits to main game menu, or exits to Apple TV Home Screen. |
| Play/Pause | Activates media playback. Pauses/resumes media playback. | Performs secondary button behavior. Skips intro video. |

### Compatible remotes

- Some remotes that are compatible with Apple TV include buttons for browsing live TV or other channel-based content.
- **If your live-viewing app provides an EPG, respond to a remote’s EPG-browsing buttons in ways people expect.**
- **While your content plays, respond to a compatible remote’s “page up” or “page down” button by changing the channel.**

### Platform considerations

- *Not supported in iOS, iPadOS, macOS, visionOS, or watchOS.*

## Recursos relacionados

- *Related:*
  - [Use your Siri Remote or Apple TV Remote with Apple TV](https://support.apple.com/en-us/HT205305)
