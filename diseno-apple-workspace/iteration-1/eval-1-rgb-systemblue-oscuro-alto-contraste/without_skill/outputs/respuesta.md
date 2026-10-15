# systemBlue en modo oscuro con alto contraste

## Respuesta corta

| Variante | RGB | Hex |
|---|---|---|
| **Oscuro + alto contraste** (iOS 13–18, valor clásico) | **R 64 · G 156 · B 255** | **#409CFF** |

Es el valor que devuelve `UIColor.systemBlue` (o `Color.blue` en SwiftUI) cuando el rasgo de la interfaz es `userInterfaceStyle = .dark` y `accessibilityContrast = .high` (el usuario ha activado *Ajustes > Accesibilidad > Pantalla y tamaño de texto > Aumentar contraste*).

## Contexto: las cuatro variantes de systemBlue

| Variante | RGB | Hex |
|---|---|---|
| Claro (por defecto) | 0, 122, 255 | #007AFF |
| Oscuro | 10, 132, 255 | #0A84FF |
| Claro + alto contraste | 0, 64, 221 | #0040DD |
| **Oscuro + alto contraste** | **64, 156, 255** | **#409CFF** |

En modo oscuro el alto contraste *aclara* el azul (para que destaque más sobre fondos negros), mientras que en modo claro lo *oscurece*.

## De dónde sale el dato

- **Fuente:** Apple **Human Interface Guidelines**, sección *Foundations > Color*, tabla «System colors», que lista para cada color del sistema los valores RGB en *Light*, *Dark*, *Light (increased contrast)* y *Dark (increased contrast)*.
- Estos valores coinciden con lo que se obtiene al resolver el color dinámico en código, por ejemplo:
  ```swift
  let traits = UITraitCollection(traitsFrom: [
      UITraitCollection(userInterfaceStyle: .dark),
      UITraitCollection(accessibilityContrast: .high)
  ])
  let resolved = UIColor.systemBlue.resolvedColor(with: traits)
  ```
- **Origen de esta respuesta:** está escrita de memoria, sin consultar la web en este momento. No he podido comprobar la versión actual de la página.

## Aviso importante: actualización de iOS 26 (2025)

Con el rediseño *Liquid Glass* (iOS 26 / macOS Tahoe 26, junio de 2025), Apple **ajustó la paleta de colores del sistema** en las HIG. Si no me falla la memoria, los valores nuevos de systemBlue son estos:

| Variante (HIG actual, iOS 26+) | RGB | Hex |
|---|---|---|
| Claro | 0, 136, 255 | #0088FF |
| Oscuro | 0, 145, 255 | #0091FF |
| Claro + alto contraste | 30, 110, 244 | #1E6EF4 |
| **Oscuro + alto contraste** | **92, 184, 255** | **#5CB8FF** |

No tengo la misma seguridad con estos valores nuevos que con los clásicos. Antes de usarlos en producción, compruébalos en la página *Color* de las HIG o resolviendo el color en un dispositivo o simulador con iOS 26.

## Recomendación

No escribas el hexadecimal a mano en el código. Usa `UIColor.systemBlue` / `Color.blue` / `NSColor.systemBlue`: el sistema elige la variante correcta según el modo (claro u oscuro), el contraste y la versión del sistema operativo. Recurre a los valores fijos solo en maquetas, diseños (Figma/Sketch) o en plataformas que no son de Apple.
