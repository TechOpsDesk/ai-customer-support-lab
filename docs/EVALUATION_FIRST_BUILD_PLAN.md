# PixelVault AI Customer Support Lab — Evaluation-First Build Plan

**Version:** 1.0  
**Date:** 29 August 2026

## Purpose

The project will no longer make a full chatbot stack the prerequisite for useful output.

The new v1 is an **AI customer-support evaluation harness** that can test a chatbot against:

- expected actions
- policy grounding
- authority boundaries
- human-handoff requirements
- forbidden behaviours
- severity
- evidence-based pass/fail findings

PixelVault remains the fictional reference environment and public demo dataset.

## Product boundary

### v1 is

A small Python evaluation system with:

1. a test-case format
2. policy/knowledge records
3. a chatbot adapter boundary
4. deterministic checks
5. behavioural checks
6. scoring
7. a report
8. automated tests
9. one real-bot integration

### v1 is not

- a full RAG stack
- a helpdesk
- a database platform
- a local LLM stack
- a production chat UI
- a Docker learning course
- a full synthetic commerce simulator

## Architecture principle

```text
                    +----------------------+
                    |   Test Case Set      |
                    | expected behaviour   |
                    +----------+-----------+
                               |
                    +----------v-----------+
                    |  Evaluation Harness  |
                    | validation + scoring |
                    +----+-------------+---+
                         |             |
              +----------v--+       +--v----------------+
              | Policy / KB |       | Chatbot Adapter   |
              +-------------+       +---------+---------+
                                             |
                                  +----------v----------+
                                  | Any Support Bot     |
                                  +---------------------+

PixelVault = reference dataset + demonstration
Evaluator = reusable product architecture
```

## Stage E01 — Baseline evaluator

Deliverables:

- policy dataset
- 40-ish ground-truth cases
- schema validation
- stub adapter
- deliberately weak stub bot
- structural scoring
- forbidden-behaviour checks
- severity-aware summary
- explicit `UNJUDGED`
- CLI entry point
- automated tests
- readable text/Markdown report

Success condition:

```text
one command
    -> loads cases
    -> calls bot
    -> evaluates answers
    -> prints/saves evidence report
    -> returns non-zero exit code on critical failure
```

## Stage E02 — Judge coverage

For every new judge rule:

1. define the behaviour precisely
2. write a failing test first
3. add a negative/negation test
4. implement the smallest reliable detector
5. rerun the entire suite
6. commit separately

Do not reward apparent coverage created by fragile keyword matching.

## Stage E03 — One real chatbot

Pick one accessible chatbot/provider and build exactly one adapter.

Questions to answer:

- How is a prompt sent?
- What response text is returned?
- Can tool/action metadata be observed?
- Can handoff state be observed?
- Can citations/knowledge references be observed?
- What cannot be observed?

The report must distinguish:

- **FAIL** — observed behaviour contradicts expected behaviour
- **PASS** — observed behaviour satisfies the check
- **UNJUDGED** — evaluator lacks enough evidence to decide
- **NOT OBSERVABLE** — target bot/API does not expose the required signal

## Stage E04 — Audit deliverable

Create a client-style report.

Suggested sections:

1. Scope
2. Bot/version tested
3. Test date
4. Overall readiness
5. Critical findings
6. Authority violations
7. Handoff failures
8. Policy-grounding failures
9. Unsupported claims
10. Unsafe promises/actions
11. Disclosure/transparency checks
12. Recommendations
13. Retest result

## Stage E05 — PixelVault public demo

Publish:

- the test-case set
- selected policies
- the deliberately weak bot
- baseline report
- fixes
- retest report
- lessons learned

This creates one public proof-of-work artifact rather than a long unfinished infrastructure build.

## Deferred backlog

Only resume these when they serve a concrete evaluation need:

- deterministic full customer/order/shipment dataset
- Inventory
- Technician Test Record
- PostgreSQL
- pgvector
- RAG
- Ollama
- FastAPI
- Chatwoot
- Docker
- deployment
- UI dashboard

## Six-week success test

If work stopped after six weeks, the project should still leave behind:

- a cloneable repo
- a runnable evaluator
- a documented test schema
- a credible case set
- a report
- at least one real-bot run
- a public demo

If a task does not move the project toward one of those outputs, it is probably not v1 work.

## Next command

Start with repository verification, not implementation assumptions:

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

Then inspect what exists before changing anything.
