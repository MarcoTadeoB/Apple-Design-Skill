# Diseño de Apple: de la versión 26 a la 27

> **Una advertencia antes de empezar.** Respondo solo con lo que ya sé, sin consultar la web. Conozco bien la generación 26, que se presentó en la WWDC de junio de 2025. De la generación 27 (WWDC de junio de 2026) **no tengo un registro detallado y fiable** de lo que se anunció, así que lo separo en tres niveles: **confirmado**, **anunciado por Apple de antemano** y **esperado o rumoreado**. Antes de tomar decisiones de diseño, compruébalo en las Human Interface Guidelines (HIG) actuales y en las sesiones de la WWDC26.

---

## 1. Punto de partida: qué trajo la versión 26

Con la versión 26, Apple unificó la numeración de todos sus sistemas (iOS 26, iPadOS 26, macOS Tahoe 26, watchOS 26, tvOS 26 y visionOS 26) y presentó el mayor rediseño desde iOS 7.

- **Liquid Glass.** Es un material translúcido y dinámico que refleja y refracta el contenido que tiene detrás y reacciona al movimiento y a la luz. Está inspirado en visionOS.
- **Jerarquía "contenido primero".** Los controles y la navegación (barras de pestañas, barras de herramientas, barras laterales) flotan sobre el contenido como una capa de cristal.
- **Barras de pestañas que se minimizan** al hacer scroll y un botón de búsqueda separado de la barra.
- **Formas concéntricas.** Las esquinas de los controles siguen la curvatura del hardware, y los botones y menús se vuelven más redondeados (cápsulas).
- **Iconos por capas.** Los iconos tienen modos claro, oscuro, tintado y transparente ("clear"), y se diseñan en la nueva app **Icon Composer**.
- **Pantalla de bloqueo.** La hora es adaptable y se coloca detrás del sujeto de la foto, con fondos espaciales en 3D.
- **macOS Tahoe.** La barra de menús es totalmente transparente, las carpetas y el Dock se pueden personalizar más y las barras laterales flotan.
- **Para desarrolladores.** En SwiftUI, UIKit y AppKit, las apps adoptan el material casi automáticamente al recompilar con Xcode 26. Hay API nuevas como `glassEffect` y `GlassEffectContainer`, y Apple ofrecía una clave temporal para no adoptar el nuevo diseño (`UIDesignRequiresCompatibility`).

### Ajustes durante el ciclo 26 (26.1 y 26.2)

Las críticas por legibilidad y contraste llevaron a Apple a corregir parte del diseño ya dentro del propio ciclo 26:

- En **iOS 26.1**, Ajustes > Pantalla y brillo añadió la opción **Liquid Glass "Transparente" o "Tintado"**. "Tintado" hace el cristal más opaco y con más contraste.
- En **iOS 26.2** llegó un control para ajustar la opacidad del cristal del reloj en la pantalla de bloqueo, junto con otros retoques de contraste.
- Además, se mantuvieron y reforzaron las opciones de accesibilidad "Reducir transparencia" y "Aumentar contraste".

Estos ajustes ya marcaban la dirección que tomaría la versión 27: **menos transparencia por defecto y más control para el usuario**.

---

## 2. Qué cambia en la versión 27

### 2.1 Confirmado o anunciado por Apple con antelación

- **Fin de la opción para no adoptar Liquid Glass.** Apple dijo en su documentación que la clave `UIDesignRequiresCompatibility` (y su equivalente en macOS) era temporal y que pensaba **retirarla en la siguiente versión mayor**. En la práctica, las apps que se compilan con el SDK 27 (Xcode 27) **tienen que adoptar Liquid Glass**. Este es el cambio con más impacto para quien diseña o desarrolla apps.
- **macOS 27 sin Mac con Intel.** Apple anunció que macOS Tahoe 26 sería la última versión compatible con Intel. No es un cambio visual, pero sí significa que el diseño de macOS 27 se piensa solo para Apple silicon.
- **Cambio en el liderazgo de diseño.** A finales de 2025, Alan Dye, responsable de diseño de interfaces y principal impulsor de Liquid Glass, dejó Apple para irse a Meta, y **Stephen Lemay** asumió el diseño de interfaces. La versión 27 es la primera generación que se cierra bajo la nueva dirección. Esto encaja con el giro hacia el refinamiento en lugar de nuevos golpes de efecto.

### 2.2 Lo que se esperaba (rumores previos a la WWDC26, sin verificar)

- **Una versión "estilo Snow Leopard".** Se esperaba un ciclo centrado en **calidad, rendimiento y estabilidad**, no en un nuevo rediseño. Liquid Glass sigue siendo la base visual: la 27 **lo pule, no lo sustituye**.
- **Liquid Glass más maduro.** Se esperaban mejor legibilidad y contraste por defecto, un cristal algo más opaco en las zonas con texto, animaciones más fluidas y menos fallos visuales. También se daba por hecha la consolidación de los controles de transparencia aparecidos en 26.1 y 26.2.
- **Una Siri renovada.** Se esperaba una Siri más conversacional y con una presencia visual nueva, apoyada en los nuevos modelos de Apple Intelligence. Afectaría a cómo se presentan visualmente las respuestas y la interacción por voz.
- **Diseño para el iPhone plegable.** Si el plegable llega en otoño de 2026, iOS 27 necesitaría patrones adaptables entre la pantalla externa y la interna, más cercanos a iPadOS: multitarea, barras laterales y continuidad al desplegar. Esto refuerza la importancia de los layouts adaptables y de las size classes.
- **Coherencia entre plataformas.** Se esperaba seguir alineando iPadOS y macOS (ventanas, barra de menús en iPad, barras laterales) sobre el mismo lenguaje de cristal.

---

## 3. Resumen comparativo

| Aspecto | Versión 26 | Versión 27 |
|---|---|---|
| Lenguaje visual | Estreno de Liquid Glass | Liquid Glass refinado, sin rediseño nuevo (esperado) |
| Transparencia | Muy alta al principio; opciones "Tintado" y de opacidad añadidas en 26.1 y 26.2 | Más legibilidad y contraste por defecto (esperado) |
| Adopción en apps | Opcional y temporal (`UIDesignRequiresCompatibility`) | Obligatoria al compilar con el SDK 27 (anunciado) |
| Iconos | Nuevo sistema por capas con Icon Composer | Continuidad; los iconos por capas pasan a ser la norma |
| macOS | Tahoe: menú transparente, compatible con Intel | Solo Apple silicon (anunciado) |
| Enfoque del ciclo | Rediseño | Calidad, rendimiento e IA (esperado) |
| Liderazgo de diseño | Alan Dye | Stephen Lemay |

---

## 4. Recomendaciones prácticas si diseñas apps

1. **Da por hecho que Liquid Glass es obligatorio.** Si tu app seguía usando la clave de compatibilidad, planifica la migración ya.
2. **Usa los componentes del sistema** (barras de pestañas, barras de herramientas, hojas y menús de SwiftUI y UIKit) en lugar de imitar el cristal con desenfoques propios. Así heredas gratis las mejoras de cada versión.
3. **No coloques texto crítico sobre cristal** encima de contenido con mucho ruido visual. Prueba la app con "Tintado", "Reducir transparencia" y "Aumentar contraste".
4. **Diseña layouts adaptables** pensando en tamaños de pantalla intermedios, como el posible plegable.
5. **Actualiza los iconos** con Icon Composer y cubre los modos claro, oscuro, tintado y transparente.
6. **Comprueba los detalles concretos de la 27** en las HIG, en las notas de la versión de Xcode 27 y en las sesiones "What's new in design" y "What's new in SwiftUI/UIKit" de la WWDC26. Lo que aquí aparece como esperado puede no coincidir con lo que Apple lanzó finalmente.
