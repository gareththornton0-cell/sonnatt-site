# Sonnatt Studio

Local tool for making AI character/mascot videos for Sonnatt.ai clients. Runs on your own machine; it is **not** published with the website.

## Pipeline
Client project → **Claude** writes character + shot list → **fal.ai** (Flux) makes the character image → **fal.ai** (Kling image-to-video) animates each shot → **ElevenLabs** voices the dialogue → **ffmpeg** stitches shots, burns captions, exports MP4 + `.srt`.

## Run
Needs Node 22+ and ffmpeg.

    cd studio
    cp .env.example .env     # add your API keys
    npm start                # http://localhost:4747

Any step without a key runs in **demo mode** (placeholder card images, silent audio) so you can try the whole flow free. The header shows live/demo per provider.

Output is saved in `studio/data/<client>/<project>/` (git-ignored).

## Notes
- fal.ai model ids change often. Set `FAL_IMAGE_MODEL` / `FAL_VIDEO_MODEL` in `.env`; the video request sends `prompt`, `image_url`, `duration`, `aspect_ratio` (Kling-style), so other models may need small tweaks in `lib/providers.js`.
- The live provider calls (Claude, fal.ai, ElevenLabs) are written from their public docs but have not been run against real keys yet. Test with one short project first.
- Only create content of real people with their written consent, and label AI content as the platforms require.
- Never commit `.env`. The website publish workflow excludes `studio/`.
