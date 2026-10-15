# ¿Puedo usar SF Symbols o SF Pro en mi web?

**En resumen: no puedes incrustar ninguno de los dos.** Lo que sí puedes hacer es pedir al navegador la **fuente del sistema** del visitante. En un iPhone, iPad o Mac esa fuente ya es San Francisco, así que la verá sin que tú distribuyas nada. Para los iconos, usa unos propios o de una biblioteca con licencia libre.

> No es asesoramiento legal. Esto resume los textos de Apple descargados el 15-10-2026. Si tienes dudas, prevalece el texto de Apple y conviene consultar a un abogado.

---

## 1. SF Pro (y New York, SF Compact, SF Mono)

**Qué dice la licencia.** La licencia *Apple San Francisco Font* se publica en [developer.apple.com/fonts](https://developer.apple.com/fonts/).

| Lo permite | Lo prohíbe |
|---|---|
| Usarla «solely for creating mock-ups of user interfaces to be used in software products running on Apple’s iOS, OS X or tvOS operating systems» | Usarla en maquetas de software para «any non-Apple operating system» |
| Mostrarla en capturas y maquetas de ese software | «You may not embed the Apple Font in any software programs or other products» |
| Solo si eres **Apple Developer registrado** (o tienes permiso escrito de Apple) | Usarla para crear o mostrar «documentation, artwork, website content or any other work product» |
| | Redistribuirla, ponerla en un servidor, modificarla o crear derivados |

*SF Compact* tiene una licencia con la misma estructura, pero solo para maquetas de **watchOS**. La licencia termina, entre otros casos, si dejas de ser desarrollador registrado.

**Qué significa para tu web:**

| Caso | ¿Se puede? |
|---|---|
| Subir los archivos de SF Pro y cargarlos con `@font-face` | **No**. La licencia prohíbe incrustarla y usarla para «website content». |
| Usar SF Pro en el logotipo o en gráficos de marketing de la web | **No**. No es uno de los usos permitidos. |
| Usar `font-family: -apple-system, BlinkMacSystemFont, system-ui, …` | **Sí.** Así no distribuyes la fuente: le pides al sistema del visitante la suya. La licencia regula la copia que *tú* descargas, no la fuente que el visitante ya tiene instalada. |
| Usar SF Pro en maquetas (Figma/Sketch) de una app de iOS/macOS/tvOS | **Sí**, si eres desarrollador registrado. |

**Cómo hacerlo bien en CSS.** Este patrón viene de la guía web de esta skill. La pila de fuentes y la alternativa son decisión propia, no de Apple:

```css
:root {
  /* En dispositivos Apple → San Francisco del sistema (no se descarga ni se incrusta nada).
     Fuera de Apple → Inter (SIL OFL, auto-alojada) u otra fuente del sistema. */
  font-family: -apple-system, BlinkMacSystemFont, system-ui, "Inter", "Segoe UI",
               Roboto, "Helvetica Neue", Arial, sans-serif;
}

/* Extra para Safari en iOS: respeta el tamaño de texto que el usuario elige en Ajustes (Dynamic Type) */
html { font: -apple-system-body; }
body { font-size: 1rem; }   /* de aquí en adelante, tamaños en rem/em */
```

- En Windows, Android o Linux **no** se verá San Francisco. Diseña contando con la fuente alternativa.
- **Inter** es la alternativa habitual porque sus métricas se parecen. Esto es una recomendación propia, no de Apple. Tiene licencia SIL OFL (compruébalo en su web) y la puedes alojar tú mismo.
- `-apple-system-body` es una palabra clave de WebKit y solo funciona en Safari.

## 2. SF Symbols

**Qué dice Apple.** Las HIG de [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) dicen:

> «Be sure to understand the terms and conditions for using SF Symbols, including the prohibition against using symbols — or images that are confusingly similar — in app icons, logos, or any other trademarked use.»

- La licencia completa de SF Symbols viene dentro del instalador `.dmg` de la app [SF Symbols](https://developer.apple.com/sf-symbols/). No forma parte de las fuentes que consulté, así que no puedo citarla.
- En la documentación de Apple que revisé **no aparece ningún permiso para usar SF Symbols en una web**, ni fuera de software para plataformas Apple. Apple sí los presenta como gratuitos *para apps*. En el vídeo WWDC26 «251» lo dice así: [15:23](https://developer.apple.com/videos/play/wwdc2026/251/?time=923) «SF Symbols is a Mac app with over 7,000 symbols that you can use for free.» Pero eso se refiere a apps nativas.
- La prohibición explícita cubre **iconos de app, logotipos y cualquier uso como marca**, y alcanza también a los dibujos «confusingly similar». Calcar un símbolo para saltártela no sirve.

**Conclusión práctica:** no exportes SVG desde la app SF Symbols para tu web y no los redibujes. Si tu proyecto lo necesita de verdad, revisa la licencia del `.dmg` o pide permiso a Apple.

**Qué hacer en su lugar.** Son recomendaciones propias, basadas en el estilo de SF Symbols:

- Usa **iconos propios** o una **biblioteca de licencia abierta** que tenga un estilo parecido: trazo con extremos redondeados, grosor acorde al peso del texto (unos 1,5–2 px a 24 px), rejilla de 24×24 y `currentColor` para que hereden el color del texto.
- Toma de Apple la **metáfora**, no el dibujo: papelera para borrar, lupa para buscar. Las acciones comunes y su símbolo preferido están en las HIG [Icons](https://developer.apple.com/design/human-interface-guidelines/icons).
- Mantén la coherencia: usa el mismo icono para la misma acción en toda la web.
- Accesibilidad: pon `aria-hidden="true"` en el SVG decorativo y da al botón una etiqueta de texto visible o un `aria-label`.

```html
<button class="icon-button" aria-label="Buscar">
  <svg aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="none"
       stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/>
  </svg>
</button>
```

*(Este icono es un dibujo genérico propio, no un SF Symbol.)*

## 3. Tabla rápida

| Quiero… | ¿Se puede? | Cómo |
|---|---|---|
| Que mi web se vea con San Francisco en dispositivos Apple | Sí | `-apple-system` / `system-ui`, sin incrustar archivos |
| Incrustar SF Pro o New York con `@font-face` | No | Usa Inter u otra fuente libre como alternativa |
| Usar SF Pro en el logotipo de mi web | No | Usa una tipografía con licencia para uso de marca |
| Usar SF Symbols (SVG exportados) en la web | No hay permiso | Iconos propios o de una biblioteca abierta |
| Usar un SF Symbol en el logotipo o en el icono de la app | No, está prohibido expresamente | Diseña un logotipo propio |
| Usar SF Symbols en mi app nativa de iOS/macOS | Sí, es lo recomendado | API del sistema (SwiftUI `Image(systemName:)`) |
| Imitar el estilo visual de Apple (colores, espaciados, Liquid Glass) | Sí, el estilo no es una marca | Sin logotipos ni marcas de Apple, y sin presentarlo como «de Apple» |

## Fuentes

- Apple — Fonts y licencias *Apple San Francisco Font* / *SF Compact*: https://developer.apple.com/fonts/
- HIG — SF Symbols (última actualización 28-7-2025): https://developer.apple.com/design/human-interface-guidelines/sf-symbols
- Apple — SF Symbols (app): https://developer.apple.com/sf-symbols/
- HIG — Icons: https://developer.apple.com/design/human-interface-guidelines/icons
- WWDC26, sesión 251, [15:23](https://developer.apple.com/videos/play/wwdc2026/251/?time=923)
- Apple — Licensing and Trademarks: https://developer.apple.com/licensing-trademarks/

**Origen de cada parte:** las citas en inglés entre «» son textos literales de Apple. La pila de `font-family`, la propuesta de Inter y las pautas de estilo de los iconos son recomendaciones propias de esta guía para la web. Lo de `-apple-system-body` es comportamiento de WebKit, no una norma de Apple sobre diseño.
