# VoiceOver — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/voiceover
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2025-03-07 — New page.

> Resumen de Apple: VoiceOver is a screen reader that lets people experience your app’s interface without needing to see the screen.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- By supporting VoiceOver, you help people who are blind or have low vision access information in your app and navigate its interface and content when they can’t see the display.
- VoiceOver is supported in apps and games built for Apple platforms.

### Descriptions

- You inform VoiceOver about your app’s content by providing alternative text that explains your app’s interface and the content it displays.
- **Provide alternative labels for all key interface elements.**
- **Describe meaningful images.**
- **Make charts and other infographics fully accessible.**
- **Exclude purely decorative images from VoiceOver.**

### Navigation

- **Use titles and headings to help people navigate your information hierarchy.**
- **Specify how elements are grouped, ordered, or linked.**
- VoiceOver reads elements in the same order people read content in the their active language and locale.
  - ❌ Ejemplo incorrecto: Ungrouped related elements make it hard for VoiceOver to accurately describe the UI.
  - ✅ Ejemplo correcto: Grouped related elements help VoiceOver accurately describe the UI.
- For developer guidance, see [shouldGroupAccessibilityChildren](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/shouldgroupaccessibilitychildren).
- **Inform VoiceOver when visible content or layout changes occur.**
- **Support the VoiceOver rotor when possible.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS.*

#### visionOS

- **Be mindful that custom gestures aren’t always accessible.**

## Recursos relacionados

- *Related:*
  - [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
  - [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion)
- *Developer documentation:*
  - [Accessibility](https://developer.apple.com/documentation/accessibility)
  - [VoiceOver](https://developer.apple.com/documentation/accessibility/voiceover)
  - [Supporting VoiceOver in your app](https://developer.apple.com/documentation/uikit/supporting-voiceover-in-your-app)

## Vídeos que la explican

- [Writing Great Accessibility Labels](https://developer.apple.com/videos/play/wwdc2019/254) → `references/videos/2019-254.md`
- [Tailor the VoiceOver experience in your data-rich apps](https://developer.apple.com/videos/play/wwdc2021/10121) → `references/videos/2021-10121.md`
- [VoiceOver efficiency with custom rotors](https://developer.apple.com/videos/play/wwdc2020/10116) → `references/videos/2020-10116.md`

## Registro de cambios

| Date | Changes |
|---|---|
| March 7, 2025 | New page. |
