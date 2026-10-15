# Digital Crown — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/digital-crown
- Descargado: 2026-10-15
- Sección: inputs
- Plataformas: visionos,watchos
- Última actualización: 2023-12-05 — Added artwork for Apple Vision Pro and Apple Watch, and clarified that visionOS apps don’t receive direct information from the Digital Crown.

> Resumen de Apple: The Digital Crown is an important hardware input for Apple Vision Pro and Apple Watch.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- On both Apple Vision Pro and Apple Watch, people can use the Digital Crown to interact with the system; on Apple Watch, people can also use the Digital Crown to interact with apps.

### Apple Vision Pro

- On Apple Vision Pro, people use the Digital Crown to:
  - Adjust volume
  - Adjust the amount of immersion in a portal, an Environment, or an app or game running in a Full Space (for guidance, see [Immersive…
  - Recenter content so it’s in front of them
  - Open Accessibility settings
  - Exit an app and return to the Home View

### Apple Watch

- As people turn the Digital Crown, it generates information you can use to enhance or facilitate interactions with your app, like scrolling or operating standard or custom controls.
- Starting with watchOS 10, the Digital Crown takes on an elevated role as the primary input for navigation.
- Beyond its use for navigation, turning the Digital Crown generates information you can use to enhance or facilitate interactions with your app, such as inspecting data or…
> **Note:** Apps don’t respond to presses on the Digital Crown because watchOS reserves these interactions for system-provided functionality like revealing the Home Screen.
- Most Apple Watch models provide haptic feedback for the Digital Crown, which gives people a more tactile experience as they scroll through content.
- **Anchor your app’s navigation to the Digital Crown.**
- **Consider using the Digital Crown to inspect data in contexts where navigation isn’t necessary.**
- **Provide visual feedback in response to Digital Crown interactions.**
- **Update your interface to match the speed with which people turn the Digital Crown.**
- **Use the default haptic feedback when it makes sense in your app.**

### Platform considerations

- *Not supported in iOS, iPadOS, macOS, or tvOS.*

## Recursos relacionados

- *Related:*
  - [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback)
  - [Action button](https://developer.apple.com/design/human-interface-guidelines/action-button)
  - [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences)
- *Developer documentation:*
  - [WKCrownDelegate](https://developer.apple.com/documentation/watchkit/wkcrowndelegate) — WatchKit

## Registro de cambios

| Date | Changes |
|---|---|
| December 5, 2023 | Added artwork for Apple Vision Pro and Apple Watch, and clarified that visionOS apps don’t receive direct information from the Digital Crown. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Added guidelines emphasizing the central role of the Digital Crown for navigation. |
