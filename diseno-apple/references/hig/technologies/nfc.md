# NFC — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/nfc
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados
- Última actualización: sin registro de cambios

> Resumen de Apple: Near-field communication (NFC) allows devices within a few centimeters of each other to exchange information wirelessly.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- iOS apps running on supported devices can use NFC scanning to read data from electronic tags attached to real-world objects.

### In-app tag reading

- An app can support single- or multiple-object scanning when the app is active, and display a scanning sheet whenever people are about to scan something.
- **Don’t encourage people to make contact with physical objects.**
- **Use approachable terminology.**

| Use | Don’t use |
|---|---|
| Scan the [*object name*]. | Scan the NFC tag. |
| Hold your iPhone near the [*object name*] to learn more about it. | To use NFC scanning, tap your phone to the [*object*]. |

- **Provide succinct instructional text for the scanning sheet.**

| First scan | Subsequent scans |
|---|---|
| Hold your iPhone near the [*object name*] to learn more about it. | Now hold your iPhone near another [*object name*]. |

### Background tag reading

- Background tag reading lets people scan tags quickly any time, without needing to first open your app and initiate scanning.
- **Support both background and in-app tag reading.**

### Platform considerations

- *No additional considerations for iOS or iPadOS.

## Recursos relacionados

- *Developer documentation:*
  - [Core NFC](https://developer.apple.com/documentation/corenfc)
