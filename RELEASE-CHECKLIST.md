# Release checklist

The theme and page files are ready locally. Blogger pages do not update from Git automatically, so publish in this order.

For the audio edition update, upload the theme and republish the existing Privacy page. Follow [AUDIO-PUBLISHING.md](AUDIO-PUBLISHING.md) when adding a read version to a paper.

0. If anything was edited in Blogger's theme editor since the last upload, take **Theme → Backup** and run `python scripts/compare-live.py <downloaded.xml>`. Copy any live-only changes into the local theme first, or the upload will erase them.
1. Commit and push this repository so the social card and Apple touch icon are available at their stable GitHub URLs.
2. In Blogger, upload `pwavwe-papers-editorial-theme.xml` from **Theme → Restore → Upload**.
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

- The order is: author and newsletter card, **Continue reading**, newer/older links, comments. The site footer has no second newsletter form on a paper but keeps it on the homepage and pages.
- A test sign-up replaces the form with "You are in — thanks for subscribing." Firestore still receives `{email, source, status, timestamp}`.

### Pages

- Contact's **Write a message** button is white text on the dark red fill.
- All Papers titles are dark ink, turning red on hover. Filtering for "AI" finds the Artificial Intelligence papers, and a filter with no matches says so.
- No page shows a byline, "A short read" or an empty bordered strip under the text. Each page ends with links onward.
