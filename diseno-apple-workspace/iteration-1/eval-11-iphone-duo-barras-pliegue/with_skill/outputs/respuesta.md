# Adaptar tu app de iOS a iPhone Duo: barras y pliegue

**En corto:** en iPhone Duo, las barras (navigation bar, toolbar y tab bar) **dejan de estar arriba y abajo y pasan a una franja vertical en el lateral**. Si usas las barras del sistema, el cambio es casi automático. Lo que sí depende de ti es dar a cada elemento un título y un símbolo, ordenarlos y decidir qué se oculta antes en el menú de desbordamiento. Con el **pliegue** pasa algo parecido: los componentes del sistema ya se apartan de él. Tu trabajo es que **ningún control ni contenido que no haga scroll quede sobre el pliegue**, y que la app funcione igual en todas las posturas.

Fuente principal: la página de las HIG [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo), nueva desde el **9-9-2026**, y tres Tech Talks publicados el mismo día. Las reglas en **negrita y en inglés** son literales de Apple. El resto es resumen mío de esas fuentes.

> Recuerda: Apple insiste en que sigues diseñando para iPhone. Tu app debe adaptarse con las *size classes*: **compact width** en la pantalla exterior y **regular width** en la interior. No hace falta un diseño distinto para cada postura. «Avoid fixed widths, breakpoints, or any metrics tied to a specific screen.» ([Design for iPhone Duo, 4:08](https://developer.apple.com/videos/play/tech-talks/111466/?time=248))

---

## 1. Barras: qué cambia

- **Cerrado (pantalla exterior)** y **abierto en horizontal**: la navegación, la toolbar y la tab bar comparten una **región vertical en el lateral**. Ahí también están la Dynamic Island y la nueva barra de estado. La pantalla exterior es más ancha y menos alta, y así se gana espacio vertical para el contenido ([Raise the bar with iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111462/); [Design for iPhone Duo, 5:36](https://developer.apple.com/videos/play/tech-talks/111466/?time=336): «it's not just your app controls that have moved to the side»).
- **Abierto en vertical (pantalla interior)**: solo en esta postura se vuelve a las barras horizontales de siempre ([Raise the bar, 5:41](https://developer.apple.com/videos/play/tech-talks/111462/?time=341): «not every pose lays out bars vertically»).
- La franja está **alineada con el hardware**: mantiene la misma posición respecto a la cámara exterior. En idiomas de derecha a izquierda (RTL) **no cambia de lado**; es el contenido el que se adapta alrededor ([Raise the bar, 4:18](https://developer.apple.com/videos/play/tech-talks/111462/?time=258)).
- Con **Split View multitasking** en la pantalla interior, cada app coloca sus controles en su borde exterior: la app de la izquierda los lleva a la izquierda (HIG, *Vertical controls*).

Esto contradice todo lo publicado antes de septiembre de 2026, que da por hecho que las barras van arriba y abajo. Aplica la guía de iPhone Duo **solo a ese dispositivo**.

## 2. Barras: lo que tienes que hacer

### Activarlo bien
1. **Compila con el SDK más reciente** y **usa las barras de los contenedores de navegación** (`TabView`/`NavigationStack` en SwiftUI; `UINavigationController`/`UITabBarController` en UIKit). Si montas tus propias barras con `UIToolbar`, `UINavigationBar` o `UITabBar`, el sistema no las tiene en cuenta ([Raise the bar, 2:20](https://developer.apple.com/videos/play/tech-talks/111462/?time=140) y [2:36](https://developer.apple.com/videos/play/tech-talks/111462/?time=156)).
2. **«In general, don’t override the default bar placement.»** (HIG). Apple solo admite dos excepciones para desactivar la barra vertical:
   - apps de una sola página con la interfaz cargada abajo, como Calculadora;
   - sheets con muchos controles y un solo botón de barra, como un Cerrar.

   ([Raise the bar, 14:28](https://developer.apple.com/videos/play/tech-talks/111462/?time=868) y [14:37](https://developer.apple.com/videos/play/tech-talks/111462/?time=877)). En la misma línea: **«Consider using the full display width for interfaces where bars aren’t necessary.»**

### Orden y agrupación
3. **«Follow the standard placement order for toolbar items.»** Arriba van la navegación principal (Atrás o Cerrar) y después la acción destacada (Done). El resto mantiene su agrupación ([Raise the bar, 4:47](https://developer.apple.com/videos/play/tech-talks/111462/?time=287)). En UIKit, usa un *leading item* con `leftItemSupplementsBackButton = false`, que es el valor por defecto ([5:05](https://developer.apple.com/videos/play/tech-talks/111462/?time=305)).
4. Los botones de la toolbar superior suben a lo alto de la franja y los de la inferior bajan a la parte baja. La tab bar queda alineada abajo ([Design for iPhone Duo, 6:04](https://developer.apple.com/videos/play/tech-talks/111466/?time=364)). Piénsalo como «rotating 90 degrees into a vertical stack» ([Raise the bar, 3:15](https://developer.apple.com/videos/play/tech-talks/111462/?time=195)).
5. **«Group related toolbar items instead of spacing them manually.»** y **«Locate controls near the content they affect.»** (HIG). Los elementos relacionados deben quedarse en el mismo eje ([Raise the bar, 8:08](https://developer.apple.com/videos/play/tech-talks/111462/?time=488)).
6. **«Keep controls consistent across device poses.»** y **«Account for asymmetry in your layouts.»** (HIG). Los márgenes ya no son simétricos: no des por hecho que los insets de lados opuestos son iguales ([Prepare your app for iPhone Duo, 7:25](https://developer.apple.com/videos/play/tech-talks/111461/?time=445)).

### Contenido de cada elemento
7. **«Provide both a title and a symbol for each toolbar item that isn’t text-only.»** (HIG). Un elemento con solo icono puede pasar a la barra vertical; uno con solo texto se queda en horizontal. Aunque el contenido sea una imagen, ponle título ([Raise the bar, 7:36](https://developer.apple.com/videos/play/tech-talks/111462/?time=456)).
8. **«Keep text-based buttons to a minimum.»** (HIG). Prefiere elementos de solo símbolo: por ejemplo, un *badge* en lugar de un contador junto al texto ([Raise the bar, 9:12](https://developer.apple.com/videos/play/tech-talks/111462/?time=552)). Si el texto lleva información propia, como el importe del carrito, déjalo en horizontal.
9. Los elementos demasiado anchos para la franja, como un botón de texto o un **segmented control**, se quedan en la navigation bar ([Design for iPhone Duo, 6:22](https://developer.apple.com/videos/play/tech-talks/111466/?time=382)).
10. **Vistas personalizadas en la barra:** deben caber en el ancho fijo de la barra o tener una versión vertical. Revisa si alguna métrica debe cambiar en esa versión ([Raise the bar, 10:11](https://developer.apple.com/videos/play/tech-talks/111462/?time=611)).
11. Las **barras de accesorios del teclado** siguen pegadas al teclado y no pasan al eje vertical ([Raise the bar, 10:00](https://developer.apple.com/videos/play/tech-talks/111462/?time=600)). Los *inspectors* no tienen barra propia al expandirse, porque la columna de detalle ya tiene una ([3:50](https://developer.apple.com/videos/play/tech-talks/111462/?time=230)).

### Cuando no cabe todo
12. **«Use the system overflow menu.»** (HIG). La elipsis es *el* símbolo de desbordamiento en iPhone, así que no la uses para otros menús ([Raise the bar, 12:53](https://developer.apple.com/videos/play/tech-talks/111462/?time=773)). Tampoco conviertas cualquier menú existente en un desbordamiento ([12:50](https://developer.apple.com/videos/play/tech-talks/111462/?time=770)).
13. **«When space is limited, preserve either the toolbar or tab bar based on the experience that the view provides.»** (HIG). En las vistas orientadas a una tarea, minimiza la tab bar y conserva las acciones de la toolbar.
14. **«Prioritize frequently used toolbar items to keep them easily available.»** (HIG). Las acciones frecuentes (Compose en Mail, New Note en Notas) y los elementos con *badge* deben ser los últimos en pasar al desbordamiento. Asigna **prioridades de desbordamiento** para que el sistema pueda adaptarse ([Raise the bar, 13:59](https://developer.apple.com/videos/play/tech-talks/111462/?time=839) y [15:23](https://developer.apple.com/videos/play/tech-talks/111462/?time=923)).

### Composición alrededor de la barra
15. En la pantalla exterior, casi todo el contenido necesita un desplazamiento para no quedar debajo de los controles. Lo consigues automáticamente con los *safe area insets* ([Design for iPhone Duo, 6:52](https://developer.apple.com/videos/play/tech-talks/111466/?time=412)). Centra en toda la pantalla, sin desplazamiento, solo las interfaces inmersivas que no hacen scroll, y siempre que ningún elemento interactivo quede tapado por los controles de la derecha ([7:10](https://developer.apple.com/videos/play/tech-talks/111466/?time=430)).
16. **Accesibilidad:** con Reduce Transparency, la barra vertical se muestra con fondo ([Raise the bar, 10:57](https://developer.apple.com/videos/play/tech-talks/111462/?time=657)). Con la barra del sistema no tienes que hacer nada; si es una barra propia, tendrías que replicar este comportamiento.

---

## 3. El pliegue (folding region o región de división)

En las HIG, el pliegue es una de las tres **reserved regions** de iPhone Duo. Se suman a las safe areas habituales:

| Región reservada | Cuándo existe |
|---|---|
| Cámara frontal exterior | Siempre. Se amplía a la Dynamic Island con las Live Activities |
| Cámara frontal interior | Solo con la cámara activa (es una región de *oclusión*: tapa, no divide) |
| **Región del pliegue** | **Condicional**, según cómo se use el dispositivo. En los vídeos se llama *division region* y está activa al plegarlo parcialmente |

Fuentes: HIG, *Reserved regions*; [Strike a pose with adaptive layouts on iPhone Duo, 0:27](https://developer.apple.com/videos/play/tech-talks/111463/?time=27) y [7:54](https://developer.apple.com/videos/play/tech-talks/111463/?time=474).

### Reglas
1. **«Adapt your layout when the device folds.»** y **«Avoid extreme layout changes as people fold the device.»** (HIG).
2. **No dejes controles ni contenido estático cruzando el pliegue.** Apple lo explica así: «We found buttons are tough to tap when they land right in the fold.» ([Design for iPhone Duo, 9:28](https://developer.apple.com/videos/play/tech-talks/111466/?time=568)) y «Content and controls that span the fold behave very similarly.» ([Strike a pose, 2:00](https://developer.apple.com/videos/play/tech-talks/111463/?time=120)).
3. **Usa componentes del sistema.** Las sheets, alerts, menús y botones de toolbar se apartan del pliegue automáticamente. Por ejemplo, con el dispositivo parcialmente plegado, las sheets se deslizan para no quedar sobre él ([Design for iPhone Duo, 9:17](https://developer.apple.com/videos/play/tech-talks/111466/?time=557)). «Many system components automatically adapt to reserved regions.» (HIG).
4. **El contenido con scroll no tiene que evitarlo**: artículos, feeds, documentos y listas no se desplazan ([Design for iPhone Duo, 9:57](https://developer.apple.com/videos/play/tech-talks/111466/?time=597); [Strike a pose, 3:45](https://developer.apple.com/videos/play/tech-talks/111463/?time=225)). Lo que tienes que revisar son las **interfaces centradas y fijas**. Apple recomienda empezar por ahí la auditoría ([Strike a pose, 16:37](https://developer.apple.com/videos/play/tech-talks/111463/?time=997)).
5. **Patrón de desplazamiento (displacement):** mueve, redimensiona o reorganiza lo que ya tienes en lugar de inventar otra interfaz.
   - Si un elemento es independiente, muévelo solo.
   - Si varios elementos funcionan juntos, muévelos juntos. Por ejemplo, la foto seleccionada y su menú contextual se alinean juntos alrededor del pliegue.
   - No los alejes demasiado de su posición original y evita el movimiento excesivo.

   ([Strike a pose, 3:17](https://developer.apple.com/videos/play/tech-talks/111463/?time=197), [3:26](https://developer.apple.com/videos/play/tech-talks/111463/?time=206) y [3:35](https://developer.apple.com/videos/play/tech-talks/111463/?time=215))
6. **Adónde moverlo:**
   - En **postura libro**, elementos como las alerts van al lado final (*trailing*), más cerca de donde aparecerán al cerrar.
   - En **postura sobre la mesa**, lo que se mira va arriba y lo que se toca, abajo.

   ([Strike a pose, 4:09](https://developer.apple.com/videos/play/tech-talks/111463/?time=249))
7. **Rejillas:** si hay región de división, prefiere un **número par de columnas**, esté activa o no ([Strike a pose, 7:42](https://developer.apple.com/videos/play/tech-talks/111463/?time=462)).
8. **Layouts de dos zonas:** si tu pantalla ya parece una división (reproductor y transcripción, lista y detalle…), plantéate una *arrangement view*:
   - **split** para una relación principal–detalle;
   - **overlay** para una relación primer plano–fondo.

   Es la regla **«Consider an arrangement view when your layout already resembles one.»**, y va junto a **«Keep navigation outside of arrangement views.»** (HIG): no metas un `NavigationSplitView` dentro de un `ArrangementView`, ni `ArrangementView`s dentro de `List` o `ScrollView` ([Strike a pose, 15:08](https://developer.apple.com/videos/play/tech-talks/111463/?time=908) y [16:19](https://developer.apple.com/videos/play/tech-talks/111463/?time=979)). Las arrangements llegan con iOS 27.1. Las APIs son [ArrangementView](https://developer.apple.com/documentation/swiftui/arrangementview) en SwiftUI y [UIArrangementViewController](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller) en UIKit.
9. **Layouts complejos:** consulta las regiones reservadas con [ReservedRegion](https://developer.apple.com/documentation/swiftui/reservedregion) en SwiftUI o [UIView.ReservedRegion](https://developer.apple.com/documentation/uikit/uiview/reservedregion) en UIKit, y no calcules a mano dónde está la bisagra ([Prepare your app for iPhone Duo, 9:08](https://developer.apple.com/videos/play/tech-talks/111461/?time=548)).
10. **Mismas funciones en todas las posturas:** **«Maintain the same functionality across device poses.»** (HIG). Si haces un diseño especial para una postura, como «sobre la mesa», debe tener los mismos controles y la misma jerarquía ([Design for iPhone Duo, 4:55](https://developer.apple.com/videos/play/tech-talks/111466/?time=295)).

---

## 4. Relacionado: la pantalla interior

- «You don't want just a stretched out iPhone app.» Usa split views (sin cambiar la jerarquía), layouts de dos columnas o la tab bar como sidebar en apps densas ([Design for iPhone Duo, 7:39](https://developer.apple.com/videos/play/tech-talks/111466/?time=459)).
- El split view se expande en la pantalla interior y se reduce a un solo panel en la exterior, igual que entre regular y compact (HIG, *Split views*).
- En código, no uses el *idiom*, la orientación ni `main screen` para decidir el layout. Usa *size classes*, márgenes de layout y *safe areas* ([Prepare your app for iPhone Duo, 3:50](https://developer.apple.com/videos/play/tech-talks/111461/?time=230) y [3:57](https://developer.apple.com/videos/play/tech-talks/111461/?time=237)).

## 5. Lo que Apple no publica

Las fuentes no dan medidas numéricas de:

- el **ancho de la franja vertical** de barras;
- el **ancho o la posición de la región del pliegue**;
- las **dimensiones de cada pantalla**. Las tablas de tamaños por dispositivo se retiraron de *Layout* el 9-9-2026.

No las pongas fijas: léelas en tiempo de ejecución con safe area insets y reserved regions. Para maquetar, Apple ofrece los [marcos de iPhone Duo](https://devimages-cdn.apple.com/design/resources/download/Bezel-iPhone-Duo.dmg) en Design Resources (18-9-2026).

## 6. Cómo probarlo

- Compila con **Xcode 27.1** y prueba el iPhone Duo y sus posturas en **[Device Hub](https://developer.apple.com/documentation/xcode/device-hub)** ([Prepare your app for iPhone Duo, 9:38](https://developer.apple.com/videos/play/tech-talks/111461/?time=578)).
- Para cada pantalla importante, comprueba:
  - [ ] Barras del sistema (no propias) y ubicación por defecto.
  - [ ] Cada elemento de la toolbar tiene título y símbolo; hay pocos botones de texto.
  - [ ] Orden: Atrás o Cerrar arriba, luego Done, luego el resto agrupado.
  - [ ] Prioridades de desbordamiento asignadas; las acciones frecuentes y los *badges* son los últimos en ocultarse.
  - [ ] Contenido desplazado por los safe area insets; nada interactivo tapado por la franja.
  - [ ] Nada interactivo ni estático cruzando el pliegue al plegar parcialmente.
  - [ ] Mismas funciones y jerarquía en pantalla exterior, interior, libro, sobre la mesa y de pie.
  - [ ] Split View multitasking y RTL revisados.
  - [ ] Reduce Transparency e Increase Contrast revisados.

---

**Fuentes**
- HIG: [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo) (nueva, 9-9-2026) · [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) · [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views)
- Vídeos (Tech Talks, 9-9-2026): [Design for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111466/) · [Raise the bar with iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111462/) · [Strike a pose with adaptive layouts on iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111463/) · [Prepare your app for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111461/)
- Documentación: [Preparing your app for iPhone Duo](https://developer.apple.com/documentation/technologyoverviews/preparing-your-app-for-iphone-duo)
