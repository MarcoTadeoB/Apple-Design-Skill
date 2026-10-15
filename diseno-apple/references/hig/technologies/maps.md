# Maps — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/maps
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2024-12-18 — Added guidance for place cards and included additional artwork.

> Resumen de Apple: A map displays outdoor or indoor geographical data in your app or on your website.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- A map uses a familiar interface that supports much of the same functionality as the system-provided Maps app, such as zooming, panning, and rotation.

### Best practices

- **In general, make your map interactive.**
- **Pick a map emphasis style that suits the needs of your app.**
  - The *default* style presents a version of the map with fully saturated colors, and is a good option for most standard map applications without a lot of custom elements.
  - The *muted* style, by contrast, presents a desaturated version of the map.
- For developer guidance, see [MKStandardMapConfiguration.EmphasisStyle](https://developer.apple.com/documentation/mapkit/mkstandardmapconfiguration/emphasisstyle-swift.enum).
- **Help people find places in your map.**
- **Clearly identify elements that people select.**
- **Cluster overlapping points of interest to improve map legibility.**
- **Help people see the Apple logo and legal link.**
  - Use adequate padding to separate the logo and link from the map boundaries and your custom controls.
  - Avoid causing the logo and link to move with your interface. It’s best when the Apple logo and legal link appear to be fixed to the map.
  - If your custom interface can move relative to the map, use the lowest position of the custom element to determine the placement of the logo and link.
> **Note:** The Apple logo and legal link aren’t shown on maps that are smaller than 200x100 pixels.

### Custom information

- **Use annotations that match the visual style of your app.**
- **If you want to display custom information that’s related to standard map features, consider making them independently selectable.**
- **Use overlays to define map areas with a specific relationship to your content.**
  - *Above roads*, the default level, places the overlay above roads but below buildings, trees, and other features.
  - *Above labels* places the overlay above both roads and labels, hiding everything beneath it.
- For developer guidance, see [Displaying overlays on a map](https://developer.apple.com/documentation/mapkit/displaying-overlays-on-a-map) and…
- **Make sure there’s enough contrast between custom controls and the map.**

### Place cards

- Place cards display rich place information in your app or website, such as operating hours, phone numbers, addresses, and more.

#### Displaying place cards in a map

- You can present a place card that appears directly in your map anytime someone selects a place.
- You can also display place cards for other places on a map, such as points of interest, territories, and physical features, to provide valuable context to people about nearby…
> **Developer note:** In websites, you can embed a custom map that displays a place card by default for a single place that you specify.
- The system defines several place card styles, which specify the size, appearance, and information included in a place card.
  - The *automatic* style lets the system determine the place card style based on the size of your map view.
  - The *callout* style displays a place card in a popover style next to the selected place.
  - The *caption* style displays an “Open in Apple Maps” link.
  - The *sheet* style displays a place card in a [sheet](https://developer.apple.com/design/human-interface-guidelines/sheets).
- For developer guidance, see [MapItemDetailSelectionAccessoryStyle](https://developer.apple.com/documentation/mapkit/mapitemdetailselectionaccessorystyle),…
- Full callout style place cards appear differently depending on a person’s device.
- **Consider your map presentation when choosing a style.**
- **Make sure your place card looks great on different devices and window sizes.**
- **Avoid duplicating information.**
- **Keep the location on your map visible when displaying a place card.**

#### Adding place cards outside of a map

- You can also display place information outside of a map in your app or website.
> **Important:** If you don’t display a place card directly within a map view, you must include a map in the place card.
- **Use location-related cues in surrounding content to help communicate that people can open a place card.**

### Indoor maps

- Apps connected with specific venues like shopping malls and stadiums can design custom interactive maps that help people locate and navigate to indoor points of interest.
- **Adjust map detail based on the zoom level.**
- **Use distinctive styling to differentiate the features of your map.**
- **Offer a floor picker if your venue includes multiple levels.**
- **Include surrounding areas to provide context.**
- **Consider supporting navigation between your venue and nearby transit points.**
- **Limit scrolling outside of your venue.**
- **Design an indoor map that feels like a natural extension of your app.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.*

#### watchOS

- On Apple Watch, maps are static snapshots of geographic locations.
- **Fit the map interface element to the screen.**
- **Show the smallest region that encompasses the points of interest.**
- For developer guidance, see [WKInterfaceMap](https://developer.apple.com/documentation/watchkit/wkinterfacemap).

## Recursos relacionados

- *Developer documentation:*
  - [MapKit](https://developer.apple.com/documentation/mapkit)
  - [MapKit JS](https://developer.apple.com/documentation/mapkitjs)
  - [Indoor Mapping Data Format](https://register.apple.com/resources/imdf/)

## Vídeos que la explican

- [Go further with MapKit](https://developer.apple.com/videos/play/wwdc2025/204) → `references/videos/2025-204.md`
- [Unlock the power of places with MapKit](https://developer.apple.com/videos/play/wwdc2024/10097) → `references/videos/2024-10097.md`

## Registro de cambios

| Date | Changes |
|---|---|
| December 18, 2024 | Added guidance for place cards and included additional artwork. |
| September 12, 2023 | Added artwork. |
| September 23, 2022 | Added guidelines for presenting custom information, refined best practices, and consolidated guidance into one page. |
