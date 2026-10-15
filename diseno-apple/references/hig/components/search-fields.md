# Search fields — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/search-fields
- Descargado: 2026-10-15
- Sección: components › Navigation and search
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2026-06-08 — Updated terminology and refined guidance for search as a tab in iOS.

> Resumen de Apple: A search field lets people search a collection of content for specific terms they enter.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- A search field is an editable text field that displays a Search icon, a Clear button, and placeholder text where people can enter what they are searching for.
- For developer guidance, see [Adding a search interface to your app](https://developer.apple.com/documentation/swiftui/adding-a-search-interface-to-your-app); for guidance related…

### Best practices

- **Use placeholder text to help people know what they can search for.**
- **If possible, start search immediately when a person types.**
- **Consider showing suggested search terms.**
- **Simplify search results.**
- **Consider letting people filter search results.**

### Scope bars and tokens

- Scope bars and tokens are components you can use to let someone narrow the parameters of a search either before or after they make it.
  - A *scope bar* is a control for filtering and adjusting the scope of a search.
  - A *token* is a visual representation of a search term that someone can select and edit, and acts as a filter for any additional terms in the search.
- **Use a scope bar to filter among clearly defined search categories.**
- **Default to a broader scope and let people refine it as they need.**
- **Use tokens to filter by common search terms or items.**
- **Consider pairing tokens with search suggestions.**

### Platform considerations

- *No additional considerations for visionOS*.

#### iOS

- There are three main places you can position the entry point for search:
  - As a tab in a tab bar
  - In a toolbar at the bottom or top of the screen
  - Directly inline with content
- Where search makes the most sense depends on the layout, content, and navigation of your app.

##### Search as a tab

- You can place search as a tab in a tab bar, which keeps search visible and always available as people switch between the sections of your app.
  - **Standard tab.** This style displays the search tab uniformly with the rest of the tab bar.
  - **Button appearance.** This style displays the search tab as a separate button and allows people to start searching immediately.
- **Choose the standard tab style to provide suggestions, promote discovery, and encourage exploration.**
- **Choose the button appearance to help people quickly find what they need.**

##### Search in a toolbar

- As an alternative to search in a tab bar, you can also place search in a toolbar either at the bottom or top of the screen.
  - You can include search in a bottom toolbar either as an expanded field or as a toolbar button, depending on how much space is available.
  - You can include search in a top toolbar, also called a navigation bar, where it appears as a toolbar button.
- **Place search at the bottom if there’s room.**
- **Place search at the top when itʼs important to defer to content at the bottom of the screen, or thereʼs no bottom toolbar.**

##### Search as an inline field

- In some cases you might want your app to include a search field inline with content.
- **Place search as an inline field when its position alongside the content it searches strengthens that relationship.**
- **When at the top, position an inline search field above the list it searches, and consider pinning it to the top toolbar when scrolling.**

#### iPadOS, macOS

- The placement and behavior of the search field in iPadOS and macOS is similar.
- **Put a search field at the trailing side of the toolbar for many common uses.**
- **Include search at the top of the sidebar when filtering content or navigation there.**
- **Include search as an item in the sidebar or tab bar when you want an area dedicated to discovery.**
- **In a search field in a dedicated area, consider immediately focusing the field when a person navigates to the area to help them search faster and locate the field more easily.**
  - «An exception to this is on iPad when only a virtual keyboard is available, in which case it’s better to leave the field unfocused to prevent the keyboard from unexpectedly covering the view.»
- **Account for window resizing with the placement of the search field.**

#### tvOS

- A search screen is a specialized keyboard screen that helps people enter search text, displaying search results beneath the keyboard in a fully customizable view.
- **Provide suggestions to make searching easier.**

#### watchOS

- When someone taps the search field, the system displays a text-input control that covers the entire screen.

## Recursos relacionados

- *Related:*
  - [Searching](https://developer.apple.com/design/human-interface-guidelines/searching)
  - [Token fields](https://developer.apple.com/design/human-interface-guidelines/token-fields)
- *Developer documentation:*
  - [Adding a search interface to your app](https://developer.apple.com/documentation/swiftui/adding-a-search-interface-to-your-app) — SwiftUI
  - [searchable(text:placement:prompt:)](https://developer.apple.com/documentation/swiftui/view/searchable(text:placement:prompt:)) — SwiftUI
  - [UISearchBar](https://developer.apple.com/documentation/uikit/uisearchbar) — UIKit
  - [UISearchTextField](https://developer.apple.com/documentation/uikit/uisearchtextfield) — UIKit
  - [NSSearchField](https://developer.apple.com/documentation/appkit/nssearchfield) — AppKit

## Vídeos que la explican

- [Design intuitive search experiences](https://developer.apple.com/videos/play/wwdc2026/292) → `references/videos/2026-292.md`
- [Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356) → `references/videos/2025-356.md`
- [Discoverable design](https://developer.apple.com/videos/play/wwdc2021/10126) → `references/videos/2021-10126.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 8, 2026 | Updated terminology and refined guidance for search as a tab in iOS. |
| June 9, 2025 | Updated guidance for search placement in iOS, consolidated iPadOS and macOS platform considerations, and added guidance for tokens. |
| September 12, 2023 | Combined guidance common to all platforms. |
| June 5, 2023 | Added guidance for using search fields in watchOS. |
