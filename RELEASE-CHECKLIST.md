# Release checklist

The theme and page files are ready locally. Blogger pages do not update from Git automatically, so publish in this order.

For the audio edition update, upload the theme and republish the existing Privacy page. Follow [AUDIO-PUBLISHING.md](AUDIO-PUBLISHING.md) when adding a read version to a paper.

For the theme release of 5 November 2026 (author card, case-study cards, share-preview fixes, a 404 page with search, and comment links that open the discussion), only the theme changes: steps 0–2 below, then the checks under **Author box, case studies and share previews** and **Theme release of 5 November 2026**. No page needs republishing. Follow [CASE-STUDY-LINKS.md](CASE-STUDY-LINKS.md) to end a paper with a case study.

To see which theme the live site runs, use `python scripts/check-theme.py --live`. It compares the `pwavwe-theme-version` stamp in the theme's head with the live site's; a site that predates the stamp reports none.

0. If anything was edited in Blogger's theme editor since the last upload, take **Theme → Backup** and run `python scripts/compare-live.py <downloaded.xml>`. Copy any live-only changes into the local theme first, or the upload will erase them.
1. Commit and push this repository, and merge the release branch into `main`, so the social card (`assets/pwavwe-papers-default-share.jpg`), the author photo (`assets/francis-pwavwe.jpg`) and the Apple touch icon are available at their stable GitHub URLs. The theme loads them from `raw.githubusercontent.com/…/main/assets/`, so they show as broken images until they are on `main`. `python scripts/check-theme.py --live` checks each URL.
2. Set the `pwavwe-theme-version` meta in the theme's head to the release date and run `python scripts/check-theme.py`. It must report **All checks passed**: Blogger rejects a theme that is not well-formed XML, and a script that does not parse breaks the whole page. Then upload `pwavwe-papers-editorial-theme.xml` in Blogger from **Theme → Restore → Upload**.
   - The homepage cards use Blogger's `snippet()` expression for a longer summary. If Blogger refuses to save the theme with an error about `snippet`, replace both `<b:eval expr='snippet(data:post.body, …)'/>` lines in the theme with `<data:post.snippet/>` and upload again. Cards still drop the photo credit and audio text, but most will then show no summary.
3. Republish all five pages in Blogger HTML view, because their styles now come from the theme:
   - `start-here-page.html`
   - `all-papers-page.html`
   - `about-page.html`
   - `contact-page.html`
   - `privacy-page.html`
4. Deploy the create-only newsletter rules with `firebase deploy --only firestore:rules` while authenticated to the `francis-pwavwe` Firebase project.
5. Confirm the email-sending service adds a one-click unsubscribe link to every message. Double opt-in requires that sending service or a Firebase backend function; the public theme deliberately does not pretend to confirm addresses by itself.

## Post-release checks

### Existing behaviour

- At 390px wide, the page must have no horizontal scrollbar and the closed mobile menu must not receive keyboard focus.
- The homepage and Start Here page must not show strings such as `&#8226;`, `&#8212;`, or `&#8594;`.
- Homepage cards should show at most one section and one topic.
- The article comment frame should not load until **Read or leave a comment** is opened.
- Article titles should render as `Article title | The Pwavwe Papers`.
- A paper with a SoundCloud embed should show the **Audio edition** strip above the text, fit the phone screen, and play only when requested. Check **Open audio** as well. A paper without an embed should have no audio strip.
- A paper with an AZ Studio embed (`.pwavwe-audio-embed`) should show it under the **Audio edition** strip above the text, switch the player between light and dark with the theme toggle, and resize the iframe to fit the player with no inner scrollbar.
- On a first visit with no saved choice, the site should follow the device's light/dark setting.
- Test the social card with Facebook Sharing Debugger and LinkedIn Post Inspector after GitHub has cached the new assets.

### Cards and credits

- No homepage card summary contains "Unsplash", "Wikimedia", "Listen to this paper", "ElevenLabs" or a URL. Check page 2 (**Older papers**) as well.
- Papers with an AZ Studio or SoundCloud player show an **Audio edition** badge on their card. Cards no longer repeat "By Francis Pwavwe".
- A paper whose first image has a caption shows that credit under the hero. The body does not repeat the hero image, including posts that open with a bare image (The Moana Effect, the Free AI Programme paper).
- A paper with a Search Description shows it under the title, ending on a full sentence. A paper without one shows nothing there.

### Reading page

- At 1280px the text column is 760px wide and lines up with the author card. At 1024px and 1100px both side rails are visible and the column is at least 640px.
- The contents rail highlights the section being read. At 980px and below, **On this page** appears above the text and the share buttons appear under the author card.
- An audio paper shows **Listen instead** in the byline, which jumps to the player.
- Pressing Tab once on a fresh page shows **Skip to content**.

### Index pages and site chrome

- At 375px the first paper's image is visible without scrolling on the homepage.
- `/search/label/Life` has a single heading, an **Older papers** page has its own short header, and a search with no results says so.
- Search, theme and menu icons look the same on Windows, Android and iOS. The menu icon turns into a close icon while the menu is open.
- In dark mode, white text on filled buttons stays readable (the theme uses `--accent-solid` for fills).
- With search open, Tab stays inside the dialog, and Escape or a click on the backdrop closes it.

### End of a paper

- The order is: case-study card (when the paper has one), author and newsletter card, **Continue reading**, newer/older links, comments. The site footer has no second newsletter form on a paper but keeps it on the homepage and pages.
- A test sign-up replaces the form with "You are in — thanks for subscribing." Firestore still receives `{email, source, status, timestamp}`.

### Author box, case studies and share previews

- Every paper ends with the author card: photo, the bio that starts "Francis Pwavwe builds websites, web applications and AI-assisted systems from Cape Coast, Ghana", and the links **Portfolio at pwavwe.com →** (https://pwavwe.com/) and **Work with Pwavwe Studio →** (https://pwavwe.com/studio). At 390px the photo sits above the bio.
- The byline's **Francis Pwavwe** links to https://pwavwe.com/.
- A paper ending in a `case-study-link` paragraph shows the case-study card above the author card, with the project's name and summary. Check The Election Platform I Never Planned to Build once its Comitia link is added.
- View the source of a paper with an image: it has exactly one `og:image` (a `lh3.googleusercontent.com/blogger_img_proxy/…` or `blogger.googleusercontent.com/…/w1200-h630-…` URL) and no `twitter:image`. The homepage and an image-less paper end with `pwavwe-papers-default-share.jpg`.
- Paste a paper's URL into Facebook Sharing Debugger, LinkedIn Post Inspector and a WhatsApp chat to yourself. Each shows the title, description and image. Use **Scrape Again** in the Facebook debugger to replace its cached preview.
- Rich Results Test on a paper finds a BlogPosting whose author is Francis Pwavwe with `@id` https://pwavwe.com/#francis.

### Theme release of 5 November 2026

- `python scripts/check-theme.py --live` reports the live theme version as `2026-11-05`.
- Open a comment's link from Blogger's comment email or the comments feed (it ends in `?showComment=…#c…`). The paper opens with **Read or leave a comment** expanded and that comment just below the header. A paper URL ending in `#comments` opens the discussion too. A plain paper URL still keeps the comments closed.
- An address that does not exist, such as `/no-such-paper.html`, shows **This page wandered off.** as its heading, a search box that returns results, and **Homepage** and **All papers** buttons. The browser tab reads **Page not found | The Pwavwe Papers**. At 390px the search box and button fit on one line.
- After a test sign-up, the same address in the same browser says it is already on the list, and a different address can still subscribe.

### Share previews that need a fix in Blogger, not the theme

Checked against the live site on 2 November 2026; the homepage description rechecked on 5 November.

- **Set the blog's search description** in **Settings → Meta tags**: turn on **Enable search description**, then fill in **Search description**. Blogger prints it as the homepage's `og:description`. Today that tag is empty and comes before the theme's generic fallback, so a shared homepage link may show no summary. (**Settings → Basic → Description** is a different field: it is already set and is the homepage headline, "The Things That Matter".) After saving, open a paper that has no Search Description of its own and check that no standfirst appears under its title.
- **Add a Search Description** (post editor → **Post settings → Search Description**) to these papers. Without one, Blogger prints an empty `og:description` ahead of the theme's site-wide line, so Facebook and LinkedIn may show no summary. Each is at `blogs.pwavwe.com/<year>/<month>/<slug>.html`:
  - 2026/04 what-does-tourism-management-degree
  - 2026/06 echoes-of-1999-is-generative-ai-boom, life-game-or-play
  - 2026/07 6-wholesome-reddit-stories-i-read-today, atheism-is-not-one-thing-stop-judging, everything-you-need-to-know-about, ghanas-education-system-must-teach, i-am-leaving-ucc-with-one-big-lesson, i-vibe-coded-ucc-src-app-heres-why-i, preparing-for-national-service-in-ghana, stop-breaking-world-we-still-have-to, stupid-financial-traps-young-people, the-business-model-is-unhinged-checkout, the-many-rooms-of-reality-how, the-worlds-top-ai-models-today-what, too-small-to-matter-too-big-to-ignore, what-life-gives-you-when-you-finally, why-ghana-is-one-of-africas-most
  - 2026/08 applied-to-20-jobs-and-heard-nothing, what-actually-sells-these-days-lessons
  - 2026/09 the-moana-effect-when-boat-outgrows
  - 2026/10 three-bible-stories-we-only-call-normal
- **Make the first image smaller** on these papers. Their share image is over 300 KB, and WhatsApp often drops a preview image that large. Re-upload the first image as a JPEG (most are PNG screenshots or illustrations), or put a smaller image first:
  - 2026/04 what-does-tourism-management-degree (1.3 MB PNG)
  - 2026/07 the-business-model-is-unhinged-checkout (506 KB PNG), the-many-rooms-of-reality-how (313 KB), what-life-gives-you-when-you-finally (965 KB PNG)
  - 2026/08 are-travel-agencies-dying-where (1.0 MB PNG), the-product-doesnt-exist-until-people (524 KB PNG), your-tiktok-feed-is-rewriting-your (1.0 MB PNG)
  - 2026/10 low-resource-language-does-not-mean-low-people (378 KB), zoeys-racism-episode-tonight-i-understand (347 KB)
- **2026/07 preparing-for-national-service-in-ghana**: Blogger's copy of its first image (a Wikimedia photo) returns 404, so it shares without an image. Upload the photo to Blogger, or replace it.

### Pages

- Contact's **Write a message** button is white text on the dark red fill.
- All Papers titles are dark ink, turning red on hover. Filtering for "AI" finds the Artificial Intelligence papers, and a filter with no matches says so.
- No page shows a byline, "A short read" or an empty bordered strip under the text. Each page ends with links onward.
