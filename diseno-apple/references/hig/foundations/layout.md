# Layout — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/layout
- Descargado: 2026-10-15
- Sección: foundations
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2026-09-09 — Updated guidance to reflect current best practices.

> Resumen de Apple: A consistent layout that adapts across display sizes, orientations, and multitasking configurations helps people understand and enjoy your app or game on all their devices.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Your layout provides the structure for people to understand your content from the moment they open your app.
- Apple provides templates and layout guides that can help you integrate Apple technologies and design your apps and games to run on all Apple platforms.

### Visual hierarchy

- **Order content by relative importance.**
- **Align elements to make them easier to scan, and use indentation to convey hierarchy.**
- **Group related items to clearly express related information or functions.**
- **Use progressive disclosure to make layouts cleaner and easier to interact with.**
- **Differentiate controls from content.**
- If scaling a background image to the full window edge results in components like sidebars or inspectors covering important parts of the image, you can use a background extension…

### Adaptability

- Apps and games need to adapt to different display sizes, orientation changes, window sizes, and multitasking states.
- Here are some of the most common device and system characteristics that apps need to handle:
  - Regular and compact horizontal and vertical [size classes](https://developer.apple.com/design/human-interface-guidelines/layout#Size-classes)
  - Different device screen sizes
  - Different device orientations and aspect ratios
  - System features like the Dynamic Island
  - External display support, Display Zoom, and resizable windows on iPad and Mac
  - Text-size changes
  - Locale-based internationalization features like left-to-right/right-to-left layout direction, date/time/number formatting, font variation, and text length
- **Design a layout that adapts gracefully and consistently.**
- Even if your app is locked to a certain orientation, such as a landscape-only game, it’s still important to ensure your interface resizes well to provide the best experience…
- **Be prepared for text-size changes.**
- To support Dynamic Type in your Unity-based game, use Apple’s accessibility plug-in (for developer guidance, see [Apple –…
- **Preview your app on multiple devices, using different size classes, localizations, and text sizes.**
- **When necessary, scale background artwork in response to display changes.**

#### Size classes

- In iOS and iPadOS, size classes are an indication of how much horizontal and vertical space is available to an app’s interface.
- Each dimension — horizontal and vertical — is represented by one of two size classes: *compact* or *regular*.
- The system sets size classes based on the device type, [window](https://developer.apple.com/design/human-interface-guidelines/windows) configuration, and…
- For developer guidance, see [UITraitChangeObservable](https://developer.apple.com/documentation/uikit/uitraitchangeobservable-67e94) and…
- **Determine layout based on size classes, not device type or orientation.**
- Size classes also let your app’s interface adapt to a wide range of window sizes.
- **Consider all possible combinations of size classes.**
- **Keep functionality the same as size classes change, and keep layout changes recognizable and familiar to the platform.**
- Similarly, while an app’s size classes might change when someone resizes it, its idiom — the device type it’s made for — remains the same: keep the layout recognizable and…

### Guides and safe areas

- A *layout guide* defines a rectangular region that helps you position, align, and space your content on the screen.
- A *safe area* defines the area within a window that isn’t covered on the edge by a hardware feature or another view within the window, like a toolbar, tab bar, or status bar.

### Platform considerations

- *No additional considerations for iOS or iPadOS.*

#### macOS

- **Avoid placing controls or critical information at the bottom of a window.**
- **Avoid displaying content behind the camera housing at the top edge of the window.**

#### tvOS

- **Adhere to the screen’s safe area.**
  - «Inset primary content 60 points from the top and bottom of the screen, and 80 points from the sides.»
- (imagen) An illustration of a TV with a safe zone border on all sides. In width, the top and bottom borders measure 60 points, and the side borders both measure 80 points.
- **Include appropriate padding between focusable elements.**

##### Grids

- The following grid layouts provide an optimal viewing experience.
- If you use the UIKit collection view flow element, the number of columns in a grid is automatically determined based on the width and spacing of your content.

**Pestaña «Two-column»**

##### Two-column grid

| Attribute | Value |
|---|---|
| Unfocused content width | 860 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Pestaña «Three-column»**

##### Three-column grid

| Attribute | Value |
|---|---|
| Unfocused content width | 560 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Pestaña «Four-column»**

##### Four-column grid

| Attribute | Value |
|---|---|
| Unfocused content width | 410 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Pestaña «Five-column»**

##### Five-column grid

| Attribute | Value |
|---|---|
| Unfocused content width | 320 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Pestaña «Six-column»**

##### Six-column grid

| Attribute | Value |
|---|---|
| Unfocused content width | 260 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Pestaña «Seven-column»**

##### Seven-column grid

| Attribute | Value |
|---|---|
| Unfocused content width | 217 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Pestaña «Eight-column»**

##### Eight-column grid

| Attribute | Value |
|---|---|
| Unfocused content width | 184 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Pestaña «Nine-column»**

##### Nine-column grid

| Attribute | Value |
|---|---|
| Unfocused content width | 160 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

- **Include additional vertical spacing for titled rows.**
- **Use consistent spacing.**
- **Make partially hidden content look symmetrical.**

#### visionOS

- In visionOS, you can lay out content within a window, a bounded 3D volume, or an immersive space.
- **In general, support resizing.**
- You can also choose to set a minimum and maximum size for windows, volumes, and attached UI elements like ornaments.
- **Use 3D content sparingly in windows.**
- To display larger models or views that primarily consist of 3D content, consider using a volume or placing content in an immersive space.
- **Display supplemental content in an adjacent window, not in an ornament.**
- **Include enough space around controls for them to be easy to interact with.**
  - «For example, place buttons so their centers are at least 60 points apart.»

#### watchOS

- **Avoid placing more than two or three controls side by side in your interface.**
- **Support autorotation in views people might want to show others.**

## Recursos relacionados

- *Related:*
  - [Right to left](https://developer.apple.com/design/human-interface-guidelines/right-to-left)
  - [Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout)
  - [Layout and organization](https://developer.apple.com/design/human-interface-guidelines/layout-and-organization)
- *Developer documentation:*
  - [Composing custom layouts with SwiftUI](https://developer.apple.com/documentation/swiftui/composing-custom-layouts-with-swiftui) — SwiftUI

## Vídeos que la explican

- [Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356) → `references/videos/2025-356.md`
- [Compose custom layouts with SwiftUI](https://developer.apple.com/videos/play/wwdc2022/10056) → `references/videos/2022-10056.md`
- [Essential Design Principles](https://developer.apple.com/videos/play/wwdc2017/802) → `references/videos/2017-802.md`

## Registro de cambios

| Date | Changes |
|---|---|
| September 9, 2026 | Updated guidance to reflect current best practices. |
| September 9, 2025 | Added specifications for iPhone 17, iPhone Air, iPhone 17 Pro, iPhone 17 Pro Max, Apple Watch SE 3, Apple Watch Series 11, and Apple Watch Ultra 3. |
| June 9, 2025 | Added guidance for Liquid Glass. |
| March 7, 2025 | Added specifications for iPhone 16e, iPad 11-inch, iPad Air 11-inch, and iPad Air 13-inch. |
| September 9, 2024 | Added specifications for iPhone 16, iPhone 16 Plus, iPhone 16 Pro, iPhone 16 Pro Max, and Apple Watch Series 10. |
| June 10, 2024 | Made minor corrections and organizational updates. |
| February 2, 2024 | Enhanced guidance for avoiding system controls in iPadOS app layouts, and added specifications for 10.9-inch iPad Air and 8.3-inch iPad mini. |
| December 5, 2023 | Clarified guidance on centering content in a visionOS window. |
| September 15, 2023 | Added specifications for iPhone 15 Pro Max, iPhone 15 Pro, iPhone 15 Plus, iPhone 15, Apple Watch Ultra 2, and Apple Watch SE. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | Added specifications for iPhone 14 Pro Max, iPhone 14 Pro, iPhone 14 Plus, iPhone 14, and Apple Watch Ultra. |
