# Contraste mínimo para 15 pt normal y 20 pt negrita

## Respuesta corta

| Texto | ¿Cuenta como "texto grande"? | Mínimo (WCAG AA / Apple HIG) | Recomendado (WCAG AAA) |
|---|---|---|---|
| **15 pt, peso normal** | No | **4.5:1** | 7:1 |
| **20 pt, negrita** | Sí | **3:1** | 4.5:1 |

## Por qué

**Criterio de WCAG 2.x (1.4.3 Contraste mínimo, nivel AA):**
- Texto normal: **4.5:1**.
- Texto grande: **3:1**. Se considera "grande" el texto de **al menos 18 pt normal** o **al menos 14 pt en negrita**.

Con eso:
- **15 pt normal**: no llega a 18 pt y no es negrita, así que es texto normal y necesita **4.5:1**.
- **20 pt negrita**: supera los 14 pt en negrita (e incluso los 18 pt), así que es texto grande y basta con **3:1**.

**Apple Human Interface Guidelines (Accesibilidad → Color y contraste)** usa la misma lógica:
- Hasta 17 pt, cualquier peso: **4.5:1**.
- 18 pt o más, cualquier peso: **3:1**.
- Cualquier tamaño en negrita: **3:1**.

Resultado: 15 pt Regular → 4.5:1, y 20 pt Bold → 3:1. Las dos fuentes coinciden.

**Nivel AAA (1.4.6 Contraste mejorado):** si quieres el nivel más exigente, sube a **7:1** para los 15 pt normales y a **4.5:1** para los 20 pt en negrita.

## Matices prácticos

- **Puntos frente a píxeles en la web:** los "pt" de WCAG son puntos CSS (1 pt = 1,333 px). 18 pt ≈ **24 px** y 14 pt ≈ **18,66 px**. Así que 15 pt ≈ 20 px normal (texto normal) y 20 pt ≈ 26,7 px negrita (texto grande).
- **Puntos en iOS/macOS:** en las plataformas de Apple el tamaño se expresa en puntos de interfaz. 15 pt corresponde al estilo *Subheadline* de iOS y 20 pt es cercano a *Title 3*. Con **Dynamic Type** el tamaño real puede bajar si el usuario elige un tamaño menor, así que no confíes en el umbral de "grande" justo en el límite.
- **"Negrita" significa realmente negrita:** pesos *Semibold* o *Medium* no siempre cuentan. Para quedarte del lado seguro, aplica 3:1 solo con *Bold* o más.
- **Los mínimos son mínimos:** 3:1 en texto grande se lee bien en condiciones normales, pero con sol directo o pantallas con brillo bajo conviene apuntar más alto (por ejemplo, 4.5:1 también para el texto grande).
- **Modo oscuro y "Aumentar contraste":** comprueba el ratio en modo claro y oscuro, y considera ofrecer colores con más contraste cuando el usuario active *Aumentar contraste* en Ajustes de accesibilidad.
- **Cómo medirlo:** usa la herramienta *Accessibility Inspector* de Xcode (auditoría de contraste), *Color Contrast Analyser* o cualquier calculadora de ratio WCAG.

## Resumen

- **15 pt normal → mínimo 4.5:1** (ideal 7:1).
- **20 pt negrita → mínimo 3:1** (ideal 4.5:1).
