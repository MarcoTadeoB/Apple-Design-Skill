# Sign in with Apple — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2022-09-14 — Refined guidance on supporting existing accounts, helping people set up a new account, and indicating the current sign-in status. Consolidated guidance into one page.

> Resumen de Apple: Sign in with Apple provides a fast, private way to sign into apps and websites, giving people a consistent experience they can trust and the convenience of not having to remember multiple accounts and passwords.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Supporting Sign in with Apple lets people use the Apple Account they already have to sign in or sign up, and skip filling out forms, verifying email addresses, and choosing…
- You can offer Sign in with Apple in every version of your app or website across all platforms — including non-Apple platforms.
- Sign in with Apple makes it easy for people to authenticate with Face ID, Touch ID, or Optic ID and has two-factor authentication built in for an added layer of security.

### Offering Sign in with Apple

- Follow these guidelines to offer Sign in with Apple when it’s most convenient for people.
- **Ask people to sign in only in exchange for value.**
- **Delay sign-in as long as possible.**
- **If you require an account, ask people to set it up before offering any sign-in options.**
- **Consider letting people link an existing account to Sign in with Apple.**
  - If people share an email address through Sign in with Apple and it matches the address in an existing account, you can suggest that they link Sign in with Apple to that account.
  - If people used an existing user name and password to sign in, you can display an account-linking suggestion in their account’s settings view or another logical place.
- **In a commerce app, wait until after people make a purchase before asking them to create an account.**
- **As soon as Sign in with Apple completes, welcome people to their new account.**
- **Indicate when people are currently signed in.**

### Collecting data

- People appreciate Sign in with Apple for its privacy and convenience.
- **Clarify whether the additional data you request is required or just recommended.**
- **Don’t ask people to supply a password.**
  - «Unless people have stopped using Sign in with Apple with your app or website, don’t ask for a password.»
- **Avoid asking for a personal email address when people supply a private relay address.**
  - Make sure that people can view their private relay address in your app or website
  - Direct people to Settings > Apple Account > Password & Security > Apps using Apple Account to retrieve their private relay address
  - Use other identifying values, like an order number or phone number collected as part of a purchase
- **Give people a chance to engage with your app before asking for optional data.**
- **Be transparent about the data you collect.**

### Displaying buttons

- Apple provides several Sign in with Apple buttons you can use to let people set up an account and sign in.
- **Prominently display a Sign in with Apple button.**

#### Using the system-provided buttons

- When you use the system-provided APIs to create a Sign in with Apple button, you get the following advantages.
  - A button that’s guaranteed to use an Apple-approved appearance
  - Assurance that the button’s contents maintain ideal proportions as you change its style
  - Automatic translation of the button’s title into the language specified by the device
  - Support for configuring the button’s corner radius to match the style of your UI (iOS, macOS, and web)
  - A system-provided alternative text label that lets VoiceOver describe the button
- For developer guidance, see [ASAuthorizationAppleIDButton](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidbutton) (iOS, macOS, and tvOS),…
- The system provides several variants of the button title.
- The following button titles are available for iOS, macOS, tvOS, and the web:
- For watchOS, the system provides one title:  Sign in.
- Depending on the platform, the system provides up to three options for the appearance of the Sign in with Apple button: white, white with an outline, and black.

##### White

- The white style is available on all platforms and the web.
  - ✅ Ejemplo correcto: An illustration of a white button correctly positioned on a dark shaded background. The button includes the Apple logo and text that reads 'Sign in with Apple'.
  - ❌ Ejemplo incorrecto: An illustration of a white button incorrectly positioned on a light shaded background. The button includes the Apple logo and text that reads 'Sign in with Apple'.

##### White with outline

- The white outlined style is available in iOS, macOS, and the web.
  - ✅ Ejemplo correcto: An illustration of a white, outlined button correctly positioned on a light shaded background. The button includes the Apple logo and text that reads 'Sign in with Apple'.
  - ❌ Ejemplo incorrecto: An illustration of a white, outlined button incorrectly positioned on a dark shaded background. The button includes the Apple logo and text that reads 'Sign in with Apple'.

##### Black

- The black style is available on all platforms and the web.
  - ✅ Ejemplo correcto: An illustration of a black button correctly positioned on a light shaded background. The button includes the Apple logo and text that reads 'Sign in with Apple'.
  - ❌ Ejemplo incorrecto: An illustration of a black button incorrectly positioned on a dark shaded background. The button includes the Apple logo and text that reads 'Sign in with Apple'.
- Unlike the black Sign in with Apple button for other platforms, the watchOS button uses a fill color that’s not fully black.

##### Button size and corner radius

- **Adjust the corner radius to match the appearance of other buttons in your app.**
- **Maintain the minimum button size and margin around the button in iOS, macOS, and the web.**

| Minimum width | Minimum height | Minimum margin |
|---|---|---|
| 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |

#### Creating a custom Sign in with Apple button

- If your interface requires it, you can create a custom Sign in with Apple button for iOS, macOS, or the web.
- Always make sure that people can instantly identify your custom button as a Sign in with Apple button.
- [Apple Design Resources](https://developer.apple.com/design/resources/) provides downloadable Apple logo artwork you can use to create custom Sign in with Apple buttons that…
- All downloadable logo files include padding that simplifies positioning the logo in a button.
- Use only the logo artwork downloaded from [Apple Design Resources](https://developer.apple.com/design/resources/); never create a custom Apple logo.
  - Use the logo file to position the Apple logo in a button; never use the Apple logo as a button.
  - Match the height of the logo file to the height of the button.
  - Don’t crop the logo file.
  - Don’t add vertical padding.
- To make sure that your custom button is visually consistent with the system-provided Sign in with Apple button, don’t change the following attributes.
  - Titles. Use only *Sign in with Apple*, *Sign up with Apple*, or *Continue with Apple*.
  - General shape. Buttons that combine the logo with text are always rectangular; logo-only buttons can be circular or rectangular.
  - Logo and title colors. Within a button, both items must be either black or white; don’t use custom colors.
- To coordinate with your app design, you can change:
  - Title font. You can also adjust the font’s weight and size.
  - Title case. You can capitalize every letter in the title.
  - Background appearance.
  - Button corner radius. You can use a corner radius value that matches the other buttons in your UI.
  - Button bezel and shadow. For example, you can use a stroke to emphasize the button bezel or add a drop shadow.

##### Custom buttons with a logo and text

- **Choose the format of the logo file based on the height of your button.**
  - «Use the PNG files only in buttons that are 44 points tall, which is the default (and recommended) button height in iOS.»
- **Prefer the system font for the title — that is, Sign in with Apple, Sign up with Apple, or Continue with Apple.**
- (imagen) An illustration of a Sign in with Apple button, with callouts that indicate a button height of 44 points and a font size of 19 points.
- (imagen) An illustration of a Sign in with Apple button, with callouts that indicate a button height of 56 points and a font size of 24 points.
- **In general, preserve the capitalization style of the title.**
  - «Avoid changing this style unless your interface uses only uppercase.»
- **Keep the title and logo vertically aligned within the button.**
- **Inset the logo if necessary.**
- **Maintain a minimum margin between the title and the right edge of the button.**
  - «Ensure the margin measures at least 8% of the button’s width.»
- **Maintain the minimum button size and margin around the button.**

| Minimum width | Minimum height | Minimum margin |
|---|---|---|
| 140 pt (140 px @1x, 280 px @2x) | 30 pt (30 px @1x, 60 px @2x) | 1/10 of the button’s height |

##### Custom logo-only buttons

- **Choose the format of the logo file based on the size of your button.**
- **Don’t add horizontal padding to a logo-only image.**
  - «A logo-only Sign in with Apple button always has a 1:1 aspect ratio, and the artwork already includes the correct padding on all sides.»
- **Use a mask to change the default square shape of the logo-only image.**
- **Maintain a minimum margin around the button.**
  - «Ensure the margin measures at least 1/10 of the button’s height.»

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Recursos relacionados

- *Related:*
  - [Sign in with Apple button](https://appleid.apple.com/signinwithapple/button)
- *Developer documentation:*
  - [Authentication Services](https://developer.apple.com/documentation/authenticationservices)
  - [Displaying Sign in with Apple buttons on the web](https://developer.apple.com/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web) — Sign in with Apple

## Vídeos que la explican

- [Move beyond passwords](https://developer.apple.com/videos/play/wwdc2021/10106) → `references/videos/2021-10106.md`
- [Simplify sign in for your tvOS apps](https://developer.apple.com/videos/play/wwdc2021/10279) → `references/videos/2021-10279.md`
- [Introducing Sign In with Apple](https://developer.apple.com/videos/play/wwdc2019/706) → `references/videos/2019-706.md`

## Registro de cambios

| Date | Changes |
|---|---|
| September 14, 2022 | Refined guidance on supporting existing accounts, helping people set up a new account, and indicating the current sign-in status. Consolidated guidance into one page. |
