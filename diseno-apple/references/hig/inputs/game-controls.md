# Game controls — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/game-controls
- Descargado: 2026-10-15
- Sección: inputs
- Plataformas: ios,ipados,macos,tvos,visionos
- Última actualización: 2025-06-09 — Updated touch control best practices, updated game controller mapping for UI, and added guidance for spatial game controller support in visionOS.

> Resumen de Apple: Precise, intuitive game controls enhance gameplay and can increase a player’s immersion in the game.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- On Apple platforms, a game can support input from physical game controllers or default system interactions, like touch, a remote, or a mouse and keyboard.
  - Even though all platforms except watchOS support physical game controllers, not every player might have access to one.
  - Players appreciate games that let them use the platform interaction method they’re most familiar with.
- To reach the widest audience and provide the best experience for each platform, keep these factors in mind when choosing the input methods to support.

### Touch controls

- For iOS and iPadOS games, supporting touch interaction means that you can provide virtual controls on top of game content while also letting players interact with game elements…
- **Determine whether it makes sense to display virtual controls on top of game content.**
- **Place virtual buttons where they’re easy to access.**
- **Make sure controls are large enough.**
  - «Make sure frequently used controls are a minimum size of 44x44 pt, and less important controls, such as menus, are a minimum size of 28x28 pt to accommodate people’s fingers.»
- **Always include visible and tactile press states.**
- **Use symbols that communicate the actions they perform.**
- **Show and hide virtual controls to reflect gameplay.**
- **Combine functionality into a single control.**
- **Map movement and camera controls to predictable behavior.**

### Physical controllers

- **Support the platform’s default interaction method.**
- **Tell people about game controller requirements.**
- **Automatically detect whether a controller is paired.**
- **Customize onscreen content to match the connected game controller.**
- **Map controller buttons to expected UI behavior.**

| Button | Expected behavior for UI |
|---|---|
| A | Activates a control |
| B | Cancels an action or returns to previous screen |
| X | — |
| Y | — |
| Left shoulder | Navigates left to a different screen or section |
| Right shoulder | Navigates right to a different screen or section |
| Left trigger | — |
| Right trigger | — |
| Left/right thumbstick | Moves selection |
| Directional pad | Moves selection |
| Home/logo | Reserved for system controls |
| Menu | Opens game settings or pauses gameplay |

- **Support multiple connected controllers.**
- **Prefer using symbols, not text, to refer to game controller elements.**

### Keyboards

- Keyboard players appreciate using keyboard bindings to speed up their interactions with apps and games.
- **Prioritize single-key commands.**
- **Test key binding comfort game using an Apple keyboard.**
- **Take the proximity of keys into account.**
- **Let players customize key bindings.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, or tvOS.

#### visionOS

- **Match spatial game controller behavior to hand input.**

## Recursos relacionados

- *Related:*
  - [Designing for games](https://developer.apple.com/design/human-interface-guidelines/designing-for-games)
  - [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures)
  - [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards)
  - [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics)
- *Developer documentation:*
  - [Create games for Apple platforms](https://developer.apple.com/games/)
  - [Touch Controller](https://developer.apple.com/documentation/touchcontroller)
  - [Game Controller](https://developer.apple.com/documentation/gamecontroller)

## Vídeos que la explican

- [Make your game great with touch](https://developer.apple.com/videos/play/wwdc2026/358) → `references/videos/2026-358.md`
- [Design advanced games for Apple platforms](https://developer.apple.com/videos/play/wwdc2024/10085) → `references/videos/2024-10085.md`
- [Explore game input in visionOS](https://developer.apple.com/videos/play/wwdc2024/10094) → `references/videos/2024-10094.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 9, 2025 | Updated touch control best practices, updated game controller mapping for UI, and added guidance for spatial game controller support in visionOS. |
| June 10, 2024 | Added guidance for supporting touch controls and changed title from Game controllers. |
