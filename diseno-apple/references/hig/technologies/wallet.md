# Wallet — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/wallet
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados,macos,visionos,watchos
- Última actualización: 2026-06-08 — Updated to reflect guidance for iOS 27 and the Pass Designer app.

> Resumen de Apple: Wallet helps people securely store their credit and debit cards, driver’s license or state ID, transit cards, event tickets, keys, and more on iPhone and Apple Watch.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- People use their cards and passes in Wallet to make Apple Pay purchases, track their orders, confirm their identity, and streamline activities like boarding a plane, attending a…
- When you integrate Apple Wallet into your app, you can create custom passes and present them the moment people need them, securely verify an individual’s identity so they can…

### Passes

- Passes are digital representations of information that people can add to Wallet, like event tickets, boarding passes, membership reward cards, and coupons.
- **Offer to add new passes to Wallet.**
- **Help people add a pass created outside your app.**
- **Add related passes as a group.**
- **Display an Add to Apple Wallet button to let people add an existing pass not already in Wallet.**
- **Let people jump from your app to their pass in Wallet.**
- **Tell the system when your passes expire.**
- **Always get permission before deleting passes from Wallet.**
- **Help the system suggest a pass when relevant.**
- **Keep passes up to date.**
- **Use change messages only for updates to time-critical information.**

### Pass anatomy

- You define the content and structure of a pass using a combination of pass fields and semantic tags.
- In some cases, you can provide supplemental information that people can access via sheets linked from the front of the pass.
- For developer guidance, see [Wallet Passes](https://developer.apple.com/documentation/walletpasses).

#### Pass field types

- Pass fields are organized into the following areas:
  - Logo and logo text fields: Show the brand icon and name; they remain visible when the pass is collapsed in Wallet.
  - Header fields: Show critical information that remains visible when the pass is collapsed.
  - Primary field: Shows the most important information people need.
  - Secondary and auxiliary fields: Show useful, but less critical information.
  - Footer fields: Show supplemental information, such as pass category (for example, “Family” or “Annual”).
  - Back fields: Show supplemental details that appear in pass details in Wallet.
- Layout varies by pass style.

### Designing passes

- Wallet uses a consistent visual style to build familiarity and trust.
- Use Pass Designer to design and preview passes for Apple Wallet.
- **Design a pass that looks great and works well on all devices.**
- **Keep the pass front uncluttered.**
- **Make your pass instantly identifiable.**
- **Ensure sufficient contrast between background and text colors.**
  - ✅ Ejemplo correcto: Sufficient contrast between a solid background and label text
  - ❌ Ejemplo incorrecto: Insufficient contrast between a solid background and label text
  - ✅ Ejemplo correcto: Sufficient contrast between an image background and label text
  - ❌ Ejemplo incorrecto: Insufficient contrast between an image background and label text
- **Use language that works on any device.**

### Pass styles

- You can choose from a variety of pass styles.

#### Boarding passes

- The boarding pass style is for travel tickets: airline boarding passes, train tickets, bus tickets, boat tickets, and generic transit passes.

#### Coupons

- The coupon style is for coupons, special offers, and other discounts.

#### Event tickets

- The event ticket pass style is for entry into events like sporting events, concerts, movies, and plays.
- Non-poster style event tickets use standard pass fields and can use a background image and thumbnail.

#### Store cards

- The store card style is for store loyalty cards, discount cards, points cards, and gift cards.

#### Poster generic passes

- The poster generic pass style features a full background image and a pass field layout distinct from other pass styles, offering a flexible option that supports a wide range of…

#### Generic passes

- The generic style is for passes that don’t fit the other categories, such as a gym membership card or coat-check claim ticket.

### Pass images

- Passes support a variety of image types.
  - «Create pass images in PNG format in @2x and @3x format.»
- **Reserve pass images for visual content.**
- **Keep image file sizes small.**
- **Provide a pass icon.**

#### Logo

- The logo appears in the top leading corner of passes with pass fields.

|  |  |
|---|---|
| **Supported pass styles** | Non-semantic airline boarding passes, non-airline boarding pass styles, coupons, non-poster event tickets, generic passes, store cards |
| **Filename** | logo.png |
| **Minimum width** | 50 pt |
| **Maximum width** | 160 pt |
| **Height** | 50 pt |

- **Avoid inner drop shadows on logo artwork.**
  - ✅ Ejemplo correcto: A brown paper bag icon with a flat appearance and no inner drop shadow.
  - ❌ Ejemplo incorrecto: A brown paper bag icon with an inner drop shadow applied, creating a recessed effect inside the icon shape.

#### Primary logo

- Like the logo, the primary logo appears in the top-leading corner of your pass, but is used exclusively for semantic passes.

|  |  |
|---|---|
| **Supported pass styles** | Airline boarding passes, poster event tickets, and poster generic passes |
| **Filename** | primaryLogo.png |
| **Minimum width** | 30 pt |
| **Maximum width** | 126 pt |
| **Height** | 30 pt |

#### Secondary logo

- The secondary logo displays an additional logo for a ticket issuer or event organizer.

|  |  |
|---|---|
| **Supported pass styles** | Poster event ticket |
| **Filename** | secondaryLogo.png |
| **Minimum width** | 12 pt |
| **Maximum width** | 135 pt |
| **Height** | 12 pt |

#### Icon

- Icons are square and represent your company or brand when your pass appears on the Lock Screen, in Mail, and on passes in Wallet.

|  |  |
|---|---|
| **Supported pass styles** | All |
| **Filename** | icon.png |
| **Width** | 38 pt |
| **Height** | 38 pt |

#### Strip image

- Strip images appear on coupons and store cards to reinforce your brand or offer.

|  |  |
|---|---|
| **Supported pass styles** | Coupon, store card |
| **Filename** | strip.png |
| **Width** | 375 pt |
| **Height** | 144 pt |

#### Thumbnail

- Thumbnails are small images, such as a movie poster, that appear on event tickets and generic passes.

|  |  |
|---|---|
| **Supported pass styles** | Event ticket, generic pass |
| **Filename** | thumbnail.png |
| **Minimum width** | 60 pt |
| **Maximum width** | 90 pt |
| **Height** | 90 pt |

#### Background

- The background image is the visual centerpiece of a pass.
- **Non-poster pass backgrounds**

|  |  |
|---|---|
| **Supported pass styles** | Event tickets |
| **Filename** | background.png |
| **Width** | 343 pt |
| **Height** | 503 pt |

- **Poster pass backgrounds**

|  |  |
|---|---|
| **Supported pass styles** | Poster event tickets, poster generic passes |
| **Filename** | artwork.png |
| **Width** | 358 pt |
| **Height** | 448 pt |

- Position content within the safe area — on poster generic passes and poster event tickets, a material strip covers the bottom edge of the image.

#### Footer

- The footer is only available for airline boarding passes.

|  |  |
|---|---|
| **Supported pass styles** | Airline boarding passes |
| **Filename** | footer.png |
| **Width** | 268 pt |
| **Height** | 15 pt |

### Order tracking

- When you support order tracking, Wallet can display information about an order a customer placed through your app or website, updating the information whenever the status of the…
- Wallet presents a dashboard that displays a customer’s active and completed orders.
- The [Wallet Orders](https://developer.apple.com/documentation/walletorders) schema defines the properties you use to provide order data like product descriptions, order status,…
- **Make it easy for people to add an order to Wallet.**
- **Make information about an order available immediately after people place it.**
- **Provide fulfillment information as soon as it’s available, and keep the status up to date.**
- **Supply a high-resolution logo image that uses a nontransparent background.**
- **Supply distinct, high-resolution product images that use nontransparent backgrounds.**
- (imagen) An illustration of a donut, representing a product image. Horizontal and vertical lines extend along the bottom and right side of the image, and include labels that denote the illustration is 300 pixels wide by 300 pixels high.
- **In general, keep text brief.**
- **Use clear, approachable language, and localize the text you provide.**

#### Displaying order and fulfillment details

- An order gives people ways to contact the merchant and displays details about their Apple Pay purchase, including fulfillment status and per-item information.
- **Provide a link to an area where people manage their order.**
- **Clearly describe each item so people can verify that their order contains everything they expect.**
- **Supply a prioritized list of your apps that might be installed on the device.**
- **Avoid sending duplicate notifications.**
- **Make it easy for customers to contact the merchant.**
- **Help people track their order.**
  - A link that opens the carrier’s website to a page with information about a shipping fulfillment.
  - A scannable barcode when one is required to pick up the order in a pickup fulfillment.
  - Clear, detailed instructions that can help people receive or pick up their order.
- **Keep the fulfillment screen centered on order tracking.**
- **Choose shipping-fulfillment values that match the details you have about the shipping process.**
- **Keep customers informed through relevant fulfillment status descriptions.**
- **Be direct and thorough when describing an Issue or Canceled status.**

### Identity verification

- On iPhone running iOS 16 and later, people can store an ID card in Wallet, and later allow an app or App Clip to access information on the card to verify their identity without…
> **Developer note:** Apple doesn’t create or see the ID documents that people add to Wallet, and when people agree to share identifying information with your app, you receive only encrypted data that isn’t readable on the device.
- To help you offer a consistent experience that people can trust, Apple provides a Verify with Wallet button you can use in your app when you need to ask for identity verification.
- **Present a Wallet verification option only when the device supports it.**
- **Ask for identity information only at the precise moment you need it.**
- **Clearly and succinctly describe the reason you need the information you’re requesting.**

| To verify… | To support… | Example purpose string |
|---|---|---|
| Identity | Opening an account for which proof of identity is legally required to prevent fraud | Federal law requires this information to verify your identity and also to help [App Name] prevent fraud. |
| Driving privilege | Renting a vehicle that requires legal driving privileges | Applicable state law requires [App Name] to verify your driving privileges. |

- For each purpose string, aim for a brief, complete sentence that’s direct, specific, and easy for everyone to understand.
- **Ask only for the data you actually need.**
- **Clearly indicate whether you will keep the data and — if you need to keep it — specify how long you’ll do so.**
- **Choose the system-provided verification button that matches your use case and the visual design of your app.**

| Button type | Consider using when… |
|---|---|
| ![An illustration of a Verify Age with Apple Wallet button.](https://developer.apple.com/images/com.apple.HIG/wallet-button-verify-age@2x.png) | Your app can complete the current transaction after you verify a person’s age. An example transaction is making a car available to lease. |
| ![An illustration of a Verify Identity with Apple Wallet button.](https://developer.apple.com/images/com.apple.HIG/wallet-button-verify-identity@2x.png) | Your app can complete the current transaction after you verify a person’s identity. An example transaction is a car rental. |
| ![An illustration of a Continue with Apple Wallet button.](https://developer.apple.com/images/com.apple.HIG/wallet-button-continue-with@2x.png) | Verify with Wallet forms one part of a verification process that also requires people to supply additional information not provided by Verify with Wallet, such as a Social Security number or phone number. Examples include opening a financial account or performing a background check. |
| ![An illustration of a Verify with Apple Wallet button.](https://developer.apple.com/images/com.apple.HIG/wallet-button-verify-with@2x.png) | Your app can complete the current verification flow without additional steps, but the “Verify Age,” “Verify Identity,” and “Continue” button labels aren’t appropriate for your use case. An example is an app that helps people sign up for a government service. |

- All button labels are also available in a multiline variant that the system automatically uses when horizontal space is constrained.
- The verification button always uses white letters on a black background.

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, or visionOS.

#### watchOS

- On Apple Watch, Wallet displays passes in a scrolling carousel of cards.
- People can tap a pass on their Apple Watch to reveal a details screen that displays additional information in a scroll view.
- Each pass style specifies the fields and images that can appear in the basic layout areas shown below:
- If some information doesn’t fit within the layout areas, the system displays it in the scrolling details screen.
> **Important:** In every style, watchOS crops the strip image to fit the aspect ratio of the card interface and may crop white space from other images.

## Recursos relacionados

- *Related:*
  - [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay)
  - [ID Verifier](https://developer.apple.com/design/human-interface-guidelines/id-verifier)
- *Developer documentation:*
  - [FinanceKitUI](https://developer.apple.com/documentation/financekitui)
  - [FinanceKit](https://developer.apple.com/documentation/financekit)
  - [PassKit (Apple Pay and Wallet)](https://developer.apple.com/documentation/passkit)
  - [Wallet Passes](https://developer.apple.com/documentation/walletpasses)
  - [Wallet Orders](https://developer.apple.com/documentation/walletorders)

## Vídeos que la explican

- [What’s new in Wallet](https://developer.apple.com/videos/play/wwdc2026/209) → `references/videos/2026-209.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 8, 2026 | Updated to reflect guidance for iOS 27 and the Pass Designer app. |
| January 17, 2025 | Added specifications for pass image dimensions. |
| December 18, 2024 | Added guidance for the poster event ticket style. |
| September 12, 2023 | Added guidance for helping people add orders to Wallet. |
| February 20, 2023 | Enhanced guidance for presenting order-tracking information and added artwork. |
| November 30, 2022 | Added guidance to include a carrier name in status information for a shipping fulfillment. |
| September 14, 2022 | Added guidelines for using Verify with Wallet, updated guidance on providing shipping status values and descriptions, and consolidated guidance into one page. |
