# ResearchKit — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/researchkit
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados
- Última actualización: 2023-09-12 — Updated artwork.

> Resumen de Apple: A research app lets people everywhere participate in important medical research studies.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- The ResearchKit framework provides predesigned screens and transitions that make it easy to design and build an engaging custom research app.

### Creating the onboarding experience

- When opening a research app for the first time, people encounter a series of screens that introduce them to the study, determine their eligibility to participate, request…
- **Always display the onboarding screens in the correct order.**

#### 1. Introduction

- **Provide an introduction that informs and provides a call to action.**

#### 2. Determine eligibility

- **Determine eligibility as soon as possible.**

#### 3. Get informed consent

- **Make sure participants understand your study before you get their consent.**
- **Break a long consent form into easily digestible sections.**
- **If it makes sense, provide a quiz that tests the participant’s understanding.**
- **Get the participant’s consent and, if appropriate, some contact information.**

#### 4. Request permission to access data

- **Get permission to access the participant’s device or data, and to send notifications.**

### Conducting research

- To get input from participants, your study might use surveys, active tasks, or a combination of both.
- **Create surveys that keep participants engaged.**
  - Tell participants how many questions there are and about how long the survey will take.
  - Use one screen per question.
  - Show participants their progress in the survey.
  - Keep the survey as short as possible. Several short surveys tend to work better than one long survey.
  - For questions that require some additional explanation, use the standard font for the question and a slightly smaller font for the explanatory text.
  - Tell participants when the survey is complete.
- **Make active tasks easy to understand.**
  - Describe how to perform the task using clear, simple language.
  - Explain any requirements, such as if the task must be performed at a particular time or under specific circumstances.
  - Make sure participants can tell when the task is complete.

### Managing personal information and providing encouragement

- ResearchKit offers a profile screen you can use to let participants manage personal information while they’re in your research app.
- **Use a profile to help participants manage personal data related to your study.**
- **Use a dashboard to show progress and motivate participants to continue.**

### Platform considerations

- *No additional considerations for iOS or iPadOS.

## Recursos relacionados

- *Related:*
  - [Research & Care > ResearchKit](https://www.researchandcare.org/researchkit/)
- *Developer documentation:*
  - [Research & Care > Developers](https://www.researchandcare.org/developers/)
  - [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) — HealthKit
  - [ResearchKit GitHub project](https://github.com/ResearchKit/ResearchKit)

## Vídeos que la explican

- [What's new in CareKit](https://developer.apple.com/videos/play/wwdc2020/10151) → `references/videos/2020-10151.md`
- [Build a research and care app, part 1: Setup onboarding](https://developer.apple.com/videos/play/wwdc2021/10068) → `references/videos/2021-10068.md`
- [ResearchKit and CareKit Reimagined](https://developer.apple.com/videos/play/wwdc2019/217) → `references/videos/2019-217.md`

## Registro de cambios

| Date | Changes |
|---|---|
| September 12, 2023 | Updated artwork. |
