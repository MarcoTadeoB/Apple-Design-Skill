# Action button — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/action-button
- Descargado: 2026-10-15
- Sección: inputs
- Plataformas: ios,watchos
- Última actualización: 2023-09-12 — Updated to include guidance for iOS.

> Resumen de Apple: The Action button gives people quick access to their favorite features on supported iPhone and Apple Watch models.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- On a supported device, people can use the Action button to run [App Shortcuts](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts) or access…
- A person chooses a function for the Action button when they set up their device; later, they can adjust this choice in Settings.
- When designing your app or game, think of the Action button as another way for someone to quickly access a function that they use on a regular basis.

### Best practices

- **Support the Action button with a set of your app’s essential functions.**
- **For each action you support, write a short label that succinctly describes it.**
- **Prefer letting the system show people how to use the Action button with your app.**

### Platform considerations

- *Not supported in iPadOS, macOS, tvOS, or visionOS.*

#### iOS

- **Let people use your actions without leaving their current context.**

#### watchOS

- In watchOS, a person can assign the Action button’s first press to drop a waypoint, start a dive, or begin a specific workout.
- **Consider offering a secondary function that supports or advances the primary action people choose.**
- **Prefer using subsequent button presses to support additional functionality rather than to stop or conclude a function.**
- **Pause the current function when people press the Action button and side button together.**
  - «The exception is in a diving app where pausing a dive may be dangerous to the diver, causing them to lose track of their depth or not understand how long they’ve been underwater.»
  - «Unless pausing the current function results in a negative experience, be sure to meet people’s expectations by letting them pause their current activity when they press both buttons at the same time.»

## Recursos relacionados

- *Related:*
  - [Workouts](https://developer.apple.com/design/human-interface-guidelines/workouts)
  - [Digital Crown](https://developer.apple.com/design/human-interface-guidelines/digital-crown)
  - [App Shortcuts](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts)
  - [Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities)

## Registro de cambios

| Date | Changes |
|---|---|
| September 12, 2023 | Updated to include guidance for iOS. |
| September 14, 2022 | New page. |
