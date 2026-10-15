# Siri — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/siri
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2026-06-08 — Revised for Siri AI.

> Resumen de Apple: People use Siri to help them with the things they need to find, know, or do every day.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Siri is a personal assistant that helps people get information and perform quick actions throughout the system and the apps they use.
- On supported devices, Siri AI introduces a version of Siri powered by Apple Intelligence.
- For example, someone can say “Send a message to Marisa in *AppName*” from anywhere in the system, and Siri can help them complete that task in a contextually appropriate way.

### Getting your app to work with Siri

- By default, the system doesn’t have specific awareness of what an app can do or the information it contains.
- When an app implements intents, the system can expose the things the app can do (the app’s actions, or *intents*) and its content (the app’s *entities*) in system experiences…
- To get the most out of Siri, an app can additionally associate its features and content with app…

#### Sharing contextual information

- In addition to exposing actions and content with schemas, an app can offer a more personalized experience by giving the system contextual information about its content and…
- An app can tell the system what’s onscreen by annotating its views and other content with app entities.
- To provide content information to the system, an app can donate entities to the on-device Spotlight index, which makes the app’s information available to someone searching in…
- An app can also tell the system about actions a person takes while using it by donating the actions as intents.

### Best practices

- **Identify your app’s most popular actions, and when and where they occur.**
- **Use familiar terms for your content and actions.**
- **Offer relevant content.**
- **Don’t advertise.**
- **Only provide a custom response if built-in responses don’t meet your app’s needs.**

### Customizing your app’s experience with Siri

- For apps with many common feature sets, existing [app schema domains](https://developer.apple.com/documentation/appintents/app-schema-domains) provide the built-in functionality…
- To customize the experience of an action or a piece of content associated with an existing schema, an app can define additional optional properties as part of an intent or entity…
> **Note:** Siri is powered by Apple Intelligence to provide contextually relevant responses.
- When you provide additional custom properties as part of your schema responses, consider the following guidelines.
- **Write response dialogue that’s clear and descriptive.**
- **Keep responses as succinct as possible.**
- **Provide responses that Siri can deliver audibly and visually.**
- **Design inclusive interactions.**
- **Ask an open-ended question when the full list of options is too long.**
- **Keep responses device-independent whenever possible.**
- **Omit your app name from responses.**
- **Use appropriate language and respect parental controls.**
- **Help people understand errors and failures.**

### Editorial guidelines

- **Refer to Siri by name.**
- **Be aware that the system reserves important actions and phrases for Siri.**
- **In a localized context, translate only the word *Hey* in the phrase “Hey Siri.”**

| Locale code | “Hey Siri” translation | Locale code | “Hey Siri” translation |
|---|---|---|---|
| ar_AE | يا Siri | fr_CA | Dis Siri |
| ar_SA | يا Siri | fr_CH | Dis Siri |
| da_DK | Hej Siri | fr_FR | Dis Siri |
| de_AT | Hey Siri | it_CH | Ehi Siri |
| de_CH | Hey Siri | it_IT | Ehi Siri |
| de_DE | Hey Siri | ja_JP | Hey Siri |
| en_AU | Hey Siri | ko_KR | Siri야 |
| en_CA | Hey Siri | ms_MY | Hai Siri |
| en_GB | Hey Siri | nb_NO | Hei Siri |
| en_IE | Hey Siri | nl_BE | Hé, Siri |
| en_IN | Hey Siri | nl_NL | Hé Siri |
| en_NZ | Hey Siri | no_NO | Hei Siri |
| en_SG | Hey Siri | pt_BR | E aí Siri |
| en_US | Hey Siri | ru_RU | привет Siri |
| en_ZA | Hey Siri | sv_SE | Hej Siri |
| es_CL | Oye Siri | th_TH | หวัดดี Siri |
| es_ES | Oye Siri | tr_TR | Hey Siri |
| es_MX | Oye Siri | zh_CN | 嘿Siri |
| es_US | Oye Siri | zh_HK | 喂 Siri |
| fi_FI | Hei Siri | zh_TW | 嘿 Siri |
| fr_BE | Dis Siri |  |  |

## Recursos relacionados

- *Related:*
  - [App Shortcuts](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts)
  - [Snippets](https://developer.apple.com/design/human-interface-guidelines/snippets)
- *Developer documentation:*
  - [App Intents](https://developer.apple.com/documentation/appintents)
  - [App schema domains](https://developer.apple.com/documentation/appintents/app-schema-domains)
  - [Apple Intelligence and Siri AI](https://developer.apple.com/documentation/appintents/apple-intelligence-and-siri-ai)

## Vídeos que la explican

- [Build intelligent Siri experiences with App Schemas](https://developer.apple.com/videos/play/wwdc2026/240) → `references/videos/2026-240.md`
- [Discover new capabilities in the App Intents framework](https://developer.apple.com/videos/play/wwdc2026/345) → `references/videos/2026-345.md`
- [Explore advanced App Intents features for Siri and Apple Intelligence](https://developer.apple.com/videos/play/wwdc2026/343) → `references/videos/2026-343.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 8, 2026 | Revised for Siri AI. |
| June 5, 2023 | Removed Add to Siri guidance. Added references to the new [App Shortcuts](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts) page. |
| May 2, 2023 | Consolidated guidance into one page. |
