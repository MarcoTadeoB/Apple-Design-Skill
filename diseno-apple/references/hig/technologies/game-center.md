# Game Center — HIG (condensado)

- URL: https://developer.apple.com/design/human-interface-guidelines/game-center
- Descargado: 2026-10-15
- Sección: technologies
- Plataformas: ios,ipados,macos,tvos,visionos,watchos
- Última actualización: 2025-06-09 — Added guidance for new challenges and multiplayer activities, and considerations for the Apple Games app and Game Overlay. Updated guidance and specifications for activity preview images.

> Resumen de Apple: Game Center is Apple’s social gaming network, which lets players track their progress and connect with friends across Apple platforms, and boosts the discovery of your game across players’ devices.

_Formato: las frases en **negrita** son las reglas literales de Apple (citas cortas);
«…» son frases literales con valores numéricos; las tablas son las especificaciones
originales. Para el texto completo, abre la URL._
- Supporting Game Center in your game allows players to:
  - Discover new games their friends are playing.
  - Seamlessly invite friends to play.
  - See the latest activity from their games across the system, in the Apple Games app, the App Store, notifications, and more.
- By enabling the player activities listed above, supporting Game Center also helps surface your game to more players across Apple platforms.
- You can add Game Center into your game using the GameKit framework, which provides a full-featured UI that makes it easy for players to access and view their Game Center data…

### Accessing Game Center

- To provide the best Game Center experience for your players, begin by determining whether the player is signed in to their Game Center account on the system when they launch your…

#### Integrating the access point

- The Game Center *access point* is an Apple-designed UI element that lets players view their Game Center profile and information without leaving your game.
- In iOS, iPadOS, and macOS the access point leads players to the Game Overlay, a system overlay that allows players to view their progress and start game activities.
- In visionOS and tvOS, the access point leads players to the in-game dashboard, a full-screen view of a player’s Game Center activity that appears on top of your game.
- **Display the access point in menu screens.**
- **Avoid placing controls near the access point.**
> **Note:** In visionOS, the locations of the access point vary based on game type, such as immersive or volume-based.
- **Consider pausing your game while the Game Overlay or dashboard is present.**

#### Using custom UI

- Your game can include custom links into the Game Overlay (in iOS, iPadOS, macOS) or the dashboard (in visionOS and tvOS).
- **Use the artwork Game Center provides in custom links.**
- **Use the correct terminology in custom links.**

| Term | Incorrect terms | Localization |
|---|---|---|
| Game Center | GameKit, GameCenter, game center | Use the system-provided translation of *Game Center* |
| Game Center Profile | Profile, Account, Player Info | Use the system-provided translation of *Game Center* and localize *Profile* |
| Achievements | Awards, Trophies, Medals |  |
| Leaderboards | Rankings, Scores, Leaders |  |
| Challenges | Competitions |  |
| Add Friends | Add, Add Profiles, Include Friends |  |

### Achievements

- Achievements give players an added incentive to stay engaged with your game.

#### Integrating achievements into your game

- **Align with Game Center achievement states.**
- **Determine a display order.**
- **Be succinct when describing achievements.**
- **Give players a sense of progress.**

#### Creating achievement images

- **Design rich, high-quality images that help players feel rewarded.**
- **Create artwork in the appropriate size and format.**

**Pestaña «iOS, iPadOS, macOS, visionOS»**

| Attribute | Value |
|---|---|
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 512x512 pt (1024x1024 px @2x) |
| Mask diameter | 512 pt (1024 px @2x) |

**Pestaña «tvOS»**

| Attribute | Value |
|---|---|
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 320x320 pt (640x640 px @2x) |
| Mask diameter | 200 pt (400 px @2x) |

### Leaderboards

- Leaderboards are a great way to encourage friendly competition within your game.
- **Choose a leaderboard type.**
  - A *classic leaderboard* tracks a player’s best all-time score.
  - A *recurring leaderboard* resets based on a time interval you define, such as every week or every day.
- **Take advantage of leaderboard sets for multiple leaderboards.**
  - Difficulty modes (Easy, Standard, Hard)
  - Activity types (Combat, Crafting, Farming)
  - Genres and themes (Disco, Pop, Rock)
- **Add leaderboard images.**
- For games that run in iOS, iPadOS, and macOS, use a single image for your leaderboard image.

**Pestaña «iOS, iPadOS, macOS»**

| Attribute | Value |
|---|---|
| Format | JPEG, JPG, or PNG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 512x512 pt (1024x1024 px @2x) |
| Cropped area | 512x312 pt (1024x624 px @2x) |

**Pestaña «tvOS»**

| Attribute | Value |
|---|---|
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 659x371 pt (1318x742 px @2x) |
| Focused size | 618x348 pt (1236x696 px @2x) |
| Unfocused size | 548x309 pt (1096x618 px @2x) |

> **Note:** Be mindful of how cropping might affect your leaderboard artwork.

### Challenges

- Challenges turn single player activities into multiplayer experiences with friends.
- **Create engaging challenges.**
  - Complete the fastest lap in a racing level.
  - Defeat the most enemies in a single round.
  - Solve a daily puzzle with the fewest mistakes.
- **Avoid creating challenges that track overall progress or personal best scores.**
- **Make it easy to jump into your challenge.**
- **Create high-quality artwork that encourages players to engage with your challenges.**

| Attribute | Value |
|---|---|
| Format | JPEG, JPG, or PNG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 1920x1080 pt (3840x2160 px @2x) |
| Cropped area | 1465x767 pt (2930x1534 px @2x) |

### Multiplayer activities

- Game Center supports both real-time and turn-based multiplayer activities that make it easy to connect players with friends or other players.
- **Use party codes to invite players to multiplayer activities.**
  - Allow players to join gameplay late, leave early, and return later.
  - Provide a way for players to view the current party code in your game.
  - Allow players to enter a party code manually.
- **Support multiplayer activities through in-game UI.**
- **Provide engaging activity artwork.**

| Attribute | Value |
|---|---|
| Format | JPEG, JPG, or PNG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 1920x1080 pt (3840x2160 px @2x) |
| Cropped area | 1465x767 pt (2930x1534 px @2x) |

### Platform considerations

- *No additional considerations for iOS, iPadOS, macOS, or visionOS.*

#### tvOS

- **Display an optional image at the top of the dashboard.**

| Attribute | Value |
|---|---|
| Image size | 600x180 pt (1200x360 px @2x) |
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |

#### watchOS

- **Be aware of Game Center support on watchOS.**

## Recursos relacionados

- *Related:*
  - [Designing for games](https://developer.apple.com/design/human-interface-guidelines/designing-for-games)
  - [Game controls](https://developer.apple.com/design/human-interface-guidelines/game-controls)
  - [Apple Design Resources](https://developer.apple.com/design/resources/#technologies)
- *Developer documentation:*
  - [GameKit](https://developer.apple.com/documentation/gamekit)
  - [Creating activities for your game](https://developer.apple.com/documentation/gamekit/creating-activities-for-your-game)
  - [Creating engaging challenges from leaderboards](https://developer.apple.com/documentation/gamekit/creating-engaging-challenges-from-leaderboards)
  - [Create games for Apple platforms](https://developer.apple.com/games/)
  - [Game Porting Toolkit](https://developer.apple.com/games/game-porting-toolkit/)

## Vídeos que la explican

- [Get started with Game Center](https://developer.apple.com/videos/play/wwdc2025/214) → `references/videos/2025-214.md`
- [Engage players with the Apple Games app](https://developer.apple.com/videos/play/wwdc2025/215) → `references/videos/2025-215.md`

## Registro de cambios

| Date | Changes |
|---|---|
| June 9, 2025 | Added guidance for new challenges and multiplayer activities, and considerations for the Apple Games app and Game Overlay. Updated guidance and specifications for activity preview images. |
| February 2, 2024 | Added links to developer guidance on using the access point and dashboard in a visionOS game. |
| September 12, 2023 | Added artwork for the iOS achievement layout. |
| May 2, 2023 | Consolidated guidance into one page. |
