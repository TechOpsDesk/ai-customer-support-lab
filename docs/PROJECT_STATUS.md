# PixelVault AI Customer Support Lab — Project Status

**Updated:** 29 August 2026  
**Repository:** `TechOpsDesk/ai-customer-support-lab`  
**Local path:** `C:\Users\amir.omanovic\Projects\ai-customer-support-lab`  
**Branch:** `main`

## Current direction

The project is now **evaluation-first**.

The original full-stack chatbot build is not deleted, but it is no longer the v1 path. The immediate goal is to build a small, reusable system that can test a support chatbot against expected behaviour, authority limits, handoff rules, and policy grounding.

### One-line reframe

> Build the thing that judges chatbots before building another chatbot.

## Completed work

- S00 — Master plan and scope work — **complete**
- S01 — Repository setup and project rules — **complete**
- S02 — Synthetic data / ground-truth specification — **complete**
- S02 established the useful evaluation concepts:
  - Test Case / Ground Truth
  - Policy / Knowledge
  - expected action
  - required human handoff
  - required knowledge
  - forbidden behaviour (`must_not_do`)
  - severity
  - deterministic, inspectable test data

## Previous S03 status

The old S03 goal was:

> Generate the full deterministic synthetic PixelVault dataset.

That work is now **deferred**. It is not required for the first useful version of the project.

The full 11-entity dataset, Inventory, Technician Test Record, database loading, and broader synthetic generation may return later if they support a real evaluation need.

## New current phase

# E01 — Evaluation Harness Baseline

**Status:** CURRENT — verify/import/build the first runnable evaluator.

The first usable version should contain:

- PixelVault policy records
- PixelVault ground-truth test cases
- a loader with validation
- a chatbot adapter interface
- deterministic structural checks
- forbidden-behaviour checks
- severity-aware scoring
- explicit `UNJUDGED` results when a rule cannot yet be checked
- a readable evaluation report
- a deliberately bad stub bot for testing the evaluator itself
- automated tests

A previous external draft claimed an E01 package with 16 policies, 40 test cases, a scorer, report, adapter, stub bot, and tests. **Do not mark E01 complete until those files are actually present in this repository and run successfully on this machine.**

## v1 scope

### Keep in v1

- Test Case / Ground Truth
- Policy / Knowledge
- enough Customer / Order / Product / Shipment / Ticket context to make test cases concrete
- support authority rules
- human-handoff rules
- grounding checks
- forbidden-behaviour checks
- severity
- audit-style reporting
- vendor-neutral chatbot adapter
- PixelVault as the public reference/demo dataset
- repository discipline and automated tests

### Defer from v1

- Docker
- PostgreSQL
- pgvector
- Ollama
- FastAPI
- Chatwoot
- RAG stack
- full synthetic business dataset
- Inventory
- Technician Test Record
- web dashboard
- deployment stack
- full chatbot implementation

Deferred means **not on the critical path**, not permanently cancelled.

## Revised build order

### E01 — Evaluation Harness Baseline
Goal: one command runs the PixelVault cases against a stub bot and produces a report.

Definition of Done:

- evaluator files exist in the repo
- all test-case and policy files load successfully
- automated tests pass
- evaluator can run twice with consistent results
- critical failures are visible in the report
- uncheckable rules show `UNJUDGED`, never silent pass
- code is inspected before commit
- Git checkpoint is committed and pushed

### E02 — Make the Judge Trustworthy
Goal: reduce `UNJUDGED` coverage carefully.

Method:

- one behaviour rule at a time
- one positive test where the rule must trigger
- one negative test where it must not trigger
- avoid naive keyword-only false positives
- make small commits

Examples:

- discount / compensation promises
- delivery-date guarantees
- account deletion claims
- legal discussion
- AI identity disclosure
- unsupported policy claims
- chargeback handling
- unsafe repair instructions

### E03 — Vendor-Neutral Adapter + One Real Bot
Goal: point the evaluator at one real chatbot.

The adapter should support whatever the target bot can expose, for example:

- answer text
- action/tool name if available
- handoff state if available
- cited knowledge IDs if available
- raw provider response

Do not pretend to observe internal fields when testing a black-box bot that only returns text.

### E04 — Audit Report
Goal: turn evaluation output into a usable support-quality deliverable.

Report should include:

- executive summary
- overall score
- critical/high/medium/low failures
- test-case evidence
- expected behaviour
- actual behaviour
- violated policy/control
- handoff/authority finding
- remediation suggestion
- retest status

### E05 — Public PixelVault Demo
Goal: publish a complete before/after evaluation example.

PixelVault becomes the reference demonstration:

1. run a deliberately weak bot
2. show failures
3. fix selected failures
4. rerun
5. show improvement
6. document what the evaluator caught and what it could not judge

After E05, decide whether there is demand for the deferred infrastructure work.

## Immediate next action

Do not rewrite more architecture documents yet.

First verify what is actually in the repository.

Run these commands in the VS Code PowerShell terminal from the repository root:

```powershell
pwd
git status
Test-Path .venv
Test-Path scripts\evaluate.py
Test-Path requirements.txt
Get-ChildItem scripts
Get-ChildItem tests
Get-ChildItem data
```

If evaluator files are present, inspect them before installing or running anything.

Useful inspection commands:

```powershell
Get-Content scripts\evaluate.py
git status
git diff
```

The existing virtual environment previously worked by calling its Python executable directly:

```powershell
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -m pip --version
```

Do not change the PowerShell execution policy just to activate `.venv`.

## Known cleanup items

These are real issues to fix, but they are **not blockers for E01**:

1. The ERD contains two entities labelled **Support Message**. The second should be deleted or renamed.
2. The ERD and written specification have drift in Ground Truth foreign-key links. Reconcile them later.
3. The old full synthetic-data generator is no longer required before the evaluator works.

## Working rules

Keep the original rule:

> Build it → inspect it → test it → break it → understand the failure → fix it → document it.

Add:

> No new large specification unless it unlocks the next runnable increment.

And:

> Never mark generated or externally supplied code as complete until it has been inspected and run locally.

## Current project map

```text
S00  Master plan / scope                         COMPLETE
S01  Repository foundation                      COMPLETE
S02  Synthetic data + ground-truth design       COMPLETE

E01  Evaluation Harness v1                      CURRENT
E02  Judge coverage                             NEXT
E03  Real chatbot adapter                       LATER
E04  Audit/report format                        LATER
E05  Public PixelVault evaluation demo          LATER

Deferred:
- full synthetic dataset
- database
- RAG
- local model
- API
- chat UI
- Chatwoot
- Docker/deployment
```

## Next-session instruction

Attach this file and say:

> Continue the PixelVault AI Customer Support Lab from this status file. The project has pivoted to evaluation-first. E01 is current. Teach me in small steps. First verify the real repository state and do not assume the external E01 package exists until we see and run the files locally.
