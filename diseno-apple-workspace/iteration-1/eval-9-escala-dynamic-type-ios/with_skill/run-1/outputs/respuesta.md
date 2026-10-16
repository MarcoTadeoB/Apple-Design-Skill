# Escala de Dynamic Type de iOS y iPadOS en el tamaño por defecto (Large)

En iOS y iPadOS el tamaño por defecto de Dynamic Type es **Large**. En él, el texto de cuerpo mide 17 pt y el tamaño mínimo es 11 pt. La fuente del sistema es **SF Pro**.

Fuente: [HIG › Typography › Specifications](https://developer.apple.com/design/human-interface-guidelines/typography#Specifications). Última actualización de la página: 16-12-2025 («Added emphasized weights to the Dynamic Type style specifications for each platform»). Datos tomados el 15-10-2026.

## Tabla completa

| Estilo (text style) | Peso | Tamaño (pt) | Interlineado / leading (pt) | Tracking (1/1000 em) | Tracking (pt) | Peso enfatizado |
|---|---|---|---|---|---|---|
| Large Title | Regular | 34 | 41 | +12 | +0.40 | Bold |
| Title 1 | Regular | 28 | 34 | +14 | +0.38 | Bold |
| Title 2 | Regular | 22 | 28 | −12 | −0.26 | Bold |
| Title 3 | Regular | 20 | 25 | −23 | −0.45 | Semibold |
| Headline | **Semibold** | 17 | 22 | −26 | −0.43 | Semibold |
| Body | Regular | 17 | 22 | −26 | −0.43 | Semibold |
| Callout | Regular | 16 | 21 | −20 | −0.31 | Semibold |
| Subhead | Regular | 15 | 20 | −16 | −0.23 | Semibold |
| Footnote | Regular | 13 | 18 | −6 | −0.08 | Semibold |
| Caption 1 | Regular | 12 | 16 | 0 | 0.0 | Semibold |
| Caption 2 | Regular | 11 | 13 | +6 | +0.06 | Semibold |

**De dónde sale cada columna**

- **Peso, tamaño, leading y peso enfatizado**: tabla literal «iOS, iPadOS Dynamic Type sizes › Large (default)» de la HIG.
- **Tracking**: Apple no lo publica por estilo. Lo publica **por tamaño en puntos**, en la tabla «iOS, iPadOS, visionOS tracking values › SF Pro» ([Typography › Tracking values](https://developer.apple.com/design/human-interface-guidelines/typography#Specifications)). Yo he cruzado el tamaño de cada estilo con esa tabla. Los valores son de Apple; solo la asignación a cada estilo es mía.
- Apple aclara que los tamaños son «Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.»

## Notas de uso

- **En apps nativas no copies los valores: usa los estilos del sistema.** Reglas de Apple: «Consider using the built-in text styles» y «Modify the built-in text styles if necessary». Con los estilos del sistema, Dynamic Type escala el texto solo, y el sistema aplica el tracking y el tamaño óptico. Esta nota sobre las API es mía, no viene de las HIG: en SwiftUI los estilos son `.largeTitle`, `.title`, `.title2`, `.title3`, `.headline`, `.body`, `.callout`, `.subheadline`, `.footnote`, `.caption` y `.caption2`.
- **Peso enfatizado**: es la variante que se obtiene con `bold()` en SwiftUI o `traitBold` en UIKit. Apple: «You can display emphasized variants of system text styles using symbolic traits.»
- **El tracking sirve sobre todo para maquetas.** Apple dice: «If necessary, adjust tracking in interface mockups.» El tracking de SF Pro varía con el tamaño. Es positivo en tamaños pequeños, negativo entre unos 13 y 23 pt, y vuelve a ser positivo en los títulos. Esto se debe a que SF Pro es una fuente variable que «transitions from Text to Display between 17 and 28 points» ([WWDC20 «The details of UI typography», 11:33](https://developer.apple.com/videos/play/wwdc2020/10175/?time=693)).
- **El leading ya está resuelto**: «Most of the time, you don't need to concern yourself with leading or line height, because we've already defined them in most of our UI components» ([WWDC20, 14:35](https://developer.apple.com/videos/play/wwdc2020/10175/?time=875)).
- **El diseño debe adaptarse a todos los tamaños.** Large es solo el punto de partida. La escala tiene además xSmall, Small, Medium, xLarge, xxLarge y xxxLarge, y los tamaños de accesibilidad AX1–AX5. Reglas de Apple: «Make sure your app’s layout adapts to all font sizes» y «Keep text truncation to a minimum as font size increases» ([Typography › Supporting Dynamic Type](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type)).

## Si lo llevas a CSS (web)

En Safari de iOS, 1 pt equivale a 1 px CSS, y el tracking se pasa a `letter-spacing` en em (milésimas / 1000). Esta conversión es una aproximación propia de la skill, no una especificación de Apple.

```css
.large-title { font-size: 34px; line-height: 41px; font-weight: 400; letter-spacing: 0.012em; }
.title-1     { font-size: 28px; line-height: 34px; font-weight: 400; letter-spacing: 0.014em; }
.title-2     { font-size: 22px; line-height: 28px; font-weight: 400; letter-spacing: -0.012em; }
.title-3     { font-size: 20px; line-height: 25px; font-weight: 400; letter-spacing: -0.023em; }
.headline    { font-size: 17px; line-height: 22px; font-weight: 600; letter-spacing: -0.026em; }
.body        { font-size: 17px; line-height: 22px; font-weight: 400; letter-spacing: -0.026em; }
.callout     { font-size: 16px; line-height: 21px; font-weight: 400; letter-spacing: -0.02em; }
.subhead     { font-size: 15px; line-height: 20px; font-weight: 400; letter-spacing: -0.016em; }
.footnote    { font-size: 13px; line-height: 18px; font-weight: 400; letter-spacing: -0.006em; }
.caption-1   { font-size: 12px; line-height: 16px; font-weight: 400; letter-spacing: 0em; }
.caption-2   { font-size: 11px; line-height: 13px; font-weight: 400; letter-spacing: 0.006em; }
```

Usa la fuente del sistema (`font-family: system-ui, -apple-system, …`). **No incrustes SF Pro en una web**, porque su licencia no lo permite. Si quieres que la web respete el tamaño de texto elegido en Ajustes, usa `html { font: -apple-system-body; }`, que solo funciona en WebKit, y expresa el resto en `rem`.
