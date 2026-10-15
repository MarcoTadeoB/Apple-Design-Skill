# Activity rings — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/activity-rings
- Descargado: 2026-10-15
- Sección: components › Status
- Plataformas: ios,ipados,watchos
- Última actualización: 2024-03-29 — Enhanced guidance for displaying Activity rings and listed specific colors for displaying related content.

> Resumen de Apple: Activity rings show an individual’s daily progress toward Move, Exercise, and Stand goals.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- In watchOS, the Activity ring element always contains three rings, whose colors and meanings match those the Activity app provides.

### Best practices

- **Display Activity rings when they’re relevant to the purpose of your app.**
- **Use Activity rings only to show Move, Exercise, and Stand information.**
- **Use Activity rings to show progress for a single person.**
- **Always keep the visual appearance of Activity rings the same, regardless of where you display them.**
  - Never change the colors of the rings; for example, don’t use filters or modify opacity.
  - Always display Activity rings on a black background.
  - Prefer enclosing the rings and background within a circle. To do this, adjust the corner radius of the enclosing view rather than applying a circular mask.
  - Ensure that the black background remains visible around the outermost ring.
  - Always scale the rings appropriately so they don’t seem disconnected or out of place.
  - When necessary, design the surrounding interface to blend with the rings; never change the rings to blend with the surrounding interface.
- **To display a label or value that’s directly associated with an Activity ring, use the colors that match it.**

| Move | Exercise | Stand |
|---|---|---|
| ![R-250,G-17,B-79](https://developer.apple.com/images/com.apple.HIG/activity-rings-color-swatch-red@2x.png) | ![R-166,G-255,B-0](https://developer.apple.com/images/com.apple.HIG/activity-rings-color-swatch-green@2x.png) | ![R-0,G-255,B-246](https://developer.apple.com/images/com.apple.HIG/activity-rings-color-swatch-blue@2x.png) |

- **Maintain Activity ring margins.**
- **Differentiate other ring-like elements from Activity rings.**
- **Don’t send notifications that repeat the same information the Activity app sends.**
- **Don’t use Activity rings for decoration.**
- **Don’t use Activity rings for branding.**

### Platform considerations

- *No additional considerations for iPadOS or watchOS.

#### iOS

- Activity rings are available in iOS with [HKActivityRingView](https://developer.apple.com/documentation/healthkitui/hkactivityringview).
  - With an Apple Watch paired, iOS shows all three Activity rings.
  - Without an Apple Watch paired, iOS shows the Move ring only, which represents an approximation of a person’s activity based on their steps and workout information from other apps.
- Because iOS shows Activity rings whether or not an Apple Watch is paired, activity history can include a combination of both styles.

## Recursos relacionados

- *Related:*
  - [Workouts](https://developer.apple.com/design/human-interface-guidelines/workouts)
- *Developer documentation:*
  - [HKActivityRingView](https://developer.apple.com/documentation/healthkitui/hkactivityringview) — HealthKit

## Vídeos que la explican

- [Track workouts with HealthKit on iOS and iPadOS](https://developer.apple.com/videos/play/wwdc2025/322) → `references/videos/2025-322.md`
- [Build a workout app for Apple Watch](https://developer.apple.com/videos/play/wwdc2021/10009) → `references/videos/2021-10009.md`
- [Build custom workouts with WorkoutKit](https://developer.apple.com/videos/play/wwdc2023/10016) → `references/videos/2023-10016.md`

## Registro de cambios

| Date | Changes |
|---|---|
| March 29, 2024 | Enhanced guidance for displaying Activity rings and listed specific colors for displaying related content. |
| December 5, 2023 | Added artwork representing Activity rings in iOS. |
