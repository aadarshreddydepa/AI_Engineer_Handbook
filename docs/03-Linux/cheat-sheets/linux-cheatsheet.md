# Cheat Sheet · Module 03 — Linux for AI Engineers

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md)

> One-page reference for the whole module. Scan it; learn it in the [lessons](../weeks/README.md). Keep a terminal open.

---

## Foundations (03.1–03.3)

```text
KERNEL(core) ⊂ OS(kernel+tools) ⊂ DISTRO(packaged, e.g. Ubuntu=apt) · AI/cloud/Docker/K8s ALL run on Linux
ARCH: [user space: apps/shell/libc] —(SYSCALLS)→ [kernel: scheduler/memory/VFS/net/drivers] → hardware
  user mode(isolated) vs kernel mode(hw access) · strace <cmd> = watch syscalls · NVIDIA driver = kernel module
FILESYSTEM: ONE tree from / · "everything is a file" · storage MOUNTED in (no drive letters)
  /home(~) · /etc config · /var/log logs · /tmp scratch(volatile) · /dev devices(/dev/nvidia0,/dev/null) · /proc kernel info · /data(mount big data here, NOT /)
  paths: absolute /a/b(prod!) · ~ home · . here · .. up · inode=metadata (stat, ls -li, df -i)
  ln -s target link (symlink → atomic version swap: ln -sfn v4 current)
```

## Terminal & commands (03.4–03.5)

```text
STREAMS: stdin(0) stdout(1) stderr(2) · REDIRECT: > overwrite · >> append · 2>&1 merge · >/dev/null 2>&1 silent
PIPE: cmd1 | cmd2 (stdout→stdin) · tee file(save+pass) · e.g. cat log | grep ERROR | sort | uniq -c | sort -rn | head
ENV/PATH: export VAR=val · which python(what runs) · venv PREPENDS bin · CUDA_VISIBLE_DEVICES=0,1 (assign GPUs)
  secrets → .env chmod 600 (NOT export on CLI) · NEVER . in PATH
GLOB (shell expands FIRST): * ? [abc] {a,b} · ls the pattern before rm-ing!
NAV: ls -lh/-la/-lt · cd - · FILES: cp -r · mv · mkdir -p · rm -rf ⚠️IRREVERSIBLE (guard "${DIR:?}")
VIEW: less(big) · head/tail · TAIL -F(live log!) · wc -l · diff
SEARCH: find(files: -name -size -mtime) vs grep(content: -r -i -n -c -v)
TEXT: cut -d, -fN · sort -n/-r · uniq -c(SORT FIRST) · awk -F, '{s+=$2}END{print s}' · sed 's/old/new/g' · xargs (-print0|-0, -P parallel)
```

## Permissions, processes, services (03.6–03.8)

```text
PERMS: ls -l [type][owner rwx][group][others] · octal r4 w2 x1 → 600 secrets · 755 script/dir · 644 file · 777 ⚠️NEVER
  file: x=RUN · DIR: x=ENTER r=list · chmod 600 .env · chmod +x script · chown svc:svc /app (real deploy fix)
  SUID(runs as owner: find / -perm -4000) · sticky(/tmp) · least privilege · non-root services
PROCESS: ps aux|grep · top/htop · nvidia-smi(GPU!) · states R/S/D(io-stuck)/Z(zombie→kill parent) · all descend from PID 1
  ★ tmux new -s x → run → Ctrl-b d → tmux attach (LONG JOBS survive SSH drop!) · nohup cmd &
  kill PID=SIGTERM(graceful, saves checkpoint) → kill -9=SIGKILL(force) · pkill -f · nice -n 10
SYSTEMD (PID 1): systemctl status/start/stop/restart · enable --now(start+onboot) · daemon-reload
  unit /etc/systemd/system/x.service: User=svc(non-root) · ExecStart=/ABS/path/.venv/bin/python · Restart=on-failure · EnvironmentFile=.env
  journalctl -u <svc> [-f] [--since] [-p err] · systemd = clean env (absolute paths!)
```

## Networking, storage, logs (03.9–03.11)

```text
NET: ip addr · localhost=127.0.0.1(this machine only!) · dig name · /etc/hosts
  SSH (front door): ssh user@host · keys not passwords (ssh-keygen -t ed25519, ssh-copy-id, private key chmod 600)
  ~/.ssh/config (Host gpu...) · tunnel: ssh -L 8888:localhost:8888 gpu (remote Jupyter/TensorBoard)
  TRANSFER: rsync -avz --progress --partial src/ host:/dst/ (diffs, resumable — for datasets/models) · scp(one-off)
  DEBUG: ss -tlnp(listening+proc) · curl -v · ping · dig · "can't reach": bind 0.0.0.0 not localhost? firewall/security group?
STORAGE: disk→partition→filesystem(ext4/xfs)→MOUNT · df -h(free, CHECK FIRST) · du -sh dir/*|sort -rh(hogs) · lsblk · df -i(inodes)
  DISK-FULL DRILL: df -h → du|sort -rh → clean · fstab(persist mount by UUID) · data on /data NOT /
LOGS: journalctl -u <svc> [-f] · /var/log/(syslog,auth.log) · dmesg|grep "killed process"(OOM!)|nvidia(GPU)
  rotate to avoid disk-full (logrotate, journalctl --vacuum-size=) · DEBUG DRILL: systemctl status → journalctl → dmesg → df/free
```

## Scripting, envs, performance, security, Docker (03.12–03.16)

```text
BASH: #!/usr/bin/env bash · set -euo pipefail(ALWAYS) · "${VAR}"(quote!) · ${1:?usage} ${2:-default}
  [[ -f/-d/-z ]] · for f in *.csv · while IFS= read -r line · f(){ local x=$1; } · exit codes(0 ok) · trap cleanup EXIT · shellcheck
  bash=orchestrate(<50 lines) · Python=logic
PACKAGES: SYSTEM apt(update first! install build-essential) vs PYTHON venv/conda/uv (NEVER sudo pip into system!)
  conda installs CUDA/binary deps · uv=fast default · commit LOCKFILE not env dir · ~/.bashrc(interactive; NOT services)
PERFORMANCE: 4 bottlenecks CPU/RAM/DISK/NET (+GPU) · uptime(load vs nproc) · free(AVAILABLE not free; swap=bad)
  vmstat(r=cpu, wa=io wait, si/so=swap) · iostat -x(%util,await) · sar(history) · GPU low util=STARVED→more workers/faster storage
SECURITY (defense in depth): SSH key-only(no password/root) · UFW default-deny (allow 22 BEFORE enable!) · Fail2Ban · secrets .env 600 (never git/args/logs, rotate) · apt upgrade · non-root
DOCKER = NAMESPACES(isolation: pid/net/mount/user) + CGROUPS(limits: cpu/mem→OOM) + UNION FS(layers, cache: deps before code)
  container = isolated PROCESS on host kernel (NOT a VM) · run non-root · never bake secrets
```

## The AI Engineer's daily loop

```text
ssh gpu (03.9) → nvidia-smi/df -h/free -h recon (03.7/03.10/03.14) → tmux (03.7) → activate env (03.13)
→ rsync dataset to /data (03.9/03.10) → CUDA_VISIBLE_DEVICES=0 python train.py > log 2>&1 (03.4/03.7)
→ detach; watch nvidia-smi + tail -f log (03.5/03.7) → diagnose slow: vmstat/iostat (03.14)
→ rsync backup model (03.9) → systemctl enable --now model-api (03.8) → journalctl/dmesg debug (03.11)
```
