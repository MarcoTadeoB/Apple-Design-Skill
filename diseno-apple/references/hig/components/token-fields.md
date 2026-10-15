# Token fields — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/token-fields
- Descargado: 2026-10-15
- Sección: components › Navigation and search
- Plataformas: macos
- Última actualización: sin registro de cambios

> Resumen de Apple: A token field is a type of text field that can convert text into *tokens* that are easy to select and manipulate.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- For example, Mail uses token fields for the address fields in the compose window.
- You can configure a token field to present people with a list of suggestions as they enter text into the field.
- An individual token can also include a contextual menu that offers information about the token or editing options.
- Tokens can also represent search terms in some situations; for guidance, see [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields).

### Best practices

- **Add value with a context menu.**
- **Consider providing additional ways to convert text into tokens.**
- **Consider customizing the delay the system uses before showing suggested tokens.**

### Platform considerations

- *Not supported in iOS, iPadOS, tvOS, visionOS, and watchOS.*

## Recursos relacionados

- *Related:*
  - [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields)
  - [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields)
  - [Context menus](https://developer.apple.com/design/human-interface-guidelines/context-menus)
- *Developer documentation:*
  - [NSTokenField](https://developer.apple.com/documentation/appkit/nstokenfield) — AppKit
