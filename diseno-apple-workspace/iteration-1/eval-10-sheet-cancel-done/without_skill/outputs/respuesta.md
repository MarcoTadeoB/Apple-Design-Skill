# Cancel y Done en una sheet de iOS

## Respuesta corta

En una sheet que recoge datos o edita algo, los botones van en la **barra de navegación superior**:

| Posición | Botón | Estilo |
|---|---|---|
| Arriba a la izquierda (*leading*) | **Cancel** | Normal |
| Centro | Título de la sheet | Corto, describe la tarea |
| Arriba a la derecha (*trailing*) | **Done** (o un verbo concreto: *Add*, *Save*, *Send*) | Destacado (en negrita, o con estilo prominente en iOS 26) |

Es el patrón que usan Calendario, Contactos, Recordatorios o Mail. La acción que confirma va siempre a la derecha y la que descarta, a la izquierda. En idiomas que se escriben de derecha a izquierda (RTL) los lados se invierten solos si usas *leading* y *trailing*.

## Detalles que conviene cuidar

- **Usa un verbo concreto si puedes.** «Add» o «Save» dicen más que «Done» cuando la sheet crea o guarda algo. Deja «Done» para cuando el usuario solo termina de ver o de ajustar algo.
- **Desactiva el botón de confirmar** mientras el formulario no sea válido; por ejemplo, si falta un campo obligatorio.
- **Si la sheet solo muestra información** y no hay nada que cancelar, pon un único botón para cerrarla: «Done» a la derecha, o el botón de cerrar (✕). No añadas un «Cancel» que no cancela nada.
- **Deslizar hacia abajo equivale a Cancel.** Si el usuario ya ha cambiado algo, no descartes esos cambios sin preguntar. Bloquea el gesto y muestra un diálogo con «Descartar cambios» / «Seguir editando». En SwiftUI se hace con `.interactiveDismissDisabled(hayCambios)` y un `confirmationDialog`.
- **iOS 26 (Liquid Glass):** los botones de la barra se dibujan como botones de vidrio. Es habitual ver Cancel como un icono ✕ a la izquierda y la confirmación como ✓ con el tinte de acento a la derecha. Si usas los *placements* semánticos, el sistema aplica estos estilos por ti.

### SwiftUI

```swift
.sheet(isPresented: $showEditor) {
    NavigationStack {
        Form { /* ... */ }
            .navigationTitle("Nuevo evento")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Add") { save(); dismiss() }
                        .disabled(!isValid)
                }
            }
    }
    .interactiveDismissDisabled(hasChanges)
}
```

Con `.cancellationAction` y `.confirmationAction` el sistema coloca cada botón en su sitio y le da el estilo correcto en cada plataforma: negrita en la confirmación, lado correcto en RTL y aspecto de vidrio en iOS 26. En UIKit, el equivalente es `navigationItem.leftBarButtonItem` con `.cancel` y `rightBarButtonItem` con `.done`.

## ¿Y si la sheet tiene varios pasos?

Usa **una sola sheet con un `NavigationStack` dentro** y navega con *push* de un paso al siguiente. No presentes una sheet encima de otra para cada paso.

| Paso | Izquierda | Derecha |
|---|---|---|
| Primero | **Cancel** | **Next** (desactivado hasta que el paso sea válido) |
| Intermedios | **‹ Back** (automático) | **Next** |
| Último | **‹ Back** | **Done** / verbo final (*Create*, *Add*…) en estilo destacado |

Reglas clave:

1. **El botón de avanzar está siempre a la derecha.** «Next» en los pasos intermedios y la acción final en el último. Solo el último paso usa el estilo de confirmación (negrita o prominente), porque es el único que termina la tarea.
2. **A partir del segundo paso, Back ocupa la izquierda.** Sirve para retroceder sin perder lo ya rellenado.
3. **Que siempre se pueda abandonar el flujo.** Hay dos formas habituales:
   - Confiar en el gesto de deslizar hacia abajo para salir, con el diálogo de «Descartar cambios» si ya hay datos.
   - Mover la confirmación abajo: un botón grande «Continuar» al pie de la pantalla, como en los flujos de configuración de Apple. Así queda libre la barra para **Back a la izquierda y Cancel a la derecha**.
   
   No pongas Back y Cancel juntos en el mismo lado.
4. **Ponle un título a cada paso** (por ejemplo «Cuenta», «Permisos», «Resumen»). Si el flujo es largo, indica el progreso con algo como «Paso 2 de 3» o un indicador discreto.
5. **Mantén pocos pasos.** Si pasan de 3 o 4, pregúntate si algunos pueden ir juntos o ser opcionales. Una sheet es para tareas acotadas.

```swift
NavigationStack(path: $path) {
    StepOneView()
        .toolbar {
            ToolbarItem(placement: .cancellationAction) { Button("Cancel") { dismiss() } }
            ToolbarItem(placement: .primaryAction) {
                Button("Next") { path.append(Step.two) }.disabled(!stepOneValid)
            }
        }
        .navigationDestination(for: Step.self) { step in
            switch step {
            case .two:
                StepTwoView()   // Back automático a la izquierda; "Next" a la derecha
            case .three:
                StepThreeView() // Back a la izquierda; .confirmationAction "Create" a la derecha
            }
        }
}
.interactiveDismissDisabled(hasEnteredData)
```

## Resumen

- **Una sheet, un paso:** Cancel a la izquierda y Done (o un verbo concreto) a la derecha, destacado.
- **Varios pasos:** Cancel solo en el primero; luego Back a la izquierda. «Next» a la derecha y la acción final destacada solo en el último paso.
- **Siempre:** usa los *placements* semánticos, pide confirmación antes de descartar cambios y deja siempre una forma clara de salir.
