# Notifications — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/notifications
- Descargado: 2026-10-15
- Sección: components › System experiences
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2023-10-24 — Updated watchOS platform considerations with guidance for presenting notification responses to double tap.

> Resumen de Apple: A notification gives people timely, high-value information they can understand at a glance.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Before you can send any notifications to people, you have to get their consent (for developer guidance, see [Asking permission to use…

### Anatomy

- Depending on the platform, a notification can use various styles, such as:
  - A banner or view on a Lock Screen, Home Screen, Home View, or desktop
  - A badge on an app icon
  - An item in Notification Center
- In addition, a notification related to direct communication — like a phone call or message — can provide an interface that’s distinct from noncommunication notifications,…

### Best practices

- **Provide concise, informative notifications.**
- **Avoid sending multiple notifications for the same thing, even if someone hasn’t responded.**
- **Avoid sending a notification that tells people to perform specific tasks within your app.**
- **Use an alert — not a notification — to display an error message.**
- **Handle notifications gracefully when your app is in the foreground.**
- **Avoid including sensitive, personal, or confidential information in a notification.**

### Content

- When a notification includes a title, the system displays it at the top where it’s most visible.
- **Create a short title if it provides context for the notification content.**
- **Write succinct, easy-to-read notification content.**
- **Provide generically descriptive text to display when notification previews aren’t available.**
- **Avoid including your app name or icon.**
- **Consider providing a sound to supplement your notifications.**

### Notification actions

- A notification can present a customizable detail view that contains up to four buttons people use to perform actions without opening your app.
- **Provide beneficial actions that make sense in the context of your notification.**
- **Avoid providing an action that merely opens your app.**
- **Prefer nondestructive actions.**
- **Provide a simple, recognizable interface icon for each notification action.**

### Badging

- A badge is a small, filled oval containing a number that can appear on an app icon to indicate the number of unread notifications that are available.
- **Use a badge only to show people how many unread notifications they have.**
- **Make sure badging isn’t the only method you use to communicate essential information.**
- **Keep badges up to date.**
- **Avoid creating a custom image or component that mimics the appearance or behavior of a badge.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.*

#### watchOS

- On Apple Watch, notifications occur in two stages: *short look* and *long look*.
- You can help people have a great notification experience by designing app-specific assets and actions that are relevant on Apple Watch.

##### Short looks

- A short look appears when the wearer’s wrist is raised and disappears when it’s lowered.
- **Avoid using a short look as the only way to communicate important information.**
- **Keep privacy in mind.**

##### Long looks

- Long looks provide more detail about a notification.
- A custom long-look interface can be static or dynamic.
- You can customize the content area for both static and dynamic long looks, but you can’t change the overall structure of the interface.
- **Consider using a rich, custom long-look notification to let people get the information they need without launching your app.**
- **At the minimum, provide a static interface; prefer providing a dynamic interface too.**
- **Choose a background appearance for the sash.**
- **Choose a background color for the content area.**
- **Provide up to four custom actions below the content area.**

##### Double tap

- People can double-tap to respond to notifications on supported devices.
- **Keep double tap in mind when choosing the order of custom actions you present as responses to a notification.**

## Recursos relacionados

- *Related:*
  - [Managing notifications](https://developer.apple.com/design/human-interface-guidelines/managing-notifications)
  - [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts)
- *Developer documentation:*
  - [Asking permission to use notifications](https://developer.apple.com/documentation/usernotifications/asking-permission-to-use-notifications) — User Notifications
  - [User Notifications UI](https://developer.apple.com/documentation/usernotificationsui)
  - [User Notifications](https://developer.apple.com/documentation/usernotifications)

## Vídeos que la explican

- [Send communication and Time Sensitive notifications](https://developer.apple.com/videos/play/wwdc2021/10091) → `references/videos/2021-10091.md`
- [The Push Notifications primer](https://developer.apple.com/videos/play/wwdc2020/10095) → `references/videos/2020-10095.md`

## Registro de cambios

| Date | Changes |
|---|---|
| October 24, 2023 | Updated watchOS platform considerations with guidance for presenting notification responses to double tap. |
