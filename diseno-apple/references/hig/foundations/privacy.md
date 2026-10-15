# Privacy — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/privacy
- Descargado: 2026-10-15
- Sección: foundations
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2023-06-21 — Consolidated guidance into new page and updated for visionOS.

> Resumen de Apple: Privacy is paramount: it’s critical to be transparent about the privacy-related data and resources you require and essential to protect the data people allow you to access.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- People use their devices in very personal ways and they expect apps to help them preserve their privacy.
- When you submit a new or updated app, you must provide details about your privacy practices and the privacy-relevant data you collect so the App Store can display the information…

### Best practices

- **Request access only to data that you actually need.**
- **Be transparent about how your app collects and uses people’s data.**
- **Process data on the device where possible.**
- **Adopt system-defined privacy protections and follow security best practices.**

### Requesting permission

- Here are several examples of the things you must request permission to access:
  - Personal data, including location, health, financial, contact, and other personally identifying information
  - User-generated content like emails, messages, calendar data, contacts, gameplay information, Apple Music activity, HomeKit data, and audio, video, and photo content
  - Protected resources like Bluetooth peripherals, home automation features, Wi-Fi connections, and local networks
  - Device capabilities like camera and microphone
  - In a visionOS app running in a Full Space, ARKit data, such as hand tracking, plane estimation, image anchoring, and world tracking
  - The device’s advertising identifier, which supports app tracking
- The system provides a standard alert that lets people view each request you make.
- **Request permission only when your app clearly needs access to the data or resource.**
- **Avoid requesting permission at launch unless the data or resource is required for your app to function.**
- **Write copy that clearly describes how your app uses the ability, data, or resource you’re requesting.**

|  | Example purpose string | Notes |
|---|---|---|
| ✅ (correcto) | The app records during the night to detect snoring sounds. | An active sentence that clearly describes how and why the app collects the data. |
| ❌ (incorrecto) | Microphone access is needed for a better experience. | A passive sentence that provides a vague, undefined justification. |
| ❌ (incorrecto) | Turn on microphone access. | An imperative sentence that doesn’t provide any justification. |

- Here are several examples of the standard system alert:

#### Pre-alert screens, windows, or views

- Ideally, the current context helps people understand why you’re requesting their permission.
- **Include only one button and make it clear that it opens the system alert.**
  - ✅ Ejemplo correcto: A screenshot of an app's pre-alert screen that reads Turning on location services allows us to provide features like: alerts when your friends are nearby, news of events happening near you, tagging…
- **Don’t include additional actions in your custom screen or window, unless needed to obtain a legal consent.**
  - ❌ Ejemplo incorrecto: A screenshot of an app’s pre-alert screen that includes a button titled Cancel that appears below the Next button.
  - ❌ Ejemplo incorrecto: A screenshot of an app’s pre-alert screen that includes a Close button in the top-left corner. The Next button appears near the bottom of the screen.

#### Tracking requests

- App tracking is a sensitive issue.
- **Never precede the system-provided alert with a custom screen or window that could confuse or mislead people.**
- There are several prohibited custom-screen designs that will cause rejection.

**Pestaña «Incentive»**

- ❌ (incorrecto)

**Pestaña «Imitation request»**

- ❌ (incorrecto)

**Pestaña «Alert image»**

- ❌ (incorrecto)

**Pestaña «Alert annotation»**

- ❌ (incorrecto)

### Location button

- In iOS, iPadOS, and watchOS, Core Location provides a button so people can grant your app temporary authorization to access their location at the moment a task needs it.
- The first time people open your app and tap a location button, the system displays a standard alert.
- After people confirm their understanding of the button’s action, simply tapping the location button gives your app one-time permission to access their location.
> **Note:** If your app has no authorization status, tapping the location button has the same effect as when a person chooses *Allow Once* in the standard alert.
- **Consider using the location button to give people a lightweight way to share their location for specific app features.**
- **Consider customizing the location button to harmonize with your UI.**
  - Choose the system-provided title that works best with your feature, such as “Current Location” or “Share My Current Location.”
  - Choose the filled or outlined location glyph.
  - Select a background color and a color for the title and glyph.
  - Adjust the button’s corner radius.
- To help people recognize and trust location buttons, you can’t customize the button’s other visual attributes.
> **Important:** If the system identifies consistent problems with your customized location button, it won’t give your app access to the device location when people tap it.

### Protecting data

- Protecting people’s information is paramount.
- Here are some high-level guidelines.
- **Avoid relying solely on passwords for authentication.**
- **Store sensitive information in a keychain.**
- **Never store passwords or other secure content in plain-text files.**
- **Avoid inventing custom authentication schemes.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, tvOS, or watchOS.*

#### macOS

- **Sign your app with a valid Developer ID.**
- **Protect people’s data with app sandboxing.**
- **Avoid making assumptions about who is signed in.**

#### visionOS

- By default, visionOS uses ARKit algorithms to handle features like persistence, world mapping, segmentation, matting, and environment lighting.
- ARKit doesn’t send data to apps in the Shared Space; to access ARKit APIs, your app must open a Full Space.
- In visionOS, user input is private by design.
- Developer access to device cameras works differently in visionOS than it does in other platforms.

## Recursos relacionados

- *Related:*
  - [Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data)
  - [Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding)
- *Developer documentation:*
  - [Requesting access to protected resources](https://developer.apple.com/documentation/uikit/requesting-access-to-protected-resources) — UIKit
  - [Security](https://developer.apple.com/documentation/security)
  - [Requesting authorization to use location services](https://developer.apple.com/documentation/corelocation/requesting-authorization-to-use-location-services) — CoreLocation
  - [App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency)

## Vídeos que la explican

- [Meet Trust Insights](https://developer.apple.com/videos/play/wwdc2026/379) → `references/videos/2026-379.md`
- [Integrate privacy into your development process](https://developer.apple.com/videos/play/wwdc2025/246) → `references/videos/2025-246.md`
- [What’s new in passkeys](https://developer.apple.com/videos/play/wwdc2025/279) → `references/videos/2025-279.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 21, 2023 | Consolidated guidance into new page and updated for visionOS. |
