# Quiz · Module 04 — Advanced Git & Collaboration

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md) · [✅ Answers](answers-01.md)

> 26 questions across all 12 concept lessons. Answer from memory first, then check [answers-01.md](answers-01.md). Scoring at the bottom.

---

### Part 1 — Internals & History (04.1–04.2)
1. Is a commit a diff or a snapshot? Explain.
2. What is a branch internally, and what is HEAD?
3. What is the reflog, and why does it make Git nearly loss-proof?
4. How many parents does a merge commit have?
5. Fast-forward vs three-way merge — when does each happen?
6. What is detached HEAD, and how do you avoid losing work in it?

### Part 2 — Branching & Advanced Ops (04.3–04.4)
7. What invariant do all branching strategies protect?
8. Compare GitHub Flow, Git Flow, and trunk-based development.
9. What's the hotfix pattern, and the classic mistake?
10. Merge vs rebase — when each? Why is rebasing a shared branch dangerous?
11. Explain the three reset modes.
12. Reset vs revert — which for shared history, and why?

### Part 3 — Conflicts, Tags, Collaboration (04.5–04.7)
13. Is a merge conflict an error? What do the markers mean?
14. What's the best way to *prevent* merge conflicts?
15. Lightweight vs annotated tags; explain SemVer.
16. What must be versioned together for AI reproducibility?
17. What is a pull request, and why keep PRs small?
18. What do protected branches enforce?

### Part 4 — Repo Mgmt, Large Files, Automation, CI, Debugging (04.8–04.12)
19. What does CODEOWNERS do, and why is a LICENSE essential for OSS?
20. Why is committing large binaries to Git bad, and how does Git LFS help?
21. You added a file to `.gitignore` but it's still tracked — why, and how do you fix it?
22. Why use the `pre-commit` framework, and what belongs in pre-commit vs CI?
23. Why is CI the "unbypassable" quality gate? How do you handle secrets in Actions?
24. First move when you've broken your Git? How do you recover lost commits?
25. How do you recover from a force-push that erased commits, and how do you prevent it?
26. What is `git bisect` and how does it work?

---

### Scoring

| Score | Meaning |
|---|---|
| 23–26 | Excellent — proceed to Module 05 |
| 18–22 | Good — review the missed lessons' summaries/flashcards |
| 13–17 | Reread the weaker lessons before continuing |
| < 13 | Rework the module — Git fluency is foundational |

> [!TIP]
> Every missed question maps to a lesson. For recovery questions, *do the drill* on a throwaway repo — Git is learned by breaking and fixing.
