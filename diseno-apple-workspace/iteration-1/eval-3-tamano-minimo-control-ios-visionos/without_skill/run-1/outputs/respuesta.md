# Tamaño mínimo de un control en iOS y visionOS

## Resumen rápido

| Plataforma | Tamaño recomendado (por defecto) | Mínimo absoluto | Método de entrada |
|---|---|---|---|
| **iOS / iPadOS** | **44 × 44 pt** | 28 × 28 pt | Dedo (toque) |
| **visionOS** | **60 × 60 pt** (área interactiva) | 28 × 28 pt | Mirada + pellizco (o toque directo) |

> Las cifras están en **puntos (pt)**, no en píxeles. El sistema las escala según la densidad de pantalla (@2x, @3x) o, en visionOS, según la distancia y el tamaño angular.

---

## iOS (y iPadOS)

- **Objetivo táctil de 44 × 44 pt.** Es la cifra clásica de las Human Interface Guidelines de Apple: cualquier elemento que se pueda tocar (botones, iconos de la barra de navegación, celdas, interruptores…) debe tener al menos esa área de impacto.
- **28 × 28 pt** es el límite inferior que Apple contempla para casos muy densos, pero por debajo de 44 pt la precisión cae y aumentan los errores de toque, sobre todo para personas con dificultades motoras.
- **Lo que cuenta es el área de impacto, no el dibujo.** Un icono puede medir 20–24 pt visualmente siempre que su zona tocable llegue a 44 × 44 pt (mediante *padding*, `contentShape` o ampliando el `frame`).
- **Separación:** deja espacio suficiente entre controles adyacentes (del orden de 8 pt o más) para que las áreas no se solapen.

```swift
// SwiftUI: icono pequeño con área táctil de 44 pt
Button(action: share) {
    Image(systemName: "square.and.arrow.up")
        .frame(width: 44, height: 44)
        .contentShape(Rectangle())
}
```

---

## visionOS

- **Área interactiva de 60 × 60 pt.** En visionOS la selección se hace principalmente con la **mirada** (y se confirma con un pellizco), y el seguimiento ocular es menos preciso que un dedo. Por eso Apple pide un objetivo mayor que en iOS.
- **El elemento visible puede ser más pequeño.** Un botón puede medir, por ejemplo, 44 pt de forma visual, siempre que tenga el *padding* necesario para que su región de impacto llegue a 60 pt.
- **Separación entre controles:** procura que los centros de los elementos interactivos estén separados al menos **60 pt**, para que la mirada no salte de uno a otro de forma accidental.
- **Tamaño angular:** los puntos de visionOS se escalan con la distancia de la ventana, de modo que el tamaño percibido se mantiene; 60 pt equivale aproximadamente a un ángulo visual cómodo para la mirada. Si colocas contenido en un espacio inmersivo con tamaños en metros, mantén un tamaño angular equivalente.
- **Efecto *hover*:** usa los controles del sistema o `.hoverEffect()` para que el usuario reciba feedback al mirar el control; refuerza la sensación de objetivo claro.
- **28 × 28 pt** es el mínimo absoluto (por ejemplo, controles muy compactos dentro de un grupo), pero debe ser la excepción.

```swift
// SwiftUI en visionOS: control visual de 44 pt con área de 60 pt
Button(action: play) {
    Image(systemName: "play.fill")
        .frame(width: 44, height: 44)
}
.padding(8)                     // 44 + 8 + 8 = 60 pt
.contentShape(.hoverEffect, Circle())
.hoverEffect()
```

---

## Claves para recordar

1. **iOS → 44 × 44 pt. visionOS → 60 × 60 pt.**
2. Se mide el **área interactiva**, no solo el gráfico.
3. Usa los controles estándar del sistema siempre que puedas: ya cumplen estos tamaños.
4. Respeta el **Dynamic Type** y las opciones de accesibilidad: los objetivos no deberían encogerse cuando el texto crece.
5. Prueba en dispositivo real (y en visionOS, con la mirada) para comprobar que los controles se pueden seleccionar con comodidad.

*Respuesta basada en mi conocimiento de las Human Interface Guidelines de Apple (sin consultar fuentes en línea); conviene comprobarla con la versión vigente de las HIG.*
