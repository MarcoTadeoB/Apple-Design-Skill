# Apple Pencil and Scribble — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble
- Descargado: 2026-10-15
- Sección: inputs
- Plataformas: ipados
- Última actualización: 2024-05-07 — Added guidance for handling squeeze and barrel roll on Apple Pencil Pro.

> Resumen de Apple: Apple Pencil helps make drawing, handwriting, and marking effortless and natural, in addition to performing well as a pointer and UI interaction tool.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Apple Pencil is a versatile, intuitive tool for iPad apps that offers pixel‑level precision when jotting notes, sketching, painting, marking up documents, and more.
- For details on Apple Pencil features and compatibility, see [Apple Pencil](https://www.apple.com/apple-pencil/).

### Best practices

- **Support behaviors people intuitively expect when using a marking instrument.**
- **Let people choose when to switch between Apple Pencil and finger input.**
- **Let people make a mark the moment Apple Pencil touches the screen**
- **Help people express themselves by responding to the way they use Apple Pencil.**
- (imagen) An illustration of Apple Pencil tilted up from a horizontal line by 45 degrees.
- **Provide visual feedback to indicate a direct connection with content.**
- **Design a great left- and right-handed experience.**

### Hover

- **Use hover to help people predict what will happen when Apple Pencil touches the screen.**
- **Avoid using hover to initiate an action.**
- **Prefer showing a preview value that’s near the middle in a range of dynamic values.**
  - ❌ Ejemplo incorrecto: An illustration of Apple Pencil hovering slightly above a gray rectangle that represents the screen. A small blue oval beneath the tip represents a preview.
  - ✅ Ejemplo correcto: An illustration of Apple Pencil hovering slightly above a gray rectangle that represents the screen. A medium blue oval beneath the tip represents a preview.
  - ❌ Ejemplo incorrecto: An illustration of Apple Pencil hovering slightly above a gray rectangle that represents the screen. A large blue oval beneath the tip represents a preview.
- **Consider using hover to support relevant interactions close to where people are marking.**
- **Prefer showing hover previews for Apple Pencil, not for a pointing device.**

### Double tap

- **Respect people’s settings for the double-tap gesture when they make sense in your app.**
- **Give people a way to specify custom double-tap behavior if necessary.**
- **Avoid using the double-tap gesture to perform an action that modifies content.**

### Squeeze

- Using Apple Pencil Pro, people can squeeze to perform an action.
> **Note:** The squeeze gesture is available only when the paired iPad screen is on and while the Apple Pencil Pro is not directly contacting it.
- **Treat squeeze as a single, quick gesture that performs a discrete — not continuous — action.**
- **If you use squeeze to reveal app UI, like a contextual menu, display it close to Apple Pencil Pro.**
- **Define squeeze actions that are nondestructive and easy to undo.**

### Barrel roll

- While marking with Apple Pencil Pro, people can use a barrel-roll gesture to change the type of mark they’re making.
- **Use barrel roll only to modify marking behavior, not to enable navigation or display other controls.**

### Scribble

- With Scribble and Apple Pencil, people can simply write wherever text is accepted in your app — they don’t have to tap or switch modes first.
- **Make text entry feel fluid and effortless.**
  - «By default, Scribble works in all standard text components — such as text fields, text views, search fields, and editable fields in web content — except password fields.»
- **Make Scribble available everywhere people might want to enter text.**
- **Avoid distracting people while they write.**
- **While people are writing in a text field, make sure it remains stationary.**
- **Prevent autoscrolling text while people are writing and editing in a text field.**
- **Give people enough space to write.**

### Custom drawing

- Using [PencilKit](https://developer.apple.com/documentation/pencilkit), you can let people take notes, annotate documents and images, and draw with the same low-latency…
- **Help people draw on top of existing content.**
- **Consider displaying custom undo and redo buttons when your app runs in a compact environment.**

### Platform considerations

- *Not supported in iOS, macOS, tvOS, visionOS, or watchOS.*

## Recursos relacionados

- *Related:*
  - [Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data)
- *Developer documentation:*
  - [PencilKit](https://developer.apple.com/documentation/pencilkit)
  - [PaperKit](https://developer.apple.com/documentation/paperkit)

## Vídeos que la explican

- [Read between the strokes with PencilKit](https://developer.apple.com/videos/play/wwdc2026/203) → `references/videos/2026-203.md`
- [Unwrap PaperKit](https://developer.apple.com/videos/play/wwdc2026/372) → `references/videos/2026-372.md`
- [Meet PaperKit](https://developer.apple.com/videos/play/wwdc2025/285) → `references/videos/2025-285.md`

## Registro de cambios

| Date | Changes |
|---|---|
| May 7, 2024 | Added guidance for handling squeeze and barrel roll on Apple Pencil Pro. |
| September 12, 2023 | Updated artwork. |
| November 3, 2022 | Added guidelines for using hover to enhance your app. |
