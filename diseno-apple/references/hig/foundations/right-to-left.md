# Right to left — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/right-to-left
- Descargado: 2026-10-15
- Sección: foundations
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: sin registro de cambios

> Resumen de Apple: Support right-to-left languages like Arabic and Hebrew by reversing your interface as needed to match the reading direction of the related scripts.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- When people choose a language for their device — or just your app or game — they expect the interface to adapt in various ways (to learn more, see…
- System-provided UI frameworks support right-to-left (RTL) by default, allowing system-provided UI components to flip automatically in the RTL context.
- If you want to fine-tune your layout or enhance specific localizations to adapt to different currencies, numerals, or mathematical symbols that can occur in various locales in…

### Text alignment

- **Adjust text alignment to match the interface direction, if the system doesn’t do so automatically.**
- **Align a paragraph based on its language, not on the current context.**
  - ✅ Ejemplo correcto: A left-aligned paragraph in the RTL context
  - ❌ Ejemplo incorrecto: A right-aligned paragraph in the RTL context
- **Use a consistent alignment for all text items in a list.**
  - ✅ Ejemplo correcto: Right-aligned content in the RTL context
  - ❌ Ejemplo incorrecto: Mixed alignment in the RTL content

### Numbers and characters

- Different RTL languages can use different number systems.
- If your app covers mathematical concepts or other number-centric topics, it’s a good idea to identify the appropriate way to display such information in each locale you support.
- **Don’t reverse the order of numerals in a specific number.**
- **Reverse the order of numerals that show progress or a counting direction; never flip the numerals themselves.**

### Controls

- **Flip controls that show progress from one value to another.**
- **Flip controls that help people navigate or access items in a fixed order.**
- **Preserve the direction of a control that refers to an actual direction or points to an onscreen area.**
- **Visually balance adjacent Latin and RTL scripts when necessary.**
  - «To visually balance Arabic or Hebrew text with Latin text that uses all capitals, it often works well to increase the RTL font size by about 2 points.»

### Images

- **Avoid flipping images like photographs, illustrations, and general artwork.**
  - ✅ Ejemplo correcto: A simplified illustration of a globe that uses solid black shapes to show most of Africa, Europe, Asia, Australia, and Antarctica.
  - ❌ Ejemplo incorrecto: A simplified illustration of a globe that shows a horizontally flipped Eastern hemisphere with Africa on the far right and Australia on the far left.
- **Reverse the positions of images when their order is meaningful.**

### Interface icons

- When you use [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) to supply interface icons for your app, you get variants for the RTL context…
- **Flip interface icons that represent text or reading direction.**
- **Consider creating a localized version of an interface icon that displays text.**
- If you have a custom interface icon that uses letters or words to communicate a concept unrelated to reading or writing, consider designing an alternative image that doesn’t use…
- **Flip an interface icon that shows forward or backward motion.**
- **Don’t flip logos or universal signs and marks.**
- **In general, avoid flipping interface icons that depict real-world objects.**
  - «Unless you use the object to indicate directionality, it’s best to avoid flipping an icon that represents a familiar item.»
- **Before merely flipping a complex custom interface icon, consider its individual components and the overall visual balance.**
- In other cases, you might need to flip a component (or its position) to ensure the localized version of the icon still makes sense.
  - ✅ Ejemplo correcto: A silhouette of a wheeled shopping cart that faces right. A white plus sign inside a black disk is in the top-right corner.
  - ❌ Ejemplo incorrecto: A silhouette of a wheeled shopping cart that faces left. A white plus sign inside a black disk is in the top-right corner.
  - ✅ Ejemplo correcto: A silhouette of a wheeled shopping cart that faces left. A white plus sign inside a black disk is in the top-left corner.
- If your custom interface icon includes a component that can imply handedness, like a tool, consider preserving the orientation of the tool while flipping the base image if…
- (imagen) A rounded rectangle that contains a black dot in the top-right corner. The outline of a magnifying glass that contains a stack of two left-aligned lines is on top of the rectangle and to the left of the dot, slanted at about 135 degrees.
- (imagen) A rounded rectangle that contains a black dot in the top-left corner. The outline of a magnifying glass that contains a stack of two rightt-aligned lines is on top of the rectangle and to the right of the dot, slanted at about 135 degrees.

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Recursos relacionados

- *Related:*
  - [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
  - [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion)
  - [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols)
- *Developer documentation:*
  - [Localization](https://developer.apple.com/localization/)
  - [Preparing views for localization](https://developer.apple.com/documentation/swiftui/preparing-views-for-localization) — SwiftUI

## Vídeos que la explican

- [Enhance your app’s multilingual experience](https://developer.apple.com/videos/play/wwdc2025/222) → `references/videos/2025-222.md`
- [Design for Arabic](https://developer.apple.com/videos/play/wwdc2022/10034) → `references/videos/2022-10034.md`
