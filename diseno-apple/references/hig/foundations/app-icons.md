# App icons — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/app-icons
- Descargado: 2026-10-15
- Sección: foundations
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2026-06-08 — Refined guidance for Liquid Glass.

> Resumen de Apple: A unique, memorable icon expresses your app’s or game’s purpose and personality and helps people recognize it at a glance.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Your app icon is a crucial aspect of your app’s or game’s branding and user experience.

### Layer design

- Although you can provide a flattened image for your icon, layers give you the most control over how your icon design is represented.
- iOS, iPadOS, macOS, and watchOS app icons include a background layer and one or more foreground layers that coalesce to create dimensionality.
- tvOS app icons use between two and five layers to create a sense of dynamism as people bring them into focus.
- A visionOS app icon includes a background layer and one or two layers on top, producing a three-dimensional object that subtly expands when people view it.
- You use your favorite design tool to craft the individual foreground layers of your app icon.
- For tvOS and visionOS app icons, you add your icon layers directly to an image stack in Xcode to form your complete icon.
- **Prefer clearly defined edges in foreground layers.**
- **Vary opacity in foreground layers to increase the sense of depth and liveliness.**
- **Design a background that both stands out and emphasizes foreground content.**
- **Prefer vector graphics when bringing layers into Icon Composer.**

### Icon shape

- An app icon’s shape varies based on a platform’s visual language.
- **Produce appropriately shaped, unmasked layers.**
- **Keep primary content centered to avoid truncation when the system adjusts corners or applies masking.**

### Design

- Embrace simplicity in your icon design.
- **Provide a visually consistent icon design across all the platforms your app supports.**
- **Consider basing your icon design around filled, overlapping shapes.**
  - ❌ Ejemplo incorrecto: An illustration of two circles centered above a grid. One circle encloses the other. The inner circle has a solid fill. The outer circle is larger than the inner circle, allowing some space between…
  - ✅ Ejemplo correcto: An illustration of two circles centered above a grid. One circle encloses the other. The inner circle has a solid fill. The outer circle is larger than the inner circle, has no outline, and has a…
- **Include text only when it’s essential to your experience or brand.**
- **Prefer illustrations to photos and avoid replicating UI components.**
- **Don’t use replicas of Apple hardware products.**

### Visual effects

- **Let the system handle blurring and other visual effects.**
- **Create layer groupings to apply effects to multiple layers at once.**

### Appearances

- In iOS, iPadOS, and macOS, people can choose whether their Home Screen app icons are default, dark, clear, or tinted in appearance.
- **Keep your icon’s features consistent across appearances.**
- **Design dark and tinted icons that feel at home beside system app icons and widgets.**
- **Use your light app icon as the basis for your dark icon.**
- **Consider offering alternate app icons.**
> **Note:** Alternate app icons in iOS and iPadOS require their own dark, clear, and tinted variants.

### Platform considerations

- *No additional considerations for iOS, iPadOS, or macOS.*

#### tvOS

- **Include a safe zone to ensure the system doesn’t crop your content.**

#### visionOS

- **Avoid adding a shape that’s intended to look like a hole or concave area to the background layer.**

#### watchOS

- **Avoid using black for your icon’s background.**

### Specifications

- The layout, size, style, and appearances of app icons vary by platform.

| Platform | Layout shape | Icon shape after system masking | Layout size | Style | Appearances |
|---|---|---|---|---|---|
| iOS, iPadOS, macOS | Square | Rounded rectangle (square) | 1024x1024 px | Layered | Default, dark, clear light, clear dark, tinted light, tinted dark |
| tvOS | Rectangle (landscape) | Rounded rectangle (rectangular) | 800x480 px | Layered (Parallax) | N/A |
| visionOS | Square | Circular | 1024x1024 px | Layered (3D) | N/A |
| watchOS | Square | Circular | 1088x1088 px | Layered | N/A |

- The system automatically scales your icon to produce smaller variants that appear in certain locations, such as Settings and notifications.
- App icons support the following color spaces:
  - sRGB (color)
  - Gray Gamma 2.2 (grayscale)
  - Display P3 (wide-gamut color in iOS, iPadOS, macOS, tvOS, and watchOS only)

## Recursos relacionados

- *Related:*
  - [Apple Design Resources](https://developer.apple.com/design/resources/)
  - [Icon Composer](https://developer.apple.com/icon-composer/)
  - [Icons](https://developer.apple.com/design/human-interface-guidelines/icons)
  - [Images](https://developer.apple.com/design/human-interface-guidelines/images)
  - [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode)
- *Developer documentation:*
  - [Creating your app icon using Icon Composer](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer)
  - [Configuring your app icon using an asset catalog](https://developer.apple.com/documentation/xcode/configuring-your-app-icon)

## Vídeos que la explican

- [Say hello to the new look of app icons](https://developer.apple.com/videos/play/wwdc2025/220) → `references/videos/2025-220.md`
- [Create icons with Icon Composer](https://developer.apple.com/videos/play/wwdc2025/361) → `references/videos/2025-361.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 8, 2026 | Refined guidance for Liquid Glass. |
| June 9, 2025 | Updated guidance to reflect layered icons, consistency across platforms, and best practices for Liquid Glass. |
| June 10, 2024 | Added guidance for creating dark and tinted app icon variants for iOS and iPadOS. |
| January 31, 2024 | Clarified platform availability for alternate app icons. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | Added specifications for Apple Watch Ultra. |
