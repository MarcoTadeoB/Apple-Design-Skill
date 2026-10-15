# Augmented reality — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/augmented-reality
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados,visionos
- Última actualización: sin registro de cambios

> Resumen de Apple: Augmented reality (or AR) lets you deliver immersive, engaging experiences that seamlessly blend virtual objects with the real world.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Using the device’s camera to present the physical world onscreen live, your app can superimpose three-dimensional virtual objects, creating the illusion that these objects…
- **Offer AR features only on capable devices.**
> **Note:** The following guidance applies to apps that run in iOS and iPadOS.

### Best practices

- **Let people use the entire display.**
- **Strive for convincing illusions when placing realistic objects.**
- **Consider how virtual objects with reflective surfaces show the environment.**
- **Use audio and haptics to enhance the immersive experience.**
- **Minimize text in the environment.**
- **If additional information or controls are necessary, consider displaying them in screen space.**
- **Consider using indirect controls when you need to provide persistent controls.**
- **Anticipate that people will use your app in a wide variety of real-world environments.**
- **Be mindful of people’s comfort.**
- **If your app encourages people to move, introduce motion gradually.**
- **Be mindful of people’s safety.**

### Providing coaching

- Before people can enjoy an AR experience in your app, they need to move their device in ways that lets ARKit evaluate the surroundings and detect surfaces.
- **Hide unnecessary app UI while people are using a coaching view.**
- **If necessary, offer a custom coaching experience.**

### Helping people place objects

- **Show people when to locate a surface and place an object.**
- **When people place an object, immediately integrate that object into the AR environment.**
- **Consider guiding people toward offscreen virtual objects.**
- **Avoid trying to precisely align objects with the edges of detected surfaces.**
- **Incorporate plane classification information to inform object placement.**

### Designing object interactions

- **Let people use direct manipulation to interact with objects when possible.**
- **Let people directly interact with virtual objects using standard, familiar gestures.**
- **In general, keep interactions simple.**
- **Respond to gestures within reasonable proximity of interactive virtual objects.**
- **Let people initiate object scaling when it makes sense in your app.**
> **Tip:** Regardless of the purpose of your app, don’t use scaling as a way to adjust the distance of an object.
- **Be wary of potentially conflicting gestures.**
- **Strive for virtual object movement that’s consistent with the physics of your app’s AR environment.**
- **Explore even more engaging methods of interaction.**

### Offering a multiuser experience

- When multiple people share your app’s AR experience, each participant maps the environment independently and ARKit automatically merges the maps.
- **Consider allowing people occlusion.**
- **When possible, let new participants enter a multiuser AR experience.**
  - «Unless your app requires all participants to join before the experience begins, consider using implicit map merging to let new people quickly join an ongoing AR experience.»

### Reacting to real-world objects

- You can enhance an AR experience by using known images and objects in the real-world environment to make virtual content appear.
- **When a detected image first disappears, consider delaying the removal of virtual objects that are attached to it.**
- **Limit the number of reference images in use at one time.**
- **Limit the number of reference images requiring an accurate position.**

### Communicating with people

- **If you must display instructional text, use approachable terminology.**

| Do | Don’t |
|---|---|
| Unable to find a surface. Try moving to the side or repositioning your phone. | Unable to find a plane. Adjust tracking. |
| Tap a location to place the *[name of object to be placed]*. | Tap a plane to anchor an object. |
| Try turning on more lights and moving around. | Insufficient features. |
| Try moving your phone more slowly. | Excessive motion detected. |

- **In a three-dimensional context, prefer 3D hints.**
  - «Avoid displaying textual overlay hints in a 3D context unless people aren’t responding to contextual hints.»
- **Make important text readable.**
- **If necessary, provide a way to get more information.**

### Handling interruptions

- ARKit can’t track device position and orientation during an interruption, such as when people briefly switch to another app or accept a phone call.
- **Consider using the system-provided coaching view to help people relocalize.**
- **Consider hiding previously placed virtual objects during relocalization.**
- **Minimize interruptions if your app supports both AR and non-AR experiences.**
- **Allow people to cancel relocalization.**
- **Indicate when the front-facing camera is unable to track a face for more than about half a second.**

### Suggesting problem resolutions

- **Let people reset the experience if it doesn’t meet their expectations.**
- **Suggest possible fixes if problems occur.**

| Problem | Possible suggestion |
|---|---|
| Insufficient features detected. | Try turning on more lights and moving around. |
| Excessive motion detected. | Try moving your phone slower. |
| Surface detection takes too long. | Try moving around, turning on more lights, and making sure your phone is pointed at a sufficiently textured surface. |

### Icons and badges

- Apps can display an AR icon in controls that launch ARKit-based experiences.
- **Use the AR glyph as intended.**
- **Maintain minimum clear space.**
  - «The minimum amount of clear space required around an AR glyph is 10% of the glyph’s height.»
- Apps that include collections of products or other objects can use badging to identify specific items that can be viewed in AR using ARKit.
- **Use the AR badges as intended and don’t alter them.**
- **Prefer the AR badge to the glyph-only badge.**
- **Use badging only when your app contains a mixture of objects that can be viewed in AR and objects that cannot.**
- **Keep badge placement consistent and clear.**
- **Maintain minimum clear space.**
  - «The minimum amount of clear space required around an AR badge is 10% of the badge’s height.»

### Platform considerations

- *No additional considerations for iOS or iPadOS.

#### visionOS

- With the wearer’s [permission](https://developer.apple.com/design/human-interface-guidelines/privacy#visionOS), you can use ARKit in your visionOS app to detect surfaces in a…

## Recursos relacionados

- *Related:*
  - [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics)
  - [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures)
  - [Apple Design Resources](https://developer.apple.com/design/resources/#ios-apps)
- *Developer documentation:*
  - [ARKit](https://developer.apple.com/documentation/arkit)

## Vídeos que la explican

- [Qualities of great AR experiences](https://developer.apple.com/videos/play/wwdc2022/10131) → `references/videos/2022-10131.md`
- [Explore ARKit 5](https://developer.apple.com/videos/play/wwdc2021/10073) → `references/videos/2021-10073.md`
