# SF Symbols — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/sf-symbols
- Descargado: 2026-10-15
- Sección: foundations
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2025-07-28 — Updated with guidance for Draw animations and gradient rendering in SF Symbols 7.

> Resumen de Apple: SF Symbols provides thousands of consistent, highly configurable symbols that integrate seamlessly with the San Francisco system font, automatically aligning with text in all weights and sizes.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- You can use a symbol to convey an object or concept wherever interface icons can appear, such as in toolbars, tab bars, context menus, and within text.
- Availability of individual symbols and features varies based on the version of the system you’re targeting.
- Visit [SF Symbols](https://developer.apple.com/sf-symbols/) to download the app and browse the full set of symbols.

### Rendering modes

- SF Symbols provides four rendering modes — monochrome, hierarchical, palette, and multicolor — that give you multiple options when applying color to symbols.
- To support the rendering modes, SF Symbols organizes a symbol’s paths into distinct layers.
- Depending on the rendering mode you choose, a symbol can produce various appearances.
- To learn more about supporting rendering modes in custom symbols, see [Custom symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Custom-symbols).
- SF Symbols supports the following rendering modes.
- **Monochrome**
- **Hierarchical**
- **Palette**
- **Multicolor**
- Regardless of rendering mode, using system-provided colors ensures that symbols automatically adapt to accessibility accommodations and appearance modes like vibrancy and Dark…
- **Confirm that a symbol’s rendering mode works well in every context.**

### Gradients

- In SF Symbols 7 and later, gradient rendering generates a smooth linear gradient from a single source color.

### Variable color

- With variable color, you can represent a characteristic that can change over time — like capacity or strength — regardless of rendering mode.
  - «To visually communicate such a change, variable color applies color to different layers of a symbol as a value reaches different thresholds between zero and 100 percent.»
- For example, you could use variable color with the `speaker.wave.3` symbol to communicate three different ranges of sound — plus the state where there’s no sound — by mapping the…
- Sometimes, it can make sense for some of a symbol’s layers to opt out of variable color.
- **Use variable color to communicate change — don’t use it to communicate depth.**

### Weights and scales

- SF Symbols provides symbols in a wide range of weights and scales to help you create adaptable designs.
- Each of the nine symbol weights — from ultralight to black — corresponds to a weight of the San Francisco system font, helping you achieve precise weight matching between symbols…
- Each symbol is also available in three scales: small, medium (the default), and large.
- Specifying a scale lets you adjust a symbol’s emphasis compared to adjacent text, without disrupting the weight matching with text that uses the same point size.

### Design variants

- SF Symbols defines several design variants — such as fill, slash, and enclosed — that can help you communicate precise states and actions while maintaining visual consistency and…
- Outline is the most common variant in SF Symbols.
- In addition to outline and fill, SF Symbols also defines variants that include a slash or enclose a symbol within a shape like a circle, square, or rectangle.
- SF Symbols provides many variants for specific languages and writing systems, including Latin, Arabic, Hebrew, Hindi, Thai, Chinese, Japanese, Korean, Cyrillic, Devanagari, and…
- Symbol variants support a range of design goals.
  - The outline variant works well in toolbars, lists, and other places where you display a symbol alongside text.
  - Symbols that use an enclosing shape — like a square or circle — can improve legibility at small sizes.
  - The solid areas in a fill variant tend to give a symbol more visual emphasis, making it a good choice for iOS tab bars and swipe actions and places where you use an accent color…
- In many cases, the view that displays a symbol determines whether to use outline or fill, so you don’t have to specify a variant.

### Animations

- SF Symbols provides a collection of expressive, configurable animations that enhance your interface and add vitality to your app.
- Animations work on all SF Symbols in the library, in all rendering modes, weights, and scales, and on custom symbols.
- **Appear**
- **Disappear**
- **Bounce**
- **Scale**
- **Pulse**
- **Variable color**
- The arrangement of layers within a symbol determines how variable color behaves during a repeating animation.
- **Replace**
  - Down-up, where the outgoing symbol scales down and the incoming symbol scales up, communicating a change in state.
  - Up-up, where both the outgoing and incoming symbols scale up. This configuration communicates a change in state that includes a sense of forward progression.
  - Off-up, where the outgoing symbol hides immediately and the incoming symbol scales up.
- **Magic Replace**
- **Wiggle**
- **Breathe**
- **Rotate**
- **Draw On / Draw Off**
- **Apply symbol animations judiciously.**
- **Make sure that animations serve a clear purpose in communicating a symbol’s intent.**
- **Use symbol animations to communicate information more efficiently.**
- **Consider your app’s tone when adding animations.**

### Custom symbols

- If you need a symbol that SF Symbols doesn’t provide, you can create your own.
> **Important:** SF Symbols includes copyrighted symbols that depict Apple products and features.
- Using a process called *annotating*, you can assign a specific color — or a specific hierarchical level, such as primary, secondary, or tertiary — to each layer in a custom symbol.
- **Use the template as a guide.**
  - Simple
  - Recognizable
  - Inclusive
  - Directly related to the action or content it represents
- For guidance, see [Icons](https://developer.apple.com/design/human-interface-guidelines/icons).
- **Assign negative side margins to your custom symbol if necessary.**
- **Optimize layers to use animations with custom symbols.**
- **Test animations for custom symbols.**
- **Avoid making custom symbols that include common variants, such as enclosures or badges.**
- **Provide alternative text labels for custom symbols.**
- **Don’t design replicas of Apple products.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Recursos relacionados

- *Related:*
  - [Download SF Symbols](https://developer.apple.com/sf-symbols/)
  - [Typography](https://developer.apple.com/design/human-interface-guidelines/typography)
  - [Icons](https://developer.apple.com/design/human-interface-guidelines/icons)
- *Developer documentation:*
  - [Symbols](https://developer.apple.com/documentation/symbols) — Symbols framework
  - [Configuring and displaying symbol images in your UI](https://developer.apple.com/documentation/uikit/configuring-and-displaying-symbol-images-in-your-ui) — UIKit
  - [Creating custom symbols](https://developer.apple.com/documentation/technologyoverviews/custom-sf-symbols)

## Vídeos que la explican

- [What’s new in SF Symbols 7](https://developer.apple.com/videos/play/wwdc2025/337) → `references/videos/2025-337.md`

## Registro de cambios

| Date | Changes |
|---|---|
| July 28, 2025 | Updated with guidance for Draw animations and gradient rendering in SF Symbols 7. |
| June 10, 2024 | Updated with guidance for new animations and features of SF Symbols 6. |
| June 5, 2023 | Added a new section on animations. Included animation guidance for custom symbols. |
| September 14, 2022 | Added a new section on variable color. Removed instructions on creating custom symbol paths, exporting templates, and layering paths, deferring to developer articles that cover these topics. |
