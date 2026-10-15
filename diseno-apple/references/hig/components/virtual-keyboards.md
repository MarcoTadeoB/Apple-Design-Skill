# Virtual keyboards — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards
- Descargado: 2026-10-15
- Sección: components › Selection and input
- Plataformas: ios,ipados,tvos,visionos,watchos
- Última actualización: 2025-06-09 — Added guidance for displaying custom controls above the keyboard, and updated to reflect virtual keyboard availability in watchOS.

> Resumen de Apple: On devices without physical keyboards, the system offers various types of virtual keyboards people can use to enter data.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- A virtual keyboard can provide a specific set of keys that are optimized for the current task; for example, a keyboard that supports entering email addresses can include the “@”…
- When it makes sense in your app, you can replace the system-provided keyboard with a custom view that supports app-specific data entry.

### Best practices

- **Choose a keyboard that matches the type of content people are editing.**
- **Consider customizing the Return key type if it helps clarify the text-entry experience.**

### Custom input views

- In some cases, you can create an *input view* if you want to provide custom functionality that enhances data-entry tasks in your app.
- **Make sure your custom input view makes sense in the context of your app.**
- **Play the standard keyboard sound while people type.**

### Custom keyboards

- In iOS, iPadOS, and tvOS, you can provide a custom keyboard that replaces the system keyboard by creating an app extension.
- After people choose your custom keyboard in Settings, they can use it for text entry within any app, except when editing secure text fields and phone number fields.
- Custom keyboards make sense when you want to expose unique keyboard functionality systemwide, such as a novel way of inputting text or the ability to type in a language the…
- **Provide an obvious and easy way to switch between keyboards.**
- **Avoid duplicating system-provided keyboard features.**
- **Consider providing a keyboard tutorial in your app.**

### Platform considerations

- *Not supported in macOS.*

#### iOS, iPadOS

- **Use the keyboard layout guide to make the keyboard feel like an integrated part of your interface.**
  - ✅ Ejemplo correcto: An illustration of an app layout on iPhone, showing two stacked text fields and a button above the keyboard.
  - ❌ Ejemplo incorrecto: An illustration of an app layout on iPhone, showing two stacked text fields. The keyboard covers part of the bottom text field.
  - ❌ Ejemplo incorrecto: An illustration of an app layout on iPhone, showing two stacked text fields and a button above the keyboard. The keyboard covers part of the button.
- **Place custom controls above the keyboard thoughtfully.**

#### tvOS

- tvOS displays a linear virtual keyboard when people select a text field using the Siri Remote.
> **Note:** A grid keyboard screen appears when people use devices other than the Siri Remote, and the layout of content automatically adapts to the keyboard.
- When people activate a digit entry view, tvOS displays a digit-specific keyboard.

#### visionOS

- In visionOS, the system-provided virtual keyboard supports both direct and indirect gestures and appears in a separate window that people can move where they want.

#### watchOS

- On Apple Watch, a text field can show a keyboard if the device screen is large enough.
- People can also use a nearby paired iPhone to enter text on Apple Watch.

## Recursos relacionados

- *Related:*
  - [Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data)
  - [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards)
  - [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- *Developer documentation:*
  - [keyboardType(_:)](https://developer.apple.com/documentation/swiftui/view/keyboardtype(_:)) — SwiftUI
  - [textContentType(_:)](https://developer.apple.com/documentation/swiftui/view/textcontenttype(_:)) — SwiftUI
  - [UIKeyboardType](https://developer.apple.com/documentation/uikit/uikeyboardtype) — UIKit

## Registro de cambios

| Date | Changes |
|---|---|
| June 9, 2025 | Added guidance for displaying custom controls above the keyboard, and updated to reflect virtual keyboard availability in watchOS. |
| February 2, 2024 | Clarified the virtual keyboard’s support for direct and indirect gestures in visionOS. |
| December 5, 2023 | Added artwork for visionOS. |
| June 21, 2023 | Changed page title from Onscreen keyboards and updated to include guidance for visionOS. |
