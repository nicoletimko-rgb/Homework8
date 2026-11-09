# Iteration: Improving `no-rewrite` Review Depth

## What went wrong

My initial `no-rewrite` skill focused on identifying which files a coding agent changed and whether those file changes matched my request. I realized that a file-level summary was not specific enough for the kind of review I wanted. For example, when adding a height clue to my NBA guessing game, `script.js` contained both the new clue logic and existing functions for scoring, animations, and guessing. A review that only says `script.js` was modified to add height could overlook an unrelated change inside that same file.

**Evidence boundary:** This describes a weakness I identified in the original review instructions, not a confirmed missed change in the checker output. The checker report I obtained did discuss individual functions and scoring changes.

## Diagnosis

The original instructions emphasized comparing files but did not make the required depth of analysis explicit enough. A file can contain a mixture of requested changes, necessary supporting changes, and unrelated changes. Treating the whole file as one unit makes it harder to see those differences and their effects on existing functionality.

## What I changed

I revised `SKILL.md` to require the checker to identify every affected function, method, variable, event listener, and other relevant code component within each changed file. It must explain the purpose of each change, compare before-and-after behavior, consider indirect effects, and classify changes individually as **Requested**, **Necessary**, **Outside Scope**, or **Unclear**. I also specified that HTML, CSS, configuration, and other non-function changes must be reviewed.

## Rerun and result

The available `no-rewrite` review of the height-clue implementation shows the level of detail I wanted: it separately discusses `getClues()`, `updateReadouts()`, `checkGuess()`, scoring constants, shot positions, and effects on `revealClue()` and `missShot()`. It also flags the change to the final available score as an **Unclear** decision rather than automatically approving it.

I cannot establish from the available evidence that this report was produced **after** the revision, so it should not be presented as a verified before-and-after retest. To complete that part of the iteration, I would run the same review in a fresh Codex session using the revised skill and compare its function-level findings against the earlier output.
