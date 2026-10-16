# Botones Cancel y Done en una sheet de iOS

## Respuesta corta

En iOS y iPadOS, los dos botones van en la **toolbar superior** de la sheet:

- **Cancel** (o Close), en el **borde inicial**: a la izquierda en idiomas que se escriben de izquierda a derecha.
- **Done**, en el **borde final**: a la derecha. Usa el estilo prominente, que lo tiñe; desde iOS 26 suele mostrarse como un checkmark azul.
- **No pongas Done solo.** Si hay Done, tiene que haber también una forma de salir sin guardar (Cancel o Back).

En una sheet **de varios pasos**, **Back** ocupa el borde inicial en lugar de Cancel a partir del segundo paso. **Nunca muestres Cancel, Done y Back a la vez.**

Esta guía es reciente. Apple la actualizó el **24-3-2026** («Updated guidance for button placement») en la página [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets).

---

## Qué hace cada botón (según Apple)

En el apartado *Anatomy* de [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets), Apple define tres botones habituales:

| Botón | Qué hace (resumen de la HIG) | Dónde va en iOS/iPadOS |
|---|---|---|
| **Cancel** (o Close) | «dismisses a sheet without saving any changes». Aparece en la mayoría de las sheets. | Borde inicial de la toolbar superior |
| **Done** | Cierra la sheet «after completing a task or explicitly saving changes». | Borde final de la toolbar superior |
| **Back** | Vuelve al paso anterior de un flujo de varios pasos o a la vista padre. **«It isn't intended to dismiss a sheet.»** | Borde inicial, en los pasos 2 y siguientes |

## Reglas literales de Apple

De [Sheets › iOS, iPadOS](https://developer.apple.com/design/human-interface-guidelines/sheets):

- «For sheets with a single view, the Cancel button belongs on the leading edge of the top toolbar.»
- «For sheets with a multi-step flow, the placement of buttons can vary across steps.»
- **«Provide an alternative to the Done button.»** Apple muestra como ejemplo incorrecto una sheet con Done solo en la esquina superior derecha. El correcto lleva Cancel arriba a la izquierda y Done arriba a la derecha.
- «Avoid showing all three buttons — Cancel, Done, and Back — together.» El ejemplo incorrecto es Back a la izquierda con Cancel y Done juntos a la derecha.
- **«Support swiping to dismiss a sheet.»**

Sobre la apariencia de Done:

- [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars): **«Use the `.prominent` style for key actions such as Done or Submit.»** También: **«Group navigation controls and critical actions like Done, Close, or Save in dedicated, familiar, and visually distinct sections.»**
- Vídeo *Get to know the new design system* (WWDC25), [9:56](https://developer.apple.com/videos/play/wwdc2025/356/?time=596): «A primary action, like Done, stays separate and appears tinted, often as a blue checkmark on iOS and iPadOS…»

## Sheet de un solo paso

```
┌───────────────────────────────────────┐
│               ───  (grabber)          │
│ [Cancel]     Título de la tarea  [✓ Done]│
│                                       │
│   contenido…                          │
└───────────────────────────────────────┘
```

- Cancel va a la izquierda. Done va a la derecha, separado y teñido.
- Si la sheet es redimensionable, incluye un grabber («Include a grabber in a resizable sheet») y permite cerrarla deslizando hacia abajo.

## Sheet de varios pasos

Apple fija lo esencial: Back no cierra la sheet, Done siempre tiene una alternativa y los tres botones nunca aparecen juntos. Deja libre la colocación exacta en cada paso («can vary across steps»). El patrón que cumple todas esas reglas es este:

| Paso | Borde inicial | Borde final | Comentario |
|---|---|---|---|
| 1 (primero) | **Cancel** | Acción para avanzar (p. ej. *Next*) | Cancel es aquí la forma de salir sin guardar |
| Intermedios | **Back** | Acción para avanzar | Back sustituye a Cancel; no añadas Cancel a la derecha |
| Último | **Back** | **Done** (prominente) | Back es la «alternativa a Done» que pide Apple |

Qué viene de Apple y qué es propuesta mía:

- **De Apple:** Back no está pensado para cerrar la sheet. No se muestran los tres botones juntos. Done siempre va acompañado de una alternativa. El resumen de cambios del 24-3-2026 recogido en esta skill indica que, en flujos de varios pasos, Back sustituye a Cancel.
- **Mío:** el botón *Next* del borde final en los pasos intermedios. Las fuentes no dicen qué botón va a la derecha en los pasos intermedios. Es solo el patrón habitual. Puedes poner ahí la acción que haga avanzar el flujo, o colocarla dentro del contenido.
- **Cómo salir desde un paso intermedio:** sin Cancel visible, el usuario cierra la sheet deslizando hacia abajo, que Apple pide admitir. Si al cerrar se perdería lo introducido, pide confirmación. Lo dice [Modality](https://developer.apple.com/design/human-interface-guidelines/modality): **«When necessary, help people avoid data loss by getting confirmation before closing a modal view.»** También pide **«Always give people an obvious way to dismiss a modal view.»**

### Antes de alargar el flujo

Apple avisa: **«For complex or prolonged user flows, consider alternatives to sheets.»** ([Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets)). [Modality](https://developer.apple.com/design/human-interface-guidelines/modality) añade **«Aim to keep modal tasks simple, short, and streamlined»** y **«Consider using a full-screen modal style for in-depth content or a complex task.»** Si el asistente tiene muchos pasos, plantéate una presentación a pantalla completa. Evita también abrir otra sheet encima: **«Display only one sheet at a time from the main interface.»**

## Checklist rápida

- [ ] Cancel en el borde inicial y Done en el borde final de la toolbar superior.
- [ ] Done nunca aparece solo: lo acompaña Cancel o Back.
- [ ] Cancel, Done y Back nunca aparecen a la vez.
- [ ] En los pasos 2 y siguientes, Back sustituye a Cancel. Back no cierra la sheet.
- [ ] Done tiene estilo `.prominent`, teñido (en iOS 26 o posterior suele ser un checkmark azul).
- [ ] Se puede cerrar la sheet deslizando, y se pide confirmación si se pierden datos.
- [ ] Si la sheet es redimensionable, tiene grabber. Plantéate el detent medium en iPhone.

## Nota sobre otras plataformas

La colocación de los botones cambia según la plataforma, como indica la propia página Sheets. Todo lo anterior se refiere a **iOS y iPadOS**. En watchOS, por ejemplo, Apple pide mantener el botón Cancel por defecto en la toolbar superior. Si cambias su etiqueta, usa SF Symbols («If you change the default label, prefer using SF Symbols to represent the action»).
