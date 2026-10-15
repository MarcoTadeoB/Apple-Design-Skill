# Herramientas de diseño de Apple y Design Pathway

Páginas descargadas el 15-10-2026. Inventario de descargas en `recursos-diseno.md`; licencias en
`licencias-y-marcas.md`.

## SF Symbols — https://developer.apple.com/sf-symbols/

- Biblioteca de **más de 7.000 símbolos** integrados con San Francisco; **9 pesos y 3 escalas**; se alinean con el
  texto; exportables y editables para crear símbolos propios.
- Versión: la página y Design Resources enlazan `SF-Symbols-27.dmg` («Requires macOS Sonoma or later»); *What's new*
  (8-6-2026) lo anunció como «SF Symbols 8 beta» (ver contradicción en `novedades.md`).
- Novedades de la página: **Enhanced Search** (búsqueda semántica), símbolos nuevos para las plataformas 27, **Draw**
  (Draw On/Draw Off), **Annotation** (puntos guía; Ultralight, Regular y Black), **Variable Rendering** (Variable
  Color y Variable Draw), animaciones (Bounce, Wiggle, Rotate, Breathe…, Magic Replace) y 4 modos de renderizado:
  Monochrome, Hierarchical, Palette y Multicolor.
- Guía de uso: `hig/foundations/sf-symbols.md`; acciones comunes con su símbolo preferido: `hig/foundations/icons.md`
  (tablas «Action | Icon | Symbol name»). Vídeos: `2025-337` (SF Symbols 7), `2024-10188` (SF Symbols 6).
- Prohibido usarlos (o algo «confusingly similar») en iconos de app, logotipos u otros usos de marca (HIG).

## Icon Composer — https://developer.apple.com/icon-composer/

- Crea iconos por capas de Liquid Glass a partir de **un único diseño** para iPhone, iPad, Mac y Apple Watch;
  anotación por modo **Default, Dark y Mono**; exporta una versión plana para marketing; el archivo `.icon` se
  integra en Xcode.
- Icon Composer 2: **Refraction** por capa, nuevos **specular highlights** (dentro/fuera o automático; ángulo de
  luz vertical desde arriba), material más nítido al importar archivos anteriores.
- Requisito (página de Icon Composer): **macOS Tahoe 26.4 o posterior** (Design Resources aún dice «macOS Sequoia
  or later»; prevalece la página de la herramienta).
- Flujo y valores: `videos/2025-361.md` (lienzo 1024 px; Watch 1088 px; hasta 4 grupos; SVG/PNG; sin máscara),
  `videos/2025-220.md`, `hig/foundations/app-icons.md`. Laboratorio WWDC26: `videos/2026-8012.md`.

## Pass Designer — https://developer.apple.com/pass-designer/

- App del Mac para crear y previsualizar pases de Apple Wallet con plantillas de Apple o propias; vista previa en
  tiempo real con el mismo renderizado que iOS y watchOS; colores de fondo, primer plano y etiquetas; diseños
  adaptables y pases compatibles con versiones anteriores; campos estándar; validación; **semantic tags**.
- **Beta; requiere macOS 27 o posterior.** Guía: `hig/technologies/wallet.md` (actualizada el 8-6-2026 para iOS 27
  y Pass Designer).

## Reality Composer Pro 3 — https://developer.apple.com/reality-composer-pro/

- Iterar, previsualizar y preparar contenido 3D para visionOS, iOS y más; integración con Xcode, scripting visual,
  inteligencia generativa para crear assets; Reality Composer Pro Preview en Apple Vision Pro.
- **Beta; requiere macOS 26.5 o posterior.** Vídeos WWDC26: `2026-252` (juegos sin código), `2026-280`,
  `2026-281`, `2026-393`.

## Fuentes — https://developer.apple.com/fonts/

- San Francisco: tamaños ópticos y tracking dinámico; cifras proporcionales por defecto; nueve pesos con
  cursivas, versalitas, fracciones…
- SF Pro (sistema), SF Compact (watchOS), SF Mono, New York; SF Arabic, Armenian, Georgian, Hebrew.
- Licencia: solo maquetas de software de plataformas Apple (ver `licencias-y-marcas.md`).

## Parallax Previewer

- Para efectos de paralaje en tvOS y visionOS; versión 2 requiere macOS 13.5 (Design Resources).

## Design Pathway — https://developer.apple.com/design/get-started/

Ruta de aprendizaje oficial, en este orden:
1. **Fundamentos** — vídeos *The qualities of great design* (`2018-801`), *Essential design principles*
   (`2017-802`), *Design foundations from idea to interface* (`2025-359`).
2. **HIG** por secciones: Getting started, Foundations, Patterns, Components, Inputs, Technologies.
3. **Caja de herramientas**: Apple Design Resources (fuentes, iconos, marcos, plantillas).
4. **Prototipos**: *Prototyping: Fake it till you make it* (`2014-223`), *60-second prototyping* (`2017-818`),
   *Design with SwiftUI* (`2023-10115`).
5. **Inspiración**: artículos y perfiles de desarrolladores, Apple Design Awards (`premios-e-historias.md`),
   [*10 Questions with Design Evangelism*](https://developer.apple.com/news/?id=s8sl4tpa), [*Meet the prototypers*](https://developer.apple.com/news/?id=97dgimaa).
6. **Ir más allá**: *What's new*, todos los vídeos de diseño (`videos/_indice.md`), actividades para desarrolladores.
