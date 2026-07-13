# Cheat Sheet · Module 05 — Databases & Data Engineering

[🏠 Module](../README.md) · [📚 Lessons](../weeks/README.md)

> One-page reference for the whole module. Scan it; learn it in the [lessons](../weeks/README.md). Keep a PostgreSQL running.

---

## Foundations (05.1–05.2)

```text
DB gives you (files can't): 1 CONCURRENCY · 2 INDEXED SPEED (O(log n) not O(n)) · 3 DURABILITY (ACID) ·
  4 STRUCTURE (schema) · 5 QUERYABILITY (declarative SQL) [+ access control]
DATA SHAPES: structured→relational · semi (JSON/logs)→JSONB/document · unstructured (text/img)→object storage
★ AI PATTERN: raw object → OBJECT STORAGE · metadata → POSTGRES · embedding → pgvector/vector DB
RELATIONAL PRINCIPLE: each fact stored EXACTLY ONCE (duplication → drift → data lies)
KEYS: PK(surrogate id, not email) · FK(referential integrity) · relationships: 1:many=FK · 1:1=FK+UNIQUE · many:many=JOIN TABLE
NORMALIZE TO 3NF (fixes update/insert/delete anomalies): "the key, the whole key, and nothing but the key"
DENORMALIZE deliberately (measured) → routine in analytics/warehouses, last resort in apps
```

## SQL (05.3–05.4)

```text
SELECT cols FROM t WHERE row_cond GROUP BY g HAVING agg_cond ORDER BY c LIMIT n;
LOGICAL ORDER: FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
★ WHERE filters ROWS (before grouping) · HAVING filters GROUPS (after aggregation)
JOINS: INNER = only matches (⚠️ SILENTLY DROPS unmatched rows!) · LEFT = all left + NULLs
  ANTI-JOIN (rows with no match): LEFT JOIN b ON ... WHERE b.id IS NULL
  ⚠️ missing ON = CROSS JOIN = cartesian explosion
WRITE: ⚠️ UPDATE/DELETE ALWAYS WITH WHERE (no WHERE = whole table!) — SELECT first; BEGIN...ROLLBACK
  UPSERT (idempotent!): INSERT ... ON CONFLICT (key) DO UPDATE SET c = EXCLUDED.c
NULL = UNKNOWN: NULL = NULL is NULL → use IS NULL · COALESCE(x, default) · ⚠️ NOT IN + NULL returns NOTHING → NOT EXISTS
CTE (readability): WITH a AS (...), b AS (SELECT ... FROM a) SELECT ... FROM b;  · WITH RECURSIVE for hierarchies
★★ WINDOW FUNCTIONS (per-row calc WITHOUT collapsing rows): fn() OVER (PARTITION BY g ORDER BY c)
  ROW_NUMBER/RANK · LAG/LEAD · SUM/AVG OVER (running) · NTILE
  ★ TOP-N PER GROUP: WITH r AS (SELECT *, ROW_NUMBER() OVER (PARTITION BY g ORDER BY s DESC) rn FROM t) SELECT * FROM r WHERE rn<=3;
VIEW = saved query (abstraction + security) · MATERIALIZED VIEW = stored result (fast, must REFRESH — a cache)
TRIGGERS/PROCS: sparingly (hidden side effects) — ok for updated_at/audit, NOT business logic
SECURITY: ALWAYS parameterized queries (%s) — NEVER f-string SQL (injection, esp. LLM values!)
```

## Optimization & Transactions (05.5–05.6)

```text
★ EXPLAIN ANALYZE FIRST (never optimize blind) — RED FLAGS: "Seq Scan" on a big table · huge "Rows Removed by Filter"
  good: Index Scan · BEST: Index Only Scan (covering) · est rows ≠ actual → ANALYZE table (stale stats)
INDEXES: B-TREE (default: equality + RANGES + sorting) · HASH(= only) · GIN(JSONB/full-text) · HNSW(vectors)
  COMPOSITE (a,b,c) → ★ LEFTMOST-PREFIX: serves a, (a,b), (a,b,c) — NOT b alone! (equality col FIRST, range/sort SECOND)
  COVERING index → Index Only Scan (this is why SELECT * hurts!)
  ⚠️ NOT FREE: slows every write, uses disk · defeated by: fn on column (→ expression index), LIKE '%x', low selectivity
  INDEX your FOREIGN KEYS (commonly forgotten!)
N+1 PROBLEM (app-side, no index fixes it): 1 query + 1 per row → use ONE JOIN or WHERE id IN (...)
ACID: Atomicity · Consistency · Isolation · Durability(WAL)
ISOLATION: Read Uncommitted < READ COMMITTED (PG default) < Repeatable Read < Serializable
  ⚠️ Read Committed ALLOWS the LOST UPDATE (the credit-deduction bug!)
  ✅ FIX: UPDATE users SET credits = credits - 10 WHERE id=1 AND credits>=10  (atomic in DB)  or  SELECT ... FOR UPDATE
DEADLOCK: circular lock wait → acquire locks in a CONSISTENT ORDER + short txns + RETRY
MVCC (Postgres): row versions → READERS DON'T BLOCK WRITERS · needs VACUUM (bloat if autovacuum lags)
JOB QUEUE: SELECT ... FOR UPDATE SKIP LOCKED
⚠️ NEVER call an LLM/network API inside an open transaction (holds locks for seconds!)
```

## NoSQL, Modeling, Warehouses (05.7–05.9)

```text
NoSQL = TRADE-OFFS (gain scale/flex, lose JOINs/ACID/ad-hoc): DOCUMENT(Mongo — try PG JSONB first!) ·
  KEY-VALUE(Redis: ★ CACHE, rate limits, queues) · WIDE-COLUMN(Cassandra: huge writes) · GRAPH(Neo4j: traversal, knowledge graphs)
CAP (during a PARTITION): Consistency (reject) OR Availability (serve stale = eventual consistency)
★ PRAGMATIC AI STACK: Postgres + Redis + object storage + pgvector
OLTP (app): NORMALIZED, small reads/writes  vs  OLAP (warehouse): DENORMALIZED star, huge aggregations, COLUMNAR
★ STAR SCHEMA: FACT table (measures + FKs to dims — huge) + DIMENSIONS (who/what/when — small, denormalized)
  always build dim_date · SNOWFLAKE (normalized dims) = more JOINs → prefer STAR
  SCD TYPE 2: don't overwrite → new row with valid_from/valid_to (preserves history)
  ★ POINT-IN-TIME CORRECTNESS: join dims as they were AT EVENT TIME (else DATA LEAKAGE!)
COLUMNAR STORAGE = the warehouse innovation (read only the needed column: 10-100× less I/O + great compression)
WAREHOUSE(structured, modeled) · LAKE(raw, any format, cheap — ⚠️ DATA SWAMP without governance) ·
  LAKEHOUSE(★ ML default: Delta/Iceberg = ACID + schema + TIME TRAVEL over Parquet)
PLATFORMS: Snowflake · BigQuery(⚠️ PAY PER BYTE SCANNED) · Redshift · Databricks(ML) — but < ~100GB → JUST USE POSTGRES
```

## Pipelines & AI Data (05.10–05.12)

```text
ELT (★ modern) > ETL: LOAD RAW first, transform in the warehouse (SQL/dbt) → keep raw = re-transform without re-extracting
STAGES: extract (INCREMENTAL w/ watermark; CDC) → VALIDATE → load → transform
VALIDATE AT INGESTION: schema · nulls · ranges · uniqueness · freshness · ★ VOLUME (rows vs 7-day avg)
  fail → QUARANTINE + ALERT (never publish corrupt data — stale > corrupt)
★★ IDEMPOTENCY (non-negotiable — retries/backfills WILL re-run): UPSERT · DELETE-then-INSERT partition · content-hash IDs
  non-idempotent + retry = DUPLICATES = silently biased models (and in AI, re-embedding costs REAL MONEY)
LAYERS (medallion): 🥉BRONZE raw (IMMUTABLE!) → 🥈SILVER cleaned → 🥇GOLD modeled
ORCHESTRATION (Airflow): DAG · tasks · schedule · RETRIES(backoff) · BACKFILL(needs idempotency)
  ★ a failed task HALTS downstream — never publish partial data
MONITOR THE DATA (not just the job): ★ FRESHNESS + ★ VOLUME = highest-value alerts · quality tests block publication
LINEAGE: ← debug backwards ("where did this number come from?") · → blast radius forwards ("which models used this?") · GDPR
★ MOST AI FAILURES ARE DATA FAILURES:
  LEAKAGE (looks like SUCCESS! suspiciously great scores → hunt it): target · temporal(→ point-in-time joins) · split(dedup!) · preprocessing(fit on train only)
    diagnostic: "at prediction time, would this value actually be available?"  (usually a JOIN bug)
  TRAINING/SERVING SKEW: feature computed 2 ways → diverges → FIX: ONE definition both paths (feature store)
  DRIFT: the world changes → models decay with NO code change → monitor input distributions → RETRAIN
REPRODUCIBILITY: version code(git tag) + data(snapshot/DVC/time travel) + features + model + env(lockfile)
```

## Security, Scaling, Vectors (05.13–05.15)

```text
★ 3 CONTROLS PREVENTING MOST BREACHES: 1 NEVER internet-facing (private subnet+firewall) · 2 LEAST-PRIVILEGE roles ·
  3 PARAMETERIZED queries
★ ROW-LEVEL SECURITY (multi-tenancy): POLICY (tenant_id = current_setting(...)) → kills the "forgot WHERE tenant_id" leak class
ENCRYPTION: in transit(TLS) · at rest · ★ BACKUPS TOO (protects stolen media, NOT attackers with creds)
BACKUPS/DR: full + WAL archiving → PITR (restore to just before the bad DELETE) · RPO/RTO · off-site
  ★★ AN UNTESTED BACKUP IS NOT A BACKUP → RESTORE DRILLS
SECRETS: manager/env/.env(600, gitignored) · NEVER in Git (persists forever → ROTATE) · never CLI args
★ LLM-GENERATED SQL = UNTRUSTED INPUT (prompt injection → DB command): READ-ONLY role on restricted VIEWS ·
  allowlist the SQL (no DDL/DML) · statement_timeout + row limits · RLS so RETRIEVAL respects the END USER's permissions
★★ SCALING LADDER (in order!): 1 INDEXES → 2 CACHE → 3 CONNECTION POOLING → 4 SCALE UP → 5 READ REPLICAS →
  6 PARTITIONING → 7 SHARDING (LAST RESORT — no cross-shard JOINs/transactions)
  "most teams that shard should have added an index"
  POOLING (PgBouncer) mandatory (PG = 1 process/conn) · ⚠️ never hold a conn during an LLM call
  REPLICAS: ⚠️ replication lag → "read-your-own-write" bug → route fresh-critical reads to the PRIMARY
  PARTITION by date: pruning + instant retention (DROP partition vs bloating DELETE)
EMBEDDING = meaning as GEOMETRY (similar text → nearby vectors) · deterministic → cacheable by content hash
  SQL matches EXACT values; AI needs MEANING ("refund" must find "money-back guarantee")
  exact k-NN O(N·d) 🐌 → ★ ANN: ~99% recall for ~1000× speed · HNSW = a GRAPH traversed greedily (Module 02.3!)
  ★ START WITH pgvector (vectors + SQL filters + JOINs + RLS in ONE system)
  ★ #1 RAG SECURITY BUG: retrieval that IGNORES PERMISSIONS → leaks another tenant's docs into the prompt!
```

## The golden rules

```text
1. Normalize the app; denormalize the warehouse.     6. Most AI failures are DATA failures (leakage/skew/drift).
2. EXPLAIN ANALYZE before optimizing.                 7. Never publish corrupt data (stale > corrupt).
3. Never UPDATE/DELETE without WHERE.                 8. Climb the scaling ladder in order (shard last).
4. Always parameterize queries (incl. LLM values).    9. Never expose a DB to the internet; least privilege + RLS.
5. Every pipeline task must be IDEMPOTENT.           10. An untested backup is not a backup.
```
