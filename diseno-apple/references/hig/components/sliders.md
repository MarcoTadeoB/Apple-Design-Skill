# Sliders — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/sliders
- Descargado: 2026-10-15
- Sección: components › Selection and input
- Plataformas: ios,ipados,macos,visionos,watchos
- Última actualización: 2023-06-21 — Updated to include guidance for visionOS.

> Resumen de Apple: A slider is a horizontal track with a control, called a thumb, that people can adjust between a minimum and maximum value.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- As a slider’s value changes, the portion of track between the minimum value and the thumb fills with color.

### Best practices

- **Customize a slider’s appearance if it adds value.**
- **Use familiar slider directions.**
  - «For example, people expect to be able to move a horizontal slider that represents a percentage from 0 percent on the leading side to 100 percent on the trailing side.»
- **Consider supplementing a slider with a corresponding text field and stepper.**

### Platform considerations

- *Not supported in tvOS.*

#### iOS, iPadOS

- **Don’t use a slider to adjust audio volume.**

#### macOS

- Sliders in macOS can also include tick marks, making it easier for people to pinpoint a specific value within the range.
- In a linear slider either with or without tick marks, the thumb is a narrow lozenge shape, and the portion of track between the minimum value and the thumb is filled with color.
- In a circular slider, the thumb appears as a small circle.
- **Consider giving live feedback as the value of a slider changes.**
- **Choose a slider style that matches peoples’ expectations.**
  - «For example, a graphics app might offer a horizontal slider for setting the opacity level of an object between 0 and 100 percent.»
  - «For example, a graphics app might use a circular slider to adjust the rotation of an object between 0 and 360 degrees.»
  - «An animation app might use a circular slider to adjust how many times an object spins when animated — four complete rotations equals four spins, or 1440 degrees of rotation.»
- **Consider using a label to introduce a slider.**
- **Use tick marks to increase clarity and accuracy.**
- **Consider adding labels to tick marks for even greater clarity.**
  - «It’s unnecessary to label every tick mark unless doing so is needed to reduce confusion.»

#### visionOS

- **Prefer horizontal sliders.**

#### watchOS

- A slider is a horizontal track — appearing as a set of discrete steps or as a continuous bar — that represents a finite range of values.
- **If necessary, create custom glyphs to communicate what the slider does.**

## Recursos relacionados

- *Related:*
  - [Steppers](https://developer.apple.com/design/human-interface-guidelines/steppers)
  - [Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers)
- *Developer documentation:*
  - [Slider](https://developer.apple.com/documentation/swiftui/slider) — SwiftUI
  - [UISlider](https://developer.apple.com/documentation/uikit/uislider) — UIKit
  - [NSSlider](https://developer.apple.com/documentation/appkit/nsslider) — AppKit

## Registro de cambios

| Date | Changes |
|---|---|
| June 21, 2023 | Updated to include guidance for visionOS. |
