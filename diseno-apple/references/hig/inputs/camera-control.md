# Camera Control — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/camera-control
- Descargado: 2026-10-15
- Sección: inputs
- Plataformas: ios
- Última actualización: 2024-09-09 — New page.

> Resumen de Apple: The Camera Control provides direct access to your app’s camera experience.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- On iPhone 16 and iPhone 16 Pro models, the Camera Control quickly opens your app’s camera experience to capture moments as they happen.
- The overlay allows people to quickly adjust controls.

### Anatomy

- The Camera Control offers two types of controls for adjusting values or changing between options:
  - A *slider* provides a range of values to choose from, such as how much contrast to apply to the content.
  - A *picker* offers discrete options, such as turning a grid on and off in the viewfinder.
- In addition to custom controls that you create, the system provides a set of standard controls that you can optionally include in the overlay to allow someone to adjust their…

### Best practices

- **Use SF Symbols to represent control functionality.**
- **Keep names of controls short.**
- **Include units or symbols with slider control values to provide context.**
  - ✅ Ejemplo correcto: A partial screenshot showing an example of the Camera Control overlay with a slider control displaying a value and context for the type of value.
  - ❌ Ejemplo incorrecto: A partial screenshot showing an example of the Camera Control overlay with a slider control displaying a value without information about what the value represents.
- **Define prominent values for a slider control.**
- **Make space for the overlay in the viewfinder.**
- **Minimize distractions in the viewfinder.**
  - ✅ Ejemplo correcto: A partial screenshot showing an example of the Camera Control overlay with UI elements removed from the capture viewport.
  - ❌ Ejemplo incorrecto: A partial screenshot showing an example of the Camera Control overlay with UI elements duplicated in the capture viewport.
- **Enable or disable controls depending on the camera mode.**
- **Consider how to arrange your controls.**
- **Allow people to use the Camera Control to launch your experience from anywhere.**

### Platform considerations

- *Not supported in iPadOS, macOS, watchOS, tvOS, or visionOS.*

## Recursos relacionados

- *Related:*
  - [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols)
  - [Controls](https://developer.apple.com/design/human-interface-guidelines/controls)
- *Developer documentation:*
  - [Enhancing your app experience with the Camera Control](https://developer.apple.com/documentation/avfoundation/enhancing-your-app-experience-with-the-camera-control) — AVFoundation
  - [AVCaptureControl](https://developer.apple.com/documentation/avfoundation/avcapturecontrol) — AVFoundation
  - [LockedCameraCapture](https://developer.apple.com/documentation/lockedcameracapture)

## Registro de cambios

| Date | Changes |
|---|---|
| September 9, 2024 | New page. |
