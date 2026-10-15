# Materials — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/materials
- Descargado: 2026-10-15
- Sección: foundations
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2025-09-09 — Updated guidance for Liquid Glass.

> Resumen de Apple: A material is a visual effect that creates a sense of depth, layering, and hierarchy between foreground and background elements.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Materials help visually separate foreground elements, such as text and controls, from background elements, such as content and solid colors.
- Apple platforms feature two types of materials: Liquid Glass, and standard materials. [Liquid…

### Liquid Glass

- Liquid Glass forms a distinct functional layer for controls and navigation elements — like tab bars and sidebars — that floats above the content layer, establishing a clear…
- **Don’t use Liquid Glass in the content layer.**
  - «An exception to this is for controls in the content layer with a transient interactive element like [sliders](https://developer.apple.com/design/human-interface-guidelines/sliders) and…»
- **Use Liquid Glass effects sparingly.**
- **Only use clear Liquid Glass for components that appear over visually rich backgrounds.**
- The *regular* variant blurs and adjusts the luminosity of background content to maintain legibility of text and other foreground elements.
- The *clear* variant is highly translucent, which is ideal for prioritizing the visibility of the underlying content and ensuring visually rich background elements remain prominent.
- For optimal contrast and legibility, determine whether to add a dimming layer behind components with clear Liquid Glass:
  - If the underlying content is bright, consider adding a dark dimming layer of 35% opacity.
  - If the underlying content is sufficiently dark, or if you use standard media playback controls from AVKit that provide their own dimming layer, you don’t need to apply a dimming…
- For guidance about the use of color, see [Liquid Glass color](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color).

### Standard materials

- Use standard materials and effects — such as [blur](https://developer.apple.com/documentation/uikit/uiblureffect),…
- **Choose materials and effects based on semantic meaning and recommended usage.**
- **Help ensure legibility by using vibrant colors on top of materials.**
  - ❌ Ejemplo incorrecto: Poor contrast between the material and `systemGray3` label
  - ✅ Ejemplo correcto: Good contrast between the material and vibrant color label
- **Consider contrast and visual separation when choosing a material to combine with blur and vibrancy effects.**
  - Thicker materials, which are more opaque, can provide better contrast for text and other elements with fine features.
  - Thinner materials, which are more translucent, can help people retain their context by providing a visible reminder of the content that’s in the background.
- For developer guidance, see [Material](https://developer.apple.com/documentation/swiftui/material).

### Platform considerations

#### iOS, iPadOS

- In addition to Liquid Glass, iOS and iPadOS continue to provide four standard materials — ultra-thin, thin, regular (default), and thick — which you can use in the content layer…
- iOS and iPadOS also define vibrant colors for labels, fills, and separators that are specifically designed to work with each material.
- Except for quaternary, you can use the following vibrancy values for labels on any material.
  - [UIVibrancyEffectStyle.label](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/label) (default)
  - [UIVibrancyEffectStyle.secondaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/secondarylabel)
  - [UIVibrancyEffectStyle.tertiaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/tertiarylabel)
  - [UIVibrancyEffectStyle.quaternaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/quaternarylabel)
- You can use the following vibrancy values for fills on all materials.
  - [UIVibrancyEffectStyle.fill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/fill) (default)
  - [UIVibrancyEffectStyle.secondaryFill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/secondaryfill)
  - [UIVibrancyEffectStyle.tertiaryFill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/tertiaryfill)
- The system provides a single, default vibrancy value for a [separator](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/separator), which works well on all…

#### macOS

- macOS provides several standard materials with designated purposes, and vibrant versions of all [system…
- **Choose when to allow vibrancy in custom views and controls.**
- **Choose a background blending mode that complements your interface design.**

#### tvOS

- In tvOS, Liquid Glass appears throughout navigation elements and system experiences such as Top Shelf and Control Center.
- In addition to Liquid Glass, tvOS continues to provide standard materials, which you can use to help define structure in the content layer.

| Material | Recommended for |
|---|---|
| [ultraThin](https://developer.apple.com/documentation/swiftui/material/ultrathin) | Full-screen views that require a light color scheme |
| [thin](https://developer.apple.com/documentation/swiftui/material/thin) | Overlay views that partially obscure onscreen content and require a light color scheme |
| [regular](https://developer.apple.com/documentation/swiftui/material/regular) | Overlay views that partially obscure onscreen content |
| [thick](https://developer.apple.com/documentation/swiftui/material/thick) | Overlay views that partially obscure onscreen content and require a dark color scheme |

#### visionOS

- In visionOS, windows generally use an unmodifiable system-defined material called *glass* that helps people stay grounded by letting light, the current Environment, virtual…
> **Note:** visionOS doesn’t have a distinct Dark Mode setting.
- **Prefer translucency to opaque colors in windows.**
  - ❌ Ejemplo incorrecto: An illustration of a field of view in visionOS with a window in the center. The window has an opaque background that obstructs its surroundings.
  - ✅ Ejemplo correcto: An illustration of a field of view in visionOS with a window in the center. The window has a translucent material background that allows its surroundings to pass through.
- **If necessary, choose materials that help you create visual separations or indicate interactivity in your app.**
  - The [thin](https://developer.apple.com/documentation/swiftui/material/thin) material brings attention to interactive elements like buttons and selected items.
  - The [regular](https://developer.apple.com/documentation/swiftui/material/regular) material can help you visually separate sections of your app, like a sidebar or a grouped table…
  - The [thick](https://developer.apple.com/documentation/swiftui/material/thick) material lets you create a dark element that remains visually distinct when it’s on top of an area…
- To ensure foreground content remains legible when it displays on top of a material, visionOS applies vibrancy to text, symbols, and fills.
- visionOS defines three vibrancy values that help you communicate a hierarchy of text, symbols, and fills.
  - Use [UIVibrancyEffectStyle.label](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/label) for standard text.
  - Use [UIVibrancyEffectStyle.secondaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/secondarylabel) for descriptive text like footnotes and subtitles.
  - Use [UIVibrancyEffectStyle.tertiaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/tertiarylabel) for inactive elements, and only when text doesn’t…

#### watchOS

- **Use materials to provide context in a full-screen modal view.**

## Recursos relacionados

- *Related:*
  - [Color](https://developer.apple.com/design/human-interface-guidelines/color)
  - [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
  - [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode)
- *Developer documentation:*
  - [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass)
  - [glassEffect(_:in:)](https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)) — SwiftUI
  - [Material](https://developer.apple.com/documentation/swiftui/material) — SwiftUI
  - [UIVisualEffectView](https://developer.apple.com/documentation/uikit/uivisualeffectview) — UIKit
  - [NSVisualEffectView](https://developer.apple.com/documentation/appkit/nsvisualeffectview) — AppKit

## Vídeos que la explican

- [Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219) → `references/videos/2025-219.md`
- [Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356) → `references/videos/2025-356.md`

## Registro de cambios

| Date | Changes |
|---|---|
| September 9, 2025 | Updated guidance for Liquid Glass. |
| June 9, 2025 | Added guidance for Liquid Glass. |
| August 6, 2024 | Added platform-specific art. |
| December 5, 2023 | Updated descriptions of the various material types, and clarified terms related to vibrancy and material thickness. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Added guidance on using materials to provide context and orientation in watchOS apps. |
