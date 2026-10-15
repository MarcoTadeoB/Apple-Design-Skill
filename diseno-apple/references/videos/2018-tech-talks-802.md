# Designing for Apple Watch Series 4 — Tech Talks

- URL: https://developer.apple.com/videos/play/tech-talks/802/
- Evento: Tech Talks · Publicado: 2018-09-12 · Duración: 9:26
- Descargado: 2026-10-15 · Transcripción: sí, 189 fragmentos
- Temas: Design · Plataformas: watchos
- Origen en la lista: videos/design

> Descripción de Apple: Apple Watch Series 4 provides new opportunities for designers and developers to do more with their apps. Series 4 watches have new displays with larger dimensions, and other enhancements that allow developers to deliver richer and more immersive experiences.

## Citas clave (literales, con marca de tiempo)

_Selección automática de frases con recomendaciones o valores; verifica el contexto en el vídeo._

  - [0:30](https://developer.apple.com/videos/play/tech-talks/802/?time=30) «They come in two sizes, measured on the exterior of the case: 40mm and 44mm.»
  - [0:38](https://developer.apple.com/videos/play/tech-talks/802/?time=38) «Previous series of Apple Watch are 38mm and 42mm.»
  - [0:42](https://developer.apple.com/videos/play/tech-talks/802/?time=42) «And the display dimensions of these watches measure 272 by 340 pixels on 38mm watches, and 312 by 390 pixels on 42mm watches.»
  - [0:56](https://developer.apple.com/videos/play/tech-talks/802/?time=56) «The displays of Series 4 watches have grown significantly, measuring 324 by 394 pixels for 40mm, and 368 by 448 pixels for 44mm.»
  - [1:24](https://developer.apple.com/videos/play/tech-talks/802/?time=84) «Your app should deliver the same information and actions to the user, regardless of screen size.»
  - [1:30](https://developer.apple.com/videos/play/tech-talks/802/?time=90) «As you consider your layouts, notice that the display of the 40mm Series 4 watch is actually very similar in dimension to the display of the 42mm watches of previous series.»
  - [1:43](https://developer.apple.com/videos/play/tech-talks/802/?time=103) «The new 40mm watch has a display size that is 12 pixels wider and 4 pixels taller.»
  - [1:50](https://developer.apple.com/videos/play/tech-talks/802/?time=110) «Looking across the case sizes, 40 and 42mm watches sit in the middle of a spectrum.»
  - [1:56](https://developer.apple.com/videos/play/tech-talks/802/?time=116) «If you target your screens layouts here, you should then ensure your layouts scale down to 38mm dimensions, and up for 44mm dimensions.»
  - [3:18](https://developer.apple.com/videos/play/tech-talks/802/?time=198) «Both of these elements will be indented, and this indentation should create left and right margins that extend vertically through the display of content in your app.»
  - [3:31](https://developer.apple.com/videos/play/tech-talks/802/?time=211) «Graphic elements and button backgrounds should extend beyond these margins and run nearly edge to edge, up to the one pixel margin that runs by default on either side.»
  - [3:41](https://developer.apple.com/videos/play/tech-talks/802/?time=221) «Text should align to the left margin, extending from the left edge of the text in the status bar.»
  - [4:21](https://developer.apple.com/videos/play/tech-talks/802/?time=261) «The best watch experiences are simple and glanceable, so you may have views within your app that are intentionally single-screen and should not scroll.»
  - [4:30](https://developer.apple.com/videos/play/tech-talks/802/?time=270) «For example, if you want to make sure that a button rests in the clear area, rather than getting nudged up by the system, you can do so by setting an attribute in Xcode.»
  - [5:02](https://developer.apple.com/videos/play/tech-talks/802/?time=302) «It will be displayed at 38mm dimensions on 40mm watches, and at 42mm dimensions on 44mm watches.»
  - [5:44](https://developer.apple.com/videos/play/tech-talks/802/?time=344) «If your app contains a full-screen SpriteKit or SceneKit scene, you'll want to make sure that text and controls in your scene are rendered correctly on Series 4 watches.»
  - [5:54](https://developer.apple.com/videos/play/tech-talks/802/?time=354) «You should access the System Minimum Layout Margins to ensure that your content is inset properly from the left and right edges of the screen, and the Content Safe Area Inset information to ensure that text and actions settle appropriately in the content…»
  - [6:37](https://developer.apple.com/videos/play/tech-talks/802/?time=397) «You should evaluate your app's experience with this new haptic feedback on Series 4 watches.»
  - [6:43](https://developer.apple.com/videos/play/tech-talks/802/?time=403) «Users will become accustomed to a consistent tactile experience, so if your app coordinates events in the UI with Digital Crown rotation, you'll want to make sure that those UI events line up with these new haptic effects.»
  - [7:22](https://developer.apple.com/videos/play/tech-talks/802/?time=442) «As you're implementing and testing these styles, remember that there are different default content categories that correspond to the watch case size.»
  - [7:31](https://developer.apple.com/videos/play/tech-talks/802/?time=451) «Small is the default category for 38mm, Large for 40mm and 42mm, and XLarge for 44mm.»
  - [8:20](https://developer.apple.com/videos/play/tech-talks/802/?time=500) «When you bring this PDF asset into Xcode, place it in the Asset Catalog of your Watch project, drop the asset in the Universal 2x box.»
  - [8:35](https://developer.apple.com/videos/play/tech-talks/802/?time=515) «This scales your graphics down by 9 percent for 38mm displays, and up 10 percent for 44mm displays.»
  - [8:45](https://developer.apple.com/videos/play/tech-talks/802/?time=525) «One last note: To account for the UI of the 44mm watch, there are two new app icon sizes.»

## Recursos enlazados

- [Apple Design Resources](https://developer.apple.com/design/resources/)
- [Designing for watchOS](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-watchos)

## Vídeos relacionados

- [Developing Complications for Apple Watch Series 4](https://developer.apple.com/videos/play/tech-talks/208/) → `s-f-tech-talks-208.md`
