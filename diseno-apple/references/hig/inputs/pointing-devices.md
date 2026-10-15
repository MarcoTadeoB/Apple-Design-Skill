# Pointing devices — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/pointing-devices
- Descargado: 2026-10-15
- Sección: inputs
- Plataformas: ios,ipados,macos,visionos
- Última actualización: 2023-06-21 — Updated to include guidance for visionOS.

> Resumen de Apple: People can use a pointing device like a trackpad or mouse to navigate the interface and initiate actions.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- People appreciate the precision and flexibility that pointing devices offer.

### Best practices

- **Be consistent when responding to mouse and trackpad gestures.**
- **Avoid redefining systemwide trackpad gestures.**
- **Provide a consistent experience in your app, whether people are using gestures, eyes, a pointing device, or a keyboard.**
- **Let people use the pointer to reveal and hide controls that automatically minimize or fade out.**
- **Provide a consistent experience when people press and hold a modifier key while interacting with objects in your app.**

### Platform considerations

- *No additional considerations for iOS.

#### iPadOS

- iPadOS builds on the traditional pointer experience, automatically adapting the pointer to the current context and providing rich visual feedback at a level of precision that…
- **Allow multiple selection in custom views when necessary.**
- **Distinguish between pointer and finger input only if it provides value.**

##### Pointer shape and content effects

- iPadOS integrates the appearance and behavior of both the pointer and the element it moves over, bringing focus to the item the pointer is targeting.
- By default, the pointer’s shape is a circle, but it can display a system-defined or custom shape when people move it over specific elements or regions.
- With a *content effect*, the UI element or region beneath the pointer can also change its appearance when people hold the pointer over it.
- iPadOS defines three content effects that bring focus to different types of interactive elements in your app: highlight, lift, and hover.
- The *highlight* effect transforms the pointer into a translucent, rounded rectangle that acts as a background for a control and includes a gentle parallax.
- The *lift* effect combines a subtle parallax with the appearance of elevation to make an element seem like it’s floating above the screen.
- *Hover* is a generic effect that lets you apply custom scale, tint, or shadow values to an element as the pointer moves over it.

##### Pointer accessories

- Pointer accessories are visual indicators that help people understand how they can use the pointer to interact with the current UI element.
- Unlike pointer shapes and content effects, accessories are secondary items that can combine with any pointer to communicate additional information.
- **Use clear, simple images to create custom accessories.**
- **Consider using the accessory transition to signal a change in an element’s state or behavior.**

##### Pointer magnetism

- iPadOS helps people use the pointer to target an element by making the element appear to attract the pointer.
- When people move the pointer close to an element, the system starts transforming the pointer’s shape as soon as it reaches the element’s hit region.
- When people flick the pointer toward an element, iPadOS examines the pointer’s trajectory to discover the element that’s the most likely target.
- By default, iPadOS applies magnetism to elements that use the lift effect (like app icons) and the highlight effect (like bar buttons), but not to elements that use hover.
- The system also applies magnetism to text-entry areas, where it can help people avoid skipping to another line if they make unintended vertical movements while they’re selecting…

##### Standard pointers and effects

- **When possible, support the system-provided content effects.**
  - Use highlight for a small element that has a transparent background.
  - Use lift for a small element that has an opaque background.
  - Use hover for large elements and customize the scale, tint, and shadow attributes as needed (for guidance, see [Customizing…
- **Prefer the system-provided pointer appearances for standard buttons and text-entry areas.**
- **Add padding around interactive elements to create comfortable hit regions.**
  - «In general, it works well to add about 12 points of padding around elements that include a bezel; for elements without a bezel, it works well to add about 24 points of padding around the element’s visible edges.»
- (imagen) An illustration of a button that has a filled, rounded-rectangle bezel. The button is centered on top of a shaded rectangle that extends beyond the button by the same distance on all sides. Centered on each side, a callout indicates that the padding between the button and each edge of the shaded rectangle is 12 points.
- (imagen) An illustration of a symbol centered on top of a shaded rectangle that extends beyond the symbol by the same distance on all sides. Centered on each side, a callout indicates that the padding between the symbol and each edge of the shaded rectangle is 24 points.
- (imagen) An illustration of a button without a bezel, centered on top of a shaded rectangle that extends beyond the button by the same distance on all sides. Centered on each side, a callout indicates that the padding between the button and each edge of the shaded rectangle is 24 points.
- **Create contiguous hit regions for custom bar buttons.**
- **Specify the corner radius of a nonstandard element that receives the lift effect.**

##### Customizing pointers

- **Prefer system-provided pointer effects for custom elements that behave like standard elements.**
- **Use pointer effects in consistent ways throughout your app.**
- **Avoid creating gratuitous pointer and content effects.**
- **Keep custom pointer shapes simple.**
- **Consider enhancing the pointer experience by displaying custom annotations that provide useful information.**
- **Avoid displaying instructional text with a pointer.**
- **Consider the interplay of shadow, scale, and element spacing when defining custom hover effects.**

#### macOS

- macOS supports a wide range of standard mouse and trackpad interactions that people can customize.

| Click or gesture | Expected behavior | Mouse | Trackpad |
|---|---|---|---|
| Primary click | Select or activate an item, such as a file or button. | ● | ● |
| Secondary click | Reveal contextual menus. | ● | ● |
| Scrolling | Move content up, down, left, or right within a view. | ● | ● |
| Smart zoom | Zoom in or out on content, such as a web page or PDF. | ● | ● |
| Swipe between pages | Navigate forward or backward between individually displayed pages. | ● | ● |
| Swipe between full-screen apps | Navigate forward or backward between full-screen apps and spaces. | ● | ● |
| Mission Control (double-tap the mouse with two fingers or swipe up on the trackpad with three or four fingers) | Activate Mission Control. | ● | ● |
| Lookup and data detectors (force click with one finger or tap with three fingers) | Display a lookup window above selected content. |  | ● |
| Tap to click | Perform the primary click action using a tap rather than a click. |  | ● |
| Force click | Click then press firmly to display a Quick Look window or lookup window above selected content. Apply a variable amount of pressure to affect pressure-sensitive controls, such as variable speed media controls. |  | ● |
| Zoom in or out (pinch with two fingers) | Zoom in or out. |  | ● |
| Rotate (move two fingers in a circular motion) | Rotate content, such as an image. |  | ● |
| Notification Center (swipe from the edge of the trackpad) | Display Notification Center. |  | ● |
| App Exposé (swipe down with three or four fingers) | Display the current app’s windows in Exposé. |  | ● |
| Launchpad (pinch with thumb and three fingers) | Display the Launchpad. |  | ● |
| Show Desktop (spread with thumb and three fingers) | Slide all windows out of the way to reveal the desktop. |  | ● |

##### Pointers

- macOS offers a variety of standard pointer styles, which your app can use to communicate the interactive state of an interface element or the result of a drag operation.

| Pointer | Name | Meaning | AppKit API |
|---|---|---|---|
| ![A pointer that resembles a diagonal arrow pointing up and to the left.](https://developer.apple.com/images/com.apple.HIG/pointers-arrow@2x.png) | Arrow | Standard pointer for selecting and interacting with content and interface elements. | [arrow](https://developer.apple.com/documentation/appkit/nscursor/arrow) |
| ![A closed, gloved hand.](https://developer.apple.com/images/com.apple.HIG/pointers-closed-hand@2x.png) | Closed hand | Dragging to reposition the display of content within a view—for example, dragging a map around in Maps. | [closedHand](https://developer.apple.com/documentation/appkit/nscursor/closedhand) |
| ![A pointer arrow with a small menu-like square to the right of the arrow.](https://developer.apple.com/images/com.apple.HIG/pointers-contextual-menu@2x.png) | Contextual menu | A contextual menu is available for the content below the pointer. This pointer is generally shown only when the Control key is pressed. | [contextualMenu](https://developer.apple.com/documentation/appkit/nscursor/contextualmenu) |
| ![A plus symbol.](https://developer.apple.com/images/com.apple.HIG/pointers-crosshair@2x.png) | Crosshair | Precise rectangular selection is possible, such as when viewing an image in Preview. | [crosshair](https://developer.apple.com/documentation/appkit/nscursor/crosshair) |
| ![A small pointer arrowhead with a circle underneath; the circle contains an Ex.](https://developer.apple.com/images/com.apple.HIG/pointers-disappearing-item@2x.png) | Disappearing item | A dragged item will disappear when dropped. If the item references an original item, the original is unaffected. For example, when dragging a mailbox out of the favorites bar in Mail, the original mailbox isn’t removed. | [disappearingItem](https://developer.apple.com/documentation/appkit/nscursor/disappearingitem) |
| ![A small pointer arrowhead with a circle underneath; the circle contains a plus symbol.](https://developer.apple.com/images/com.apple.HIG/pointers-drag-copy@2x.png) | Drag copy | Duplicates a dragged—not moved—item when dropped into the destination. Appears when pressing the Option key during a drag operation. | [dragCopy](https://developer.apple.com/documentation/appkit/nscursor/dragcopy) |
| ![A curved arrow, pointing up and to the right.](https://developer.apple.com/images/com.apple.HIG/pointers-drag-link@2x.png) | Drag link | During a drag and drop operation, creates an alias of the selected file when dropped. The alias points to the original file, which remains unmoved. Appears when pressing the Option and Command keys during a drag operation. | [dragLink](https://developer.apple.com/documentation/appkit/nscursor/draglink) |
| ![Opposing veritcal braces, used to form an insertion marker.](https://developer.apple.com/images/com.apple.HIG/pointers-horizontal-beam@2x.png) | Horizontal I beam | Selection and insertion of text is possible in a horizontal layout, such as a TextEdit or Pages document. | [iBeam](https://developer.apple.com/documentation/appkit/nscursor/ibeam) |
| ![An open, gloved hand.](https://developer.apple.com/images/com.apple.HIG/pointers-open-hand@2x.png) | Open hand | Dragging to reposition content within a view is possible. | [openHand](https://developer.apple.com/documentation/appkit/nscursor/openhand) |
| ![A small pointer arrowhead with a do not enter symbol underneath.](https://developer.apple.com/images/com.apple.HIG/pointers-operation-not-allowed@2x.png) | Operation not allowed | A dragged item can’t be dropped in the current location. | [operationNotAllowed](https://developer.apple.com/documentation/appkit/nscursor/operationnotallowed) |
| ![A gloved hand, with the index finger extended.](https://developer.apple.com/images/com.apple.HIG/pointers-pointing-hand@2x.png) | Pointing hand | The content beneath the pointer is a URL link to a webpage, document, or other item. | [pointingHand](https://developer.apple.com/documentation/appkit/nscursor/pointinghand) |
| ![A horizontal bar with a downward-pointing arrow at its midpoint.](https://developer.apple.com/images/com.apple.HIG/pointers-resize-down@2x.png) | Resize down | Resize or move a window, view, or element downward. | [resizeDown](https://developer.apple.com/documentation/appkit/nscursor/resizedown) |
| ![A vertical bar with a left-pointing arrow at its midpoint.](https://developer.apple.com/images/com.apple.HIG/pointers-resize-left@2x.png) | Resize left | Resize or move a window, view, or element to the left. | [resizeLeft](https://developer.apple.com/documentation/appkit/nscursor/resizeleft) |
| ![A vertical bar with left- and right-pointing arrows extending from its midpoint.](https://developer.apple.com/images/com.apple.HIG/pointers-resize-left-right@2x.png) | Resize left/right | Resize or move a window, view, or element to the left or right. | [resizeLeftRight](https://developer.apple.com/documentation/appkit/nscursor/resizeleftright) |
| ![A vertical bar with a right-pointing arrow at its midpoint.](https://developer.apple.com/images/com.apple.HIG/pointers-resize-right@2x.png) | Resize right | Resize or move a window, view, or element to the right. | [resizeRight](https://developer.apple.com/documentation/appkit/nscursor/resizeright) |
| ![A horizontal bar with an up-pointing arrow at its midpoint.](https://developer.apple.com/images/com.apple.HIG/pointers-resize-up@2x.png) | Resize up | Resize or move a window, view, or element upward. | [resizeUp](https://developer.apple.com/documentation/appkit/nscursor/resizeup) |
| ![A horizontal bar with up- and down-pointing arrows extending from its midpoint.](https://developer.apple.com/images/com.apple.HIG/pointers-resize-up-down@2x.png) | Resize up/down | Resize or move a window, view, or element upward or downward. | [resizeUpDown](https://developer.apple.com/documentation/appkit/nscursor/resizeupdown) |
| ![Opposing horizontal braces, used to form an insertion marker.](https://developer.apple.com/images/com.apple.HIG/pointers-vertical-beam@2x.png) | Vertical I beam | Selection and insertion of text is possible in a vertical layout. | [iBeamCursorForVerticalLayout](https://developer.apple.com/documentation/appkit/nscursor/ibeamcursorforverticallayout) |

#### visionOS

- In visionOS, people can attach an external pointing device or keyboard, and use both devices while they continue to use their eyes and hands.
- When a pointing device is attached, the area people are looking at determines the pointer’s context.
- When people use an attached pointing device that supports gestures, like a trackpad or mouse, the pointer hides while people are gesturing, minimizing visual distraction.

## Recursos relacionados

- *Related:*
  - [Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data)
  - [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards)
- *Developer documentation:*
  - [Input events](https://developer.apple.com/documentation/swiftui/input-events) — SwiftUI
  - [Pointer interactions](https://developer.apple.com/documentation/uikit/pointer-interactions) — UIKit
  - [Mouse, Keyboard, and Trackpad](https://developer.apple.com/documentation/appkit/mouse-keyboard-and-trackpad) — AppKit

## Vídeos que la explican

- [Design for the iPadOS pointer](https://developer.apple.com/videos/play/wwdc2020/10640) → `references/videos/2020-10640.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 21, 2023 | Updated to include guidance for visionOS. |
