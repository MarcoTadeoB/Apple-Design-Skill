# Sheets — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/sheets
- Descargado: 2026-10-15
- Sección: components › Presentation
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2026-03-24 — Updated guidance for button placement.

> Resumen de Apple: A sheet helps people perform a scoped task that’s closely related to their current context.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- A sheet is useful for requesting specific information from people or presenting a simple task that they can complete before returning to the parent view.

### Anatomy

- In macOS, tvOS, visionOS, and watchOS, a sheet is always *modal*.
- In iOS and iPadOS, a sheet can be either modal or *nonmodal*.
- There are several common buttons that help people navigate through and dismiss sheets.
  - The **Cancel** (or Close) button dismisses a sheet without saving any changes. This type of button is common in most sheets.
  - The **Done** button dismisses a sheet after completing a task or explicitly saving changes.
  - The **Back** button lets people navigate to a previous step in a multi-step flow or to a parent view in a hierarchy. It isn’t intended to dismiss a sheet.
- The placement of these buttons varies between platforms; see [Platform…

### Best practices

- **For complex or prolonged user flows, consider alternatives to sheets.**
- **Display only one sheet at a time from the main interface.**
- **Use a nonmodal view when you want to present supplementary items that affect the main task in the parent view.**
- **Provide an alternative to the Done button.**
  - ❌ Ejemplo incorrecto: An illustration of the top half of a sheet on iPhone. A Done button appears in the top-right corner on its own.
  - ✅ Ejemplo correcto: An illustration of the top half of a sheet on iPhone. A Cancel button appears in the top-left corner of the view, and a Done button appears in the top-right corner.
- Avoid showing all three buttons — Cancel, Done, and Back — together.
  - ❌ Ejemplo incorrecto: An illustration of the top half of a sheet on iPhone. A Back button appears in the top-left corner of the view, and Cancel and Done buttons appear together in the top-right corner.

### Platform considerations

- *No additional considerations for tvOS.*

#### iOS, iPadOS

- In iOS and iPadOS, for sheets with a single view, the Cancel button belongs on the leading edge of the top toolbar.
- For sheets with a multi-step flow, the placement of buttons can vary across steps.
- A resizable sheet expands when people scroll its contents or drag the *grabber*, which is a small horizontal indicator that can appear at the top edge of a sheet.
- Sheets automatically support the large detent.
- **In an iPhone app, consider supporting the medium detent to allow progressive disclosure of the sheet’s content.**
- **Include a grabber in a resizable sheet.**
- **Support swiping to dismiss a sheet.**
- **Prefer using the page or form sheet presentation styles in an iPadOS app.**

#### macOS

- In macOS, a sheet is a cardlike view with rounded corners that floats on top of its parent window.
- **Present a sheet in a reasonable default size.**
- **Let people interact with other app windows without first dismissing a sheet.**
- **Use a panel instead of a sheet if people need to repeatedly provide input and observe results.**

#### visionOS

- While a sheet is visible in a visionOS app, it floats in front of its parent window, dimming it, and becoming the target of people’s interactions with the app.
- **Avoid displaying a sheet that emerges from the bottom edge of a window.**
- **Present a sheet in a default size that helps people retain their context.**

#### watchOS

- In watchOS, a sheet is a full-screen view that slides over your app’s current content.
- **Use a sheet only when your modal task requires a custom title or custom content presentation.**
- **Keep sheet interactions brief and occasional.**
- **If you change the default label, prefer using SF Symbols to represent the action.**
  - ❌ Ejemplo incorrecto: A screenshot that shows a top toolbar with a custom Back button at the top of the screen on Apple Watch.
  - ❌ Ejemplo incorrecto: A screenshot that shows a top toolbar with a button with the words Page title at the top of the screen on Apple Watch.
  - ✅ Ejemplo correcto: A screenshot that shows a top toolbar with the default Cancel button at the top of the screen on Apple Watch.

## Recursos relacionados

- *Related:*
  - [Modality](https://developer.apple.com/design/human-interface-guidelines/modality)
  - [Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets)
  - [Popovers](https://developer.apple.com/design/human-interface-guidelines/popovers)
  - [Panels](https://developer.apple.com/design/human-interface-guidelines/panels)
- *Developer documentation:*
  - [sheet(item:onDismiss:content:)](https://developer.apple.com/documentation/swiftui/view/sheet(item:ondismiss:content:)) — SwiftUI
  - [UISheetPresentationController](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller) — UIKit
  - [presentAsSheet(_:)](https://developer.apple.com/documentation/appkit/nsviewcontroller/presentassheet(_:)) — AppKit

## Registro de cambios

| Date | Changes |
|---|---|
| March 24, 2026 | Updated guidance for button placement. |
| March 29, 2024 | Added guidance to use form or page sheet styles in iPadOS apps. |
| December 5, 2023 | Recommended using a split view to offer supplementary items in a visionOS app. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Updated guidance for using sheets in watchOS. |
