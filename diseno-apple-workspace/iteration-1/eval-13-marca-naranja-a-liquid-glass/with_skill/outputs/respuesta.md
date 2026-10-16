# Cómo pasar tu tab bar y tu barra de navegación naranjas a Liquid Glass sin perder la marca

> Plataforma que doy por hecha: **iPhone (iOS 26/27)**. Lo que va entre «» son citas literales de Apple (en inglés). Lo que aparece como **(propio)** es una recomendación o un cálculo mío, no una regla de Apple.

## En pocas palabras

Con Liquid Glass, Apple pide justo lo contrario de lo que haces ahora. **Las barras dejan de ser el sitio donde va la marca.** El naranja sale de los fondos de la tab bar y de la barra de navegación y pasa a tres sitios:

1. **El contenido.** Cabeceras, ilustraciones, tarjetas y fotos. Pasan por debajo del cristal, que recoge su color de forma dinámica.
2. **El color de acento, con significado.** La pestaña seleccionada, la acción principal de cada pantalla (por ejemplo *Done* o *Añadir*), los badges y los estados.
3. **El resto de la identidad.** Tipografía, iconografía, tono de voz, movimiento y el icono de la app.

Apple lo dice así en *Communicate your brand identity on iOS* (WWDC26), en [9:42](https://developer.apple.com/videos/play/wwdc2026/251/?time=582): «our recommendation is to move color into the content area of your app, into the scroll view.»

La página [Branding](https://developer.apple.com/design/human-interface-guidelines/branding) de las HIG se actualizó el **9-9-2026** («Refined guidance for using brand color») con el mismo mensaje. Su ejemplo incorrecto es una app con «the brand color used in all controls». El correcto lleva «the brand color in the content layer».

---

## 1. Por qué el naranja sólido en las barras ya no encaja

| Qué haces hoy | Qué dice Apple | Fuente |
|---|---|---|
| Fondo naranja en la barra de navegación | «**Reduce the use of toolbar backgrounds and tinted controls.**» (la barra de navegación ahora forma parte de *Toolbars*) | [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars) (16-12-2025) |
| Fondo naranja en la tab bar | El cristal no tiene color propio: «By default, Liquid Glass has no inherent color, and instead takes on colors from the…» contenido de detrás | [Color › Liquid Glass color](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color) |
| Todo el *chrome* de la app en color de marca | «**Apply color sparingly to the Liquid Glass material, and to symbols or text on the material.**» | [Color](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color) |
| Color de marca en todos los controles | «**Apply your app’s accent color judiciously.**» | [Branding](https://developer.apple.com/design/human-interface-guidelines/branding) |
| Relleno opaco sobre el cristal | Un relleno sólido en lugar del tintado nativo vuelve el control opaco y «breaks the visual character of Liquid Glass» | [*Meet Liquid Glass*, 17:03](https://developer.apple.com/videos/play/wwdc2025/219/?time=1023) |
| Tintar todos los elementos | «Avoid tinting all your elements.» Si quieres color, ponlo en la capa de contenido | [*Meet Liquid Glass*, 17:29](https://developer.apple.com/videos/play/wwdc2025/219/?time=1049) |
| Color para separar las barras del contenido | Usa un *scroll edge effect*: «**Prefer the automatic scroll edge effect style.**» | [Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views) (8-6-2026) |

En la práctica, una barra opaca y naranja anula lo que da sentido a Liquid Glass. Es una **capa funcional que flota sobre el contenido** y que cambia entre claro y oscuro según lo que tenga detrás ([Materials](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass); [*Meet Liquid Glass*, 15:16](https://developer.apple.com/videos/play/wwdc2025/219/?time=916)). También pierdes las adaptaciones automáticas de accesibilidad (ver §5).

---

## 2. Qué hacer con cada pieza

| Pieza | Antes | Después (Liquid Glass) | Fuente |
|---|---|---|---|
| **Barra de navegación** | Fondo naranja opaco y título blanco | Barra estándar del sistema, sin fondo propio. Usa *large title* para orientar. Debajo, el *scroll edge effect* en modo **automatic** | [Toolbars › iOS](https://developer.apple.com/design/human-interface-guidelines/toolbars): «Use a large title to help people stay oriented…»; [Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views) |
| **Botones de la barra** | Iconos blancos (o naranjas) sobre el naranja | Símbolos **monocromos** del sistema, sin bordes ni fondos propios, agrupados por función. Botón Atrás estándar | [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars): «Prefer system-provided symbols without borders.», «Use the standard Back and Close buttons.»; [*Get to know the new design system*, 8:55](https://developer.apple.com/videos/play/wwdc2025/356/?time=535) |
| **Acción principal** (Guardar, Done, Pedir…) | Un botón más | **Solo esa** lleva el naranja de marca como tinte del fondo, con estilo prominente y separada del resto | [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars): «Use the `.prominent` style for key actions such as Done or Submit.»; [*Get to know the new design system*, 9:56](https://developer.apple.com/videos/play/wwdc2025/356/?time=596) |
| **Tab bar** | Fondo naranja y pestañas blancas | Tab bar estándar flotante abajo, sin color de fondo. El naranja va solo en la **pestaña seleccionada** (color de acento) y en los badges | [Tab bars › iOS](https://developer.apple.com/design/human-interface-guidelines/tab-bars); [*Communicate your brand identity on iOS*, 10:01](https://developer.apple.com/videos/play/wwdc2026/251/?time=601) (color para «hierarchy, groupings, or indicating interaction»: acciones primarias, badges, selección en la tab bar) |
| **Contenido** | Fondo neutro bajo las barras naranjas | Aquí va el naranja: cabecera o *hero* de marca al principio del scroll, ilustraciones, tarjetas destacadas, gráficos. Al hacer scroll pasa bajo el cristal, que lo refleja | [Branding](https://developer.apple.com/design/human-interface-guidelines/branding); [*Communicate your brand identity on iOS*, 2:50](https://developer.apple.com/videos/play/wwdc2026/251/?time=170): «Conceptually, the content layer is the best opportunity to express your brand identity.» |

### Una precaución importante en el contenido

Si una zona del contenido es naranja, **las etiquetas de las barras no pueden ser naranjas**. Apple lo repite en tres páginas:

- «**Avoid applying a similar color to tab labels and content layer backgrounds.**» ([Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars))
- «**Avoid applying a similar color to toolbar item labels and content layer backgrounds.**» ([Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars))
- «**Avoid using similar colors in control labels if your app has a colorful background.**» ([Color](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color))

**(Propio)** Si tienes una cabecera naranja grande que sube hasta la barra de navegación, deja los iconos de la barra en monocromo, que es el comportamiento por defecto. No los tintes de naranja.

Evita también que, en reposo (por ejemplo al abrir la app), contenido importante quede cortado bajo el cristal: «avoid intersections between content and Liquid Glass» ([*Meet Liquid Glass*, 17:54](https://developer.apple.com/videos/play/wwdc2025/219/?time=1074)).

---

## 3. Cómo mantener la identidad sin pintar las barras

Según el vídeo de WWDC26 y la página Branding, la marca se reconoce por más cosas que el color:

- **Tipografía propia**, si la tenéis: «**Consider using a custom font.**» ([Branding](https://developer.apple.com/design/human-interface-guidelines/branding)). Tiene que admitir Dynamic Type y pasar a varias líneas en vez de truncarse ([vídeo 2026-251, 12:14](https://developer.apple.com/videos/play/wwdc2026/251/?time=734)).
- **Componentes familiares con carácter.** «**Express your brand with familiar components.**» Dedica los componentes a medida a las zonas de mayor impacto, no a los utilitarios como menús o barras ([vídeo 2026-251, 5:07](https://developer.apple.com/videos/play/wwdc2026/251/?time=307) y [6:11](https://developer.apple.com/videos/play/wwdc2026/251/?time=371)).
- **Iconografía reconocible.** Símbolos propios o SF Symbols, coherentes y legibles en tamaños pequeños ([vídeo 2026-251, 16:28](https://developer.apple.com/videos/play/wwdc2026/251/?time=988)).
- **Tono de voz y movimiento.** «**Use your brand’s unique voice and tone in all the written communication you display.**» ([Branding](https://developer.apple.com/design/human-interface-guidelines/branding)). Las transiciones también transmiten marca ([vídeo 2026-251, 8:31](https://developer.apple.com/videos/play/wwdc2026/251/?time=511)).
- **Logotipo, con discreción.** «**Resist the temptation to display your logo throughout your app…**» No lo metas en la barra de navegación. NYT Cooking, por ejemplo, lo muestra solo en Home y lo desvanece al hacer scroll ([vídeo 2026-251, 16:03](https://developer.apple.com/videos/play/wwdc2026/251/?time=963)). Tampoco uses la pantalla de lanzamiento para la marca: «**Avoid using a launch screen as a branding opportunity.**»
- **Icono de app.** Es el sitio natural para el naranja. En iOS 26 o posterior necesita las apariencias *default, dark, clear* y *tinted* (`tokens.md` §10; [App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons)).

---

## 4. Define bien el naranja de marca (claro, oscuro y alto contraste)

- «**Make sure all your app’s colors work well in light, dark, and increased contrast contexts.**» ([Color](https://developer.apple.com/design/human-interface-guidelines/color)). Liquid Glass pide variantes clara y oscura aunque tu app tenga una sola apariencia: «provide both light and dark colors to support Liquid Glass adaptivity» (Color, recogido en `liquid-glass.md` §4).
- Créalo como **color de recursos con 4 variantes**: claro, oscuro, alto contraste claro y alto contraste oscuro. Asígnalo como color de acento (*tint*) de la app.
- Contraste: 4.5:1 para texto de hasta 17 pt y 3:1 desde 18 pt o en negrita ([Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)). Con colores propios, aspira a 7:1 en texto pequeño ([Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode)).

**(Propio, cálculo de contraste WCAG con los valores publicados del `systemOrange`)**

Sirve para orientarte si tu naranja se parece al de Apple. Los valores son de [Color › Specifications](https://developer.apple.com/design/human-interface-guidelines/color).

| systemOrange | RGB | Contraste con blanco | Contraste con negro |
|---|---|---|---|
| Claro | 255,141,40 · #FF8D28 | 2,31:1 ❌ | 9,09:1 |
| Oscuro | 255,146,48 · #FF9230 | 2,23:1 ❌ | 9,41:1 |
| Alto contraste claro | 197,83,0 · #C55300 | 4,55:1 ✅ (justo) | 4,61:1 |
| Alto contraste oscuro | 255,160,86 · #FFA056 | 2,02:1 ❌ | 10,41:1 |

Qué significa en la práctica:

- Un naranja vivo **no sirve para texto blanco** pequeño encima, como el título blanco de tu barra actual. Tampoco como texto naranja pequeño sobre fondo claro.
- Para la acción prominente tintada y para la pestaña seleccionada, comprueba tu naranja real en las cuatro variantes.
- Para la variante de alto contraste, oscurece el naranja como hace Apple (#C55300).
- La selección de la tab bar no depende solo del color, porque la forma del indicador también la marca. Aun así, «**Avoid relying solely on color…**» ([Color › Inclusive color](https://developer.apple.com/design/human-interface-guidelines/color)).

Si tu naranja es muy parecido al `systemOrange`, ten en cuenta otra regla. «**Avoid using the same color to mean different things.**» Si en tu app el naranja es la marca, no lo uses también para avisos o advertencias.

---

## 5. Accesibilidad: lo que ganas al quitar el color sólido

Con las barras y el material del sistema, Liquid Glass se adapta solo ([*Meet Liquid Glass*, 18:22](https://developer.apple.com/videos/play/wwdc2025/219/?time=1102)):

- **Reduce Transparency**: el cristal se vuelve más esmerilado («frostier»).
- **Increase Contrast**: los elementos pasan a ser predominantemente negros o blancos, con un borde de contraste.
- **Reduce Motion**: los efectos son menos intensos y desaparece la elasticidad.

Prueba en Dark Mode con Increase Contrast y Reduce Transparency, juntos y por separado ([Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)). Mira sobre todo las pantallas donde la cabecera naranja pasa bajo las barras.

---

## 6. Orientación técnica **(propia; verifica las firmas en la documentación de Apple)**

**UIKit.** Elimina las personalizaciones heredadas de las barras, porque son las que «tapan» el cristal:

- `UINavigationBarAppearance` / `UITabBarAppearance` con `configureWithOpaqueBackground()` y `backgroundColor = marca`.
- `barTintColor`.
- Fondos o imágenes propias.

Deja la apariencia por defecto y define el naranja como `tintColor` de la ventana o como *AccentColor* del catálogo de recursos.

**SwiftUI.** Esquema orientativo:

```swift
TabView {
    Tab("Inicio", systemImage: "house") {
        NavigationStack {
            ScrollView {
                CabeceraDeMarca()          // el naranja vive aquí, en el contenido
                ContenidoPrincipal()
            }
            .navigationTitle("Inicio")     // large title, sin fondo de barra
            .toolbar {
                ToolbarItem(placement: .confirmationAction) {
                    Button("Pedir", systemImage: "checkmark") { /* … */ }
                    // acción principal: la única tintada con la marca (estilo prominente)
                }
            }
        }
    }
    // … resto de pestañas
}
.tint(Color("Marca"))   // color de acento: pestaña seleccionada y acción prominente
// Sin .toolbarBackground(.orange, …) ni .toolbarColorScheme forzado
```

API de referencia: [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), [`ScrollEdgeEffectStyle`](https://developer.apple.com/documentation/swiftui/scrolledgeeffectstyle) y [`glassEffect(_:in:)`](https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)). Usa `glassEffect` solo en algún control propio muy importante: «**Use Liquid Glass effects sparingly.**» ([Materials](https://developer.apple.com/design/human-interface-guidelines/materials)). Nunca lo pongas sobre otro cristal ni en listas o tarjetas: «Don’t use Liquid Glass in the content layer».

---

## 7. Checklist de la migración

- [ ] Barra de navegación y tab bar **sin fondo propio**: sin naranja, sin opacidad y sin imagen.
- [ ] *Scroll edge effect* en modo **automatic**, solo donde hay UI flotante encima, uno por vista.
- [ ] Iconos de barra **monocromos**, sin bordes ni fondos, y botón Atrás estándar.
- [ ] Naranja **solo** en la acción principal de cada pantalla (prominente), la pestaña seleccionada, los badges y los estados.
- [ ] Naranja abundante en el **contenido**: cabecera, ilustración, tarjetas destacadas.
- [ ] Sin etiquetas de barra naranjas sobre zonas de contenido naranjas.
- [ ] Naranja definido en claro, oscuro y alto contraste (×2), con contraste comprobado.
- [ ] Logotipo fuera de las barras y de la pantalla de lanzamiento.
- [ ] Probado con Dark Mode, Reduce Transparency, Increase Contrast y Reduce Motion.

## Fuentes

- HIG: [Branding](https://developer.apple.com/design/human-interface-guidelines/branding) (9-9-2026) · [Color](https://developer.apple.com/design/human-interface-guidelines/color) (16-12-2025) · [Materials](https://developer.apple.com/design/human-interface-guidelines/materials) · [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) (8-6-2026) · [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars) (16-12-2025) · [Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views) (8-6-2026) · [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) · [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode)
- Vídeos: [*Communicate your brand identity on iOS*](https://developer.apple.com/videos/play/wwdc2026/251/) (WWDC26) · [*Meet Liquid Glass*](https://developer.apple.com/videos/play/wwdc2025/219/) (WWDC25) · [*Get to know the new design system*](https://developer.apple.com/videos/play/wwdc2025/356/) (WWDC25)
