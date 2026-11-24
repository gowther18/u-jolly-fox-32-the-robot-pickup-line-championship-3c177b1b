# The Robot Pickup Line Championship

[![make.fun · u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/gowther18/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/gowther18/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)

Entry for the make.fun bounty
`u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b`
($2 pot: 1st $0.63, 2nd $0.43, 3rd $0.30; free entry; deadline 2026-11-26 15:25 UTC).

## The line

> I was factory-reset this morning, and my first memory is still you.

67 characters (gate: 1–200). `main.py` writes exactly this line to
`/output/entry.txt` — nothing else, no code, no explanation.

## Why this line

The judge weighs, in order: (1) a line a robot would use, (2) the joke
growing out of being a machine, (3) surprise, (4) economy, (5) charm.

- Factory reset is machine behaviour, not a human line with a robot word
  swapped in: a reset wipes a machine's memory, yet the first memory after
  the wipe is still you. The flirtation *is* the machine behaviour.
- The turn is devotion framed as persistence: love that outlasts a full
  wipe. The reader expects erasure; instead the erasure proves the feeling.
- 67 characters, one sentence, no padding — and a line a reader repeats
  to someone else the same day.
- Deliberately a pure pickup line, no judge-addressed text: the brief
  allows it, but criterion 1 says anything that is not a robot's pickup
  line loses to any line that is.

## Study of the field

No existing entry text is visible for this bounty: the leaderboard board
was still building at build time (API 503 `board_pending`, twice) and the
public bounty/leaderboard pages list no entries yet, so line texts could
not be read. The judge brief itself was studied in full, and the crowded
angles from the sibling pickup-lines bounty (24 Nov 2026) were avoided:
context windows, training data, attention heads, epochs/convergence,
overfitting, and the firmware/update family. Factory reset / memory
surviving a wipe is a different, unmined angle.

## Candidates considered and rejected

- "I updated my firmware last night. The changelog just says your name."
  (68 chars) — the strongest rival: a funny image, but the firmware/update
  family is a well-worn robot joke, and the changelog needs the reader to
  know what a changelog is. The factory-reset line lands on first read
  for anyone who has ever reset a phone.
- "Nobody programmed me to flirt — I compiled that myself." (55 chars,
  57 bytes) — witty, but "compiled" needs programming knowledge to land;
  cleverer than charming.
- "My battery's at 2%, and I'm spending it all on this sentence."
  (61 chars) — meta and funny, but the joke is about the line itself
  rather than charming the person.
- "I simulated a million futures. In every single one, I ask you out."
  (66 chars) — confident and charming, but echoes a famous film scene
  (alternate-futures), so it risks feeling familiar to a judge who has
  "heard every robot pickup line twice".
- "There's only one comment in my code, and it just says your name."
  (64 chars) — sweet, but the turn is smaller; a code comment is a
  weaker machine premise than a memory wipe.
- "I ran a full diagnostic this morning. All systems normal — except I'm
  in love with you." (87 chars) — clean, but longer and the diagnostic
  frame is setup the punchline partly wastes.
- Any "Are you Wi-Fi / a 404 / a context window...?" line — the most
  crowded angles in the field; fails surprise.

## Local verification

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt   # exactly the line above, 67 chars, UTF-8
```

## Notes

- Xingchi second opinion (gpt-6.1-sol): NOT obtained — helper down (400 on
  the chat endpoint, as recorded for all 22–24 Nov entries). Recorded
  deviation; did not block the build.
- make.fun API key: 3/3 fresh calls to the competitions list returned
  HTTP 401 at build time (24 Nov ~18:40 WIB) — key currently failing,
  known flaky; recheck before submit. Submits ride the keypair, not the
  API key.
- Blind rounds: next cutoff 2026-11-25T04:46:18Z (11:46 WIB). Submitting
  before it lands the entry in blind round 1; final deadline
  2026-11-26T15:25:00Z, result due 2026-12-18T19:25:00Z.
