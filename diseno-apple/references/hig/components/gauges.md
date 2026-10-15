# Gauges — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/gauges
- Descargado: 2026-10-15
- Sección: components › Status
- Plataformas: ios,ipados,macos,visionos,watchos
- Última actualización: 2022-09-23 — New page.

> Resumen de Apple: A gauge displays a specific numerical value within a range of values.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- In addition to indicating the current value in a range, a gauge can provide more context about the range itself.

### Anatomy

- A gauge uses a circular or linear path to represent a range of values, mapping the current value to a specific point on the path.
- Circular and linear gauges in both standard and capacity styles are also available in a variant that’s visually similar to watchOS complications.
> **Note:** In addition to gauges, macOS also supports level indicators, some of which have visual styles that are similar to gauges.

### Best practices

- **Write succinct labels that describe the current value and both endpoints of the range.**
- **Consider filling the path with a gradient to help communicate the purpose of the gauge.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, visionOS, or watchOS.

#### macOS

- In addition to supporting gauges, macOS also defines a level indicator that displays a specific numerical value within a range.
- The capacity style can depict discrete or continuous values.
- **Continuous.**
- **Discrete.**
- **Consider using the continuous style for large ranges.**
- **Consider changing the fill color to inform people about significant parts of the range.**
- For guidance using the rating style to help people rank something, see [Rating indicators](https://developer.apple.com/design/human-interface-guidelines/rating-indicators).
- Although rarely used, the relevance style can communicate relevancy using a shaded horizontal bar.

## Recursos relacionados

- *Related:*
  - [Ratings and reviews](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews)
- *Developer documentation:*
  - [Gauge](https://developer.apple.com/documentation/swiftui/gauge) — SwiftUI
  - [NSLevelIndicator](https://developer.apple.com/documentation/appkit/nslevelindicator) — AppKit

## Registro de cambios

| Date | Changes |
|---|---|
| September 23, 2022 | New page. |
