# Apple In-App Purchase — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2026-09-17 — Rebranded as Apple In-App Purchase and refined guidance to reflect current best practices.

> Resumen de Apple: People can use Apple In-App Purchase to pay for digital goods and services, like premium content and subscriptions, securely within your app.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- You can also promote and offer your Apple In-App Purchase items directly through the App Store.
> **Tip:** Apple In-App Purchase and [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay) are different technologies that support different use cases.
- Apple In-App Purchase supports four types of content:
  - *Consumable* content like lives or gems in a game. After purchase, consumable content depletes as people use it, and people can purchase it again.
  - *Non-consumable* content like premium features in an app. Purchased non-consumable content doesn’t expire.
  - *Auto-renewable subscriptions* to virtual content, services, and premium features in your app on an ongoing basis.
  - *Non-renewing subscriptions* to a service or content that lasts for a limited time, like access to an in-game battle pass.
- For marketing and business guidance, see [Apple In-App Purchase](https://developer.apple.com/in-app-purchase/) and [Auto-renewable…
> **Note:** For apps with exceptionally large, frequently updated catalogs of one-time purchases or subscription content from multiple creators, or apps that provide subscriptions with optional add-on content as a single purchase within the app, the…

### Best practices

- **Let people experience your app before making a purchase.**
- **Design an integrated shopping experience.**
- **Use simple, succinct product names and descriptions.**
- **Display the total billing price for each in-app purchase you offer, regardless of type.**
- **Display your store only when people can make payments.**
- **Use the default confirmation sheet.**

#### Supporting Family Sharing

- People can use Family Sharing to share access to their purchased content, such as auto-renewable subscriptions and non-consumable in-app purchases, with up to five additional…
- **Prominently mention Family Sharing in places where people learn about the content you offer.**
- **Help people understand the benefits of Family Sharing and how to participate.**
- **Aim to customize your in-app messaging so that it makes sense to both purchasers and family members.**

#### Providing help

- Sometimes, people need help with a purchase or want to request a refund.
- **Provide help that customers can view before they request a refund.**
- **Use a simple title for the refund action, like “Refund” or “Request a Refund”.**
- **Help people find the problematic purchase.**
- **Consider offering alternative solutions.**
- **Make it easy for people to request a refund.**
- **Avoid characterizing or providing guidance on Apple’s refund policies.**

### Auto-renewable subscriptions

- **Call attention to subscription benefits during onboarding.**
- **Offer a range of content choices, service levels, and durations.**
- **Consider letting people try your content for free before signing up.**
- **Prompt people to subscribe at relevant times, like when they near their monthly limit of free content.**
- **Encourage a new subscription only when someone isn’t already a subscriber.**

#### Making signup effortless

- A simple and informative sign-up experience makes it easy for people to act on their interest in your content, whether they’re in your app or viewing your App Store product page.
- **Provide clear, distinguishable subscription options.**
- **Simplify initial signup by asking only for necessary information.**
- **In your tvOS app, help people sign up or authenticate using another device.**
- **Give people more information in your app’s sign-up screen.**
  - The subscription name, duration, and the content or services provided during each subscription period
  - The billing amount, correctly localized for the territories and currencies where the subscription is available for purchase
  - A way for existing subscribers to sign in or restore purchases
- For example, the Forest Explorer sign-up screen displays billing totals for monthly, biannual, and annual subscriptions in the most prominent positions.
- **Clearly describe how a free trial works.**
- **Include a sign-up opportunity in your app’s settings.**

#### Supporting offer codes

- In iOS and iPadOS, subscription offer codes let you use both online and offline channels to give new, existing, and lapsed subscribers free or discounted access to your…
- There are two types of offer codes you can support:
  - A *one-time use code* is a unique code you generate in App Store Connect.
  - A *custom code* is a code you create, such as NEWYEAR or SPRINGSALE.
- For developer guidance on implementing offer codes, see [Offer codes](https://developer.apple.com/app-store/subscriptions/#offer-codes) and [Set up offer…
- **Clearly explain offer details.**
- **Follow guidelines for creating a custom code.**
- **Tell people how to redeem a custom code.**
- **Consider supporting offer redemption within your app.**
- After people tap your custom redeem button, the system automatically provides a series of code-redemption screens like the ones shown below.
- **Supply an engaging and informative promotional image.**
- **Help people benefit from unlocked content as soon as they complete the redemption flow.**

#### Helping people manage their subscriptions

- Supporting subscription management means people can upgrade, downgrade, or cancel a subscription without leaving your app.
- **Provide summaries of the customer’s subscriptions.**
- **Consider using the system-provided subscription-management UI.**
- **Encourage a subscriber to keep their subscription or resubscribe later.**
- **Always make it easy for customers to cancel an auto-renewable subscription.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.*

#### watchOS

- The sign-up screen in your watchOS app needs to display the same set of information about your subscription options that you display in other versions of your app.
- **Clearly describe the differences between versions of your app that run on different devices.**
- **Consider using a modal sheet to display the required information.**
- **Make subscription options easy to compare on a small screen.**
  - Display each option in a separate button.
  - Display a list of options, followed by a button people tap to start the signup process.

## Recursos relacionados

- *Related:*
  - [Apple In-App Purchase](https://developer.apple.com/in-app-purchase/)
  - [Offering Subscriptions](https://developer.apple.com/app-store/subscriptions/)
  - [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- *Developer documentation:*
  - [Apple In-App Purchase](https://developer.apple.com/documentation/storekit/in-app-purchase) — StoreKit

## Vídeos que la explican

- [What’s new in Apple In-App Purchase](https://developer.apple.com/videos/play/wwdc2026/210) → `references/videos/2026-210.md`

## Registro de cambios

| Date | Changes |
|---|---|
| September 17, 2026 | Rebranded as Apple In-App Purchase and refined guidance to reflect current best practices. |
| September 12, 2023 | Updated artwork and guidance for redeeming offer codes. |
| November 3, 2022 | Added a guideline for displaying the total billing price for every in-app purchase item and consolidated guidance into one page. |
