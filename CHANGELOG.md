# Changelog

All notable changes to this handbook are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project aims to follow it loosely. Dates are in `YYYY-MM-DD`.

---

## [Unreleased]

### Planned
- Module 05 · SQL — lesson content
- Weekly lessons authored module by module

---

## [0.9.0] — 2026-07-09

### Added
- **Module 04 · Advanced Git & Collaboration for AI Engineers — complete.**
  - 13 lessons (`docs/04-Git/weeks/04.1`–`04.13`): Git internals (objects, refs, reflog), commit history (the DAG, merges, detached HEAD), branching strategies (GitHub Flow/Git Flow/trunk-based), advanced branch management (rebase, interactive rebase, cherry-pick, reset, revert, reflog recovery), merge conflict resolution, tags & releases (SemVer, GitHub Releases), GitHub collaboration (PRs, reviews, protected branches, merge strategies), repository management (README/CONTRIBUTING/CODEOWNERS/templates), large files (Git LFS, `.gitignore`), automation (Git hooks, pre-commit), GitHub Actions (CI/CD), debugging Git (recovery walkthroughs), and a complete AI-project-workflow + projects + summary lesson.
  - Companion artifacts: consolidated [exercises](docs/04-Git/exercises/README.md) (branching, conflict labs, rebase, recovery drills, collaboration, CI — difficulty-ramped), a 26-question [quiz](docs/04-Git/quizzes/quiz-01.md) with model [answers](docs/04-Git/quizzes/answers-01.md), a full [flashcard deck](docs/04-Git/flashcards/deck.md), and a [master cheat sheet](docs/04-Git/cheat-sheets/git-cheatsheet.md).
  - Five mini-projects (professional OSS repo, CI pipeline, release automation, AI project with Git LFS, branching-strategy design) plus a Git recovery playbook, and an end-to-end "feature branch → PR → review → merge → tag → release" workflow.
  - Module [lesson index](docs/04-Git/weeks/README.md); linked from the module README.
- Glossary: added an "Advanced Git & Collaboration (Module 04)" section (objects/refs/reflog, rebase, reset/revert, merge conflict, protected branch, CODEOWNERS, Git LFS, pre-commit, GitHub Actions, `git bisect`, and more).

### Notes
- Assumes Git fundamentals (no `init`/`add`/`commit` reteaching); focuses on internals, recovery, collaboration, releases, automation, and AI-project specifics (notebooks, LFS, model/data versioning, secret handling). Heavily cross-referenced to Modules 00–03; the object model builds on Module 02 data structures, and CI runs on Module 03 Linux runners.

---

## [0.8.0] — 2026-07-09

### Added
- **Module 03 · Linux for AI Engineers — complete.**
  - 17 lessons (`docs/03-Linux/weeks/03.1`–`03.17`): introduction (kernel vs OS vs distro, why AI/cloud/Docker/K8s use Linux), architecture (kernel/user space/syscalls/scheduler), filesystem (hierarchy, inodes, symlinks, `/proc`, `/dev`), terminal mastery (pipes, redirection, PATH, env vars, globs), essential commands (grep/find/awk/sed/xargs/…), permissions (chmod/chown, SUID/SGID/sticky, least privilege), processes (states, tmux, nvidia-smi, signals), systemd services, networking (SSH keys, rsync, diagnostics), storage (df/du, ext4/xfs, fstab), logs (journalctl, dmesg, rotation), bash scripting (`set -euo pipefail`, functions, traps, exit codes), package & environment management (apt vs uv/conda), performance monitoring (free/vmstat/iostat/sar, bottleneck analysis), security (SSH hardening, UFW, Fail2Ban, secrets), Docker preparation (namespaces/cgroups/OverlayFS), and a workflow + projects + summary lesson.
  - Companion artifacts: consolidated [exercises](docs/03-Linux/exercises/README.md) (terminal/debug/log/permission/bash, difficulty-ramped), a 28-question [quiz](docs/03-Linux/quizzes/quiz-01.md) with model [answers](docs/03-Linux/quizzes/answers-01.md), a full [flashcard deck](docs/03-Linux/flashcards/deck.md), and a [master cheat sheet](docs/03-Linux/cheat-sheets/linux-cheatsheet.md).
  - Six mini-projects threaded through their host lessons: log analyzer, file backup utility, dataset organizer, monitoring dashboard, deployment automation, and server health & security checker — plus a "day in the life of an AI Engineer" end-to-end workflow.
  - Module [lesson index](docs/03-Linux/weeks/README.md); linked from the module README.
- Glossary: added a "Linux for AI Engineers (Module 03)" section (kernel, distro, shell, syscall, systemd, `journalctl`, SSH keys, `rsync`, `tmux`, `nvidia-smi`, load average, swap, UFW, Fail2Ban, namespaces, cgroups, containers, and more).

### Notes
- Teaches Linux **as an operating system** (not a command list), with every topic tied to real AI-Engineer usage (SSH into GPU servers, tmux training jobs, nvidia-smi, systemd model services, rsync datasets, hardening) and cross-referenced to Modules 00–02. The Docker-preparation lesson reveals containers as namespaces + cgroups + union filesystems, priming Module 16.

---

## [0.7.0] — 2026-07-08

### Added
- **Module 02 · Computer Science Foundations for AI Engineers — complete.**
  - 13 lessons (`docs/02-Computer-Science/weeks/02.1`–`02.13`): how computers work (CPU/cache/instruction cycle/compilers), memory (stack/heap/fragmentation/GC/cache locality), data structures (arrays→graphs), algorithms (search/sort/DP/greedy/graph/backtracking), time & space complexity (Big-O/Ω/Θ), operating systems (processes/threads/scheduling/virtual memory), networking (TCP/IP, HTTP(S), REST/WebSocket/gRPC, load balancers), concurrency (threading/multiprocessing/async, the GIL, races/locks), serialization (JSON/YAML/Pickle/MessagePack/Protobuf + security), file systems (permissions/symlinks/compression/durable writes), system-design basics (scaling/availability/fault tolerance/caching), debugging (stack traces/profiling/observability), and a projects+summary consolidation lesson.
  - Companion artifacts: consolidated [exercises](docs/02-Computer-Science/exercises/README.md) (conceptual/coding/debug/architecture, difficulty-ramped), a 26-question [quiz](docs/02-Computer-Science/quizzes/quiz-01.md) with model [answers](docs/02-Computer-Science/quizzes/answers-01.md), a full [flashcard deck](docs/02-Computer-Science/flashcards/deck.md), and a [master cheat sheet](docs/02-Computer-Science/cheat-sheets/cs-foundations-cheatsheet.md).
  - Seven mini-projects threaded through their host lessons: trie autocomplete, graph traversal visualizer, thread-safe queue, LRU cache, in-memory cache, URL shortener (core), and a simple HTTP server.
  - Module [lesson index](docs/02-Computer-Science/weeks/README.md); linked from the module README.
- Glossary: added a "Computer Science Foundations (Module 02)" section (memory hierarchy, cache locality, Big-O, process/thread, deadlock, virtual memory, TCP/HTTP, load balancer, serialization, statelessness, observability, and more).

### Notes
- Taught from first principles (no prior CS assumed) but at professional depth, with every concept tied to AI-system relevance (GPUs, tensors, model serving, distributed training) and cross-referenced to Modules 00–01.

---

## [0.6.0] — 2026-07-08

### Added
- **Module 01 · Advanced Python for AI Engineering — complete.**
  - 15 lessons (`docs/01-Advanced-Python/weeks/01.1`–`01.15`): Python architecture/bytecode/import system, memory & the data model, OOP, functional programming, iterators & generators, decorators, context managers, type hinting (+ Pydantic), error handling & logging, testing, performance & the GIL, async programming, packaging & code quality, reading open-source code, and a projects+summary consolidation lesson.
  - Companion artifacts: consolidated [exercises](docs/01-Advanced-Python/exercises/README.md) (coding/debug/refactor/design, difficulty-ramped), a 25-question [quiz](docs/01-Advanced-Python/quizzes/quiz-01.md) with model [answers](docs/01-Advanced-Python/quizzes/answers-01.md), a full [flashcard deck](docs/01-Advanced-Python/flashcards/deck.md), and a [master cheat sheet](docs/01-Advanced-Python/cheat-sheets/advanced-python-cheatsheet.md).
  - Six progressively harder mini-projects (file indexer → log analyzer → async API client → CLI → config manager → plugin system), with the async API client as the flagship.
  - Module [lesson index](docs/01-Advanced-Python/weeks/README.md); linked from the module README.
- Glossary: added an "Advanced Python (Module 01)" section (CPython, bytecode, PVM, GIL, closures, decorators, generators, context managers, Protocol, Pydantic, coroutine/event loop, vectorization, lockfile, and more).

### Notes
- Lessons assume Python fundamentals (no beginner reteaching) and target production AI-engineering depth; §9 (Error Handling) and §10 (Logging) from the module spec are combined into lesson 01.9.

---

## [0.5.0] — 2026-07-08

### Added
- **Module 00 · Orientation & Foundations — complete.** First authored module of the handbook.
  - 12 lessons (`docs/00-Orientation/weeks/00.1`–`00.12`): vocabulary of the field, the AI Engineering landscape, careers & roles, learning strategy, development environment, GitHub workflow, reading documentation, reading research papers, the daily learning workflow, the AI Engineer mindset, recommended resources, and a consolidation/summary lesson.
  - Companion artifacts: consolidated [exercises](docs/00-Orientation/exercises/README.md), a 20-question [quiz](docs/00-Orientation/quizzes/quiz-01.md) with model [answers](docs/00-Orientation/quizzes/answers-01.md), a full [flashcard deck](docs/00-Orientation/flashcards/deck.md), and a [master cheat sheet](docs/00-Orientation/cheat-sheets/orientation-cheatsheet.md).
  - Module [lesson index](docs/00-Orientation/weeks/README.md); linked from the module README.
- Glossary: added a "Foundations, Engineering & Learning (Module 00)" section (AI Engineering, AGI, reproducibility, SemVer, Conventional Commits, active recall, spaced repetition, and more).

### Notes
- Lessons follow the standards library and the 26-section master template, adapted for conceptual/orientation content (template sections not applicable to non-technical material — e.g. Security/Performance Considerations — are intentionally omitted with a note).

---

## [0.4.0] — 2026-07-08

### Changed
- **Adopted Curriculum Review Option A — expanded to 22 modules.** Inserted `12-Prompt-Engineering` (after LLMs) and `15-Fine-Tuning` (after AI-Agents); renumbered former modules `12–19` → `13–21`.
- Regenerated all `docs/` module folders, READMEs, and navigation from the updated [scripts/generate_structure.py](scripts/generate_structure.py) (single source of truth).
- Realigned `README.md`, `ROADMAP.md` (now ~57 weeks, updated dependency graph & phases), `CURRICULUM.md`, and `PROGRESS_TRACKER.md` to the 22-module taxonomy.
- Marked the structural decision as applied in [CURRICULUM_REVIEW.md](CURRICULUM_REVIEW.md).

---

## [0.3.0] — 2026-07-08

### Added
- **Standards library** in [standards/](standards/): documentation philosophy, visual, code, retention, exercise, project, interview, and reference standards, plus an index.
- **Master lesson template** — canonical 26-section structure in [templates/lesson-template.md](templates/lesson-template.md).
- **Curriculum validation** in [CURRICULUM_REVIEW.md](CURRICULUM_REVIEW.md): gap analysis (fine-tuning, prompt engineering, data engineering, evaluation), ordering check, and a structural decision proposal.

### Changed
- Upgraded [templates/project-template.md](templates/project-template.md) to the required 9-section project standard.
- Linked the standards library from [CONTRIBUTING.md](CONTRIBUTING.md) and [README.md](README.md); aligned naming conventions to the `NN-Title-Case` scheme.

---

## [0.2.0] — 2026-07-08

### Changed
- **Expanded to a 20-module taxonomy** (`00-Orientation` … `19-Capstone-Projects`), superseding the earlier 16-module ML-only structure. Added Computer Science, Linux, Git, SQL, Data Analysis, Cloud, System Design, and Interview Preparation as first-class modules.
- Restructured `docs/` so each module is a top-level folder (removed the `docs/modules/` nesting).
- Realigned `README.md`, `ROADMAP.md`, `CURRICULUM.md`, `REPOSITORY_STRUCTURE.md`, and `PROGRESS_TRACKER.md` to the new taxonomy.

### Added
- Full repository skeleton: every module folder with eight standardized subfolders (`weeks/`, `diagrams/`, `exercises/`, `projects/`, `quizzes/`, `flashcards/`, `cheat-sheets/`, `references/`).
- Navigation-rich `README.md` for every module and top-level folder (parent / prev / next / roadmap / related).
- New top-level folders: `code/`, `notebooks/`, `interview-preparation/`, `scripts/`, `archive/`, and `assets/{icons,cheatsheets}`.
- Twelve reusable templates (lesson, weekly summary, project, exercise, quiz, flashcards, architecture notes, research-paper summary, cheat sheet, interview notes, debugging session, project retrospective).
- `LICENSE.md` (CC BY 4.0 content + MIT code) and `.gitignore`.
- `scripts/generate_structure.py` — idempotent generator that owns the structural/templated files.

### Removed
- Superseded top-level `cheatsheets/`, `interview-prep/`, and `glossary/` folders (replaced by `assets/cheatsheets/`, `interview-preparation/`, and per-module `references/`).

---

## [0.1.0] — 2026-07-08

### Added
- Initial repository structure (docs, assets, exercises, quizzes, flashcards, projects, notebooks, references, cheatsheets, interview-prep, glossary, templates).
- Planning documents:
  - `README.md` — entry point and overview
  - `ROADMAP.md` — full modules → weeks → lessons plan with estimates, difficulty, and dependency graph
  - `CURRICULUM.md` — lesson-by-lesson learning outcomes
  - `REPOSITORY_STRUCTURE.md` — folder map and conventions
  - `LEARNING_STRATEGY.md` — retention system (active recall, spaced repetition, project-based learning)
  - `CONTRIBUTING.md` — style guide and standards
  - `PROGRESS_TRACKER.md` — personal progress checklist
  - `RESOURCES.md` — curated external resources
  - `GLOSSARY.md` — master glossary index
  - `FAQ.md` — frequently asked questions
  - `CHANGELOG.md` — this file

### Notes
- Planning phase complete. Module content authoring begins next, one module at a time.
