# Checklist para revisar un diseño según las HIG

Cómo usarla: recorre las secciones que apliquen, marca cada punto como ✅ / ⚠️ / ❌ y, para cada problema,
**cita la regla literal y su página** (las frases en inglés entre «» son de Apple). Al final de este archivo hay
un apéndice generado con **todas las reglas negativas** («Avoid…», «Don’t…», «Never…») de cada página, para
buscar con Ctrl+F.

## Formato de informe recomendado

| # | Severidad | Dónde | Problema | Regla de Apple (cita) | Fuente | Arreglo |
|---|---|---|---|---|---|---|
| 1 | Alta | Tab bar | La pestaña «Añadir» ejecuta una acción | «Use a tab bar to support navigation, not to provide actions.» | [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) | Mover «Añadir» a la toolbar de la pantalla |

Severidad: **Alta** = rompe accesibilidad, navegación o una regla explícita «Don’t/Never»; **Media** = contradice una
recomendación («Prefer…», «Consider…»); **Baja** = pulido. Si una observación no está respaldada por una fuente,
márcala como «opinión» o no la incluyas.

## 1. Plataforma y estructura

- [ ] ¿Responde cada pantalla a «¿dónde estoy?, ¿qué puedo hacer?, ¿adónde puedo ir?» — vídeo `2025-359`.
- [ ] ¿Se usan los patrones de la plataforma de destino (iOS, iPadOS, macOS, watchOS, tvOS, visionOS)? —
  `hig/getting-started/designing-for-*.md`.
- [ ] ¿La navegación principal usa tab bar (iPhone) o sidebar (iPad/Mac con jerarquía profunda)? — Tab bars, Sidebars.
- [ ] ¿La tab bar solo navega? «Use a tab bar to support navigation, not to provide actions.» — Tab bars.
- [ ] ¿Ninguna pestaña está oculta o desactivada? «Don’t disable or hide tab bar buttons, even when their content is
  unavailable.» — Tab bars.
- [ ] ¿Cada pestaña tiene etiqueta? «Include tab labels to help with navigation.» — Tab bars.
- [ ] ¿La pantalla tiene título y solo las acciones esenciales en la toolbar? — vídeo `2025-359`.
- [ ] ¿Se usa progressive disclosure en lugar de mostrarlo todo? — Layout.
- [ ] ¿Funcionalidad igual en todos los tamaños? «Keep functionality the same as size classes change» — Layout.
- [ ] iPhone Duo (si aplica): controles en el lateral, nada interactivo en el pliegue, mismas funciones en todas las
  posturas — `hig/getting-started/designing-for-iphone-duo.md`.

## 2. Componentes estándar

- [ ] ¿Se usan componentes del sistema en vez de réplicas propias de tareas convencionales? — vídeo `2026-251`.
- [ ] Botones: destino ≥ 44×44 pt (60×60 en visionOS); estilo, no tamaño, para distinguir la opción preferida; rol
  primario nunca en una acción destructiva — Buttons.
- [ ] Alerts: solo información crítica y, a ser posible, accionable — Feedback, Alerts.
- [ ] Sheets (iOS/iPadOS): Cancel en el borde inicial, Done en el final; si hay Done, hay Cancel o Back; nunca
  Cancel, Done y Back juntos — Sheets (24-3-2026).
- [ ] Modales: solo con beneficio claro, cortos y con forma obvia de cerrarlos — Modality.
- [ ] Menús: no se ocultan elementos según el contexto (se atenúan); iconos con moderación — Menus; vídeo `2025-208`.
- [ ] Búsqueda en el sitio adecuado (toolbar inferior / pestaña Search en iOS; toolbar o sidebar en iPad/Mac),
  recientes, sugerencias y estado vacío — Search fields, Searching; vídeo `2026-292`.

## 3. Liquid Glass y materiales

- [ ] Liquid Glass solo en la capa funcional; nunca en contenido («Don’t use Liquid Glass in the content layer»).
- [ ] Sin cristal sobre cristal; sin fondos/bordes extra en botones de barra; elementos agrupados por función.
- [ ] Regular por defecto; clear solo sobre medios, con atenuación del 35 % si el fondo es brillante.
- [ ] Color solo en acciones primarias o estados, en el fondo del control; no en todos los controles.
- [ ] Scroll edge effect *automatic*, uno por vista y solo bajo UI flotante; nada de fondos sólidos bajo las barras.
- [ ] Detalle: `liquid-glass.md` §10.

## 4. Color

- [ ] ¿Colores de sistema o colores propios con variantes claro, oscuro y alto contraste? — Color.
- [ ] ¿Ningún dato depende solo del color? «Convey information with more than color alone.» — Accessibility.
- [ ] ¿Contraste ≥ 4.5:1 (≤ 17 pt) / 3:1 (≥ 18 pt o negrita)? — Accessibility; `tokens.md` §4.
- [ ] ¿No se redefine el significado de los colores semánticos (p. ej. separator como texto)? — Color.
- [ ] ¿El color de marca vive en el contenido, no en las barras? — Branding; vídeo `2026-251`.

## 5. Tipografía

- [ ] ¿Estilos de texto del sistema / Dynamic Type? «Consider using the built-in text styles.» — Typography.
- [ ] ¿Tamaños ≥ mínimos (iOS 17 pt por defecto, 11 pt mínimo; macOS 13/10; tvOS 29/23; visionOS 17/12;
  watchOS 16/12)? — Typography; `tokens.md` §5.1.
- [ ] ¿Se evitan pesos finos? «In general, avoid light font weights.» — Typography.
- [ ] ¿Pocas familias tipográficas? «Minimize the number of typefaces you use» — Typography.
- [ ] ¿El diseño aguanta los tamaños de accesibilidad sin cortar texto? — Typography › Supporting Dynamic Type.
- [ ] ¿Las fuentes propias implementan Dynamic Type? — Typography; vídeo `2026-251`.

## 6. Layout y adaptabilidad

- [ ] ¿Se respetan safe areas y márgenes del sistema? — Layout › Guides and safe areas.
- [ ] ¿Contenido ordenado por importancia, alineado y agrupado? — Layout › Visual hierarchy.
- [ ] ¿Decisiones por size class, no por dispositivo u orientación? — Layout.
- [ ] ¿El fondo a pantalla completa se extiende bajo barras y sidebars? — Layout.
- [ ] macOS: nada crítico en la parte inferior de la ventana — Layout › macOS.
- [ ] tvOS: margen de 60 pt arriba/abajo y 80 pt a los lados — Layout › tvOS.

## 7. Accesibilidad

- [ ] Controles ≥ tamaño por defecto (iOS 44×44 pt; mínimo 28×28) y separación (~12 pt con bisel, ~24 sin) —
  Accessibility; `tokens.md` §6.
- [ ] Etiquetas de VoiceOver en todo elemento interactivo; controles propios con valor, acciones y respuesta —
  Accessibility; vídeo `2026-220`.
- [ ] Alternativas a gestos complejos; navegación con teclado; Switch Control y Voice Control.
- [ ] Respeta Reduce Motion, Reduce Transparency e Increase Contrast; prueba Dark Mode + Increase Contrast.
- [ ] Subtítulos/transcripciones para audio y vídeo; sin destellos rápidos.

## 8. Iconos y símbolos

- [ ] Icono de app por capas, simple, sin texto salvo esencial, sin réplicas de hardware de Apple, con apariencias
  dark/clear/tinted coherentes — App icons; vídeos `2025-220`, `2025-361`.
- [ ] Mismos símbolos para las mismas acciones; texto si no hay un símbolo inequívoco — vídeo `2025-356`.
- [ ] Metáforas estándar (papelera = borrar…) — vídeo `2026-250`; `hig/foundations/icons.md`.
- [ ] SF Symbols no usados en logotipos ni iconos de app — SF Symbols.

## 9. Escritura

- [ ] Sin relleno («simply», «quickly», «Oops»), sin repeticiones, beneficio delante — vídeo `2025-404`.
- [ ] Mismo nombre para la misma cosa en toda la app (lista de palabras) — vídeo `2025-404`; Writing.
- [ ] Mensajes de error claros y con siguiente paso; pantallas vacías con siguiente paso — Writing.
- [ ] Nombres de funciones claros para la persona, no para la tecnología — vídeo `2026-290`.

## 10. Privacidad, permisos y responsabilidad

- [ ] Permisos solo cuando hacen falta, no al abrir la app, con texto que explique el uso — Privacy.
- [ ] Nada de pantallas propias engañosas antes de la alerta del sistema — Privacy.
- [ ] Funciones de IA con salvaguardas (vista previa, confirmación, avisos) — vídeo `2026-250`; Generative AI.

## 11. Movimiento

- [ ] Movimiento con propósito, breve y opcional; nada de animar interacciones muy frecuentes — Motion.

## 12. Marcas y licencias (sobre todo en webs y marketing)

- [ ] Sin SF Pro incrustada ni SF Symbols en webs; sin logotipo de Apple; marcas sin traducir — `licencias-y-marcas.md`.

---
