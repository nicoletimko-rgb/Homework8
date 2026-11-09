# Demonstration: checking changes to my NBA guessing game

## What real task I used it on

I used my NBA guessing game, APIAPP repository, to demonstrate my NBA API Explorer MCP tool and my `no-rewrite` checker skill. The game loads data from an NBA API, and lets users guess an NBA player, reveal clues at a decreasing point value, and watch a basketball move toward the hoop. Correct guesses make the shot, and giving up misses it.

I wanted to add height and country as clues while keeping the existing game functionality. I saved the original five-clue game in `before/` so the checker could identify what the agent changed. The original clues were position, jersey number, draft year, college, and NBA team.

Before making changes, I asked the agent to inspect the API through my MCP tool. It reported 525 players and 27 fields, including `HEIGHT` and `COUNTRY`. I then used those fields for the feature requests below.

## Run 1: adding height

### Trimmed transcript

**Me:**
> What fields are returned by my `inspect_nba_players` MCP tool.

> Add player height as a clue in the starter NBA guessing game.

**Agent:**
> The game currently has five clues, and its saved player data omits height. I’ll add height as the second clue, update the data generator to keep `HEIGHT`, and extend the score and shot indicators to six clues.

**What the agent did:**

- Added `height` from the API's `HEIGHT` field to `create_players.py`.
- Added height as the second clue in `getClues()`, formatting values such as `6-8` as `6 ft 8 in`.
- Extended the score and readout tables and added a basketball position for the sixth clue.
- Updated the HTML clue counter and score ticks, CSS space for clue rows, and README instructions.
- Replaced hardcoded five-clue checks with the actual clue count.

**Agent, excerpt from its final response:**
> Added height as the second of six clues, mapping API `HEIGHT` values such as `6-8` to `6 ft 8 in`. Updated scoring, clue counters, and shot progression. Logic and syntax checks passed.

**Me, in a separate checker chat:**
> Use my … no-rewrite … skill to independently review the changes in the game compared to the `/before` files. The update was adding height as a clue.

### What the checker caught

The checker identified all five modified files and explained how the changes supported the height clue:

| File | Changes identified by the checker |
|---|---|
| `create_players.py` | The player-building loop now includes `height` from `HEIGHT`. |
| `script.js` | `getClues()` adds height second and formats feet/inches; `shotPositions` adds an intermediate descending position; `SCORES`, `CERTAINTY`, `ARC_PCT`, and `DECAY` expand for six clues. |
| `index.html` | The clue denominator changes from `/5` to `/6`, and the score meter gains a sixth tick. |
| `style.css` | The clue area's minimum height increases from 145 px to 174 px to reserve six rows. |
| `README.md` | The instructions describe six clues, the `HEIGHT` field, and height formatting. |

It also caught less obvious behavior changes: `updateReadouts()` now calculates the clue total dynamically, and the delayed callback in `checkGuess()` recognizes the final clue dynamically instead of assuming clue five. The extra shot position affects ball movement, trajectory drawing, and the remaining miss animation even though those functions were not rewritten.


## Run 2: adding country

### Trimmed transcript

I next tested the same process again but by adding a different feature as a clue.

**Me:**
> What fields are returned by my `inspect_nba_players` MCP tool.

> I want to add **country as a clue** to my NBA guessing game.

**Agent:**
> I’ll add country to the player data and clue sequence, and update the scoring and shot progression for a seventh clue.

**What the agent did:**

- Added `country` from the API's `COUNTRY` field to `create_players.py`.
- Added country as the sixth clue, before NBA team.
- Extended the score/readout tables and basketball positions to seven clues.
- Updated HTML counters and ticks, CSS space for seven rows, and README instructions.

**Agent, excerpt from its final response:**
> Added **COUNTRY** as the sixth clue, before team. Updated the counter, scoring, and animation for seven clues; the final clue leaves 25 points.

**Me, in a separate checker chat:**
> Use my … no-rewrite … skill to independently review the changes in the game compared to the `/before` files The update was adding country as a clue

### What the checker caught

The checker identified the country addition and traced its supporting changes across the same five files:

| File | Changes identified by the checker |
|---|---|
| `create_players.py` | The player-building loop now includes `country` from `COUNTRY`, alongside the previously added height field. |
| `script.js` | `getClues()` adds country before team; shot positions and the four readout tables expand to seven clues; the final available score becomes 25 points. |
| `index.html` | The clue denominator becomes `/7`, and the score meter contains seven ticks. |
| `style.css` | The clue area's minimum height becomes 203 px to reserve seven rows. |
| `README.md` | The instructions describe country, its position in the sequence, seven clues, and the 25-point final reward. |

It also explained the cumulative gameplay effect: the team clue moved from fifth to seventh, its available reward changed from 100 to 25 points, and an early give-up animation could traverse two additional clue positions, adding up to 900 ms before the rebound.

Because both reviews used the original `before/` snapshot, the second review also detected the earlier height edits. It classified those as outside the country-only request. Those were separately requested changes; their appearance in this review shows that the checker was reporting the full difference from the original baseline rather than only the most recent edit.

## Do I Agree?

I agree with with the outputs the checker gave. After playing the game multiple times during the testing stage when I was creating the project, the check covered all the aspects that would be changed by adding another clue (points, path of the ball, scoring denominator, clue area visual formatting, etc). It also put it in simple language that I understood, as desired.