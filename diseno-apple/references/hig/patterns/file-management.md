# File management — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/file-management
- Descargado: 2026-10-15
- Sección: patterns
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2024-06-10 — Added guidelines for using the document launcher in iOS and iPadOS.

> Resumen de Apple: Some apps can support documents and files that people expect to manage throughout the system.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Document-based apps — such as Pages, Keynote, Photos, and Preview — help people create, edit, and save documents and files, often providing customized ways for people to browse…
- People also expect to browse documents without first opening a document-based app.

### Creating and opening files

- **Use app menus and keyboard shortcuts to give people convenient ways to create and open documents.**
- **If your app requires a custom file browser, support people’s understanding of the platform’s file system.**

### Saving work

- **Help people be confident that their work is always preserved unless they cancel or delete it.**
- **Hide file extensions by default, but let people view them if they choose.**

### Quick Look previews

- Quick Look helps you create previews of the files your app handles so that people can view them within your app and in some cases interact with them.
- **Use a Quick Look viewer to let people preview a file even when your app can’t open it.**
- **Consider implementing a Quick Look generator if your app produces custom file types.**

### Platform considerations

- *No additional considerations for tvOS, visionOS, or watchOS.*

#### iOS, iPadOS

##### Document launcher

- Starting in iOS 18 and iPadOS 18, document-based apps can use the system’s document launcher to give people a consistent, highly graphical way to browse, open, and create files.
- The document launcher consists of three main parts:
  - A *title card* that displays the app title and two app-specific buttons
  - A background image that appears behind the title card and additional images — called *accessories* — that can appear around it
  - A sheet that contains a file browser and optional app-specific controls
- You can customize all three parts of the document launcher.
- **Assign the title card’s buttons to your app’s most important functions.**
- **Provide a background that’s clearly distinct from the accessories and title card.**
- **Be mindful of accessory placement.**
- **Use animation sparingly.**

##### File provider app extension

- If your app can share its files with other apps, you can create a file provider app extension that displays a custom interface for importing, exporting, opening, and moving your…
- **When someone uses your file provider extension to open or import documents, display only documents that are appropriate in the current context.**
- **Let people select a destination when exporting and moving documents.**
  - «Unless your app stores documents in a single directory, let people navigate to a specific destination in your directory hierarchy.»
- **Avoid including a custom top toolbar.**
- Your app can also let people browse and open files from other apps.

#### macOS

##### Custom file management

- People have strong associations with the familiar file browsing experience of the Finder and most document-based apps.
- **Make your custom file-opening interface convenient.**
- **Provide a save interface to let people change a file’s name, format, or location.**
- **Consider extending the functionality of the Save dialog.**

##### Finder Sync extensions

- If your app syncs local and remote files, you can create a Finder Sync app extension to express file synchronization status and control within the Finder.
- For example, you can use a Finder Sync extension to:
  - Display badges in the Finder to indicate the sync status of items
  - Provide custom contextual menu items that perform file and folder management tasks, like favoriting and adding password-protection
  - Provide custom toolbar buttons that perform global actions, like initiating a sync operation
- **Help people avoid losing work if they turn off autosaving.**
- **When autosaving is off, make sure people know when a document has unsaved changes.**

## Recursos relacionados

- *Related:*
  - [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars)
  - [File menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#File-menu)
  - [Printing](https://developer.apple.com/design/human-interface-guidelines/printing)
- *Developer documentation:*
  - [Documents](https://developer.apple.com/documentation/swiftui/documents) — SwiftUI

## Vídeos que la explican

- [Build document-based apps in SwiftUI](https://developer.apple.com/videos/play/wwdc2020/10039) → `references/videos/2020-10039.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 10, 2024 | Added guidelines for using the document launcher in iOS and iPadOS. |
| June 21, 2023 | Updated to include guidance for visionOS. |
