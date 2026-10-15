# Del naranja sólido a Liquid Glass sin perder la marca

## Resumen

En iOS 26 las barras ya no se pintan con el color de marca. El naranja sale del **fondo de la barra** y pasa a tres sitios: el **tint** de los controles, las **acciones principales** y el **contenido** que se ve a través del cristal.

La tab bar y la barra de navegación de Liquid Glass son una capa de cristal que flota sobre el contenido y lo refracta. Si les pones un fondo naranja opaco, pierdes el efecto, la app se ve "antigua" frente al resto del sistema y además tapas el contenido que ahora debería verse por debajo.

---

## 1. Qué cambia de forma de pensar

| Antes (iOS 18 y anteriores) | Ahora (Liquid Glass, iOS 26+) |
|---|---|
| La barra es una franja de color de marca | La barra es cristal neutro que flota sobre el contenido |
| La marca está en el "chrome" (barras) | La marca está en el **contenido** y en los **controles** |
| Iconos y texto blancos sobre naranja | Iconos en color de sistema y el ítem seleccionado en naranja |
| Fondo opaco fijo | El cristal toma el color de lo que hay debajo y se adapta a claro/oscuro |

La idea de Apple es separar dos capas: el **contenido** (tu marca, tus fotos, tus colores) y la **capa de navegación** (cristal, funcional, discreta). Tu identidad no se pierde: cambia de sitio.

---

## 2. Paso a paso

### Paso 1: quita los fondos personalizados de las barras

Es lo primero y lo que más se nota. Busca y elimina (o deja solo para iOS < 26):

**UIKit**
```swift
// ❌ Esto desactiva Liquid Glass en la barra
let appearance = UINavigationBarAppearance()
appearance.configureWithOpaqueBackground()
appearance.backgroundColor = .brandOrange
appearance.titleTextAttributes = [.foregroundColor: UIColor.white]
navigationBar.standardAppearance = appearance
navigationBar.scrollEdgeAppearance = appearance

let tabAppearance = UITabBarAppearance()
tabAppearance.configureWithOpaqueBackground()
tabAppearance.backgroundColor = .brandOrange
tabBar.standardAppearance = tabAppearance
```

**SwiftUI**
```swift
// ❌ Igual: quítalo en iOS 26
.toolbarBackground(Color.brandOrange, for: .navigationBar, .tabBar)
.toolbarBackground(.visible, for: .navigationBar, .tabBar)
.toolbarColorScheme(.dark, for: .navigationBar)
```

Si necesitas mantener iOS 17/18 con el look anterior, envuélvelo en una comprobación de disponibilidad:

```swift
if #available(iOS 26, *) {
    // No tocar el fondo: dejar el cristal del sistema
} else {
    applyLegacyOrangeAppearance()
}
```

### Paso 2: usa el naranja como **tint** global

El color de marca pasa a ser el *accent color* de la app. Así el ítem seleccionado de la tab bar, los botones de la barra de navegación, los toggles, los enlaces, etc. salen en naranja.

- En el Asset Catalog, define el color `AccentColor` (o `BrandOrange`) con variantes para **Light**, **Dark** y **High Contrast**.
- Aplícalo en la raíz:

```swift
// SwiftUI
WindowGroup {
    ContentView()
        .tint(.brandOrange)
}
```

```swift
// UIKit
window.tintColor = .brandOrange
// o, por barra:
tabBarController.tabBar.tintColor = .brandOrange
navigationController.navigationBar.tintColor = .brandOrange
```

Resultado: la tab bar es cristal y la pestaña activa se ve en naranja. Es el patrón que usan las apps del sistema (Música en rojo, Podcasts en morado, etc.).

### Paso 3: el naranja "fuerte" solo para la acción principal

Liquid Glass permite **cristal teñido**, pero Apple recomienda usarlo con moderación: solo para la acción más importante de la pantalla, no para toda la barra.

**SwiftUI**
```swift
.toolbar {
    ToolbarItem(placement: .confirmationAction) {
        Button("Pedir", systemImage: "checkmark") { order() }
            .buttonStyle(.glassProminent)
            .tint(.brandOrange)
    }
}
```

**UIKit**
```swift
let pedir = UIBarButtonItem(title: "Pedir", style: .prominent, target: self, action: #selector(order))
pedir.tintColor = .brandOrange
navigationItem.rightBarButtonItem = pedir
```

Para controles propios que flotan sobre el contenido (por ejemplo un botón flotante de "Nuevo"):

```swift
Button { create() } label: {
    Image(systemName: "plus").font(.title2.bold())
        .frame(width: 56, height: 56)
}
.glassEffect(.regular.tint(.brandOrange).interactive(), in: .circle)
```

Regla práctica: **una sola pieza naranja de cristal por pantalla.** Si todo es naranja, nada destaca.

### Paso 4: lleva la marca al **contenido**, debajo del cristal

Aquí es donde recuperas la sensación "naranja" de tu app, y queda mejor que antes:

- **Cabeceras de marca:** pon un header naranja (degradado, ilustración o foto con tu color) al principio del scroll. Como el contenido ahora llega por debajo de la barra de navegación, el cristal se ve **naranja** mientras el header está detrás y se vuelve neutro al hacer scroll. Tienes la identidad al abrir la pantalla y la legibilidad al leer.
- **Extiende el fondo bajo las barras:** no metas el contenido en un `safeArea` con margen. Deja que fluya por detrás de la tab bar y la nav bar.
- **Imágenes hero:** en SwiftUI, `.backgroundExtensionEffect()` extiende una imagen por detrás de barras y sidebars con un reflejo difuminado.
- **Tarjetas, iconos y estados vacíos** con tu naranja, tu tipografía y tus ilustraciones.

```swift
ScrollView {
    BrandHeader()               // degradado naranja + logo/ilustración
        .frame(height: 220)
    ContentList()
}
.ignoresSafeArea(edges: .top)   // solo para el header, si procede
.navigationTitle("Inicio")
```

### Paso 5: controla la legibilidad con el *scroll edge effect*

En iOS 26 las barras no tienen fondo, pero el sistema aplica un **efecto de borde** que difumina el contenido bajo ellas para que se lean los títulos y botones.

- Por defecto es `.soft` (difuminado suave), que es lo que conviene en casi todos los casos.
- Si tu contenido es muy denso o tiene mucho contraste (por ejemplo, listas con cabeceras fijas o tablas de datos), usa `.hard`:

```swift
.scrollEdgeEffectStyle(.hard, for: .top)
```

**No intentes recrear el fondo naranja** con un `Rectangle` detrás de la barra: pierdes el efecto y el sistema puede dibujar encima de forma rara.

### Paso 6: aprovecha los comportamientos nuevos de la tab bar

- **Minimizar al hacer scroll:** da más protagonismo a tu contenido (y a tu color).
  ```swift
  TabView { ... }
      .tabBarMinimizeBehavior(.onScrollDown)
  ```
- **Accesorio inferior** (mini reproductor, pedido en curso, etc.), que puede llevar tu acento:
  ```swift
  .tabViewBottomAccessory { PedidoEnCursoView() }
  ```
- **Pestaña de búsqueda** separada con `Tab(role: .search)`.
- Usa **SF Symbols** en las pestañas (o símbolos personalizados con el mismo grosor). Los iconos rellenos y blancos pensados para fondo naranja quedan mal sobre cristal.

### Paso 7: agrupa bien los botones de la barra

En iOS 26 los botones de la barra se agrupan en "cápsulas" de cristal compartidas. Agrupa por función y separa lo que no tiene relación:

```swift
.toolbar {
    ToolbarItemGroup(placement: .topBarTrailing) {
        Button("Compartir", systemImage: "square.and.arrow.up") { }
        Button("Favorito", systemImage: "heart") { }
    }
    ToolbarSpacer(.fixed, placement: .topBarTrailing)
    ToolbarItem(placement: .topBarTrailing) {
        Button("Pedir", systemImage: "bag") { }
            .buttonStyle(.glassProminent)
    }
}
```

En UIKit, `UIBarButtonItem.hidesSharedBackground` y `UIBarButtonItem.fixedSpace(_:)` cumplen la misma función.

---

## 3. Otros sitios donde vive la marca

- **Icono de la app:** rehazlo con **Icon Composer**, por capas, para que funcione en los modos claro, oscuro, tintado y transparente (*clear*). Es el sitio donde más se ve tu naranja.
- **Pantalla de inicio (launch screen)** y **onboarding** con fondo de marca a sangre.
- **Widgets, Live Activities y notificaciones** con tu color como acento.
- **Tipografía y tono de voz:** son identidad igual que el color.

---

## 4. Accesibilidad y contraste (importante con el naranja)

- El naranja medio (tipo `#FF9500`) **no llega a 4,5:1** sobre blanco para texto normal. Para texto y glifos pequeños en modo claro usa una variante más oscura del naranja. En modo oscuro puedes usar una más luminosa.
- Define el color en el Asset Catalog con variantes **Any / Dark** y **High Contrast**, y no uses el hex directamente en el código.
- Prueba con **Reducir transparencia** y **Aumentar contraste** (Ajustes > Accesibilidad > Pantalla y tamaño del texto). El sistema convierte el cristal en superficies más opacas; comprueba que tu tint sigue siendo legible.
- No transmitas información **solo** con el naranja (por ejemplo, estado "seleccionado"): el sistema ya añade forma y peso, no lo anules.

---

## 5. Errores habituales

1. **Teñir toda la barra de naranja con cristal teñido.** Parece la solución intermedia, pero queda pesado, compite con el contenido y empeora la legibilidad. El tint de cristal es para acciones puntuales.
2. **Cristal sobre cristal:** poner un botón con `.glassEffect` dentro de una barra que ya es cristal. Usa los estilos de botón del sistema dentro de las barras.
3. **Mantener los iconos blancos** que estaban pensados para fondo naranja.
4. **Meter el contenido en márgenes** para que "no se vea por debajo": así desaparece la gracia del material.
5. **Usar `UIDesignRequiresCompatibility` como solución definitiva.** Esa clave del `Info.plist` mantiene el diseño antiguo temporalmente, pero Apple ha avisado de que dejará de funcionar en una versión mayor próxima. Úsala solo para ganar tiempo mientras migras.

---

## 6. Checklist de migración

- [ ] Eliminar los `UINavigationBarAppearance` / `UITabBarAppearance` con fondo opaco (o limitarlos a iOS < 26).
- [ ] Eliminar `.toolbarBackground(...)` con color de marca en iOS 26.
- [ ] Definir `AccentColor` naranja con variantes Light/Dark/High Contrast y aplicarlo como `tint` global.
- [ ] Marcar como `.prominent` / `.glassProminent` solo la acción principal de cada pantalla.
- [ ] Añadir cabeceras o fondos de marca en el contenido que pasen por debajo de las barras.
- [ ] Revisar los iconos de la tab bar (SF Symbols, sin relleno blanco forzado).
- [ ] Valorar `.tabBarMinimizeBehavior(.onScrollDown)` y `.tabViewBottomAccessory`.
- [ ] Ajustar `scrollEdgeEffectStyle` en pantallas densas.
- [ ] Rehacer el icono con Icon Composer (claro, oscuro, tintado, transparente).
- [ ] Probar con Reducir transparencia, Aumentar contraste, modo oscuro y Dynamic Type grande.

---

## En una frase

**El cristal es del sistema, el contenido es tuyo.** Deja las barras en cristal neutro, pon el naranja en el tint, en la acción principal y en un contenido con mucha presencia de marca que se vea a través del cristal. Tu app se seguirá reconociendo como tuya y además se sentirá nativa en iOS 26.
