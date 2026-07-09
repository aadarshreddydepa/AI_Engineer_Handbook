# Exercises · Module 03 — Linux for AI Engineers

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md)

> A structured set spanning all 16 concept lessons — terminal drills, debugging labs, log analysis, file/permission tasks, and bash challenges — with a deliberate difficulty ramp per the [exercise standards](../../../standards/exercise-standards.md). **Do these on a real Linux system** (WSL2, container, or cloud VM), keeping a terminal open.

**Difficulty:** ⭐ warm-up · ⭐⭐ practice · ⭐⭐⭐ challenge · ⭐⭐⭐⭐ stretch. **Types:** 🖥️ Terminal · 🐞 Debug · 📊 Log analysis · 📁 File/permission · 📜 Bash.

---

## 03.1 · Introduction
- [ ] **⭐ 🖥️** Get a Linux environment; run `uname -a`, `cat /etc/os-release`; identify your kernel and distro.
- [ ] **⭐⭐ 🖥️** Explain (in writing) why your AI deployment target is Linux, covering GPU/cost/containers.

## 03.2 · Architecture
- [ ] **⭐ 🖥️** Run `lsmod`; identify modules and what hardware they support.
- [ ] **⭐⭐ 🖥️** Run `strace -c ls`; identify `openat`/`read`/`write`/`stat` syscalls.
- [ ] **⭐⭐⭐ 🐞** `strace` a failing command; find the exact failing syscall and fix the cause.

## 03.3 · Filesystem
- [ ] **⭐ 🖥️** Explore `/`, `/etc`, `/var/log`, `/proc`; `cat /proc/meminfo`; `stat` a file.
- [ ] **⭐⭐ 📁** Create a symlink to a directory; break it; repoint with `ln -sfn`.
- [ ] **⭐⭐ 📁** Design and create a sensible AI project layout (data/models/code/logs); justify locations.

## 03.4 · Terminal
- [ ] **⭐ 🖥️** Redirect stdout and stderr separately, then merge with `2>&1`.
- [ ] **⭐⭐ 🖥️** Build a pipeline finding the 5 most common words in a text file.
- [ ] **⭐⭐ 🖥️** Set/export an env var; use `which`/`echo $PATH` to explain which `python` runs; activate a venv and observe PATH change.

## 03.5 · Commands
- [ ] **⭐⭐ 📊** Produce a value-count table for a CSV column (`cut | sort | uniq -c | sort -rn`).
- [ ] **⭐⭐ 🖥️** Sum a numeric column with `awk`; bulk-replace with `sed` (test before `-i`).
- [ ] **⭐⭐⭐ 📁** Safely delete files matching a pattern, handling spaces (`find -print0 | xargs -0`), previewing first.

## 03.6 · Permissions
- [ ] **⭐ 📁** Decode 6 permission strings/octals.
- [ ] **⭐⭐ 📁** Set `600` on a fake secret, `755` on a script, `700` on a dir; verify.
- [ ] **⭐⭐⭐ 📁** Audit SUID binaries (`find / -perm -4000`); explain why `passwd` needs it.

## 03.7 · Processes
- [ ] **⭐ 🖥️** Launch `sleep 1000 &`; find it with `ps`/`jobs`/`pgrep`; note PID and state.
- [ ] **⭐⭐ 🖥️** Run a job in `tmux`; detach, "disconnect", reattach, find it still running.
- [ ] **⭐⭐ 🖥️** Send SIGTERM then SIGKILL; observe the difference in cleanup.
- [ ] **⭐⭐⭐ 🐞** Create a zombie; observe it in `ps`; explain why you can't kill it directly.

## 03.8 · systemd
- [ ] **⭐ 🖥️** `systemctl status`/`start`/`stop` an existing service; read its output.
- [ ] **⭐⭐⭐ 🖥️** Write a unit file for a Python HTTP server; run as non-root with `Restart=on-failure`; verify.
- [ ] **⭐⭐⭐ 🐞** Use a relative path in `ExecStart`, watch it fail, diagnose via `journalctl`, fix with absolute path.

## 03.9 · Networking
- [ ] **⭐⭐ 🖥️** Generate an ed25519 key; set up key-based login to a VM/container; confirm passwordless SSH.
- [ ] **⭐⭐ 🖥️** Copy a dir with `scp -r`, then re-sync with `rsync -avz --progress`; observe rsync transferring only changes.
- [ ] **⭐⭐⭐ 🐞** Start a service bound to `localhost`; confirm unreachable remotely; rebind to `0.0.0.0`; verify with `ss`/`curl`.

## 03.10 · Storage
- [ ] **⭐ 🖥️** Run `df -h`, `lsblk`, `du -sh`; identify the largest directory.
- [ ] **⭐⭐ 🐞** Simulate a space hog; use `du | sort -rh` to locate it; clean up.
- [ ] **⭐⭐ 🖥️** Create many tiny files; compare `df -h` vs `df -i`.

## 03.11 · Logs
- [ ] **⭐ 📊** Use `journalctl -u <svc>` with `--since` and `-p err`; follow with `-f`.
- [ ] **⭐⭐ 📊** Analyze `auth.log` (or a sample) to count failed SSH attempts per source IP.
- [ ] **⭐⭐⭐ 🐞** Run the full debug drill (status → journalctl → dmesg → resources) on a "down service" scenario.

## 03.12 · Bash
- [ ] **⭐ 📜** Script with shebang + `set -euo pipefail`, a required arg (usage check), timestamped output.
- [ ] **⭐⭐ 📜** Script with a conditional (dir exists?) and a loop processing files.
- [ ] **⭐⭐⭐ 📜** Script with `trap cleanup EXIT`, quoted vars, `${VAR:?}` guards; run `shellcheck` and fix all warnings.

## 03.13 · Packages & Envs
- [ ] **⭐⭐ 🖥️** Create a venv and a uv env; install into each; show isolation (different `which python`).
- [ ] **⭐⭐⭐ 🖥️** Create an env, produce a lockfile, delete the env, recreate from the lockfile — confirm identical.

## 03.14 · Performance
- [ ] **⭐⭐ 🖥️** Generate CPU load and I/O load; watch `vmstat` distinguish CPU-bound (`r`/`us`) vs I/O-bound (`wa`/`b`).
- [ ] **⭐⭐ 🖥️** Allocate memory until swap engages; observe `free` and `vmstat si/so`.
- [ ] **⭐⭐⭐ 🖥️** If a GPU is available, run training, check `nvidia-smi`; if underutilized, diagnose the bottleneck.

## 03.15 · Security
- [ ] **⭐⭐ 🖥️** (In a VM) set up key-only SSH; disable password login; verify.
- [ ] **⭐⭐ 🖥️** Configure UFW default-deny + allow SSH + one app port; verify.
- [ ] **⭐⭐⭐ 📁** Mini security audit: SUID (`find / -perm -4000`), open ports (`ss -tlnp`), failed logins, world-writable files.

## 03.16 · Docker Prep
- [ ] **⭐⭐ 🖥️** `docker run -it ubuntu bash`; inside, `ps aux`/`ip addr`/`ls /` to see isolation; compare to host.
- [ ] **⭐⭐ 🐞** Run a container with `--memory=256m` and a program that over-allocates; observe the OOM-kill.
- [ ] **⭐⭐⭐ 🖥️** Build a small image with deps-before-code vs after; compare rebuild times after a code change.

## Projects
- [ ] Build **Project 5 (Deployment Automation)** and **Project 6 (Server Health & Security Checker)** at minimum.
- [ ] Execute the full **"day in the life" workflow** ([03.17](../weeks/03.17-workflow-projects-summary.md)) end-to-end.

---

## Completion criteria

- [ ] Every ⭐/⭐⭐ exercise attempted on a real Linux system
- [ ] At least four ⭐⭐⭐ challenges solved (incl. one debug + one bash)
- [ ] The deployment automation and health/security checker scripts work (`shellcheck`-clean)
- [ ] You can execute the "day in the life" workflow comfortably
- [ ] You can tick the [03.17 mastery checklist](../weeks/03.17-workflow-projects-summary.md#module-03-mastery-checklist-from-memory--on-a-real-system)

> [!TIP]
> Linux is muscle memory — the debugging (🐞) and bash (📜) exercises build the reflexes you'll use daily. Type every command; don't just read.
