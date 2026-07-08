# Exercises · Module 00 — Orientation & Foundations

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md)

> Orientation is about **doing**, not just reading. By the end of these exercises you'll have a configured workstation, a portfolio-quality study repo, a learning journal, a daily routine, and the reading habits that carry you through the handbook.

Difficulty ramps ⭐ → ⭐⭐⭐⭐ per the [exercise standards](../../../standards/exercise-standards.md). Types: **Reflection**, **Setup**, **Git**, **Reading**, **Design**.

---

## A. Reflection questions (⭐)

Answer in your journal (`journal/00-orientation.md`). These have no single right answer — they build self-awareness.

- [ ] **A1.** In your own words (5 sentences), explain AI Engineering to a web developer friend.
- [ ] **A2.** Which of the seven roles ([00.3](../weeks/00.3-career-roadmap.md)) are you aiming for, and why? What draws you to it?
- [ ] **A3.** Recall a time you learned something shallowly and it failed you. How would the [four principles](../weeks/00.4-learning-strategy.md) have changed the outcome?
- [ ] **A4.** For each of the [seven mindsets](../weeks/00.10-ai-engineer-mindset.md), write one concrete way you'll practice it this year.

## B. Practical setup tasks (⭐⭐)

- [ ] **B1.** Install a modern package manager (`uv` or `poetry`) and confirm it runs.
- [ ] **B2.** Create a project inside a **virtual environment**, add `numpy`, and run a script that prints its version.
- [ ] **B3.** Add **Ruff, mypy, and pytest**. Write one tiny function and one test; get all three green.
- [ ] **B4.** Configure **VS Code**: select the project's `.venv` interpreter, enable format-on-save, install the recommended extensions ([00.5](../weeks/00.5-development-environment.md)).
- [ ] **B5. (⭐⭐⭐ Debug)** Deliberately select the *wrong* interpreter in VS Code, trigger an import error, then fix it. Write down the diagnostic steps you used.

## C. Repository preparation checklist (⭐⭐)

Build your **study repository** — the home for your year of work.

- [ ] **C1.** Initialize a Git repo with a clear `README.md` (what it is, how it's organized, your goals).
- [ ] **C2.** Add a sensible folder structure (`notes/`, `journal/`, `exercises/`, `projects/`, `references/`).
- [ ] **C3.** Add a `.gitignore` (ignore `.venv/`, `__pycache__/`, `.env`, data dumps).
- [ ] **C4.** Add a `CHANGELOG.md` and record your setup under `Added`.
- [ ] **C5.** Push it to GitHub as a **public** repo (it's your portfolio).

## D. Development environment checklist (⭐)

Confirm your workstation is truly reproducible:

- [ ] **D1.** Python **3.11+** selected as the interpreter.
- [ ] **D2.** One **virtual environment** per project (not global installs).
- [ ] **D3.** Dependencies **declared** in `pyproject.toml` + a committed **lockfile**.
- [ ] **D4.** Formatter + linter + type checker + test runner all configured.
- [ ] **D5. (⭐⭐ Reproduce)** Delete `.venv/`, reinstall from the lockfile, confirm the project still runs. Document the exact commands.

## E. Git exercises (⭐⭐)

- [ ] **E1.** Make **five small commits** using Conventional Commits (`type(scope): why`). Review `git log` — does it tell a story?
- [ ] **E2.** Create a `feat/notes` **branch**, add a note, merge it back to `main`.
- [ ] **E3.** Add a `CHANGELOG.md` entry in the *same commit* as a change.
- [ ] **E4. (⭐⭐⭐ Recover)** Make a change, commit it, then use Git to view and **revert** it. Document the commands you used.

## F. Reading exercises (⭐⭐ → ⭐⭐⭐)

- [ ] **F1. (Docs)** Pick a library you've never used. Using *only* its docs, get its quickstart running in under 20 minutes ([00.7](../weeks/00.7-reading-technical-documentation.md)).
- [ ] **F2. (API)** From that library's reference alone, document one function's required args, defaults, return type, and possible exceptions.
- [ ] **F3. (Repo)** Evaluate a popular open-source AI repo's **health** (last commit, open issues, tests). Would you depend on it? Why?
- [ ] **F4. (Paper — ⭐⭐⭐)** Pick a well-known AI paper. Do a 10-minute **Pass 1** and fill the [core-contribution template](../weeks/00.8-reading-research-papers.md#7-finding-the-core-contribution). Then explain its method from its main **figure** alone in 3 sentences.

## G. Design / scenario (⭐⭐⭐⭐)

- [ ] **G1.** A PM says "let's add AI to our search feature." Write a one-page decision: *whether* AI is the right tool, *which kind*, the simplest non-AI baseline, and how you'd measure success ([00.1](../weeks/00.1-introduction.md), [00.10](../weeks/00.10-ai-engineer-mindset.md)).
- [ ] **G2.** Draft your **personal daily loop** and **weekly rhythm** with realistic times, plus a **falling-behind recovery protocol** ([00.9](../weeks/00.9-learning-workflow.md)). Commit it to `journal/daily-loop.md`.

---

## Completion criteria

You've completed Module 00's exercises when:

- [ ] Your study repo is public on GitHub with clean structure and commits
- [ ] Your dev environment rebuilds from scratch (delete `.venv` → one install → runs)
- [ ] You've read one library's docs and one paper using the module's methods
- [ ] Your journal, daily loop, and recovery protocol exist and are committed
- [ ] You can tick every box on the [00.12 mastery checklist](../weeks/00.12-summary.md#5-revision-checklist--module-00-mastery) from memory

> [!TIP]
> These aren't busywork — they *are* the deliverable of Module 00. Knowledge fades; this infrastructure and these habits carry you through all 21 remaining modules.
