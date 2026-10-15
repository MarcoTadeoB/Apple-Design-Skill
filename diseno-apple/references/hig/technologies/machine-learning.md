# Machine learning — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/machine-learning
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2026-06-08 — Made minor updates for clarity.

> Resumen de Apple: Machine learning enables apps and games to learn from data and usage patterns, letting you improve existing experiences and create engaging new ones.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- In addition to providing familiar features like image recognition and content recommendations, your app can use machine learning to forge deep connections with people and help…
- For related guidance on how to use machine learning models to enable intelligent experiences, see [Generative…

### Planning your design

- Features powered by machine learning use *models* to perform tasks that make people’s experiences more unique, like curated feeds, customized trip itineraries, and personalized…
- As you design your models, keep the intended experience of your app in mind.
- Designing the UI and user experience of a machine learning app can be uniquely challenging.
- To help you meet this challenge, first consider the role that machine learning plays in your app.
- Use the machine learning role you identify to help you define ways your app can receive and display data.

### The role of machine learning in your app

- Machine learning systems vary widely, and the ways an app can use machine learning vary widely, too.

#### Critical or complementary

- If an app can still work without the feature that machine learning supports, machine learning is complementary to the app; otherwise, it’s a critical dependency.
  - The keyboard uses machine learning to provide QuickType suggestions.
  - Face ID relies on machine learning to perform accurate face recognition. Without machine learning, Face ID would not work.
- In general, the more central a feature is to your app’s purpose — like a personalized news feed for a news app — the more people expect accurate and reliable results.

#### Private or public

- Machine learning results depend on data.
  - If a health app misinterprets data and incorrectly recommends a visit to the doctor, people are likely to experience anxiety and may lose trust in the app.
  - If a music app misinterprets data and recommends an artist that people don’t like, they’re likely to view the result as an inconsequential mistake.
- As with critical app features, features that use sensitive data must prioritize accuracy and reliability.

#### Proactive or reactive

- A *proactive* feature provides results without people requesting it to do so.
  - Siri Suggestions can proactively suggest a shortcut based on people’s recent routines.
  - QuickType suggests words in reaction to what people type.
- Because people don’t ask for the results that a proactive feature provides, they may have less tolerance for low-quality information.

#### Visible or invisible

- Apps may use machine learning to support visible or invisible features.
- As the name suggests, an invisible feature provides results that aren’t obvious to people.
- People’s impression of the reliability of results can differ depending on whether a feature is visible or invisible.

#### Dynamic or static

- All machine learning models can improve, but some improve dynamically, as people interact with the feature, and others improve offline and affect the feature only when the app…
- In addition to the frequency of app updates, static or dynamic improvements can affect other parts of the user experience, too.

### Explicit feedback

- Explicit feedback provides actionable information your app can use to improve the content and experience it presents to people.
- *Favoriting* — marking an item for quick access in the future — and *social feedback* — expressing emotions toward others — are common user interactions that seem like mechanisms…
- **Request explicit feedback only when necessary.**
- **Always make providing explicit feedback a voluntary task.**
- **Use simple, direct language to describe each explicit feedback option and its consequences.**
  - Suggest less pop music
  - Suggest more thrillers
  - Mute politics for a week
- **Add icons to an option description if it helps people understand it.**
- **Consider offering multiple options when requesting explicit feedback.**
- **Act immediately when you receive explicit feedback and persist the resulting changes.**
- **Consider using explicit feedback to help improve when and where you show results.**

### Implicit feedback

- Implicit feedback is information that arises as people interact with your app’s features.
- **Always secure people’s information.**
- **Help people control their information.**
- **Don’t let implicit feedback decrease people’s opportunities to explore.**
- **When possible, use multiple feedback signals to improve suggestions and mitigate mistakes.**
- **Consider withholding private or sensitive suggestions.**
- **Prioritize recent feedback.**
- **Use feedback to update predictions on a cadence that matches the person’s mental model of the feature.**
- **Be prepared for changes in implicit feedback when you make changes to your app’s UI.**
- **Beware of confirmation bias.**

### Calibration

- Calibration is a process during which people provide information that a feature needs to function.
- In general, only use calibration when your feature can’t function without that initial information.
- **Always secure people’s information.**
- **Be clear about why you need people’s information.**
- **Collect only the most essential information.**
- **Avoid asking people to participate in calibration more than once.**
  - «An exception is a feature that needs calibration with an object instead of a person.»
- **Make calibration quick and easy.**
  - Prioritize getting a few pieces of important information and infer the rest from other sources or by getting people’s feedback.
  - Avoid asking for information that most people would have to look up.
  - Avoid asking people to perform actions that might be difficult.
- **Make sure people know how to perform calibration successfully.**
- **Immediately provide assistance if progress stalls.**
- **Confirm success.**
- **Let people cancel calibration at any time.**
- **Give people a way to update or remove information they provided during calibration.**

### Mistakes

- It’s inevitable that your app will make mistakes.
  - Anticipate mistakes. As much as possible, design ways to avoid mistakes and mitigate them when they happen.
  - Help people handle mistakes. Mistakes can have a wide range of consequences, so the tools you provide to handle a mistake must be able to address those consequences.
  - Learn from mistakes when doing so improves your app.
- There are several machine learning patterns that can help you address mistakes:
  - [Limitations](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Limitations) help you set people’s expectations about the accuracy of your suggestions.
  - [Corrections](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Corrections) give people a way to be successful even when your results are wrong.
  - [Attribution](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Attribution) gives people insight into where suggestions come from, which can help…
  - [Confidence](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Confidence) helps you gauge the quality of your results, which can impact how you…
  - Feedback — both [explicit](#Explicit-feedback) and [implicit](#Implicit-feedback) — lets people tell you about mistakes that you might not be aware of.
- **Understand the significance of a mistake’s consequences.**
- **Make it easy for people to correct frequent or predictable mistakes.**
- **Continuously update your feature to reflect people’s evolving interests and preferences and help avoid mistakes.**
- **When possible, address mistakes without complicating the UI.**
- **Be especially careful to avoid mistakes in proactive features.**
- **As you work on reducing mistakes in one area, always consider the effect your work has on other areas and overall accuracy.**

### Corrections

- People use corrections to fix mistakes that apps make.
- **Give people familiar, easy ways to make corrections.**
- **Provide immediate value when people make a correction.**
- **Let people correct their corrections.**
- **Always balance the benefits of a feature with the effort required to make a correction.**
- **Never rely on corrections to make up for low-quality results.**
- **Learn from corrections when it makes sense.**
- **When possible, use guided corrections instead of freeform corrections.**

### Multiple options

- Depending on the design of your feature, it might work best to present a single result or multiple results from which people can choose.
- You might present multiple options to people in the following contexts:
  - Suggested options, a proactive feature that suggests content to people based on their past interactions. For example, For You recommendations from Apple Music.
  - Requested options, a reactive feature that suggests potential next steps to people based on their recent actions. For example, QuickType suggestions.
  - Corrections, which are actions people take to fix mistakes your app has made when it’s acting on their behalf. For example, the Photos Auto-Crop feature.
- **Prefer diverse options.**
- **In general, avoid providing too many options.**
- **List the most likely option first.**
- **Make options easy to distinguish and choose.**
- **Learn from selections when it makes sense.**

### Confidence

- Confidence indicates the measure of certainty for a result.
- Although it might seem like higher confidence produces a higher quality result — and therefore a better user experience — it doesn’t necessarily work that way.
- **Know what your confidence values mean before you decide how to present them.**
- **In general, translate confidence values into concepts that people already understand.**
- **In situations where attributions aren’t helpful, consider ranking or ordering the results in a way that implies confidence levels.**
- **In scenarios where people expect statistical or numerical information, display confidence values that help them interpret the results.**
- **Whenever possible, help people make decisions by conveying confidence in terms of actionable suggestions.**
- **Consider changing how you present results based on different confidence thresholds.**
- **When you know that confidence values correspond to result quality, you generally want to avoid showing results when confidence is low.**

### Attribution

- An attribution expresses the underlying basis or rationale for a result, without explaining exactly how a model works.
- To help you decide whether to include attributions in your app, consider how you want them to affect people.
  - Encourage people to change what they do in your app
  - Minimize the impact of [mistakes](#Mistakes)
  - Help people build a mental model of your feature
  - Promote trust in your app over time
- **Consider using attributions to help people distinguish among results.**
- **Avoid being too specific or too general.**
- **Keep attributions factual and based on objective analysis.**
- **In general, avoid technical or statistical jargon.**
  - «The exception to this is when the result itself is of a statistical or technical nature, such as information in the areas of weather, sports, polling and election results, or scientific data.»

### Limitations

- Every feature — whether it’s based on machine learning or not — has certain limitations to what it can deliver.
- An important part of the design process is to identify the scenarios where limitations impact the user experience and design ways to help people work with them.
  - Set people’s expectations before they use the feature.
  - Show people how to get the best results while they’re using the feature.
  - When inferior results occur, explain why so that people can understand the feature better.
- **Help people establish realistic expectations.**
- **Demonstrate how to get the best results.**
  - Use placeholder text to suggest input.
  - As people interact with the feature, provide feedback on their actions to guide them toward a result without overwhelming them.
  - Suggest alternative ways to accomplish the goal instead of showing no results.
- **Explain how limitations can cause unsatisfactory results.**
- **Consider telling people when limitations are resolved.**

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Recursos relacionados

- *Related:*
  - [Generative AI](https://developer.apple.com/design/human-interface-guidelines/generative-ai)
  - [Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy)
- *Developer documentation:*
  - [Apple Intelligence and machine learning](https://developer.apple.com/documentation/technologyoverviews/ai-machine-learning)
  - [Create ML](https://developer.apple.com/documentation/createml)
  - [Core ML](https://developer.apple.com/documentation/coreml)

## Vídeos que la explican

- [Explore prompt design & safety for on-device foundation models](https://developer.apple.com/videos/play/wwdc2025/248) → `references/videos/2025-248.md`
- [Discover machine learning & AI frameworks on Apple platforms](https://developer.apple.com/videos/play/wwdc2025/360) → `references/videos/2025-360.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 8, 2026 | Made minor updates for clarity. |
| October 24, 2023 | Added art to Corrections section. |
| May 2, 2023 | Consolidated guidance into one page. |
