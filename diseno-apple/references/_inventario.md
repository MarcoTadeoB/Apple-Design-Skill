# Inventario de fuentes descargadas

Fechas de descarga: 2026-10-15

## Human Interface Guidelines

- Páginas descargadas: **172** + la raíz (173 archivos JSON).
  - components: 73 (incluye la página índice de la sección)
  - foundations: 19 (incluye la página índice de la sección)
  - getting-started: 10 (incluye la página índice de la sección)
  - inputs: 14 (incluye la página índice de la sección)
  - patterns: 26 (incluye la página índice de la sección)
  - raíz: 1
  - technologies: 30 (incluye la página índice de la sección)
- Fallos: 1
  - `spatial-interactions` — https://developer.apple.com/tutorials/data/design/human-interface-guidelines/spatial-interactions.json: HTTP Error 404: Not Found → Enlace roto en «Designing for iOS»: la página no existe (404 en JSON). No hay contenido que recuperar.

## Páginas web de diseño (no HIG)

- Descargadas: **84**
  - páginas de diseño, herramientas, premios y marcas: 19
  - historias/noticias (news, articles): 65
- Fallos: 4
  - https://developer.apple.com/augmented-reality/reality-composer-pro/ — https://developer.apple.com/augmented-reality/reality-composer-pro/: HTTP Error  → URL antigua (404); sustituida por https://developer.apple.com/reality-composer-pro/ (descargada).
  - https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html — https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html:  → Dominio bloqueado por la política de red del entorno (403 del proxy). Hay que permitir www.apple.com y volver a ejecutar descargar_paginas.py.
  - https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html — https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html: <u → Dominio bloqueado por la política de red del entorno (403 del proxy). Hay que permitir www.apple.com y volver a ejecutar descargar_paginas.py.
  - https://developer.apple.com/design/awards/2019/ — https://developer.apple.com/design/awards/2019/: HTTP Error 403: Forbidden → Apple devuelve 403 Forbidden: la página de ganadores de 2019 ya no está publicada.

## Vídeos

- En la lista oficial https://developer.apple.com/videos/design/: **192**
- Total procesados (lista + enlazados desde HIG y páginas de diseño): **289**
  - videos/design: 192
  - solo HIG: 90
  - páginas de diseño / otros: 7
- Por evento: wwdc2026 34, wwdc2025 44, wwdc2024 18, wwdc2023 31, wwdc2022 28, wwdc2021 39, wwdc2020 27, wwdc2019 22, wwdc2018 6, wwdc2017 15, wwdc2016 1, wwdc2015 2, wwdc2014 2, tech-talks 9, meet-with-apple 11
- Con transcripción: **271** · Sin transcripción: **18** → Apple no publica transcripción para estas sesiones (Q&A, «Meet the Presenter», laboratorios en grupo y dos sesiones antiguas): el bloque de transcripción de la página está vacío (comprobado en el HTML).
  - meet-with-apple/285 — iPhone Duo Group Lab
  - meet-with-apple/286 — iPhone Duo Group Lab
  - meet-with-apple/287 — iPhone Duo Group Lab
  - meet-with-apple/288 — iPhone Duo Group Lab
  - wwdc2019/801 — What’s New in iOS and macOS Design
  - wwdc2020/20022 — The winners of the 2020 Apple Design Awards
  - wwdc2022/10175 — Q&A: Prototyping
  - wwdc2022/110484 — Meet the Presenter: Explore design navigation on iOS
  - wwdc2022/110530 — Q&A: Human Interface Guidelines
  - wwdc2022/110531 — Meet the Presenter: Design app experiences with charts
  - wwdc2022/110532 — Meet the Presenter: Writing for interfaces
  - wwdc2022/110533 — Meet the Presenter: Design App Shortcuts
  - wwdc2023/10337 — Meet the presenters: Design with SwiftUI
  - wwdc2023/111243 — Q&A: Spatial design
  - wwdc2023/111324 — Q&A: Spatial design
  - wwdc2023/111484 — Q&A: UX writing
  - wwdc2023/111520 — Q&A: watchOS 10 design
  - wwdc2023/111522 — Q&A: Widgets in the Smart Stack on watchOS
- Fallos de descarga: 0

## Design Resources

- Inventario de kits y plantillas en `references/recursos-diseno.md` (no se descargan los .dmg).

## Huecos conocidos que no dependen de la descarga

- Las licencias completas de New York y de SF Symbols solo vienen dentro de los .dmg (no descargados por indicación). Se documenta lo que dicen la página /fonts/ (licencias de SF y SF Compact), la HIG de SF Symbols y las guías de marcas de developer.apple.com.
- La página Layout (actualizada el 9-9-2026) ya no incluye las tablas de tamaños de pantalla por dispositivo; los valores de dispositivos antiguos que citen vídeos anteriores no se pueden verificar en la HIG vigente.
