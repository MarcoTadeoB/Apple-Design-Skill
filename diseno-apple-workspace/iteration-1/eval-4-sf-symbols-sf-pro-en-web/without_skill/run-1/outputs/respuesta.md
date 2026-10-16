# ¿Puedo usar SF Symbols o SF Pro en mi web?

**Respuesta corta:** no puedes alojarlos ni distribuirlos en tu web. Lo que sí puedes hacer es pedir la **fuente del sistema** por CSS. Así los visitantes que usan dispositivos Apple ven SF Pro sin que tú sirvas ningún archivo. Para los iconos, usa una biblioteca con licencia abierta que tenga un estilo parecido.

> Nota: esto resume cómo suelen entenderse las licencias de Apple, pero no es asesoramiento legal. Antes de publicar, lee la licencia que viene con cada descarga en developer.apple.com/fonts y developer.apple.com/sf-symbols. Apple puede cambiarla.

---

## 1. SF Pro (y SF Compact, SF Mono, New York)

### Lo que dice la licencia
Las fuentes de Apple que descargas desde Apple Developer tienen una licencia que **limita su uso a crear maquetas (mockups) y a desarrollar interfaces de software para las plataformas de Apple** (iOS, iPadOS, macOS, tvOS, watchOS, visionOS). En la práctica, esto significa lo siguiente:

| Uso | ¿Permitido? |
|---|---|
| Diseñar maquetas de una app de iOS o macOS en Figma o Sketch | Sí |
| Subir `SF-Pro.woff2` a tu servidor y cargarlo con `@font-face` | **No** (eso es redistribuir la fuente) |
| Cargarlo desde un CDN de terceros que lo "ofrece" | **No** (el problema es el mismo, y además ese CDN tampoco tiene permiso) |
| Usarlo en el logotipo, la marca o el material impreso de tu web | **No** |
| Pedir la fuente del sistema con `system-ui` / `-apple-system` | **Sí** (no distribuyes nada, solo pides la fuente que el dispositivo ya tiene) |

### La forma correcta: la pila de fuentes del sistema

```css
:root {
  font-family:
    system-ui,          /* estándar: SF Pro en Apple, Segoe UI en Windows, Roboto en Android */
    -apple-system,      /* Safari y navegadores antiguos de Apple */
    BlinkMacSystemFont, /* Chrome antiguo en macOS */
    "Segoe UI",
    Roboto,
    "Helvetica Neue",
    Arial,
    sans-serif,
    "Apple Color Emoji", "Segoe UI Emoji";
}
```

Safari también admite **familias genéricas** que apuntan a las otras fuentes del sistema de Apple:

```css
.serif   { font-family: ui-serif, Georgia, serif; }                 /* New York */
.mono    { font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace; } /* SF Mono */
.rounded { font-family: ui-rounded, system-ui, sans-serif; }        /* SF Pro Rounded */
```

Hay que tener en cuenta algunas cosas:
- **Solo verán SF Pro los visitantes que usan Apple.** En Windows, Android o Linux se mostrará otra fuente. Diseña pensando en eso y no te bases en las métricas exactas de SF.
- Con `system-ui`, macOS e iOS cambian solos entre los tamaños ópticos **Text** y **Display**, y también ajustan el *tracking*. No hace falta que lo imites a mano.
- `font-weight` funciona de 100 a 900 porque SF Pro es una fuente variable.
- **No escribas `font-family: "SF Pro"` ni `"SF Pro Display"` en tu CSS.** Esos nombres solo funcionan si el usuario tiene la fuente instalada (en general, diseñadores), así que el resultado es inconsistente. Usa `system-ui`.
- En iOS, Safari también tiene `font: -apple-system-body` (y `-apple-system-headline`, etc.). Así respetas el **Tipo Dinámico**, es decir, el tamaño de texto que el usuario eligió en Ajustes.

### Si necesitas la misma fuente en todas las plataformas
Si quieres una tipografía idéntica en todas partes, usa una fuente libre con un aire parecido:
- **Inter** (OFL): la alternativa más parecida y la más usada. Desde la versión 4 tiene tamaños ópticos (`opsz`).
- **Geist**, **Manrope**, **Plus Jakarta Sans** o **Public Sans**: otras sans neogrotescas con licencia libre.
- Para monoespaciada: **JetBrains Mono**, **Geist Mono** o **IBM Plex Mono**.

---

## 2. SF Symbols

### Lo que dice la licencia
SF Symbols tiene una licencia más restrictiva que la de las fuentes:
- Solo se pueden usar **en apps para las plataformas de Apple**, como parte de su interfaz.
- **No se pueden usar en sitios web**, ni siquiera si los exportas como SVG desde la app SF Symbols.
- **No se pueden usar en iconos de app, logotipos ni elementos de marca.**
- Algunos símbolos representan productos o tecnologías de Apple (iPhone, AirPods, Apple Watch, iCloud, FaceTime, etc.). Esos son aún más restringidos: aunque estés en una app nativa, solo puedes usarlos para referirte a ese producto concreto.

| Uso | ¿Permitido? |
|---|---|
| Iconos en una app nativa de SwiftUI o UIKit | Sí |
| Maquetas de una app de iOS o macOS | Sí |
| Exportar SVG o PNG y ponerlos en tu web | **No** |
| Usarlos en un PWA o una web "con estilo iOS" | **No** |
| Truco de los caracteres de uso privado (PUA) de SF Pro para mostrar símbolos en Safari | **No lo hagas**: solo funciona en dispositivos Apple, no es accesible y queda fuera del uso que permite la licencia |
| Usarlos en tu logotipo o favicon | **No** |

### Alternativas libres con un estilo parecido

| Biblioteca | Licencia | Por qué encaja |
|---|---|---|
| **Framework7 Icons** | MIT | Imita deliberadamente el estilo de iOS y SF Symbols |
| **Phosphor Icons** | MIT | Varios pesos (thin → bold, fill, duotone), parecido a los pesos de SF |
| **Lucide** (sucesor de Feather) | ISC | Trazo limpio y redondeado, muy completo |
| **Ionicons** | MIT | Tiene variantes de estilo iOS |
| **Heroicons** | MIT | Versiones outline y solid, buen acabado |
| **Tabler Icons** | MIT | Más de 5000 iconos de trazo uniforme |
| **Material Symbols** | Apache 2.0 | Fuente variable con eje de peso, relleno y tamaño óptico |

Para que se parezcan aún más a SF Symbols:
- Ajusta el **grosor del trazo al peso del texto** que los acompaña (por ejemplo, `stroke-width: 1.5` para texto regular y `2` para semibold).
- Dimensiona los iconos con `em` (`width: 1em; height: 1em`) y usa `color: currentColor` para que sigan al texto, como hacen los SF Symbols.
- Alinéalos con la línea base o con el centro óptico del texto (`vertical-align: -0.125em` suele funcionar bien).

---

## 3. Casos especiales

- **Botones oficiales de Apple** (Sign in with Apple JS, Apple Pay en la web, MapKit JS): Apple te da sus propios recursos y estilos. Úsalos tal cual y sigue sus guías. Ahí sí verás iconografía de Apple, pero la proporciona Apple.
- **Capturas de pantalla de tu app de iOS** en la web de marketing: no hay problema en que aparezcan SF Pro y SF Symbols. Es tu app nativa mostrada como imagen, que es lo normal en marketing. Sigue también las *Apple Marketing Guidelines* para los marcos de dispositivo y los distintivos de App Store.
- **Web dentro de una app nativa (WKWebView)**: `system-ui` también te da SF Pro ahí. Los SF Symbols en HTML siguen sin estar permitidos. Si los necesitas, dibújalos en la parte nativa.

---

## Resumen

1. **SF Pro:** no lo alojes. Usa `font-family: system-ui, -apple-system, …`. Los usuarios de Apple lo verán gratis y de forma legal. Si quieres el mismo aspecto en todas las plataformas, usa **Inter**.
2. **SF Symbols:** no los uses en la web de ninguna forma. Usa **Framework7 Icons**, **Phosphor** o **Lucide**, con el trazo ajustado al peso del texto.
3. Revisa la licencia vigente que viene con cada descarga de Apple antes de publicar.
