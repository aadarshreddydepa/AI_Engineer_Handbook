# Answers · Module 03 Quiz 01

[🏠 Module](../README.md) · [❓ Questions](quiz-01.md)

> Model answers with the *why*. If you got the gist but not the reasoning, reread the linked lesson — and *run the command* on a real system.

---

### Part 1 — Foundations

**1.** Kernel = the core managing hardware/processes/memory (Linux itself); OS = kernel + system libraries + tools; distribution = a complete packaged OS (Ubuntu, Fedora) with a package manager and defaults. → [03.1](../weeks/03.1-introduction.md)

**2.** Containers are built on Linux kernel features — **namespaces** (isolation) and **cgroups** (resource limits); Kubernetes orchestrates Linux containers across Linux nodes. Docker on Mac/Windows runs a hidden Linux VM. → [03.1](../weeks/03.1-introduction.md)/[03.16](../weeks/03.16-docker-preparation.md)

**3.** A system call is a request from a user-space program to the kernel for a privileged service (file I/O, process creation, networking). The user/kernel boundary is a hardware-enforced privilege separation: programs run in user mode and can't touch hardware directly — they must go through syscalls, which isolates faults and enforces security. → [03.2](../weeks/03.2-architecture.md)

**4.** Data, directories, devices (`/dev/nvidia0`, `/dev/null`), and even kernel/process state (`/proc`) are all accessed through the same file interface (open/read/write) — so the same tools work on all of them. → [03.3](../weeks/03.3-filesystem.md)

**5.** Filling the root partition (`/`) destabilizes or breaks the whole system (potentially unbootable). Big, growing data belongs on a separate mounted volume (`/data`) so it can't take down the OS. → [03.3](../weeks/03.3-filesystem.md)/[03.10](../weeks/03.10-storage.md)

### Part 2 — Terminal & Commands

**6.** stdin (0) = input, stdout (1) = normal output, stderr (2) = errors. They're separate so you can pipe/redirect results independently of errors (e.g., process output while still seeing/logging errors). → [03.4](../weeks/03.4-terminal-mastery.md)

**7.** It searches the directories in `PATH` in order and runs the first `python` it finds (`which python` shows it); activating a virtualenv prepends its `bin/` to PATH so its python wins. → [03.4](../weeks/03.4-terminal-mastery.md)

**8.** `find` searches for *files* by name/size/time/type (walking the tree); `grep` searches *content* (lines matching a pattern) in files or piped input. → [03.5](../weeks/03.5-essential-commands.md)

**9.** `tail -f` follows a log file live, streaming new lines as they're written — how you watch training loss, errors, or a server's activity in real time. → [03.5](../weeks/03.5-essential-commands.md)

**10.** `uniq` only collapses *adjacent* duplicate lines, so unsorted input leaves non-adjacent duplicates uncounted; `sort | uniq -c` groups them first. → [03.5](../weeks/03.5-essential-commands.md)

### Part 3 — Permissions, Processes, Services

**11.** `-rwxr-x---`: a file; owner rwx (7), group r-x (5), others none (0) → octal `750`. `chmod 777` grants everyone read/write/execute — a security hole; grant specific access to specific users instead. → [03.6](../weeks/03.6-permissions.md)

**12.** On a file, `x` = permission to run it as a program; on a directory, `x` = permission to enter/traverse it (`cd`, access files inside), while `r` = list its contents. → [03.6](../weeks/03.6-permissions.md)

**13.** `tmux` creates a persistent server-side session that keeps running after you disconnect (a plain shell job dies on SIGHUP); you can detach and reattach to monitor — so a long training run survives a dropped SSH connection. → [03.7](../weeks/03.7-processes.md)

**14.** SIGTERM (`kill`) first — it asks the process to shut down gracefully (finish writing a checkpoint, clean up). SIGKILL (`kill -9`) force-kills with no cleanup — reserve it for stuck processes, since it can corrupt a half-written checkpoint. → [03.7](../weeks/03.7-processes.md)

**15.** `start` runs the service now (but not after a reboot); `enable` makes it start automatically on boot (but not now). Production usually wants both: `systemctl enable --now`. → [03.8](../weeks/03.8-services-systemd.md)

**16.** systemd runs services with a clean, minimal environment from `/` (no shell PATH, aliases, or exported vars); relative paths and assumed env vars break. Fix with absolute paths in `ExecStart` and explicit `Environment=`/`EnvironmentFile=`. → [03.8](../weeks/03.8-services-systemd.md)

### Part 4 — Networking, Storage, Logs

**17.** Keys are far more secure (no password to brute-force/phish) and convenient; cloud GPU instances require them. The private key stays secret, `chmod 600` (SSH refuses over-permissive keys), and is never shared or committed. → [03.9](../weeks/03.9-networking.md)

**18.** `rsync` — it transfers only differences, compresses (`-z`), shows progress, and resumes interrupted transfers (`--partial`); `scp` restarts from scratch on failure. → [03.9](../weeks/03.9-networking.md)

**19.** It bound to `localhost`/`127.0.0.1` instead of `0.0.0.0` (all interfaces), or a firewall/cloud security group blocks the port. Diagnose with `ss -tlnp` and `curl`. → [03.9](../weeks/03.9-networking.md)

**20.** `df -h` to find which filesystem is full, then `du -sh /path/* | sort -rh | head` to find the space hog; if `df -h` shows free space but writes fail, run `df -i` (out of inodes — too many small files). → [03.10](../weeks/03.10-storage.md)

**21.** `dmesg` (`dmesg | grep -i "killed process"`) to see if the kernel OOM-killer terminated it (out of RAM) — the log that explains a mysterious exit-code-137 death. → [03.11](../weeks/03.11-logs.md)

**22.** `journalctl -u <service> -f` (follow), filterable by `--since`, `-p err`, `-b` (boot). → [03.11](../weeks/03.11-logs.md)

### Part 5 — Scripting, Envs, Performance, Security, Docker

**23.** `set -euo pipefail`: `-e` exit on any error, `-u` error on undefined variables, `-o pipefail` catch failures anywhere in a pipeline — so scripts fail loudly/safely instead of silently continuing. Quote variables (`"${VAR}"`) to prevent word-splitting and empty-variable disasters (e.g., `rm -rf $DIR/` → `rm -rf /`). → [03.12](../weeks/03.12-bash-scripting.md)

**24.** OS tools depend on the system Python's packages; changing them can break the operating system. Every project should use an isolated environment (venv/conda/uv) instead. → [03.13](../weeks/03.13-package-environment.md)

**25.** Linux uses "free" RAM as reclaimable page cache to speed file access, so low `free` is healthy — look at `available` for real headroom. The red flag is **swap being used**: paging to disk (~10⁴× slower) collapses performance and signals near-OOM. → [03.14](../weeks/03.14-performance-monitoring.md)

**26.** The GPU (the expensive resource) is being starved by another resource — CPU data preprocessing, disk data-loading, or RAM/swap. Diagnose: `nvidia-smi` (GPU busy?), then `vmstat` (high `r`=CPU, `wa`=I/O wait, `si`/`so`=swap) and `iostat -x` (disk `%util`). Fixes: more DataLoader workers, faster storage/formats, or smaller batch. → [03.14](../weeks/03.14-performance-monitoring.md)

**27.** Any four of: key-only SSH (no passwords/root login), a default-deny firewall (UFW) exposing only needed ports, Fail2Ban, non-root service users (least privilege), secrets in `chmod 600` files (never in Git/args/logs), regular patching (`apt upgrade`), and log/auth monitoring — layered as defense in depth. → [03.15](../weeks/03.15-security.md)

**28.** A container is an isolated Linux *process* running on the host's kernel (not a VM), made to look like a separate machine using three kernel features: **namespaces** (isolate what it sees — PIDs, network, filesystem, users), **cgroups** (limit what it uses — CPU, memory, I/O), and a **union/overlay filesystem** (layered, cached images). → [03.16](../weeks/03.16-docker-preparation.md)

---

> [!TIP]
> Turn every missed question into a flashcard *and run the relevant command* on a real Linux system — for this module, doing beats rereading.
