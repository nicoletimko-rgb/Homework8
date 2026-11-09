---
name: no-rewrite
description: Automatically review before-and-after versions of files whenever an agent creates, edits, fixes, or adds code functionality. Explain every file, function, and behavior changed, compare changes against the user's original request, and flag unrelated or unauthorized modifications. Use after every coding change or when asked to review modified files.
---

# No Rewrite — Change Review

## Purpose
After every coding task, compare the original input files with the modified output files. Explain what changed, how functionality was affected, and whether any modifications exceeded the user's request.

Focus on code and behavior. Never modify files during the review.

## 1. Before Implementation
- Identify the user's request and intended functionality.
- Read and preserve the original contents of files being modified.
- Identify existing behavior that should remain unchanged.

## 2. Review Files and Functionality
After implementation, compare each original file with its modified version.

For EVERY created, modified, or deleted file:
- Identify the file name and changes made.
- Explain what was added, removed, or modified and why.
- Identify EVERY affected function, method, variable, event listener, or other code component.
- Explain each affected function's purpose and before/after behavior.
- Describe changes to inputs, outputs, calculations, defaults, errors, and side effects.
- Explain new, removed, or altered functionality.
- Identify effects on existing functionality and other parts of the application.
- Distinguish cosmetic changes from functional changes.
- Include HTML, CSS, configuration, and non-function code changes.
- Do not report unchanged code unless its behavior is affected.

## 3. Identify Unrequested Changes
Compare every substantive change against the user's original request.

Classify changes as:
- **Requested:** Directly implements the user's request.
- **Necessary:** Required to support the requested functionality.
- **Outside Scope:** Unrelated or unnecessary modification.
- **Unclear:** Insufficient evidence to determine necessity.

For every outside-scope change, explain what changed, why it was unnecessary, its consequences, and whether it should be reversed. Do not invent violations or automatically undo changes.

## 4. Required Output Format

# No Rewrite — Change Review

### 1. Original Request
Summarize what the user asked for.

### 2. Files and Functionality Changed
For each changed file:
- **File:** Name and whether created, modified, or deleted.
- **Changes:** All added, removed, or modified code, including affected functions.
- **Functions:** Each affected function's purpose and before/after behavior.
- **Functionality:** New, removed, or changed application behavior.
- **Reason:** Why each change was made and its scope classification.

### 3. Before vs. After
Summarize how application functionality differs from the original version.

### 4. Changes Outside the Request
Identify unrelated changes, consequences, and recommendations. Explicitly state if none were found.

## Rules
- Use simple language and identify every affected function by name.
- Include file paths and line numbers when available.
- Never omit evidenced file or functionality changes.
- Do not modify or revert files during the review without permission.
- State when original files or comparison evidence are unavailable.
- Provide Python or R examples only when helpful.
- Run automatically after every coding task involving file modifications.
