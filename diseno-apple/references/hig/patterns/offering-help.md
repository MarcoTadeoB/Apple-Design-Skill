# Offering help — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/offering-help
- Descargado: 2026-10-15
- Sección: patterns
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2023-12-05 — Included visionOS in guidance for creating tooltips.

> Resumen de Apple: Although the most effective experiences are approachable and intuitive, you can provide contextual help when necessary.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
### Best practices

- **Let your app’s tasks inform the types of help people might need.**
- **Use relevant and consistent language and images in your help content.**
- **Make sure all help content is inclusive.**
- **Avoid bloating your help content by explaining how standard components or patterns work.**
  - «If your experience introduces a unique control or expects people to use an input device in a nonstandard way — such as holding the Siri Remote rotated 90 degrees — orient people quickly, preferring animation or graphics to educate instead…»

### Creating tips

- A tip is a small, transient view that briefly describes how to use a feature in your app.
- **Use the most appropriate tip type for your app’s user interface.**
- **Use tips for simple features.**
- **Make tips short, actionable, and engaging.**
- **Define rules to help ensure your tips reach the intended audience.**
- **If there’s an image or symbol that people associate with the feature, consider including it in the tip, and prefer the filled variant.**
  - ❌ Ejemplo incorrecto: An illustration of a hint-style tip with an unfilled blue star symbol on the leading side.
  - ✅ Ejemplo correcto: An illustration of a hint-style tip with a filled blue star symbol on the leading side.
- If the feature is represented by an image that the tip connects to directly, avoid repeating the same image in both the tip and the UI.
  - ❌ Ejemplo incorrecto: An illustration of an annotation-style tip pointing to a feature depicted by a blue star icon. The tip includes a similar blue star symbol on its leading side.
  - ✅ Ejemplo correcto: An illustration of an annotation-style tip pointing to a feature depicted by a blue star icon. The tip is text-only and omits an accompanying symbol.
- **Use buttons to direct people to information or options.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, tvOS, or watchOS.*

#### macOS, visionOS

- A *tooltip* (called a *help tag* in user documentation) displays a small, transient view that briefly describes how to use a component in the interface.
- **Describe only the control that people indicate interest in.**
- **Explain the action or task the control initiates.**
- **In general, avoid repeating a control’s name in its tooltip.**
- **Be brief.**
  - «As much as possible, limit tooltip content to a maximum of 60 to 75 characters (note that localization often changes the length of text).»
- **Use sentence case.**
  - «If you write complete sentences, omit ending punctuation unless it’s required to be consistent with your app’s style.»
- **Consider offering context-sensitive tooltips.**

## Recursos relacionados

- *Related:*
  - [Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding)
  - [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback)
  - [Writing](https://developer.apple.com/design/human-interface-guidelines/writing)
  - [Help menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Help-menu)
- *Developer documentation:*
  - [TipKit](https://developer.apple.com/documentation/tipkit)
  - [NSHelpManager](https://developer.apple.com/documentation/appkit/nshelpmanager) — AppKit

## Vídeos que la explican

- [Make features discoverable with TipKit](https://developer.apple.com/videos/play/wwdc2023/10229) → `references/videos/2023-10229.md`

## Registro de cambios

| Date | Changes |
|---|---|
| December 5, 2023 | Included visionOS in guidance for creating tooltips. |
| September 12, 2023 | Added guidance for creating tips. |
