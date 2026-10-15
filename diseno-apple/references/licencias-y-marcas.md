# Licencias y marcas — qué se puede y qué no

> No es asesoramiento legal. Resume los textos descargados el 15-10-2026; ante cualquier duda, el texto de Apple
> prevalece y conviene consultar a un abogado. Cita siempre la fuente al responder.

Fuentes: [Fonts](https://developer.apple.com/fonts/) (incluye las licencias de *Apple San Francisco Font* y
*Apple San Francisco Compact Font*), HIG [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols),
[Licensing and Trademarks](https://developer.apple.com/licensing-trademarks/),
[Marketing Resources and Identity Guidelines](https://developer.apple.com/app-store/marketing/guidelines/),
[Design Resources](https://developer.apple.com/design/resources/) y páginas HIG de tecnologías (Apple Pay,
Sign in with Apple, Maps, App Clips…).

**Huecos**: las licencias completas de **New York** y de **SF Symbols** vienen dentro de los .dmg (no descargados);
las *Guidelines for Using Apple Trademarks and Copyrights* y la *Apple Trademark List* están en www.apple.com,
dominio bloqueado en el entorno de descarga. Lo que sigue se limita a lo que sí está en las fuentes.

## 1. Fuentes de Apple (SF Pro, SF Compact, SF Mono, New York…)

Licencia *Apple San Francisco Font* (en /fonts/):

| Se permite | No se permite |
|---|---|
| Usarla «solely for creating mock-ups of user interfaces to be used in software products running on Apple’s iOS, OS X or tvOS operating systems» | Usarla para maquetas de software de «any non-Apple operating system» (Android, Windows, web genérica…) |
| Mostrarla en capturas, imágenes y maquetas (digitales o impresas) de ese software | «You may not embed the Apple Font in any software programs or other products» |
| Solo si eres **Apple Developer registrado** (o con permiso escrito de Apple) | «you may not use the Apple Font to, create, develop, display or otherwise distribute any documentation, artwork, website content or any other work product» (salvo lo permitido expresamente) |
| | Ponerla disponible en red para varios equipos; redistribuirla, sublicenciarla, modificarla o crear derivados |

- La licencia termina, entre otros casos, si dejas de ser Apple Developer registrado.
- *SF Compact*: misma estructura, pero solo para maquetas de software de **watchOS**.
- Familias (página /fonts/): SF Pro (nueve pesos, anchos variables, variante redondeada, más de 150 idiomas),
  SF Compact (watchOS), SF Mono (seis pesos) y New York (serif, seis pesos); extensiones SF Arabic, Armenian,
  Georgian y Hebrew.

### ¿Puedo usar SF Pro en mi web?

- **Incrustarla (`@font-face` con los archivos de SF Pro)**: **no**. La licencia prohíbe incrustarla en productos
  y usarla para «website content».
- **En un logotipo o una pieza de marca**: **no**; tampoco está entre los usos permitidos (solo maquetas de UI
  de software de plataformas Apple).
- **`font-family: -apple-system, BlinkMacSystemFont, system-ui`**: no distribuye la fuente; pide al sistema del
  visitante su propia fuente de sistema (en dispositivos Apple será San Francisco porque ya está instalada). La
  licencia de /fonts/ regula la copia que tú descargas, no la fuente de sistema del visitante. Fuera de
  dispositivos Apple se usará otra fuente: declara una alternativa (ver `web.md`).
- Para maquetas de una app de iOS/macOS/tvOS/watchOS: sí, siendo desarrollador registrado.

## 2. SF Symbols

- HIG: «Be sure to understand the terms and conditions for using SF Symbols, including the prohibition against
  using symbols — or images that are confusingly similar — in **app icons, logos, or any other trademarked use**.»
- Página SF Symbols: más de 7.000 símbolos; nueve pesos y tres escalas; se integran con San Francisco.
- La licencia completa de SF Symbols no está en las fuentes descargadas. **No hay en ellas ningún permiso para
  usar SF Symbols en webs** ni fuera de software de plataformas Apple. Recomendación de la skill: en web, usa
  **iconos propios** (o de una biblioteca con licencia abierta) que sigan el estilo (trazos redondeados, pesos que
  acompañan al texto), y no copies ni calques símbolos de SF Symbols («confusingly similar»).
- En apps nativas, SF Symbols es la opción recomendada (vídeo `2026-251`: «you can use for free»; HIG Icons,
  Tab bars…).

## 3. Kits, plantillas y marcos (Design Resources)

- Los kits de UI (Figma/Sketch) y plantillas sirven para **diseñar apps** para plataformas Apple (vídeo
  `2026-tech-talks-111427`).
- **Marcos de producto (*product bezels*)**: úsalos en marketing según las *Marketing Resources and Identity Guidelines*
  (sección *Apple Product Images*):
  - Usa los marcos de Apple «as is»: no añadas reflejos, sombras, brillos, elementos que entren o salgan de la
    pantalla; no recortes, inclines, tapes, animes, voltees ni gires la imagen; no crees botones o iconos con ella.
  - Tamaño mínimo del dispositivo: **25 mm** de alto en impresión y **200 px** en pantalla.
  - Usa la última generación de dispositivos para la que está desarrollada tu app; no muestres productos de la
    competencia junto a los de Apple.
  - Prohibido: renderizar en 3D o simular un producto de Apple, ilustraciones de productos (salvo material
    instructivo), troquelados con su forma, logotipos o gráficos que representen un producto Apple. Si dibujas un
    dispositivo genérico, sin detalles exclusivos de Apple (botón de inicio, alojamiento de sensores, interruptor…).
- HIG App icons: «Don’t use replicas of Apple hardware products» en el icono.

## 4. Marcas, logotipos e insignias

- [Licensing and Trademarks](https://developer.apple.com/licensing-trademarks/): insignias y logotipos oficiales
  (App Store, Apple Pay, Apple Wallet, Apple Music, Apple Podcasts, Apple Health, Apple Home, CarPlay, Find My,
  MagSafe, MFi, Swift, Mac…). El **logotipo Mac** exige firmar el *Mac Logo Trademark License Agreement*.
- Insignia App Store (Marketing Guidelines): una por pieza, subordinada al mensaje principal; no la modifiques,
  inclines ni animes; margen libre mínimo = **un cuarto de la altura** de la insignia; usa solo la artwork
  proporcionada.
- Logotipo de Apple: «Never use the Apple logo in place of the word Apple. Don’t use the standalone Apple logo.»
  (Marketing). En la UI: «Never include the Apple logo in any button label» y no crees un logotipo propio de
  Apple; usa los archivos oficiales (Sign in with Apple, Tap to Pay, Apple Pay).
- Nombres: las marcas de Apple **no se traducen** («Always set Apple trademarks in English»); escribe iPhone,
  iPad, Apple Watch, Apple Vision Pro, App Store, Apple In-App Purchase tal cual; no digas «iPhone NombreApp» sino
  «NombreApp para iPhone»; las marcas de Apple no pueden aparecer en el nombre ni en las imágenes de tu app (HIG
  App Clips, Apple Pay, HomeKit…).
- Símbolos ™/®: solo en comunicaciones de EE. UU., la primera vez en el cuerpo del texto; nunca en titulares ni en
  la insignia. Incluye líneas de crédito («… are trademarks of Apple Inc.») donde haya avisos legales.
- URL: una marca de Apple solo puede ir **después** del nombre de tu empresa o producto; nunca al principio.
- Apple Pay: no ajustes ancho, radio ni proporción de la marca; sin efectos; mínimos de botón en
  `hig/technologies/apple-pay.md`.

## 5. Aplicado a una web «estilo Apple»

| Quiero… | ¿Se puede? | Cómo |
|---|---|---|
| Usar la tipografía del sistema | Sí | `-apple-system`/`system-ui` sin incrustar archivos (`web.md` §1) |
| Incrustar SF Pro o New York | No | Usa Inter u otra fuente libre como alternativa |
| Usar SF Symbols en la web | No consta permiso | Iconos propios con licencia clara |
| Imitar el estilo visual (Liquid Glass, colores, espaciados) | Sí, el estilo no es marca | Valores de `tokens.md`; sin logotipos ni marcas de Apple |
| Mostrar mi app dentro de un iPhone | Sí, con los marcos oficiales | Reglas de *Apple Product Images* |
| Poner «Disponible en el App Store» | Sí | Insignia oficial, sin modificar, con margen libre |
| Decir que es «de Apple» o usar el logotipo de Apple | No | — |
