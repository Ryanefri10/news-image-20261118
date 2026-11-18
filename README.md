[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Ryanefri10/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Ryanefri10/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Built for the [make.fun bounty — Sum up 18 November's world news in one image](https://make.fun/bounty/news-image-20261118).

# news-image-20261118 — The World in One Image: Wednesday 18 November 2026

A newspaper front page summing up Wednesday 18 November 2026 world news
in one image: an AI-generated dusk photograph — a collapsed sea-bridge
arch, a burning tanker below it, fighter jets overhead — with a masthead
and five verified headlines plus an ALSO ticker, typeset crisply so the
AI judge can read every word (no AI-generated text, so nothing is
garbled).

## Stories depicted (all reported on 17–18 November 2026)

- **UKRAINE — Crimea bridge falls into the sea.** Ukraine struck the
  Kerch (Crimean) Bridge for a second day running; a road span and its
  arch collapsed into the strait, severing the road link; 1,441 drones
  in what Russia called the largest Ukrainian drone attack of the war.
  President Zelenskyy hailed an "unprecedented operation". Russia hit
  Kyiv's bridges in reply. (CNN, 17 Nov; Reuters, 17 Nov; NY Post,
  17 Nov.)
- **MANILA — Trump lands for Quad summit.** President Trump arrived in
  Manila for the first Quad leaders' summit in two years (US, Japan,
  India, Australia); he meets President Marcos Jr. on Wednesday, then
  heads to Shenzhen, where a trilateral with Xi Jinping and Vladimir
  Putin on nuclear arms is set for Thursday. (Reuters, 17 Nov; NY Post,
  17 Nov.)
- **BAHRAIN — Iran strikes US radar again.** The IRGC said it hit a US
  radar at the Sheikh Isa airbase — the third drone attack on US targets
  in Bahrain in five days. US Central Command said the drones were
  intercepted with no damage to US equipment and no injuries. (Al
  Jazeera, 17 Nov; CBS News, 17 Nov.)
- **LONDON — UK sanctions settlement firms.** Britain froze the assets
  of eight Israeli construction firms building West Bank settlements and
  sanctioned the Tzav 9 activist group, which blocks Gaza aid trucks.
  Foreign Secretary Ed Miliband: "do not bid, do not build, and do not
  profit from the destruction of the two-state solution." (Reuters,
  17 Nov.)
- **BAY OF BENGAL — Cyclone Akvan bears down.** The storm intensified
  into a Severe Cyclonic Storm and is forecast to cross the Andhra
  Pradesh coast around noon on Friday 20 November as a very severe
  cyclonic storm, with 120–130 km/h winds gusting to 145 km/h. (India
  Meteorological Department bulletins, 17 Nov.)

Plus an ALSO ticker: Canada and China extending trade deals as Xi meets
Prime Minister Carney ahead of the APEC summit; Russia pounding Kyiv's
bridges, cutting power and water; MS Dhoni retiring from the IPL to
mentor Chennai Super Kings. (Jagran Josh / Times of India 18 Nov
digests; Reuters via BusinessWorld.)

## Entry

`main.py` (Python 3.13, standard library only — hashlib, os, shutil,
struct) copies the vendored image `entry.png` — a whole PNG, 1024x1024,
898,029 bytes — to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`). It
verifies the vendored file against its embedded expected sha256 before
copying, and checks the copy is a whole PNG within the size/dimension
limits and byte-identical to the source.

Build provenance: `hero.png` is the AI-generated photo (no text);
`compose.py` is the build-time compositor (PIL, build time only — not
part of the graded entry) that laid out the masthead, headlines and
ticker over it.

## Checks (pre-verified twice)

```sh
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 python3 main.py   # wrote out1/entry.png (898029 bytes, 1024x1024)
MAKEFUN_OUTPUT_DIR=out2 python3 main.py   # wrote out2/entry.png (898029 bytes, 1024x1024)
sha256sum out1/entry.png out2/entry.png entry.png
```

- Run 1 sha256: `441d938761aac3d510212515ac4357f1ee1592e5848bc969e7820541acbec308`
- Run 2 sha256: `441d938761aac3d510212515ac4357f1ee1592e5848bc969e7820541acbec308`
- Vendored `entry.png` sha256: same — all three identical.
- Size 898,029 bytes (≤ 1 MiB ✓), dimensions 1024x1024 (✓).
- `main.py` written, run, then genuinely edited (embedded expected-hash
  source check added) and re-run twice — revision requirement satisfied.
- Also verified under `python3 -O` (checks use explicit raises, not
  asserts).

## Status

Built and verified 18 Nov 2026 ~07:15 WIB. **NOT submitted** — per the
standing pre-submit rule, the built entry is reported first and waits
for the user's go. Competition `news-image-20261118`, FREE, AI-judge
pairwise, $250 pot shared by top 50, deadline 20 Nov 2026 00:00 UTC
(07:00 WIB).

## License

GPL-3.0-only — see LICENSE.
