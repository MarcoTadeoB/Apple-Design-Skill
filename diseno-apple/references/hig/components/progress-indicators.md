# Progress indicators — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/progress-indicators
- Descargado: 2026-10-15
- Sección: components › Status
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2023-09-12 — Combined guidance common to all platforms.

> Resumen de Apple: Progress indicators let people know that your app isn’t stalled while it loads content or performs lengthy operations.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Some progress indicators also give people a way to estimate how long they have to wait for something to complete.
- Because the duration of an operation is either known or unknown, there are two types of progress indicators:
  - *Determinate*, for a task with a well-defined duration, such as a file conversion
  - *Indeterminate*, for unquantifiable tasks, such as loading or synchronizing complex data
- Both determinate and indeterminate progress indicators can have different appearances depending on the platform.
- An indeterminate progress indicator — also called an *activity indicator* — uses an animated image to indicate progress.
- For developer guidance, see [ProgressView](https://developer.apple.com/documentation/swiftui/progressview).

### Best practices

- **When possible, use a determinate progress indicator.**
- **Be as accurate as possible when reporting advancement in a determinate progress indicator.**
  - «Showing 90 percent completion in five seconds and the last 10 percent in 5 minutes can make people wonder if your app is still working and can even feel deceptive.»
- **Keep progress indicators moving so people know something is continuing to happen.**
- **When possible, switch a progress bar from indeterminate to determinate.**
- **Don’t switch from the circular style to the bar style.**
- **If it’s helpful, display a description that provides additional context for the task.**
- **Display a progress indicator in a consistent location.**
- **When it’s feasible, let people halt processing.**
- **Let people know when halting a process has a negative consequence.**

### Platform considerations

- *No additional considerations for tvOS or visionOS.*

#### iOS, iPadOS

##### Refresh content controls

- A refresh control lets people immediately reload content, typically in a table view, without waiting for the next automatic content update to occur.
- **Perform automatic content updates.**
- **Supply a short title only if it adds value.**
- For developer guidance, see [UIRefreshControl](https://developer.apple.com/documentation/uikit/uirefreshcontrol).

#### macOS

- In macOS, an indeterminate progress indicator can have a bar or circular appearance.
- **Prefer an activity indicator (spinner) to communicate the status of a background operation or when space is constrained.**
- **Avoid labeling a spinning progress indicator.**

#### watchOS

- By default the system displays the progress indicators in white over the scene’s background color.

## Recursos relacionados

- *Developer documentation:*
  - [ProgressView](https://developer.apple.com/documentation/swiftui/progressview) — SwiftUI
  - [UIProgressView](https://developer.apple.com/documentation/uikit/uiprogressview) — UIKit
  - [UIActivityIndicatorView](https://developer.apple.com/documentation/uikit/uiactivityindicatorview) — UIKit
  - [UIRefreshControl](https://developer.apple.com/documentation/uikit/uirefreshcontrol) — UIKit
  - [NSProgressIndicator](https://developer.apple.com/documentation/appkit/nsprogressindicator) — AppKit

## Registro de cambios

| Date | Changes |
|---|---|
| September 12, 2023 | Combined guidance common to all platforms. |
| June 5, 2023 | Updated guidance to reflect changes in watchOS 10. |
