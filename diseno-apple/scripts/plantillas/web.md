# Llevar el diseño de Apple a HTML/CSS (legalmente)

Las HIG son para apps de plataformas Apple; **no hay una guía de Apple para webs**. Este archivo traduce sus
valores y reglas a la web. Distingue siempre:

- **[HIG]** / **[vídeo]**: dato de Apple, con fuente.
- **[Web]**: conocimiento de la plataforma web (WebKit, W3C), no de Apple.
- **[Skill]**: decisión de esta skill (aproximación propia) — dilo así al usuario.
- **[Probado]**: verificado en este entorno (Chromium 141 headless, 15-10-2026). No había WebKit para probar Safari.

Licencias y marcas: `licencias-y-marcas.md`. Valores completos: `tokens.md`.

## 1. Tipografía del sistema

```css
:root {
  /* En dispositivos Apple → San Francisco (fuente del sistema del visitante; no se distribuye nada). */
  font-family: -apple-system, BlinkMacSystemFont, system-ui, "Inter", "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
```

- **No incrustes SF Pro ni New York** (`@font-face` con sus archivos): la licencia prohíbe incrustarlas y usarlas
  para «website content» [HIG/Fonts, ver `licencias-y-marcas.md`].
- Fuera de Apple, **Inter** es la alternativa habitual [Skill]: es de licencia libre (SIL OFL, compruébalo en su
  web) y tiene métricas cercanas. Auto-alójala si la necesitas.
- `font-feature-settings`/`font-optical-sizing: auto` ayudan con fuentes variables [Web].

## 2. Dynamic Type en Safari de iOS

```css
html { font: -apple-system-body; }   /* [Web/WebKit] toma el tamaño de texto elegido en Ajustes */
body { font-size: 1rem; }             /* a partir de aquí, todo en rem/em para que escale */
.title-1 { font-size: 1.647rem; }     /* 28/17: proporciones de la tabla Large de la HIG */
@supports not (font: -apple-system-body) { html { font-size: 106.25%; } } /* 17 px de base fuera de WebKit [Skill] */
```

- `-apple-system-body` es una palabra clave de WebKit; solo funciona en Safari/WebKit. WebKit tiene otras
  (`-apple-system-headline`, etc.); compruébalas en Safari antes de usarlas [Web].
- Regla de Apple: «Make sure your app’s layout adapts to all font sizes» y «Keep text truncation to a minimum as
  font size increases» [HIG Typography]. En web: evita alturas fijas en contenedores de texto y deja que los
  elementos en línea pasen a apilarse.
- Tamaños mínimos de texto: 17 pt por defecto y 11 pt mínimo en iOS [HIG Accessibility/Typography].

## 3. Escala tipográfica y tracking según el tamaño

El tracking de SF Pro cambia con el tamaño (positivo en tamaños pequeños, negativo en medianos, positivo otra vez
en títulos grandes) [HIG Typography › Tracking values]. Valores en 1/1000 em → `letter-spacing: Xem`.

<<css_tipo>>

Para cualquier otro tamaño, usa la fila de la tabla SF Pro de `tokens.md` §5.7 (6–96 pt…). Si usas **Inter** u otra
fuente, el tracking de SF Pro **no** aplica tal cual [Skill]: empieza en 0 y ajusta a ojo.

## 4. Tokens en variables CSS (modo oscuro y alto contraste)

<<css_colores>>

**Colores semánticos** (texto, fondos, separadores): Apple **no publica sus RGB** [HIG Color]. Aproximación
[Skill], decláralo así si la usas:

```css
:root {
  --label: #000;  --label-2: rgb(60 60 67 / .6);  --label-3: rgb(60 60 67 / .3); /* [Skill] aproximación */
  --bg: #fff;     --bg-2: var(--gray6);  --fill: rgb(120 120 128 / .2);           /* gray6 sí es de la HIG */
  --separator: rgb(60 60 67 / .29);
  --accent: var(--blue);
}
@media (prefers-color-scheme: dark) {
  :root { --label: #fff; --label-2: rgb(235 235 245 / .6); --label-3: rgb(235 235 245 / .3);
          --bg: #000; --bg-2: var(--gray6); --separator: rgb(84 84 88 / .6); }
}
```

Otros tokens:

```css
:root {
  --tap-min: 44px;          /* [HIG Accessibility] iOS: 44x44 pt por defecto, 28x28 mínimo */
  --pad-bezel: 12px;        /* [HIG Accessibility] ~12 pt alrededor de elementos con bisel */
  --pad-sin-bezel: 24px;    /* ~24 pt sin bisel */
  --dim-clear: rgb(0 0 0 / .35); /* [HIG Materials] atenuación de Liquid Glass clear sobre fondo brillante */
  /* Radios: la HIG no publica números. Concentricidad [vídeo 2025-356, 3:42]: */
  --r-contenedor: 28px;     /* [Skill] valor de partida para tu contenedor */
  --pad-contenedor: 8px;
  --r-interno: calc(var(--r-contenedor) - var(--pad-contenedor)); /* concéntrico = radio padre − padding */
}
.capsula { border-radius: 999px; } /* cápsula = radio de la mitad de la altura */
```

Contraste mínimo: 4.5:1 hasta 17 pt; 3:1 desde 18 pt o en negrita [HIG Accessibility]; aspira a 7:1 en colores
propios de texto pequeño [HIG Dark Mode].

## 5. Preferencias de accesibilidad del sistema

Equivalentes web de los ajustes que Liquid Glass respeta automáticamente [vídeo 2025-219, 18:22]:

| Ajuste de Apple | Media query [Web] | Qué hacer en tu CSS |
|---|---|---|
| Dark Mode | `prefers-color-scheme: dark` | Variables oscuras (arriba) |
| Increase Contrast | `prefers-contrast: more` | Colores de alto contraste de la HIG; vidrio casi opaco y **borde contrastado** |
| Reduce Transparency | `prefers-reduced-transparency: reduce` | Quita `backdrop-filter` o hazlo «más esmerilado»/opaco |
| Reduce Motion | `prefers-reduced-motion: reduce` | Sin rebotes ni elasticidad; transiciones cortas de opacidad |
| (Windows) Contraste alto | `forced-colors: active` | Deja que el sistema pinte; borde visible |

## 6. Liquid Glass en la web

Reglas que se mantienen [HIG Materials; vídeo 2025-219]: solo en la **capa funcional** (barras, controles
flotantes), nunca en tarjetas o listas de contenido; **nada de cristal sobre cristal**; *regular* por defecto y
*clear* solo sobre fotos o vídeo con atenuación; color solo en la acción primaria.

### 6.1 Estructura (sombra en capa hermana)

```html
<!-- Filtro de refracción (una vez por página). Solo lo aplica Chromium (Chrome, Edge). -->
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <filter id="lg-refraccion" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.012" numOctaves="2" seed="7" result="ruido"/>
    <feGaussianBlur in="ruido" stdDeviation="2" result="ruidoSuave"/>
    <feDisplacementMap in="SourceGraphic" in2="ruidoSuave" scale="18" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
</svg>

<div class="glass">
  <span class="glass__sombra" aria-hidden="true"></span>  <!-- sombra exterior: capa hermana -->
  <div class="glass__vidrio">…contenido del control…</div>
</div>
```

```css
.glass { position: relative; isolation: isolate; border-radius: var(--r, 999px); }
.glass__sombra {                       /* la sombra va AQUÍ, no en el vidrio */
  position: absolute; inset: 0; border-radius: inherit; z-index: -1; pointer-events: none;
  box-shadow: 0 8px 24px rgb(0 0 0 / .18), 0 1px 3px rgb(0 0 0 / .12);
}
.glass__vidrio {
  position: relative; border-radius: inherit;
  background: rgb(255 255 255 / .55);
  -webkit-backdrop-filter: blur(16px) saturate(180%);          /* Safari: vidrio esmerilado */
  backdrop-filter: blur(16px) saturate(180%) url(#lg-refraccion); /* Chromium: + refracción */
  /* Borde especular: brillo superior + filo fino. Las sombras INSET sí son compatibles con el filtro [Probado]. */
  box-shadow: inset 0 1px 0 rgb(255 255 255 / .75), inset 0 0 0 1px rgb(255 255 255 / .35),
              inset 0 -1px 0 rgb(0 0 0 / .06);
}
@media (prefers-color-scheme: dark) {
  .glass__vidrio { background: rgb(40 40 44 / .55);
    box-shadow: inset 0 1px 0 rgb(255 255 255 / .22), inset 0 0 0 1px rgb(255 255 255 / .12); }
}
/* Variante clear (solo sobre medios): más transparente + atenuación del 35 % [HIG Materials] */
.glass--clear .glass__vidrio { background: rgb(255 255 255 / .12); }
.glass--clear::before { content: ""; position: absolute; inset: 0; border-radius: inherit; background: var(--dim-clear); z-index: -1; }
/* Acción primaria tintada: color en el FONDO del control, no en el texto [HIG Color] */
.glass--primaria .glass__vidrio { background: color-mix(in srgb, var(--accent) 85%, transparent); color: #fff; }

@media (prefers-reduced-transparency: reduce) {
  .glass__vidrio { -webkit-backdrop-filter: none; backdrop-filter: none; background: rgb(246 246 248); }
}
@media (prefers-reduced-transparency: reduce) and (prefers-color-scheme: dark) {
  .glass__vidrio { background: rgb(36 36 38); }
}
@media (prefers-contrast: more) {
  .glass__vidrio { background: #fff; color: #000; box-shadow: inset 0 0 0 2px #000; }
}
@media (prefers-contrast: more) and (prefers-color-scheme: dark) {
  .glass__vidrio { background: #000; color: #fff; box-shadow: inset 0 0 0 2px #fff; }
}
```

### 6.2 Qué se probó y qué no

- [Probado, Chromium 141] `backdrop-filter: url(#filtro)` con `feDisplacementMap` produce la refracción.
- [Probado, Chromium 141] Una **sombra exterior en el mismo elemento** (`box-shadow` exterior o `filter: drop-shadow`)
  **rompe** el filtro SVG: la zona refractada se desplaza y se recorta (en otras versiones de Chrome puede desaparecer
  del todo). Con la sombra en una **capa hermana** se ve correcta y respeta el `border-radius`.
- [Probado] Las sombras `inset` (borde especular) en el mismo elemento **no** afectan al filtro.
- [No probado aquí] Safari/WebKit no aplica `url()` en `backdrop-filter`: se queda con el desenfoque
  (`-webkit-backdrop-filter`), que es una degradación aceptable. Firefox: comprueba el soporte de `backdrop-filter`.
- Rendimiento [Web]: `backdrop-filter` y los filtros SVG son caros; úsalos en pocos elementos (coincide con «Use
  Liquid Glass effects sparingly» [HIG]).

### 6.3 Separar controles del contenido (scroll edge effect)

[HIG Layout/Scroll views] En lugar de un fondo sólido bajo la barra, un efecto de borde que solo aparece cuando hay
contenido debajo:

```css
.barra-superior { position: sticky; top: 0; z-index: 10; }
.barra-superior::before {        /* difumina el contenido que pasa por debajo */
  content: ""; position: absolute; inset: 0 0 -24px 0; z-index: -1; pointer-events: none;
  -webkit-backdrop-filter: blur(8px); backdrop-filter: blur(8px);
  -webkit-mask-image: linear-gradient(#000 60%, transparent); mask-image: linear-gradient(#000 60%, transparent);
}
```

Úsalo solo donde haya UI flotante y uno por vista.

## 7. Ejemplo: tab bar flotante de iPhone

Reglas aplicadas [HIG Tab bars; vídeos 2025-356 y 2025-359]: navegación, no acciones; etiquetas visibles; iconos
claros; badge para información crítica; no ocultar ni desactivar pestañas; Liquid Glass sobre el contenido; destino
de 44 pt; búsqueda como pestaña al final si la app la necesita.

```html
<nav class="tab-bar glass" aria-label="Principal">
  <span class="glass__sombra" aria-hidden="true"></span>
  <ul class="glass__vidrio" role="list">
    <li><a href="/" aria-current="page"><svg aria-hidden="true" viewBox="0 0 24 24"><path d="M4 11 12 4l8 7v8a1 1 0 0 1-1 1h-4v-6H9v6H5a1 1 0 0 1-1-1z"/></svg><span>Inicio</span></a></li>
    <li><a href="/biblioteca"><svg aria-hidden="true" viewBox="0 0 24 24"><rect x="4" y="4" width="6" height="16" rx="1.5"/><rect x="14" y="4" width="6" height="16" rx="1.5"/></svg><span>Biblioteca</span></a></li>
    <li><a href="/avisos"><svg aria-hidden="true" viewBox="0 0 24 24"><path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/></svg><span>Avisos</span><b class="badge" aria-label="3 nuevos">3</b></a></li>
    <li class="buscar"><a href="/buscar"><svg aria-hidden="true" viewBox="0 0 24 24"><circle cx="11" cy="11" r="6"/><path d="m16 16 4 4"/></svg><span>Buscar</span></a></li>
  </ul>
</nav>
```

```css
.tab-bar { position: fixed; left: 50%; transform: translateX(-50%);
  bottom: calc(env(safe-area-inset-bottom, 0px) + 8px); width: min(100% - 32px, 420px); }
.tab-bar ul { display: flex; margin: 0; padding: 4px; list-style: none; gap: 2px; }
.tab-bar li { flex: 1; }
.tab-bar a { position: relative; display: flex; flex-direction: column; align-items: center; justify-content: center;
  min-height: 48px; min-width: var(--tap-min); border-radius: 999px; gap: 2px;
  font-size: 10px; font-weight: 600; letter-spacing: 0.01em; color: var(--label); text-decoration: none; }
.tab-bar svg { width: 24px; height: 24px; fill: none; stroke: currentColor; stroke-width: 1.8;
  stroke-linecap: round; stroke-linejoin: round; }
.tab-bar a[aria-current="page"] { color: var(--accent); background: rgb(120 120 128 / .16); }
.badge { position: absolute; top: 2px; left: 55%; min-width: 18px; height: 18px; padding: 0 5px; border-radius: 9px;
  background: var(--red); color: #fff; font: 600 12px/18px system-ui; text-align: center; }
@media (prefers-reduced-motion: no-preference) { .tab-bar a { transition: background-color .2s, color .2s; } }
```

- El tamaño de 10 px de las etiquetas es una elección [Skill] para encajar 4 pestañas en 360 px; las HIG no publican
  el tamaño de la etiqueta de la tab bar. Mantén el destino táctil ≥ 44 px [HIG].
- Añade `padding-bottom` al contenido para que la barra no tape lo último de la página.

## 8. Iconos propios en lugar de SF Symbols

- No uses SF Symbols en la web (no consta permiso) ni copias «confusingly similar» [HIG SF Symbols].
- Diseña o usa una biblioteca con licencia libre; recomendaciones de estilo inspiradas en SF Symbols [Skill + HIG]:
  trazo con extremos redondeados, grosor que acompañe al peso del texto (≈1.5–2 px a 24 px), `currentColor`,
  rejilla de 24×24 con margen óptico, mismos iconos para las mismas acciones en toda la app («Use the same symbols
  across devices» [vídeo 2025-356]).
- Accesibilidad: `aria-hidden="true"` en el SVG y etiqueta de texto visible o `aria-label` en el control.
- Las acciones comunes y su símbolo preferido de Apple están en `hig/foundations/icons.md`: úsalo como guía de
  **metáfora** (papelera = borrar, lupa = buscar), no como fuente de dibujos.

## 9. Instalación como app (pantalla de inicio)

Fuente: plataforma web/WebKit [Web], no las HIG.

```html
<link rel="manifest" href="/manifest.webmanifest">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">           <!-- PNG cuadrado opaco (p. ej. 180×180) -->
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes">             <!-- modo standalone en iOS (heredado) -->
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Nombre corto">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

```json
{
  "name": "Nombre completo", "short_name": "Nombre corto",
  "start_url": "/", "scope": "/", "display": "standalone",
  "background_color": "#ffffff", "theme_color": "#ffffff",
  "icons": [
    { "src": "/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icon-512.png", "sizes": "512x512", "type": "image/png" },
    { "src": "/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
  ]
}
```

- Con `viewport-fit=cover` y barra de estado translúcida, respeta `env(safe-area-inset-top|bottom|left|right)`.
- El icono: aplica los consejos de la HIG de iconos de app (formas simples, fondo de color, sin texto salvo que sea
  esencial, sin réplicas de hardware de Apple) [HIG App icons], pero **no** imites iconos de Apple.

## 10. Checklist web

- [ ] Sin archivos de SF Pro/New York ni SF Symbols; fuente del sistema + alternativa libre.
- [ ] Texto en rem con base `-apple-system-body` en Safari; nada se corta al aumentar el tamaño.
- [ ] Colores con variables para claro/oscuro/alto contraste; contraste ≥ 4.5:1.
- [ ] Destinos táctiles ≥ 44 px; ≥ 12 px de separación con bisel.
- [ ] Liquid Glass solo en la capa funcional; sombra exterior en capa hermana; degradación en Safari.
- [ ] `prefers-reduced-transparency`, `prefers-contrast`, `prefers-reduced-motion` atendidos.
- [ ] Sin logotipos, marcas ni capturas de UI de Apple que hagan pensar que es de Apple.
