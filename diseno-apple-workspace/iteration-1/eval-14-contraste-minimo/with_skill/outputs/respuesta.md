# Contraste mínimo para texto de 15 pt normal y 20 pt en negrita

## Respuesta corta

| Texto | Regla que se aplica | Contraste mínimo |
|---|---|---|
| **15 pt, peso normal** | «Up to 17 pts», cualquier peso | **4.5:1** |
| **20 pt, negrita** | «18 pts» (cualquier peso) y además «Bold» (cualquier tamaño) | **3:1** |

El texto de 20 pt en negrita cumple **dos** condiciones que bajan el mínimo a 3:1: mide 18 pt o más y va en negrita. Con cualquiera de las dos bastaría.

## La tabla de Apple

Viene de la página [Accessibility › Vision](https://developer.apple.com/design/human-interface-guidelines/accessibility#Vision) de las HIG, con la regla **«Strive to meet color contrast minimum standards.»** (última actualización de la página: 9-6-2025):

| Text size | Text weight | Minimum contrast ratio |
|---|---|---|
| Up to 17 pts | All | 4.5:1 |
| 18 pts | All | 3:1 |
| All | Bold | 3:1 |

## Matices

- **Si usas colores propios, apunta más alto en texto pequeño.** La página [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Dark-Mode-colors) dice: «For custom foreground and background colors, strive for a contrast ratio of 7:1, especially in small text.» Para tu texto de 15 pt con colores propios, lo recomendable es **7:1**. 4.5:1 es solo el mínimo.
- **Las dos páginas no dicen exactamente lo mismo.** En Dark Mode, Apple escribe «At a minimum, make sure the contrast ratio between colors is no lower than 4.5:1», sin rebaja para el texto grande o en negrita. La tabla de Accessibility (9-6-2025) es más reciente y más concreta que Dark Mode (6-8-2024), así que el mínimo de **3:1 para 20 pt en negrita** sigue valiendo. Aun así, para ir sobre seguro puedes dar 4.5:1 también a ese texto, sobre todo en modo oscuro *(recomendación propia)*.
- **Si no llegas al mínimo por defecto**, Apple pide al menos ofrecer un esquema de colores con más contraste cuando el usuario active **Increase Contrast**: «If your app doesn’t provide this minimum contrast by default, ensure it at least provides a higher contrast color scheme when the system setting Increase Contrast is turned on.» ([Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility#Vision)).
- **Comprueba todas las apariencias.** El contraste tiene que cumplirse en claro, en oscuro y con más contraste. Reglas de Apple: «Aim for sufficient color contrast in all appearances» ([Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode)) y «Make sure all your app’s colors work well in light, dark, and increased contrast contexts» ([Color](https://developer.apple.com/design/human-interface-guidelines/color)). Si usas los colores del sistema («Prefer system-defined colors»), estos ya se adaptan solos a cada apariencia.
- **El peso también afecta a la legibilidad.** Apple lo recuerda: «Bear in mind that font weight can also impact how easy text is to read.» Los pesos finos (Light, Thin) a 15 pt se leen peor aunque cumplan 4.5:1.
- **Unidades.** Los tamaños de la tabla están en puntos (pt) de la plataforma. 15 pt está por encima del mínimo de texto en iOS/iPadOS (11 pt) y en macOS (10 pt). En tvOS, en cambio, queda por debajo del mínimo (23 pt) ([Typography](https://developer.apple.com/design/human-interface-guidelines/typography)).

*Observación propia, no de Apple: estos umbrales (4.5:1 y 3:1) coinciden con los del nivel AA de WCAG, así que puedes medirlos con cualquier comprobador de contraste WCAG.*
