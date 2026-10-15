# Drag and drop — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/drag-and-drop
- Descargado: 2026-10-15
- Sección: patterns
- Plataformas: ios,ipados,macos,visionos
- Última actualización: 2023-10-24 — Added artwork.

> Resumen de Apple: Using drag and drop, people can move or duplicate selected photos, text, and other content by dragging the selection from one location to another.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- To perform drag and drop, people select content in one location, called the *source*, and drop it in another, called the *destination*.
- Depending on various factors, the drag and drop action might *move* the selected content to the destination or *copy* it.
- People use different interactions to perform drag and drop depending on platform.
  - In visionOS, people pinch and hold a virtual object while dragging it to a new location in any direction, including along the z-axis.
  - iOS and iPadOS support drag and drop through gestures on the touchscreen, interactions with a pointing device, and through full keyboard-access mode.
  - Universal Control lets people drag content between their Mac and iPad.
  - On a Mac, people can interact with a pointing device, use full keyboard access mode, or use VoiceOver to perform drag and drop.

### Best practices

- **As much as possible, support drag and drop throughout your app.**
- **Offer alternative ways to accomplish drag-and-drop actions.**
- **Determine when dragging and dropping content within your app results in a move or a copy.**
- **Support multi-item drag and drop when it makes sense.**
- **Prefer letting people undo a drag-and-drop operation.**
- **Consider offering multiple versions of dragged content, ordered from highest to lowest fidelity.**
- **Consider supporting spring loading.**

### Providing feedback

- Drag and drop is a dynamic process that can result in multiple outcomes.
- **Display a drag image as soon as people drag a selection about three points.**
- **If it adds clarity, modify the drag image to help people predict the result of a drag-and-drop operation.**
- **Show people whether a destination can accept dragged content.**
- **When people drop an item on an invalid destination, or when dropping fails, provide visual feedback.**

### Accepting drops

- **Scroll the contents of a destination when necessary.**
- **When there’s a choice, pick the richest version of dropped content your app can accept.**
- **Extract only the relevant portion of dropped content if necessary.**
- **When a physical keyboard is attached, check for the Option key at drop time.**
- **Provide feedback when dropped content needs time to transfer.**
- **Provide feedback when dropped content initiates a task or action.**
- **Apply appropriate styling to dropped text.**
- **After a drop, maintain the content’s selection state in the destination, updating it in the source as needed.**

### Platform considerations

- *Not supported in tvOS or watchOS.*

#### iOS, iPadOS

- **Let people perform multiple simultaneous drag activities.**

#### macOS

- **Consider letting people drag content from your app into the Finder.**
- **Let people drag selected content from an inactive window without first making the window active.**
- **When possible, let people drag individual items from an inactive window without affecting an existing background selection.**
- **Consider displaying a badge during multi-item drag operations.**
- **Consider changing the pointer appearance to indicate what will happen when people drop content.**
- **As much as possible, let people select and drag content with a single motion.**
  - «Unless people are selecting multiple items, they appreciate it when they don’t have to pause between making a selection and starting the drag operation.»

#### visionOS

- **When possible, launch your app to handle content that people drop into empty space.**

## Recursos relacionados

- *Related:*
  - [Universal Control](https://support.apple.com/en-us/HT212757)
- *Developer documentation:*
  - [Drag and drop](https://developer.apple.com/documentation/uikit/drag-and-drop) — UIKit
  - [Drag and Drop](https://developer.apple.com/documentation/appkit/drag-and-drop) — AppKit
  - [File Provider](https://developer.apple.com/documentation/fileprovider)

## Vídeos que la explican

- [What's new in UIKit](https://developer.apple.com/videos/play/wwdc2021/10059) → `references/videos/2021-10059.md`
- [SwiftUI on the Mac: The finishing touches](https://developer.apple.com/videos/play/wwdc2021/10289) → `references/videos/2021-10289.md`
- [Designed for iPad](https://developer.apple.com/videos/play/wwdc2020/10206) → `references/videos/2020-10206.md`

## Registro de cambios

| Date | Changes |
|---|---|
| October 24, 2023 | Added artwork. |
| June 21, 2023 | Updated to include guidance for visionOS. |
