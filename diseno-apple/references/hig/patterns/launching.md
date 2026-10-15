# Launching — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/launching
- Descargado: 2026-10-15
- Sección: patterns
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2024-06-10 — Added guidance on displaying a splash screen.

> Resumen de Apple: A streamlined launch experience helps people start using your app or game immediately.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Launching begins when someone opens your app or game, includes an initial download, and ends when the first screen is ready.

### Best practices

- **Launch instantly.**
- **If the platform requires it, provide a launch screen.**
- **If you need a splash screen, consider displaying it at the beginning of your onboarding flow.**
- **Restore the previous state when your app restarts so people can continue where they left off.**

### Launch screens

- *Not applicable for macOS, visionOS, or watchOS.*
- **Downplay the launch experience.**
- **Design a launch screen that’s nearly identical to the first screen of your app or game.**
- **Avoid including text on your launch screen, even if your first screen displays text.**
- **Don’t advertise.**
  - «Avoid creating a screen that looks like a splash screen or an “About” window, and don’t include logos or other branding elements unless they’re a fixed part of your app’s first screen.»

### Platform considerations

- *No additional considerations for macOS or watchOS.*

#### iOS, iPadOS

- **Launch in the appropriate orientation.**

#### tvOS

> **Note:** Unlike the [layered images](https://developer.apple.com/design/human-interface-guidelines/images#Layered-images) throughout much of a tvOS app, the launch screen is static.
- **In a live-viewing app, consider automatically starting playback soon after people start the app.**

#### visionOS

- **Consider launching in the Shared Space even if your app is fully immersive.**

## Recursos relacionados

- *Related:*
  - [Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding)
  - [Loading](https://developer.apple.com/design/human-interface-guidelines/loading)
- *Developer documentation:*
  - [Specifying your app’s launch screen](https://developer.apple.com/documentation/xcode/specifying-your-apps-launch-screen) — Xcode
  - [Responding to the launch of your app](https://developer.apple.com/documentation/uikit/responding-to-the-launch-of-your-app) — UIKit

## Vídeos que la explican

- [Optimizing App Launch](https://developer.apple.com/videos/play/wwdc2019/423) → `references/videos/2019-423.md`
- [Love at First Launch](https://developer.apple.com/videos/play/wwdc2017/816) → `references/videos/2017-816.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 10, 2024 | Added guidance on displaying a splash screen. |
| June 21, 2023 | Updated to include guidance for visionOS. |
