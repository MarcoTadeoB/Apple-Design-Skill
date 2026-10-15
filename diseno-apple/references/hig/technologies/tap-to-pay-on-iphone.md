# Tap to Pay on iPhone — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/tap-to-pay-on-iphone
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios
- Última actualización: 2024-01-17 — Updated merchant education guidance.

> Resumen de Apple: Tap to Pay on iPhone lets merchants accept contactless payments using an app on their iPhone, without having to connect external hardware.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- When you support Tap to Pay on iPhone in your iOS payment app, you help merchants present a consistent and trusted payment experience to their customers.
> **Note:** Tap to Pay on iPhone works alongside your existing payment-acceptance hardware and accessories.
- Before you can integrate Tap to Pay on iPhone into your iOS app, you need to work with a supported payment service provider (PSP), request the Tap to Pay on iPhone entitlement,…
> **Note:** If your PSP offers an SDK that supplies user interfaces for experiences like showing a tap result, see the documentation the PSP provides.

### Enabling Tap to Pay on iPhone

- Before your app can enable Tap to Pay on iPhone and configure a merchant’s device, the merchant must accept the relevant terms and conditions.
- **Help merchants accept Tap to Pay on iPhone terms and conditions before they begin interacting with their customers.**
- **Present Tap to Pay on iPhone terms and conditions only to an administrative user.**
- **If necessary, help merchants make sure their device is up to date.**

### Educating merchants

- Some merchants may be unfamiliar with Tap to Pay on iPhone, so it’s important to give them a quick and easy way to get started.
- **Provide a tutorial that describes the supported payment types and shows how to use Tap to Pay on iPhone to accept each type.**
  - Including it in a Learn More option in your in-app messaging
  - Automatically presenting it after merchants accept the Tap to Pay on iPhone terms and conditions
  - Automatically presenting it to new users of your app
  - Making it easy to find in a consistent place like your app’s help content or settings area
- You can build your app’s tutorial using Apple-approved assets from the [Tap to Pay on iPhone marketing guidelines](https://developer.apple.com/tap-to-pay/marketing-guidelines/),…
- If you design your own tutorial, make sure it shows how to:
  - Launch a checkout flow for each type of payment
  - Help a customer position their contactless card or digital wallet on the merchant’s device for payment
  - Handle PIN entry for a card, including accessibility mode
- Finally, provide an opportunity at the end of the tutorial for merchants who haven’t accepted the Tap to Pay on iPhone terms and conditions yet to do so.

### Checking out

- Checking out is a time-sensitive action, and merchants need the process to work smoothly.
  - Offer payment options in addition to Tap to Pay on iPhone, as necessary
  - Respond quickly if a merchant initiates checkout before enabling Tap to Pay on iPhone
  - Help merchants perform checkout even if device configuration is still in progress
  - Present pre-payment actions that affect the final total before checkout completes
- **Provide Tap to Pay on iPhone as a checkout option whether the feature is enabled or not.**
- **Avoid making merchants wait to use Tap to Pay on iPhone.**
- **Make sure the Tap to Pay on iPhone checkout option is available even if configuration is continuing in the background.**
- **If your app supports multiple payment-acceptance methods, make the Tap to Pay on iPhone button easy to find.**
- **Make it easy for merchants to switch between Tap to Pay on iPhone and the hardware accessories you support.**
- **For the label of the button that activates the feature, use “Tap to Pay on iPhone” or, if space is constrained, “Tap to Pay.”**
  - «The exception is if Tap to Pay on iPhone is the only payment-acceptance method you support.»
  - ✅ Ejemplo correcto: An illustration of a 'Tap to Pay' button containing an icon. The button correctly includes a wave symbol followed by the words 'Tap to Pay on iPhone'.
  - ❌ Ejemplo incorrecto: An illustration of a 'Tap to Pay' button containing an icon. The button incorrectly includes the Apple logo followed by the words 'Tap to Pay on iPhone'.
> **Important:** Use the “Tap to Pay on iPhone” label only for payment actions.
- **Design your Tap to Pay on iPhone button to match the other buttons in your app.**
- **Determine the final amount that customers need to pay before merchants initiate the Tap to Pay on iPhone experience.**
- **If you support pre-payment options in your checkout flow, display them before the Tap to Pay on iPhone screen.**

### Displaying results

- Customers pay by *tapping* — that is, bringing a contactless card or digital wallet near the Tap to Pay on iPhone screen in your app.
- **Start processing a transaction as soon as possible.**
- **Display a progress indicator while payment is authorizing before you show your transaction result screen.**
- **Clearly display the result of a transaction, whether it’s declined or successful.**
- **Help merchants complete the checkout flow when a payment can’t complete with Tap to Pay on iPhone.**
  - Present a new screen or reuse your checkout screen, letting merchants accept an alternate form of payment, like cash
  - Support checkout with a different method, like external hardware or a payment link
  - Relaunch Tap to Pay on iPhone, if a customer has another card they want to try
- After you receive payment card data, you might also encounter scenarios like the ones listed below.
  - Some regions require Strong Customer Authentication (SCA) support, which means that although the payment card might not require a card PIN during a tap, the bank that issues the…
  - In some regions your app may need to meet additional requirements to address the limitations of some cards, such as those in Offline PIN markets.
- **If the system returns an error that the merchant must address, display a clear description of the problem and recommend an appropriate resolution.**
- **Make it easy for merchants to get help with issues they can’t resolve.**

### Additional interactions

- Tap to Pay on iPhone lets merchants read a payment card when there’s no transaction amount to support use cases like looking up a past transaction, or retaining card information…
- **Use a generic label in a button that opens the Tap to Pay on iPhone screen to read a payment card when there’s no transaction amount.**
- When customers have other types of NFC-compatible cards or passes in Apple Wallet — such as loyalty, discount, and points cards — Tap to Pay on iPhone lets merchants read these…
- **If your app supports an independent loyalty card transaction, distinguish this flow from a payment-acceptance flow that uses Tap to Pay on iPhone.**
  - ✅ Ejemplo correcto: An illustration of a button labeled 'Loyalty Card'.
  - ❌ Ejemplo incorrecto: An illustration of a button labeled 'Tap to Pay on iPhone - Loyalty'.

### Platform considerations

- *No additional considerations for iOS.

## Recursos relacionados

- *Related:*
  - [Tap to Pay on iPhone Marketing guidelines](https://developer.apple.com/tap-to-pay/marketing-guidelines/)
- *Developer documentation:*
  - [Adding support for Tap to Pay on iPhone to your app](https://developer.apple.com/documentation/proximityreader/adding-support-for-tap-to-pay-on-iphone-to-your-app) — ProximityReader

## Registro de cambios

| Date | Changes |
|---|---|
| January 17, 2024 | Updated merchant education guidance. |
| May 7, 2024 | Updated to include guidance on enabling the feature and educating merchants. |
| March 3, 2023 | Enhanced guidance for educating merchants and improving their experience. |
| September 14, 2022 | Refined guidance on preparing Tap to Pay on iPhone and helping merchants learn how to use the feature. |
