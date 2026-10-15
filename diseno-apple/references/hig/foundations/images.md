# Images — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/images
- Descargado: 2026-10-15
- Sección: foundations
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2025-12-16 — Added guidance for spatial photos and spatial scenes in visionOS.

> Resumen de Apple: To make sure your artwork looks great on all devices you support, learn how the system displays content and how to deliver art at the appropriate scale factors.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
### Resolution

- Different devices can display images at different resolutions.
- A *point* is an abstract unit of measurement that helps visual content remain consistent regardless of how it’s displayed.
- When creating bitmap images, you specify a *scale factor* which determines the resolution of an image.
  - «For example, a scale factor of 1 (also called @1x) describes a 1:1 pixel density, where one pixel is equal to one point.»
  - «High-resolution 2D displays have higher pixel densities, such as 2:1 or 3:1.»
  - «A 2:1 density (called @2x) has a scale factor of 2, and a 3:1 density (called @3x) has a scale factor of 3.»
- (imagen) Image of a circle that's in standard resolution at scale factor of @1x, and is 10 by 10 pixels.
- (imagen) Image of a circle that's in high resolution at a scale factor of @2x, and is 20 by 20 pixels.
- (imagen) Image of a circle that's in high resolution at a scale factor of @3x, and is 30 by 30 pixels.
- **Provide high-resolution assets for all bitmap images in your app, for every device you support.**
  - «As you add each image to your project’s asset catalog, identify its scale factor by appending “@1x,” “@2x,” or “@3x” to its filename.»

| Platform | Scale factors |
|---|---|
| iPadOS, watchOS | @2x |
| iOS | @2x and @3x |
| visionOS | @2x or higher (see [visionOS](https://developer.apple.com/design/human-interface-guidelines/images#visionOS)) |
| macOS, tvOS | @1x and @2x |

- **In general, design images at the lowest resolution and scale them up to create high-resolution assets.**
  - «When you use resizable vectorized shapes, you might want to position control points at whole values so that they’re cleanly aligned at 1x.»
  - «This positioning allows the points to remain cleanly aligned to the raster grid at higher resolutions, because 2x and 3x are multiples of 1x.»

### Formats

- As you create different types of images, consider the following recommendations.

| Image type | Format |
|---|---|
| Bitmap or raster work | De-interlaced PNG files |
| PNG graphics that don’t require full 24-bit color | An 8-bit color palette |
| Photos | JPEG files, optimized as necessary, or HEIC files |
| Stereo or spatial photos | Stereo HEIC |
| Flat icons, interface icons, and other flat artwork that requires high-resolution scaling | PDF or SVG files |

### Best practices

- **Include a color profile with each image.**
- **Always test images on a range of actual devices.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, or macOS.*

#### tvOS

- Layered images are at the heart of the Apple TV user experience.

##### Parallax effect

- *Parallax* is a subtle visual effect the system uses to convey depth and dynamism when an element is in focus.
- Layered images are required to support the parallax effect.

##### Layered images

- A *layered image* consists of two to five distinct layers that come together to form a single image.
> **Important:** Your tvOS [app icon](https://developer.apple.com/design/human-interface-guidelines/app-icons#tvOS) must use a layered image.
- You can embed layered images in your app or retrieve them from a content server at runtime.
> **Developer note:** If your app retrieves layered images from a content server at runtime, you must provide runtime layered images (`.lcr`).
- **Use standard interface elements to display layered images.**
- **Identify logical foreground, middle, and background elements.**
- **Generally, keep text in the foreground.**
  - «Unless you want to obscure text, bring it to the foreground layer for clarity.»
- **Keep the background layer opaque.**
- **Keep layering simple and subtle.**
- **Leave a safe zone around the foreground layers of your image.**
- **Always preview layered images.**

#### visionOS

- In visionOS, people can view images at a much larger range of sizes than in any other platform, and the system dynamically scales the image resolution to match the current size.
  - «Because you can position images at specific angles within someone’s surroundings, image pixels may not line up 1:1 with screen pixels.»
- **Create a layered app icon.**
- **Prefer vector-based art for 2D images.**
- **If you need to use rasterized images, balance quality with performance as you choose a resolution.**
  - «Although a @2x image looks fine at common viewing distances, its fixed resolution means that the system doesn’t dynamically scale it and it might not look sharp from close up.»
  - «To help a rasterized image look sharp when people view it from a wide range of distances, you can use a higher resolution, but each increase in resolution results in a larger file size and may impact your app’s runtime performance,…»
  - «If you use images that have resolutions higher than @2x, be sure to also apply high-quality image filtering to help balance quality and performance (for developer guidance, see…»

##### Spatial photos and spatial scenes

- In addition to 2D and stereoscopic images, visionOS apps and games can use RealityKit to display spatial photos and spatial scenes.
- **Make sure spatial photos render correctly in your app.**
- **Prefer the feathered glass background effect to display text over spatial photos.**
- **Take visual comfort into consideration when you make spatial photos from existing 2D content.**
- **Display spatial photos and spatial scenes in standalone views.**
- **Use spatial scenes in your app for specific moments.**
- **When displaying immersively, prefer minimal UI.**
- **Prefer displaying larger spatial scenes that you center in someone’s field of view.**

#### watchOS

- **In general, avoid transparency to keep image files small.**
- **Use autoscaling PDFs to let you provide a single asset for all screen sizes.**
  - «Design your image for the 40mm and 42mm screens at 2x.»

| Screen size | Image scale |
|---|---|
| 38mm | 90% |
| 40mm | 100% |
| 41mm | 106% |
| 42mm | 100% |
| 44mm | 110% |
| 45mm | 119% |
| 49mm | 119% |

## Recursos relacionados

- *Related:*
  - [Apple Design Resources](https://developer.apple.com/design/resources/)
- *Developer documentation:*
  - [Drawing sharp layer-based content in visionOS](https://developer.apple.com/documentation/visionos/drawing-sharp-layer-based-content) — visionOS
  - [Images](https://developer.apple.com/documentation/swiftui/images) — SwiftUI
  - [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview) — UIKit
  - [NSImageView](https://developer.apple.com/documentation/appkit/nsimageview) — AppKit

## Registro de cambios

| Date | Changes |
|---|---|
| December 16, 2025 | Added guidance for spatial photos and spatial scenes in visionOS. |
| December 5, 2023 | Clarified guidance on choosing a resolution for a rasterized image in a visionOS app. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | Added specifications for Apple Watch Ultra. |
