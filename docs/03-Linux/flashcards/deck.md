# Flashcards · Module 03 — Linux for AI Engineers

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md)

> Active-recall deck for the whole module. Answer **out loud before flipping**. Review on the [spaced-repetition schedule](../../../LEARNING_STRATEGY.md): same day, +1d, +3d, +7d, +16d, +35d. A failed card resets to interval 1.

---

## 03.1 · Introduction
**Q:** Kernel vs OS vs distribution?
**A:** Kernel = core managing hardware (Linux); OS = kernel + system libraries/tools; distribution = a complete packaged OS (Ubuntu, Fedora) with a package manager and defaults.

**Q:** Why do Docker and Kubernetes fundamentally require Linux?
**A:** Containers are built on Linux kernel features (namespaces + cgroups); Kubernetes orchestrates Linux containers across Linux nodes.

---

## 03.2 · Architecture
**Q:** What is a system call?
**A:** A request from a user-space program to the kernel for a privileged service (file I/O, process creation, networking) — the only legitimate way across the user/kernel boundary.

**Q:** What does `strace` do? — **A:** Traces every system call a program makes, revealing exactly what it tried to do at the kernel boundary — invaluable for debugging permission/file/config issues.

---

## 03.3 · Filesystem
**Q:** What does "everything is a file" mean? — **A:** Data, directories, devices (`/dev`), and kernel/process state (`/proc`) are all accessed through the same file interface.

**Q:** AI use of a `current` symlink? — **A:** Point it at the active model version; atomically repoint (`ln -sfn`) to deploy/rollback instantly without copying data.

---

## 03.4 · Terminal
**Q:** What does a pipe (`|`) connect? — **A:** The stdout of one program to the stdin of the next, streaming data through a chain of tools with no temp files.

**Q:** How do AI apps get config/secrets and assign GPUs? — **A:** Environment variables — a `.env` file for secrets, and `CUDA_VISIBLE_DEVICES` to restrict which GPUs a job uses.

**Q:** How does the shell decide which `python` runs? — **A:** It searches `PATH` directories in order and runs the first match (`which python`); a virtualenv prepends its `bin/`.

---

## 03.5 · Commands
**Q:** `find` vs `grep`? — **A:** `find` searches for *files* (by name/size/time); `grep` searches *content* (matching lines) in files or piped input.

**Q:** Why is `tail -f` essential for AI work? — **A:** It follows a log live, streaming new lines — how you watch training loss/errors in real time.

**Q:** Why `sort` before `uniq -c`? — **A:** `uniq` only collapses *adjacent* duplicates; unsorted data leaves non-adjacent dupes uncounted.

---

## 03.6 · Permissions
**Q:** Why `chmod 600` for a `.env`? — **A:** Owner read/write only — no one else can read the secrets it contains.

**Q:** Real fix for a service's "permission denied" (not 777)? — **A:** `chown` the files to the service user and set minimal permissions (least privilege), not `chmod 777`.

**Q:** What does `x` mean on a directory? — **A:** Permission to enter/traverse it (`cd`, access files inside) — different from `r` (list contents).

---

## 03.7 · Processes
**Q:** Why use `tmux` for long training jobs? — **A:** It creates a persistent server-side session that keeps running after you disconnect; you can detach and reattach to monitor.

**Q:** SIGTERM vs SIGKILL? — **A:** SIGTERM (`kill`) asks for graceful shutdown (save checkpoint, clean up); SIGKILL (`kill -9`) force-kills with no cleanup — use only when stuck.

**Q:** Why is `nvidia-smi` essential? — **A:** Shows GPU utilization/memory and which processes use each GPU — to confirm training uses the GPU, find hogs, and diagnose CUDA OOM.

---

## 03.8 · systemd
**Q:** `systemctl start` vs `enable`? — **A:** `start` runs a service now (not after reboot); `enable` starts it on boot (not now) — usually want both (`enable --now`).

**Q:** Why does a service work in your shell but fail under systemd? — **A:** systemd runs with a clean, minimal environment from `/`; relative paths and assumed env vars break — use absolute paths and `Environment=`.

---

## 03.9 · Networking
**Q:** Why SSH keys over passwords? — **A:** Far more secure (no password to brute-force/phish) and convenient; cloud GPU instances require them. Private key stays secret, `chmod 600`.

**Q:** `scp` vs `rsync` for a large dataset? — **A:** `rsync` — transfers only differences, compresses, shows progress, and resumes interrupted transfers.

**Q:** Two common causes of "service runs but unreachable"? — **A:** It bound to `localhost` (not `0.0.0.0`), or a firewall/security group blocks the port.

---

## 03.10 · Storage
**Q:** The disk-full debugging drill? — **A:** `df -h` to find the full filesystem, then `du -sh /path/* | sort -rh | head` to find the hog; if free space but writes fail, `df -i` (inodes).

**Q:** Why keep datasets off `/`? — **A:** Filling the root partition destabilizes/breaks the whole system; put big/growing data on a separate mounted volume (`/data`).

---

## 03.11 · Logs
**Q:** A process vanished with no app error — where do you look? — **A:** `dmesg` (`dmesg | grep -i "killed process"`) to see if the kernel OOM-killer terminated it (out of memory).

**Q:** How do you read a systemd service's logs live? — **A:** `journalctl -u <service> -f`, filterable by `--since`, `-p err`, `-b`.

---

## 03.12 · Bash
**Q:** What does `set -euo pipefail` do? — **A:** `-e` exit on error, `-u` error on undefined variables, `-o pipefail` catch pipeline failures — makes scripts fail loudly/safely instead of silently continuing.

**Q:** Why quote bash variables? — **A:** To prevent word-splitting and empty-variable disasters (e.g., `rm -rf $DIR/` becoming `rm -rf /` when `DIR` is empty).

---

## 03.13 · Packages & Envs
**Q:** Why never `sudo pip install` into system Python? — **A:** OS tools depend on the system Python's packages; changing them can break the operating system.

**Q:** Why is conda popular for ML? — **A:** It can install non-Python system dependencies (CUDA, cuDNN, compiled libs) inside the environment, avoiding system/PyTorch CUDA mismatches.

---

## 03.14 · Performance
**Q:** Why isn't low `free` memory a problem? — **A:** Linux uses "free" RAM as reclaimable page cache; look at `available`. The real red flag is swap being used.

**Q:** GPU only 30% utilized during training — what's happening? — **A:** The GPU is starved by another resource (CPU preprocessing, disk data-loading, or RAM/swap); diagnose with vmstat/iostat and fix the feeder.

---

## 03.15 · Security
**Q:** What is defense in depth? — **A:** Layering multiple security controls so if one is breached, others still protect the system.

**Q:** What must you do before `ufw enable`? — **A:** `ufw allow 22/tcp` (SSH) — enabling a default-deny firewall without allowing SSH locks you out of a remote server.

**Q:** How do you handle secrets on a server? — **A:** Store in `.env` with `chmod 600` owned by the app user (or a secrets manager); never hard-code, commit, pass as CLI args, or log; rotate if leaked.

---

## 03.16 · Docker Prep
**Q:** What is a container, really? — **A:** An isolated Linux *process* on the host kernel, made to look like a separate machine using namespaces, cgroups, and a union filesystem — not a VM.

**Q:** Namespaces vs cgroups? — **A:** Namespaces isolate what a container *sees* (PIDs, network, filesystem, users); cgroups limit what it *uses* (CPU, memory, I/O).

**Q:** Why does Dockerfile layer order matter? — **A:** Layers are cached; ordering least- to most-frequently-changed (deps before code) lets slow dependency installs be reused across rebuilds.

---

> [!TIP]
> When you can answer every card across two spaced reviews AND execute the "day in the life" workflow, Module 03 is locked in.
