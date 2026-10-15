# Top Shelf — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/top-shelf
- Descargado: 2026-10-15
- Sección: components › System experiences
- Plataformas: tvos
- Última actualización: sin registro de cambios

> Resumen de Apple: The Apple TV Home Screen provides an area called Top Shelf, which showcases your content in a rich, engaging way while also giving people access to their favorite apps in the Dock.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- When you support full-screen Top Shelf, people can swipe through multiple full-screen content views, play trailers and previews, and get more information about your content.
- Top Shelf is a unique opportunity to highlight new, featured, or recommended content and let people jump directly to your app or game to view it.
- The system defines several layout templates that you can use to give people a compelling Top Shelf experience when they select your app in the Dock.

### Best practices

- **Help people jump right into your content.**
- **Feature new content.**
- **Personalize people’s favorite content.**
- **Avoid showing advertisements or prices.**
- **Showcase compelling dynamic content that can help draw people in and encourage them to view more.**
- **If you don’t provide the recommended full-screen content, supply at least one static image as a fallback.**
  - «The system displays a static image when your app is in the Dock and in focus and full-screen content is unavailable. tvOS flips and blurs the image, ensuring that it fits into a width of 1920 pixels at the 16:9 aspect ratio.»

| Image size |
|---|
| 2320x720 pt (2320x720 px @1x, 4640x1440 px @2x) |

- **Avoid implying interactivity in a static image.**

### Dynamic layouts

- Dynamic Top Shelf images can appear in several ways:
  - A carousel of full-screen video and images that includes two buttons and optional details
  - A row of focusable content
  - A set of scrolling banners

#### Carousel actions

- The carousel actions layout style focuses on full-screen video and images and includes a few unobtrusive controls that help people see more.
- **Provide a title.**

#### Carousel details

- This layout style extends the carousel actions layout style, giving you the opportunity to include some information about the content.
- **Provide a title that identifies the currently playing content.**

#### Sectioned content row

- This layout style shows a single labeled row of sectioned content, which can work well to highlight recently viewed content, new content, or favorites.
- **Provide enough content to constitute a complete row.**
- You can use the following image sizes in a sectioned content row.

##### Poster (2:3)

| Aspect | Image size |
|---|---|
| Actual size | 404x608 pt (404x608 px @1x, 808x1216 px @2x) |
| Focused/Safe zone size | 380x570 pt (380x570 px @1x, 760x1140 px @2x) |
| Unfocused size | 333x570 pt (333x570 px @1x, 666x1140 px @2x) |

##### Square (1:1)

| Aspect | Image size |
|---|---|
| Actual size | 608x608 pt (608x608 px @1x, 1216x1216 px @2x) |
| Focused/Safe zone size | 570x570 pt (570x570 px @1x, 1140x1140 px @2x) |
| Unfocused size | 500x500 pt (500x500 px @1x, 1000x1000 px @2x) |

##### 16:9

| Aspect | Image size |
|---|---|
| Actual size | 908x512 pt (908x512 px @1x, 1816x1024 px @2x) |
| Focused/Safe zone size | 852x479 pt (852x479 px @1x, 1704x958 px @2x) |
| Unfocused size | 782x440 pt (782x440 px @1x, 1564x880 px @2x) |

- **Be aware of additional scaling when combining image sizes.**
  - «For example, a 16:9 image scales to 500 pixels high if included in a row with a poster or square image.»

##### Scrolling inset banner

- This layout shows a series of large images, each of which spans almost the entire width of the screen.
- When a banner is in focus, a small, circular gesture on the remote’s Touch surface enacts the system focus effect, animating the item, applying lighting effects, and, if the…
- **Provide three to eight images.**
- **If you need text, add it to your image.**
- Use the following size for a scrolling inset banner image:

| Aspect | Image size |
|---|---|
| Actual size | 1940x692 pt (1940x692 px @1x, 3880x1384 px  @2x) |
| Focused/Safe zone size | 1740x620 pt (1740x620 px @1x, 3480x1240 px @2x) |
| Unfocused size | 1740x560 pt (1740x560 px @1x, 3480x1120 px @2x) |

### Platform considerations

- *Not supported in iOS, iPadOS, macOS, visionOS, or watchOS.*

## Recursos relacionados

- *Related:*
  - [Apple Design Resources](https://developer.apple.com/design/resources/#tvos-apps)

## Vídeos que la explican

- [Mastering the Living Room With tvOS](https://developer.apple.com/videos/play/wwdc2019/211) → `references/videos/2019-211.md`
