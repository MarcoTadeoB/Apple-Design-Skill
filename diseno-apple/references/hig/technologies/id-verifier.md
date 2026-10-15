# ID Verifier — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/id-verifier
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios
- Última actualización: 2023-09-12 — New page.

> Resumen de Apple: ID Verifier lets your iPhone app read mobile IDs in person without requiring external hardware.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Beginning in iOS 17, you can integrate ID Verifier into your app, letting iPhone read ISO18013-5 compliant mobile IDs and helping you support in-person ID verification.
- Using ID Verifier has advantages for both customers and organizations.
  - Customers only present the minimum data needed to prove their age or identity, without handing over their ID card or showing their device.
  - Apple provides the key components of the certificate issuance, management, and validation process, simplifying app development and enabling a consistent and trusted ID…
- Depending on the needs of your app, you can use ID Verifier to make the following types of requests:
  - **Display Only request.** Use a Display Only request to display data — such as a person’s name or age alongside their photo portrait — within system-provided UI on the…
  - **Data Transfer request.** Use a Data Transfer request only when you have a legal verification requirement and you need to store or process information like a person’s address or…

### Best practices

- **Ask only for the data you need.**
- **If your app qualifies for Apple Business Register, register for ID Verifier to ensure that people can view essential information about your organization when you make a request.**
- **Provide a button that initiates the verification process.**

| Button type | Example usage |
|---|---|
| ![An illustration of a Verify Age button.](https://developer.apple.com/images/com.apple.HIG/id-verifier-button-age@2x.png) | An app that checks whether people are old enough to attend an event or access a venue, like a concert hall. |
| ![An illustration of a Verify Identity button.](https://developer.apple.com/images/com.apple.HIG/id-verifier-button-identity@2x.png) | An app that verifies whether specific identity information matches expected values, such as name and birth date when picking up a rental car. |

- **In a Display Only request, help the person using your app provide feedback on the visual confirmation they perform.**

### Platform considerations

- *No additional considerations for iOS.

## Recursos relacionados

- *Related:*
  - [Apple Business Register](https://register.apple.com/services/login?returnTo=/signin/tap-to-present-id-on-iphone)
  - [IDs in Wallet](https://learn.wallet.apple/id)
  - [Identity verification](https://developer.apple.com/design/human-interface-guidelines/wallet#Identity-verification)
- *Developer documentation:*
  - [Adopting the Verifier API in your iPhone app](https://developer.apple.com/documentation/proximityreader/adopting-the-verifier-api-in-your-iphone-app) — ProximityReader

## Vídeos que la explican

- [What’s new in Wallet and Apple Pay](https://developer.apple.com/videos/play/wwdc2023/10114) → `references/videos/2023-10114.md`

## Registro de cambios

| Date | Changes |
|---|---|
| September 12, 2023 | New page. |
