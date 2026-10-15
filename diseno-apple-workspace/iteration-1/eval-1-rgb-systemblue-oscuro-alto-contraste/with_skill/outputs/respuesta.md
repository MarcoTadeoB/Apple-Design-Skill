# systemBlue en modo oscuro con alto contraste

| Variante | RGB | Hexadecimal |
|---|---|---|
| **Increased contrast (dark)** | **R 92 · G 184 · B 255** | **#5CB8FF** |

En el modo oscuro con **Increase Contrast** activado, el systemBlue vale **92, 184, 255**, es decir **#5CB8FF**.

## De dónde sale el dato

- **Fuente:** Human Interface Guidelines de Apple, página **Color**, apartado *Specifications › System colors*:
  <https://developer.apple.com/design/human-interface-guidelines/color#Specifications>
- Está en la columna **«Increased contrast (dark)»**, fila **Blue** (API de SwiftUI [`Color.blue`](https://developer.apple.com/documentation/swiftui/color/blue); en UIKit, `UIColor.systemBlue`).
- Apple publica el valor en el texto alternativo de la muestra de color: `R-92,G-184,B-255`
  (imagen `colors-unified-accessible-blue-dark@2x.png`).
- **El hexadecimal no lo da Apple:** sale de convertir ese RGB (92 → 5C, 184 → B8, 255 → FF).
- **Vigencia:** estos valores llegaron con la actualización de la versión 26 (9-6-2025), cuyo registro de cambios dice «Updated system color values». Después, la página Color se volvió a actualizar el 16-12-2025, pero ese cambio fue de guía sobre Liquid Glass y los colores no cambiaron. Las HIG se consultaron el 15-10-2026 (plataformas 27).

## Las cuatro variantes, para comparar

| Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
|---|---|---|---|
| 0,136,255 · #0088FF | 0,145,255 · #0091FF | 30,110,244 · #1E6EF4 | **92,184,255 · #5CB8FF** |

Apple indica que la tabla es común a todas las plataformas. En visionOS se usan los valores oscuros por defecto: «visionOS system colors use the default dark color values.»

## Aviso importante

En una app nativa **no escribas este valor a mano**. Usa `Color.blue` o `UIColor.systemBlue`, que cambian solos entre claro, oscuro y alto contraste. Así lo dice Apple: «Avoid hard-coding system color values in your app… The actual color values may fluctuate from release to release» ([Color › System colors](https://developer.apple.com/design/human-interface-guidelines/color#System-colors)).

El valor fijo **#5CB8FF** solo sirve para webs (por ejemplo, con `@media (prefers-color-scheme: dark) and (prefers-contrast: more)`) o para maquetas. Si lo usas, anota la fecha de la HIG de la que sale.
