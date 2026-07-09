# Quiz · Module 03 — Linux for AI Engineers

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md) · [✅ Answers](answers-01.md)

> 28 questions across all 16 concept lessons. Answer from memory first, then check [answers-01.md](answers-01.md). Scoring at the bottom.

---

### Part 1 — Foundations (03.1–03.3)
1. What's the difference between the kernel, the OS, and a distribution?
2. Why are Docker and Kubernetes fundamentally Linux technologies?
3. What is a system call, and what is the user/kernel boundary?
4. What does "everything is a file" mean in Linux?
5. Why should AI datasets live on `/data` and not `/`?

### Part 2 — Terminal & Commands (03.4–03.5)
6. What are stdin/stdout/stderr, and why are stdout and stderr separate?
7. How does the shell decide which `python` to run?
8. What's the difference between `find` and `grep`?
9. Why is `tail -f` essential when running training jobs?
10. Why must you `sort` before `uniq -c`?

### Part 3 — Permissions, Processes, Services (03.6–03.8)
11. Decode `-rwxr-x---`; what's the risk of `chmod 777`?
12. What's the difference between `x` on a file vs a directory?
13. Why use `tmux` for long training jobs?
14. SIGTERM vs SIGKILL — which first and why?
15. What's the difference between `systemctl start` and `enable`?
16. Why does a service work in your shell but fail under systemd?

### Part 4 — Networking, Storage, Logs (03.9–03.11)
17. Why use SSH keys instead of passwords, and how is the private key protected?
18. `scp` vs `rsync` for a large dataset?
19. A service runs but is unreachable remotely — two common causes?
20. The disk-full debugging drill?
21. A process vanished with no app error — where do you look?
22. How do you read a systemd service's logs live?

### Part 5 — Scripting, Envs, Performance, Security, Docker (03.12–03.16)
23. What does `set -euo pipefail` do, and why quote variables?
24. Why never `sudo pip install` into system Python?
25. Why isn't low `free` memory a problem, and what IS a red flag?
26. Your GPU is 30% utilized during training — what's happening and how do you diagnose it?
27. What's the security baseline for a public AI server (name 4 controls)?
28. What is a container in terms of Linux features?

---

### Scoring

| Score | Meaning |
|---|---|
| 25–28 | Excellent — proceed to Module 04 |
| 20–24 | Good — review missed lessons' summaries/flashcards |
| 14–19 | Reread the weaker lessons before continuing |
| < 14 | Rework the module — Linux fluency is foundational |

> [!TIP]
> Every missed question maps to a lesson. But Linux is practical — for any you miss, *do the command* on a real system, not just reread.
