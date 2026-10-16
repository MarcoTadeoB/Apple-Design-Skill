# Liquid Glass: ¿cuándo *clear* en vez de *regular*?

## Respuesta corta

Usa **regular** casi siempre: es la variante por defecto y la que usan la mayoría de los componentes del sistema.
Usa **clear** solo en un caso: controles que flotan sobre **contenido multimedia rico** (fotos, vídeo, una cámara,
un mapa con imágenes), cuando quieres que ese contenido siga viéndose bien a través del control. Además, tienes que
poder poner una **capa de atenuación** (*dimming*) debajo para que se lean los iconos y las etiquetas.

Si dudas, la respuesta es **regular**.

## Qué dice Apple (reglas literales)

**HIG › [Materials › Liquid Glass](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass)**
(página actualizada el 9-9-2025, «Updated guidance for Liquid Glass»):

- **«Only use clear Liquid Glass for components that appear over visually rich backgrounds.»**
- *Regular*: «blurs and adjusts the luminosity of background content to maintain legibility of text and other
  foreground elements».
- *Clear*: «is highly translucent, which is ideal for prioritizing the visibility of the underlying content and
  ensuring visually rich background elements remain prominent».
- Sobre la atenuación con *clear*:
  - Si el contenido de debajo es brillante: «consider adding a dark dimming layer of 35% opacity».
  - Si el contenido es lo bastante oscuro, o si usas los controles estándar de reproducción de **AVKit** (que ya
    traen su propia atenuación), no hace falta añadir una.

**Vídeo *Meet Liquid Glass* (WWDC25, sesión 219)**:

- Regular es la opción por defecto: «Regular is the most versatile and the one you will be using the most» —
  [14:00](https://developer.apple.com/videos/play/wwdc2025/219/?time=840).
- *Clear* no tiene comportamientos adaptativos y es siempre más transparente —
  [14:16](https://developer.apple.com/videos/play/wwdc2025/219/?time=856).
- Para que los símbolos y las etiquetas se lean, necesita atenuación: «To provide enough legibility for symbols or
  labels, it needs a dimming layer to darken the underlying content» —
  [14:27](https://developer.apple.com/videos/play/wwdc2025/219/?time=867).
- Si los elementos de cristal son pequeños, puedes atenuar solo la zona que hay debajo de ellos (atenuación
  localizada). Así el resto del contenido conserva más color e intensidad —
  [14:37](https://developer.apple.com/videos/play/wwdc2025/219/?time=877).
- **La regla de las 3 condiciones**: «Clear should only be used when these 3 conditions are met» —
  [14:50](https://developer.apple.com/videos/play/wwdc2025/219/?time=890).
- **No se mezclan**: «They should never be mixed, as they each have their own characteristics and specific use
  cases» — [13:55](https://developer.apple.com/videos/play/wwdc2025/219/?time=835).

## Las 3 condiciones para usar *clear*

Según el vídeo ([14:50](https://developer.apple.com/videos/play/wwdc2025/219/?time=890)), deben cumplirse
**las tres**. Si falla una, usa **regular**.

| # | Condición | Pregunta para comprobarla |
|---|---|---|
| 1 | El elemento está sobre **contenido rico en medios** | ¿Debajo hay una foto, un vídeo o el visor de la cámara, y no una lista, texto o un fondo liso? |
| 2 | La capa de contenido **tolera una capa de atenuación** | ¿Oscurecer un poco la imagen (hasta un 35 % si es brillante) estropea la experiencia? Si no la estropea, se cumple. |
| 3 | Lo que va **encima** del cristal (símbolos, etiquetas) es **llamativo y brillante** | ¿Los glifos son claros, gruesos y se distinguen bien sobre la imagen atenuada? |

## Comparativa

| | Regular | Clear |
|---|---|---|
| Qué hace | Desenfoca el fondo y ajusta su luminosidad para que el contenido de primer plano se lea | Muy translúcido: da prioridad a ver el contenido de debajo |
| Adaptación | Tiene todos los efectos adaptativos (sombra, tinte, cambio entre claro y oscuro…) | **Ninguno**: siempre más transparente |
| Dónde | Por defecto: barras, botones, menús, y también *alerts*, *sidebars*, *popovers* o cualquier sitio con mucho texto o con un fondo que pueda dificultar la lectura | Solo componentes que flotan sobre fotos o vídeo |
| Atenuación | No necesita | Oscura al 35 % si el fondo es brillante. No hace falta si el fondo es oscuro o si usas AVKit |
| SwiftUI | [`Glass.regular`](https://developer.apple.com/documentation/swiftui/glass/regular) | [`Glass.clear`](https://developer.apple.com/documentation/swiftui/glass/clear) |

## Ejemplos

**Buenos candidatos para *clear*** (se cumplen las 3 condiciones):

- Los controles superpuestos sobre el visor de la cámara o sobre una foto a pantalla completa.
- Los controles flotantes de un reproductor de vídeo propio.
  - Si usas los controles de AVKit, ya incluyen la atenuación (HIG Materials).
- Botones pequeños sobre una galería de imágenes vistosas, con atenuación localizada.

**Contraejemplos: usa *regular*.**

- Una tab bar o una toolbar sobre una lista, un formulario o un texto. Falla la condición 1.
- Un panel con mucho texto (alert, popover, sidebar), aunque haya una foto detrás. Necesita la legibilidad
  adaptativa de *regular*.
- Una app de fotografía artística donde oscurecer la imagen es inaceptable. Falla la condición 2.
- Controles con símbolos finos o de colores apagados. Falla la condición 3.
- Usar *clear* «porque queda más bonito» o más moderno. Apple lo limita a fondos ricos en medios.
- Mezclar en la misma pantalla botones *clear* y botones *regular*. Apple dice que no se mezclen nunca.

## Matices y avisos

- **Fuente más reciente.** El vídeo de junio de 2025 dice que *clear* «needs a dimming layer». La página Materials,
  revisada el 9-9-2025, lo matiza: decide si la necesitas. No hace falta si el fondo ya es oscuro o si usas AVKit.
  Prevalece la HIG por ser más reciente.
- **El 35 % es una recomendación** («consider»), no un valor obligatorio. Para la atenuación localizada, Apple no
  publica ningún porcentaje ni tamaño.
- **Las reglas generales siguen valiendo con cualquiera de las dos variantes:**
  - Liquid Glass va solo en la capa funcional, nunca en la capa de contenido: «Don’t use Liquid Glass in the
    content layer».
  - Nada de cristal sobre cristal: [13:24](https://developer.apple.com/videos/play/wwdc2025/219/?time=804).
  - Úsalo con moderación: «Use Liquid Glass effects sparingly».
- **Accesibilidad.** Ambas variantes cambian según los ajustes del sistema: el aspecto preferido de Liquid Glass
  que elige la persona, Reduce Transparency e Increase Contrast (HIG Materials). Con el material del sistema, esto
  ocurre automáticamente. Por ejemplo, Reduce Transparency hace el cristal más esmerilado
  ([18:22](https://developer.apple.com/videos/play/wwdc2025/219/?time=1102)). Prueba los controles *clear* con
  esos ajustes y en Dark Mode.
- **Por plataforma.** La regla regular/clear de Materials es general; las HIG no dan variaciones por plataforma.
  - En **visionOS**, las ventanas usan el material *glass* del sistema, que no se puede modificar.
  - En **tvOS**, las imágenes y los botones adoptan Liquid Glass al recibir el foco.
- **No lo confundas con:**
  - El material estándar `regular` de iOS/iPadOS (ultraThin, thin, regular, thick). Es otro material, pensado
    para la capa de contenido.
  - Las apariencias *clear* de los **iconos de app** y de los **widgets**. Son conceptos distintos de la variante
    clear del material.

## Fuentes

- HIG › [Materials](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass)
  (actualizada el 9-9-2025)
- *Meet Liquid Glass*, WWDC25:
  [developer.apple.com/videos/play/wwdc2025/219](https://developer.apple.com/videos/play/wwdc2025/219/)
  (marcas 13:24, 13:55, 14:00, 14:16, 14:27, 14:37, 14:50 y 18:22)
- SwiftUI: [`Glass.regular`](https://developer.apple.com/documentation/swiftui/glass/regular),
  [`Glass.clear`](https://developer.apple.com/documentation/swiftui/glass/clear) y
  [Applying Liquid Glass to custom views](https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views)
