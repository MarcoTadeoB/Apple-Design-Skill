# Designing for games — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/designing-for-games
- Descargado: 2026-10-15
- Sección: getting-started
- Plataformas: n/d
- Última actualización: 2025-06-09 — Updated guidance for touch-based controls and Game Center.

> Resumen de Apple: When people play your game on an Apple device, they dive into the world you designed while relying on the platform features they love.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- As you create or adapt a game for Apple platforms, learn how to integrate the fundamental platform characteristics and patterns that help your game feel at home on all Apple…

### Jump into gameplay

- **Let people play as soon as installation completes.**
- **Provide great default settings.**
- **Teach through play.**
- **Defer requests until the right time.**

### Look stunning on every display

- **Make sure text is always legible.**

| Platform | Default text size | Minimum text size |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

- **Make sure buttons are always easy to use.**
  - «For example, buttons in iOS must be at least 44x44 pt to accommodate touch interaction.»

| Platform | Default button size | Minimum button size |
|---|---|---|
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |
| tvOS | 66x66 pt | 56x56 pt |
| visionOS | 60x60 pt | 28x28 pt |
| watchOS | 44x44 pt | 28x28 pt |

- **Prefer resolution-independent textures and graphics.**
- **Integrate device features into your layout.**
- **Make sure in-game menus adapt to different aspect ratios.**
- **Design for the full-screen experience.**

### Enable intuitive interactions

- **Support each platform’s default interaction method.**

| Platform | Default interaction methods | Additional interaction methods |
|---|---|---|
| iOS | Touch | Game controller |
| iPadOS | Touch | Game controller, keyboard, mouse, trackpad, Apple Pencil |
| macOS | Keyboard, mouse, trackpad | Game controller |
| tvOS | Remote | Game controller, keyboard, mouse, trackpad |
| visionOS | Touch | Game controller, keyboard, mouse, trackpad, spatial game controller |
| watchOS | Touch | – |

- **Support physical game controllers, while also giving people alternatives.**
  - «Every platform except watchOS supports physical game controllers.»
- **Offer touch-based game controls that embrace the touchscreen experience on iPhone and iPad.**

### Welcome everyone

- **Prioritize perceivability.**
  - Text sizes
  - Color and effects
  - Motion
  - Interactions
  - Buttons
- **Help players personalize their experience.**
- **Give players the tools they need to represent themselves.**
- **Avoid stereotypes in your stories and characters.**

### Adopt Apple technologies

- **Integrate Game Center to help players discover your game across their devices and connect with their friends.**
- **Let players pick up their game on any of their devices.**
- **Support haptics to help players feel the action.**
- **Use Spatial Audio to immerse players in your game’s soundscape.**
- **Take advantage of Apple technologies to enable unique gameplay mechanics.**

## Recursos relacionados

- *Related:*
  - [Game Center](https://developer.apple.com/design/human-interface-guidelines/game-center)
  - [Game controls](https://developer.apple.com/design/human-interface-guidelines/game-controls)
- *Developer documentation:*
  - [Games Pathway](https://developer.apple.com/games/get-started/)
  - [Create games for Apple platforms](https://developer.apple.com/games/)

## Vídeos que la explican

- [Bringing Cyberpunk 2077 to Mac](https://developer.apple.com/videos/play/wwdc2026/356) → `references/videos/2026-356.md`
- [Design no-code games with Reality Composer Pro 3](https://developer.apple.com/videos/play/wwdc2026/252) → `references/videos/2026-252.md`
- [Level up your games](https://developer.apple.com/videos/play/wwdc2025/209) → `references/videos/2025-209.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 9, 2025 | Updated guidance for touch-based controls and Game Center. |
| June 10, 2024 | New page. |
