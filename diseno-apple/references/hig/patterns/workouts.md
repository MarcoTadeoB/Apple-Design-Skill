# Workouts — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/workouts
- Descargado: 2026-10-15
- Sección: patterns
- Plataformas: ios,ipados,watchos
- Última actualización: sin registro de cambios

> Resumen de Apple: A great workout or fitness experience encourages people to engage with their current activity and helps them track their progress on their devices.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- People can wear their Apple Watch during many types of workouts, and they might carry their iPhone or iPad during fitness activities like walking, wheelchair pushing, and running.
- You can create a workout experience for Apple Watch, iPhone, or iPad that helps people reach their goals by leveraging activity data from the device and using familiar components…

### Best practices

- **In a watchOS fitness app, use workout sessions to provide useful data and relevant controls.**
- **Avoid distracting people from a workout with information that’s not relevant.**
- **Use a distinct visual appearance to indicate an active workout.**
- **Provide workout controls that are easy to find and tap.**
- **Help people understand the health information your app records if sensor data is unavailable during a workout.**

|  | Example text from the Workout app |  |  |
|---|---|---|---|
| ✅ (correcto) | GPS is not used during a Pool Swim, and water may prevent a heart-rate measurement, but Apple Watch will still track your calories, laps, and distance using the built-in accelerometer. |  |  |
| ✅ (correcto) | In this type of workout, you earn the calorie equivalent of a brisk walk anytime sensor readings are unavailable. |  |  |
| ✅ (correcto) | GPS will only provide distance when you do a freestyle stroke. Water might prevent a heart-rate measurement, but calories will still be tracked using the built-in accelerometer. |  |  |

- **Provide a summary at the end of a session.**
- **Discard extremely brief workout sessions.**
- **Make sure text is legible for when people are in motion.**
- **Use Activity rings correctly.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, or watchOS.

## Recursos relacionados

- *Related:*
  - [Activity rings](https://developer.apple.com/design/human-interface-guidelines/activity-rings)
- *Developer documentation:*
  - [WorkoutKit](https://developer.apple.com/documentation/workoutkit)
  - [Workouts and activity rings](https://developer.apple.com/documentation/healthkit/workouts-and-activity-rings) — HealthKit

## Vídeos que la explican

- [Track workouts with HealthKit on iOS and iPadOS](https://developer.apple.com/videos/play/wwdc2025/322) → `references/videos/2025-322.md`
- [Build custom workouts with WorkoutKit](https://developer.apple.com/videos/play/wwdc2023/10016) → `references/videos/2023-10016.md`
- [Build a workout app for Apple Watch](https://developer.apple.com/videos/play/wwdc2021/10009) → `references/videos/2021-10009.md`
