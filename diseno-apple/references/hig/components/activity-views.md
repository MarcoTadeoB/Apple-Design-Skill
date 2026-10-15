# Activity views — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/activity-views
- Descargado: 2026-10-15
- Sección: components › Menus and actions
- Plataformas: ios,ipados,visionos
- Última actualización: sin registro de cambios

> Resumen de Apple: An activity view — often called a *share sheet* — presents a range of tasks that people can perform in the current context.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Activity views present sharing activities like messaging and actions like Copy and Print, in addition to quick access to frequently used apps.
- You can provide app-specific activities that can appear in a share sheet when people open it within your app or game.
- You can also create app extensions to provide custom share and action activities that people can use in other apps.

### Best practices

- **Avoid creating duplicate versions of common actions that are already available in the activity view.**
- **Consider using a symbol to represent your custom activity.**
- **Write a succinct, descriptive title for each custom action you provide.**
- **Make sure activities are appropriate for the current context.**
- **Use the Share button to display an activity view.**

### Share and action extensions

- Share extensions give people a convenient way to share information from the current context with apps, social media accounts, and other services.
- The system presents share and action extensions differently depending on the platform:
  - In iOS and iPadOS, share and action extensions are displayed in the share sheet that appears when people choose an Action button.
  - In macOS, people access share extensions by clicking a Share button in the toolbar or choosing Share in a context menu.
- **If necessary, create a custom interface that feels familiar to people.**
- **Streamline and limit interaction.**
- **Avoid placing a modal view above your extension.**
- **If necessary, provide an image that communicates the purpose of your extension.**
- **Use your main app to denote the progress of a lengthy operation.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, or visionOS.

## Recursos relacionados

- *Related:*
  - [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets)
  - [Popovers](https://developer.apple.com/design/human-interface-guidelines/popovers)
- *Developer documentation:*
  - [UIActivityViewController](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller) — UIKit
  - [UIActivity](https://developer.apple.com/documentation/uikit/uiactivity) — UIKit
  - [App Extension Support](https://developer.apple.com/documentation/foundation/app-extension-support) — Foundation

## Vídeos que la explican

- [Design for Collaboration with Messages](https://developer.apple.com/videos/play/wwdc2022/10015) → `references/videos/2022-10015.md`
