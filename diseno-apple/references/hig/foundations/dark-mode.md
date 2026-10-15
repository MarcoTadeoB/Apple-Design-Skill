# Dark Mode — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/dark-mode
- Descargado: 2026-10-15
- Sección: foundations
- Plataformas: ios,ipados,macos,tvos
- Última actualización: 2024-08-06 — Added art contrasting the light and dark appearances.

> Resumen de Apple: Dark Mode is a systemwide appearance setting that uses a dark color palette to provide a comfortable viewing experience tailored for low-light environments.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- In iOS, iPadOS, macOS, and tvOS, people often choose Dark Mode as their default interface style, and they generally expect all apps and games to respect their preference.

### Best practices

- **Avoid offering an app-specific appearance setting.**
- **Ensure that your app looks good in both appearance modes.**
- **Test your content to make sure that it remains comfortably legible in both appearance modes.**
- **In rare cases, consider using only a dark appearance in the interface.**

### Dark Mode colors

- The color palette in Dark Mode includes dimmer background colors and brighter foreground colors.
- **Embrace colors that adapt to the current appearance.**
- **Aim for sufficient color contrast in all appearances.**
  - «At a minimum, make sure the contrast ratio between colors is no lower than 4.5:1.»
  - «For custom foreground and background colors, strive for a contrast ratio of 7:1, especially in small text.»
- **Soften the color of white backgrounds.**

#### Icons and images

- The system uses [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) (which automatically adapt to Dark Mode) and full-color images that are…
- **Use SF Symbols wherever possible.**
- **Design separate interface icons for the light and dark appearances if necessary.**
- **Make sure full-color images and icons look good in both appearances.**

#### Text

- The system uses vibrancy and increased contrast to maintain the legibility of text on darker backgrounds.
- **Use the system-provided label colors for labels.**
- **Use system views to draw text fields and text views.**

### Platform considerations

- *No additional considerations for tvOS.

#### iOS, iPadOS

- In Dark Mode, the system uses two sets of background colors — called *base* and *elevated* — to enhance the perception of depth when one dark interface is layered above another.
- **Prefer the system background colors.**

#### macOS

- When people choose the graphite accent color in General settings, macOS causes window backgrounds to pick up color from the current desktop picture.
- **Include some transparency in custom component backgrounds when appropriate.**

## Recursos relacionados

- *Related:*
  - [Color](https://developer.apple.com/design/human-interface-guidelines/color)
  - [Materials](https://developer.apple.com/design/human-interface-guidelines/materials)
  - [Typography](https://developer.apple.com/design/human-interface-guidelines/typography)

## Vídeos que la explican

- [Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219) → `references/videos/2025-219.md`
- [Implementing Dark Mode on iOS](https://developer.apple.com/videos/play/wwdc2019/214) → `references/videos/2019-214.md`

## Registro de cambios

| Date | Changes |
|---|---|
| August 6, 2024 | Added art contrasting the light and dark appearances. |
