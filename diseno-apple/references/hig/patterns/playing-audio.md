# Playing audio — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/playing-audio
- Descargado: 2026-10-15
- Sección: patterns
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2023-06-21 — Updated to include guidance for visionOS.

> Resumen de Apple: People expect rich audio experiences that automatically adjust when the context changes on the device.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Devices can play audio in a variety of ways, such as through internal or external speakers, headphones, and wirelessly through devices that use Bluetooth or AirPlay.
- **Silence.**
- **Volume.**
  - «An exception is the ringer volume on iPhone, which people can adjust separately in Settings.»
- **Headphones.**

### Best practices

- **Adjust levels automatically when necessary — don’t adjust the overall volume.**
- **Permit rerouting of audio when possible.**
  - «Support this capability unless there’s a compelling reason not to.»
- **Use the system-provided volume view to let people make audio adjustments.**
- **Choose an audio category that fits the way your app or game uses sound.**

| Category | Meaning | Behavior |
|---|---|---|
| Solo ambient | Sound isn’t essential, but it silences other audio. For example, a game with a soundtrack. | Responds to the silence switch. Doesn’t mix with other sounds. Doesn’t play in the background. |
| Ambient | Sound isn’t essential, and it doesn’t silence other audio. For example, a game that lets people play music from another app during gameplay in place of the game’s soundtrack. | Responds to the silence switch. Mixes with other sounds. Doesn’t play in the background. |
| Playback | Sound is essential and might mix with other audio. For example, an audiobook or educational app that teaches a foreign language, which people might want to listen to after leaving the app. | Doesn’t respond to the silence switch. May or may not mix with other sounds. Can play in the background. |
| Record | Sound is recorded. For example, a note-taking app that offers an audio recording mode. An app of this nature might switch its category to playback if it lets people play the recorded notes. | Doesn’t respond to the silence switch. Doesn’t mix with other sounds. Can record in the background. |
| Play and record | Sound is recorded and played, potentially simultaneously. For example, an audio messaging or video calling app. | Doesn’t respond to the silence switch. May or may not mix with other sounds. Can record and play in the background. |

- **Respond to audio controls only when it makes sense.**
- **Avoid repurposing audio controls.**
- **Consider creating custom audio player controls only if you need to offer commands that the system doesn’t support.**
- **Let other apps know when your app finishes playing temporary audio.**

### Handling interruptions

- Although most apps and games rely on the system’s default interruption behavior, you can customize this behavior to better accommodate your needs.
- **Determine how to respond to audio-session interruptions.**
  - «For example, if your app supports recording or other audio-related tasks that people don’t want interrupted, you can tell the system to avoid interrupting the currently playing audio for an incoming call unless people choose to accept it.»
- **When an interruption ends, determine whether to resume audio playback automatically.**

### Platform considerations

#### iOS, iPadOS

- **Use the system’s sound services to play short sounds and vibrations.**

#### macOS

- In macOS, notification sounds mix with other audio by default.

#### tvOS

- In tvOS, the system plays audio only when people initiate it, through interactions within apps and games or when performing device calibrations.

#### visionOS

- Subtle, expressive sounds are everywhere in visionOS, enhancing experiences and providing essential feedback when people look at a virtual object and use gestures to interact…
> **Important:** In visionOS, as in every platform, avoid communicating important information using only sound.
- In visionOS, audio playback from the Now Playing app pauses automatically when people close the app’s window, and audio from an app that isn’t the Now Playing app can duck when…
- **Prefer playing sound.**
- **Design custom sounds for custom UI elements.**
- **Use Spatial Audio to create an intuitive, engaging experience.**
- **Consider defining a range of places from which your app sounds can originate.**
- **Consider varying sounds that people could perceive as repetitive over time.**
- **Decide whether you need to play sound that’s fixed to the wearer or tracked by the wearer.**

#### watchOS

- In watchOS, the system manages audio playback.
- **Use the recommended encoding values for media assets.**
- **Consider**

## Recursos relacionados

- *Related:*
  - [Playing video](https://developer.apple.com/design/human-interface-guidelines/playing-video)
  - [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback)
- *Developer documentation:*
  - [Configuring your app for media playback](https://developer.apple.com/documentation/avfoundation/configuring-your-app-for-media-playback) — AVFoundation
  - [AVAudioSession](https://developer.apple.com/documentation/avfaudio/avaudiosession) — AVFAudio
  - [MusicKit](https://developer.apple.com/documentation/musickit) — MusicKit

## Vídeos que la explican

- [Integrate MusicKit into your app](https://developer.apple.com/videos/play/wwdc2026/254) → `references/videos/2026-254.md`
- [Explore immersive sound design](https://developer.apple.com/videos/play/wwdc2023/10271) → `references/videos/2023-10271.md`
- [Immerse your app in Spatial Audio](https://developer.apple.com/videos/play/wwdc2021/10265) → `references/videos/2021-10265.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 21, 2023 | Updated to include guidance for visionOS. |
