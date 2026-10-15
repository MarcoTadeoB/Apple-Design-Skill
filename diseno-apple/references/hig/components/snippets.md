# Snippets — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/snippets
- Descargado: 2026-10-15
- Sección: components › System experiences
- Plataformas: ios,ipados,macos
- Última actualización: 2026-06-08 — New page.

> Resumen de Apple: When someone performs a task with Siri or an App Shortcut, a snippet shows the result or asks for confirmation.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Snippets are compact views that appear in response to an action that someone takes using [Siri](https://developer.apple.com/design/human-interface-guidelines/siri), Spotlight, or…
- You can present a snippet related to one of your app’s actions by including it with an [app intent](https://developer.apple.com/documentation/appintents) that you design to meet…
- There are two snippet types: confirmation and result.
- For developer guidance, see [Displaying static and interactive snippets](https://developer.apple.com/documentation/appintents/displaying-static-and-interactive-snippets).

### Anatomy

- A snippet consists of the following elements:
  - **Dialogue.** The app intent dialogue that Siri speaks to communicate the snippet’s information.
  - **Custom view.** A view that visually communicates the snippet’s information.
  - **System-provided button(s).** A confirmation snippet includes two system-provided buttons under the custom view: a secondary Cancel button and a primary button with a…
- (imagen) An illustration of a snippet's anatomy. The dialogue appears at the top of the snippet. The custom view appears in the middle, with a maximum height of 400 pt. Two system-provided buttons appear at the bottom: the secondary button on the left and the primary button on the right.

### Best practices

- **Ensure legibility.**
- **Keep content concise.**
- **Choose a descriptive label for a confirmation snippet’s primary button.**
- **Communicate a snippet’s purpose visually.**
  - ❌ Ejemplo incorrecto: An illustration of a result snippet from Calendar that shows details for an upcoming event. The dialogue at the top repeats the information from the custom view, so that the event title, date, time,…
  - ✅ Ejemplo correcto: An illustration of a result snippet from Calendar that shows details for an upcoming event. The snippet omits the dialogue from the top and includes the event title, date, time, and participants in…

### Platform considerations

- *No additional considerations for iOS, iPadOS, or macOS.

## Recursos relacionados

- *Related:*
  - [Siri](https://developer.apple.com/design/human-interface-guidelines/siri)
  - [App Shortcuts](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts)
  - [Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities)
- *Developer documentation:*
  - [App Intents](https://developer.apple.com/documentation/appintents)

## Vídeos que la explican

- [Design interactive snippets](https://developer.apple.com/videos/play/wwdc2025/281) → `references/videos/2025-281.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 8, 2026 | New page. |
