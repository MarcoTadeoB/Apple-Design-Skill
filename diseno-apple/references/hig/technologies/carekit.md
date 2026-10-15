# CareKit — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/carekit
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados
- Última actualización: 2023-05-02 — Consolidated guidance into one page.

> Resumen de Apple: People can use CareKit apps to manage care plans related to a chronic illness like diabetes, recover from an injury or surgery, or achieve health and wellness goals.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- To learn more about CareKit, see [Research & Care > CareKit](https://www.researchandcare.org/carekit/).
- CareKit 2.0 contains two projects, CareKit UI and CareKit Store.

### Data and privacy

- Nothing is more important than protecting people’s privacy and safeguarding the extremely sensitive data your CareKit app collects and stores.
- **Provide a coherent privacy policy.**
- In addition to the data that people enter into your CareKit app, you may be able to access data through iOS features and capabilities.

#### HealthKit integration

- HealthKit is the central repository for health and fitness data in iOS and watchOS.
- **Request access to health data only when you need it.**
- **Clarify your app’s intent by adding descriptive messages to the standard permission screen.**
- **Manage health data sharing solely through the system’s privacy settings.**
- For related design guidance, see [HealthKit](https://developer.apple.com/design/human-interface-guidelines/healthkit).

#### Motion data

- If it’s useful for treatment and if people give permission, your app can get motion information from the device to determine if people are standing still, walking, running,…
- Motion information can also include custom data collected as part of physical therapy.
- For developer guidance, see [Core Motion](https://developer.apple.com/documentation/coremotion).

#### Photos

- Pictures are a great way to communicate treatment progress.
- For developer guidance, see [UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller).

#### ResearchKit integration

- A ResearchKit app lets people participate in important medical research studies.
- For related design guidance, see [ResearchKit](https://developer.apple.com/design/human-interface-guidelines/researchkit).

### CareKit views

- CareKit UI provides customizable views organized into three categories — tasks, charts, and contacts — and defines several default view styles in each.
- Each view category is designed to support specific types of content and interaction.

| Category | Purpose |
|---|---|
| [Tasks](https://developer.apple.com/design/human-interface-guidelines/carekit#Tasks) | Present tasks, like taking medication or doing physical therapy. Support logging of patient symptoms and other data. |
| [Charts](https://developer.apple.com/design/human-interface-guidelines/carekit#Charts) | Display graphical data that can help people understand how their treatment is progressing. |
| [Contact views](https://developer.apple.com/design/human-interface-guidelines/carekit#Contact-views) | Display contact information. Support communication through phone, message, and email, and link to a map of the contact’s location. |

- A CareKit UI view consists of a header and may include a stack of content subviews.
- CareKit UI takes care of all the layout constraints within a view, so you don’t have to worry about breaking existing constraints when you add new subviews to the stack.

#### Tasks

- A care plan generally presents a set of prescribed actions for people to perform, such as taking medication, eating specific foods, exercising, or reporting symptoms.
- A task can contain the following types of information.

| Information | Required | Description | Example value |
|---|---|---|---|
| Title | Yes | A word or short phrase that introduces the task. | *Ibuprofen* |
| Schedule | Yes | The schedule on which a task must be completed. | *Four times a day* |
| Instructions | No | Detailed instructions, recommendations, and warnings. | *Take 1 tablet every 4–6 hours (not to exceed 4 tablets daily).* |
| Group ID | No | An identifier you can use to group similar tasks in ways that make sense in your app. | A category identifier like  *medication* or *exercise*. |

- In CareKit 2.0, CareKit UI defines five styles of task views: simple, instructions, log, checklist, and grid.
- **Use the simple style for a one-step task.**
- **Use the instructions style when you need to add informative text to a simple task.**
- **Use the log style to help people log events.**
- **Use the checklist style to display a list of actions or steps in a multistep task.**
- **Use the grid style to display a grid of buttons in a multistep task.**
- **Consider using color to reinforce the meaning of task items.**
- **Combine accuracy with simplicity when describing a task and its steps.**
- **Consider supplementing multistep or complex tasks with videos or images.**

#### Charts

- Chart views let you present data and trends in graphical ways that can help people visualize their progress in a care plan.
- In CareKit 2.0, CareKit UI provides three chart styles: bar, scatter, and line.
- **Consider highlighting narratives and trends to illustrate progress.**
- **Label chart elements clearly and succinctly.**
- **Use distinct colors.**
- **Consider providing a legend to add clarity.**
- **Clearly denote units of time.**
- **Consolidate large data sets for greater readability.**
- **If necessary, offset data to keep charts proportional.**
- For developer guidance, see [CareKit > Chart Interfaces](https://carekit-apple.github.io/CareKit/documentation/carekit/chart-interfaces).

#### Contact views

- A care plan typically includes a care team and other trusted individuals who can help patients follow the plan.
- In CareKit 2.0, CareKit UI provides two styles of the contact view: simple and detailed.
- **Consider using color to categorize care team members.**

### Notifications

- Notifications can tell people when it’s time to take medication or complete a task, and badging your app icon can show that there’s an unread message from a caregiver.
- **Minimize notifications.**
- **Consider providing a detail view.**

### Symbols and branding

- CareKit uses a variety of built-in symbols to help people understand what they can do in a care app.
- Although you can customize the default symbols, most view styles work best with the CareKit-provided symbols.
- In a grid view, you might want to display custom symbols that are relevant to the unique content and experience in your app.
- Using SF Symbols in your app gives you:
  - Designs that coordinate with CareKit’s visual design language
  - Support for creating custom symbols to represent the unique content in your app
- **Design a relevant care symbol.**
- **Incorporate refined, unobtrusive branding.**

### Platform considerations

- *No additional considerations for iOS or iPadOS.

## Recursos relacionados

- *Related:*
  - [Research & Care > CareKit](https://www.researchandcare.org/carekit/)
- *Developer documentation:*
  - [CareKit](https://carekit-apple.github.io/CareKit/documentation/carekit)
  - [Research & Care > Developers](https://www.researchandcare.org/developers/)
  - [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) — HealthKit
  - [HealthKit](https://developer.apple.com/documentation/healthkit)
  - [ResearchKit GitHub project](https://github.com/ResearchKit/ResearchKit)

## Vídeos que la explican

- [What's new in CareKit](https://developer.apple.com/videos/play/wwdc2020/10151) → `references/videos/2020-10151.md`
- [Build a research and care app, part 1: Setup onboarding](https://developer.apple.com/videos/play/wwdc2021/10068) → `references/videos/2021-10068.md`

## Registro de cambios

| Date | Changes |
|---|---|
| May 2, 2023 | Consolidated guidance into one page. |
