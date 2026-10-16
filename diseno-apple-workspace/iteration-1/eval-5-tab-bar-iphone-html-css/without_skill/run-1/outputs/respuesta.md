# Barra de pestañas para una app de recetas en iPhone

Te dejo la barra hecha en HTML/CSS en **`index.html`**. Es un solo archivo, sin dependencias. Si lo abres en el ordenador, la verás dentro de un marco de iPhone de 393 × 852 pt. Si lo abres en un iPhone, ocupa toda la pantalla y usa las zonas seguras reales (`env(safe-area-inset-*)`).

> **Sobre las fuentes:** he trabajado sin acceso a la web. Las referencias de abajo salen de lo que sé de la documentación de Apple, WebKit y W3C, y no las he comprobado durante esta sesión. Las medidas de la barra flotante de iOS 26 (alto de la cápsula, márgenes) son **aproximaciones visuales**: Apple no las publica como cifras fijas. Si las necesitas exactas, tómalas de los kits de diseño de iOS 26 que ofrece Apple.

---

## 1. Qué hay en el diseño

```
┌───────────────────────────────────────┐
│  (contenido que pasa por debajo)      │
│                                       │
│  ╭───────────────────────────────╮    │  ← accesorio: temporizador en marcha
│  │ ⏱ Lentejas estofadas  12:30  ⏸ │    │
│  ╰───────────────────────────────╯    │
│  ╭──────────────────────────╮  ╭───╮  │
│  │ ✦     📖     📅     🛒³  │  │ 🔍 │  │  ← barra de vidrio + pestaña Buscar
│  │Descubrir Recetas Plan Compra│  ╰───╯  │
│  ╰──────────────────────────╯         │
│               ───────                 │  ← indicador de inicio
└───────────────────────────────────────┘
```

| Pestaña | Icono (equivalente en SF Symbols) | Para qué sirve |
|---|---|---|
| **Descubrir** | `sparkles` | Ideas y recetas para hoy (es la pestaña de inicio) |
| **Recetas** | `book` | Recetas guardadas del usuario |
| **Plan** | `calendar` | Menú de la semana |
| **Compra** | `cart` + insignia | Lista de la compra; la insignia cuenta lo que falta por comprar |
| **Buscar** | `magnifyingglass` (rol *search*) | Buscar recetas e ingredientes |

**Qué hace:**
- **Cambiar de pestaña:** cada sección guarda su posición de desplazamiento. Si vuelves a tocar la pestaña activa, la sección sube al inicio.
- **Desplazarse:** la barra **se minimiza** al bajar (solo queda la pestaña activa y la lupa) y vuelve a su tamaño al subir o al tocarla. El temporizador ocupa entonces el hueco entre las dos.
- **Pulsación larga** sobre una pestaña: aparece el **visor de contenido ampliado**, con el icono y la etiqueta en grande.
- **Teclado:** las flechas ← → recorren las pestañas, e Inicio/Fin van a la primera y a la última. Mientras el foco está en la barra, no se minimiza.
- **Lista de la compra:** al marcar artículos, la insignia y el texto que lee VoiceOver («Compra, 3 pendientes») se actualizan solos.

---

## 2. Decisiones de diseño y sus fuentes

### 2.1 La barra solo sirve para moverse entre secciones, nunca para ejecutar acciones
**Decisión:** las cinco pestañas son **secciones de primer nivel**. No he puesto el típico botón central «+ Nueva receta». Crear una receta es una acción, y su sitio es la barra de navegación o una barra de herramientas dentro de *Recetas*.
**Fuente:** HIG, *Tab bars*: la barra de pestañas sirve para navegar entre secciones de la app, y Apple pide no usarla para acciones; para eso está la barra de herramientas (*Toolbars*).
— https://developer.apple.com/design/human-interface-guidelines/tab-bars
— https://developer.apple.com/design/human-interface-guidelines/toolbars

### 2.2 Cuatro secciones más Buscar
**Decisión:** pocas pestañas, y cada una responde a un momento real de cocinar: inspirarse, consultar lo guardado, planificar y comprar. Buscar va aparte, a la derecha, en su propio círculo.
**Fuentes:**
- HIG, *Tab bars*: en iPhone conviene usar pocas pestañas. A partir de cinco, `UITabBarController` agrupa las sobrantes en una pestaña «Más», lo que esconde contenido y añade un paso.
- iOS 26 / WWDC25: la pestaña de búsqueda se declara con `Tab(role: .search)`, y el sistema la dibuja separada del resto, al final de la barra.
  — *Build a SwiftUI app with the new design* (WWDC25): https://developer.apple.com/videos/play/wwdc2025/323/
  — `TabRole.search`: https://developer.apple.com/documentation/swiftui/tabrole

### 2.3 Material Liquid Glass flotante, con el contenido pasando por debajo
**Decisión:** la barra es una **cápsula de vidrio translúcido** (`backdrop-filter: blur() saturate()`), flota sobre el contenido y lo deja ver al desplazarse. Tiene un borde superior iluminado y una sombra suave. Arriba y abajo, un **degradado de borde** (*scroll edge effect*) hace que el texto que pasa por debajo no compita con las etiquetas.
**Fuentes:**
- WWDC25, *Meet Liquid Glass* (https://developer.apple.com/videos/play/wwdc2025/219/) y *Get to know the new design system* (https://developer.apple.com/videos/play/wwdc2025/356/). Liquid Glass se reserva a la capa de navegación y controles, que flota por encima del contenido; no se aplica al contenido en sí.
- HIG, *Materials*: https://developer.apple.com/design/human-interface-guidelines/materials
- Cuidado con mezclar vidrio sobre vidrio. Por eso las tarjetas de receta son opacas y el vidrio solo aparece en la barra, en la lupa y en el accesorio.

> Si tu app tiene que funcionar en iOS 18 o anteriores, cambia la cápsula por la barra clásica: ocupa todo el ancho, mide 49 pt más la zona segura inferior y lleva un fondo de material con una línea separadora arriba. Los tokens del CSS ya están preparados para ese cambio.

### 2.4 Iconos rellenos, etiqueta corta siempre visible
**Decisión:** todos los iconos van **rellenos**, a unos 26 pt, con una **etiqueta de una sola palabra** debajo (10 pt, seminegrita). La pestaña seleccionada se distingue por el **color de acento** y por una píldora de fondo, no por cambiar de icono. Así la selección no depende solo del color.
**Fuentes:**
- HIG, *Tab bars* y *SF Symbols*: en las barras de pestañas de iOS se prefieren los símbolos rellenos, y las etiquetas deben ser cortas y claras. En SwiftUI basta con pasar el nombre base del símbolo, porque el sistema aplica la variante adecuada en la barra.
  — https://developer.apple.com/design/human-interface-guidelines/sf-symbols
- WCAG 2.2, criterio 1.4.1 *Uso del color*: la información no puede transmitirse solo con el color.
  — https://www.w3.org/TR/WCAG22/#use-of-color
- **Licencia:** en la web **no he usado SF Symbols**. Según su licencia, solo pueden usarse en interfaces de apps para plataformas de Apple, así que he dibujado iconos SVG que se les parecen. En la app nativa, usa los símbolos reales.

### 2.5 Color: un acento «tomate» con contraste comprobado
**Decisión:** el acento es un **naranja tomate**, relacionado con la cocina y propio de la marca, en lugar del azul por defecto del sistema. El naranja de sistema (`systemOrange`) **no llega a 4,5:1 sobre blanco**, así que lo he oscurecido.

| Token | Claro | Oscuro | Contraste aproximado |
|---|---|---|---|
| `--accent` (seleccionada) | `#C2410C` | `#FF8A50` | 5,2:1 sobre blanco · más de 7:1 sobre gris oscuro |
| `--tab-inactive` | `#58585E` | `#AEAEB2` | más de 6:1 · más de 8:1 |
| `--badge` | `#D70015` + texto blanco | ídem | unos 5,4:1 |

He oscurecido también el gris de las pestañas inactivas, porque el `systemGray` estándar (#8E8E93) se queda en unos 3,3:1 sobre blanco. El rojo de la insignia es la variante de alto contraste de `systemRed`.
**Fuentes:**
- HIG, *Color*: usa un color de acento propio de forma coherente y comprueba el contraste en los modos claro y oscuro. https://developer.apple.com/design/human-interface-guidelines/color
- WCAG 2.2, 1.4.3 *Contraste (mínimo)* y 1.4.11 *Contraste de elementos no textuales*: https://www.w3.org/TR/WCAG22/#contrast-minimum
- **Ojo:** sobre vidrio, el contraste real depende de lo que pase por debajo. La opacidad del 64 % y el degradado inferior lo mantienen estable, pero conviene revisarlo con fotos de comida muy saturadas.

### 2.6 Insignia solo en *Compra*
**Decisión:** solo una pestaña lleva insignia: el número de artículos pendientes. Es información útil, se puede actuar sobre ella y cambia con el uso. Desaparece cuando la cuenta llega a 0 y no pasa de «99+».
**Fuente:** HIG, *Tab bars*: usa las insignias con moderación, solo para información importante y nueva, para que no pierdan valor. Ver también `UITabBarItem.badgeValue` y el modificador `.badge(_:)` de SwiftUI.

### 2.7 Minimizar al desplazarse y añadir un accesorio inferior
**Decisión:** al bajar por un listado de recetas, que es contenido largo y muy visual, la barra **se encoge** para dejar más espacio a las fotos. El **temporizador de cocina** ocupa la posición de **accesorio inferior**: sigue visible en todas las pestañas porque mientras cocinas lo necesitas tengas abierta la sección que tengas abierta. No lo he hecho pestaña porque no es una sección, sino un estado temporal.
**Fuentes:** iOS 26 / WWDC25, `tabBarMinimizeBehavior(.onScrollDown)` y `tabViewBottomAccessory` en SwiftUI (`bottomAccessory` en UIKit). Minimizar es **opcional**: Apple lo ofrece para apps centradas en contenido.
— *Build a SwiftUI app with the new design*: https://developer.apple.com/videos/play/wwdc2025/323/
— *Build a UIKit app with the new design*: https://developer.apple.com/videos/play/wwdc2025/284/

### 2.8 Cada pestaña conserva su estado; volver a tocarla sube al inicio
**Decisión:** al cambiar de pestaña, cada sección guarda su posición de desplazamiento. Tocar de nuevo la pestaña activa lleva la sección al principio.
**Fuente:** HIG, *Tab bars*: al cambiar de pestaña hay que conservar el estado de navegación de cada una y no reiniciarlo. La subida al inicio al repetir el toque es el comportamiento estándar de `UITabBarController`.

### 2.9 Accesibilidad

| Aspecto | Cómo lo he resuelto | Fuente |
|---|---|---|
| Objetivos táctiles | Cada pestaña mide unos 70 × 54 pt; el círculo de búsqueda, 62 pt; el botón del temporizador, 44 × 44 pt | HIG *Accessibility* (mínimo 44 × 44 pt); WCAG 2.2, 2.5.8 |
| Lectores de pantalla | Patrón de pestañas WAI-ARIA (`tablist` / `tab` / `tabpanel`, `aria-selected`, *roving tabindex*). Así VoiceOver anuncia «pestaña, 1 de 5», igual que en nativo | WAI-ARIA APG *Tabs*: https://www.w3.org/WAI/ARIA/apg/patterns/tabs/ |
| Nombre accesible | «Compra, 3 pendientes» empieza por la etiqueta visible | WCAG 2.2, 2.5.3 *Etiqueta en el nombre* |
| Dynamic Type | El contenido usa `font: -apple-system-body`, así que escala con el tamaño de texto del sistema en Safari. La barra **no escala**, igual que en iOS, y ofrece en su lugar el **visor de contenido ampliado** con pulsación larga | HIG *Typography* y *Accessibility* (*Large Content Viewer*, `UILargeContentViewerInteraction`) |
| Reducir transparencia / Aumentar contraste | El vidrio pasa a fondo opaco y, con más contraste, se añade un borde visible | `prefers-reduced-transparency` y `prefers-contrast` (Media Queries Level 5) |
| Reducir movimiento | Las transiciones se vuelven instantáneas y desaparece el efecto de escala al pulsar | `prefers-reduced-motion`; HIG *Motion* |
| Teclado | Flechas, Inicio y Fin; foco visible con un anillo del color de acento | WAI-ARIA APG *Tabs* |
| Colores forzados | Bordes con `CanvasText` y `Highlight` | CSS Color Adjust, `forced-colors` |

### 2.10 Detalles para la web en iPhone
- `viewport-fit=cover` junto con `env(safe-area-inset-bottom)` para que la barra no choque con el indicador de inicio. Fuente: WebKit, *Designing Websites for iPhone X*, https://webkit.org/blog/7929/designing-websites-for-iphone-x/
- Fuente del sistema mediante `-apple-system, system-ui`, que en dispositivos de Apple carga SF Pro.
- `touch-action: manipulation` elimina el retardo del doble toque, y `-webkit-touch-callout: none` evita que la pulsación larga abra el menú de Safari.
- 1 px CSS ≈ 1 pt en iPhone, así que las medidas en pt de la HIG pasan directamente a px.

---

## 3. Cómo quedaría en la app nativa (SwiftUI, iOS 26)

```swift
TabView {
    Tab("Descubrir", systemImage: "sparkles") { DescubrirView() }
    Tab("Recetas",   systemImage: "book")     { RecetasView() }
    Tab("Plan",      systemImage: "calendar") { PlanView() }
    Tab("Compra",    systemImage: "cart")     { CompraView() }
        .badge(pendientes)
    Tab("Buscar", systemImage: "magnifyingglass", role: .search) { BuscarView() }
}
.tint(Color("Tomate"))                 // acento con variantes clara/oscura
.tabBarMinimizeBehavior(.onScrollDown)
.tabViewBottomAccessory {
    TemporizadorView()                 // solo mientras hay un temporizador activo
}
```

En nativo, el sistema se encarga gratis del vidrio, la minimización, el visor ampliado, VoiceOver y Reducir transparencia. El HTML reproduce ese comportamiento para un prototipo o una web app.

---

## 4. Cosas que conviene validar
1. **Etiquetas con textos largos:** en alemán o en finés, «Descubrir» puede cortarse. Las etiquetas acaban en «…», pero es mejor elegir palabras cortas en cada idioma.
2. **Contraste sobre fotos reales:** pruébalo con imágenes muy rojas o naranjas pasando bajo la barra, porque se parecen al acento.
3. **El accesorio solo cuando hace falta:** si no hay ningún temporizador activo, no lo muestres. Un accesorio vacío ocupa espacio sin aportar nada.
4. **Medidas de iOS 26:** las proporciones de la cápsula son aproximadas. Ajústalas con el kit de diseño oficial de Apple.
