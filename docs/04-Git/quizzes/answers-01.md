# Answers · Module 04 Quiz 01

[🏠 Module](../README.md) · [❓ Questions](quiz-01.md)

> Model answers with the *why*. If you got the gist but not the reasoning, reread the linked lesson — and *do the drill* on a throwaway repo.

---

### Part 1 — Internals & History

**1.** A **snapshot** — each commit points to a complete tree (full project state) plus parent(s). Diffs are computed on the fly; identical content is deduplicated as shared blobs (content-addressing). → [04.1](../weeks/04.1-git-internals.md)

**2.** A branch is a movable **pointer** to a commit — a small file containing a SHA (`refs/heads/<name>`). HEAD is a pointer to the *current branch* (hence the current commit) — "where you are now." → [04.1](../weeks/04.1-git-internals.md)

**3.** The reflog records every move of HEAD/branch pointers. Because committed objects persist in `.git/objects` and the reflog remembers where you were, you can recover "lost" commits (bad reset, deleted branch, botched rebase) via `git reflog` → the SHA. Committed work is recoverable (~30–90 days); uncommitted is not. → [04.1](../weeks/04.1-git-internals.md)

**4.** Two (or more) — a merge commit joins two diverged lines; a normal commit has one parent. → [04.2](../weeks/04.2-commit-history.md)

**5.** Fast-forward when the target branch didn't diverge (Git just slides the pointer forward, linear history, no merge commit); three-way when both branches have new commits (Git creates a merge commit with two parents). → [04.2](../weeks/04.2-commit-history.md)

**6.** Detached HEAD is HEAD pointing directly at a commit instead of a branch (e.g., after checking out a SHA/tag). To avoid losing work: if you commit there, immediately create a branch (`git switch -c name`) before switching away — otherwise those commits become unreachable (recoverable via reflog). → [04.2](../weeks/04.2-commit-history.md)

### Part 2 — Branching & Advanced Ops

**7.** `main` (the trunk) is **always deployable** — risky, in-progress, or unreviewed work stays on branches. → [04.3](../weeks/04.3-branching-strategies.md)

**8.** GitHub Flow: simple default (branch → PR → merge → deploy; `main` always deployable). Git Flow: structured with `develop`/`release`/`hotfix` branches for versioned/released software (often overkill for continuous delivery). Trunk-based: everyone integrates into `main` frequently via tiny branches + feature flags + strong CI (fastest, elite). → [04.3](../weeks/04.3-branching-strategies.md)

**9.** Branch from the released commit (a tag), make the minimal fix, deploy — then **back-merge into `main`**. The classic mistake is forgetting to back-merge, which reintroduces the bug in the next release. → [04.3](../weeks/04.3-branching-strategies.md)

**10.** Merge preserves branches with a merge commit; rebase replays commits onto a new base for linear history (creating new hashes). Rebasing a *shared* branch is dangerous because it rewrites commits others have based work on — changing their hashes causes divergent-history chaos and can erase teammates' work. Rebase only local/unpushed work. → [04.4](../weeks/04.4-advanced-branch-management.md)

**11.** `--soft` (move the branch pointer, keep changes staged), `--mixed`/default (move pointer, unstage, keep changes in the working directory), `--hard` (move pointer AND discard uncommitted working-directory changes — dangerous, not in reflog). → [04.4](../weeks/04.4-advanced-branch-management.md)

**12.** **`revert`** for shared history — it adds a new inverse commit, preserving history (safe for anything others have). `reset` rewrites history and is only for local/private work. Never reset shared/pushed commits. → [04.4](../weeks/04.4-advanced-branch-management.md)

### Part 3 — Conflicts, Tags, Collaboration

**13.** No — a conflict is Git asking you to decide when two branches changed the same lines differently (vs their common ancestor); it safely stops rather than guessing. `<<<<<<< HEAD` marks your ("ours") version, `=======` divides, `>>>>>>> branch` ends the incoming ("theirs") version. Resolve to the correct content and delete all markers. → [04.5](../weeks/04.5-merge-conflicts.md)

**14.** Frequent integration + short-lived branches + small PRs (plus auto-formatting and modular code) — minimize divergence and overlapping edits. → [04.5](../weeks/04.5-merge-conflicts.md)

**15.** Lightweight = just a pointer (a name); annotated = a full object with tagger/date/message (signable) — use annotated for releases. SemVer `MAJOR.MINOR.PATCH`: MAJOR = breaking change, MINOR = backward-compatible feature, PATCH = backward-compatible fix — a communication contract about upgrade risk. → [04.6](../weeks/04.6-tags-releases.md)

**16.** Code, config, model weights, and data — a result is only reproducible if you can recover the exact combination (code+config via Git tags; models/data via LFS/registry/DVC, referenced by the code version). → [04.6](../weeks/04.6-tags-releases.md)

**17.** A pull request is a request to merge your branch into another (usually `main`) plus a space to review, discuss, and CI-check it before merging — the quality gate and unit of collaboration. Keep PRs small because small PRs get thorough reviews (catching more bugs), merge faster, and are easier to revert; large PRs get rubber-stamped. → [04.7](../weeks/04.7-github-collaboration.md)

**18.** Protected branches can require PRs (no direct push), N approving reviews, passing CI status checks, up-to-date branches, and CODEOWNERS approval — and block force-push/deletion — *enforcing* "main is always deployable." → [04.7](../weeks/04.7-github-collaboration.md)

### Part 4 — Repo Mgmt, Large Files, Automation, CI, Debugging

**19.** CODEOWNERS maps files/paths to responsible owners so GitHub auto-requests their review (and with protected branches, requires it). A LICENSE is essential for OSS because without one, others legally cannot use/modify/redistribute the code (all rights reserved by default), no matter how public. → [04.8](../weeks/04.8-repository-management.md)

**20.** Git stores every version of every file forever, and binaries don't diff/dedup — so the repo bloats permanently and everyone clones the history. Git LFS stores a tiny (~130-byte) pointer in Git and keeps the actual file in a separate LFS store, downloaded on demand — keeping the repo small. → [04.9](../weeks/04.9-large-files.md)

**21.** `.gitignore` only ignores files that aren't *already tracked*. If it was already committed, add-to-gitignore doesn't untrack it — you must `git rm --cached <file>` (untrack, keep locally) and commit. (And it remains in history.) → [04.9](../weeks/04.9-large-files.md)

**22.** The `pre-commit` framework stores its config in a committed `.pre-commit-config.yaml`, so the whole team runs identical checks (unlike raw `.git/hooks/` which aren't shared). Fast checks (format, lint, types, secret-scan) go in pre-commit for instant feedback; slow checks (full test suite) go in CI so committing stays fast. → [04.10](../weeks/04.10-automation.md)

**23.** CI runs on GitHub's servers for every push/PR, so developers can't skip it (unlike bypassable local hooks), and protected branches block merging until it passes. Secrets: store them in GitHub Secrets and reference as `${{ secrets.NAME }}` (encrypted, injected as env vars, masked in logs) — never hard-code them in the workflow. → [04.11](../weeks/04.11-github-actions.md)

**24.** Don't panic — run `git status` and `git reflog` (and `git log --graph`) to understand the state *before* acting. To recover lost commits: find the good state's SHA in `git reflog`, then `git reset --hard <sha>` (or `git branch rescue <sha>`). → [04.12](../weeks/04.12-debugging-git.md)

**25.** Recover the erased commits' SHA from *somewhere they still exist* — your reflog, a teammate's local clone, or GitHub's records (merged-PR pages / branch events) — then reset `main` to the good SHA and `push --force-with-lease`. Prevent it with protected branches (block force-push to `main`) and `--force-with-lease` (never bare `--force`). → [04.12](../weeks/04.12-debugging-git.md)

**26.** `git bisect` does a binary search through history: you mark a known-good and known-bad commit, Git checks out the midpoint, you test and mark it good/bad, and it narrows down (O(log n) tests) to the exact commit that introduced the bug. It can be automated with `git bisect run <test-script>`. → [04.12](../weeks/04.12-debugging-git.md)

---

> [!TIP]
> Turn every missed question into a flashcard, and for recovery questions, reproduce the disaster and fix it on a throwaway repo — that's the only way Git recovery becomes reflexive.
