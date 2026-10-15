# App Shortcuts — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/app-shortcuts
- Descargado: 2026-10-15
- Sección: components › System experiences
- Plataformas: ios,ipados,visionos,watchos
- Última actualización: 2026-06-08 — Added guidance for adopting app schemas.

> Resumen de Apple: An App Shortcut gives people access to your app’s key functions or content throughout the system.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- People can initiate App Shortcuts using features like Siri, Spotlight, and the Shortcuts app; using hardware features like the [Action…
- Because App Shortcuts are part of your app, they are available immediately when installation finishes.
- App Shortcuts use [App Intents](https://developer.apple.com/documentation/appintents) to define actions within your app to make available to the system.
  - «Each app can include up to 10 App Shortcuts.»
- For developer guidance, see [App Shortcuts](https://developer.apple.com/documentation/appintents/app-shortcuts).
> **Note:** When you use App Intents to make your app’s actions available to the system, in addition to the App Shortcuts that your app provides, people can also make their own custom shortcuts by combining actions in the Shortcuts app.

### Best practices

- **To surface common types of app functionality throughout the system, consider adopting app schemas instead.**
- App Shortcuts are useful for exposing unique features or custom content to the system in areas not covered by app schemas.
- **Offer App Shortcuts for your app’s most common and important tasks.**
- **Add flexibility by letting people choose from a set of options.**
- **Ask for clarification in response to a request that’s missing optional information.**
- **Keep voice interactions simple.**
- **Make App Shortcuts discoverable in your app.**

#### Responding to App Shortcuts

- As a person engages with an App Shortcut, your app can respond in a variety of ways, including with dialogue that Siri speaks aloud and custom visuals like snippets and Live…
  - [Snippets](https://developer.apple.com/design/human-interface-guidelines/snippets) are great for custom views that display static information or dialog options, like showing the…
  - [Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities) offer continuous access to information that’s likely to remain relevant and…
- **Provide enough detail for interaction on audio-only devices.**

### Editorial guidelines

- **Provide brief, memorable activation phrases and natural variants.**
- **When referring to App Shortcuts or the Shortcuts app, always use title case and make sure that *Shortcuts* is plural.**
- **When referring to individual shortcuts (not App Shortcuts or the Shortcuts app), use lowercase.**

### Platform considerations

- *No additional considerations for visionOS or watchOS.

#### iOS, iPadOS

- App Shortcuts can appear in the Top Hit area of Spotlight when people search for your app, or in the Shortcuts area below.
- **Order shortcuts based on importance.**

#### macOS

- App Shortcuts aren’t supported in macOS.

## Recursos relacionados

- *Related:*
  - [Siri](https://developer.apple.com/design/human-interface-guidelines/siri)
  - [Siri Style Guide](https://developer.apple.com/siri/style-guide/)
  - [Shortcuts User Guide](https://support.apple.com/guide/shortcuts/welcome/ios)
- *Developer documentation:*
  - [App Intents](https://developer.apple.com/documentation/appintents)
  - [SiriKit](https://developer.apple.com/documentation/sirikit)
  - [Getting started with the App Intents framework](https://developer.apple.com/documentation/appintents/getting-started-with-the-app-intents-framework) — App Intents
  - [Defining app entities for your custom data types](https://developer.apple.com/documentation/appintents/defining-app-entities-for-your-custom-data-types) — App Intents

## Vídeos que la explican

- [What’s new in Shortcuts](https://developer.apple.com/videos/play/wwdc2026/310) → `references/videos/2026-310.md`
- [Design interactive snippets](https://developer.apple.com/videos/play/wwdc2025/281) → `references/videos/2025-281.md`
- [Get to know App Intents](https://developer.apple.com/videos/play/wwdc2025/244) → `references/videos/2025-244.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 8, 2026 | Added guidance for adopting app schemas. |
| January 17, 2025 | Updated and streamlined guidance. |
| June 5, 2023 | New page. |
