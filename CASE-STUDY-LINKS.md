# Ending a paper with a case study

A paper about something Pwavwe Studio built can end with a link to that project's case study on pwavwe.com. The theme shows the link as a card: **Pwavwe Studio case study**, the project's name, its one-line summary and **Read the case study →**.

## Adding the link

1. In the Blogger post editor, switch to **HTML view**.
2. Paste one line at the very end of the post, after the last paragraph and outside any other element:

   ```html
   <p class="case-study-link"><a href="https://pwavwe.com/work/comitia">Read the Comitia case study</a></p>
   ```

3. Change `comitia` to the project's slug from the table below, and the link text to match.
4. Preview the post, then publish or update it.

The link text is what readers see when the theme's styles and script don't run, for example in feed readers and email, so keep it a full phrase such as "Read the Comitia case study".

| Project | Slug | Link |
| --- | --- | --- |
| Comitia | `comitia` | https://pwavwe.com/work/comitia |
| VitaForge AI | `vitaforge-ai` | https://pwavwe.com/work/vitaforge-ai |
| SMG Transport Agency | `smg-transport-agency` | https://pwavwe.com/work/smg-transport-agency |
| UCC SRC App | `ucc-src-app` | https://pwavwe.com/work/ucc-src-app |
| HallKey | `hallkey` | https://pwavwe.com/work/hallkey |
| AZ Learner | `az-learner` | https://pwavwe.com/work/az-learner |

The names and summaries for these six live in the theme script (`caseStudyLinks` in `pwavwe-papers-editorial-theme.xml`), copied from each case study's description on pwavwe.com. If a case study's description changes there, change it in the theme too.

A link to any other `pwavwe.com/work/…` page, such as a future Project Kasena case study, still becomes a card, with the link text as its title and no summary. Add the project to `caseStudyLinks` to give it a name and summary.

## Existing papers that match a case study

These papers are about a project that has a case study:

| Paper | Case study |
| --- | --- |
| [The Election Platform I Never Planned to Build](https://blogs.pwavwe.com/2026/08/election-platform-i-never-planned-to-build.html) | `comitia` |
| [Applied to 20 Jobs and Heard Nothing Back?](https://blogs.pwavwe.com/2026/08/applied-to-20-jobs-and-heard-nothing.html) | `vitaforge-ai` |
| [Building a Product Isn't the Hard Part. Getting Users Is](https://blogs.pwavwe.com/2026/08/building-product-getting-users-folivera.html) | `vitaforge-ai` (its URL uses the old name, Folivera; check the text for it too) |
| [I Vibe-Coded the UCC SRC App](https://blogs.pwavwe.com/2026/07/i-vibe-coded-ucc-src-app-heres-why-i.html) | `ucc-src-app` |

[Are Travel Agencies Dying?](https://blogs.pwavwe.com/2026/08/are-travel-agencies-dying-where.html) may suit `smg-transport-agency` if the paper discusses booking intercity travel online.
