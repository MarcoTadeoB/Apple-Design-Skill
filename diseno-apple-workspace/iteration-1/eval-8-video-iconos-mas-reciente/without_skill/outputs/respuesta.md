# Iconos de app según Apple: resumen del vídeo más reciente que conozco

## Antes de nada: lo que no he podido comprobar

- **No he podido confirmar cuál es el vídeo más reciente.** Hoy es 15 de octubre de 2026 y no tengo acceso a internet. Puede haber sesiones más nuevas (por ejemplo, de la WWDC26) que no conozco.
- **No tengo las marcas de tiempo exactas.** No tengo la transcripción ni el capítulo del vídeo delante, y no quiero inventarme minutos. Abajo indico en qué **parte aproximada** del vídeo sale cada tema. Para el minuto exacto, mira los capítulos de la página del vídeo en developer.apple.com/videos o en la app Apple Developer.

## Vídeo de referencia

**«Say hello to the new look of app icons»**, WWDC25 (junio de 2025). Va acompañado de **«Create icons with Icon Composer»**, también de la WWDC25.

Son las sesiones más recientes sobre iconos de app que conozco. Coinciden con el nuevo lenguaje visual **Liquid Glass** de iOS 26, iPadOS 26, macOS Tahoe 26, watchOS 26 y visionOS 26.

## Resumen por secciones (marcas de tiempo aproximadas)

| Parte del vídeo (aprox.) | Tema | Qué dice Apple |
|---|---|---|
| Inicio (~0:00) | Introducción | Los iconos se rediseñan con Liquid Glass. Pasan a ser objetos de varias capas que reaccionan a la luz, al movimiento y al aspecto que elige el usuario. |
| Primer tercio | Nuevo lenguaje visual | Los iconos se construyen con **capas** sobre un fondo, a las que el sistema aplica **reflejos especulares, refracción, desenfoque, sombras y translucidez**. El material es dinámico, no se queda fijo en la imagen. |
| Primer tercio | Aspectos (*appearances*) | Cada icono tiene varias variantes: **Default** (claro), **Dark** (oscuro), **Clear** (transparente, claro u oscuro) y **Tinted** (teñido con un color, claro u oscuro). El sistema genera muchas de ellas, pero el diseñador puede ajustarlas. |
| Parte central | Cómo diseñar el icono | Formas simplificadas, más planas y frontales. Hay que evitar sombras, degradados o efectos de vidrio pintados a mano, porque los añade el sistema. Las capas se separan en primer plano y fondo para que se vea la profundidad. Mejor siluetas claras y reconocibles con pocas capas. |
| Parte central | Geometría y retícula | Hay una **retícula y una forma redondeada unificadas para todas las plataformas**: iPhone, iPad y Mac comparten la forma de icono, y watchOS sigue siendo circular. En macOS se acaban los iconos con siluetas libres que salen del contorno. Si un icono no se adapta, el sistema lo mete dentro de la forma estándar. |
| Parte central y final | Color y legibilidad | Hay que comprobar que el icono funciona en todos los aspectos. En las variantes Tinted y Clear el sistema trabaja sobre todo con la luminancia, así que el contraste entre capas es clave. |
| Final | Herramientas: Icon Composer | **Icon Composer** es la nueva app de Apple. En ella se importan las capas, por ejemplo exportadas como SVG desde Figma, Sketch, Illustrator u otras herramientas. Permite ajustar las propiedades de Liquid Glass por capa (desenfoque, translucidez, sombra, especular), previsualizar todas las plataformas y aspectos, y exportar un único archivo `.icon` que se añade a Xcode. |
| Cierre | Recomendaciones | Hay que empezar a rediseñar los iconos ya, usar las plantillas actualizadas de Apple Design Resources y revisar el icono en contexto (pantalla de inicio, Dock, Ajustes, notificaciones). |

## Ideas clave

1. **El icono es un objeto de varias capas, no una imagen plana.** El sistema aplica el material Liquid Glass.
2. **El diseño es más sencillo.** No hay que pintar efectos de luz, sombra ni vidrio a mano.
3. **Hay un icono para todas las plataformas,** con una forma y una retícula unificadas, y variantes Default, Dark, Clear y Tinted.
4. **Icon Composer** es la herramienta recomendada para montar, previsualizar y exportar el icono en formato `.icon` para Xcode.

## Cómo conseguir las marcas de tiempo exactas

1. Abre la sesión en la app **Apple Developer** o en `developer.apple.com/videos/play/wwdc2025/` y busca «app icons».
2. Usa la pestaña de **capítulos** (*Chapters*) o la **transcripción**. Al pulsar una frase, el vídeo salta a ese minuto.
3. Busca también sesiones posteriores, por ejemplo de la WWDC26, por si hay un vídeo más nuevo sobre iconos.
