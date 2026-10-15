# HealthKit — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/healthkit
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados,watchos
- Última actualización: sin registro de cambios

> Resumen de Apple: HealthKit is the central repository for health and fitness data in iOS, iPadOS, and watchOS.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- When you support HealthKit in your app, you can ask people for permission to access and update their health information.
> **Important:** If your app doesn’t provide health and fitness functionality, don’t request access to people’s private health data.
- For example, a nutrition app might ask for permission to retrieve people’s weight and activity data, so it can define calorie consumption goals and make dietary recommendations.
- For developer guidance, see [HealthKit](https://developer.apple.com/documentation/healthkit).

### Privacy protection

- You must request permission to access people’s data, and you must take all necessary steps to protect that data.
- **Provide a coherent privacy policy.**
- **Request access to health data only when you need it.**
- **Clarify your app’s intent by adding descriptive messages to the standard permission screen.**
- **Manage health data sharing solely through the system’s privacy settings.**

### Activity rings

- You can enhance your app’s health and wellness offerings by displaying the Activity ring element to show people’s progress toward their Move, Exercise, and Stand goals.
- **Use Activity rings for Move, Exercise, and Stand information only.**
- **Use Activity rings to show progress for a single person.**
- **Don’t use Activity rings for ornamentation.**
- **Don’t use Activity rings for branding.**
- **Maintain Activity ring and background colors.**
- **Maintain Activity ring margins.**
- **Differentiate other ring-like elements from Activity rings.**
- **Provide app-specific information only in Activity notifications.**
- For developer guidance, see [HKActivityRingView](https://developer.apple.com/documentation/healthkitui/hkactivityringview).

### Apple Health icon

- The Apple Health icon shows that an app works with HealthKit and the Health app.
- **Use only the Apple-provided icon.**
- **Display the name *Apple Health* close to the Apple Health icon.**
- **Display the Apple Health icon consistently with other health-related app icons.**
- **Don’t use the Apple Health icon as a button.**
- **Don’t alter the appearance of the Apple Health icon.**
- **Maintain a minimum clear space around the Apple Health icon of 1/10 of its height.**
- **Don’t use the Apple Health icon within text or as a replacement for the terms *Health*, *Apple Health*, or *HealthKit*.**
- **Don’t display Health app images or screenshots.**

### Editorial guidelines

- **Refer to the Health app as *Apple Health* or *the Apple Health app*.**
- **Don’t use the term *HealthKit*.**
- **Use correct capitalization when using the term *Apple Health*.**
- **Use the system-provided translation of *Health* to avoid confusing people.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, or watchOS.

## Recursos relacionados

- *Related:*
  - [Works with Apple Health](https://developer.apple.com/health-fitness/works-with-apple-health/)
  - [Activity rings](https://developer.apple.com/design/human-interface-guidelines/activity-rings)
  - [Apple Design Resources](https://developer.apple.com/design/resources/#technologies)
- *Developer documentation:*
  - [HealthKit](https://developer.apple.com/documentation/healthkit)
  - [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) — HealthKit

## Vídeos que la explican

- [Deliver workout insights with HealthKit workout zones](https://developer.apple.com/videos/play/wwdc2026/207) → `references/videos/2026-207.md`
- [Meet the HealthKit Medications API](https://developer.apple.com/videos/play/wwdc2025/321) → `references/videos/2025-321.md`
- [Track workouts with HealthKit on iOS and iPadOS](https://developer.apple.com/videos/play/wwdc2025/322) → `references/videos/2025-322.md`
