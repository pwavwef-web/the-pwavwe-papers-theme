# Publishing a read version of a paper

## One-time setup

1. Back up the current Blogger theme, then upload `pwavwe-papers-editorial-theme.xml` under **Theme → Restore → Upload**.
2. Update the existing Privacy page in Blogger's HTML view with `privacy-page.html`.

## Two supported players

- **AZ Studio player (current).** Recent papers paste a `<div class="pwavwe-audio-embed">` block whose iframe loads `https://az-studio.web.app/embed/audio/<id>`. The theme moves the first such block into the **Listen to this paper** panel above the text, opens the player in the reader's light/dark theme and keeps it in sync, and resizes the iframe to the height the player reports (up to 600px). The theme now carries the block's styles, so the `<style>` element inside the copied block is optional; older posts that include it still render the same. Paste the block in **HTML view**, as below.
- **SoundCloud (older papers).** Described in the rest of this guide.

The theme displays a **Listen to this paper** panel above the article text when the post contains a SoundCloud player. Its caption is **In Francis Pwavwe's voice.** Papers without a player have no audio panel. No API key or connection between Blogger and ElevenLabs is needed.

## For each paper

1. Finish editing the written paper first. Prepare the narration text: include the title and body, spell out abbreviations or unusual names where needed, and omit navigation, raw URLs and other text that does not make sense aloud.
2. Create an Audio project in ElevenLabs Studio, add that text, and select your saved voice for the narration. Review the complete audio, correct pronunciation or pacing, then **Export** the whole paper as one MP3.
3. Upload the MP3 to SoundCloud as one public track. Use the paper's title, add its cover image, and include the written paper's URL in the track description. Enable embedding in the track's **Permissions** settings.
4. On the track, choose **Share → Embed**. Leave automatic playback off. The standard waveform player is a compact choice; the larger visual player also works. Copy the embed code from **Code & preview**.
5. In the Blogger post editor, switch to **HTML view**. Paste the full embed code on its own line near the start of the post, outside any paragraph, link or other element. Keep the existing article text below it. Do not paste the code into Compose view and do not paste it into the theme XML.
6. Preview the post on desktop and a phone. The theme moves the first SoundCloud player above the article text and adds its heading automatically. Check play, pause, seeking and **Open audio**, then publish or update the post.

Use the same routine to add audio to an older paper. Add only one narration player per paper; the first AZ Studio or SoundCloud player is treated as its read version. Other embedded players remain where you put them. The original iframe still works in the post when the theme's JavaScript is unavailable.

## When a paper changes

Update the narration to match any meaningful edits. Export a new MP3, update the SoundCloud audio if your account supports replacing a track, or upload a new track and replace the old embed code in Blogger. Check playback again after publishing.

## If the player is missing or unavailable

- Confirm that you pasted an `<iframe ... src="https://w.soundcloud.com/player/...">` in **HTML view**, rather than a track link or escaped text such as `&lt;iframe`.
- Check that the SoundCloud track is public, playable and permitted to be embedded. Try **Open audio** if a browser extension blocks the inline player.
- Confirm that the updated theme is installed. Blogger's editor preview can differ from the published post; check the actual post URL as well.

## Reference

- [ElevenLabs Studio: audio projects and exporting](https://elevenlabs.io/docs/eleven-creative/products/studio)
- [SoundCloud: copying embed code and enabling embeds](https://help.soundcloud.com/hc/en-us/articles/115003453587-Embedding-a-track-or-playlist)
