# The Pwavwe Papers theme

The Blogger theme and page bodies for [The Pwavwe Papers](https://blogs.pwavwe.com/), Francis Pwavwe's blog. This repository is the source of truth: Blogger does not read from Git, so changes reach the site only when the theme is uploaded and the pages are republished by hand.

## What is here

| File | What it is |
| --- | --- |
| `pwavwe-papers-editorial-theme.xml` | The whole theme: layout, styles and scripts. Uploaded under **Theme → Restore**. |
| `start-here-page.html`, `all-papers-page.html`, `about-page.html`, `contact-page.html`, `privacy-page.html` | The bodies of the five Blogger pages at `/p/<name>.html`, pasted in the page editor's HTML view. Their styles come from the theme. |
| `assets/` | The site-wide share card, the author photo and the Apple touch icon. The theme loads them from this repository's `main` branch on GitHub. |
| `firestore.rules`, `firebase.json`, `.firebaserc` | Rules for the newsletter's `subscribers` collection in the `francis-pwavwe` Firebase project. The public site may only add a sign-up of the exact shape `{email, source, status, timestamp}`. |
| `scripts/check-theme.py` | Checks the theme before an upload; `--live` also reports which theme version the live site runs. |
| `scripts/compare-live.py` | Lists changes made in Blogger's theme editor that the local theme lacks. |

## Guides

- [RELEASE-CHECKLIST.md](RELEASE-CHECKLIST.md): how to publish a change, and what to check afterwards.
- [AUDIO-PUBLISHING.md](AUDIO-PUBLISHING.md): adding the audio edition of a paper.
- [CASE-STUDY-LINKS.md](CASE-STUDY-LINKS.md): ending a paper with a Pwavwe Studio case study.

## Before every upload

```bash
python scripts/check-theme.py --live
```

Edit the theme here rather than in Blogger's theme editor. If someone did edit it there, back up the live theme and run `scripts/compare-live.py` first, or the upload will undo their change.
