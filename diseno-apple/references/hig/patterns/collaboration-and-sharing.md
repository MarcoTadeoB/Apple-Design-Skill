# Collaboration and sharing — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing
- Descargado: 2026-10-15
- Sección: patterns
- Plataformas: ios,ipados,macos,visionos,watchos
- Última actualización: 2023-12-05 — Added artwork illustrating button placement and various types of collaboration permissions.

> Resumen de Apple: Great collaboration and sharing experiences are simple and responsive, letting people engage with the content while communicating effectively with others.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- System interfaces and the Messages app can help you provide consistent and convenient ways for people to collaborate and share.
- After a collaboration begins, people can use the Collaboration button in your app to communicate with others, perform custom actions, and manage details.
- You can take advantage of Messages integration and the system-provided sharing interfaces whether you implement collaboration and sharing through CloudKit, iCloud Drive, or a…
- With SharePlay, people can also take part in your app’s activities together in real time, from their own devices.

### Best practices

- **Place the Share button in a convenient location, like a toolbar, to make it easy for people to start sharing or collaborating.**
- **If necessary, customize the share sheet or sharing popover to offer the types of file sharing your app supports.**
- **Write succinct phrases that summarize the sharing permissions you support.**
- **Provide a set of simple sharing options that streamline collaboration setup.**
- **Prominently display the Collaboration button as soon as collaboration starts.**
- **Provide custom actions in the collaboration popover only if needed.**
- **If it makes sense in your app, customize the title of the modal view’s collaboration-management button.**
- **Consider posting collaboration event notifications in Messages.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, or macOS.

#### visionOS

- By default, the system supports screen sharing for an app running in the Shared Space by streaming the current window to other collaborators.

#### watchOS

- In your SwiftUI app running in watchOS, use [ShareLink](https://developer.apple.com/documentation/swiftui/sharelink) to present the system-provided share sheet.

## Recursos relacionados

- *Related:*
  - [Activity views](https://developer.apple.com/design/human-interface-guidelines/activity-views)
- *Developer documentation:*
  - [Shared with You](https://developer.apple.com/documentation/sharedwithyou)
  - [ShareLink](https://developer.apple.com/documentation/swiftui/sharelink) — SwiftUI

## Vídeos que la explican

- [Design for Collaboration with Messages](https://developer.apple.com/videos/play/wwdc2022/10015) → `references/videos/2022-10015.md`
- [Enhance collaboration experiences with Messages](https://developer.apple.com/videos/play/wwdc2022/10095) → `references/videos/2022-10095.md`
- [Integrate your custom collaboration app with Messages](https://developer.apple.com/videos/play/wwdc2022/10093) → `references/videos/2022-10093.md`

## Registro de cambios

| Date | Changes |
|---|---|
| December 5, 2023 | Added artwork illustrating button placement and various types of collaboration permissions. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | New page. |
