# Sonnatt Studio

Our own AI video studio for Sonnatt.ai client work. Runs on your own machine at `http://localhost:4747`; it is **not** published with the website (the Pages workflow excludes `studio/`).

## What it does
**Brief → Claude writes script + character → image model makes the character → video model animates each shot → ElevenLabs voices it → ffmpeg assembles** (captions, branded outro, music bed) → MP4 + `.srt`.

- **Autopilot**: one button fills in whatever is missing and assembles the video. Re-run it after a failure; finished steps are kept. Failed provider calls retry automatically.
- **Pick the model per project or per shot**: Seedance 1 Pro/Lite, Kling 2.1, Hailuo 02, Veo 3, Luma Ray 2 (all through one fal.ai key), plus any custom provider.
- **Takes**: every "New take" is kept; click a take number to choose the one that goes in the final cut.
- **Brand kits per client**: voice/tone for scripts, do's and don'ts, default models, ElevenLabs voice, logo, outro text/colour, background music.
- **Own character image**: upload a client's real mascot or product image instead of generating one.
- **Settings tab**: paste API keys once (saved to `data/settings.json`, mode 600, git-ignored; never sent back to the browser).
- Any provider without a key runs in **demo mode** (placeholder images, silent audio), so the whole flow can be tried free. The header shows live/demo per provider.

## Run
Needs Node 22+ and ffmpeg.

    cd studio
    npm start        # then open http://localhost:4747 and add keys in Settings
    npm test         # offline end-to-end check in demo mode

Keys can also come from environment variables / `.env` (see `.env.example`).

## Adding Higgsfield (or any other video API)
Higgsfield isn't built in because its API details must come from its own docs. Copy `providers.example.json` to `data/providers.json`, fill in the URLs, request body and response paths, add the key in Settings, and it appears in the model lists as "(custom)". The adapter handles submit → poll → download generically.

## Honest status
- Tested end to end offline (demo mode), including the UI, brand outro, takes and the local-request guard.
- **Not yet tested with real keys**: the live Claude, fal.ai and ElevenLabs calls follow the public docs, but model ids and parameters change often. Run one short test per model first; if one is rejected, adjust its entry in `lib/registry.js` (ids are in one place).
- Seedance and Kling clips from image-to-video don't lip-sync the voice; the audio is laid over the clip. A lip-sync step would be the next upgrade.

## Safety
- The server only accepts requests from `localhost` and the studio page itself, because it holds keys and spends money. Don't expose it to the internet without adding real login.
- Only generate real people's likeness with their written consent, and label AI content as platforms require.
- Never commit `data/` or `.env`.
