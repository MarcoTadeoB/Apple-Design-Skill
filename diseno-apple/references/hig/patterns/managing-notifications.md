# Managing notifications — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/managing-notifications
- Descargado: 2026-10-15
- Sección: patterns
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: sin registro de cambios

> Resumen de Apple: Notifications can give people timely and important information, whether the device is locked or in use.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- You need to get permission before sending any notification.

### Integrating with Focus

- People appreciate receiving a notification for something they care about, but they don’t always appreciate being interrupted.
  - A Focus helps people filter notifications during a time period they reserve for an activity like sleeping, working, reading, or driving.
  - Delivery scheduling lets people choose whether to receive notification alerts immediately or in a summary that’s delivered at times they choose.
- People identify the contacts and apps that can break through a Focus to deliver notification alerts.
> **Important:** Even though a Focus might delay the delivery of a notification alert, the notification itself is available as soon as it arrives.
- To support these behavior customizations, you first identify the types of notifications your app or game can send.
- You need to specify a system-defined interruption level for each noncommunication notification you send.
- The system defines four interruption levels for noncommunication notifications:
  - *Passive*. Information people can view at their leisure, like a restaurant recommendation.
  - *Active* (the default). Information people might appreciate knowing about when it arrives, like a score update on their favorite sports team.
  - *Time Sensitive*. Information that directly impacts the person and requires their immediate attention, like an account security issue or a package delivery.
  - *Critical*.
- Notification alerts in each system-defined interruption level can behave in the following ways:

| Interruption level | Overrides scheduled delivery | Breaks through Focus | Overrides Ring/Silent switch on iPhone and iPad |
|---|---|---|---|
| Passive | No | No | No |
| Active | No | No | No |
| Time Sensitive | Yes | Yes | No |
| Critical | Yes | Yes | Yes |

> **Note:** Because a Critical notification can override the Ring/Silent switch and break through scheduled delivery and Focus, you must get an entitlement to send one.

### Best practices

- **Build trust by accurately representing the urgency of each notification.**
- **Use the Time Sensitive interruption level only for notifications that are relevant in the moment.**

### Sending marketing notifications

- Don’t use notifications to send marketing or promotional content unless people explicitly agree to receive such information.
- **Never use the Time Sensitive interruption level to send a marketing notification.**
- **Get people’s permission if you want to send them promotional or marketing notifications.**
- **Make sure people can manage their notification settings within your app.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.*

#### watchOS

- By default, the notification settings people use for apps on their iPhone apply to the same apps on their Apple Watch.

## Recursos relacionados

- *Related:*
  - [Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy)
- *Developer documentation:*
  - [User Notifications](https://developer.apple.com/documentation/usernotifications)

## Vídeos que la explican

- [Send communication and Time Sensitive notifications](https://developer.apple.com/videos/play/wwdc2021/10091) → `references/videos/2021-10091.md`
- [The Push Notifications primer](https://developer.apple.com/videos/play/wwdc2020/10095) → `references/videos/2020-10095.md`
