# Adaptar una app de iOS a un iPhone plegable ("iPhone Duo"): barras y pliegue

> **Aviso importante:** no tengo información fiable sobre un dispositivo llamado oficialmente **"iPhone Duo"** ni sobre unas guías de Apple publicadas para él. No me lo voy a inventar: no te puedo dar medidas, nombres de API ni reglas de la HIG específicas de ese modelo. Lo que sí puedo darte son los principios que Apple ya aplica (safe areas, size classes, diseño adaptable, barras del sistema, comportamiento en iPad) y cómo se trasladan a un iPhone con pantalla plegable o doble. **Antes de cerrar decisiones, contrasta todo con la HIG actual, la documentación de UIKit/SwiftUI y el simulador de ese dispositivo en Xcode.**

---

## 1. La idea de fondo: deja de pensar en "un tamaño de iPhone"

Un plegable es, en la práctica, **dos dispositivos en uno**:

- **Plegado:** se comporta como un iPhone normal (ancho compacto).
- **Desplegado:** una superficie mucho más ancha, más cercana a un iPad mini, donde es probable que el ancho pase a ser **regular**.

Y además la app **cambia de uno a otro en caliente**, sin reiniciarse. Por eso:

- Diseña con **size classes** y con el tamaño real de la ventana/escena, nunca con el modelo de dispositivo (`UIDevice`, `UIScreen.main.bounds`, comprobaciones de `userInterfaceIdiom == .phone` para decidir el layout…).
- Usa **Auto Layout / SwiftUI con layouts adaptables**, no posiciones fijas.
- Asegúrate de que la transición plegado ↔ desplegado **conserva el estado**: la pantalla en la que estaba el usuario, el scroll, el texto escrito, la selección y la reproducción en curso.
- Si tu app ya funciona bien en iPad (incluido Split View y Stage Manager con ventanas redimensionables), tienes medio camino hecho.

---

## 2. Barras (navegación, pestañas, herramientas)

### Usa siempre los componentes del sistema
`UINavigationBar` / `NavigationStack`, `UITabBarController` / `TabView`, `UIToolbar` / `.toolbar`. Son los que Apple adapta automáticamente a nuevos tamaños, a la geometría de la pantalla y al estilo visual actual (Liquid Glass en iOS 26). Las barras hechas a mano son las que se rompen primero en un dispositivo nuevo.

### Respeta las safe areas, no las calcules
- Ancla contenido y barras a `safeAreaLayoutGuide` (UIKit) o deja que SwiftUI gestione las safe areas; usa `safeAreaInset`/`safeAreaPadding` para barras propias.
- No metas a mano márgenes para la isla dinámica, el indicador de inicio ni las esquinas redondeadas. Un plegable puede tener **safe areas distintas en cada postura** (cámara en otra posición, esquinas diferentes, quizá zonas a evitar junto al pliegue). Si el sistema las expone, tu layout las recibirá solo si no las sobrescribes.
- Deja que el contenido **se desplace por debajo** de las barras (scroll edge effect / fondo translúcido) en lugar de recortarlo con fondos opacos.

### Barra de pestañas: plegado vs. desplegado
- **Plegado:** tab bar inferior estándar, como en cualquier iPhone.
- **Desplegado (ancho regular):** es muy probable que lo adecuado sea lo que ya hace iPad: tab bar más compacta/flotante en la parte superior o **convertirla en barra lateral**. En iOS 18+ lo tienes con `TabView` + `.tabViewStyle(.sidebarAdaptable)` y en UIKit con `UITabBarController` en modo `.tabSidebar`. Esto evita una tab bar de cinco iconos estirada a lo ancho de una pantalla grande.
- Mantén **las mismas secciones** en ambas posturas: el usuario no debe perder destinos al desplegar.

### Barra de navegación y toolbars
- Desplegado, con columnas (ver punto 4), **cada columna tiene su propia barra de navegación**. No pongas una sola barra que cruce toda la pantalla con acciones de la columna derecha alineadas a la izquierda o viceversa.
- Agrupa las acciones de la toolbar según el contenido al que afectan y colócalas en la columna de ese contenido.
- En pantalla ancha puedes mostrar más acciones en la barra; en compacto, pásalas a un menú (`UIMenu` / `Menu`) en lugar de apretarlas.
- Comprueba títulos grandes, campos de búsqueda (`searchable`) y botones de retroceso en ambas posturas: los títulos largos que se truncan plegados pueden verse bien desplegados, y al revés con títulos centrados que quedan justo encima del pliegue.

### Barras y pliegue
- **Ningún botón de una barra debe quedar sobre el pliegue.** Si una barra cruza toda la anchura, revisa que los elementos centrados (título, controles segmentados, botones centrales de la toolbar) no caigan en la bisagra.
- Si el dispositivo resulta ser de **dos pantallas físicas con bisagra** (y no una pantalla continua), una barra que cruce el hueco quedará visualmente partida: es una razón más para usar barras por columna.

---

## 3. El pliegue

Hay dos escenarios posibles, y el diseño cambia según cuál sea:

| Tipo | Qué implica |
|---|---|
| **Pantalla continua con pliegue** (sin hueco) | Se puede mostrar contenido a través del pliegue, pero el pliegue puede notarse al tacto y a la vista (brillo, reflejos, ligera hendidura). |
| **Dos pantallas con bisagra** (hueco físico) | El área de la bisagra no muestra nada; tratarlo como una "zona muerta" que separa dos regiones. |

### Reglas prácticas
1. **Nada interactivo ni crítico sobre el pliegue**: botones, campos de texto, controles deslizantes, handles de arrastre, el cursor de edición, códigos QR, caras en videollamadas, texto que hay que leer con precisión.
2. **Lo que sí puede cruzarlo**: contenido continuo y "tolerante", como fotos o vídeo a pantalla completa, mapas, fondos, lienzos de dibujo o listas con scroll (siempre que el texto no quede siempre en el mismo punto del pliegue).
3. **Aprovecha el pliegue como separador natural**: es el sitio lógico para el divisor de un split view (lista | detalle, bandeja | mensaje, vídeo | comentarios).
4. **Diálogos, alertas, hojas y popovers**: usa los del sistema (`alert`, `sheet`, `popover`, `confirmationDialog`), que el sistema debería posicionar correctamente. Si haces modales propios centrados, **acabarán justo encima del pliegue**: evítalo.
5. **Teclado**: ten en cuenta que puede ocupar una mitad o toda la anchura; usa `keyboardLayoutGuide` (UIKit) o el manejo automático de SwiftUI, nunca alturas fijas.
6. **Gestos**: no coloques gestos de arrastre que empiecen justo en el pliegue, y no dependas de gestos horizontales que atraviesen la bisagra en un dispositivo de dos pantallas.
7. **Posturas semiabiertas** (tipo "portátil" o "tienda"): si el sistema las soporta y las notifica, son útiles para cámara, vídeo o llamadas (contenido arriba, controles abajo). Implémentalas **solo si hay una API oficial** para detectar la postura y la posición del pliegue; no la deduzcas a partir del tamaño de la pantalla.

> Sobre las APIs: en Android esto existe como `FoldingFeature` (Jetpack WindowManager). **No sé si Apple ha publicado un equivalente** para este dispositivo (por ejemplo, como safe area, como una guía de layout o como información de la escena). Búscalo en la documentación de UIKit/SwiftUI del SDK correspondiente antes de diseñar en torno a ello. Si no existe, la estrategia segura es: columnas con el divisor en el centro y nada crítico en la franja central.

---

## 4. Patrón de layout recomendado al desplegar

- **Navegación jerárquica (lista → detalle):** `NavigationSplitView` (SwiftUI) o `UISplitViewController` (UIKit). Plegado colapsa a una pila normal; desplegado muestra dos columnas, con el divisor en el pliegue.
- **Contenido único (lectura, vídeo, foto):** aprovecha el ancho, pero limita la longitud de línea del texto (`readableContentGuide`) y evita que un párrafo cruce el pliegue a media línea; considera dos columnas de texto o márgenes amplios.
- **Rejillas y colecciones:** aumenta el número de columnas según el ancho disponible, y si puedes, haz que el hueco entre columnas coincida con el pliegue.
- **No te limites a "estirar" la versión de iPhone**: es el fallo más común y el que peor se ve.

---

## 5. Lista de comprobación

- [ ] El layout depende de size classes y del tamaño de la ventana, no del modelo.
- [ ] La transición plegado ↔ desplegado conserva estado, scroll, selección y texto.
- [ ] Todas las barras son componentes del sistema y respetan las safe areas.
- [ ] La tab bar se adapta (inferior plegado; superior o barra lateral desplegado) con las mismas secciones.
- [ ] Desplegado, cada columna tiene su propia barra y sus propias acciones.
- [ ] Ningún botón, campo, título centrado ni modal queda sobre el pliegue.
- [ ] Alertas, hojas y popovers son del sistema.
- [ ] El teclado se gestiona con guías de layout, no con alturas fijas.
- [ ] Probado en el simulador del dispositivo en ambas posturas, en vertical y horizontal, con Dynamic Type grande y con texto en idiomas largos (alemán) y de derecha a izquierda (árabe).
- [ ] Revisado contra la HIG y la documentación oficial de Apple para este modelo.

---

**Resumen:** usa barras del sistema y safe areas sin márgenes manuales, deja que la tab bar se convierta en barra lateral cuando haya anchura, da a cada columna su propia barra y trata el pliegue como el divisor natural entre dos zonas: nada interactivo ni crítico encima, y solo contenido continuo y tolerante cruzándolo. Para lo específico de este dispositivo (posición exacta del pliegue, APIs de postura y safe areas nuevas), consulta la documentación oficial, porque ahí no te puedo dar datos fiables.
