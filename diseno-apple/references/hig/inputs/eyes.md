# Eyes — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/eyes
- Descargado: 2026-10-15
- Sección: inputs
- Plataformas: visionos
- Última actualización: 2024-06-10 — Added guidance for custom hover effects.

> Resumen de Apple: In visionOS, people look at a virtual object to identify it as a target they can interact with.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- When people look at an interactive element, visionOS highlights it, providing visual feedback that helps them confirm the item is one they want.
- In some cases, the system can automatically display an expanded view of a component after people look at it.
> **Important:** To help preserve people’s privacy, visionOS doesn’t provide direct information about where people are looking before they tap.
- visionOS also supports *focus effects* that help people navigate apps and the system using a connected input device like a keyboard or game controller.

### Best practices

- **Always give people multiple ways to interact with your app.**
- **Design for visual comfort.**
- **Place content at a comfortable viewing distance.**
  - «In general, you don’t want to place content very close to people unless they’ll view or interact with it for only a little while.»
- **Prefer using standard UI components.**

### Making items easy to see

- **Minimize visual distractions.**
- **Make it easy for people to look at an item by providing enough space around it.**
  - «You can help ensure that there’s enough space between interactive items by using a margin of at least 16 points around the bounds of each item or by placing items so that their centers are always at least 60 points apart.»
- **Avoid using a repeating pattern or texture that fills the field of view.**

### Encouraging interaction

- **Consider using subtle visual cues to encourage people to look at the item they’re most likely to want.**
- **In general, give an interactive item a rounded shape.**
  - ❌ Ejemplo incorrecto: A square button.
  - ✅ Ejemplo correcto: A circular button.
- **If you create an interactive component that consists of more than one element, be sure to provide an overall containing shape that visionOS can highlight.**

### Custom hover effects

- When it makes sense in your app or game, you can design a hover effect that animates in a custom way when people look at an element, including system-provided or custom UI…
- Before you start designing custom hover effects, it’s important to understand how they work.
- As an example that shows what a custom hover effect can and can’t do, consider a photo-browsing app where a photo’s custom effect displays a different symbol depending on whether…
- **Prefer using a custom hover effect to emphasize or enhance a special moment in your experience.**
- **Choose the right delay.**
  - **No delay (default).** A custom hover effect that appears without delay tends to be especially useful when the effect is subtle or invites interaction, like when a knob appears…
  - **Short delay.** Consider using a short delay to let people look at an element and quickly interact with it without waiting for the effect to appear; for example, the expansion…
  - **Long delay.** If your custom hover effect shows additional information, like when a tooltip appears below a button, a slightly longer delay can work well because most people…
- **Aim to keep one or more of the element’s primary views unchanged in both states of a custom hover effect.**
- **Thoroughly test custom hover effects.**

### Platform considerations

- *Not supported in iOS, iPadOS, macOS, tvOS, or watchOS.*

## Recursos relacionados

- *Related:*
  - [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences)
  - [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures)
  - [Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout)
- *Developer documentation:*
  - [Adopting best practices for privacy and user preferences](https://developer.apple.com/documentation/visionos/adopting-best-practices-for-privacy) — visionOS

## Vídeos que la explican

- [Design hover interactions for visionOS](https://developer.apple.com/videos/play/wwdc2025/303) → `references/videos/2025-303.md`
- [Design for spatial input](https://developer.apple.com/videos/play/wwdc2023/10073) → `references/videos/2023-10073.md`
- [Design considerations for vision and motion](https://developer.apple.com/videos/play/wwdc2023/10078) → `references/videos/2023-10078.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 10, 2024 | Added guidance for custom hover effects. |
| March 29, 2024 | Added artwork showing the visionOS hover effect. |
| October 24, 2023 | Clarified the difference between focus effects and the visionOS hover effect. |
| June 21, 2023 | New page. |
