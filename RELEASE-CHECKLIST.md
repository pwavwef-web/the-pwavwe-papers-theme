# Release checklist

The theme and page files are ready locally. Blogger pages do not update from Git automatically, so publish in this order.

For the audio edition update, upload the theme and republish the existing Privacy page. Follow [AUDIO-PUBLISHING.md](AUDIO-PUBLISHING.md) when adding a read version to a paper.

0. If anything was edited in Blogger's theme editor since the last upload, take **Theme → Backup** and run `python scripts/compare-live.py <downloaded.xml>`. Copy any live-only changes into the local theme first, or the upload will erase them.
1. Commit and push this repository so the social card and Apple touch icon are available at their stable GitHub URLs.
2. In Blogger, upload `pwavwe-papers-editorial-theme.xml` from **Theme → Restore → Upload**.
3. Republish these pages in Blogger HTML view:
   - `start-here-page.html`
   - `all-papers-page.html`
   - `privacy-page.html`
4. Deploy the create-only newsletter rules with `firebase deploy --only firestore:rules` while authenticated to the `francis-pwavwe` Firebase project.
5. Confirm the email-sending service adds a one-click unsubscribe link to every message. Double opt-in requires that sending service or a Firebase backend function; the public theme deliberately does not pretend to confirm addresses by itself.

## Post-release checks

- At 390px wide, the page must have no horizontal scrollbar and the closed mobile menu must not receive keyboard focus.
- The homepage and Start Here page must not show strings such as `&#8226;`, `&#8212;`, or `&#8594;`.
- Homepage cards should show at most one section and one topic.
- The article comment frame should not load until **Read or leave a comment** is opened.
- Article titles should render as `Article title | The Pwavwe Papers`.
- A paper with a SoundCloud embed should show **Listen to this paper** above the text, fit the phone screen, and play only when requested. Check **Open audio** as well. A paper without an embed should have no audio panel.
- A paper with an AZ Studio embed (`.pwavwe-audio-embed`) should show it inside **Listen to this paper** above the text, switch the player between light and dark with the theme toggle, and resize the iframe to fit the player with no inner scrollbar.
- On a first visit with no saved choice, the site should follow the device's light/dark setting.
- Test the social card with Facebook Sharing Debugger and LinkedIn Post Inspector after GitHub has cached the new assets.
