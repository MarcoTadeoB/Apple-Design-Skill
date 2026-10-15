# Tamaño mínimo de un control en iOS y en visionOS

## Respuesta corta

| Plataforma | Tamaño por defecto (recomendado) | Tamaño mínimo | Fuente |
|---|---|---|---|
| **iOS / iPadOS** | **44 × 44 pt** | **28 × 28 pt** | [Accessibility › Mobility](https://developer.apple.com/design/human-interface-guidelines/accessibility#Mobility) |
| **visionOS** | **60 × 60 pt** | **28 × 28 pt** | [Accessibility › Mobility](https://developer.apple.com/design/human-interface-guidelines/accessibility#Mobility) |

Esta es la tabla «Default control size / Minimum control size» de la página *Accessibility* de las HIG (consultada el
15-10-2026; última actualización de la página: 9-6-2025). Los valores están en **puntos**, no en píxeles.

El tamaño mínimo es el mismo en las dos plataformas (28 × 28 pt). Lo que cambia es el tamaño por defecto, que es la
zona interactiva que deberías tener: 44 pt con el dedo y 60 pt con la mirada.

## La regla de Apple sobre el área táctil

En la página *Buttons* (actualizada el 16-12-2025), Apple lo expresa como un área de impacto (hit region):

> «As a general rule, a button needs a hit region of at least 44x44 pt — in visionOS, 60x60 pt — to ensure that
> people can select it easily, whether they use a fingertip, a pointer, their eyes, or a remote.»
> — [Buttons › Best practices](https://developer.apple.com/design/human-interface-guidelines/buttons)

Es decir:

- **iOS / iPadOS**: el área interactiva debe medir **44 × 44 pt** o más. Un control puede verse más pequeño, pero
  nunca por debajo de 28 × 28 pt.
- **visionOS**: el área interactiva debe medir **60 × 60 pt** o más, porque se apunta con los ojos, que son menos
  precisos que un dedo. El control visible puede ser menor (hasta 28 pt), siempre que tenga espacio libre alrededor.

## Detalle de visionOS: tamaño visible frente a espacio de interacción

En visionOS, los 60 pt se consiguen sumando el tamaño del control y el espacio que lo rodea:

- **Tamaños de botón del sistema** ([Buttons › visionOS](https://developer.apple.com/design/human-interface-guidelines/buttons)):

  | Forma | Mini (28 pt) | Small (32 pt) | Regular (44 pt) | Large (52 pt) | Extra large (64 pt) |
  |---|---|---|---|---|---|
  | Circular | ✓ | ✓ | ✓ | ✓ | ✓ |
  | Capsule (solo texto) |  | ✓ | ✓ | ✓ |  |
  | Capsule (texto e icono) |  |  | ✓ | ✓ |  |
  | Rounded rectangle |  | ✓ | ✓ | ✓ |  |

- **Separación**: «Aim to place buttons so their centers are always at least 60 pts apart» ([Buttons › visionOS](https://developer.apple.com/design/human-interface-guidelines/buttons)).
  La misma idea aparece en [Layout › visionOS](https://developer.apple.com/design/human-interface-guidelines/layout#visionOS)
  (actualizada el 9-9-2026): «place buttons so their centers are at least 60 points apart».
- **Margen alrededor**: «a margin of at least 16 points around the bounds of each item or by placing items so that
  their centers are always at least 60 points apart» ([Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes)).
- En los vídeos de Apple:
  - [1:07](https://developer.apple.com/videos/play/wwdc2025/303/?time=67) «For precise interactions, give each element
    at least 60 points of space.» y [1:12](https://developer.apple.com/videos/play/wwdc2025/303/?time=72) «Elements
    can be visually smaller than this, as long they each have a total space of 60 points.» (*Design hover
    interactions for visionOS*, WWDC25).
  - [1:18](https://developer.apple.com/videos/play/wwdc2025/303/?time=78) para objetos 3D de escala fija: 60 pt
    equivalen a «roughly… two and a half degrees, which is about 4.4 cm for an object one meter away» (mismo vídeo).
  - [10:54](https://developer.apple.com/videos/play/wwdc2023/10076/?time=654) un botón de 44 pt necesita «at least
    eight points of empty space around it so it meets the minimum of having a target area of 60 points» (*Design for
    spatial user interfaces*, WWDC23).

**Cálculo propio (no lo publica Apple así):** las cifras cuadran entre sí. Un botón Mini de 28 pt con el margen de
16 pt por cada lado ocupa 28 + 16 + 16 = 60 pt, y un botón Regular de 44 pt con 8 pt por lado también llega a 60 pt.
Por eso 28 pt es el mínimo visible en visionOS y 60 pt el área de interacción que debes reservar.

## Espaciado entre controles (iOS y visionOS)

La página *Accessibility* también recomienda dejar margen alrededor de los controles:

- «add about 12 points of padding around elements that include a bezel»
- «For elements without a bezel, about 24 points of padding works well around the element’s visible edges.»

— [Accessibility › Mobility](https://developer.apple.com/design/human-interface-guidelines/accessibility#Mobility)

## Recomendación práctica

- **iPhone / iPad**: diseña con un área táctil de 44 × 44 pt. Si un icono se ve más pequeño, amplía su área táctil
  hasta 44 pt en vez de dejarlo en el tamaño del dibujo. No bajes de 28 × 28 pt.
- **Vision Pro**: usa los tamaños de botón del sistema (Regular, de 44 pt, es el caso típico). Asegúrate de que cada
  control tenga 60 pt de espacio de interacción, con centros a 60 pt o más, o un margen de 16 pt alrededor.
- Si puedes, usa los controles estándar del sistema, porque ya traen las áreas de interacción correctas.
