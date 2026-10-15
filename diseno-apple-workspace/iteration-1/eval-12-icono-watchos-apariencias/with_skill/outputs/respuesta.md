# Icono de app: lienzo de watchOS y apariencias en iOS 27

## Respuesta corta

- **watchOS**: el lienzo (*layout size*) del icono es **1088×1088 px**, cuadrado. Después el sistema lo enmascara en un **círculo**. Es un icono por capas (*Layered*).
- **iOS 27** (igual en iPadOS y macOS): el icono admite **seis apariencias**: **Default, Dark, Clear light, Clear dark, Tinted light y Tinted dark**. El lienzo es de **1024×1024 px**.

Fuente: tabla *Specifications* de [App icons — HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons), actualizada por última vez el **8-6-2026** («Refined guidance for Liquid Glass»), que es la versión vigente para las plataformas 27.

## Tabla de especificaciones (literal de Apple)

| Platform | Layout shape | Icon shape after system masking | Layout size | Style | Appearances |
|---|---|---|---|---|---|
| iOS, iPadOS, macOS | Square | Rounded rectangle (square) | 1024x1024 px | Layered | Default, dark, clear light, clear dark, tinted light, tinted dark |
| tvOS | Rectangle (landscape) | Rounded rectangle (rectangular) | 800x480 px | Layered (Parallax) | N/A |
| visionOS | Square | Circular | 1024x1024 px | Layered (3D) | N/A |
| watchOS | Square | Circular | 1088x1088 px | Layered | N/A |

Como muestra la tabla, en watchOS no hay variantes de apariencia (**N/A**). Las apariencias dark, clear y tinted solo existen en iOS, iPadOS y macOS.

## Detalle: watchOS (1088 px)

- **Por qué 1088 y no 1024**: en *Say hello to the new look of app icons* (WWDC25), Apple explica que el lienzo circular sobresale del rectángulo redondeado. Así es más fácil adaptar el mismo diseño de una plataforma a otra: [4:38](https://developer.apple.com/videos/play/wwdc2025/220/?time=278) «The 1088 pixel canvas overshoots our rounded rectangle, which helps to create easier translations between platforms and to achieve visual consistency.»
- **Entrega capas cuadradas sin máscara**: el sistema aplica el círculo. Las reglas de Apple son **«Produce appropriately shaped, unmasked layers.»** y **«Keep primary content centered to avoid truncation when the system adjusts corners or applies masking.»**
- **Regla propia de watchOS**: **«Avoid using black for your icon's background.»**
- Los iconos de iOS, iPadOS, macOS y watchOS llevan una capa de fondo y una o varias capas de primer plano (App icons, *Layer design*).

## Detalle: apariencias en iOS 27

- La HIG dice: «In iOS, iPadOS, and macOS, people can choose whether their Home Screen app icons are default, dark, clear, or tinted in appearance.» Clear y tinted tienen cada una una versión clara y otra oscura, y por eso son seis en total.
- El vídeo [WWDC25-220](https://developer.apple.com/videos/play/wwdc2025/220) explica qué es cada una. Esta es una paráfrasis del resumen, no un texto literal de Apple:
  - **Default** (claro).
  - **Dark**.
  - **Clear light / clear dark**: el icono se muestra como cristal monocromo.
  - **Tinted dark**: el color se aplica al primer plano.
  - **Tinted light**: el color se mezcla con el cristal.
- Reglas literales de la sección *Appearances*:
  - **«Keep your icon's features consistent across appearances.»**
  - **«Design dark and tinted icons that feel at home beside system app icons and widgets.»**
  - **«Use your light app icon as the basis for your dark icon.»**
  - **«Consider offering alternate app icons.»** Nota de Apple: «Alternate app icons in iOS and iPadOS require their own dark, clear, and tinted variants.»
- **Herramienta**: con [Icon Composer](https://developer.apple.com/icon-composer/) (Icon Composer 2, desde el 8-6-2026) creas un solo diseño para iPhone, iPad, Mac y Apple Watch. Puedes ajustar cada modo con las anotaciones **Default, Dark y Mono**. Necesita **macOS Tahoe 26.4 o posterior**.

## Otros datos útiles

- Espacios de color admitidos: sRGB, Gray Gamma 2.2 y Display P3. Display P3 solo funciona en iOS, iPadOS, macOS, tvOS y watchOS, no en visionOS.
- El sistema reduce automáticamente el icono para generar los tamaños pequeños (Settings, notificaciones). No necesitas crearlos a mano.
- **Novedades en la versión 27**: según el registro de cambios, la actualización del 8-6-2026 «refinó la guía de Liquid Glass». Los tamaños de lienzo y el conjunto de apariencias son los que se introdujeron en la versión 26 (9-6-2025); la tabla vigente es la de arriba.
