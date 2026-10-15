# Searching — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/searching
- Descargado: 2026-10-15
- Sección: patterns
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2026-06-08 — Updated terminology and refined best practices.

> Resumen de Apple: People use various search techniques to find content on their device, within an app, and within a document or file.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- To search for content within an app, people generally expect to use a [search field](https://developer.apple.com/design/human-interface-guidelines/search-fields).
- In some cases, people appreciate the ability to scope a search or filter the results.
- In iOS, iPadOS, and macOS, Spotlight helps people find content across all apps in the system and on the web.

### Best practices

- **If search is important, give it a primary position in your app or view.**
- **Aim to make your app’s content searchable through a single location.**
- **Clearly display the current scope of a search.**
- **Provide suggestions to make searching easier.**
- **Take privacy into consideration before displaying search history.**

### Systemwide search

- **Make your app’s content searchable in Spotlight.**
- **Define metadata for custom file types you handle.**
- **Use Spotlight to offer advanced file-search capabilities within the context of your app.**
- **Prefer using the system-provided open and save views.**
- **Implement a Quick Look generator if your app produces custom file types.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Recursos relacionados

- *Related:*
  - [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields)
- *Developer documentation:*
  - [Adding your app’s content to Spotlight indexes](https://developer.apple.com/documentation/corespotlight/adding-your-app-s-content-to-spotlight-indexes) — Core Spotlight

## Vídeos que la explican

- [Design intuitive search experiences](https://developer.apple.com/videos/play/wwdc2026/292) → `references/videos/2026-292.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 8, 2026 | Updated terminology and refined best practices. |
| June 9, 2025 | Updated best practices with general guidance from Search fields, and reorganized guidance for systemwide search. |
