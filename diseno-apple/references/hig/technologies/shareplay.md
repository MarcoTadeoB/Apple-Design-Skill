# SharePlay — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/shareplay
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados,macos,tvos,visionos
- Última actualización: 2026-09-09 — Reorganized best practices, expanded visionOS guidance, and added a section on custom templates.

> Resumen de Apple: SharePlay lets people experience activities together from anywhere, whether they’re watching a movie, playing a game, or sketching on a whiteboard.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- With SharePlay, people take part in your app’s activities together, from their own devices, even when they aren’t in the same room.
- An activity can start in different ways: from a control in your app, from a FaceTime call, or from a shared link.
> **Note:** If your activity involves content people buy or subscribe to, each participant needs their own copy or subscription.

### Best practices

- **Use SharePlay for real-time experiences.**
- **Design an experience that best fits what people are doing together.**
- **Design activities that work across Apple platforms.**
- **Make it easy to start a shared activity.**
- **Let people join an activity without friction.**
- **Describe activities clearly and concisely.**
- **Keep people oriented as an activity changes.**
- **Use the term *SharePlay* correctly.**

### Platform considerations

- *No additional considerations for tvOS.

#### iOS, iPadOS, macOS

- **Support Picture in Picture for shared video.**

#### visionOS

- In visionOS, SharePlay brings an extra level of presence to shared activities, whether people are collaborating in the same room, playing a game with distant friends, or catching…

##### Designing shared activities

- When people join a shared activity, the system creates a *shared context* so everyone experiences your content in the same relative location.
- **Prefer starting your experience from a window.**
- **Resolve conflicts naturally.**
- **Reserve unique views for moments that call for them.**
- **Let people opt in to immersion changes when they’re mid-task.**
- **Let participants customize their experience for personal comfort and accessibility needs.**
- **Make it easy to leave and rejoin.**

##### Personas

- In a shared activity, how someone appears depends on their device and location.
- **Support people who aren’t represented by a spatial Persona.**
- For developer guidance, see [Adding spatial Persona support to an…

##### Spatial templates

- A *spatial template* automatically arranges participants around your content in a way that suits what they’re doing together.
- The *side-by-side template* is ideal for viewing or watching content together.
- The *surround template* is ideal for tabletop games and other centralized experiences.
- The *conversational template* also groups participants around a center point, but places your content along the edge of the circle rather than at its center.
- **Divide a complex activity into stages.**
- **Let people initiate template transitions.**
- **Keep template transitions smooth.**

##### Custom templates

- If none of the system templates suit your activity, you can create a custom template that defines your own seat arrangement.
- **Account for people who are physically together.**
- **Provide the best seat orientation for your content.**
- **Support the maximum number of seats.**
- **Place seats at least a meter apart.**
- **Define the order in which people take seats.**
- **Keep roles independent of seats.**

## Recursos relacionados

- *Developer documentation:*
  - [Group Activities](https://developer.apple.com/documentation/groupactivities)

## Vídeos que la explican

- [Share visionOS experiences with nearby people](https://developer.apple.com/videos/play/wwdc2025/318) → `references/videos/2025-318.md`
- [Design spatial SharePlay experiences](https://developer.apple.com/videos/play/wwdc2023/10075) → `references/videos/2023-10075.md`
- [Add SharePlay to your app](https://developer.apple.com/videos/play/wwdc2023/10239) → `references/videos/2023-10239.md`

## Registro de cambios

| Date | Changes |
|---|---|
| September 9, 2026 | Reorganized best practices, expanded visionOS guidance, and added a section on custom templates. |
| December 5, 2023 | Added artwork for visionOS. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| December 19, 2022 | Clarified guidance for helping nonsubscribers join a group activity. |
