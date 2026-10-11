<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="Josh Lucem, plugins for Minecraft" src="assets/banner-dark.svg" width="100%">
</picture>

[![Website](https://img.shields.io/badge/website-joshlucem.github.io-141416?style=for-the-badge)](https://joshlucem.github.io)
[![Modrinth](https://img.shields.io/badge/Modrinth-joshlucem-1bd96a?style=for-the-badge&logo=modrinth&logoColor=white)](https://modrinth.com/user/joshlucem)
[![SpigotMC](https://img.shields.io/badge/SpigotMC-joshlucem-ed8106?style=for-the-badge&logo=spigotmc&logoColor=white)](https://www.spigotmc.org/members/joshlucem.2418115/)

</div>

Hello, I'm Josh. I'm from Lima, I study Law and Political Science, and in my spare time I make plugins for Minecraft servers. I write them in Java for Paper, simply because it's where I feel most at home, and I like to finish them properly before I share them, with the source open, a guide in English and Spanish, and the right licence.

The legal side of all this interests me just as much. I've always been fascinated by anything to do with justice, so now and then I help small communities and projects with their rules and licences.[^1]

> [!NOTE]
> I'm finishing **Skywave** at the moment. It works and it has been tested, I just need an icon, some screenshots and a page for it before I can release it.

## What I've made

| Project | Status | Built with | What it does |
| :-- | :-: | :-- | :-- |
| [**Skylease**](https://github.com/joshlucem/Skylease) | Released | Paper 1.21+, Java 21 | Gives every player their own flight time. `/fly` starts it, the time runs down while they fly, and when it's gone they glide to the ground instead of dropping. |
| **Skywave** | In development | Paper 1.21+, Java 21 | A radio for survival servers that works only with commands. How far the signal reaches depends on your height, the weather and whether you have a roof over you. |
| Community bots | Private | Node.js, Discord.js | Two bots I wrote for a poetry community on Discord, one for events and minigames with a leaderboard and one for anonymous poems. |

<details>
<summary><b>More about Skylease</b></summary>

<br>

- 33 particle effects, each with its own permission
- A WorldGuard flag to forbid flying in certain regions
- PlaceholderAPI support
- SQLite out of the box, or MySQL and MariaDB if you want to share data between servers
- English and Spanish, with room for your own language

</details>

## How I release a plugin

```mermaid
flowchart LR
    A([Idea]) --> B[Write it]
    B --> C[Tests]
    C --> D[Try it with two players]
    D --> E[Icon, screenshots, page]
    E --> F([Release with its licence])
    D -. something breaks .-> B
```

## Legal help

When a community or a project needs paperwork, I can help with the following.

- [x] Rules for a Discord community, including privacy notice and minimum age
- [x] Choosing a software licence and writing a plain summary for the README
- [ ] Commissions between server owners and developers, code assignments and NDAs, whenever someone asks

<details>
<summary><b>What I work with</b></summary>

<br>

| | |
| :-- | :-- |
| Languages | Java, JavaScript, HTML, CSS |
| Platforms | Paper, Spigot, Node.js |
| Tools | Git, Maven, YAML and JSON |

</details>

---

<div align="center">

<sub>Press <kbd>T</kbd> on [my website](https://joshlucem.github.io) and see what happens.</sub>

</div>

[^1]: I'm not a qualified lawyer yet, so if something needs a real one I'll tell you.
