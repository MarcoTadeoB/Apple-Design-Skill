# Segmented controls — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/segmented-controls
- Descargado: 2026-10-15
- Sección: components › Selection and input
- Plataformas: ios,ipados,macos,tvos,visionos
- Última actualización: 2023-06-21 — Updated to include guidance for visionOS.

> Resumen de Apple: A segmented control is a linear set of two or more segments, each of which functions as a button.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Within a segmented control, all segments are usually equal in width.
- A segmented control offers a single choice from among a set of options, or in macOS, either a single choice or multiple choices.
- In addition to representing the state of a single or multiple-choice selection, a segmented control can function as a set of buttons that perform actions without showing a…

### Best practices

- **Use a segmented control to provide closely related choices that affect an object, state, or view.**
- **Consider a segmented control when it’s important to group functions together, or to clearly show their selection state.**
- **Keep control types consistent within a single segmented control.**
- **Limit the number of segments in a control.**
- **In general, keep segment size consistent.**

### Content

- **Prefer using either text or images — not a mix of both — in a single segmented control.**
- **As much as possible, use content with a similar size in each segment.**
- **Use nouns or noun phrases for segment labels.**

### Platform considerations

- *Not supported in watchOS.*

#### iOS, iPadOS

- **Consider a segmented control to switch between closely related subviews.**

#### macOS

- **Consider using introductory text to clarify the purpose of a segmented control.**
- **Use a tab view in the main window area — instead of a segmented control — for view switching.**
- **Consider supporting spring loading.**

#### tvOS

- **Consider using a split view instead of a segmented control on screens that perform content filtering.**
- **Avoid putting other focusable elements close to segmented controls.**

#### visionOS

- When people look at a segmented control that uses icons, the system displays a tooltip that contains the descriptive text you supply.

## Recursos relacionados

- *Related:*
  - [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views)
- *Developer documentation:*
  - [segmented](https://developer.apple.com/documentation/swiftui/pickerstyle/segmented) — SwiftUI
  - [UISegmentedControl](https://developer.apple.com/documentation/uikit/uisegmentedcontrol) — UIKit
  - [NSSegmentedControl](https://developer.apple.com/documentation/appkit/nssegmentedcontrol) — AppKit

## Registro de cambios

| Date | Changes |
|---|---|
| June 21, 2023 | Updated to include guidance for visionOS. |
