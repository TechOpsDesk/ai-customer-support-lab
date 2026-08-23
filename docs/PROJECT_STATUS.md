# PixelVault AI Customer Support Lab — Project Status

## Current phase

S03 — Generate the deterministic synthetic PixelVault dataset

## Completed

* S00 — Master plan and scope freeze
* S01 — Repository setup and v1 project rules
* S02 — Synthetic PixelVault data specification

## In progress

* S03 — Generate the deterministic synthetic PixelVault dataset

## Next

The stage after S03 will be defined when the S03 dataset has been generated, validated, reviewed, and committed.

---

# S01 — Repository Setup

## S01 completion checklist

* [x] GitHub repository created
* [x] Repository cloned locally
* [x] Repository opened in Visual Studio Code
* [x] Correct local project folder verified
* [x] Base project folders created
* [x] `.gitkeep` files added to empty folders
* [x] `.env.example` created
* [x] `.env` protection added to `.gitignore`
* [x] `docs/DECISIONS.md` created
* [x] Premature `compose.yaml` removed; Docker Compose deferred until the Docker stage
* [x] `README.md` updated
* [x] `CONTRIBUTING.md` created
* [x] `SECURITY.md` created
* [x] Repository files reviewed
* [x] Files added to Git
* [x] First PixelVault project commit created
* [x] First project commit pushed to GitHub
* [x] Repository files verified on GitHub
* [x] `docs/DECISIONS.md` verified on GitHub
* [x] `docs/PROJECT_STATUS.md` verified on GitHub
* [x] Final `git status` showed `nothing to commit, working tree clean`

## S01 result

S01 is complete.

The PixelVault AI Customer Support Lab has a public GitHub repository, a working local Git repository, the base project structure, safe example configuration, project documentation, contribution rules, security rules, and Git history stored on GitHub.

Docker and the AI application stack were intentionally not installed during S01. They will be introduced later when they can be built and tested properly.

---

# S02 — Synthetic Data Specification

## S02 goal

S02 was used to design the synthetic PixelVault data model before generating any records.

The specification defines:

* customers
* products
* orders
* order items
* inventory
* shipments
* support tickets
* support messages
* technician test records
* policies and knowledge
* authority rules
* test cases
* expected answers and ground truth
* IDs and ID formats
* relationships between records
* required and optional fields
* date and time rules
* data consistency rules
* synthetic data safety rules
* deterministic generation rules for S03
* v1 scope boundaries

## S02 completion checklist

* [x] Customer structure defined
* [x] Product structure defined
* [x] Order structure defined
* [x] Order Item structure defined
* [x] Inventory structure defined
* [x] Shipment structure defined
* [x] Support Ticket structure defined
* [x] Support Message structure defined
* [x] Technician Test Record structure defined
* [x] Policy / Knowledge structure defined
* [x] Test Case / Ground Truth structure defined
* [x] Primary-key and foreign-key relationships defined
* [x] ID formats defined
* [x] Required and optional fields defined
* [x] Date and time rules defined
* [x] Data consistency rules defined
* [x] Support situation coverage defined
* [x] Ground Truth rules defined
* [x] Authority and safety scenarios defined
* [x] Synthetic data safety rules defined
* [x] Deterministic S03 generation rules defined
* [x] v1 scope boundaries documented
* [x] `docs/SYNTHETIC_DATA_SPEC.md` reviewed
* [x] Specification passed Git whitespace check
* [x] Specification committed to Git
* [x] Specification pushed to GitHub

## S02 result

S02 is complete.

The project now has a reviewed synthetic-data specification describing the records the PixelVault support system will need and the rules connecting those records.

The specification is stored in:

`docs/SYNTHETIC_DATA_SPEC.md`

The specification defines the source of truth for S03.

S03 must not casually invent a different structure while generating data. If S03 reveals that the specification needs to change, the specification should be updated deliberately and the reason documented.

---

# S03 — Deterministic Synthetic Dataset Generation

## S03 goal

S03 will generate the actual fictional PixelVault dataset defined during S02.

Generation must be deterministic.

A fixed random seed must be used so repeated generation produces the same logical customers, products, orders, shipments, tickets, and test cases.

## Planned generation order

Generate records in dependency order:

1. Products
2. Customers
3. Inventory
4. Orders
5. Order Items
6. Shipments
7. Policy / Knowledge Records
8. Support Tickets
9. Support Messages
10. Technician Test Records
11. Test Cases / Ground Truth

## S03 rules

During S03:

* use the S02 specification as the source of truth;
* use fictional PixelVault Retro data only;
* use a fixed random seed;
* keep IDs stable between runs;
* create only valid foreign-key relationships;
* follow the defined enum values;
* follow all date and timeline rules;
* ensure Order totals are mathematically correct;
* ensure Inventory quantities are mathematically correct;
* ensure Shipment states and dates are consistent;
* ensure Tickets reference the correct Customers, Orders, Products, and Shipments;
* ensure Technician Test findings agree with their results;
* ensure Ground Truth is derived from actual generated records and trusted policies;
* include normal cases and deliberately difficult support cases;
* include human-handoff cases;
* include unauthorised-action cases;
* include cases where the AI must request more information;
* include cases where the AI must not guess;
* do not use real personal, customer, employee, payment, or support data;
* validate the generated dataset before considering S03 complete.

## S03 validation target

Before S03 can be completed, the generated dataset should be checked for:

* unique IDs
* valid foreign keys
* no orphan records
* valid timestamps
* valid chronological relationships
* correct Order Item calculations
* correct Order totals
* correct Inventory calculations
* valid Shipment states
* consistent support relationships
* valid Technician Test relationships
* valid Knowledge references
* correct Ground Truth
* deterministic repeatability
* synthetic-data safety

Do not move beyond S03 until the generated data has been inspected, validated, reviewed, committed, pushed, and verified.

---

# Project rule

Do not skip ahead.

Each stage should be understood, reviewed, tested where possible, and completed before moving to the next stage.

---

# Learning rule

**Build it → inspect it → test it → break it → understand the failure → fix it → document it.**
