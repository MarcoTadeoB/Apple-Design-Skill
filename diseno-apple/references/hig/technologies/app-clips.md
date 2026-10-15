# App Clips — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/app-clips
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados
- Última actualización: 2025-06-09 — Updated guidance to include demo App Clips.

> Resumen de Apple: An App Clip is a lightweight version of your app or game that provides an on-the-go or demo experience that’s instantly available.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- App Clips deliver an experience from your app or game without requiring people to download the full app from the App Store.
- People discover and launch App Clips in a variety of situations and contexts.
- On their device, people launch an App Clip from location-based suggestions they permit in Siri Suggestions, the Maps app, Smart App Banners on websites, App Clip cards in Safari,…
- Consider creating an App Clip if your app provides an in-the-moment experience that helps people perform a task over a finite amount of time.
  - A rental bike could come with an App Clip Code that people tap or scan to launch an App Clip that lets them rent the bike.
  - A coffee shop could offer an App Clip for fast advance orders that customers launch from a Smart App Banner or an App Clip card on the shop’s website.
  - A food truck could create marketing material (for example, a poster to promote a seasonal dish) that includes an App Clip Code.
  - A restaurant could let diners pay for a meal by launching an App Clip from the Maps app or a suggestion from Siri Suggestions, or by holding their device close to an App Clip…
  - A museum could have visitors scan App Clip Codes or QR codes on labels next to displayed works to launch an App Clip that reveals augmented reality content or provides audio…
- Consider creating an App Clip to let people experience your app or game before committing to a purchase or subscription.
  - A game might offer an App Clip that lets people play a demo version of the game, including a tutorial and the first level of the game.
  - A fitness app might offer an App Clip with a free workout and a guided meditation.
  - A text editor might allow people to create and save a document using the demo App Clip.
- For developer guidance, see [App Clips](https://developer.apple.com/documentation/appclip).

### Designing your App Clip

- **Allow people to complete a task or a demo in your App Clip.**
- **Focus on essential features.**
- **Don’t use App Clips solely for marketing purposes.**
- **Avoid using web views in your App Clip.**
- **Design a linear, easy-to-use, and focused user interface.**
- **On launch, show the most relevant part of your App Clip.**
- **Ensure people can use your App Clip immediately.**
- **Ensure your App Clip is small.**
- **Make the App Clip shareable.**
- **Make it easy to pay for a service or product.**
- **Avoid requiring people to create an account before they can benefit from your App Clip.**
- **Provide a familiar, focused experience in your app.**

#### Preserving privacy

- The system imposes limits on App Clips to ensure people’s privacy.
- **Limit the amount of data you store and handle yourself.**
- **Consider offering Sign in with Apple.**
- **Offer a secure way to pay for services or goods that also respects people’s privacy.**

#### Showcasing your app

- People don’t manage App Clips themselves, and App Clips don’t appear on the Home screen.
- Because apps remain the best way to keep people engaged over time, the system helps them discover and install the full app:
  - On the App Clip card, people can either launch the App Clip or visit the full app’s page on the App Store.
  - When people first launch the App Clip, the system displays an app banner at the top of the screen.
- In addition, you can display an overlay in your App Clip that allows people to download the full app from within the App Clip.
- **Don’t compromise the user experience by asking people to install the full app.**
- **Pick the right time to recommend your app.**
- **Recommend your app in a nonintrusive, polite way.**
- For developer guidance, see [Recommending your app to App Clip users](https://developer.apple.com/documentation/appclip/recommending-your-app-to-app-clip-users).

#### Limiting notifications

- App Clips provide the option to schedule and receive notifications for up to 8 hours after launch, enough time to follow up and complete most common tasks.
- **Only ask for permission to use notifications for an extended period of time if it’s really needed.**
- **Keep notifications focused.**
- **Use notifications to help people complete a task.**
- For developer guidance, see [Enabling notifications in App Clips](https://developer.apple.com/documentation/appclip/enabling-notifications-in-app-clips).

#### Creating App Clips for businesses

- If you’re a platform provider who services businesses, you may create several App Clip experiences in [App Store Connect](https://appstoreconnect.apple.com) and use a single App…
- **Use consistent branding.**
- **Consider multiple businesses.**
- For developer guidance, see [Configuring App Clip experiences](https://developer.apple.com/documentation/appclip/configuring-the-launch-experience-of-your-app-clip).

### Creating content for an App Clip card

- The system-provided App Clip card is people’s first interaction with your App Clip, so give careful consideration to its images and copy.
- **Be informative.**
- **Prefer photography and graphics.**
- **Avoid using text.**
- **Adhere to image requirements.**
- **Use concise copy.**
  - «Create a title that has no more than 30 characters and a subtitle that has no more than 56 characters.»
- **Pick a verb for the action button that best fits your App Clip.**

### App Clip Codes

- App Clip Codes are the best way for people to discover your App Clip.
- App Clip Codes always use the designs Apple provides and follow size, placement, and printing guidelines.

#### Interacting with App Clip Codes

- App Clip Codes come in two variants: *scan-only* or with an embedded NFC tag (*NFC-integrated*).
- The scan-only variant uses a camera icon in its center to let people know to use the Camera app or the Code Scanner in Control Center to scan the App Clip Code.
  - A coffee shop could place an App Clip Code on their menu. A guest could hold their device close to the App Clip Code and instantly launch the shop’s App Clip to order a drink.
  - A gas station could have an NFC-integrated App Clip Code attached to each pump.
  - A video game creator could hand out marketing material at an industry event that includes an App Clip Code.

#### Displaying App Clip Codes

- When you start designing your App Clip Codes, choose the variant that works best for the way people use your App Clip.
  - On a tabletop at a restaurant
  - Near a register at a retail store
  - In a storefront window
  - On signage
  - On a gift card or coupon
- If you need to place your App Clip Code in an area that’s physically inaccessible or you need to display it digitally, use a scan-only App Clip Code.
  - On posters or printed advertising
  - On signage behind a counter or unreachable in a storefront
  - On digital materials such as digital displays, in emails, or on images you post to social media
- No matter which of the two variants you use, it’s important you carefully consider where you place your App Clip Code to ensure a reliable scanning experience.
- **Include the App Clip logo when space allows.**
- **Place your App Clip Code on a flat or cylindrical surface only.**
- (imagen) An illustration that shows a circle that represents a cylindrical surface. Lines divide the circle into six segments of equal size. One segment represents an App Clip Code and shows how the code doesn’t cover more than one-sixth, or 60 degrees, of the surface’s circumference.
- **Help your App Clip Code remain as flat as possible so it’s easy for people to scan.**
- **Place your App Clip Code in a location that helps ensure reliable scanning.**
- **Make sure the App Clip Code is unobstructed.**
- **Display the App Clip Code in an upright position.**
  - ✅ Ejemplo correcto: A correctly placed App Clip Code in the upright position.
  - ❌ Ejemplo incorrecto: An incorrectly placed App Clip Code that's rotated 90 degrees to the left.
  - ❌ Ejemplo incorrecto: An incorrectly placed App Clip Code that's rotated 135 degrees to the right.
- **Don’t create App Clip Codes that are too small.**

| Type | Minimum size |
|---|---|
| Printed communications | Minimum diameter of 3/4 inch (1.9 cm). |
| Digital communications | Minimum size of 256×256 px. Use a PNG or SVG file. |
| NFC-integrated App Clip Code | The embedded NFC tag needs to be at least 35 mm in diameter or of equivalent size. For example, if your embedded NFC tag is 35 mm in diameter, your printed App Clip Code needs to be at least 1.37 inches (3.48 cm) in diameter. |

- (imagen) An App Clip Code that uses the badge design and has a minimum diameter of 3/4 inch (1.9 cm).
- (imagen) An App Clip Code that uses the design without the App Clip logo and has a minimum diameter of 3/4 inch (1.9 cm).
- When determining the dimensions of your App Clip Codes, consider a distance to code size ratio of no more than 20:1.
  - «If possible, use a ratio of 10:1 to ensure reliable scanning.»
  - «For example, an App Clip that people scan from 40 inches (101 cm) away needs to be at least 4 inches (10.16 cm) in diameter.»
- If you display an App Clip Code near a QR Code or other scannable item, choose a size for the App Clip Code that’s at least the other code’s or item’s size.
- **Provide enough space between an App Clip Code and adjacent App Clip Codes, graphics, or materials.**

#### Using clear messaging

- Add clear messaging that informs people how they can use the App Clip Code to launch your App Clip, especially if you use the design without the App Clip logo.
- For a scan-only App Clip Code, you can use the following call to action:
  - Scan to [*describe what people can do with your App Clip*].
  - Scan using the camera on your iPhone or iPad to [describe what people can do with your App Clip].
- For an NFC-integrated App Clip Code, you can use the following call to action:
  - Scan to [*describe what people can do with your App Clip*].
  - Hold your iPhone near the [*object name*] to launch an App Clip that [*describe what a person can do with your App Clip*].
- For more information, see [NFC](https://developer.apple.com/design/human-interface-guidelines/nfc).
- **Adhere to [Guidelines for Using Apple Trademarks](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html) when referring to your App Clip and App Clip Codes.**

#### Customizing your App Clip Code

- Use [App Store Connect](https://appstoreconnect.apple.com) or the [App Clip Code Generator](https://developer.apple.com/app-clips/resources/) command-line tool to create App Clip…
- **Always use the generated App Clip Code.**
  - ❌ Ejemplo incorrecto: An illustration of an invalid App Clip Code with a changed aspect ratio.
  - ❌ Ejemplo incorrecto: An illustration of an invalid App Clip Code with a color gradient instead of a solid background color.
  - ❌ Ejemplo incorrecto: An illustration of an invalid App Clip Code with a drop shadow effect.
- **Choose colors with enough contrast that ensure accurate scanning.**

### Printing guidelines

- App Clip Codes offer the best experience to launch App Clips.
- Always test printed App Clip Codes before you distribute them to be sure they’re scannable from a variety of angles.
- **Use high-quality, non-textured print materials.**
- **Use high-resolution images and printer settings.**
  - «When rasterizing the SVG file, set the image resolution to at least 600 ppi, and print your App Clip Codes with a minimum resolution of 300 dpi.»
- **Use correct color settings when you convert the generated SVG file to a CMYK image.**
- **If you’re using a printer that only prints in grayscale, only generate grayscale App Clip Codes.**
- **For NFC-integrated App Clip Codes, choose Type 5 NFC tags.**
  - «The embedded NFC tag needs to be at least 35 mm in diameter or of equivalent size.»
- **If you create large batches of App Clip Codes, thoroughly test your printing workflow, and verify printed App Clip Codes.**
- If you create many App Clip Codes with the [App Clip Code Generator](https://developer.apple.com/app-clips/resources/) tool or [App Store…

#### Verifying your printer’s calibration

- A reliable scanning experience depends on the quality of your printed App Clip Codes.
- **Verify print quality of your chosen color pair with the printer calibration test sheet that shows text boxes for each default color pair.**
- **Verify your printer’s grayscale settings by printing the printer calibration test sheet that shows two grayscale bars.**

### Legal requirements

- Only the Apple-provided App Clip Codes created in App Store Connect or with the App Clip Code Generator command-line tool and that follow these guidelines are approved for use.
- App Clip Codes are approved for use to indicate availability of an App Clip.
- In the event your App Clip is no longer active, also stop displaying the App Clip Code associated with that inactive App Clip.
- You may not use the App Clip Code (including, without limitation, the Apple Logo, the App Clip mark, and the App Clip Code designs) as part of your own company name or as part of…
- The App Clip Codes described in these guidelines must not be used in any manner that is likely to reduce, diminish, or damage the goodwill, value, or reputation associated with…
- Apple retains all rights to its trademarks, copyrights, or other intellectual property rights contained in the materials provided for use hereunder, including, without…
- Don’t add a symbol to App Clip Codes created in App Store Connect or with the App Clip Code Generator command-line tool.
- Don’t translate any Apple trademark.
- For more information about using Apple trademarks, see [Guidelines for Using Apple Trademarks](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html).

### Platform considerations

- *No additional considerations for iOS or iPadOS.

## Recursos relacionados

- *Related:*
  - [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay)
  - [Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple)
  - [Guidelines for Using Apple Trademarks and Copyrights](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)
- *Developer documentation:*
  - [App Clips](https://developer.apple.com/documentation/appclip)
  - [App Store Connect](https://appstoreconnect.apple.com/)

## Vídeos que la explican

- [What's new in App Clips](https://developer.apple.com/videos/play/wwdc2021/10012) → `references/videos/2021-10012.md`
- [Build light and fast App Clips](https://developer.apple.com/videos/play/wwdc2021/10013) → `references/videos/2021-10013.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 9, 2025 | Updated guidance to include demo App Clips. |
| May 2, 2023 | Consolidated guidance into one page. |
