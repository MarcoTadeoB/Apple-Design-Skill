# Escala tipográfica de Dynamic Type en iOS (tamaño por defecto: **Large**)

El tamaño de contenido por defecto en iOS es **Large** (`UIContentSizeCategory.large` / `DynamicTypeSize.large`). Estos son los valores de cada estilo de texto del sistema con la fuente SF Pro, según las Human Interface Guidelines:

| Estilo | API (SwiftUI / UIKit) | Peso | Tamaño (pt) | Interlineado (pt) | Tracking (pt) | Peso enfatizado |
|---|---|---|---|---|---|---|
| Large Title | `.largeTitle` / `.largeTitle` | Regular | 34 | 41 | +0,40 | Bold |
| Title 1 | `.title` / `.title1` | Regular | 28 | 34 | +0,38 | Bold |
| Title 2 | `.title2` / `.title2` | Regular | 22 | 28 | −0,26 | Bold |
| Title 3 | `.title3` / `.title3` | Regular | 20 | 25 | −0,45 | Semibold |
| Headline | `.headline` / `.headline` | **Semibold** | 17 | 22 | −0,43 | Semibold |
| Body | `.body` / `.body` | Regular | 17 | 22 | −0,43 | Semibold |
| Callout | `.callout` / `.callout` | Regular | 16 | 21 | −0,31 | Semibold |
| Subheadline | `.subheadline` / `.subheadline` | Regular | 15 | 20 | −0,23 | Semibold |
| Footnote | `.footnote` / `.footnote` | Regular | 13 | 18 | −0,08 | Semibold |
| Caption 1 | `.caption` / `.caption1` | Regular | 12 | 16 | 0 | Medium |
| Caption 2 | `.caption2` / `.caption2` | Regular | 11 | 13 | +0,06 | Semibold |

## Notas útiles

- **Headline es el único estilo cuyo peso por defecto no es Regular**: es Semibold al mismo tamaño que Body (17 pt). Por eso se distingue de Body por peso, no por tamaño.
- **Peso enfatizado**: es el que obtienes con `.bold()` / `.fontWeight(.bold)` en SwiftUI o con el rasgo simbólico `.traitBold` en UIKit (`UIFontDescriptor.withSymbolicTraits`).
- **SF Pro Display vs. SF Pro Text**: el sistema usa la variante óptica *Display* a partir de 20 pt y *Text* por debajo. Con la fuente del sistema (`.font(.body)`, `UIFont.preferredFont(forTextStyle:)`) esto, igual que el tracking, se aplica de forma automática. Solo tienes que replicarlo a mano en herramientas de diseño (Figma, Sketch) o si usas una fuente personalizada.
- **Tracking**: los valores están en puntos. Para pasarlos a CSS o a porcentaje en Figma, divide entre el tamaño: por ejemplo, Body = −0,43 / 17 ≈ −0,025 em (−2,5 %).
- **Versiones anteriores**: las HIG antiguas (iOS 11–16 aprox.) daban otros valores de tracking, como Large Title +0,37, Title 1 +0,36, Title 2 +0,35, Title 3 +0,38, Headline/Body −0,41, Callout −0,32, Subheadline −0,24, Caption 2 +0,07. Los tamaños y los interlineados no han cambiado. Si tu archivo de diseño usa esos valores, lo más probable es que venga de un kit de UI antiguo.
- **Escalado**: estos valores son solo los del punto de partida. Al cambiar el tamaño de texto en Ajustes, cada estilo escala de forma no lineal. Por ejemplo, Body va de 14 pt en xSmall a 23 pt en xxxLarge, y llega hasta 53 pt en el tamaño de accesibilidad más grande (AX5). Para que tus fuentes personalizadas sigan la misma curva, usa `UIFontMetrics` (UIKit) o `@ScaledMetric` / `.font(.custom(_:size:relativeTo:))` (SwiftUI).
- **Estilos adicionales**: desde iOS 17 existen `extraLargeTitle` y `extraLargeTitle2`, pensados sobre todo para visionOS. No forman parte de la escala clásica de iOS.
