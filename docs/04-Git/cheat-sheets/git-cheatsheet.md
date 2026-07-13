# Cheat Sheet · Module 04 — Advanced Git & Collaboration

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md)

> One-page reference for the whole module. Scan it; learn it in the [lessons](../weeks/README.md). Practice dangerous commands on a **throwaway** repo.

---

## Internals & history (04.1–04.2)

```text
3 AREAS: working dir --add--> INDEX(staging) --commit--> REPO(.git) · git status(which) · git add -p(stage hunks)
4 OBJECTS (content-addressed by SHA): BLOB(file) · TREE(dir) · COMMIT(SNAPSHOT+parent+meta) · TAG
  COMMIT = SNAPSHOT not a diff · identical content → shared blob (dedup + integrity)
REFS = POINTERS: branch = pointer to a commit (instant to create) · HEAD = current branch · tag = fixed pointer
REFLOG (git reflog): every HEAD move → recover "lost" commits · committed=recoverable, uncommitted=NOT → commit often
HISTORY = DAG: commit → parent(s) · normal=1, MERGE=2 · git log --oneline --graph --all (★)
  HEAD~n(n back) · HEAD^(parent, ^2=2nd parent) · git blame · git log -S "text"(pickaxe)
MERGE: FAST-FORWARD(pointer slides, linear) vs THREE-WAY(2-parent merge commit; --no-ff forces)
DETACHED HEAD (HEAD→commit not branch, after checkout sha/tag): commit there → make a branch or lose it (reflog)
```

## Branching, advanced ops, conflicts (04.3–04.5)

```text
FOUNDATION: feature branch → PR → review → merge · main ALWAYS DEPLOYABLE · short-lived branches
STRATEGIES: GITHUB FLOW(default: branch→PR→merge→deploy) · GIT FLOW(structured, versioned sw, often overkill) · TRUNK-BASED(fast, feature flags + strong CI)
  HOTFIX: branch from released tag → minimal fix → deploy → BACK-MERGE to main
REBASE (linear, NEW hashes): git rebase main · rebase -i HEAD~N (squash/reword/reorder/drop — clean up BEFORE PR)
  ⚠️ only on LOCAL/unpushed · NEVER shared branches
CHERRY-PICK <sha> (copy 1 commit) · RESET: --soft(keep staged) --mixed(keep unstaged) --hard(⚠️DISCARD uncommitted)
REVERT <sha> (new inverse commit — SAFE for shared/public; revert -m 1 for merges)
GOLDEN RULE: rewrite PRIVATE history freely; SHARED → only add (merge/revert) · force? --force-with-lease (never bare --force)
CONFLICT (both changed same lines) = Git asking YOU (not an error): <<<<<<< HEAD ours ======= theirs >>>>>>> 
  resolve → delete markers → git add → commit/rebase --continue · BAIL: merge/rebase --abort (no penalty)
  prevent: short branches + integrate FREQUENTLY + small PRs + auto-format · notebooks → nbstripout/nbdime
```

## Releases, collaboration, repo mgmt (04.6–04.8)

```text
TAG (permanent name for a commit): annotated (releases!) git tag -a v1.4.0 -m "..." · ⚠️ push explicitly (git push origin v1.4.0)
SEMVER MAJOR.MINOR.PATCH: breaking / feature(compat) / fix(compat) · communication contract
GITHUB RELEASE = tag + notes + assets · AI: version code+model+config+data TOGETHER
PULL REQUEST = merge request + review space (the collaboration unit) · SMALL PRs (#1 lever) · clear what/why/test
REVIEW: about the CODE not the coder · kind+specific · "nit:" optional · review promptly · respond to every comment
MERGE: squash(1 clean commit — common) · merge commit(full) · rebase(linear)
PROTECTED BRANCHES (enforce "main deployable"): require PR + N approvals + CI green + no force-push + CODEOWNERS
REPO HEALTH: README(quickstart ON TOP) · CONTRIBUTING · CODEOWNERS(auto review routing) · PR/issue templates · LICENSE(req for OSS) · CHANGELOG · SECURITY.md · .gitignore
```

## Large files, automation, CI, debugging (04.9–04.12)

```text
LARGE FILES: Git stores every version forever, binaries don't dedup → repo bloat (04.1)
  .gitignore (BEFORE 1st commit!): data/ *.pt *.safetensors checkpoints/ wandb/ .venv/ __pycache__/ · .env *.key (SECRETS!)
  GIT LFS: git lfs track "*.safetensors" → tiny pointer in Git, file in LFS store · big/evolving data → DVC/registry
  already tracked? git rm --cached · notebooks → strip outputs · NEVER git add . blindly
AUTOMATION (pre-commit framework, committed config .pre-commit-config.yaml): ruff-format · ruff · mypy · GITLEAKS(secrets) · nbstripout
  fast checks → pre-commit · slow (tests) → CI · pre-commit install (per clone) · commit-msg lint (Conventional Commits)
GITHUB ACTIONS (CI = unbypassable gate): .github/workflows/ci.yml · on: push/pull_request · jobs→runner(ubuntu)→steps
  checkout → setup-python → install(lockfile) → ruff/mypy/pytest · SECRETS ${{secrets.X}} · cache: pip · matrix: python-version
  require CI on protected branch → PR can't merge until green · AI adds: model eval gate, data validation, docker build
DEBUG GIT (don't panic!): git status + git reflog FIRST · committed = recoverable (~30-90d)
  lost commits: reflog → reset --hard <sha> · wrong branch: git branch <right> + reset --hard HEAD~n · deleted branch: reflog → git branch x <sha>
  bad merge: local reset / shared revert -m 1 · force-push erased: get SHA (reflog/teammate/GitHub) → restore
  find breaking commit: git bisect (binary search 02.4) · remove secret from history: filter-repo + ROTATE the secret
```

## The complete AI project workflow

```text
1 branch (04.3) → 2 small commits (04.1) → 3 tests (01.10) → 4 docs/CHANGELOG (04.6) → 5 rebase -i clean up (04.4)
→ 6 push (pre-commit ran, 04.10) → 7 PR w/ description (04.7) → 8 CI runs (04.11) → 9 review + fixes (04.7)
→ 10 resolve conflicts (04.5) → 11 squash-merge to main (04.7) → 12 tag + release (04.6) → 13 delete branch
```
