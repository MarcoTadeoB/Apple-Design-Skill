# Modality — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/modality
- Descargado: 2026-10-15
- Sección: patterns
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2023-12-05 — Enhanced guidance for in-depth modal experiences and clarified guidance on multiple modal views.

> Resumen de Apple: Modality is a design technique that presents content in a separate, dedicated mode that prevents interaction with the parent view and requires an explicit action to dismiss.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Presenting content modally can:
  - Ensure that people receive critical information and, if necessary, act on it
  - Provide options that let people confirm or modify their most recent action
  - Help people perform a distinct, narrowly scoped task without losing track of their previous context
  - Give people an immersive experience or help them concentrate on a complex task
- Depending on the platform, you might use different components to present these types of modal experiences.
- To provide a temporary experience, like viewing media, or to help people perform a distinct, multistep task, like editing content, apps can offer a full-screen modal experience.

### Best practices

- **Present content modally only when there’s a clear benefit.**
- **Aim to keep modal tasks simple, short, and streamlined.**
- **Take care to avoid creating a modal experience that feels like an app within your app.**
- **Consider using a full-screen modal style for in-depth content or a complex task.**
- **Always give people an obvious way to dismiss a modal view.**
- **When necessary, help people avoid data loss by getting confirmation before closing a modal view.**
- **Make it easy to identify a modal view’s task.**
- **Let people dismiss a modal view before presenting another one.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Recursos relacionados

- *Related:*
  - [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets)
  - [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts)
  - [Popovers](https://developer.apple.com/design/human-interface-guidelines/popovers)
  - [Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets)
  - [Activity views](https://developer.apple.com/design/human-interface-guidelines/activity-views)
- *Developer documentation:*
  - [Presentation modifiers](https://developer.apple.com/documentation/swiftui/view-presentation) — SwiftUI
  - [UIModalPresentationStyle](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle) — UIKit
  - [Modal Windows and Panels](https://developer.apple.com/documentation/appkit/modal-windows-and-panels) — AppKit

## Vídeos que la explican

- [Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356) → `references/videos/2025-356.md`

## Registro de cambios

| Date | Changes |
|---|---|
| December 5, 2023 | Enhanced guidance for in-depth modal experiences and clarified guidance on multiple modal views. |
| June 21, 2023 | Updated to include guidance for visionOS. |
