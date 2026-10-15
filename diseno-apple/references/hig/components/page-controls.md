# Page controls — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/page-controls
- Descargado: 2026-10-15
- Sección: components › Presentation
- Plataformas: ios,ipados,tvos,visionos,watchos
- Última actualización: 2023-06-21 — Updated to include guidance for visionOS.

> Resumen de Apple: A page control displays a row of indicator images, each of which represents a page in a flat list.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- The scrolling row of indicators helps people navigate the list to find the page they want.
- Page controls appear as a series of small indicator dots by default, representing the available pages.

### Best practices

- **Use page controls to represent movement between an ordered list of pages.**
- **Center a page control at the bottom of the view or window.**
- **Although page controls can handle any number of pages, don’t display too many**

### Customizing indicators

- By default, a page control uses the system-provided dot image for all indicators, but it can also display a unique image to help people identify a specific page.
- If it enhances your app or game, you can provide a custom image to use as the default image for all indicators and you can also supply a different image for a specific page.
- **Make sure custom indicator images are simple and clear.**
- **Customize the default indicator image only when it enhances the page control’s overall meaning.**
- **Avoid using more than two different indicator images in a page control.**
  - ❌ Ejemplo incorrecto: An illustration that represents the Weather app highlighted to show a page control at the bottom edge of the screen. The page control displays a mix of icons, such as weak sun, cloud, cloud with…
  - ✅ Ejemplo correcto: An illustration that represents the Weather app highlighted to show a page control at the bottom edge of the screen. The page control displays the location symbol on the leading side followed by a…
- **Avoid coloring indicator images.**

### Platform considerations

- *Not supported in macOS.*

#### iOS, iPadOS

- A page control can adjust the appearance of indicators to provide more information about the list.
- People interact with page controls by tapping or scrubbing (to *scrub*, people touch the control and drag left or right).
> **Developer note:** In the API, *tapping* is a *discrete interaction*, whereas *scrubbing* is a *continuous interaction*; for developer guidance, see…
- **Avoid animating page transitions during scrubbing.**
- A page control can include a translucent, rounded-rectangle background appearance that provides visual contrast for the indicators.
  - Automatic — Displays the background only when people interact with the control. Use this style when the page control isn’t the primary navigational element in the UI.
  - Prominent — Always displays the background. Use this style only when the control is the primary navigational control in the screen.
  - Minimal — Never displays the background.
- For developer guidance, see [backgroundStyle](https://developer.apple.com/documentation/uikit/uipagecontrol/backgroundstyle-swift.property).
- **Avoid supporting the scrubber when you use the minimal background style.**

#### tvOS

- **Use page controls on collections of full-screen pages.**

#### visionOS

- In visionOS, page controls represent available pages and indicate the current page, but people don’t interact with them.

#### watchOS

- In watchOS, page controls can be displayed at the bottom of the screen for horizontal pagination, or next to the Digital Crown when presenting a vertical [tab…
- **Use vertical pagination to separate multiple views into distinct, purposeful pages.**
- **Consider limiting the content of an individual page to a single screen height.**

## Recursos relacionados

- *Related:*
  - [Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views)
- *Developer documentation:*
  - [PageTabViewStyle](https://developer.apple.com/documentation/swiftui/pagetabviewstyle) — SwiftUI
  - [UIPageControl](https://developer.apple.com/documentation/uikit/uipagecontrol) — UIKit

## Registro de cambios

| Date | Changes |
|---|---|
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Updated guidance for using page controls in watchOS. |
