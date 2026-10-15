# Pickers — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/pickers
- Descargado: 2026-10-15
- Sección: components › Selection and input
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2023-06-05 — Updated guidance for using pickers in watchOS.

> Resumen de Apple: A picker displays one or more scrollable lists of distinct values that people can choose from.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- The system provides several styles of pickers, each of which offers different types of selectable values and has a different appearance.
- Pickers help people enter information by letting them choose single or multipart values.

### Best practices

- **Consider using a picker to offer medium-to-long lists of items.**
- **Use predictable and logically ordered values.**
- **Avoid switching views to show a picker.**
- **Consider providing less granularity when specifying minutes in a date picker.**

### Platform considerations

- *No additional considerations for visionOS.*

#### iOS, iPadOS

- A date picker is an efficient interface for selecting a specific date, time, or both, using touch, a keyboard, or a pointing device.
  - Compact — A button that displays editable date and time content in a modal view.
  - Inline — For time only, a button that displays wheels of values; for dates and times, an inline calendar view.
  - Wheels — A set of scrolling wheels that also supports data entry through built-in or external keyboards.
  - Automatic — A system-determined style based on the current platform and date picker mode.
- A date picker has four modes, each of which presents a different set of selectable values.
  - Date — Displays months, days of the month, and years.
  - Time — Displays hours, minutes, and (optionally) an AM/PM designation.
  - Date and time — Displays dates, hours, minutes, and (optionally) an AM/PM designation.
  - Countdown timer — Displays hours and minutes, up to a maximum of 23 hours and 59 minutes. This mode isn’t available in the inline or compact styles.
- The exact values shown in a date picker, and their order, depend on the device location.
- Here are several examples of date pickers showing different combinations of style and mode.
- **Use a compact date picker when space is constrained.**

#### macOS

- **Choose a date picker style that suits your app.**
- For developer guidance, see [NSDatePicker](https://developer.apple.com/documentation/appkit/nsdatepicker).

#### tvOS

- Pickers are available in tvOS with SwiftUI.

#### watchOS

- Pickers display lists of items that people navigate using the Digital Crown, which helps people manage selections in a precise and engaging way.
- A picker can display a list of items using the wheels style. watchOS can also display date and time pickers using the wheels style.
- You can configure a picker to display an outline, caption, and scrolling indicator.
- For longer lists, the navigation link displays the picker as a button.

## Recursos relacionados

- *Related:*
  - [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons)
  - [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)
- *Developer documentation:*
  - [Picker](https://developer.apple.com/documentation/swiftui/picker) — SwiftUI
  - [UIDatePicker](https://developer.apple.com/documentation/uikit/uidatepicker) — UIKit
  - [UIPickerView](https://developer.apple.com/documentation/uikit/uipickerview) — UIKit
  - [NSDatePicker](https://developer.apple.com/documentation/appkit/nsdatepicker) — AppKit

## Registro de cambios

| Date | Changes |
|---|---|
| June 5, 2023 | Updated guidance for using pickers in watchOS. |
