# ShazamKit — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/shazamkit
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: sin registro de cambios

> Resumen de Apple: ShazamKit supports audio recognition by matching an audio sample against the ShazamKit catalog or a custom audio catalog.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- You can use ShazamKit to provide features like:
  - Enhancing experiences with graphics that correspond with the genre of currently playing music
  - Making media content accessible to people with hearing disabilities by providing closed captions or sign language that syncs with the audio
  - Synchronizing in-app experiences with virtual content in contexts like online learning and retail
- If you need the device microphone to get audio samples for your app to recognize, you must request access to it.

### Best practices

- After you receive permission to access the microphone for features that use ShazamKit, follow these guidelines.
- **Stop recording as soon as possible.**
- **Let people opt in to storing your app’s recognized songs to their iCloud library.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Recursos relacionados

- *Developer documentation:*
  - [ShazamKit](https://developer.apple.com/documentation/shazamkit)

## Vídeos que la explican

- [Explore ShazamKit](https://developer.apple.com/videos/play/wwdc2021/10044) → `references/videos/2021-10044.md`
