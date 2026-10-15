# Color — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/color
- Descargado: 2026-10-15
- Sección: foundations
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2025-12-16 — Updated guidance for Liquid Glass.

> Resumen de Apple: Judicious use of color can enhance communication, evoke your brand, provide visual continuity, communicate status and feedback, and help people understand information.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- The system defines colors that look good on various backgrounds and appearance modes, and can automatically adapt to vibrancy and accessibility settings.
- You may also want to use custom colors to enhance the visual experience of your app or game and express its unique personality.

### Best practices

- **Avoid using the same color to mean different things.**
- **Make sure all your app’s colors work well in light, dark, and increased contrast contexts.**
- **Test your app’s color scheme under a variety of lighting conditions.**
- **Test your app on different devices.**
- **Consider how artwork and translucency affect nearby colors.**
- **If your app lets people choose colors, prefer system-provided color controls where available.**

### Inclusive color

- **Avoid relying solely on color to differentiate between objects, indicate interactivity, or communicate essential information.**
- **Avoid using colors that make it hard to perceive content in your app.**
- **Consider how the colors you use might be perceived in other countries and cultures.**

### System colors

- **Avoid hard-coding system color values in your app.**
- iOS, iPadOS, macOS, and visionOS also define sets of *dynamic system colors* that match the color schemes of standard UI components and automatically adapt to both light and dark…
- **Avoid redefining the semantic meanings of dynamic system colors.**

### Liquid Glass color

- By default, [Liquid Glass](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass) has no inherent color, and instead takes on colors from the…
- For smaller elements like toolbars and tab bars, the system can adapt Liquid Glass between a light and dark appearance in response to the underlying content.
- **Apply color sparingly to the Liquid Glass material, and to symbols or text on the material.**
  - ❌ Ejemplo incorrecto: A screenshot of the top half of an iPhone app that shows a toolbar with several buttons. All of the buttons in the toolbar use a blue accent color for their Liquid Glass background.
  - ✅ Ejemplo correcto: A screenshot of the top half of an iPhone app that shows a toolbar with several buttons. Only the Done button in the toolbar uses a blue accent color for its Liquid Glass background.
- **Avoid using similar colors in control labels if your app has a colorful background.**
- **Be aware of the placement of color in the content layer.**

### Color management

- A *color space* represents the colors in a *color model* like RGB or CMYK.
- A *color profile* describes the colors in a color space using, for example, mathematical formulas or tables of data that map colors to numerical representations.
- **Apply color profiles to your images.**
- **Use wide color to enhance the visual experience on compatible displays.**
- **Provide color space–specific image and color variations if necessary.**

### Platform considerations

#### iOS, iPadOS

- iOS defines two sets of dynamic background colors — *system* and *grouped* — each of which contains primary, secondary, and tertiary variants that help you convey a hierarchy of…
- With both sets of background colors, you generally use the variants to indicate hierarchy in the following ways:
  - Primary for the overall view
  - Secondary for grouping content or elements within the overall view
  - Tertiary for grouping content or elements within secondary elements
- For foreground content, iOS defines the following dynamic colors:

| Color | Use for… | UIKit API |
|---|---|---|
| Label | A text label that contains primary content. | [label](https://developer.apple.com/documentation/uikit/uicolor/label) |
| Secondary label | A text label that contains secondary content. | [secondaryLabel](https://developer.apple.com/documentation/uikit/uicolor/secondarylabel) |
| Tertiary label | A text label that contains tertiary content. | [tertiaryLabel](https://developer.apple.com/documentation/uikit/uicolor/tertiarylabel) |
| Quaternary label | A text label that contains quaternary content. | [quaternaryLabel](https://developer.apple.com/documentation/uikit/uicolor/quaternarylabel) |
| Placeholder text | Placeholder text in controls or text views. | [placeholderText](https://developer.apple.com/documentation/uikit/uicolor/placeholdertext) |
| Separator | A separator that allows some underlying content to be visible. | [separator](https://developer.apple.com/documentation/uikit/uicolor/separator) |
| Opaque separator | A separator that doesn’t allow any underlying content to be visible. | [opaqueSeparator](https://developer.apple.com/documentation/uikit/uicolor/opaqueseparator) |
| Link | Text that functions as a link. | [link](https://developer.apple.com/documentation/uikit/uicolor/link) |

#### macOS

- macOS defines the following dynamic system colors (you can also view them in the Developer palette of the standard Color panel):

| Color | Use for… | AppKit API |
|---|---|---|
| Alternate selected control text color | The text on a selected surface in a list or table. | [alternateSelectedControlTextColor](https://developer.apple.com/documentation/appkit/nscolor/alternateselectedcontroltextcolor) |
| Alternating content background colors | The backgrounds of alternating rows or columns in a list, table, or collection view. | [alternatingContentBackgroundColors](https://developer.apple.com/documentation/appkit/nscolor/alternatingcontentbackgroundcolors) |
| Control accent | The accent color people select in System Settings. | [controlAccentColor](https://developer.apple.com/documentation/appkit/nscolor/controlaccentcolor) |
| Control background color | The background of a large interface element, such as a browser or table. | [controlBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/controlbackgroundcolor) |
| Control color | The surface of a control. | [controlColor](https://developer.apple.com/documentation/appkit/nscolor/controlcolor) |
| Control text color | The text of a control that is available. | [controlTextColor](https://developer.apple.com/documentation/appkit/nscolor/controltextcolor) |
| Current control tint | The system-defined control tint. | [currentControlTint](https://developer.apple.com/documentation/appkit/nscolor/currentcontroltint) |
| Unavailable control text color | The text of a control that’s unavailable. | [disabledControlTextColor](https://developer.apple.com/documentation/appkit/nscolor/disabledcontroltextcolor) |
| Find highlight color | The color of a find indicator. | [findHighlightColor](https://developer.apple.com/documentation/appkit/nscolor/findhighlightcolor) |
| Grid color | The gridlines of an interface element, such as a table. | [gridColor](https://developer.apple.com/documentation/appkit/nscolor/gridcolor) |
| Header text color | The text of a header cell in a table. | [headerTextColor](https://developer.apple.com/documentation/appkit/nscolor/headertextcolor) |
| Highlight color | The virtual light source onscreen. | [highlightColor](https://developer.apple.com/documentation/appkit/nscolor/highlightcolor) |
| Keyboard focus indicator color | The ring that appears around the currently focused control when using the keyboard for interface navigation. | [keyboardFocusIndicatorColor](https://developer.apple.com/documentation/appkit/nscolor/keyboardfocusindicatorcolor) |
| Label color | The text of a label containing primary content. | [labelColor](https://developer.apple.com/documentation/appkit/nscolor/labelcolor) |
| Link color | A link to other content. | [linkColor](https://developer.apple.com/documentation/appkit/nscolor/linkcolor) |
| Placeholder text color | A placeholder string in a control or text view. | [placeholderTextColor](https://developer.apple.com/documentation/appkit/nscolor/placeholdertextcolor) |
| Quaternary label color | The text of a label of lesser importance than a tertiary label, such as watermark text. | [quaternaryLabelColor](https://developer.apple.com/documentation/appkit/nscolor/quaternarylabelcolor) |
| Secondary label color | The text of a label of lesser importance than a primary label, such as a label used to represent a subheading or additional information. | [secondaryLabelColor](https://developer.apple.com/documentation/appkit/nscolor/secondarylabelcolor) |
| Selected content background color | The background for selected content in a key window or view. | [selectedContentBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/selectedcontentbackgroundcolor) |
| Selected control color | The surface of a selected control. | [selectedControlColor](https://developer.apple.com/documentation/appkit/nscolor/selectedcontrolcolor) |
| Selected control text color | The text of a selected control. | [selectedControlTextColor](https://developer.apple.com/documentation/appkit/nscolor/selectedcontroltextcolor) |
| Selected menu item text color | The text of a selected menu. | [selectedMenuItemTextColor](https://developer.apple.com/documentation/appkit/nscolor/selectedmenuitemtextcolor) |
| Selected text background color | The background of selected text. | [selectedTextBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/selectedtextbackgroundcolor) |
| Selected text color | The color for selected text. | [selectedTextColor](https://developer.apple.com/documentation/appkit/nscolor/selectedtextcolor) |
| Separator color | A separator between different sections of content. | [separatorColor](https://developer.apple.com/documentation/appkit/nscolor/separatorcolor) |
| Shadow color | The virtual shadow cast by a raised object onscreen. | [shadowColor](https://developer.apple.com/documentation/appkit/nscolor/shadowcolor) |
| Tertiary label color | The text of a label of lesser importance than a secondary label. | [tertiaryLabelColor](https://developer.apple.com/documentation/appkit/nscolor/tertiarylabelcolor) |
| Text background color | The background color behind text. | [textBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/textbackgroundcolor) |
| Text color | The text in a document. | [textColor](https://developer.apple.com/documentation/appkit/nscolor/textcolor) |
| Under page background color | The background behind a document’s content. | [underPageBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/underpagebackgroundcolor) |
| Unemphasized selected content background color | The selected content in a non-key window or view. | [unemphasizedSelectedContentBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/unemphasizedselectedcontentbackgroundcolor) |
| Unemphasized selected text background color | A background for selected text in a non-key window or view. | [unemphasizedSelectedTextBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/unemphasizedselectedtextbackgroundcolor) |
| Unemphasized selected text color | Selected text in a non-key window or view. | [unemphasizedSelectedTextColor](https://developer.apple.com/documentation/appkit/nscolor/unemphasizedselectedtextcolor) |
| Window background color | The background of a window. | [windowBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/windowbackgroundcolor) |
| Window frame text color | The text in the window’s title bar area. | [windowFrameTextColor](https://developer.apple.com/documentation/appkit/nscolor/windowframetextcolor) |

##### App accent colors

- Beginning in macOS 11, you can specify an *accent color* to customize the appearance of your app’s buttons, selection highlighting, and sidebar icons.
- If people set their accent color setting to a value other than multicolor, the system applies their chosen color to the relevant items throughout your app, replacing your accent…

#### tvOS

- **Consider choosing a limited color palette that coordinates with your app logo.**
- **Avoid using only color to indicate focus.**

#### visionOS

- **Use color sparingly, especially on glass.**
- **Prefer using color in bold text and large areas.**
- **In a fully immersive experience, help people maintain visual comfort by keeping brightness levels balanced.**

#### watchOS

- **Use background color to support existing content or supply additional information.**
- **Recognize that people might prefer graphic complications to use tinted mode instead of full color.**

### Specifications

#### System colors

| Name | SwiftUI API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
|---|---|---|---|---|---|
| Red | [red](https://developer.apple.com/documentation/swiftui/color/red) | ![R-255,G-56,B-60](https://developer.apple.com/images/com.apple.HIG/colors-unified-red-light@2x.png) | ![R-255,G-66,B-69](https://developer.apple.com/images/com.apple.HIG/colors-unified-red-dark@2x.png) | ![R-233,G-21,B-45](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-red-light@2x.png) | ![R-255,G-97,B-101](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-red-dark@2x.png) |
| Orange | [orange](https://developer.apple.com/documentation/swiftui/color/orange) | ![R-255,G-141,B-40](https://developer.apple.com/images/com.apple.HIG/colors-unified-orange-light@2x.png) | ![R-255,G-146,B-48](https://developer.apple.com/images/com.apple.HIG/colors-unified-orange-dark@2x.png) | ![R-197,G-83,B-0](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-orange-light@2x.png) | ![R-255,G-160,B-86](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-orange-dark@2x.png) |
| Yellow | [yellow](https://developer.apple.com/documentation/swiftui/color/yellow) | ![R-255,G-204,B-0](https://developer.apple.com/images/com.apple.HIG/colors-unified-yellow-light@2x.png) | ![R-255,G-214,B-0](https://developer.apple.com/images/com.apple.HIG/colors-unified-yellow-dark@2x.png) | ![R-161,G-106,B-0](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-yellow-light@2x.png) | ![R-254,G-223,B-67](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-yellow-dark@2x.png) |
| Green | [green](https://developer.apple.com/documentation/swiftui/color/green) | ![R-52,G-199,B-89](https://developer.apple.com/images/com.apple.HIG/colors-unified-green-light@2x.png) | ![R-48,G-209,B-88](https://developer.apple.com/images/com.apple.HIG/colors-unified-green-dark@2x.png) | ![R-0,G-137,B-50](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-green-light@2x.png) | ![R-74,G-217,B-104](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-green-dark@2x.png) |
| Mint | [mint](https://developer.apple.com/documentation/swiftui/color/mint) | ![R-0,G-200,B-179](https://developer.apple.com/images/com.apple.HIG/colors-unified-mint-light@2x.png) | ![R-0,G-218,B-195](https://developer.apple.com/images/com.apple.HIG/colors-unified-mint-dark@2x.png) | ![R-0,G-133,B-117](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-mint-light@2x.png) | ![R-84,G-223,B-203](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-mint-dark@2x.png) |
| Teal | [teal](https://developer.apple.com/documentation/swiftui/color/teal) | ![R-0,G-195,B-208](https://developer.apple.com/images/com.apple.HIG/colors-unified-teal-light@2x.png) | ![R-0,G-210,B-224](https://developer.apple.com/images/com.apple.HIG/colors-unified-teal-dark@2x.png) | ![R-0,G-129,B-152](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-teal-light@2x.png) | ![R-59,G-221,B-236](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-teal-dark@2x.png) |
| Cyan | [cyan](https://developer.apple.com/documentation/swiftui/color/cyan) | ![R-0,G-192,B-232](https://developer.apple.com/images/com.apple.HIG/colors-unified-cyan-light@2x.png) | ![R-60,G-211,B-254](https://developer.apple.com/images/com.apple.HIG/colors-unified-cyan-dark@2x.png) | ![R-0,G-126,B-174](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-cyan-light@2x.png) | ![R-109,G-217,B-255](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-cyan-dark@2x.png) |
| Blue | [blue](https://developer.apple.com/documentation/swiftui/color/blue) | ![R-0,G-136,B-255](https://developer.apple.com/images/com.apple.HIG/colors-unified-blue-light@2x.png) | ![R-0,G-145,B-255](https://developer.apple.com/images/com.apple.HIG/colors-unified-blue-dark@2x.png) | ![R-30,G-110,B-244](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-blue-light@2x.png) | ![R-92,G-184,B-255](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-blue-dark@2x.png) |
| Indigo | [indigo](https://developer.apple.com/documentation/swiftui/color/indigo) | ![R-97,G-85,B-245](https://developer.apple.com/images/com.apple.HIG/colors-unified-indigo-light@2x.png) | ![R-109,G-124,B-255](https://developer.apple.com/images/com.apple.HIG/colors-unified-indigo-dark@2x.png) | ![R-86,G-74,B-222](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-indigo-light@2x.png) | ![R-167,G-170,B-255](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-indigo-dark@2x.png) |
| Purple | [purple](https://developer.apple.com/documentation/swiftui/color/purple) | ![R-203,G-48,B-224](https://developer.apple.com/images/com.apple.HIG/colors-unified-purple-light@2x.png) | ![R-219,G-52,B-242](https://developer.apple.com/images/com.apple.HIG/colors-unified-purple-dark@2x.png) | ![R-176,G-47,B-194](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-purple-light@2x.png) | ![R-234,G-141,B-255](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-purple-dark@2x.png) |
| Pink | [pink](https://developer.apple.com/documentation/swiftui/color/pink) | ![R-255,G-45,B-85](https://developer.apple.com/images/com.apple.HIG/colors-unified-pink-light@2x.png) | ![R-255,G-55,B-95](https://developer.apple.com/images/com.apple.HIG/colors-unified-pink-dark@2x.png) | ![R-231,G-18,B-77](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-pink-light@2x.png) | ![R-255,G-138,B-196](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-pink-dark@2x.png) |
| Brown | [brown](https://developer.apple.com/documentation/swiftui/color/brown) | ![R-172,G-127,B-94](https://developer.apple.com/images/com.apple.HIG/colors-unified-brown-light@2x.png) | ![R-183,G-138,B-102](https://developer.apple.com/images/com.apple.HIG/colors-unified-brown-dark@2x.png) | ![R-149,G-109,B-81](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-brown-light@2x.png) | ![R-219,G-166,B-121](https://developer.apple.com/images/com.apple.HIG/colors-unified-accessible-brown-dark@2x.png) |

- visionOS system colors use the default dark color values.

#### iOS, iPadOS system gray colors

| Name | UIKit API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
|---|---|---|---|---|---|
| Gray | [systemGray](https://developer.apple.com/documentation/uikit/uicolor/systemgray) | ![R-142,G-142,B-147](https://developer.apple.com/images/com.apple.HIG/ios-default-systemgray@2x.png) | ![R-142,G-142,B-147](https://developer.apple.com/images/com.apple.HIG/ios-default-systemgraydark@2x.png) | ![R-108,G-108,B-112](https://developer.apple.com/images/com.apple.HIG/ios-accessible-systemgray@2x.png) | ![R-174,G-174,B-178](https://developer.apple.com/images/com.apple.HIG/ios-accessible-systemgraydark@2x.png) |
| Gray (2) | [systemGray2](https://developer.apple.com/documentation/uikit/uicolor/systemgray2) | ![R-174,G-174,B-178](https://developer.apple.com/images/com.apple.HIG/ios-default-systemgray2@2x.png) | ![R-99,G-99,B-102](https://developer.apple.com/images/com.apple.HIG/ios-default-systemgray2dark@2x.png) | ![R-142,G-142,B-147](https://developer.apple.com/images/com.apple.HIG/ios-accessible-systemgray2@2x.png) | ![R-124,G-124,B-128](https://developer.apple.com/images/com.apple.HIG/ios-accessible-systemgray2dark@2x.png) |
| Gray (3) | [systemGray3](https://developer.apple.com/documentation/uikit/uicolor/systemgray3) | ![R-199,G-199,B-204](https://developer.apple.com/images/com.apple.HIG/ios-default-systemgray3@2x.png) | ![R-72,G-72,B-74](https://developer.apple.com/images/com.apple.HIG/ios-default-systemgray3dark@2x.png) | ![R-174,G-174,B-178](https://developer.apple.com/images/com.apple.HIG/ios-accessible-systemgray3@2x.png) | ![R-84,G-84,B-86](https://developer.apple.com/images/com.apple.HIG/ios-accessible-systemgray3dark@2x.png) |
| Gray (4) | [systemGray4](https://developer.apple.com/documentation/uikit/uicolor/systemgray4) | ![R-209,G-209,B-214](https://developer.apple.com/images/com.apple.HIG/ios-default-systemgray4@2x.png) | ![R-58,G-58,B-60](https://developer.apple.com/images/com.apple.HIG/ios-default-systemgray4dark@2x.png) | ![R-188,G-188,B-192](https://developer.apple.com/images/com.apple.HIG/ios-accessible-systemgray4@2x.png) | ![R-68,G-68,B-70](https://developer.apple.com/images/com.apple.HIG/ios-accessible-systemgray4dark@2x.png) |
| Gray (5) | [systemGray5](https://developer.apple.com/documentation/uikit/uicolor/systemgray5) | ![R-229,G-229,B-234](https://developer.apple.com/images/com.apple.HIG/ios-default-systemgray5@2x.png) | ![R-44,G-44,B-46](https://developer.apple.com/images/com.apple.HIG/ios-default-systemgray5dark@2x.png) | ![R-216,G-216,B-220](https://developer.apple.com/images/com.apple.HIG/ios-accessible-systemgray5@2x.png) | ![R-54,G-54,B-56](https://developer.apple.com/images/com.apple.HIG/ios-accessible-systemgray5dark@2x.png) |
| Gray (6) | [systemGray6](https://developer.apple.com/documentation/uikit/uicolor/systemgray6) | ![R-242,G-242,B-247](https://developer.apple.com/images/com.apple.HIG/ios-default-systemgray6@2x.png) | ![R-28,G-28,B-30](https://developer.apple.com/images/com.apple.HIG/ios-default-systemgray6dark@2x.png) | ![R-235,G-235,B-240](https://developer.apple.com/images/com.apple.HIG/ios-accessible-systemgray6@2x.png) | ![R-36,G-36,B-38](https://developer.apple.com/images/com.apple.HIG/ios-accessible-systemgray6dark@2x.png) |

- In SwiftUI, the equivalent of `systemGray` is [gray](https://developer.apple.com/documentation/swiftui/color/gray).

## Recursos relacionados

- *Related:*
  - [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode)
  - [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
  - [Materials](https://developer.apple.com/design/human-interface-guidelines/materials)
  - [Apple Design Resources](https://developer.apple.com/design/resources/)
- *Developer documentation:*
  - [Color](https://developer.apple.com/documentation/swiftui/color) — SwiftUI
  - [UIColor](https://developer.apple.com/documentation/uikit/uicolor) — UIKit
  - [Color](https://developer.apple.com/documentation/appkit/color) — AppKit

## Vídeos que la explican

- [Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219) → `references/videos/2025-219.md`

## Registro de cambios

| Date | Changes |
|---|---|
| December 16, 2025 | Updated guidance for Liquid Glass. |
| June 9, 2025 | Updated system color values, and added guidance for Liquid Glass. |
| February 2, 2024 | Distinguished UIKit and SwiftUI gray colors in iOS and iPadOS, and added guidance for balancing brightness levels in visionOS apps. |
| September 12, 2023 | Enhanced guidance for using background color in watchOS views, and added color swatches for tvOS. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Updated guidance for using background color in watchOS. |
| December 19, 2022 | Corrected RGB values for system mint color (Dark Mode) in iOS and iPadOS. |
