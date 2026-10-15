# Image views — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/image-views
- Descargado: 2026-10-15
- Sección: components › Content
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2023-06-21 — Updated to include guidance for visionOS.

> Resumen de Apple: An image view displays a single image — or in some cases, an animated sequence of images — on a transparent or opaque background.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Within an image view, you can stretch, scale, size to fit, or pin the image to a specific location.

### Best practices

- **Use an image view when the primary purpose of the view is simply to display an image.**
- **If you want to display an icon in your interface, consider using a symbol or interface icon instead of an image view.**

### Content

- An image view can contain rich image data in various formats, like PNG, JPEG, and PDF.
- **Take care when overlaying text on images.**
- **Aim to use a consistent size for all images in an animated sequence.**

### Platform considerations

- *No additional considerations for iOS or iPadOS.*

#### macOS

- **If your app needs an editable image view, use an image well.**
- **Use an image button instead of an image view to make a clickable image.**

#### tvOS

- Many tvOS images combine multiple layers with transparency to create a feeling of depth.

#### visionOS

- Windows in visionOS apps and games can use image views to display 2D and stereoscopic images, as well as spatial photos.
- For guidance on presenting other 3D content in a window or volume, see [Windows > visionOS](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS).

#### watchOS

- **Use SwiftUI to create animations when possible.**

## Recursos relacionados

- *Related:*
  - [Images](https://developer.apple.com/design/human-interface-guidelines/images)
  - [Image wells](https://developer.apple.com/design/human-interface-guidelines/image-wells)
  - [Image buttons](https://developer.apple.com/design/human-interface-guidelines/buttons#Image-buttons)
  - [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols)
- *Developer documentation:*
  - [Image](https://developer.apple.com/documentation/swiftui/image) — SwiftUI
  - [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview) — UIKit
  - [NSImageView](https://developer.apple.com/documentation/appkit/nsimageview) — AppKit

## Vídeos que la explican

- [Support HDR images in your app](https://developer.apple.com/videos/play/wwdc2023/10181) → `references/videos/2023-10181.md`
- [Add rich graphics to your SwiftUI app](https://developer.apple.com/videos/play/wwdc2021/10021) → `references/videos/2021-10021.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 21, 2023 | Updated to include guidance for visionOS. |
