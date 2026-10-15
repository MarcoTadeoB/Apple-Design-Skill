# Charts — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/charts
- Descargado: 2026-10-15
- Sección: components › Content
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2022-09-23 — New page.

> Resumen de Apple: Organize data in a chart to communicate information with clarity and visual appeal.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- An effective chart highlights a few key pieces of information in a dataset, helping people gain insights and make decisions.
  - Learn how upcoming weather conditions might affect their plans.
  - Analyze stock prices to understand past performance and discover trends.
  - Review fitness data to monitor their progress and set new goals.
- To learn about designing charts to enhance your experience, see [Charting data](https://developer.apple.com/design/human-interface-guidelines/charting-data); for developer…

### Anatomy

- A chart comprises several graphical elements that depict the values in a dataset and convey information about them.
- A *mark* is a visual representation of a data value.
- To depict a value, each type of mark uses visual attributes that are determined by a scale, which maps data values like numbers, dates, or categories to visual characteristics…
- To give people the context they need to interpret a chart’s visual characteristics, you supply descriptive content that can take a few different forms.
- You can use an *axis* to help define a frame of reference for the data represented by a set of marks.
- An axis can include *ticks*, which are reference points that help people visually locate the position of important values along the axis, such as a 0, 50%, and 100%.
- You also have multiple ways to describe chart elements to help people interpret the data and to highlight the key information you want to communicate.
- Clear, accurate descriptions can help make a chart more approachable and accessible; to learn about additional ways to improve the accessibility of your chart, see [Enhancing the…

### Marks

- **Choose a mark type based on the information you want to communicate about the data.**
- *Bar* marks work well in charts that help people compare values in different categories or view the relative proportions of various parts in a whole.
- *Line* marks can also show how values change over time.
- *Point* marks help you depict individual data values as visually distinct marks.
- **Consider combining mark types when it adds clarity to your chart.**

### Axes

- **Use a fixed or dynamic axis range depending on the meaning of your chart.**
  - «For example, people expect a chart that shows a battery’s current charge to have a minimum value of 0% (completely empty) and a maximum value of 100% (completely full).»
- In contrast, consider using a dynamic range when the possible data values can vary widely and you want the marks to fill the available plot area.
- **Define the value of the lower bound based on mark type and chart usage.**
- **Prefer familiar sequences of values in the tick and grid-line labels for an axis.**
- **Tailor the appearance of grid lines and labels to a chart’s use cases.**

### Descriptive content

- **Write descriptions that help people understand what a chart does before they view it.**
- **Summarize the main message of your chart to help make it approachable and useful for everyone.**

### Best practices

- **Establish a consistent visual hierarchy that helps communicate the relative importance of various chart elements.**
- **In a compact environment, maximize the width of the plot area to give people enough space to comfortably examine a chart.**
- **Make every chart in your app accessible.**
- **Let people interact with the data when it makes sense, but don’t require interaction to reveal critical information.**
- **Make it easy for everyone to interact with a chart.**
- **Make an interactive chart easy to navigate when using keyboard commands (including full keyboard access) or Switch Control.**
- **Help people notice important changes in a chart.**
- **Align a chart with surrounding interface elements.**

### Color

- As in all other parts of your interface, using color in a chart can help you clarify information, evoke your brand, and provide visual continuity.
- **Avoid relying solely on color to differentiate between different pieces of data or communicate essential information in a chart.**
- **Aid comprehension by adding visual separation between contiguous areas of color.**

### Enhancing the accessibility of a chart

- When you use Swift Charts to create a chart, you get a default implementation of [Audio graphs](https://developer.apple.com/documentation/accessibility/audio-graphs), in addition…
- **Consider using Audio Graphs to give VoiceOver users more information about your chart.**
> **Important:** Unlike an image — which requires one descriptive accessibility label — a chart often needs to offer an accessibility label for each important or interactive element.
- **Write accessibility labels that support the purpose of your chart.**
- The following guidelines can help you write useful accessibility labels for chart elements.
  - **Prioritize clarity and comprehensiveness.** In general, it’s rarely enough to merely report a data value unless you also include context that helps people understand it, like…
  - **Avoid using subjective terms.** Subjective words — like rapidly, gradually, and almost — communicate your interpretation of the data.
  - **Maximize clarity in data descriptions by avoiding potentially ambiguous formats and abbreviations.** For example, using “June 6” is clearer than using “6/6”; similarly,…
  - **Describe what the chart’s details represent, not what they look like.** Consider a chart that uses red and blue colors to help people visually distinguish two different data…
  - **Be consistent throughout your app when referring to a specific axis.** For example, if you always mention the X axis first, people can spend less time figuring out which axis…
- **Hide visible text labels for axes and ticks from assistive technologies.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS.*

#### watchOS

- **In general, avoid requiring complex chart interactions in your watchOS app.**

## Recursos relacionados

- *Related:*
  - [Charting data](https://developer.apple.com/design/human-interface-guidelines/charting-data)
- *Developer documentation:*
  - [Swift Charts](https://developer.apple.com/documentation/charts)

## Vídeos que la explican

- [Bring Swift Charts to the third dimension](https://developer.apple.com/videos/play/wwdc2025/313) → `references/videos/2025-313.md`
- [Design app experiences with charts](https://developer.apple.com/videos/play/wwdc2022/110342) → `references/videos/2022-110342.md`
- [Design an effective chart](https://developer.apple.com/videos/play/wwdc2022/110340) → `references/videos/2022-110340.md`

## Registro de cambios

| Date | Changes |
|---|---|
| September 23, 2022 | New page. |
