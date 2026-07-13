# Exercises · Module 04 — Advanced Git & Collaboration

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md)

> A structured set spanning all 12 concept lessons — branching, merge-conflict labs, rebase practice, recovery drills, GitHub collaboration, and CI — with a deliberate difficulty ramp per the [exercise standards](../../../standards/exercise-standards.md).

> [!WARNING]
> **Do all dangerous exercises (reset, rebase, force-push, branch deletion) on a THROWAWAY repo** (`git init /tmp/git-practice`). Never practice destructive commands on real work.

**Difficulty:** ⭐ warm-up · ⭐⭐ practice · ⭐⭐⭐ challenge · ⭐⭐⭐⭐ stretch. **Types:** 🌿 Branching · 💥 Conflict lab · ♻️ Rebase · 🔧 Recovery · 👥 Collaboration · ⚙️ CI.

---

## 04.1 · Internals
- [ ] **⭐ 🔧** Use `git cat-file -t/-p` to walk from HEAD → commit → tree → blob by hand.
- [ ] **⭐⭐ 🔧** Observe a file across working/staged/committed via `git status`/`git diff`/`git diff --staged`.
- [ ] **⭐⭐⭐ 🔧** Make 3 commits, `reset --hard HEAD~2`, recover them via reflog.

## 04.2 · Commit History
- [ ] **⭐ 🌿** Run `git log --oneline --graph --all`; identify a merge commit and its parents.
- [ ] **⭐⭐ 🌿** Create two branches, commit on both, visualize the divergence.
- [ ] **⭐⭐⭐ 🔧** Enter detached HEAD, commit, "lose" it, recover via reflog + branch.

## 04.3 · Branching Strategies
- [ ] **⭐ 🌿** For 3 scenarios, choose a strategy and justify.
- [ ] **⭐⭐ 🌿** Simulate GitHub Flow: branch → work → "PR" (merge), keeping main deployable.
- [ ] **⭐⭐⭐ 🌿** Simulate a hotfix: tag a release, branch from the tag, fix, back-merge to main.

## 04.4 · Advanced Branch Management
- [ ] **⭐⭐ ♻️** Rebase a feature branch onto an advanced main; compare graph to a merge.
- [ ] **⭐⭐⭐ ♻️** Squash 4 messy commits into 2 clean ones with `rebase -i`.
- [ ] **⭐⭐ ♻️** Cherry-pick one commit onto main.
- [ ] **⭐⭐ 🔧** Demonstrate soft/mixed/hard reset differences; then revert a commit.
- [ ] **⭐⭐⭐ 🔧** Recovery drill: bad reset → reflog recover; delete branch → recover.

## 04.5 · Merge Conflicts
- [ ] **⭐ 💥** Create a same-line conflict; observe the markers.
- [ ] **⭐⭐ 💥** Resolve it by combining both changes; verify no leftover markers (`grep`).
- [ ] **⭐⭐ 💥** Trigger a conflict, then `git merge --abort` to bail cleanly.
- [ ] **⭐⭐⭐ 💥** Resolve a conflict during a rebase with `--continue`; enable `zdiff3`.

## 04.6 · Tags & Releases
- [ ] **⭐ 🔧** Create lightweight + annotated tags; `git show` each; push a tag.
- [ ] **⭐⭐ 🔧** Given 5 change descriptions, decide the SemVer bump for each.
- [ ] **⭐⭐ 👥** On GitHub, create a Release from a tag with notes.

## 04.7 · GitHub Collaboration
- [ ] **⭐ 👥** Open a small PR with a clear what/why/how-to-test description.
- [ ] **⭐⭐ 👥** Review a (sample) PR: one blocking comment, one "nit", one suggested change; approve.
- [ ] **⭐⭐ 👥** Merge PRs three ways (merge/squash/rebase); compare the resulting main history.
- [ ] **⭐⭐⭐ 👥** Enable branch protection (PR + review + CI required); try (and fail) to push directly to main.

## 04.8 · Repository Management
- [ ] **⭐ 👥** Write a README with quickstart-on-top for a sample AI project.
- [ ] **⭐⭐ 👥** Draft CONTRIBUTING.md and a CODEOWNERS file.
- [ ] **⭐⭐ 👥** Create PR + bug-report issue templates.

## 04.9 · Large Files
- [ ] **⭐ 🔧** Write a thorough AI-project `.gitignore` (data/models/caches/secrets).
- [ ] **⭐⭐ 🔧** Commit a file, gitignore it, observe it's still tracked, `git rm --cached` it.
- [ ] **⭐⭐ 🔧** Set up Git LFS; track a large file type; inspect the pointer file.
- [ ] **⭐⭐⭐ 🔧** Demonstrate repo bloat: commit a large binary a few times; measure `.git` growth.

## 04.10 · Automation
- [ ] **⭐ ⚙️** Add `.pre-commit-config.yaml` with Ruff + mypy; watch a failing commit get blocked.
- [ ] **⭐⭐ ⚙️** Add the `gitleaks` hook; try to commit a fake API key; watch it get blocked.
- [ ] **⭐⭐ ⚙️** Add `nbstripout`; commit a notebook; confirm outputs stripped.
- [ ] **⭐⭐⭐ ⚙️** Add a `commit-msg` hook enforcing Conventional Commits.

## 04.11 · GitHub Actions
- [ ] **⭐ ⚙️** Write a CI workflow running `ruff check` + `pytest` on every push/PR.
- [ ] **⭐⭐ ⚙️** Add dependency caching; observe the speedup.
- [ ] **⭐⭐ ⚙️** Use a GitHub Secret in a step.
- [ ] **⭐⭐⭐ ⚙️** Add a Python-version matrix; require the CI check to merge; confirm a failing PR is blocked.

## 04.12 · Debugging Git
- [ ] **⭐⭐ 🔧** Lost-commit, wrong-branch, and deleted-branch recovery drills (throwaway repo).
- [ ] **⭐⭐⭐ 🔧** Undo a bad merge locally (reset) and safely (revert).
- [ ] **⭐⭐⭐ 🔧** Use `git bisect` to find a planted bug; try `git bisect run` with a test script.
- [ ] **⭐⭐⭐⭐ 🔧** Simulate a force-push disaster with two clones; recover the erased commits.

## Projects
- [ ] Build the **template repo** (professional OSS repo + CI + release automation — projects 1–3).
- [ ] Complete the full **feature-branch → PR → merge → release** workflow ([04.13](../weeks/04.13-workflow-projects-summary.md)).

---

## Completion criteria

- [ ] Every ⭐/⭐⭐ exercise attempted (on a throwaway repo where dangerous)
- [ ] At least four ⭐⭐⭐ challenges solved (incl. one conflict lab + one recovery drill)
- [ ] The template repo (CI + release automation) works
- [ ] You can execute the full AI-project Git workflow comfortably
- [ ] You can tick the [04.13 mastery checklist](../weeks/04.13-workflow-projects-summary.md#module-04-mastery-checklist-from-memory--on-a-repo) from memory

> [!TIP]
> The recovery drills (🔧) build the most valuable, confidence-giving skill. Break a practice repo every way you can and recover it — that's how "I ruined my repo" becomes "give me 30 seconds."
