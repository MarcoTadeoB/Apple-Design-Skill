# Tab views — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/tab-views
- Descargado: 2026-10-15
- Sección: components › Layout and organization
- Plataformas: macos,watchos
- Última actualización: 2023-06-05 — Added guidance for using tab views in watchOS.

> Resumen de Apple: A tab view presents multiple mutually exclusive panes of content in the same area, which people can switch between using a tabbed control.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
### Best practices

- **Use a tab view to present closely related areas of content.**
- **Make sure the controls within a pane affect content only in the same pane.**
- **Provide a label for each tab that describes the contents of its pane.**
- **Avoid using a pop-up button to switch between tabs.**
- **Avoid providing more than six tabs in a tab view.**
- For developer guidance, see [NSTabView](https://developer.apple.com/documentation/appkit/nstabview).

### Anatomy

- The tabbed control appears on the top edge of the content area.
- When you hide the tabbed control, the content area can be borderless, bezeled, or bordered with a line.
- **In general, inset a tab view by leaving a margin of window-body area on all sides of a tab view.**

### Platform considerations

- *Not supported in iOS, iPadOS, tvOS, or visionOS.*

#### iOS, iPadOS

- For similar functionality, consider using a [segmented control](https://developer.apple.com/design/human-interface-guidelines/segmented-controls) instead.

#### watchOS

- watchOS displays tab views using [page controls](https://developer.apple.com/design/human-interface-guidelines/components/presentation/page-controls).

## Recursos relacionados

- *Related:*
  - [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars)
  - [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)
- *Developer documentation:*
  - [TabView](https://developer.apple.com/documentation/swiftui/tabview) — SwiftUI
  - [NSTabView](https://developer.apple.com/documentation/appkit/nstabview) — AppKit

## Registro de cambios

| Date | Changes |
|---|---|
| June 5, 2023 | Added guidance for using tab views in watchOS. |
