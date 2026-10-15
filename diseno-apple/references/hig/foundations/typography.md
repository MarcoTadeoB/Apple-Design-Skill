# Typography — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/typography
- Descargado: 2026-10-15
- Sección: foundations
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2025-12-16 — Added emphasized weights to the Dynamic Type style specifications for each platform.

> Resumen de Apple: Your typographic choices can help you display legible text, convey an information hierarchy, communicate important content, and express your brand or style.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
### Ensuring legibility

- **Use font sizes that most people can read easily.**

| Platform | Default size | Minimum size |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

- **Test legibility in different contexts.**
- **In general, avoid light font weights.**

### Conveying hierarchy

- **Adjust font weight, size, and color as needed to emphasize important information and help people visualize hierarchy.**
- **Minimize the number of typefaces you use, even in a highly customized interface.**
- **Prioritize important content when responding to text-size changes.**

### Using system fonts

- Apple provides two typeface families that support an extensive range of weights, sizes, styles, and languages.
- **San Francisco (SF)**
- The system also offers SF Pro, SF Compact, SF Arabic, SF Armenian, SF Georgian, and SF Hebrew in rounded variants you can use to coordinate text with the appearance of soft or…
- **New York (NY)**
- You can download the San Francisco and New York fonts [here](https://developer.apple.com/fonts/).
- The system provides the SF and NY fonts in the *variable* font format, which combines different font styles together in one file, and supports interpolation between styles to…
> **Note:** Variable fonts support *optical sizing*, which refers to the adjustment of different typographic designs to fit different sizes.
- To help you define visual hierarchies and create clear and legible designs in many different sizes and contexts, the system fonts are available in a variety of weights, ranging…
> **Note:** [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) provides a comprehensive library of symbols that integrate seamlessly with the San Francisco system font, automatically aligning with text in all…
- The system defines a set of typographic attributes — called text styles — that work with both typeface families.
- **Consider using the built-in text styles.**
- **Modify the built-in text styles if necessary.**
> **Developer note:** You can use the constants defined in [Font.Design](https://developer.apple.com/documentation/swiftui/font/design) to access all system fonts — don’t embed system fonts in your app or game.
- **If necessary, adjust tracking in interface mockups.**

### Using custom fonts

- **Make sure custom fonts are legible.**
- **Implement accessibility features for custom fonts.**

### Supporting Dynamic Type

- Dynamic Type is a system-level feature in iOS, iPadOS, tvOS, visionOS, and watchOS that lets people adjust the size of visible text on their device to ensure readability and…
- For a list of available Dynamic Type sizes, see [Specifications](https://developer.apple.com/design/human-interface-guidelines/typography#Specifications).
- For developer guidance, see [Text input and output](https://developer.apple.com/documentation/swiftui/text-input-and-output).
- **Make sure your app’s layout adapts to all font sizes.**
- **Increase the size of meaningful interface icons as font size increases.**
- **Keep text truncation to a minimum as font size increases.**
  - «Avoid truncating text in scrollable regions unless people can open a separate view to read the rest of the content.»
- **Consider adjusting your layout at large font sizes.**
- **Maintain a consistent information hierarchy regardless of the current font size.**

### Platform considerations

#### iOS, iPadOS

- SF Pro is the system font in iOS and iPadOS. iOS and iPadOS apps can also use NY.

#### macOS

- SF Pro is the system font in macOS.
- **When necessary, use dynamic system font variants to match the text in standard controls.**

| Dynamic font variant | API |
|---|---|
| Control content | [controlContentFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/controlcontentfont(ofsize:)) |
| Label | [labelFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/labelfont(ofsize:)) |
| Menu | [menuFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/menufont(ofsize:)) |
| Menu bar | [menuBarFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/menubarfont(ofsize:)) |
| Message | [messageFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/messagefont(ofsize:)) |
| Palette | [paletteFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/palettefont(ofsize:)) |
| Title | [titleBarFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/titlebarfont(ofsize:)) |
| Tool tips | [toolTipsFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/tooltipsfont(ofsize:)) |
| Document text (user) | [userFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/userfont(ofsize:)) |
| Monospaced document text (user fixed pitch) | [userFixedPitchFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/userfixedpitchfont(ofsize:)) |
| Bold system font | [boldSystemFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/boldsystemfont(ofsize:)) |
| System font | [systemFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/systemfont(ofsize:)) |

#### tvOS

- SF Pro is the system font in tvOS, and apps can also use NY.

#### visionOS

- SF Pro is the system font in visionOS.
- visionOS uses bolder versions of the Dynamic Type body and title styles and it introduces Extra Large Title 1 and Extra Large Title 2 for wide, editorial-style layouts.
- **In general, prefer 2D text.**
  - ✅ Ejemplo correcto: A screenshot that shows the correct placement of 2D text on a window in visionOS.
  - ❌ Ejemplo incorrecto: A screenshot that shows the incorrect placement of 3D text on a window in visionOS.
- **Make sure text looks good and remains legible when people scale it.**
- **Maximize the contrast between text and the background of its container.**
- **If you need to display text that’s not on a background, consider making it bold to improve legibility.**
- **Keep text facing people as much as possible.**

#### watchOS

- SF Compact is the system font in watchOS, and apps can also use NY.

### Specifications

- You can display emphasized variants of system text styles using symbolic traits.

#### iOS, iPadOS Dynamic Type sizes

**Pestaña «xSmall»**

##### xSmall

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 31 | 38 | Bold |
| Title 1 | Regular | 25 | 31 | Bold |
| Title 2 | Regular | 19 | 24 | Bold |
| Title 3 | Regular | 17 | 22 | Semibold |
| Headline | Semibold | 14 | 19 | Semibold |
| Body | Regular | 14 | 19 | Semibold |
| Callout | Regular | 13 | 18 | Semibold |
| Subhead | Regular | 12 | 16 | Semibold |
| Footnote | Regular | 12 | 16 | Semibold |
| Caption 1 | Regular | 11 | 13 | Semibold |
| Caption 2 | Regular | 11 | 13 | Semibold |

**Pestaña «Small»**

##### Small

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 32 | 39 | Bold |
| Title 1 | Regular | 26 | 32 | Bold |
| Title 2 | Regular | 20 | 25 | Bold |
| Title 3 | Regular | 18 | 23 | Semibold |
| Headline | Semibold | 15 | 20 | Semibold |
| Body | Regular | 15 | 20 | Semibold |
| Callout | Regular | 14 | 19 | Semibold |
| Subhead | Regular | 13 | 18 | Semibold |
| Footnote | Regular | 12 | 16 | Semibold |
| Caption 1 | Regular | 11 | 13 | Semibold |
| Caption 2 | Regular | 11 | 13 | Semibold |

**Pestaña «Medium»**

##### Medium

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 33 | 40 | Bold |
| Title 1 | Regular | 27 | 33 | Bold |
| Title 2 | Regular | 21 | 26 | Bold |
| Title 3 | Regular | 19 | 24 | Semibold |
| Headline | Semibold | 16 | 21 | Semibold |
| Body | Regular | 16 | 21 | Semibold |
| Callout | Regular | 15 | 20 | Semibold |
| Subhead | Regular | 14 | 19 | Semibold |
| Footnote | Regular | 12 | 16 | Semibold |
| Caption 1 | Regular | 11 | 13 | Semibold |
| Caption 2 | Regular | 11 | 13 | Semibold |

**Pestaña «Large (default)»**

##### Large (default)

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 34 | 41 | Bold |
| Title 1 | Regular | 28 | 34 | Bold |
| Title 2 | Regular | 22 | 28 | Bold |
| Title 3 | Regular | 20 | 25 | Semibold |
| Headline | Semibold | 17 | 22 | Semibold |
| Body | Regular | 17 | 22 | Semibold |
| Callout | Regular | 16 | 21 | Semibold |
| Subhead | Regular | 15 | 20 | Semibold |
| Footnote | Regular | 13 | 18 | Semibold |
| Caption 1 | Regular | 12 | 16 | Semibold |
| Caption 2 | Regular | 11 | 13 | Semibold |

**Pestaña «xLarge»**

##### xLarge

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 36 | 43 | Bold |
| Title 1 | Regular | 30 | 37 | Bold |
| Title 2 | Regular | 24 | 30 | Bold |
| Title 3 | Regular | 22 | 28 | Semibold |
| Headline | Semibold | 19 | 24 | Semibold |
| Body | Regular | 19 | 24 | Semibold |
| Callout | Regular | 18 | 23 | Semibold |
| Subhead | Regular | 17 | 22 | Semibold |
| Footnote | Regular | 15 | 20 | Semibold |
| Caption 1 | Regular | 14 | 19 | Semibold |
| Caption 2 | Regular | 13 | 18 | Semibold |

**Pestaña «xxLarge»**

##### xxLarge

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 38 | 46 | Bold |
| Title 1 | Regular | 32 | 39 | Bold |
| Title 2 | Regular | 26 | 32 | Bold |
| Title 3 | Regular | 24 | 30 | Semibold |
| Headline | Semibold | 21 | 26 | Semibold |
| Body | Regular | 21 | 26 | Semibold |
| Callout | Regular | 20 | 25 | Semibold |
| Subhead | Regular | 19 | 24 | Semibold |
| Footnote | Regular | 17 | 22 | Semibold |
| Caption 1 | Regular | 16 | 21 | Semibold |
| Caption 2 | Regular | 15 | 20 | Semibold |

**Pestaña «xxxLarge»**

##### xxxLarge

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 40 | 48 | Bold |
| Title 1 | Regular | 34 | 41 | Bold |
| Title 2 | Regular | 28 | 34 | Bold |
| Title 3 | Regular | 26 | 32 | Semibold |
| Headline | Semibold | 23 | 29 | Semibold |
| Body | Regular | 23 | 29 | Semibold |
| Callout | Regular | 22 | 28 | Semibold |
| Subhead | Regular | 21 | 28 | Semibold |
| Footnote | Regular | 19 | 24 | Semibold |
| Caption 1 | Regular | 18 | 23 | Semibold |
| Caption 2 | Regular | 17 | 22 | Semibold |

#### iOS, iPadOS larger accessibility type sizes

**Pestaña «AX1»**

##### AX1

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 44 | 52 | Bold |
| Title 1 | Regular | 38 | 46 | Bold |
| Title 2 | Regular | 34 | 41 | Bold |
| Title 3 | Regular | 31 | 38 | Semibold |
| Headline | Semibold | 28 | 34 | Semibold |
| Body | Regular | 28 | 34 | Semibold |
| Callout | Regular | 26 | 32 | Semibold |
| Subhead | Regular | 25 | 31 | Semibold |
| Footnote | Regular | 23 | 29 | Semibold |
| Caption 1 | Regular | 22 | 28 | Semibold |
| Caption 2 | Regular | 20 | 25 | Semibold |

**Pestaña «AX2»**

##### AX2

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 48 | 57 | Bold |
| Title 1 | Regular | 43 | 51 | Bold |
| Title 2 | Regular | 39 | 47 | Bold |
| Title 3 | Regular | 37 | 44 | Semibold |
| Headline | Semibold | 33 | 40 | Semibold |
| Body | Regular | 33 | 40 | Semibold |
| Callout | Regular | 32 | 39 | Semibold |
| Subhead | Regular | 30 | 37 | Semibold |
| Footnote | Regular | 27 | 33 | Semibold |
| Caption 1 | Regular | 26 | 32 | Semibold |
| Caption 2 | Regular | 24 | 30 | Semibold |

**Pestaña «AX3»**

##### AX3

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 52 | 61 | Bold |
| Title 1 | Regular | 48 | 57 | Bold |
| Title 2 | Regular | 44 | 52 | Bold |
| Title 3 | Regular | 43 | 51 | Semibold |
| Headline | Semibold | 40 | 48 | Semibold |
| Body | Regular | 40 | 48 | Semibold |
| Callout | Regular | 38 | 46 | Semibold |
| Subhead | Regular | 36 | 43 | Semibold |
| Footnote | Regular | 33 | 40 | Semibold |
| Caption 1 | Regular | 32 | 39 | Semibold |
| Caption 2 | Regular | 29 | 35 | Semibold |

**Pestaña «AX4»**

##### AX4

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 56 | 66 | Bold |
| Title 1 | Regular | 53 | 62 | Bold |
| Title 2 | Regular | 50 | 59 | Bold |
| Title 3 | Regular | 49 | 58 | Semibold |
| Headline | Semibold | 47 | 56 | Semibold |
| Body | Regular | 47 | 56 | Semibold |
| Callout | Regular | 44 | 52 | Semibold |
| Subhead | Regular | 42 | 50 | Semibold |
| Footnote | Regular | 38 | 46 | Semibold |
| Caption 1 | Regular | 37 | 44 | Semibold |
| Caption 2 | Regular | 34 | 41 | Semibold |

**Pestaña «AX5»**

##### AX5

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 60 | 70 | Bold |
| Title 1 | Regular | 58 | 68 | Bold |
| Title 2 | Regular | 56 | 66 | Bold |
| Title 3 | Regular | 55 | 65 | Semibold |
| Headline | Semibold | 53 | 62 | Semibold |
| Body | Regular | 53 | 62 | Semibold |
| Callout | Regular | 51 | 60 | Semibold |
| Subhead | Regular | 49 | 58 | Semibold |
| Footnote | Regular | 44 | 52 | Semibold |
| Caption 1 | Regular | 43 | 51 | Semibold |
| Caption 2 | Regular | 40 | 48 | Semibold |

#### macOS built-in text styles

| Text style | Weight | Size (points) | Line height (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 26 | 32 | Bold |
| Title 1 | Regular | 22 | 26 | Bold |
| Title 2 | Regular | 17 | 22 | Bold |
| Title 3 | Regular | 15 | 20 | Semibold |
| Headline | Bold | 13 | 16 | Heavy |
| Body | Regular | 13 | 16 | Semibold |
| Callout | Regular | 12 | 15 | Semibold |
| Subheadline | Regular | 11 | 14 | Semibold |
| Footnote | Regular | 10 | 13 | Semibold |
| Caption 1 | Regular | 10 | 13 | Medium |
| Caption 2 | Medium | 10 | 13 | Semibold |

#### tvOS built-in text styles

| Text style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Title 1 | Medium | 76 | 96 | Bold |
| Title 2 | Medium | 57 | 66 | Bold |
| Title 3 | Medium | 48 | 56 | Bold |
| Headline | Medium | 38 | 46 | Bold |
| Subtitle 1 | Regular | 38 | 46 | Medium |
| Callout | Medium | 31 | 38 | Bold |
| Body | Medium | 29 | 36 | Bold |
| Caption 1 | Medium | 25 | 32 | Bold |
| Caption 2 | Medium | 23 | 30 | Bold |

#### watchOS Dynamic Type sizes

**Pestaña «xSmall»**

##### xSmall

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 30 | 32.5 | Bold |
| Title 1 | Regular | 28 | 30.5 | Semibold |
| Title 2 | Regular | 24 | 26.5 | Semibold |
| Title 3 | Regular | 17 | 19.5 | Semibold |
| Headline | Semibold | 14 | 16.5 | Semibold |
| Body | Regular | 14 | 16.5 | Semibold |
| Caption 1 | Regular | 13 | 15.5 | Semibold |
| Caption 2 | Regular | 12 | 14.5 | Semibold |
| Footnote 1 | Regular | 11 | 13.5 | Semibold |
| Footnote 2 | Regular | 10 | 12.5 | Semibold |

**Pestaña «Small»**

##### Small (default 38mm)

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 32 | 34.5 | Bold |
| Title 1 | Regular | 30 | 32.5 | Semibold |
| Title 2 | Regular | 26 | 28.5 | Semibold |
| Title 3 | Regular | 18 | 20.5 | Semibold |
| Headline | Semibold | 15 | 17.5 | Semibold |
| Body | Regular | 15 | 17.5 | Semibold |
| Caption 1 | Regular | 14 | 16.5 | Semibold |
| Caption 2 | Regular | 13 | 15.5 | Semibold |
| Footnote 1 | Regular | 12 | 14.5 | Semibold |
| Footnote 2 | Regular | 11 | 13.5 | Semibold |

**Pestaña «Large»**

##### Large (default 40mm/41mm/42mm)

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 36 | 38.5 | Bold |
| Title 1 | Regular | 34 | 36.5 | Semibold |
| Title 2 | Regular | 28 | 30.5 | Semibold |
| Title 3 | Regular | 19 | 21.5 | Semibold |
| Headline | Semibold | 16 | 18.5 | Semibold |
| Body | Regular | 16 | 18.5 | Semibold |
| Caption 1 | Regular | 15 | 17.5 | Semibold |
| Caption 2 | Regular | 14 | 16.5 | Semibold |
| Footnote 1 | Regular | 13 | 15.5 | Semibold |
| Footnote 2 | Regular | 12 | 14.5 | Semibold |

**Pestaña «xLarge»**

##### xLarge (default 44mm/45mm/49mm)

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 40 | 42.5 | Bold |
| Title 1 | Regular | 38 | 40.5 | Semibold |
| Title 2 | Regular | 30 | 32.5 | Semibold |
| Title 3 | Regular | 20 | 22.5 | Semibold |
| Headline | Semibold | 17 | 19.5 | Semibold |
| Body | Regular | 17 | 19.5 | Semibold |
| Caption 1 | Regular | 16 | 18.5 | Semibold |
| Caption 2 | Regular | 15 | 17.5 | Semibold |
| Footnote 1 | Regular | 14 | 16.5 | Semibold |
| Footnote 2 | Regular | 13 | 15.5 | Semibold |

**Pestaña «xxLarge»**

##### xxLarge

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 41 | 43.5 | Bold |
| Title 1 | Regular | 39 | 41.5 | Semibold |
| Title 2 | Regular | 31 | 33.5 | Semibold |
| Title 3 | Regular | 21 | 23.5 | Semibold |
| Headline | Semibold | 18 | 20.5 | Semibold |
| Body | Regular | 18 | 20.5 | Semibold |
| Caption 1 | Regular | 17 | 19.5 | Semibold |
| Caption 2 | Regular | 16 | 18.5 | Semibold |
| Footnote 1 | Regular | 15 | 17.5 | Semibold |
| Footnote 2 | Regular | 14 | 16.5 | Semibold |

**Pestaña «xxxLarge»**

##### xxxLarge

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 42 | 44.5 | Bold |
| Title 1 | Regular | 40 | 42.5 | Semibold |
| Title 2 | Regular | 32 | 34.5 | Semibold |
| Title 3 | Regular | 22 | 24.5 | Semibold |
| Headline | Semibold | 19 | 21.5 | Semibold |
| Body | Regular | 19 | 21.5 | Semibold |
| Caption 1 | Regular | 18 | 20.5 | Semibold |
| Caption 2 | Regular | 17 | 19.5 | Semibold |
| Footnote 1 | Regular | 16 | 18.5 | Semibold |
| Footnote 2 | Regular | 15 | 17.5 | Semibold |

#### watchOS larger accessibility type sizes

**Pestaña «AX1»**

##### AX1

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 44 | 46.5 | Bold |
| Title 1 | Regular | 42 | 44.5 | Semibold |
| Title 2 | Regular | 34 | 41 | Semibold |
| Title 3 | Regular | 24 | 26.5 | Semibold |
| Headline | Semibold | 21 | 23.5 | Semibold |
| Body | Regular | 21 | 23.5 | Semibold |
| Caption 1 | Regular | 18 | 20.5 | Semibold |
| Caption 2 | Regular | 17 | 19.5 | Semibold |
| Footnote 1 | Regular | 16 | 18.5 | Semibold |
| Footnote 2 | Regular | 15 | 17.5 | Semibold |

**Pestaña «AX2»**

##### AX2

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 45 | 47.5 | Bold |
| Title 1 | Regular | 43 | 46 | Semibold |
| Title 2 | Regular | 35 | 37.5 | Semibold |
| Title 3 | Regular | 25 | 27.5 | Semibold |
| Headline | Semibold | 22 | 24.5 | Semibold |
| Body | Regular | 22 | 24.5 | Semibold |
| Caption 1 | Regular | 19 | 21.5 | Semibold |
| Caption 2 | Regular | 18 | 20.5 | Semibold |
| Footnote 1 | Regular | 17 | 19.5 | Semibold |
| Footnote 2 | Regular | 16 | 17.5 | Semibold |

**Pestaña «AX3»**

##### AX3

| Style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 46 | 48.5 | Bold |
| Title 1 | Regular | 44 | 47 | Semibold |
| Title 2 | Regular | 36 | 38.5 | Semibold |
| Title 3 | Regular | 26 | 28.5 | Semibold |
| Headline | Semibold | 23 | 25.5 | Semibold |
| Body | Regular | 23 | 25.5 | Semibold |
| Caption 1 | Regular | 20 | 22.5 | Semibold |
| Caption 2 | Regular | 19 | 21.5 | Semibold |
| Footnote 1 | Regular | 18 | 20.5 | Semibold |
| Footnote 2 | Regular | 17 | 19.5 | Semibold |

#### Tracking values

##### iOS, iPadOS, visionOS tracking values

**Pestaña «SF Pro»**

##### SF Pro

| Size (points) | Tracking (1/1000 em) | Tracking (points) |
|---|---|---|
| 6 | +41 | +0.24 |
| 7 | +34 | +0.23 |
| 8 | +26 | +0.21 |
| 9 | +19 | +0.17 |
| 10 | +12 | +0.12 |
| 11 | +6 | +0.06 |
| 12 | 0 | 0.0 |
| 13 | -6 | -0.08 |
| 14 | -11 | -0.15 |
| 15 | -16 | -0.23 |
| 16 | -20 | -0.31 |
| 17 | -26 | -0.43 |
| 18 | -25 | -0.44 |
| 19 | -24 | -0.45 |
| 20 | -23 | -0.45 |
| 21 | -18 | -0.36 |
| 22 | -12 | -0.26 |
| 23 | -4 | -0.10 |
| 24 | +3 | +0.07 |
| 25 | +6 | +0.15 |
| 26 | +8 | +0.22 |
| 27 | +11 | +0.29 |
| 28 | +14 | +0.38 |
| 29 | +14 | +0.40 |
| 30 | +14 | +0.40 |
| 31 | +13 | +0.39 |
| 32 | +13 | +0.41 |
| 33 | +12 | +0.40 |
| 34 | +12 | +0.40 |
| 35 | +11 | +0.38 |
| 36 | +10 | +0.37 |
| 37 | +10 | +0.36 |
| 38 | +10 | +0.37 |
| 39 | +10 | +0.38 |
| 40 | +10 | +0.37 |
| 41 | +9 | +0.36 |
| 42 | +9 | +0.37 |
| 43 | +9 | +0.38 |
| 44 | +8 | +0.37 |
| 45 | +8 | +0.35 |
| 46 | +8 | +0.36 |
| 47 | +8 | +0.37 |
| 48 | +8 | +0.35 |
| 49 | +7 | +0.33 |
| 50 | +7 | +0.34 |
| 51 | +7 | +0.35 |
| 52 | +6 | +0.33 |
| 53 | +6 | +0.31 |
| 54 | +6 | +0.32 |
| 56 | +6 | +0.30 |
| 58 | +5 | +0.28 |
| 60 | +4 | +0.26 |
| 62 | +4 | +0.24 |
| 64 | +4 | +0.22 |
| 66 | +3 | +0.19 |
| 68 | +2 | +0.17 |
| 70 | +2 | +0.14 |
| 72 | +2 | +0.14 |
| 76 | +1 | +0.07 |
| 80 | 0 | 0 |
| 84 | 0 | 0 |
| 88 | 0 | 0 |
| 92 | 0 | 0 |
| 96 | 0 | 0 |

**Pestaña «SF Pro Rounded»**

##### SF Pro Rounded

| Size (points) | Tracking (1/1000 em) | Tracking (points) |
|---|---|---|
| 6 | +87 | +0.51 |
| 7 | +80 | +0.54 |
| 8 | +72 | +0.57 |
| 9 | +65 | +0.57 |
| 10 | +58 | +0.57 |
| 11 | +52 | +0.56 |
| 12 | +46 | +0.54 |
| 13 | +40 | +0.51 |
| 14 | +35 | +0.48 |
| 15 | +30 | +0.44 |
| 16 | +26 | +0.41 |
| 17 | +22 | +0.37 |
| 18 | +21 | +0.37 |
| 19 | +20 | +0.37 |
| 20 | +18 | +0.36 |
| 21 | +17 | +0.35 |
| 22 | +16 | +0.34 |
| 23 | +16 | +0.35 |
| 24 | +15 | +0.35 |
| 25 | +14 | +0.35 |
| 26 | +14 | +0.36 |
| 27 | +14 | +0.36 |
| 28 | +13 | +0.36 |
| 29 | +13 | +0.37 |
| 30 | +12 | +0.37 |
| 31 | +12 | +0.36 |
| 32 | +12 | +0.38 |
| 33 | +12 | +0.39 |
| 34 | +12 | +0.38 |
| 35 | +11 | +0.38 |
| 36 | +11 | +0.39 |
| 37 | +10 | +0.38 |
| 38 | +10 | +0.39 |
| 39 | +10 | +0.38 |
| 40 | +10 | +0.39 |
| 41 | +10 | +0.38 |
| 42 | +10 | +0.39 |
| 43 | +9 | +0.38 |
| 44 | +8 | +0.37 |
| 45 | +8 | +0.37 |
| 46 | +8 | +0.36 |
| 47 | +8 | +0.37 |
| 48 | +8 | +0.35 |
| 49 | +8 | +0.36 |
| 50 | +7 | +0.34 |
| 51 | +6 | +0.32 |
| 52 | +6 | +0.33 |
| 53 | +6 | +0.31 |
| 54 | +6 | +0.32 |
| 56 | +6 | +0.30 |
| 58 | +4 | +0.25 |
| 60 | +4 | +0.23 |
| 62 | +4 | +0.21 |
| 64 | +3 | +0.19 |
| 66 | +2 | +0.16 |
| 68 | +2 | +0.13 |
| 70 | +2 | +0.14 |
| 72 | +2 | +0.11 |
| 76 | +1 | +0.07 |
| 80 | 0 | 0.00 |
| 84 | 0 | 0.00 |
| 88 | 0 | 0.00 |
| 92 | 0 | 0.00 |
| 96 | 0 | 0.00 |

**Pestaña «New York»**

##### New York

| Size (points) | Tracking (1/1000 em) | Tracking (points) |
|---|---|---|
| 6 | +40 | +0.23 |
| 7 | +32 | +0.22 |
| 8 | +25 | +0.20 |
| 9 | +20 | +0.18 |
| 10 | +16 | +0.15 |
| 11 | +11 | +.12 |
| 12 | +6 | +0.07 |
| 13 | +4 | +0.05 |
| 14 | +2 | +0.03 |
| 15 | +0 | +0.00 |
| 16 | -2 | -0.03 |
| 17 | -4 | -0.07 |
| 18 | -6 | -0.11 |
| 19 | -8 | -0.15 |
| 20 | -10 | -0.20 |
| 21 | -10 | -0.21 |
| 22 | -10 | -0.23 |
| 23 | -11 | -0.25 |
| 24 | -11 | -0.26 |
| 25 | -11 | -0.27 |
| 26 | -12 | -0.29 |
| 27 | -12 | -0.32 |
| 28 | -12 | -0.33 |
| 29 | -12 | -0.34 |
| 30 | -12 | -0.37 |
| 31 | -13 | -0.39 |
| 32 | -13 | -0.41 |
| 33 | -13 | -0.42 |
| 34 | -14 | -0.45 |
| 35 | -14 | -0.48 |
| 36 | -14 | -0.49 |
| 38 | -14 | -0.52 |
| 40 | -14 | -0.55 |
| 42 | -14 | -0.57 |
| 44 | -14 | -0.62 |
| 46 | -14 | -0.65 |
| 48 | -14 | -0.68 |
| 50 | -14 | -0.71 |
| 52 | -14 | -0.74 |
| 54 | -15 | -0.79 |
| 58 | -15 | -0.85 |
| 62 | -15 | -0.91 |
| 66 | -15 | -0.97 |
| 70 | -16 | -1.06 |
| 72 | -16 | -1.09 |
| 80 | -16 | -1.21 |
| 88 | -16 | -1.33 |
| 96 | -16 | -1.50 |
| 100 | -16 | -1.56 |
| 120 | -16 | -1.88 |
| 140 | -16 | -2.26 |
| 160 | -16 | -2.58 |
| 180 | -17 | -2.99 |
| 200 | -17 | -3.32 |
| 220 | -18 | -3.76 |
| 240 | -18 | -4.22 |
| 260 | -18 | -4.57 |

##### macOS tracking values

| Size (points) | Tracking (1/1000 em) | Tracking (points) |
|---|---|---|
| 6 | +41 | +0.24 |
| 7 | +34 | +0.23 |
| 8 | +26 | +0.21 |
| 9 | +19 | +0.17 |
| 10 | +12 | +0.12 |
| 11 | +6 | +0.06 |
| 12 | 0 | 0.0 |
| 13 | -6 | -0.08 |
| 14 | -11 | -0.15 |
| 15 | -16 | -0.23 |
| 16 | -20 | -0.31 |
| 17 | -26 | -0.43 |
| 18 | -25 | -0.44 |
| 19 | -24 | -0.45 |
| 20 | -23 | -0.45 |
| 21 | -18 | -0.36 |
| 22 | -12 | -0.26 |
| 23 | -4 | -0.10 |
| 24 | +3 | +0.07 |
| 25 | +6 | +0.15 |
| 26 | +8 | +0.22 |
| 27 | +11 | +0.29 |
| 28 | +14 | +0.38 |
| 29 | +14 | +0.40 |
| 30 | +14 | +0.40 |
| 31 | +13 | +0.39 |
| 32 | +13 | +0.41 |
| 33 | +12 | +0.40 |
| 34 | +12 | +0.40 |
| 35 | +11 | +0.38 |
| 36 | +10 | +0.37 |
| 37 | +10 | +0.36 |
| 38 | +10 | +0.37 |
| 39 | +10 | +0.38 |
| 40 | +10 | +0.37 |
| 41 | +9 | +0.36 |
| 42 | +9 | +0.37 |
| 43 | +9 | +0.38 |
| 44 | +8 | +0.37 |
| 45 | +8 | +0.35 |
| 46 | +8 | +0.36 |
| 47 | +8 | +0.37 |
| 48 | +8 | +0.35 |
| 49 | +7 | +0.33 |
| 50 | +7 | +0.34 |
| 51 | +7 | +0.35 |
| 52 | +6 | +0.31 |
| 53 | +6 | +0.33 |
| 54 | +6 | +0.32 |
| 56 | +6 | +0.30 |
| 58 | +5 | +0.28 |
| 60 | +4 | +0.26 |
| 62 | +4 | +0.24 |
| 64 | +4 | +0.22 |
| 66 | +3 | +0.19 |
| 68 | +2 | +0.17 |
| 70 | +2 | +0.14 |
| 72 | +2 | +0.14 |
| 76 | +1 | +0.07 |
| 80 | 0 | 0 |
| 84 | 0 | 0 |
| 88 | 0 | 0 |
| 92 | 0 | 0 |
| 96 | 0 | 0 |

##### tvOS tracking values

| Size (points) | Tracking (1/1000 em) | Tracking (points) |
|---|---|---|
| 6 | +41 | +0.24 |
| 7 | +34 | +0.23 |
| 8 | +26 | +0.21 |
| 9 | +19 | +0.17 |
| 10 | +12 | +0.12 |
| 11 | +6 | +0.06 |
| 12 | 0 | 0.0 |
| 13 | -6 | -0.08 |
| 14 | -11 | -0.15 |
| 15 | -16 | -0.23 |
| 16 | -20 | -0.31 |
| 17 | -26 | -0.43 |
| 18 | -25 | -0.44 |
| 19 | -24 | -0.45 |
| 20 | -23 | -0.45 |
| 21 | -18 | -0.36 |
| 22 | -12 | -0.26 |
| 23 | -4 | -0.10 |
| 24 | +3 | +0.07 |
| 25 | +6 | +0.15 |
| 26 | +8 | +0.22 |
| 27 | +11 | +0.29 |
| 28 | +14 | +0.38 |
| 29 | +14 | +0.40 |
| 30 | +14 | +0.40 |
| 31 | +13 | +0.39 |
| 32 | +13 | +0.41 |
| 33 | +12 | +0.40 |
| 34 | +12 | +0.40 |
| 35 | +11 | +0.38 |
| 36 | +10 | +0.37 |
| 37 | +10 | +0.36 |
| 38 | +10 | +0.37 |
| 39 | +10 | +0.38 |
| 40 | +10 | +0.37 |
| 41 | +9 | +0.36 |
| 42 | +9 | +0.37 |
| 43 | +9 | +0.38 |
| 44 | +8 | +0.37 |
| 45 | +8 | +0.35 |
| 46 | +8 | +0.36 |
| 47 | +8 | +0.37 |
| 48 | +8 | +0.35 |
| 49 | +7 | +0.33 |
| 50 | +7 | +0.34 |
| 51 | +7 | +0.35 |
| 52 | +6 | +0.31 |
| 53 | +6 | +0.33 |
| 54 | +6 | +0.32 |
| 56 | +6 | +0.30 |
| 58 | +5 | +0.28 |
| 60 | +4 | +0.26 |
| 62 | +4 | +0.24 |
| 64 | +4 | +0.22 |
| 66 | +3 | +0.19 |
| 68 | +2 | +0.17 |
| 70 | +2 | +0.14 |
| 72 | +2 | +0.14 |
| 76 | +1 | +0.07 |
| 80 | 0 | 0 |
| 84 | 0 | 0 |
| 88 | 0 | 0 |
| 92 | 0 | 0 |
| 96 | 0 | 0 |

##### watchOS tracking values

**Pestaña «SF Compact»**

##### SF Compact

| Size (points) | Tracking (1/1000 em) | Tracking (points) |
|---|---|---|
| 6 | +50 | +0.29 |
| 7 | +30 | +0.21 |
| 8 | +30 | +0.23 |
| 9 | +30 | +0.26 |
| 10 | +30 | +0.29 |
| 11 | +24 | +0.26 |
| 12 | +20 | +0.23 |
| 13 | +16 | +0.20 |
| 14 | +14 | +0.19 |
| 15 | +4 | +0.06 |
| 16 | 0 | 0.00 |
| 17 | -4 | -0.07 |
| 18 | -8 | -0.14 |
| 19 | -12 | -0.22 |
| 20 | 0 | 0.00 |
| 21 | -2 | -0.04 |
| 22 | -4 | -0.09 |
| 23 | -6 | -0.13 |
| 24 | -8 | -0.19 |
| 25 | -10 | -0.24 |
| 26 | -11 | -0.28 |
| 27 | -12 | -0.30 |
| 28 | -12 | -0.34 |
| 29 | -14 | -0.38 |
| 30 | -14 | -0.42 |
| 31 | -15 | -0.45 |
| 32 | -16 | -0.50 |
| 33 | -17 | -0.55 |
| 34 | -18 | -0.60 |
| 35 | -18 | -0.63 |
| 36 | -20 | -0.69 |
| 37 | -20 | -0.72 |
| 38 | -20 | -0.74 |
| 39 | -20 | -0.76 |
| 40 | -20 | -0.78 |
| 41 | -20 | -0.80 |
| 42 | -20 | -0.82 |
| 43 | -20 | -0.84 |
| 44 | -20 | -0.86 |
| 45 | -20 | -0.88 |
| 46 | -20 | -0.92 |
| 47 | -20 | -0.94 |
| 48 | -20 | -0.96 |
| 49 | -21 | -1.00 |
| 50 | -21 | -1.03 |
| 51 | -21 | -1.05 |
| 52 | -21 | -1.07 |
| 53 | -22 | -1.11 |
| 54 | -22 | -1.13 |
| 56 | -22 | -1.20 |
| 58 | -22 | -1.25 |
| 60 | -22 | -1.32 |
| 62 | -22 | -1.36 |
| 64 | -23 | -1.44 |
| 66 | -24 | -1.51 |
| 68 | -24 | -1.56 |
| 70 | -24 | -1.64 |
| 72 | -24 | -1.69 |
| 76 | -25 | -1.86 |
| 80 | -26 | -1.99 |
| 84 | -26 | -2.13 |
| 88 | -26 | -2.28 |
| 92 | -28 | -2.47 |
| 96 | -28 | -2.62 |

**Pestaña «SF Compact Rounded»**

##### SF Compact Rounded

| Size (points) | Tracking (1/1000 em) | Tracking (points) |
|---|---|---|
| 6 | +28 | +0.16 |
| 7 | +26 | +0.18 |
| 8 | +24 | +0.19 |
| 9 | +22 | +0.19 |
| 10 | +20 | +0.20 |
| 11 | +18 | +0.19 |
| 12 | +16 | +0.19 |
| 13 | +14 | +0.18 |
| 14 | +12 | +0.16 |
| 15 | +10 | +0.15 |
| 16 | +8 | +0.12 |
| 17 | +6 | +0.10 |
| 18 | +4 | +0.07 |
| 19 | +2 | +0.04 |
| 20 | 0 | 0.00 |
| 21 | -2 | -0.04 |
| 22 | -4 | -0.09 |
| 23 | -6 | -0.13 |
| 24 | -8 | -0.19 |
| 25 | -10 | -0.24 |
| 26 | -11 | -0.28 |
| 27 | -12 | -0.30 |
| 28 | -12 | -0.34 |
| 29 | -14 | -0.38 |
| 30 | -14 | -0.42 |
| 31 | -15 | -0.45 |
| 32 | -16 | -0.50 |
| 33 | -17 | -0.55 |
| 34 | -18 | -0.60 |
| 35 | -18 | -0.63 |
| 36 | -20 | -0.69 |
| 37 | -20 | -0.72 |
| 38 | -20 | -0.74 |
| 39 | -20 | -0.76 |
| 40 | -20 | -0.78 |
| 41 | -20 | -0.80 |
| 42 | -20 | -0.82 |
| 43 | -20 | -0.84 |
| 44 | -20 | -0.86 |
| 45 | -20 | -0.88 |
| 46 | -20 | -0.92 |
| 47 | -20 | -0.94 |
| 48 | -20 | -0.96 |
| 49 | -21 | -1.00 |
| 50 | -21 | -1.03 |
| 51 | -21 | -1.05 |
| 52 | -21 | -1.07 |
| 53 | -22 | -1.11 |
| 54 | -22 | -1.13 |
| 56 | -22 | -1.20 |
| 58 | -22 | -1.25 |
| 60 | -22 | -1.32 |
| 62 | -22 | -1.36 |
| 64 | -23 | -1.44 |
| 66 | -24 | -1.51 |
| 68 | -24 | -1.56 |
| 70 | -24 | -1.64 |
| 72 | -24 | -1.69 |
| 76 | -25 | -1.86 |
| 80 | -26 | -1.99 |
| 84 | -26 | -2.13 |
| 88 | -26 | -2.28 |
| 92 | -28 | -2.47 |
| 96 | -28 | -2.62 |

## Recursos relacionados

- *Related:*
  - [Fonts for Apple platforms](https://developer.apple.com/fonts/)
  - [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols)
- *Developer documentation:*
  - [Text input and output](https://developer.apple.com/documentation/swiftui/text-input-and-output) — SwiftUI
  - [Text display and fonts](https://developer.apple.com/documentation/uikit/text-display-and-fonts) — UIKit
  - [Fonts](https://developer.apple.com/documentation/appkit/fonts) — AppKit

## Vídeos que la explican

- [Get started with Dynamic Type](https://developer.apple.com/videos/play/wwdc2024/10074) → `references/videos/2024-10074.md`
- [Meet the expanded San Francisco font family](https://developer.apple.com/videos/play/wwdc2022/110381) → `references/videos/2022-110381.md`
- [The details of UI typography](https://developer.apple.com/videos/play/wwdc2020/10175) → `references/videos/2020-10175.md`

## Registro de cambios

| Date | Changes |
|---|---|
| December 16, 2025 | Added emphasized weights to the Dynamic Type style specifications for each platform. |
| March 7, 2025 | Expanded guidance for Dynamic Type. |
| June 10, 2024 | Added guidance for using Apple’s Unity plug-ins to support Dynamic Type in a Unity-based game and enhanced guidance on billboarding in a visionOS app or game. |
| September 12, 2023 | Added artwork illustrating system font weights, and clarified tvOS specification table descriptions. |
| June 21, 2023 | Updated to include guidance for visionOS. |
