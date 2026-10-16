# Iconos de app: lo que dice Apple en su vídeo más reciente

## El vídeo

- **Título:** *Icon Composer for Beginners Group Lab* (WWDC26)
- **Publicado:** 10-6-2026 · **Duración:** 61:39 · **Idioma:** inglés
- **Enlace:** https://developer.apple.com/videos/play/wwdc2026/8012/

**Por qué este vídeo:** es el más reciente del catálogo de diseño de Apple que trata los iconos de app (las fuentes se descargaron el 15-10-2026). Los vídeos posteriores (las Tech Talks de iPhone Duo del 9-9-2026 y los Group Labs de iPhone Duo) no tratan los iconos de app.

**Aviso:** no es una sesión con guion, es un *Group Lab*. El equipo de iconos e Icon Composer hace una demo y luego responde preguntas en directo. Las frases son conversación espontánea, a veces sin pulir. La sesión de referencia sobre el diseño de iconos sigue siendo [*Say hello to the new look of app icons*](https://developer.apple.com/videos/play/wwdc2025/220/) (WWDC25).

## En pocas palabras

Apple presenta **Icon Composer 2** y el **renderizado de iconos de la versión 27**. Trae un especular más nítido con zonas oscuras, un control 2D de refracción, nuevas sombras y translucidez que conviene revisar. Para los iconos ya hechos en 2025, la recomendación es abrirlos en la nueva versión y revisarlos; no hace falta recompilar la app. El resto del vídeo repite buenas prácticas: formas vectoriales simples, SVG, capas exportadas al tamaño del lienzo, revisar el icono a todos los tamaños y que se reconozca sin depender del color.

## Lo que dice, con marca de tiempo

### Novedades del renderizado (versión 27)

| Tiempo | Qué dice | Cita literal |
|---|---|---|
| [1:46](https://developer.apple.com/videos/play/wwdc2026/8012/?time=106) | Recuerda qué es Icon Composer. Es la herramienta que salió en 2025 para preparar los iconos para el renderizado Liquid Glass, y este año se actualiza. | «…a tool that we debuted last year, which allows you to customize and modify your app icons to receive the new liquid glass rendering…» |
| [4:37](https://developer.apple.com/videos/play/wwdc2026/8012/?time=277) | **Especular**: es automático por defecto, pero se puede forzar *inside* o *outside*. *Inside* funciona cuando el primer plano es más oscuro que el fondo. *Outside* funciona cuando el fondo es más oscuro que el primer plano. | «By default, you'll get automatic treatment, which most of the time will do what you want it to do, but you can actually go in and select whether inside or outside.» |
| [5:52](https://developer.apple.com/videos/play/wwdc2026/8012/?time=352) | **Refracción** (nuevo): es un control 2D. El eje vertical ajusta la altura y el horizontal la intensidad. También admite refracción inversa. | «So you can see here if you go up and down, this is actually controlling the height of the refraction.» |

### Flujo de trabajo para un icono nuevo

| Tiempo | Qué dice | Cita literal |
|---|---|---|
| [10:26](https://developer.apple.com/videos/play/wwdc2026/8012/?time=626) | Hay cuatro pasos: tener la idea o metáfora, dibujar por capas en tu herramienta, exportar las capas e importarlas a Icon Composer para ajustarlas. | «So first step is coming up with an idea, right?» |
| [11:46](https://developer.apple.com/videos/play/wwdc2026/8012/?time=706) | Usa formas vectoriales simples y potentes, y evita el detalle fino complejo. | «…if you stick to really, you know, powerful but simple vector shapes.» |
| [12:34](https://developer.apple.com/videos/play/wwdc2026/8012/?time=754) | Exporta las capas al tamaño completo del lienzo. Así llegan ya colocadas a Icon Composer. | «So if you export them at the full canvas size, then when you bring them into Icon Composer, they'll all already be correctly positioned…» |
| [13:04](https://developer.apple.com/videos/play/wwdc2026/8012/?time=784) | Hay plantillas para Figma, Sketch, Illustrator y Photoshop. La de Illustrator incluye un script que recomiendan. | «We have templates for, for applications, we have Figma, we have Sketch, Illustrator, and Photoshop…» |
| [13:27](https://developer.apple.com/videos/play/wwdc2026/8012/?time=807) | **Prefiere SVG**. Se pueden importar bitmaps, pero la recomendación es usar vectores escalables. | «You can use bitmaps, you can bring them into Icon Composer, but the recommendation is to use scalable vectors, SVG…» |

### El error más común

| Tiempo | Qué dice | Cita literal |
|---|---|---|
| [14:57](https://developer.apple.com/videos/play/wwdc2026/8012/?time=897) | El error más común es no revisar el icono a todos los tamaños y presentaciones. Míralo sobre todo a su tamaño más pequeño y sobre distintos fondos. | «…it's really important to evaluate it at all the different sizes and presentations that it's going to be. Don't skip that step.» |
| [15:35](https://developer.apple.com/videos/play/wwdc2026/8012/?time=935) | Mira el icono como lo verá el usuario. | «…it's important to really make sure you see it the way the customer will.» |
| [18:00](https://developer.apple.com/videos/play/wwdc2026/8012/?time=1080) | Apple quiere que el icono «esté vivo» y se adapte a todo el ecosistema: Mac, iPhone y Watch. | «…we're trying to make sure that the icon has, is alive and has can adapt and live in the rest of the devices ecosystem…» |

### Pasar un icono de iOS 26 a iOS 27

| Tiempo | Qué dice | Cita literal |
|---|---|---|
| [24:18](https://developer.apple.com/videos/play/wwdc2026/8012/?time=1458) | Abre el archivo de Icon Composer de 2025 en la versión nueva y el nuevo renderizado se aplica solo. Después revisa especulares, sombras y refracción. | «…if you have an Icon Composer file from last year is just open it in the new updated Icon Composer and you'll see what it looks like with the new rendering applied to it…» |
| [25:21](https://developer.apple.com/videos/play/wwdc2026/8012/?time=1521) | **No hace falta recompilar.** Un icono hecho con Icon Composer para iOS 26 adopta solo el aspecto de iOS 27. | «…your application doesn't even have to recompile to get the new benefit of the new, the new look.» |
| [26:13](https://developer.apple.com/videos/play/wwdc2026/8012/?time=1573) | **Translucidez:** Apple la redujo en muchos de sus propios iconos para que se vean más nítidos. Esto no se aplica solo, así que revísalo tú. | «…in many of our own app icons this year was we reduced the use of translucency.» |

### Modos clear, mono y tintado

| Tiempo | Qué dice | Cita literal |
|---|---|---|
| [35:08](https://developer.apple.com/videos/play/wwdc2026/8012/?time=2108) | En modo clear, el cristal del icono **no responde** al deslizador de transparencia del sistema. Es una decisión deliberada para que el icono sea siempre legible. | «…it was a deliberate choice to have the glass and clear mode is is does not respond to the slider.» |
| [35:35](https://developer.apple.com/videos/play/wwdc2026/8012/?time=2135) | Explican el motivo: detrás puede haber cualquier fondo y la experiencia tiene que ser legible en todos los casos. | «…we need to make sure that we have a consistent and legible experience in all, in all cases.» |
| [36:13](https://developer.apple.com/videos/play/wwdc2026/8012/?time=2173) | **Mono:** una sola anotación en escala de grises sirve para clear claro, clear oscuro y todos los tintados. | «…there's a single mono mode for which you make grayscale annotations to support both light, clear, dark, clear, and all of the tinted modes.» |
| [43:43](https://developer.apple.com/videos/play/wwdc2026/8012/?time=2623) | **Tintado:** al menos una parte del primer plano debe ser blanca o casi blanca. Aprovecha todo el rango de grises en la anotación mono y usa preferentemente los fondos del sistema. | «So always having foreground elements, being white or close to white, or at least one, one part of that foreground element.» |

### Marca, capas y Xcode

| Tiempo | Qué dice | Cita literal |
|---|---|---|
| [38:20](https://developer.apple.com/videos/play/wwdc2026/8012/?time=2300) | Para dar volumen a un logotipo plano en Liquid Glass, separa sus partes en capas. Por ejemplo, unos ojos pueden ir *encima* de la cara en vez de recortados en ella. | «…should the eyes be above the face rather than cut out of the face?» |
| [40:09](https://developer.apple.com/videos/play/wwdc2026/8012/?time=2409) | **Xcode** funciona igual que en 2025. Arrastra el `.icon` al proyecto, junto a los archivos Swift y no dentro del asset catalog. | «…you just drag it into your Xcode project, put it right next to your Swift files.» |
| [40:26](https://developer.apple.com/videos/play/wwdc2026/8012/?time=2426) | Después, en el editor del target, comprueba que el nombre del icono coincide con el del archivo. | «…make sure the app icon name matches the file that you dragged in.» |
| [42:08](https://developer.apple.com/videos/play/wwdc2026/8012/?time=2528) | Las capas no se vuelven de cristal todas a la fuerza. Tú eliges cuáles llevan Liquid Glass, y puedes desactivarlo en las que ya tengan un tratamiento prerrenderizado. | «You can then choose which layers to use liquid glass on and which ones to maybe opt out of…» |

### Accesibilidad, principiantes y plataformas

| Tiempo | Qué dice | Cita literal |
|---|---|---|
| [49:35](https://developer.apple.com/videos/play/wwdc2026/8012/?time=2975) | **Daltonismo:** el icono tiene que reconocerse por la forma y el contraste, no por el color. | «…you wouldn't want to depend on people's ability to be able to see color, to get meaning out of out of the icon.» |
| [51:24](https://developer.apple.com/videos/play/wwdc2026/8012/?time=3084) | Si nunca has hecho un icono, empieza por esta pregunta: ¿cómo quieres que la gente recuerde tu app? | «How do you want people to remember your app?» |
| [56:18](https://developer.apple.com/videos/play/wwdc2026/8012/?time=3378) | Apple garantiza que el diseño hecho en Icon Composer se reproduzca fielmente en todas las plataformas. | «…the design you land with in Icon Composer is faithfully executed and distributed in a natural way across all endpoints.» |
| [57:36](https://developer.apple.com/videos/play/wwdc2026/8012/?time=3456) | **Apple Watch:** replantea la composición para el círculo. Por ejemplo, Maps centra el indicador. | «…when you design for watch, you might want to reconsider how that layout works for a circle.» |
| [1:01:10](https://developer.apple.com/videos/play/wwdc2026/8012/?time=3670) | Para cualquier duda, remiten a las Human Interface Guidelines. | «If you have any questions, I highly recommend going to the Apple Human Interface Guidelines.» |

## Contexto

- **Qué cambió en las HIG:** el 8-6-2026 Apple actualizó la página [App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons) con el registro «Refined guidance for Liquid Glass». Ese cambio coincide con este vídeo (Icon Composer 2: refracción por capa, nuevos brillos especulares y anotación Default/Dark/Mono).
- **Los datos de base no cambian respecto a 2025:**
  - Lienzo de 1024 px en iOS, iPadOS y macOS.
  - Lienzo de 1088 px en watchOS.
  - Apariencias default, dark, clear y tinted.

  Están en el vídeo [*Say hello to the new look of app icons*](https://developer.apple.com/videos/play/wwdc2025/220/?time=179) (WWDC25, 2:59 y 4:38).
- **Prevalece la versión 27:** si algo de los vídeos de 2025 choca con este lab, por ejemplo el nivel de translucidez, vale lo del lab y lo de la página de las HIG actualizada.

*Marcas de tiempo y citas sacadas del archivo de referencia del vídeo, que se verificó contra la transcripción oficial de Apple. Para el texto completo, abre el enlace del vídeo.*
