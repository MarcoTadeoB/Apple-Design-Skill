# Spatial layout — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/spatial-layout
- Descargado: 2026-10-15
- Sección: foundations
- Plataformas: visionos
- Última actualización: 2024-03-29 — Emphasized the importance of keeping interactive elements from overlapping each other.

> Resumen de Apple: Spatial layout techniques help you take advantage of the infinite canvas of Apple Vision Pro and present your content in engaging, comfortable ways.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
### Field of view

- A person’s *field of view* is the space they can see without moving their head.
> **Important:** The system doesn’t provide information about a person’s field of view.
- **Center important content within the field of view.**
- **Avoid anchoring content to the wearer’s head.**

### Depth

- People rely on visual cues like distance, occlusion, and shadow to perceive depth and make sense of their surroundings.
- Because people can view your content from any angle, incorporating small amounts of depth throughout your interface — even in standard windows — can help it look more natural.
- If you need to present content with additional depth, you use RealityKit to create a 3D object (for developer guidance, see…
- **Provide visual cues that accurately communicate the depth of your content.**
- **Use depth to communicate hierarchy.**
- **In general, avoid adding depth to text.**
- **Make sure depth adds value.**

### Scale

- visionOS defines two types of scale to preserve the appearance of depth while optimizing usability.
- *Dynamic scale* helps content remain comfortably legible and interactive regardless of its proximity to people.
- *Fixed scale* means that an object maintains the same scale regardless of its proximity to people.
- To support dynamic scaling and the appearance of depth, visionOS defines a point as an angle, in contrast to other platforms, which define a point as a number of pixels that can…
- **Consider using fixed scale when you want a virtual object to look exactly like a physical object.**

### Best practices

- **Avoid displaying too many windows.**
- **Prioritize standard, indirect gestures.**
- **Rely on the Digital Crown to help people recenter windows in their field of view.**
- **Include enough space around interactive components to make them easy for people to look at.**
  - «For example, place multiple, regular-size [buttons](https://developer.apple.com/design/human-interface-guidelines/buttons#visionOS) so their centers are at least 60 points apart, leaving 16 points or more of space between them.»
- **Let people use your app with minimal or no physical movement.**
  - «Unless some physical movement is essential to your experience, help everyone enjoy it while remaining stationary.»
- **Use the floor to help you place a large immersive experience.**
- To learn more about windows and volumes in visionOS, see [Windows > visionOS](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS); for guidance on…

### Platform considerations

- *Not supported in iOS, iPadOS, macOS, tvOS, or watchOS.*

## Recursos relacionados

- *Related:*
  - [Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes)
  - [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
  - [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences)
- *Developer documentation:*
  - [Presenting windows and spaces](https://developer.apple.com/documentation/visionos/presenting-windows-and-spaces) — visionOS
  - [Positioning and sizing windows](https://developer.apple.com/documentation/visionos/positioning-and-sizing-windows) — visionOS
  - [Adding 3D content to your app](https://developer.apple.com/documentation/visionos/adding-3d-content-to-your-app) — visionOS

## Vídeos que la explican

- [Meet SwiftUI spatial layout](https://developer.apple.com/videos/play/wwdc2025/273) → `references/videos/2025-273.md`
- [Principles of spatial design](https://developer.apple.com/videos/play/wwdc2023/10072) → `references/videos/2023-10072.md`
- [Design for spatial user interfaces](https://developer.apple.com/videos/play/wwdc2023/10076) → `references/videos/2023-10076.md`

## Registro de cambios

| Date | Changes |
|---|---|
| March 29, 2024 | Emphasized the importance of keeping interactive elements from overlapping each other. |
| June 21, 2023 | New page. |
