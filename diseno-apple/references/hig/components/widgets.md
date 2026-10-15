# Widgets — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/widgets
- Descargado: 2026-10-15
- Sección: components › System experiences
- Plataformas: ios,ipados,macos,watchos,visionos
- Última actualización: 2026-10-13 — Added guidance for Apple HomeView, and updated watchOS specifications.

> Resumen de Apple: A widget provides quick access to essential information and focused interactions from your app or game in additional contexts.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Widgets help people organize and personalize their devices by displaying timely, glanceable content and offering specific functionality.
  - On the Home Screen and Lock Screen of their iPhone and iPad
  - On the desktop and Notification Center of their Mac
  - On a horizontal or vertical surface when they wear Apple Vision Pro
  - At a fixed position in the Smart Stack of Apple Watch
  - On the Home Screen and Modular face of Apple HomeView

### Anatomy

- Widgets come in different sizes, ranging from small accessory widgets on iPad, iPhone, and Apple Watch to system family widgets that include an extra large size on iPad, Mac, and…
  - The widget size to support
  - The context — devices and system experiences — in which the widget may appear
  - The rendering modes and color treatment that the widget receives based on the size and context
- The WidgetKit framework provides default appearances and treatments for each widget size to fit the system experience or device where it appears.

#### System family widgets

- System family widgets offer a broad range of sizes and may include one or more interactive elements.
- The following table shows supported contexts for each system family widget size:

| Widget size | iPhone | iPad | Mac | Apple Vision Pro |
|---|---|---|---|---|
| System small | Home Screen, Today View, StandBy, CarPlay, and Apple HomeView | Home Screen, Today View, and Lock Screen | Desktop and Notification Center | Horizontal and vertical surfaces |
| System medium | Home Screen and Today View | Home Screen and Today View | Desktop and Notification Center | Horizontal and vertical surfaces |
| System large | Home Screen and Today View | Home Screen and Today View | Desktop and Notification Center | Horizontal and vertical surfaces |
| System extra large | Not supported | Home Screen and Today View | Desktop and Notification Center | Horizontal and vertical surfaces |
| System extra large portrait | Not supported | Not supported | Not supported | Horizontal and vertical surfaces |

#### Accessory widgets

- Accessory widgets display a very limited amount of information because of their size.
- They appear on the following devices:

| Widget size | iPhone | iPad | Apple Watch |
|---|---|---|---|
| Accessory circular | Lock Screen | Lock Screen | Watch complications and in the Smart Stack |
| Accessory corner | Not supported | Not supported | Watch complications |
| Accessory inline | Lock Screen | Lock Screen | Watch complications |
| Accessory rectangular | Lock Screen | Lock Screen | Watch complications and in the Smart Stack |

#### Appearances

- A widget can appear in full-color, in monochrome with a tint color, or in a clear, translucent style.
- For example, a small system widget appears differently depending on the device and location:
  - On the Home Screen of iPad, iPhone, and Apple HomeView, people choose from different appearances for widgets: light, dark, clear, and tinted.
  - On Apple Vision Pro, the widget appears as a 3D object, surrounded by a frame.
  - On the Lock Screen of iPad, the widget takes on a monochromatic appearance without a tint color.
  - On the Lock Screen of iPhone in StandBy and the Modular face of Apple HomeView, the widget appears scaled up in size with the background removed.
- Similarly, a rectangular accessory widget appears as follows:
  - On the Lock Screen of iPhone and iPad, it takes on a monochromatic appearance without a tint color.
  - On Apple Watch, the widget can appear as a watch complication in both full-color and tinted appearances, and it can also appear in the Smart Stack.
- Each appearance described above includes a [rendering mode](https://developer.apple.com/design/human-interface-guidelines/widgets#Rendering-modes) that depends on the platform…
  - The system uses the [full color](https://developer.apple.com/documentation/widgetkit/widgetrenderingmode/fullcolor) rendering mode for system family widgets across all platforms…
  - The system uses the [accented](https://developer.apple.com/documentation/widgetkit/widgetrenderingmode/accented) rendering mode for system family widgets across all platforms and…
  - The system uses the [vibrant](https://developer.apple.com/documentation/widgetkit/widgetrenderingmode/vibrant) rendering mode for widgets on the Lock Screen of iPhone and iPad,…
- The following table lists the occurrences for each rendering mode per platform:

| Platform | Full-color | Accented | Vibrant |
|---|---|---|---|
| iPhone | Home Screen, Today view, StandBy and CarPlay (with the background removed) | Home Screen and Today view | Lock Screen, StandBy in Night Mode |
| iPad | Home Screen and Today view | Home Screen and Today view | Lock Screen |
| Apple Watch | Smart Stack, complications | Smart Stack, complications | Not supported |
| Mac | Desktop and Notification Center | Not supported | Desktop |
| Apple Vision Pro | Horizontal and vertical surfaces | Horizontal and vertical surfaces | Not supported |
| Apple HomeView | Home Screen, Modular face (with the background removed) | Home Screen, Modular face (with the background removed) | Modular face in Night Mode |

- For additional design guidance, see [Rendering modes](https://developer.apple.com/design/human-interface-guidelines/widgets#Rendering-modes).

### Best practices

- **Choose simple ideas that relate to your app’s main purpose.**
- (imagen) An image of a small Weather widget showing current conditions for Cupertino. In text, the widget displays a temperature of 70 degrees, the condition Sunny, and forecast high and low temperatures of 75 degrees and 59 degrees, respectively. The widget also displays a yellow sun symbol above the word Sunny and the filled-in location indicator to the right of the word Cupertino.
- **Aim to create a widget that gives people quick access to the content they want.**
- **Prefer dynamic information that changes throughout the day.**
- **Look for opportunities to surprise and delight.**
- **Offer widgets in multiple sizes when doing so adds value.**
- **Balance information density.**
- **Display only the information that’s directly related to the widget’s main purpose.**
- **Use brand elements thoughtfully.**
- **Choose between automatically displaying content and letting people customize displayed information.**
- **Avoid mirroring your widget’s appearance within your app.**
- **Let people know when authentication adds value.**

#### Updating widget content

- To remain relevant and useful, widgets periodically refresh their information but don’t support continuous, real-time updates, and the system may adjust the limits for updates…
- **Keep your widget up to date.**
- **Use system functionality to refresh dates and times in your widget.**
- **Use animated transitions to bring attention to data updates.**

#### Adding interactivity

- People tap or click a widget to launch its corresponding app.
- **Offer simple, relevant functionality and reserve complexity for your app.**
- **Ensure that a widget interaction opens your app at the right location.**
- **Offer interactivity while remaining glanceable and uncluttered.**

#### Choosing margins and padding

- Widgets scale to adapt to the screen sizes of different devices and onscreen areas.
- As you design for various devices and scale factors, use the values listed in…
- **In general, use standard margins to ensure legibility.**
  - «Use the standard margin width for widgets — 16 points for most widgets — to avoid crowding their edges and creating a cluttered appearance.»
  - «If you need to use tighter margins — for example, to create content groupings for graphics, buttons, or background shapes — setting margins of 11 points can work well.»
- **Coordinate the corner radius of your content with the corner radius of the widget.**

#### Displaying text in widgets

- **Prefer using the system font, text styles, and SF Symbols.**
- **Avoid very small font sizes.**
  - «In general, display text using fonts at 11 points or larger.»
  - «Text in a font that’s smaller than 11 points can be too hard for many people to read.»
- **Avoid rasterizing text.**
> **Note:** In iOS, iPadOS, and visionOS, widgets support Dynamic Type sizes from Large to AX5 when you use [Font](https://developer.apple.com/documentation/swiftui/font) to choose a system font or…

#### Using color

- **Use color to enhance a widget’s appearance without competing with its content.**
- **Convey meaning without relying on specific colors to represent information.**
- **Use full-color images judiciously.**

### Rendering modes

#### Full-color

- **Support light and dark appearances.**

#### Accented

- **Group widget components into an accented and a primary group.**
- For developer guidance, see [widgetAccentable(_:)](https://developer.apple.com/documentation/swiftui/view/widgetaccentable(_:)) and [Optimizing your widget for accented rendering…

#### Vibrant

- **Offer enough contrast to ensure legibility.**
- **Create optimized assets for the best vibrant effect.**

### Previews and placeholders

- **Design a realistic preview to display in the widget gallery.**
- **Design placeholder content that helps people recognize your widget.**
- **Write a succinct widget description.**
- **Group your widget’s sizes together, and provide a single description.**
- **Consider coloring the Add button.**

### Platform considerations

- *No additional considerations for macOS.

#### iOS, iPadOS

- Widgets on the Lock Screen are functionally similar to watch complications and follow design principles for…
- Your app can offer widgets on the Lock Screen in three different styles: as inline text that appears above the clock, and as circular and rectangular shapes that appear below the…
- **Support the Always-On display on iPhone.**
- For developer guidance, see [Creating accessory widgets and watch…
- **Offer Live Activities to show real-time updates.**

##### StandBy and CarPlay

- On iPhone in StandBy, the system displays two small system family widgets side-by-side, scaled up so they fill the Lock Screen.
- **Limit usage of rich images or color to convey meaning in StandBy.**

**Pestaña «Correct usage»**

- (imagen) An image of iPhone in StandBy. It shows a Clock widget on the left that displays the time as 9:41 a.m. and a Weather widget set to Cupertino with the temperature at 70 degrees Fahrenheit on the right.
- ✅ (correcto)

**Pestaña «Incorrect usage»**

- (imagen) An image of iPhone in StandBy. It shows a Clock widget on the left that displays the time as 9:41 a.m. and a Weather widget set to Cupertino with the temperature at 70 degrees Fahrenheit on the right. The Watch widget appears with the background removed and the Weather widget isn't optimized for StandBy.
- ❌ (incorrecto)
- On iPhone in StandBy in low-light conditions, the system renders widgets in a monochromatic look with a red tint.
- (imagen) An image of iPhone in low-light conditions. It shows a Clock widget on the left that displays the time as 9:41 a.m. and a Weather widget set to Cupertino with the temperature at 70 degrees Fahrenheit on the right.

##### Apple HomeView

- On Apple HomeView, people can place widgets on the Modular face and the Home Screen.
  - The Modular face can include up to four widgets, which can be from the iPhone devices of different household members.
  - The Home Screen contains a personalized set of widgets and apps, which can include the defaults that come with HomeView along with those that a person chooses to display from…

#### visionOS

- Widgets in visionOS are 3D objects that people place on a horizontal or vertical surface.
- visionOS widgets appear in full-color by default, but they appear in the accented rendering mode when people personalize them with tint colors using a range of system-provided…
- For developer guidance, see [Updating your widgets for visionOS](https://developer.apple.com/documentation/widgetkit/updating-your-widgets-for-visionos).
- **Adapt your design and content for the spatial experience Apple Vision Pro provides.**
- **Test your widgets across the full range of system color palettes and in different lighting conditions.**

##### Thresholds and sizes

- Widgets on Apple Vision Pro can adapt based on a person’s proximity, and visionOS provides widgets with two key thresholds to design for: the…
- Because widgets can appear throughout a person’s environment, it’s also important to match a widget’s size to the type of content it contains, and to be aware of how it appears…
- **Design a responsive layout that shows the right level of detail for each of the two thresholds.**
- **Offer widget family sizes that fit a person’s surroundings well.**
- **Display content in a way that remains legible from a range of distances.**
  - «To make a widget feel intentional and proportionate to where they place it, people can scale a widget from 75 to 125 percent in size.»

##### Mounting styles

- The way a widget appears on a surface plays a big role in how a person perceives it.
  - **[Elevated](https://developer.apple.com/documentation/widgetkit/widgetmountingstyle/elevated) style**.
  - **[Recessed](https://developer.apple.com/documentation/widgetkit/widgetmountingstyle/recessed) style**.
- By default, widgets use the elevated mounting style, because it works for horizontal and vertical surfaces.
- **Choose the mounting style that fits your content and the experience you want to create.**
> **Developer note:** Use the [supportedMountingStyles(_:)](https://developer.apple.com/documentation/swiftui/widgetconfiguration/supportedmountingstyles(_:)) property of your…
- **Test your elevated widget designs with each system-provided frame width.**

##### Treatment styles

- In addition to size and mounting style, the system applies one of two treatment styles to visionOS widgets.
  - The [paper](https://developer.apple.com/documentation/widgetkit/widgettexture/paper) style creates a more grounded, print-like style that feels solid and makes the widget feel…
  - The [glass](https://developer.apple.com/documentation/widgetkit/widgettexture/glass) style creates a lighter, layered look that adds depth and visual separation between…
- **Choose the paper style for a print-like look that feels more like a real object in the room.**
- **Choose the glass style for information-rich widgets.**

#### watchOS

- **Provide a colorful background that conveys meaning.**
- **Encourage the system to display or elevate the position of your watchOS widget in the Smart Stack.**

### Specifications

- As you design your widgets, use the following values for guidance.

#### iOS dimensions

| Screen size (portrait, pt) | Small (pt) | Medium (pt) | Large (pt) | Circular (pt) | Rectangular (pt) | Inline (pt) |
|---|---|---|---|---|---|---|
| 430×932 | 170x170 | 364x170 | 364x382 | 76x76 | 172x76 | 257x26 |
| 428x926 | 170x170 | 364x170 | 364x382 | 76x76 | 172x76 | 257x26 |
| 414x896 | 169x169 | 360x169 | 360x379 | 76x76 | 160x72 | 248x26 |
| 414x736 | 159x159 | 348x157 | 348x357 | 76x76 | 170x76 | 248x26 |
| 393x852 | 158x158 | 338x158 | 338x354 | 72x72 | 160x72 | 234x26 |
| 390x844 | 158x158 | 338x158 | 338x354 | 72x72 | 160x72 | 234x26 |
| 375x812 | 155x155 | 329x155 | 329x345 | 72x72 | 157x72 | 225x26 |
| 375x667 | 148x148 | 321x148 | 321x324 | 68x68 | 153x68 | 225x26 |
| 360x780 | 155x155 | 329x155 | 329x345 | 72x72 | 157x72 | 225x26 |
| 320x568 | 141x141 | 292x141 | 292x311 | N/A | N/A | N/A |

#### iPadOS dimensions

| Screen size (portrait, pt) | Target | Small (pt) | Medium (pt) | Large (pt) | Extra large (pt) |
|---|---|---|---|---|---|
| 768x1024 | Canvas | 141x141 | 305.5x141 | 305.5x305.5 | 634.5x305.5 |
|  | Device | 120x120 | 260x120 | 260x260 | 540x260 |
| 744x1133 | Canvas | 141x141 | 305.5x141 | 305.5x305.5 | 634.5x305.5 |
|  | Device | 120x120 | 260x120 | 260x260 | 540x260 |
| 810x1080 | Canvas | 146x146 | 320.5x146 | 320.5x320.5 | 669x320.5 |
|  | Device | 124x124 | 272x124 | 272x272 | 568x272 |
| 820x1180 | Canvas | 155x155 | 342x155 | 342x342 | 715.5x342 |
|  | Device | 136x136 | 300x136 | 300x300 | 628x300 |
| 834x1112 | Canvas | 150x150 | 327.5x150 | 327.5x327.5 | 682x327.5 |
|  | Device | 132x132 | 288x132 | 288x288 | 600x288 |
| 834x1194 | Canvas | 155x155 | 342x155 | 342x342 | 715.5x342 |
|  | Device | 136x136 | 300x136 | 300x300 | 628x300 |
| 954x1373 * | Canvas | 162x162 | 350x162 | 350x350 | 726x350 |
|  | Device | 162x162 | 350x162 | 350x350 | 726x350 |
| 970x1389 * | Canvas | 162x162 | 350x162 | 350x350 | 726x350 |
|  | Device | 162x162 | 350x162 | 350x350 | 726x350 |
| 1024x1366 | Canvas | 170x170 | 378.5x170 | 378.5x378.5 | 795x378.5 |
|  | Device | 160x160 | 356x160 | 356x356 | 748x356 |
| 1192x1590 * | Canvas | 188x188 | 412x188 | 412x412 | 860x412 |
|  | Device | 188x188 | 412x188 | 412x412 | 860x412 |

#### visionOS dimensions

| Widget | Size in pt | Size in mm (scaled to 100%) |
|---|---|---|
| Small | 158x158 | 268x268 |
| Medium | 338x158 | 574x268 |
| Large | 338x354 | 574x600 |
| Extra large | 450x338 | 763x574 |
| Extra large portrait | 338x450 | 574x763 |

#### watchOS dimensions

| Apple Watch size | Size of a widget in the Smart Stack (pt) |
|---|---|
| 40mm | 152x69.5 |
| 41mm | 165x72.5 |
| 42mm | 176x72.5 |
| 44mm | 173x76.5 |
| 45mm | 184x80.5 |
| 46mm | 194x80.5 |
| 49mm (Ultra 3, 4) | 198x81.5 |
| 49mm (Ultra 1, 2) | 191x81.5 |

## Recursos relacionados

- *Related:*
  - [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- *Developer documentation:*
  - [WidgetKit](https://developer.apple.com/documentation/widgetkit)
  - [Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy) — WidgetKit

## Vídeos que la explican

- [WidgetKit foundations](https://developer.apple.com/videos/play/wwdc2026/277) → `references/videos/2026-277.md`
- [What’s new in widgets](https://developer.apple.com/videos/play/wwdc2025/278) → `references/videos/2025-278.md`
- [Design widgets for visionOS](https://developer.apple.com/videos/play/wwdc2025/255) → `references/videos/2025-255.md`

## Registro de cambios

| Date | Changes |
|---|---|
| October 13, 2026 | Added guidance for Apple HomeView, and updated watchOS specifications. |
| December 16, 2025 | Updated guidance for all platforms, and added guidance for visionOS and CarPlay. |
| January 17, 2025 | Corrected watchOS widget dimensions. |
| June 10, 2024 | Updated to include guidance for accented widgets in iOS 18 and iPadOS 18. |
| June 5, 2023 | Updated guidance to include widgets in watchOS, widgets on the iPad Lock Screen, and updates for iOS 17, iPadOS 17, and macOS 14. |
| November 3, 2022 | Added guidance for widgets on the iPhone Lock Screen and updated design comprehensives for iPhone 14, iPhone 14 Pro, and iPhone 14 Pro Max. |
