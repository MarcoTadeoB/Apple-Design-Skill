# Revisión según las HIG: pantalla principal de la app de notas (iPhone)

## Resumen

La pantalla tiene problemas en cuatro frentes: **uso de Liquid Glass** (se aplica al contenido y se mezcla con barras sólidas), **legibilidad y accesibilidad** (contraste, tamaño de texto, áreas táctiles), **estructura de la tab bar** (una acción convertida en pestaña, una pestaña desactivada y sin etiquetas) y **permisos** (pide la ubicación al abrir la app y sin contexto).

| # | Problema | Área | Gravedad |
|---|----------|------|----------|
| 1 | Contraste del texto secundario (#C7C7CC sobre blanco ≈ 1,7:1) | Accesibilidad | Crítica |
| 2 | Botones de 24×24 pt en las tarjetas | Accesibilidad / interacción | Crítica |
| 3 | Texto secundario a 10 pt, peso Light y sin Dynamic Type | Tipografía | Alta |
| 4 | «+ Nueva nota» es una pestaña en lugar de una acción | Tab bar | Alta |
| 5 | Pestaña «Papelera» desactivada cuando está vacía | Tab bar | Alta |
| 6 | Pestañas solo con icono, sin texto | Tab bar | Alta |
| 7 | Permiso de ubicación pedido al abrir la app por primera vez | Privacidad | Alta |
| 8 | Liquid Glass aplicado a las tarjetas de contenido | Materiales | Alta |
| 9 | Barra de navegación sólida naranja en lugar del material del sistema | Barras / Liquid Glass | Media |
| 10 | Logotipo centrado en lugar de un título | Navegación / marca | Media |
| 11 | Los tres botones de la barra tintados de azul | Color / jerarquía | Media |
| 12 | «Editar» representado solo con un lápiz | Iconografía / claridad | Media |
| 13 | Colores fijos que no se adaptan al modo oscuro ni a los ajustes de accesibilidad | Color | Media |
| 14 | Botón de borrar visible en cada tarjeta | Acciones destructivas | Media |
| 15 | Barra de navegación sobrecargada y con acciones ambiguas | Jerarquía | Baja |

---

## Problemas en detalle

### 1. Contraste insuficiente del texto secundario (crítico)
- **Qué pasa:** #C7C7CC sobre #FFFFFF da una relación de contraste de aproximadamente **1,7:1**. Las HIG piden como mínimo **4,5:1** para texto de tamaño normal (y 3:1 solo para texto grande y en negrita). Con 10 pt y peso Light, el texto es prácticamente ilegible para muchas personas y también en exteriores con mucho sol.
- **Además:** #C7C7CC equivale a un gris del sistema pensado para separadores y rellenos, no para texto.
- **Solución:** usa los colores semánticos de etiqueta (`secondaryLabel`, y `tertiaryLabel` solo para información poco importante). Se adaptan solos al modo oscuro y a «Aumentar contraste». Comprueba el resultado con el inspector de accesibilidad de Xcode.

### 2. Áreas táctiles de 24×24 pt (crítico)
- **Qué pasa:** las HIG fijan un área táctil mínima de **44×44 pt** en iOS. A 24×24 pt los botones de favorito y borrar son difíciles de pulsar, y al estar juntos es fácil borrar una nota sin querer.
- **Solución:** el icono puede verse a 24 pt, pero el área táctil tiene que llegar a 44×44 pt (con relleno o `contentShape`). Deja suficiente separación entre controles, sobre todo cuando uno de ellos es destructivo.

### 3. Texto a 10 pt, peso Light y sin Dynamic Type (alto)
- **Qué pasa:** las HIG recomiendan **11 pt como mínimo** en iOS y desaconsejan los pesos Ultralight, Thin y Light en tamaños pequeños porque pierden legibilidad. Un tamaño fijo tampoco respeta la preferencia de tamaño de texto de cada persona.
- **Solución:** usa los estilos de texto del sistema (`.footnote` de 13 pt o `.caption1` de 12 pt) con peso Regular y compatibilidad con **Dynamic Type**, incluidos los tamaños de accesibilidad. Comprueba que las tarjetas crecen y que el texto pasa a la línea siguiente sin cortarse.

### 4. «+ Nueva nota» es una pestaña (alto)
- **Qué pasa:** según las HIG, la tab bar sirve **solo para navegar** entre secciones principales de la app, no para ejecutar acciones. Una pestaña que crea una nota rompe ese modelo mental: no lleva a ninguna sección y deja la selección en un estado confuso.
- **Solución:** pasa la creación de notas a un botón de redactar (SF Symbol `square.and.pencil`) en la barra de herramientas inferior o en la barra de navegación, como hace Notas de Apple. En iOS 26, una opción natural es un botón de acción flotante de Liquid Glass junto a la tab bar o en la toolbar.

### 5. Pestaña «Papelera» desactivada cuando está vacía (alto)
- **Qué pasa:** las HIG piden **no desactivar ni ocultar pestañas**. Las pestañas deben estar siempre disponibles para que la interfaz sea estable y predecible. Una pestaña desactivada no explica por qué lo está.
- **Solución:** deja la pestaña activa y, si no hay nada, muestra un estado vacío útil («La papelera está vacía. Las notas eliminadas se guardan aquí 30 días.»), por ejemplo con `ContentUnavailableView`. Plantéate también si «Papelera» merece una pestaña o si funciona mejor como carpeta especial dentro de «Carpetas», como en Notas.

### 6. Pestañas sin texto (alto)
- **Qué pasa:** en iPhone, las HIG recomiendan que cada pestaña lleve **un icono y una etiqueta corta**. Solo con icono, la navegación es ambigua (por ejemplo, ¿qué diferencia hay entre «Notas» y «Carpetas»?).
- **Solución:** añade etiquetas de una sola palabra («Notas», «Carpetas», «Papelera») y SF Symbols reconocibles (`note.text`, `folder`, `trash`). Así VoiceOver también tendrá algo que leer.

### 7. Permiso de ubicación pedido al abrir la app (alto)
- **Qué pasa:** las HIG piden **pedir los permisos solo cuando hacen falta y en el momento en que la persona usa la función** que los necesita. Una app de notas no necesita la ubicación para su función principal. Pedirla al abrir la app, sin contexto, genera desconfianza y aumenta el número de rechazos.
- **Solución:** pide el permiso solo cuando la persona use una función que lo requiera (por ejemplo, «Añadir ubicación a la nota» o «Recordar al llegar a…»). Escribe un texto de propósito (`NSLocationWhenInUseUsageDescription`) claro y concreto, y prioriza «Al usar la app» y la ubicación aproximada cuando baste. La app debe funcionar con normalidad si la persona deniega el permiso.

### 8. Liquid Glass en las tarjetas de contenido (alto)
- **Qué pasa:** Liquid Glass está pensado para la **capa de navegación y controles** que flota sobre el contenido (barras, toolbars, controles, botones flotantes), no para el contenido. Si cada tarjeta es de vidrio, el contenido pierde protagonismo y legibilidad. Además, al desplazarse quedan capas de vidrio debajo de las barras de vidrio, y las HIG desaconsejan apilar vidrio sobre vidrio.
- **Solución:** usa fondos sólidos y semánticos en las tarjetas (o una lista `insetGrouped` con `secondarySystemGroupedBackground`) y reserva Liquid Glass para las barras y los controles flotantes.

### 9. Barra de navegación sólida y naranja (medio)
- **Qué pasa:** en iOS 26, las barras de navegación y las tab bars usan el material Liquid Glass del sistema y dejan que el contenido se vea al desplazarse por debajo (con el efecto de borde de desplazamiento). Si la barra se pinta de un color sólido, se pierde esa jerarquía, la app parece anticuada y los botones de vidrio quedan flotando sobre un fondo plano, donde el efecto no tiene sentido.
- **Solución:** quita el fondo personalizado y usa la barra estándar. Si quieres reflejar la marca, aplica el naranja como **color de acento** (tint global) de forma comedida, no como relleno de la barra.

### 10. Logotipo en lugar de título (medio)
- **Qué pasa:** las HIG piden que la marca sea discreta y **no ocupe la barra de navegación con el logotipo**. La barra debe decir dónde está la persona. Un logotipo no lo dice y no se puede leer con Dynamic Type.
- **Solución:** pon un título descriptivo («Notas», o el nombre de la carpeta), preferiblemente como título grande que se reduce al desplazarse. Deja la marca para el icono de la app y la pantalla de inicio.

### 11. Los tres botones tintados de azul (medio)
- **Qué pasa:** las HIG piden **tintar el vidrio con moderación** y solo en la acción principal, para dar jerarquía. Si los tres botones están tintados, ninguno destaca. Además, el azul sobre el naranja de la barra hace que la app tenga dos colores de acento que compiten entre sí.
- **Solución:** deja los botones secundarios (Compartir, Filtrar) con el estilo de vidrio estándar y tinta como mucho la acción principal de la pantalla (por ejemplo, Nueva nota) con un único color de acento coherente.

### 12. «Editar» solo con un lápiz (medio)
- **Qué pasa:** en iOS, el lápiz (`square.and.pencil` o `pencil`) se asocia a **redactar o escribir**, no a editar una lista (seleccionar, mover o borrar). Puede confundirse con «Nueva nota». La convención del sistema para editar una lista es el botón de texto «Editar» (o «Seleccionar»).
- **Solución:** usa el `EditButton` estándar con texto o un menú «Más» (`ellipsis.circle`) con «Seleccionar notas». Cualquier botón que solo tenga icono necesita una etiqueta de accesibilidad.

### 13. Colores fijos sin modo oscuro ni ajustes de accesibilidad (medio)
- **Qué pasa:** el naranja sólido, el blanco de fondo y el gris #C7C7CC son valores fijos. En modo oscuro, el texto gris claro sobre blanco o el contraste del naranja pueden quedar mal. Tampoco hay versión para «Reducir transparencia» ni «Aumentar contraste».
- **Solución:** usa colores semánticos del sistema o define cada color en el catálogo de recursos con variantes para el modo claro, el oscuro y el de alto contraste. Prueba la pantalla con «Reducir transparencia», «Aumentar contraste» y «Texto en negrita».

### 14. Botón de borrar visible en cada tarjeta (medio)
- **Qué pasa:** tener una acción destructiva siempre visible y pequeña en cada tarjeta invita a borrar sin querer y llena la interfaz.
- **Solución:** usa las **acciones al deslizar** (deslizar a la izquierda para «Eliminar» en rojo, a la derecha para «Favorito») y un **menú contextual** con pulsación prolongada. Permite deshacer, o mueve las notas a la Papelera en lugar de borrarlas para siempre. Si mantienes el botón, aplica el rol destructivo (rojo) y respeta el área táctil de 44 pt.

### 15. Barra de navegación sobrecargada y con acciones ambiguas (bajo)
- **Qué pasa:** el logotipo y tres botones en una barra de iPhone dejan poco espacio, sobre todo con tamaños de texto grandes. Además, «Compartir» en una lista no deja claro qué se comparte.
- **Solución:** deja en la barra solo lo esencial (por ejemplo, Filtrar y un menú «Más»). Mueve «Compartir» a la vista de detalle de la nota, al modo de selección o al menú contextual de cada tarjeta.

---

## Propuesta de pantalla corregida

- **Barra de navegación:** material estándar del sistema, título grande «Notas», a la derecha un botón de filtrar y un menú «Más» (con «Seleccionar notas»), y búsqueda integrada.
- **Lista:** filas o tarjetas con fondo semántico sólido, título en `.headline`, texto secundario en `.subheadline` o `.footnote` con `secondaryLabel` y Dynamic Type, acciones al deslizar y menú contextual.
- **Tab bar:** «Notas», «Carpetas» y, si hace falta, «Papelera», siempre activas y con icono y texto. Sin pestaña de acción.
- **Nueva nota:** un único botón de redactar (`square.and.pencil`), con el color de acento de la app, en la toolbar inferior o flotando en Liquid Glass.
- **Color:** un solo color de acento (por ejemplo, el naranja de la marca) aplicado como tint, nunca como relleno de la barra.
- **Permisos:** ninguno al abrir la app. La ubicación se pide solo al usar una función que la necesite, con un texto de propósito claro.
- **Accesibilidad:** áreas táctiles de 44×44 pt como mínimo, contraste de 4,5:1 o más, etiquetas de VoiceOver en todos los botones con icono, y pruebas con el modo oscuro, «Reducir transparencia» y «Aumentar contraste».
