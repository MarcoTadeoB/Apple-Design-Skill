# Always On — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/always-on
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,watchos
- Última actualización: 2023-09-12 — Updated intro image artwork.

> Resumen de Apple: On devices that include the Always On display, the system can continue to display an app’s interface when people suspend their interactions with the device.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- In the Always On state, a device can continue to give people useful, glanceable information in a low-power, privacy-preserving way by dimming the display and minimizing onscreen…
  - On iPhone 14 Pro and iPhone 14 Pro Max, the system displays Lock Screen items like [Widgets](https://developer.apple.com/design/human-interface-guidelines/widgets) and [Live…
  - When people drop their wrist while wearing Apple Watch, the system dims the watch face, continuing to display the interface of the app as long as it’s either frontmost or running…
- On both devices, the system displays notifications while in Always On, and people can tap the display to exit Always On and resume interactions.

### Best practices

- **Hide sensitive information.**
- **Keep other types of personal information glanceable when it makes sense.**
- **Keep important content legible and dim nonessential content.**
- **Maintain a consistent layout.**
- **Gracefully transition motion to a resting state; don’t stop it instantly.**

### Platform considerations

- *No additional considerations for iOS or watchOS.

## Recursos relacionados

- *Related:*
  - [Designing for watchOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos)
- *Developer documentation:*
  - [Designing your app for the Always On state](https://developer.apple.com/documentation/watchos-apps/designing-your-app-for-the-always-on-state) — watchOS apps

## Vídeos que la explican

- [What's new in watchOS 8](https://developer.apple.com/videos/play/wwdc2021/10002) → `references/videos/2021-10002.md`
- [Build a workout app for Apple Watch](https://developer.apple.com/videos/play/wwdc2021/10009) → `references/videos/2021-10009.md`
- [What's new in SwiftUI](https://developer.apple.com/videos/play/wwdc2021/10018) → `references/videos/2021-10018.md`

## Registro de cambios

| Date | Changes |
|---|---|
| September 12, 2023 | Updated intro image artwork. |
| September 23, 2022 | Expanded guidance to cover the Always On display on iPhone 14 Pro and iPhone 14 Pro Max. |
