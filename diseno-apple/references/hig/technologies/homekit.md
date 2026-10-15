# HomeKit — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/homekit
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2023-05-02 — Consolidated guidance into one page.

> Resumen de Apple: HomeKit lets people securely control connected accessories in their homes using Siri or the Home app on iPhone, iPad, Apple Watch, and Mac.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- In iOS, the Home app also lets people manage and configure accessories.
- Your iOS, tvOS, or watchOS app can integrate with HomeKit (and by extension the Home app) to provide a custom or accessory-specific experience.
  - Help people set up, name, and organize their accessories
  - Allow fine-grained accessory configuration and control
  - Provide access to custom accessory features
  - Show people how to create powerful, hands-free automations
  - Provide support
- For developer guidance, see [HomeKit](https://developer.apple.com/documentation/homekit).

### Terminology and layout

- HomeKit models the home as a hierarchy of objects and defines a vocabulary of terms that refer to them.
- It’s crucial for your app to use the terminology and object model that HomeKit defines, so that you can reinforce people’s understanding and make home automation feel approachable.
- In the HomeKit model, the [home](#Homes) object is the root of a hierarchy that contains all other objects, such as [rooms](#Rooms),…
- **Acknowledge the hierarchical model that HomeKit uses.**
- **Make it easy for people to find an accessory’s related HomeKit details.**
- **Recognize that people can have more than one home.**
- **Don’t present duplicate home settings.**

#### Homes

- HomeKit uses the term *home* to represent a physical home, office, or other location of relevance to people.

#### Rooms

- A *room* represents a physical room in a home.

#### Accessories, services, and characteristics

- The term *accessory* represents a physical, connected home accessory, like a ceiling fan, lamp, lock, or camera.
- A controllable feature of an accessory, such as the switch on a connected light, is known as a *service*.
- A *characteristic* is a controllable attribute of a service.
- A *service group* represents a group of accessory services that someone might want to control as a unit.

#### Actions and scenes

- The term *action* refers to the changing of a service’s characteristic, such as adjusting the speed of a fan or the brightness of a light.
- A *scene* is a group of actions that control one or more services in one or more accessories.
> **Tip:** The HomeKit API uses the term *action set* instead of *scene*.

#### Automations

- *Automations* cause accessories to react to certain situations, such as when a person’s location changes, a particular time of day occurs, another accessory turns on or off, or a…

#### Zones

- A *zone* represents an area in the home that contains multiple rooms, such as *upstairs* or *downstairs*.

### Setup

- **Use the system-provided setup flow to give people a familiar experience.**
- **Provide context to explain why you need access to people’s Home data.**
- **Don’t require people to create an account or supply personal information.**
- **Honor people’s setup choices.**
- **Carefully consider how and when to provide a custom accessory setup experience.**

#### Help people choose useful names

- **Suggest service names that suit your accessory.**
- **Check that the names people provide follow HomeKit naming rules.**
  - Use only alphanumeric, space, and apostrophe characters.
  - Start and end with an alphabetic or numeric character.
  - Don’t include emojis.

|  | Example service names |
|---|---|
| ✅ (correcto) | Reading lamp |
| ❌ (incorrecto) | 📚 lamp |
| ✅ (correcto) | 2nd garage door |
| ❌ (incorrecto) | #2 garage door |

- **Help people avoid creating names that include location information.**

### Siri interactions

- HomeKit supports powerful, hands-free control using voice commands.
- **Present example voice commands to demonstrate using Siri to control accessories during setup.**
- **After setup, consider teaching people about more complex Siri commands.**
- In addition to recognizing the names of homes, rooms, zones, services, and scenes, Siri can also use information such as accessory category and characteristic to identify a…
- To illustrate the power and flexibility of Siri commands, here are some examples of the types of phrases that people could use to control their accessories.

| Phrase | Siri understands |
|---|---|
| “Turn on the floor lamp” | Service (*floor lamp*) |
| “Show me the entryway camera” | Service (*entryway camera*) |
| “Turn on the light” | Accessory category (*light*) |
| “Turn off the living room light” | Room (*living room*) |
|  | Accessory category (*light*) |
| “Make the living room a little bit brighter” | Room (*living room*) |
|  | Accessory category (implied) |
|  | Brightness characteristic (*brighter*) |
| “Turn on the recessed lights” | Service group (*recessed lights*) |
| “Turn off the lights upstairs” | Accessory category (*lights*) |
|  | Zone (*upstairs*) |
| “Dim the lights in the bedroom and nursery” | Accessory category (*lights*) |
|  | Brightness characteristic (*dim*) |
|  | Rooms (*bedroom*, *nursery*) |
| “Run Good night” | Scene (*Good night*) |
| “Is someone in the living room?” | Accessory category (implied) |
|  | Occupancy detection characteristic (implied) |
| “Is my security system tripped?” | Accessory category (*security system*) |
| “Did I leave the garage door open?” | Accessory category (*garage door*) |
|  | Open characteristic (*open*) |
| “Did I forget to turn off the lights in the Tahoe House?” | Accessory category (*lights*) |
|  | Home (*Tahoe House*) |
| “It’s dark in here” | Current home (*here*) |
|  | Current room (via HomePod) |
|  | Accessory category (implied) |

- **Recommend that people create zones and service groups, if they make sense for your accessory.**
- **Offer shortcuts only for accessory-specific functionality that HomeKit doesn’t support.**
- **If your app supports both HomeKit and shortcuts, help people understand the difference between these types of voice control.**

### Custom functionality

- Your app is a great place to help people appreciate the unique functionality of your accessory.
- **Be clear about what people can do in your app and when they might want to use the Home app.**
- **Defer to HomeKit if your database differs from the HomeKit database.**
- **Ask permission to update the HomeKit database when people make changes in your app.**

#### Cameras

- Your app can display still images or streaming video from a connected HomeKit IP camera.
- **Don’t block camera images.**
- **Show a microphone button only if the camera supports bidirectional audio.**

### Using HomeKit icons

- Use the HomeKit icon in setup or instructional communications related to HomeKit technology.
- In addition, you can use the Apple Home app icon when referencing the Apple Home app or in a button that opens the Apple Home app [product…
- **Use only Apple-provided icons.**

#### Styles

- You have several options for displaying the HomeKit icon.

##### Black HomeKit icon

- Use the HomeKit icon on white or light backgrounds when other technology icons appear in black.

##### White HomeKit icon

- Use the HomeKit icon on black or dark backgrounds when other technology icons appear in white.

##### Custom color HomeKit icon

- Use a custom color when other technology icons appear in the same color.
- **Position the HomeKit icon consistently with other technology icons.**
- **Use the HomeKit icon noninteractively.**
  - ❌ Ejemplo incorrecto: An illustration of an incorrectly used HomeKit icon in a circular button styled with a chrome appearance.
  - ❌ Ejemplo incorrecto: An illustration of a button incorrectly titled 'HomeKit' with a custom gradient background.
- **Don’t use the HomeKit icon within text or as a replacement for the word HomeKit.**
  - ✅ Ejemplo correcto: The first in a series of images showing examples of the HomeKit icon when used in text. In this example, the icon correctly appears first in the line, and then the text 'Lights set with HomeKit.'
  - ❌ Ejemplo incorrecto: The second in a series of images showing examples of the HomeKit icon when used in text. This example depicts the icon incorrectly positioned after the word 'with' in the text 'Lights set with…
  - ❌ Ejemplo incorrecto: The third in a series of images showing examples of the HomeKit icon when used in text. This example depicts the icon incorrectly positioned at the end of the line of text that reads 'Lights set…
- **Pair the icon with the name *HomeKit* correctly.**

### Referring to HomeKit

- **Emphasize your app over HomeKit.**
- **Adhere to Apple’s trademark guidelines.**
  - Use Apple product names in singular form only; do not make Apple product names possessive.
  - Don’t translate Apple, Apple Home, HomeKit, or any other Apple trademark.
  - Don’t use category descriptors. For example, say iPad, not tablet.
  - Don’t indicate any kind of sponsorship, partnership, or endorsement from Apple.
  - Attribute Apple, HomeKit, and all other Apple trademarks with the correct credit lines wherever legal information appears within your app.
  - Refer to Apple devices and operating systems only in technical specifications or compatibility descriptions.
  - ✅ Ejemplo correcto: 
- See [Guidelines for Using Apple Trademarks](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html).

#### Referencing HomeKit and the Home app

- **Use correct capitalization when using the term *HomeKit*.**
- **Don’t use the name *HomeKit* as a descriptor.**
  - ✅ Ejemplo correcto: 
- **Don’t suggest that HomeKit is performing an action or function.**
  - ✅ Ejemplo correcto: 
- **Use the name *Apple* with the name *HomeKit*, if desired.**
  - ✅ Ejemplo correcto: 
- **Use the name *HomeKit* for setup, configuration, and instructions, if desired.**
  - ✅ Ejemplo correcto: 
- **Use the app name *Apple Home* whenever referring specifically to the app.**
  - ✅ Ejemplo correcto: 

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Recursos relacionados

- *Related:*
  - [Apple Design Resources](https://developer.apple.com/design/resources/)
  - [Guidelines for Using Apple Trademarks and Copyrights](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)
- *Developer documentation:*
  - [HomeKit](https://developer.apple.com/documentation/homekit)

## Vídeos que la explican

- [Add support for Matter in your smart home app](https://developer.apple.com/videos/play/wwdc2021/10298) → `references/videos/2021-10298.md`

## Registro de cambios

| Date | Changes |
|---|---|
| May 2, 2023 | Consolidated guidance into one page. |
