# Liquid Glass: ¿cuándo usar *clear* en vez de *regular*?

**Respuesta corta:** usa **regular** casi siempre. Reserva **clear** para controles que flotan sobre **contenido multimedia rico** (fotos, vídeo, cámara, mapas a pantalla completa), siempre que puedas añadir una **capa de oscurecimiento** debajo sin estropear ese contenido y que lo que va encima del vidrio sea **lo bastante llamativo y claro** para leerse.

---

## Las dos variantes

| | **Regular** | **Clear** |
|---|---|---|
| Transparencia | Moderada: desenfoca y difumina el fondo | Alta: deja ver casi todo el contenido de detrás |
| Adaptatividad | Se adapta al contenido de fondo (ajusta luminosidad, sombras y puede pasar de aspecto claro a oscuro) para mantener la legibilidad | No se adapta automáticamente: la legibilidad es responsabilidad tuya |
| Legibilidad | Garantizada en casi cualquier contexto | Depende de una capa de atenuación (*dimming*) y de un contenido superpuesto muy contrastado |
| Uso típico | Barras de pestañas, barras de herramientas, barras de navegación, menús, *sheets*, botones, controles en general | Controles sobre fotos/vídeos a pantalla completa, visor de cámara, reproductores multimedia inmersivos |
| Frecuencia | Variante por defecto | Caso especial |

## Cuándo elegir *clear*

Apple plantea tres condiciones; conviene que se cumplan **las tres**:

1. **El elemento está sobre contenido multimedia rico.** Una foto, un vídeo, el visor de la cámara… contenido que el usuario quiere ver "a través" del control y que se beneficia de que la interfaz casi desaparezca.
2. **El contenido de fondo tolera una capa de oscurecimiento.** Clear necesita una capa oscura detrás para que los símbolos y textos se lean. Como referencia, Apple sugiere algo en torno a un **35 % de opacidad** de negro cuando el fondo es brillante. Si oscurecer el contenido lo perjudica (p. ej. edición de color de una foto), clear no es buena opción.
3. **El contenido sobre el vidrio es audaz y luminoso.** Iconos/SF Symbols con peso suficiente, texto blanco o muy claro, pocos elementos. Texto pequeño, fino o denso no funciona sobre clear.

Si falla cualquiera de ellas → **regular**.

## Cuándo quedarse con *regular*

- Interfaz general de la app: navegación, barras, menús, pop-overs, *sheets*, paneles laterales.
- Fondos impredecibles o que cambian (listas con scroll, contenido mixto de texto e imagen).
- Controles con texto, etiquetas o mucha información.
- Cuando necesitas que el sistema gestione automáticamente el contraste, el modo claro/oscuro y las opciones de accesibilidad.

## Reglas complementarias

- **No mezcles variantes** en un mismo grupo de controles o en la misma capa: el resultado se ve inconsistente. Elige una para el conjunto.
- **El vidrio es para la capa de navegación/controles**, no para el contenido. No pongas Liquid Glass sobre Liquid Glass ni lo uses como fondo de celdas o tarjetas de contenido.
- **Tinte con moderación:** el tinte (`.tint`) sirve para destacar la acción principal, no para decorar; funciona en ambas variantes, pero en clear reduce aún más el protagonismo del fondo.
- **Accesibilidad:** con "Reducir transparencia" o "Aumentar contraste" activados, el sistema vuelve el vidrio más opaco/escarchado. Comprueba que tu diseño con clear sigue siendo legible en esos modos y en modo claro y oscuro.
- **Prueba con el peor fondo posible:** una zona blanca y muy brillante de una foto es el caso crítico para clear.

## En código (SwiftUI, iOS 26+)

```swift
// Variante por defecto: regular
Image(systemName: "heart")
    .padding()
    .glassEffect()                 // equivale a .glassEffect(.regular)

// Variante clear sobre una foto a pantalla completa
ZStack {
    Image("foto")
        .resizable()
        .scaledToFill()
        .ignoresSafeArea()

    // Capa de oscurecimiento para garantizar la legibilidad
    Color.black.opacity(0.35)
        .ignoresSafeArea()

    HStack(spacing: 16) {
        Button { } label: { Image(systemName: "square.and.arrow.up") }
        Button { } label: { Image(systemName: "heart.fill") }
    }
    .font(.title2.weight(.semibold))
    .foregroundStyle(.white)
    .padding()
    .glassEffect(.clear.interactive(), in: .capsule)
}
```

En la práctica, la capa oscura suele limitarse a la zona donde están los controles (un degradado en la parte superior o inferior) en vez de cubrir toda la imagen.

Otras piezas útiles: `.regular.tint(.blue)`, `.interactive()` para controles que responden al toque, `GlassEffectContainer` para agrupar varios elementos de vidrio, y los estilos de botón `.buttonStyle(.glass)` / `.buttonStyle(.glassProminent)` (estos usan la variante regular).

## Regla mnemotécnica

> **Regular = interfaz. Clear = interfaz que se aparta para que brille el contenido multimedia.**
> Si dudas, usa regular.
