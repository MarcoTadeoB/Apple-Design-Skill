# Apple Pay — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/apple-pay
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados,macos,visionos,watchos
- Última actualización: 2026-06-08 — Refined guidance to reflect the latest Apple Pay appearance and capabilities.

> Resumen de Apple: Apple Pay is a secure, easy way to make payments for physical goods and services, donations, and subscriptions in apps and in any browser.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Use Apple Pay to sell physical goods like groceries, clothing, and appliances; for services such as club memberships, hotel reservations, and event tickets; and for donations.
- During checkout, the payment sheet can show the credit or debit card linked to Apple Pay, purchase amount (including tax and fees), shipping options, contact information, and…
- People pay using Face ID, Touch ID, or Optic ID on supported devices, or by double-clicking on Apple Watch.
- For developer guidance, see [Apple Pay](https://developer.apple.com/documentation/passkit/apple-pay) and [Apple Pay on the…
> **Note:** Use [Apple In-App Purchase](https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase) to sell virtual goods in your app, such as premium content, and subscriptions for digital content.

### Offering Apple Pay

- **Offer Apple Pay on all devices and browsers that support it.**
- **Make Apple Pay the primary payment option when credentials are available.**
- **Use Apple Pay buttons only to initiate payment or, when appropriate, the Apple Pay setup process.**
- **If you use a custom button to start the Apple Pay payment process, make sure your custom button doesn’t display “Apple Pay” or the Apple Pay logo.**
  - ✅ Ejemplo correcto: An illustration that shows the correct arrangement of the Apple Pay logo above a custom button titled 'Order Now'.
  - ❌ Ejemplo incorrecto: An illustration that shows the incorrect arrangement of the Apple Pay logo above a custom button titled 'Apple Pay'.
- **Use the Apple Pay mark graphic only to communicate that you accept Apple Pay.**
- **Don’t hide an Apple Pay button or make it appear unavailable.**
- **Inform search engines that Apple Pay is accepted on your website.**
> **Important:** All websites that offer Apple Pay must include a privacy statement and adhere to the [Acceptable use guidelines for Apple Pay on the web](https://developer.apple.com/apple-pay/acceptable-use-guidelines-for-websites/).

### Streamlining checkout

- **Provide a cohesive checkout experience.**
- **If Apple Pay is available, assume people want to use it.**
- **Accelerate single-item purchases with Apple Pay buttons on product detail pages.**
- **Accelerate multi-item purchases with express checkout.**
- **Support coupons and promotional codes in the payment sheet.**
- **Collect necessary information, like color and size options, before people reach the Apple Pay button.**
- **Collect optional information before checkout begins.**
- **Gather multiple shipping methods and destinations before showing the payment sheet.**
- **For in-store pickup, help people choose a pickup location before displaying the payment sheet.**
- **Prefer checkout information from Apple Pay.**
- **Avoid requiring account creation before purchase.**
- **Report transaction results in the payment sheet.**
- **Display an order confirmation or thank-you page.**

#### Customizing the payment sheet

- **Only present and request essential information.**
- **Display the active coupon or promotional code, or let people enter one.**
- **Let people choose the shipping method in the payment sheet.**
- **For in-store pickup, consider letting people choose a pickup window that works for them.**
- **Use line items to explain additional charges, discounts, pending costs, add-on donations, recurring payments, and future payments.**
- **Keep line items short.**
- **Provide a business name after the word *Pay* on the same line as the total.**
- **If you’re not the end merchant, identify both businesses in the payment sheet.**
- **Clearly disclose when people may incur additional costs after payment authorization.**
- **Handle data entry and payment errors gracefully.**
- **Defer to the payment sheet for progress information during payment.**

### Displaying a website icon

- Many websites provide an icon that appears with bookmarks, in URL fields, and on a device’s Home Screen.
- If your website supports Apple Pay, provide an icon in the following sizes:

| @2x | @3x |
|---|---|
| 60x60 pt (120x120 px @2x) | 60x60 pt (180x180 px @3x) |

### Handling problems

- Provide clear, actionable guidance when problems occur during checkout or payment processing, so people can resolve them quickly and complete their transaction.

#### Data validation errors

- Your app or website can respond to user input when the payment sheet appears, when people change certain field values on the payment sheet, and after they authenticate the…
- When data is invalid, system-provided error messages highlight relevant fields on the payment sheet.
- For developer guidance, see [PKPaymentAuthorizationViewControllerDelegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate) (iOS,…
> **Note:** For privacy reasons, your app or website has limited access to data until people attempt to authorize a transaction.
- **Avoid forcing compliance with your business logic.**
- **Accurately report problems to the system.**
- **Explain the problem clearly and succinctly when data is invalid or incorrectly formatted.**
  - «Aim to keep messages at 128 characters or fewer to avoid truncation.»

#### Payment processing problems

- **Handle interruptions correctly.**

### Supporting subscriptions

- Your app or website can use Apple Pay to request authorization for recurring payments.
- **Clarify subscription details before showing the payment sheet.**
- **Include line items that reiterate billing frequency, discounts, and additional upfront fees.**
- **Clearly communicate trial period terms.**
- **Clarify the current payment amount in the total line.**
- **Only show the payment sheet when a subscription change results in additional fees.**
> **Important:** Treat the billing agreement field as a plain-language summary, not a substitute for formal terms.

### Supporting donations

- [Approved nonprofits](https://developer.apple.com/support/apple-pay-nonprofits/) can use Apple Pay to accept donations.
- **Use a line item to identify a donation.**
- **Streamline checkout by offering predefined donation amounts.**

### Using Apple Pay buttons

- Apple Pay buttons come in several types and styles to fit different contexts and purchase flows.
  - Buttons with Apple-approved captions, fonts, colors, and styles
  - Content that scales proportionally at any size
  - Automatic localization into the device’s language
  - Corner radius customization to match your interface
  - Built-in VoiceOver support with automatic alternative text
- **Always use the Apple-provided API to display Apple Pay buttons.**
> **Tip:** Use the [Apple Pay mark](https://developer.apple.com/design/human-interface-guidelines/apple-pay#Apple-Pay-mark) graphic to communicate the availability of Apple Pay wherever you highlight payment options.

#### Button types

- Choose a button type that best fits the terminology and flow of your purchase or payment experience.

##### Apple Pay button

- Use the buttons below to initiate payment.

| Payment button type | Example usage |
|---|---|
| ![Buy with Apple Pay button](https://developer.apple.com/images/com.apple.HIG/button-buy-with@2x.png) | An area in an app or website where people can make a purchase, such as a product detail page or shopping cart page. |
| ![Pay with Apple Pay button](https://developer.apple.com/images/com.apple.HIG/button-pay-with@2x.png) | An app or website that lets people pay bills or invoices, such as those for a utility — like cable or electricity — or a service like plumbing or car repair. |
| ![Check Out with Apple Pay button](https://developer.apple.com/images/com.apple.HIG/button-check-out-with@2x.png) | An app or website offering a shopping cart or purchase experience that includes other payment buttons that start with the text *Check Out*. |
| ![Continue with Apple Pay button](https://developer.apple.com/images/com.apple.HIG/button-continue-with@2x.png) | An app or website offering a shopping cart or purchase experience that includes other payment buttons that start with the text *Continue*. |
| ![Book with Apple Pay button](https://developer.apple.com/images/com.apple.HIG/button-book-with@2x.png) | An app or website that helps people book flights, trips, or other experiences. |
| ![Donate with Apple Pay button](https://developer.apple.com/images/com.apple.HIG/button-donate-with@2x.png) | An app or website for an [approved nonprofit](https://developer.apple.com/support/apple-pay-nonprofits/) that lets people make donations. |
| ![Subscribe with Apple Pay button](https://developer.apple.com/images/com.apple.HIG/button-subscribe-with@2x.png) | An app or website that lets people purchase a subscription, such as a gym membership or a meal-kit delivery service. |
| ![Reload with Apple Pay button](https://developer.apple.com/images/com.apple.HIG/button-reload-with@2x.png) | An app or website that uses the term *Reload* to help people add money to a card, account, or payment system associated with a service, such as transit or a prepaid phone plan. |
| ![Add Money with Apple Pay button](https://developer.apple.com/images/com.apple.HIG/button-add-money-with@2x.png) | An app or website that uses the term *Add Money* to help people add money to a card, account, or payment system associated with a service, such as transit or a prepaid phone plan. |
| ![Top Up with Apple Pay button](https://developer.apple.com/images/com.apple.HIG/button-top-up-with@2x.png) | An app or website that uses the term *Top Up* to help people add money to a card, account, or payment system associated with a service, such as transit or a prepaid phone plan. |
| ![Order with Apple Pay button](https://developer.apple.com/images/com.apple.HIG/button-order-with@2x.png) | An app or website that lets people place orders for items like meals or flowers. |
| ![Rent with Apple Pay button](https://developer.apple.com/images/com.apple.HIG/button-rent-with@2x.png) | An app or website that lets people rent items like cars or scooters. |
| ![Support with Apple Pay button](https://developer.apple.com/images/com.apple.HIG/button-support-with@2x.png) | An app or website that uses the term *Support* to help people give money to projects, causes, organizations, and other entities. |
| ![Contribute with Apple Pay button](https://developer.apple.com/images/com.apple.HIG/button-contribute-with@2x.png) | An app or website that uses the term *Contribute* to help people give money to projects, causes, organizations, and other entities. |
| ![Tip with Apple Pay button](https://developer.apple.com/images/com.apple.HIG/button-tip-with@2x.png) | An app or website that lets people tip for goods or services. |
| ![Apple Pay button](https://developer.apple.com/images/com.apple.HIG/ap-button@2x.png) | An app or website that has stylistic reasons to use a button that can have a smaller minimum width or that doesn’t specify a call to action. If you choose a payment button type that isn’t supported on the version of the operating system your app or website is running in, the system may replace it with this button. |

##### Set Up Apple Pay button

- When a device supports Apple Pay but the person hasn’t set it up yet, you can use the Set Up Apple Pay button to show that you accept Apple Pay, and to give the person an…

#### Button styles

- Use the *automatic* style to let the current system appearance determine the appearance of Apple Pay buttons.

##### Black

- Use on white or light-color backgrounds that provide sufficient contrast.
  - ✅ Ejemplo correcto: An illustration showing the correct placement of a black Apple Pay button over a light background.
  - ❌ Ejemplo incorrecto: An illustration showing the incorrect placement of a black Apple Pay button over a dark background.

##### White with outline

- Use on white or light-color backgrounds that don’t provide sufficient contrast.
  - ✅ Ejemplo correcto: An illustration showing the correct placement of a white, outlined Apple Pay button over a light background.
  - ❌ Ejemplo incorrecto: An illustration showing the incorrect placement of a white, outlined Apple Pay button over a dark background.

##### White

- Use on dark-color backgrounds that provide sufficient contrast.
  - ✅ Ejemplo correcto: An illustration showing the correct placement of a white Apple Pay button over a dark background.
  - ❌ Ejemplo incorrecto: An illustration showing the incorrect placement of a white Apple Pay button over a light background.

#### Button size and position

- **Prominently display the Apple Pay button.**
  - ✅ Ejemplo correcto: An illustration showing an Apple Pay button positioned correctly above a custom Add to Cart button. Both buttons are the same size.
  - ❌ Ejemplo incorrecto: An illustration showing an Apple Pay button positioned incorrectly at a smaller size above a larger custom Add to Cart button.
- **Position the Apple Pay button correctly in relation to an Add to Cart button.**
- ✅ (correcto)
- ❌ (incorrecto)
- In a stacked layout, place the Apple Pay button above an Add to Cart button.
  - ✅ Ejemplo correcto: An illustration of a Check Out with Apple Pay button correctly positioned above a custom Add to Cart button.
  - ❌ Ejemplo incorrecto: An illustration of a Check Out with Apple Pay button incorrectly positioned below a custom Add to Cart button.
- **Adjust the corner radius to match the appearance of other buttons.**
- **Maintain the minimum button size and margins around the button.**
> **Note:** If the size you specify doesn’t accommodate the translated title for the type of payment button you’re using, the system automatically replaces it with the plain Apple Pay button shown below on the left.
- (imagen) An illustration of an Apple Pay button, labeled to indicate minimum margins of one-tenth the button’s height, a 100-point minimum width, and a 30-point minimum height.
- (imagen) An illustration of a Donate with Apple Pay button, labeled to indicate minimum margins of one-tenth the button’s height, a 140-point minimum width, and a 30-point minimum height.
- Use the following values for guidance.

| Button | Minimum width | Minimum height | Minimum margins |
|---|---|---|---|
| Apple Pay | 100pt (100px @1x, 200px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |
| Book with Apple Pay | 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |
| Buy with Apple Pay |  |  |  |
| Check Out with Apple Pay |  |  |  |
| Donate with Apple Pay |  |  |  |
| Set Up Apple Pay |  |  |  |
| Subscribe with Apple Pay |  |  |  |

#### Apple Pay mark

- Use the Apple Pay mark graphic to show that Apple Pay is an available payment option when showing other available payment options.
- **Use only the artwork provided by Apple, with no alterations other than height.**
- **Maintain a minimum clear space around the mark of 1/10 of its height.**
- Download the Apple Pay mark graphic and full usage guidelines from the [Apple Pay Marketing Guidelines page](https://developer.apple.com/apple-pay/marketing/).

### Referring to Apple Pay

- You can use plain text to promote Apple Pay and indicate that Apple Pay is a payment option.
- **Capitalize Apple Pay in text as it appears in the Apple Trademark List.**
- **Never use the Apple logo to represent the name *Apple* in text.**

|  | Example text |
|---|---|
| ✅ (correcto) | Purchase with Apple Pay |
| ✅ (correcto) | Purchase with Apple Pay® |
| ❌ (incorrecto) | Purchase with ApplePay |
| ❌ (incorrecto) | Purchase with  Pay |
| ❌ (incorrecto) | Purchase with APPLE PAY (when not conforming to an interface style that uses only capital letters) |

- **Coordinate the font face and size with your app or website.**
- **Don’t translate *Apple Pay* or any other Apple trademark.**
- **In a payment selection context, you can display a text-only description of Apple Pay only when all payment options have text-only descriptions.**
- **When promoting Apple Pay in an app, follow App Store guidelines.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, visionOS, or watchOS.

## Recursos relacionados

- *Related:*
  - [Apple Pay Marketing Guidelines](https://developer.apple.com/apple-pay/marketing/)
- *Developer documentation:*
  - [Apple Pay](https://developer.apple.com/documentation/passkit/apple-pay) — PassKit
  - [Apple Pay on the Web](https://developer.apple.com/documentation/applepayontheweb)
  - [WKInterfacePaymentButton](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton) — WatchKit

## Vídeos que la explican

- [What’s new in Apple Pay](https://developer.apple.com/videos/play/wwdc2025/201) → `references/videos/2025-201.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 8, 2026 | Refined guidance to reflect the latest Apple Pay appearance and capabilities. |
| December 16, 2025 | Clarified supported platforms, including web browsers and Apple Vision Pro. |
| June 10, 2024 | Updated links to developer guidance for offering Apple Pay on the web. |
| September 12, 2023 | Updated artwork. |
| May 2, 2023 | Consolidated guidance into one page. |
