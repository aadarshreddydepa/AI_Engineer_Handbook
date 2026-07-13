# Flashcards · Module 04 — Advanced Git & Collaboration

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md)

> Active-recall deck for the whole module. Answer **out loud before flipping**. Review on the [spaced-repetition schedule](../../../LEARNING_STRATEGY.md): same day, +1d, +3d, +7d, +16d, +35d. A failed card resets to interval 1.

---

## 04.1 · Internals
**Q:** Is a Git commit a diff or a snapshot?
**A:** A snapshot — it points to a complete tree plus parent(s); diffs are computed on the fly, and identical content is deduplicated as shared blobs.

**Q:** What is a branch, internally, and what is HEAD?
**A:** A branch is a movable pointer to a commit (a file with a SHA); HEAD is a pointer to the current branch.

**Q:** How do you recover a commit after a bad `reset --hard`?
**A:** `git reflog` to find the lost commit's SHA, then `git reset --hard <sha>` — the commit still exists as an object.

---

## 04.2 · Commit History
**Q:** How many parents does a merge commit have?
**A:** Two (or more) — it joins two diverged lines; a normal commit has one parent.

**Q:** Fast-forward vs three-way merge?
**A:** Fast-forward slides the pointer forward (target didn't diverge, linear); three-way creates a merge commit when both branches have new commits.

**Q:** What is detached HEAD?
**A:** HEAD pointing directly at a commit instead of a branch; commits made there aren't on a branch and can be lost if you switch away without branching.

---

## 04.3 · Branching Strategies
**Q:** What invariant do all strategies protect?
**A:** `main` is always deployable — risky/unreviewed work stays on branches.

**Q:** When is Git Flow appropriate vs overkill?
**A:** For versioned/released software with multiple supported versions; overkill for continuously-deployed services (long-lived branches diverge).

**Q:** What does trunk-based development require?
**A:** Strong CI/testing and feature flags — everyone integrates into `main` frequently via very short branches.

---

## 04.4 · Advanced Branch Management
**Q:** Merge vs rebase?
**A:** Merge preserves branches with a merge commit; rebase replays commits onto a new base for linear history (new hashes) — rebase only on local/unpushed work.

**Q:** The three reset modes?
**A:** `--soft` (keep changes staged), `--mixed`/default (keep in working dir, unstaged), `--hard` (discard uncommitted changes).

**Q:** Reset vs revert — which for shared history?
**A:** `revert` (adds an inverse commit, preserves history — safe for shared); `reset` rewrites history (local/private only).

**Q:** The golden rule of rewriting history?
**A:** Rewrite private/unpushed history freely; never rewrite history others have pulled — once shared, only add (merge/revert).

---

## 04.5 · Merge Conflicts
**Q:** Is a merge conflict an error?
**A:** No — it's Git asking you to decide when two branches changed the same lines differently; Git safely stops rather than guessing.

**Q:** What if a conflict is too complex?
**A:** `git merge --abort` / `git rebase --abort` — returns you exactly to before you started, no penalty.

**Q:** Best way to prevent conflicts?
**A:** Frequent integration + short-lived branches + small PRs (plus auto-formatting) — minimize divergence and overlap.

---

## 04.6 · Tags & Releases
**Q:** Lightweight vs annotated tag?
**A:** Lightweight is just a pointer; annotated is a full object with tagger/date/message (and signable) — use annotated for releases.

**Q:** Explain SemVer.
**A:** `MAJOR.MINOR.PATCH`: MAJOR = breaking, MINOR = backward-compatible feature, PATCH = backward-compatible fix — a contract communicating upgrade risk.

**Q:** What must be versioned together for AI reproducibility?
**A:** Code, config, model weights, and data — a result is only reproducible if you can recover the exact combination.

---

## 04.7 · GitHub Collaboration
**Q:** Why keep PRs small?
**A:** Small PRs get thorough reviews (catching more bugs), merge faster, and are easier to revert; large PRs get rubber-stamped.

**Q:** Squash vs merge-commit vs rebase merge?
**A:** Squash = one clean commit per PR (common default); merge commit = all commits + merge commit; rebase = linear replay of the commits.

**Q:** What do protected branches enforce?
**A:** They can require PRs, N approvals, passing CI, and block force-push/deletion — enforcing "main is always deployable."

---

## 04.8 · Repository Management
**Q:** What goes near the top of a README?
**A:** The quickstart (install + run) — optimize for a first-time visitor with 60 seconds.

**Q:** What does CODEOWNERS do?
**A:** Maps files/paths to owners so GitHub auto-requests their review; with protected branches, their approval becomes required before merge.

**Q:** Why is a LICENSE essential for open source?
**A:** Without one, others legally cannot use/modify/redistribute the code (all rights reserved by default), no matter how public.

---

## 04.9 · Large Files
**Q:** Why is committing large binaries to Git bad?
**A:** Git stores every version as a full blob forever (binaries don't dedup), so the repo bloats permanently and everyone downloads the history on clone.

**Q:** How does Git LFS work?
**A:** It stores a tiny text pointer in Git and keeps the actual large file in a separate LFS store, downloaded on demand — keeping the repo small.

**Q:** You added a file to `.gitignore` but it's still tracked — why?
**A:** `.gitignore` only ignores untracked files; already-committed files need `git rm --cached` (and remain in history).

---

## 04.10 · Automation
**Q:** Why use the `pre-commit` framework over raw `.git/hooks/`?
**A:** Raw hooks aren't shared (`.git/` is local); the framework's config is committed, so the whole team runs identical checks.

**Q:** What belongs in pre-commit vs CI?
**A:** Fast checks (format, lint, types, secret-scan) in pre-commit for instant feedback; slow checks (full test suite) in CI.

**Q:** Highest-value security automation for AI teams?
**A:** A secret-scanning pre-commit hook (gitleaks) that blocks commits containing keys/passwords before they enter history.

---

## 04.11 · GitHub Actions
**Q:** Why is CI the "unbypassable" quality gate?
**A:** It runs on GitHub's servers for every push/PR (can't be skipped like local hooks), and protected branches block merging until it passes.

**Q:** How do you handle secrets in Actions?
**A:** Store them in GitHub Secrets and reference as `${{ secrets.NAME }}` (injected as env vars, masked in logs) — never hard-code in the workflow.

**Q:** What is a matrix build?
**A:** Running the same job across multiple versions/OSes in parallel — essential for libraries that must support several Python versions.

---

## 04.12 · Debugging Git
**Q:** First move when you've broken your Git?
**A:** Don't panic — run `git status` and `git reflog` to understand the state and history before acting.

**Q:** Recover from a force-push that erased commits?
**A:** Find the pre-force SHA (your reflog, a teammate's clone, or GitHub's records) and restore; prevent with protected branches + `--force-with-lease`.

**Q:** What is `git bisect`?
**A:** A binary search through history (mark good/bad, test midpoints) that pinpoints the commit that introduced a bug in O(log n) steps.

---

> [!TIP]
> When you can answer every card AND execute the full feature-branch → PR → merge → release workflow, Module 04 is locked in.
