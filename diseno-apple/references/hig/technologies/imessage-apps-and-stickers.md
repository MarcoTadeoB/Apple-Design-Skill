# iMessage apps and stickers — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/imessage-apps-and-stickers
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados
- Última actualización: 2023-05-02 — Consolidated guidance into one page.

> Resumen de Apple: An iMessage app can help people share content, collaborate, and even play games with others in a conversation; stickers are images that people can use to decorate a conversation.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- An iMessage app or sticker pack is available within the context of a Messages conversation and also in effects in both Messages and FaceTime.

### Best practices

- **Prefer providing one primary experience in your iMessage app.**
- **Consider surfacing content from your iOS or iPadOS app.**
- **Present essential features in the compact view.**
- **In general, let people edit text only in the expanded view.**
- **Create stickers that are expressive, inclusive, and versatile.**
- **For each sticker, provide a localized alternative description.**

### Specifications

#### Icon sizes

- The icon for an iMessage app or sticker pack can appear in Messages, the App Store, notifications, and Settings.
- You supply a square-cornered icon for each extension you offer, and the system automatically applies a mask that rounds the corners.
- To ensure that your icon looks great in any context and on various devices, create a square-cornered icon in the following sizes:

| Usage | @2x (pixels) | @3x (pixels) |
|---|---|---|
| Messages, notifications | 148x110 | - |
|  | 143x100 | - |
|  | 120x90 | 180x135 |
|  | 64x48 | 96x72 |
|  | 54x40 | 81x60 |
| Settings | 58x58 | 87x87 |
| App Store | 1024x1024 | 1024x1024 |

#### Sticker sizes

- Messages supports small, regular, and large stickers.
- Create your sticker images using the following @3x dimensions for the sticker size you chose.
  - «If necessary, the system generates @2x and @1x versions by downscaling the images at runtime.»

| Sticker size | @3x dimensions (pixels) |
|---|---|
| Small | 300x300 |
| Regular | 408x408 |
| Large | 618x618 |

- A sticker file must be 500 KB or smaller in size.

| Format | Transparency | Animation |
|---|---|---|
| PNG | 8-bit | No |
| APNG | 8-bit | Yes |
| GIF | Single-color | Yes |
| JPEG | No | No |

### Platform considerations

- *No additional considerations for iOS or iPadOS.

## Recursos relacionados

- *Related:*
  - [iMessage Apps and Stickers](https://developer.apple.com/imessage/)
- *Developer documentation:*
  - [Messages](https://developer.apple.com/documentation/messages)
  - [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](https://developer.apple.com/documentation/messages/adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime) — Messages

## Vídeos que la explican

- [Express Yourself!](https://developer.apple.com/videos/play/wwdc2017/820) → `references/videos/2017-820.md`

## Registro de cambios

| Date | Changes |
|---|---|
| May 2, 2023 | Consolidated guidance into one page. |
