# Icono de app: lienzo en watchOS y apariencias en iOS

## 1. Tamaño del lienzo del icono en watchOS

- **Lienzo: 1088 × 1088 px** (cuadrado).
- El sistema le aplica una **máscara circular**: tú entregas un cuadrado sin redondear y watchOS lo recorta en círculo. No dibujes el círculo tú mismo ni añadas sombras o bordes exteriores.
- Para comparar: en iOS, iPadOS y macOS el lienzo es de **1024 × 1024 px**. En esas plataformas el sistema aplica la forma de esquinas redondeadas (squircle). watchOS usa un lienzo algo mayor porque la máscara es circular.
- Recomendaciones prácticas:
  - Centra el motivo principal y deja margen: las esquinas del cuadrado desaparecen con el recorte circular.
  - Usa formas simples y reconocibles, porque en la muñeca el icono se ve muy pequeño.
  - Si diseñas con **Icon Composer** (el flujo actual con capas y Liquid Glass), usa el lienzo de watchOS. El sistema genera los tamaños concretos que hacen falta.

## 2. Apariencias que admite un icono en iOS

Desde el rediseño de Liquid Glass (iOS 26), un icono de iOS puede mostrarse con estas apariencias. El usuario las elige en *Ajustes › Pantalla de inicio* (personalizar):

| Apariencia | Descripción |
|---|---|
| **Predeterminada (clara / Default)** | El icono a todo color, tal como lo diseñas. |
| **Oscura (Dark)** | Variante para fondos oscuros. Normalmente el fondo pasa a ser oscuro y el motivo conserva su color o se aclara. |
| **Transparente (Clear)** | Efecto de vidrio translúcido. Tiene variante **clara** y **oscura**. |
| **Tintada (Tinted)** | El sistema tiñe el icono en monocromo con el color que elige el usuario. Tiene variante **clara** y **oscura**. |

En total: **predeterminada, oscura, transparente (clara/oscura) y tintada (clara/oscura)**.

### Cómo prepararlo
- Diseña el icono **por capas** (fondo + 1 a 4 grupos de primer plano) en **Icon Composer** (o en Figma, Sketch, Illustrator o Photoshop con las plantillas de Apple) y expórtalo como archivo `.icon` para Xcode.
- Desde ese único archivo puedes ajustar cada apariencia: colores de fondo para la variante oscura, opacidad, qué capas se tiñen o se vuelven translúcidas, sombras y reflejos de Liquid Glass, etc.
- Si no defines una variante, el sistema genera la oscura, la transparente y la tintada automáticamente a partir de la predeterminada. Aun así, conviene revisarlas y ajustarlas.
- En la variante tintada el color desaparece. Comprueba que la forma se reconozca solo por su silueta y contraste.

> **Nota sobre iOS 27:** este conjunto de apariencias es el que introdujo iOS 26 junto con Liquid Glass. Que yo sepa, iOS 27 no añade ni quita ninguna. Esta respuesta sale de mi propio conocimiento, sin consultar la documentación actual. Antes de cerrar los recursos, revisa la sección *App icons* de las Human Interface Guidelines de Apple, por si hubiera cambios de última hora.
