# Checker Skill and NBA API MCP Server

This project contains two tools I built that were tested using my Guess the NBA Player web game from HW3:

## 1. Checker Skill

### What is does 

**`no-rewrite`**, a checker skill that instructs the coding agent to compare the original files with the files after a coding task. It identifies which files, functions, variables, event listeners, and other code components changed, explains how those changes affect functionality, and checks whether each change followed what was requested to be changed and if any change was out of the scope of what was wanted. The checker reports findings without editing or reverting files

### What Motivated Each (from Prompt Logs)

I repeatedly found myself reminding coding agents to make only the changes I requested. Two examples from my prompt logs are:

> “do not change any other aspect but this without asking me. and if you do not understand, ask” (from Crossy Road HW)

> “DO NOT CHANGE ANY OTHER FUNCTIONALITY” (From Guess the NBA Player HW)

These repeated instructions showed that I wanted a more consistent way to check for unintended changes instead of manually repeating the same warning in every prompt. The skill turns that preference into a reusable review process.

### Installation

Place the skill file at:

```text
~/.codex/skills/no-rewrite/SKILL.md
```

On macOS, `~` refers to your home directory. For example, the expanded path would be `/Users/<YOUR_USERNAME>/.agents/skills/no-rewrite/SKILL.md` (**machine-specific**).

Create the directory if needed:

```bash
mkdir -p ~/.codex/skills/no-rewrite
```

Copy `SKILL.md` into that directory, then restart Codex or start a new session so the skill can be discovered. Invoke it with a prompt such as:

```text
Use $no-rewrite to compare the original and modified files for this task.
```

## 2. MCP server: `nba-api-explorer`

### What it does

The MCP server exposes one tool, **`inspect_nba_players()`**, using Python's `FastMCP` interface. The tool calls the NBA PlayerIndex endpoint through the `nba_api` package, reads the returned data into a pandas DataFrame, and returns:

- The total number of players in the API response.
- Every available field name and its data type.
- A sample nonmissing value for each field.
- The number of missing values in each field.

This helps an AI coding agent understand the actual API schema before deciding which player attributes to use. The tool inspects data; it does not edit the game or generate `players.json`.

### What Motivated it

I also found myself taking a large amount of time reviewing possible API's and the contents within them in order to decide which ones to use. 

While working on the NBA guessing game, I needed to know which player attributes the API actually provided and how missing values were represented. Without an inspection tool, I had to look up API documentation or run separate exploratory Python code before asking an agent to implement a new clue. The MCP tool gives the agent a direct, structured way to check available fields, such as `HEIGHT` and `JERSEY_NUMBER`, rather than assuming they exist.

### Installation

Use a Python environment with the required packages:

```bash
python3 -m pip install mcp nba_api pandas
```

Use a Python version supported by the installed MCP SDK. Save `server.py` in a stable location. Then open the Codex configuration file:

```text
~/.codex/config.toml
```

Add this server registration, replacing both marked paths with the actual paths on your machine:

```toml
[mcp_servers.nba-api-explorer]
command = "/ABSOLUTE/PATH/TO/PYTHON"  # MACHINE-SPECIFIC
args = ["/ABSOLUTE/PATH/TO/server.py"]  # MACHINE-SPECIFIC
```

For example, the `command` should point to the Python interpreter where `mcp`, `nba_api`, and `pandas` are installed. Find it by running `which python3` in that environment. The `args` path should point to the full location of this project's `server.py`.

Restart Codex after saving the configuration. To check that the server is connected, ask:

```text
Call inspect_nba_players using my NBA API Explorer MCP server.
Show me the fields returned by the NBA PlayerIndex API and their missing-value counts.
Do not modify any code.
```

The server uses standard input/output transport through `mcp.run()`, so it does not require a separately hosted web service. It does require internet access to contact the NBA API.

## 3. Tools and testing

I used **Codex** as the coding agent and tested the MCP connection in Codex on my Guess the NBA Player (HW3) files. I confirmed that Codex could call `inspect_nba_players()` and receive structured field information from the live NBA PlayerIndex API. In two calls, it returned **27 fields** and approximately **524–525 players**.

I also ran the **`no-rewrite` checker in Codex** on changes to the NBA guessing game after adding height as a clue and then country as a clue. Its report identified changes across the Python data generator, JavaScript game logic, HTML, and CSS. It destinguished the changes in each file and why they were needed for the functionality of adding new clues. It reported its findings without changing files. I also tested some other cases, like changing something not requested. The checker was able to flag these **Out of Scope** changes successfully.

The two MCP calls confirm that the tool was accessible in Codex.

## 4. Borrowed or adapted components

- **Model Context Protocol (MCP) and FastMCP:** I used the Python MCP SDK's `FastMCP` interface to expose the tool. See [MCP documentation](https://modelcontextprotocol.io/) and the [Python SDK](https://github.com/modelcontextprotocol/python-sdk).
- **Codex skill conventions and MCP configuration:** I followed the Codex approach of storing a skill in `SKILL.md` and registering a local MCP server in `config.toml`. See [OpenAI Codex documentation](https://developers.openai.com/codex/).

The game and the specific review instructions were adapted for my own project and workflow.

## 5. How I used AI

I used **ChatGPT (OpenAI)** to help plan the checker skill and MCP server, troubleshoot the Python environment and Codex setup, and refine the wording of the skill. I used **Codex (OpenAI)** to invoke the MCP tool and review code changes with the checker skill. I inspected the generated outputs and used my own NBA game as the test project.
