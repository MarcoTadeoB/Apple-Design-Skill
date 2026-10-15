# Settings — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/settings
- Descargado: 2026-10-15
- Sección: patterns
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2024-06-10 — Reorganized some guidance into new topics and added game-specific examples.

> Resumen de Apple: People expect apps and games to just work, but they also appreciate having ways to customize the experience to fit their needs.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- On all Apple platforms, the system-provided Settings app lets people adjust things like the overall appearance of the system, network connections, account details, accessibility…
- When necessary, you can provide a custom settings area within your app or game to offer general settings that affect your overall experience, like interface style or game-saving…

### Best practices

- **Aim to provide default settings that give the best experience to the largest number of people.**
- **Minimize the number of settings you offer.**
- **Make settings available in ways people expect.**
- **Avoid using settings to ask for setup information you can get in other ways.**
- **Respect people’s systemwide settings and avoid including redundant versions of them in your custom settings area.**

### General settings

- **Put general, infrequently changed settings in your custom settings area.**

### Task-specific options

- **When possible, prefer letting people modify task-specific options without going to your settings area.**
> **Note:** In games, players tend to adjust their approach to a specific task as part of the gameplay, not as a settings option to change.

### System settings

- **Add only the most rarely changed options to the system-provided Settings app.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, tvOS, or visionOS.*

#### macOS

- When people choose the Settings item in your app’s or game’s App menu, your custom settings window opens.
- **Include a settings item in the [App menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#App-menu).**
- **Dim a settings window’s minimize and maximize buttons.**
- **In your settings window, use a noncustomizable toolbar that remains visible and always indicates the active toolbar button.**
- **Update the window’s title to reflect the currently visible pane.**
- **Restore the most recently viewed pane.**

#### watchOS

- In watchOS, apps and games don’t add custom settings to the system-provided Settings app.

## Recursos relacionados

- *Related:*
  - [Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding)
- *Developer documentation:*
  - [Settings](https://developer.apple.com/documentation/swiftui/settings) — SwiftUI
  - [UserDefaults](https://developer.apple.com/documentation/foundation/userdefaults) — Foundation
  - [Preference Panes](https://developer.apple.com/documentation/preferencepanes)

## Registro de cambios

| Date | Changes |
|---|---|
| June 10, 2024 | Reorganized some guidance into new topics and added game-specific examples. |
