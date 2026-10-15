# Controls — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/controls
- Descargado: 2026-10-15
- Sección: components › System experiences
- Plataformas: ios,ipados,macos
- Última actualización: 2024-06-10 — New page.

> Resumen de Apple: A control provides quick access to a feature of your app from Control Center, the Lock Screen, or the Action button.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- A control is a button or toggle that provides quick access to your app’s features from other areas of the system.
- People can add controls to Control Center by pressing and holding in an empty area of Control Center, to the Lock Screen by customizing their Lock Screen, and to the Action…

### Anatomy

- Controls contain a symbol image, a title, and, optionally, a value.
- Controls display their information differently depending on where they appear:
  - In Control Center, a control displays its symbol and, at larger sizes, its title and value.
  - On the Lock Screen, a control displays its symbol.
  - On iPhone devices with a control assigned to the Action button, pressing and holding it displays the control’s symbol in the Dynamic Island, as well as its value (if present).

### Best practices

- **Offer controls for actions that provide the most benefit without having to launch your app.**
- **Update controls when someone interacts with them, when an action completes, or remotely with a push notification.**
- **Choose a descriptive symbol that suggests the behavior of the control.**
- **Use symbol animations to highlight state changes.**
- **Select a tint color that works with your app’s brand.**
- **Help people provide additional information the system needs to perform an action.**
- **Provide hint text for the Action button.**
- **If your control title or value can vary, include a placeholder.**
- **Hide sensitive information when the device is locked.**
- **Require authentication for actions that affect security.**

### Camera experiences on a locked device

- If your app supports camera capture, starting with iOS 18 you can create a control that launches directly to your app’s camera experience while the device is locked.
- **Use the same camera UI in your app and your camera experience.**
- **Provide instructions for adding the control.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, or macOS.

## Recursos relacionados

- *Related:*
  - [Widgets](https://developer.apple.com/design/human-interface-guidelines/widgets)
  - [Action button](https://developer.apple.com/design/human-interface-guidelines/action-button)
- *Developer documentation:*
  - [LockedCameraCapture](https://developer.apple.com/documentation/lockedcameracapture)
  - [WidgetKit](https://developer.apple.com/documentation/widgetkit)

## Registro de cambios

| Date | Changes |
|---|---|
| June 10, 2024 | New page. |
