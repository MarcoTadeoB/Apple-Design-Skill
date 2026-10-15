# Lockups — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/lockups
- Descargado: 2026-10-15
- Sección: components › Layout and organization
- Plataformas: tvos
- Última actualización: sin registro de cambios

> Resumen de Apple: Lockups combine multiple separate views into a single, interactive unit.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Each lockup consists of a content view, a header, and a footer.
- According to the needs of your app, you can combine four types of lockup: cards, caption buttons, monograms, and posters.

### Best practices

- **Allow adequate space between lockups.**
- **Use consistent lockup sizes within a row or group.**
- For developer guidance, see [TVLockupView](https://developer.apple.com/documentation/tvuikit/tvlockupview) and…

### Cards

- A card combines a header, footer, and content view to present ratings and reviews for media items.
- For developer guidance, see [TVCardView](https://developer.apple.com/documentation/tvuikit/tvcardview).

### Caption buttons

- A caption button can include a title and a subtitle beneath the button.
- Make sure that when people focus on them, caption buttons tilt with the motion that they swipe.
- For developer guidance, see [TVCaptionButtonView](https://developer.apple.com/documentation/tvuikit/tvcaptionbuttonview).

### Monograms

- Monograms identify people, usually the cast and crew for a media item.
- **Prefer images over initials.**
- For developer guidance, see [TVMonogramContentView](https://developer.apple.com/documentation/tvuikit/tvmonogramcontentview).

### Posters

- Posters consist of an image and an optional title and subtitle, which are hidden until the poster comes into focus.
- For developer guidance, see [TVPosterView](https://developer.apple.com/documentation/tvuikit/tvposterview).

### Platform considerations

- *Not supported in iOS, iPadOS, macOS, visionOS, or watchOS.*

## Recursos relacionados

- *Related:*
  - [Designing for tvOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos)
  - [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- *Developer documentation:*
  - [TVLockupView](https://developer.apple.com/documentation/tvuikit/tvlockupview) — TVUIKit
  - [TVLockupHeaderFooterView](https://developer.apple.com/documentation/tvuikit/tvlockupheaderfooterview) — TVUIKit
