# Managing accounts — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/managing-accounts
- Descargado: 2026-10-15
- Sección: patterns
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: sin registro de cambios

> Resumen de Apple: When it doesn’t create an unnecessary barrier to your experience, an account can be a convenient way for people to access their content and track personal details.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Ask people to create an account only if your core functionality requires it; otherwise, let people enjoy your app or game without one.

### Best practices

- **Explain the benefits of creating an account and how to sign up.**
- **Delay sign-in for as long as possible.**
- **If you don’t use Sign in with Apple in your iOS, iPadOS, macOS, or visionOS app, prefer using a passkey.**
- **Always identify the authentication method you offer.**
- **Refer only to authentication methods that are available in the current context.**
- **In general, avoid offering an app-specific setting for opting in to biometric authentication.**
- **Avoid using the term *passcode* to refer to account authentication.**

### Deleting accounts

- If you help people create an account within your app or game, you must also help them delete it, not just deactivate it.
> **Important:** If legal requirements compel your app to maintain accounts or information — such as digital health records — or to follow a specific account-deletion process, clearly describe the situation so people can understand the information or…
- **Provide a clear way to initiate account deletion within your app or game.**
> **Developer note:** If people used [Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple) to create an account within your app, you revoke the associated tokens when they delete their account.
- **Provide a consistent account-deletion experience whether people perform it within your app or game or on the website.**
- **Consider letting people schedule account deletion to occur in the future.**
- **Tell people when account deletion will complete, and notify them when it’s finished.**
- **If you support in-app purchases, help people understand how billing and cancellation work when they delete their account.**
  - Billing for an auto-renewable subscription continues through Apple until people cancel the subscription, regardless of whether they delete their account.
  - After they delete their account, people need to cancel their subscription or request a refund.
- In addition to helping people understand these scenarios, provide information that describes how to cancel subscriptions and manage purchases.
> **Note:** Even if people didn’t use your app to purchase the subscription, you still need to support account deletion.

### TV provider accounts

- Many popular TV providers let people sign in to their accounts at the system level, eliminating the need to authenticate on an app-by-app basis.
- **Avoid displaying a sign-out option when people are signed in at the system level.**
- **Never instruct people to sign out by adjusting privacy controls.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, or visionOS.*

#### tvOS

- Most people interact with Apple TV using a remote, not a keyboard, so ask for the minimum amount of information necessary.
- **Prefer letting people use another device to sign up or authenticate.**
- **When people are signed in to a shared account, avoid asking them to choose their profile every time they become the current user.**
- **Minimize data entry.**

#### watchOS

- Use iCloud synchronization to provide access to the Keychain, letting people autofill user names and passwords and preserve app settings.

## Recursos relacionados

- *Related:*
  - [Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding)
  - [Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple)
- *Developer documentation:*
  - [Supporting passkeys](https://developer.apple.com/documentation/authenticationservices/supporting-passkeys) — Authentication Services

## Vídeos que la explican

- [What’s new in passkeys](https://developer.apple.com/videos/play/wwdc2025/279) → `references/videos/2025-279.md`
- [What’s new in device management](https://developer.apple.com/videos/play/wwdc2024/10143) → `references/videos/2024-10143.md`
