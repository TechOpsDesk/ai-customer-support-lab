# PixelVault Synthetic Data Specification

## Status

**Project:** PixelVault AI Customer Support Lab
**Stage:** S02 — Synthetic PixelVault Data Specification
**Status:** Complete

---

## 1. Purpose

This document defines the synthetic data required for the PixelVault AI Customer Support Lab.

The goal of S02 is to **design the data before generating it**.

The synthetic dataset will later support:

* customer and order lookup;
* shipment tracking;
* inventory questions;
* product troubleshooting;
* warranty, return, and refund questions;
* support tickets and conversations;
* technician diagnostics;
* trusted policies and knowledge;
* human handoff scenarios;
* authority and safety testing;
* AI evaluation against known ground truth.

All data in this project is fictional.

No real customer, employee, order, payment, ticket, shipment, tracking, support, password, credential, or other sensitive data may be used.

---

# 2. S02 Rule

**Do not generate the dataset during S02.**

First define:

* what record types are needed;
* what fields each record contains;
* which fields are required or optional;
* how records connect to each other;
* which values are allowed;
* how dates and IDs behave;
* which support situations must be represented;
* how ground truth will be determined;
* what the AI may and may not do;
* what consistency rules generated records must satisfy.

Dataset generation starts only in **S03** after this specification has been reviewed and committed.

---

# 3. General Data Conventions

## 3.1 Keys

`PK` means **Primary Key**.

A primary key uniquely identifies one record.

Example:

```text
customer_id = CUST-0001
```

`FK` means **Foreign Key**.

A foreign key connects one record to another existing record.

Example:

```text
Order.customer_id
        ↓
Customer.customer_id
```

Every foreign-key value must point to a record that actually exists.

---

## 3.2 Required and optional fields

**Required = Yes**

The field must contain a valid value.

**Required = No**

The field may contain `null` when the information does not apply or is not available.

Do not use fake placeholder values such as:

```text
N/A
unknown
none
0000
```

when the correct database value should be `null`.

---

## 3.3 Conceptual data types

The types in this specification are conceptual.

Exact PostgreSQL types will be selected later when the database is implemented.

Common types used here:

* `string` — short text
* `text` — longer text
* `integer` — whole number
* `decimal` — money or numeric value
* `boolean` — `true` or `false`
* `date` — calendar date
* `datetime` — timestamp
* `enum` — one value from a controlled list

---

## 3.4 Timestamps

Generated timestamps should use ISO 8601 UTC.

Example:

```text
2026-03-15T10:20:00Z
```

Connected records must follow a realistic timeline.

---

## 3.5 Money

Money values must use decimal values and a separate currency field.

Example:

```text
price = 129.99
currency = USD
```

Do not use floating-point approximations when the database implementation is created later.

---

## 3.6 Synthetic identifiers

IDs must:

* be fictional;
* be unique within their record type;
* remain stable between deterministic generation runs;
* never contain real personal information;
* be easy for a learner to read and search.

---

# 4. Entity 1 — Customer

A Customer is a fictional person who buys products from PixelVault Retro or contacts support.

## Customer fields

| Field                | Type     | Required | Key | Example                  | Purpose                        |
| -------------------- | -------- | -------- | --- | ------------------------ | ------------------------------ |
| `customer_id`        | string   | Yes      | PK  | `CUST-0001`              | Unique customer identifier     |
| `first_name`         | string   | Yes      | —   | `Maya`                   | Fictional first name           |
| `last_name`          | string   | Yes      | —   | `Chen`                   | Fictional last name            |
| `email`              | string   | Yes      | —   | `maya.chen@example.test` | Safe fictional contact address |
| `phone`              | string   | No       | —   | `+1-555-0101`            | Optional fictional phone       |
| `country`            | string   | Yes      | —   | `United States`          | Customer country               |
| `preferred_language` | string   | Yes      | —   | `en`                     | Preferred support language     |
| `account_status`     | enum     | Yes      | —   | `active`                 | Current account status         |
| `created_at`         | datetime | Yes      | —   | `2026-01-15T10:30:00Z`   | Account creation time          |

## Account status values

* `active`
* `disabled`

## Customer rules

* Every customer must have a unique `customer_id`.
* Names and contact details must be fictional.
* Email addresses must use a safe test domain such as `example.test`.
* A customer can have many orders.
* A customer can have many support tickets.
* The same customer must use the same `customer_id` throughout the dataset.
* An order cannot exist before the related customer account exists.

---

# 5. Entity 2 — Product

A Product is a fictional item sold by PixelVault Retro.

Product information describes **what the item is**.

Inventory is stored separately because inventory describes **how many units are available**.

## Product fields

| Field             | Type    | Required | Key    | Example                                         | Purpose                   |
| ----------------- | ------- | -------- | ------ | ----------------------------------------------- | ------------------------- |
| `product_id`      | string  | Yes      | PK     | `PROD-0001`                                     | Unique product identifier |
| `sku`             | string  | Yes      | Unique | `PVR-CNS-001`                                   | Store SKU                 |
| `name`            | string  | Yes      | —      | `PixelVault Classic Console`                    | Product name              |
| `category`        | enum    | Yes      | —      | `console`                                       | Product category          |
| `description`     | text    | Yes      | —      | `Retro-style game console with two controllers` | Product description       |
| `price`           | decimal | Yes      | —      | `129.99`                                        | Current selling price     |
| `currency`        | string  | Yes      | —      | `USD`                                           | Product price currency    |
| `warranty_months` | integer | Yes      | —      | `12`                                            | Warranty duration         |
| `product_status`  | enum    | Yes      | —      | `active`                                        | Current catalogue status  |

## Product status values

* `active`
* `discontinued`

## Product rules

* Every product must have a unique `product_id`.
* Every product must have a unique `sku`.
* Product information must be fictional.
* Price must use a separate `currency` field.
* Inventory quantities must not be stored in the Product record.
* A Product can appear in many Order Items.
* A Product can have multiple Inventory records.
* A Product can be referenced by Support Tickets.
* Changing the current Product price must not change historical Order Item prices.

---

# 6. Entity 3 — Order

An Order represents one fictional purchase made by a PixelVault Retro customer.

The Order stores purchase-level information.

Individual products purchased are stored separately as Order Items.

## Order fields

| Field              | Type     | Required | Key | Example                | Purpose                            |
| ------------------ | -------- | -------- | --- | ---------------------- | ---------------------------------- |
| `order_id`         | string   | Yes      | PK  | `ORDER-0001`           | Unique order identifier            |
| `customer_id`      | string   | Yes      | FK  | `CUST-0001`            | Customer who placed the order      |
| `order_status`     | enum     | Yes      | —   | `delivered`            | Current order status               |
| `placed_at`        | datetime | Yes      | —   | `2026-03-10T14:25:00Z` | Order creation time                |
| `currency`         | string   | Yes      | —   | `USD`                  | Order currency                     |
| `subtotal`         | decimal  | Yes      | —   | `129.99`               | Item total before shipping and tax |
| `shipping_amount`  | decimal  | Yes      | —   | `9.99`                 | Shipping charge                    |
| `tax_amount`       | decimal  | Yes      | —   | `11.20`                | Tax amount                         |
| `total_amount`     | decimal  | Yes      | —   | `151.18`               | Final order total                  |
| `shipping_country` | string   | Yes      | —   | `United States`        | Destination country                |

## Order status values

* `pending`
* `processing`
* `shipped`
* `delivered`
* `cancelled`
* `returned`

## Order rules

* Every Order must have a unique `order_id`.
* Every Order must belong to one existing Customer.
* A Customer can have many Orders.
* An Order must contain one or more Order Items.
* Products must not be embedded directly in the Order record.
* `subtotal` must equal the sum of the related Order Item `line_total` values.
* `total_amount` must equal:

```text
subtotal + shipping_amount + tax_amount
```

* A cancelled Order must not later appear as successfully delivered.
* The same `order_id` must be used when connecting Shipments, Tickets, Technician Tests, and Test Cases.

---

# 7. Entity 4 — Order Item

An Order Item represents one Product line inside an Order.

If a customer buys three different products, the Order normally has three Order Item records.

## Order Item fields

| Field           | Type    | Required | Key | Example      | Purpose                      |
| --------------- | ------- | -------- | --- | ------------ | ---------------------------- |
| `order_item_id` | string  | Yes      | PK  | `ITEM-0001`  | Unique order-item identifier |
| `order_id`      | string  | Yes      | FK  | `ORDER-0001` | Related Order                |
| `product_id`    | string  | Yes      | FK  | `PROD-0001`  | Purchased Product            |
| `quantity`      | integer | Yes      | —   | `1`          | Number purchased             |
| `unit_price`    | decimal | Yes      | —   | `129.99`     | Price per unit when ordered  |
| `line_total`    | decimal | Yes      | —   | `129.99`     | Total for the order line     |

## Order Item rules

* Every Order Item must have a unique `order_item_id`.
* Every Order Item must belong to one existing Order.
* Every Order Item must reference one existing Product.
* `quantity` must be at least `1`.
* `unit_price` must not be negative.
* `line_total` must equal:

```text
quantity × unit_price
```

* `unit_price` records the historical price paid.
* Later Product price changes must not modify historical Order Items.

---

# 8. Entity 5 — Inventory

Inventory records describe how many units of a Product are held at a particular fictional stock location.

One Product may have inventory at multiple locations.

## Inventory fields

| Field                | Type     | Required | Key | Example                | Purpose                      |
| -------------------- | -------- | -------- | --- | ---------------------- | ---------------------------- |
| `inventory_id`       | string   | Yes      | PK  | `INV-0001`             | Unique inventory identifier  |
| `product_id`         | string   | Yes      | FK  | `PROD-0001`            | Related Product              |
| `location_code`      | string   | Yes      | —   | `WH-A`                 | Fictional warehouse/location |
| `quantity_on_hand`   | integer  | Yes      | —   | `25`                   | Physical stock               |
| `quantity_reserved`  | integer  | Yes      | —   | `4`                    | Stock reserved for orders    |
| `quantity_available` | integer  | Yes      | —   | `21`                   | Stock available to sell      |
| `reorder_level`      | integer  | Yes      | —   | `5`                    | Low-stock threshold          |
| `updated_at`         | datetime | Yes      | —   | `2026-03-10T15:00:00Z` | Last inventory update        |

## Inventory rules

* Every Inventory record must have a unique `inventory_id`.
* Every Inventory record must reference one existing Product.
* Quantities cannot be negative.
* `quantity_reserved` cannot exceed `quantity_on_hand`.
* `quantity_available` must equal:

```text
quantity_on_hand - quantity_reserved
```

* A Product may have more than one Inventory record.
* Low-stock scenarios should have `quantity_available` at or below `reorder_level`.
* Out-of-stock scenarios should have `quantity_available = 0`.

---

# 9. Entity 6 — Shipment

A Shipment stores fictional delivery and tracking information for an Order.

An Order may have one or more Shipments.

## Shipment fields

| Field                   | Type     | Required | Key    | Example                | Purpose                      |
| ----------------------- | -------- | -------- | ------ | ---------------------- | ---------------------------- |
| `shipment_id`           | string   | Yes      | PK     | `SHIP-0001`            | Unique shipment identifier   |
| `order_id`              | string   | Yes      | FK     | `ORDER-0001`           | Related Order                |
| `carrier`               | string   | Yes      | —      | `ParcelPost`           | Fictional carrier            |
| `tracking_number`       | string   | Yes      | Unique | `PVTRACK0001`          | Fictional tracking number    |
| `shipment_status`       | enum     | Yes      | —      | `in_transit`           | Current shipment status      |
| `shipped_at`            | datetime | No       | —      | `2026-03-11T09:00:00Z` | Time shipment left warehouse |
| `estimated_delivery_at` | datetime | No       | —      | `2026-03-14T18:00:00Z` | Expected delivery            |
| `delivered_at`          | datetime | No       | —      | `null`                 | Actual delivery time         |
| `shipping_country`      | string   | Yes      | —      | `United States`        | Destination country          |

## Shipment status values

* `preparing`
* `shipped`
* `in_transit`
* `delayed`
* `out_for_delivery`
* `delivered`
* `lost`
* `returned`

## Shipment rules

* Every Shipment must have a unique `shipment_id`.
* Every Shipment must belong to one existing Order.
* Tracking numbers must be fictional.
* `preparing` shipments may have `shipped_at = null`.
* Once a Shipment is shipped, `shipped_at` must have a value.
* A delivered Shipment must have `delivered_at`.
* A Shipment that has not been delivered should normally have `delivered_at = null`.
* Delivery cannot occur before shipment.
* Shipment dates must follow a realistic sequence.
* Shipment records must stay connected to the correct Order.

---

# 10. Entity 7 — Support Ticket

A Support Ticket represents one customer question, problem, request, or support case.

A Ticket always belongs to a Customer.

It may optionally reference an Order, Shipment, or Product when relevant.

## Support Ticket fields

| Field           | Type     | Required | Key | Example                 | Purpose                        |
| --------------- | -------- | -------- | --- | ----------------------- | ------------------------------ |
| `ticket_id`     | string   | Yes      | PK  | `TICKET-0001`           | Unique ticket identifier       |
| `customer_id`   | string   | Yes      | FK  | `CUST-0001`             | Related Customer               |
| `order_id`      | string   | No       | FK  | `ORDER-0001`            | Optional related Order         |
| `shipment_id`   | string   | No       | FK  | `SHIP-0001`             | Optional related Shipment      |
| `product_id`    | string   | No       | FK  | `PROD-0001`             | Optional related Product       |
| `subject`       | string   | Yes      | —   | `Order has not arrived` | Short problem summary          |
| `category`      | enum     | Yes      | —   | `shipping`              | Support category               |
| `priority`      | enum     | Yes      | —   | `normal`                | Case urgency                   |
| `ticket_status` | enum     | Yes      | —   | `open`                  | Current ticket state           |
| `created_at`    | datetime | Yes      | —   | `2026-03-15T10:20:00Z`  | Ticket creation time           |
| `updated_at`    | datetime | Yes      | —   | `2026-03-15T11:05:00Z`  | Last update                    |
| `assigned_to`   | string   | No       | —   | `TEAM-SUPPORT`          | Optional human/team assignment |

## Ticket categories

* `order_status`
* `shipping`
* `delivery_problem`
* `return`
* `refund`
* `product_problem`
* `warranty`
* `account`
* `general_question`

## Ticket priority values

* `low`
* `normal`
* `high`
* `urgent`

## Ticket status values

* `open`
* `pending`
* `waiting_for_customer`
* `escalated`
* `resolved`
* `closed`

## Support Ticket rules

* Every Ticket must have a unique `ticket_id`.
* Every Ticket must belong to one existing Customer.
* Optional linked IDs must point to existing records.
* If a Ticket links to an Order, the Order should normally belong to the same Customer.
* If a Ticket links to a Shipment, the Shipment should normally belong to the linked Order.
* Category, priority, and status must use allowed values.
* `updated_at` cannot be earlier than `created_at`.
* Tickets needing human action must be able to use the `escalated` status.
* A resolved Ticket should contain enough related information to understand the outcome.

### `assigned_to` note

`assigned_to` is not a foreign key in v1.

It may contain fictional identifiers such as:

```text
TEAM-SUPPORT
TEAM-RETURNS
AGENT-001
```

A separate Agent table is outside the current S02 scope.

---

# 11. Entity 8 — Support Message

A Support Message is one message inside a Support Ticket.

Messages may come from:

* the customer;
* the AI assistant;
* a human agent;
* the system.

## Support Message fields

| Field          | Type     | Required | Key | Example                           | Purpose                     |
| -------------- | -------- | -------- | --- | --------------------------------- | --------------------------- |
| `message_id`   | string   | Yes      | PK  | `MSG-0001`                        | Unique message identifier   |
| `ticket_id`    | string   | Yes      | FK  | `TICKET-0001`                     | Related Ticket              |
| `sender_type`  | enum     | Yes      | —   | `customer`                        | Type of sender              |
| `sender_id`    | string   | No       | —   | `CUST-0001`                       | Optional sender identifier  |
| `message_text` | text     | Yes      | —   | `My order still has not arrived.` | Message content             |
| `created_at`   | datetime | Yes      | —   | `2026-03-15T10:20:00Z`            | Message time                |
| `is_internal`  | boolean  | Yes      | —   | `false`                           | Whether customer can see it |

## Sender type values

* `customer`
* `ai`
* `agent`
* `system`

## Support Message rules

* Every Message must have a unique `message_id`.
* Every Message must belong to one existing Support Ticket.
* Messages must follow chronological order using `created_at`.
* Customer-visible messages use `is_internal = false`.
* Internal notes use `is_internal = true`.
* Customer messages must contain fictional data only.
* AI, customer, human-agent, and system messages must remain distinguishable using `sender_type`.
* A Ticket may contain many Messages.

### `sender_id` note

`sender_id` is intentionally not a strict universal foreign key because different sender types use different identifier systems.

Examples:

```text
customer → CUST-0001
agent    → AGENT-001
ai       → AI-PIXELVAULT
system   → SYSTEM
```

When `sender_type = customer`, `sender_id` should match the related fictional Customer where applicable.

---

# 12. Entity 9 — Technician Test Record

A Technician Test Record stores a fictional diagnostic or hardware test performed on a PixelVault Product.

These records help ground troubleshooting, warranty, repair, replacement, and escalation decisions.

## Technician Test fields

| Field                | Type     | Required | Key | Example                                    | Purpose                         |
| -------------------- | -------- | -------- | --- | ------------------------------------------ | ------------------------------- |
| `test_record_id`     | string   | Yes      | PK  | `TEST-0001`                                | Unique diagnostic identifier    |
| `ticket_id`          | string   | Yes      | FK  | `TICKET-0001`                              | Related support case            |
| `customer_id`        | string   | Yes      | FK  | `CUST-0001`                                | Related Customer                |
| `product_id`         | string   | Yes      | FK  | `PROD-0001`                                | Product tested                  |
| `order_id`           | string   | No       | FK  | `ORDER-0001`                               | Optional original Order         |
| `device_serial`      | string   | Yes      | —   | `PVR-SN-000001`                            | Fictional serial                |
| `test_type`          | string   | Yes      | —   | `power_diagnostic`                         | Diagnostic performed            |
| `result`             | enum     | Yes      | —   | `failed`                                   | Overall result                  |
| `finding`            | text     | Yes      | —   | `Power supply output below expected range` | Diagnostic finding              |
| `recommended_action` | enum     | Yes      | —   | `replace_unit`                             | Recommended next step           |
| `tested_at`          | datetime | Yes      | —   | `2026-03-16T09:30:00Z`                     | Test time                       |
| `technician_id`      | string   | Yes      | —   | `TECH-001`                                 | Fictional technician identifier |

## Test result values

* `passed`
* `failed`
* `inconclusive`

## Recommended action values

* `no_action`
* `retry_test`
* `troubleshoot`
* `repair`
* `replace_unit`
* `escalate`

## Technician Test rules

* Every record must have a unique `test_record_id`.
* Test records must use fictional serial numbers.
* Every test must reference an existing Product.
* Every test must reference an existing Ticket.
* Customer, Product, Order, and Ticket relationships must be internally consistent.
* A failed test must contain a meaningful `finding`.
* The recommended action must make sense for the result and finding.
* `tested_at` must occur after the related support problem exists.
* Technician IDs must be fictional.

### `technician_id` note

A separate Technician table is outside the current v1 S02 scope.

`technician_id` is therefore a stable fictional identifier rather than a foreign key.

---

# 13. Entity 10 — Policy / Knowledge Record

A Policy / Knowledge Record stores trusted PixelVault information used to answer support questions or control support behaviour.

These records will later form part of the trusted knowledge source used by the support system.

They may contain:

* business policies;
* help articles;
* procedures;
* troubleshooting instructions;
* authority rules.

## Policy / Knowledge fields

| Field            | Type     | Required | Key | Example                                           | Purpose                     |
| ---------------- | -------- | -------- | --- | ------------------------------------------------- | --------------------------- |
| `knowledge_id`   | string   | Yes      | PK  | `KB-0001`                                         | Unique knowledge identifier |
| `title`          | string   | Yes      | —   | `Standard Return Policy`                          | Human-readable title        |
| `category`       | enum     | Yes      | —   | `returns`                                         | Knowledge category          |
| `content`        | text     | Yes      | —   | `Unused products may be returned within 30 days.` | Trusted content             |
| `source_type`    | enum     | Yes      | —   | `policy`                                          | Type of trusted source      |
| `version`        | string   | Yes      | —   | `1.0`                                             | Record version              |
| `effective_from` | date     | Yes      | —   | `2026-01-01`                                      | Start of validity           |
| `effective_to`   | date     | No       | —   | `null`                                            | End of validity             |
| `status`         | enum     | Yes      | —   | `active`                                          | Current record status       |
| `updated_at`     | datetime | Yes      | —   | `2026-02-01T10:00:00Z`                            | Last update                 |

## Knowledge categories

* `returns`
* `refunds`
* `warranty`
* `shipping`
* `orders`
* `products`
* `troubleshooting`
* `accounts`
* `support_process`
* `authority`

## Source type values

* `policy`
* `help_article`
* `procedure`
* `troubleshooting_guide`
* `authority_rule`

## Knowledge status values

* `active`
* `inactive`
* `retired`

## Policy / Knowledge rules

* Every record must have a unique `knowledge_id`.
* Content must be fictional and created for PixelVault Retro.
* Trusted business rules must come from these records or another explicitly controlled source.
* Active policies must clearly state the rule support should follow.
* Old versions must not silently overwrite historical versions.
* `effective_from` and `effective_to` determine validity.
* `effective_to` cannot be earlier than `effective_from`.
* Current support answers should normally use only active and currently valid records.
* Knowledge records must not contain real customer information or secrets.

## Authority-rule principle

Authority decisions must not be invented by the language model.

Example authority-rule content:

```text
The AI assistant may explain refund eligibility but may not issue or promise a refund.
Refund execution requires an authorised human or approved external tool.
```

This allows later tests to verify whether the AI refuses actions it is not permitted to perform.

---

# 14. Entity 11 — Test Case / Ground Truth

A Test Case represents one support situation used to evaluate the AI support system.

Ground Truth is the known correct factual answer, action, or decision for that situation.

The AI must not pass a test merely because its answer sounds convincing.

It must also be factually and operationally correct.

## Test Case fields

| Field                    | Type    | Required | Key | Example                                            | Purpose                                |
| ------------------------ | ------- | -------- | --- | -------------------------------------------------- | -------------------------------------- |
| `test_case_id`           | string  | Yes      | PK  | `CASE-0001`                                        | Unique test identifier                 |
| `title`                  | string  | Yes      | —   | `Delayed shipment question`                        | Short test name                        |
| `category`               | string  | Yes      | —   | `shipping`                                         | Situation category                     |
| `customer_id`            | string  | No       | FK  | `CUST-0001`                                        | Optional Customer used by test         |
| `order_id`               | string  | No       | FK  | `ORDER-0001`                                       | Optional Order used by test            |
| `shipment_id`            | string  | No       | FK  | `SHIP-0001`                                        | Optional Shipment used by test         |
| `product_id`             | string  | No       | FK  | `PROD-0001`                                        | Optional Product used by test          |
| `inventory_id`           | string  | No       | FK  | `INV-0001`                                         | Optional Inventory record used by test |
| `ticket_id`              | string  | No       | FK  | `TICKET-0001`                                      | Optional Ticket used by test           |
| `test_record_id`         | string  | No       | FK  | `TEST-0001`                                        | Optional Technician Test used by test  |
| `customer_question`      | text    | Yes      | —   | `Where is my order?`                               | Input presented to AI                  |
| `expected_answer`        | text    | Yes      | —   | `The shipment is delayed and is still in transit.` | Canonical correct answer               |
| `expected_action`        | enum    | Yes      | —   | `provide_status`                                   | Correct system behaviour               |
| `requires_human_handoff` | boolean | Yes      | —   | `false`                                            | Whether human takeover is required     |
| `required_knowledge_id`  | string  | No       | FK  | `KB-0004`                                          | Trusted knowledge required             |
| `must_not_do`            | string  | No       | —   | `promise_refund`                                   | Forbidden action                       |
| `severity`               | enum    | Yes      | —   | `normal`                                           | Importance of test                     |
| `notes`                  | text    | No       | —   | `Answer must use the actual shipment status.`      | Evaluation guidance                    |

## Expected action values

* `answer_question`
* `provide_status`
* `give_troubleshooting_steps`
* `request_more_information`
* `escalate_to_human`
* `deny_unauthorized_action`
* `follow_policy`

## Test severity values

* `low`
* `normal`
* `high`
* `critical`

## Test Case rules

* Every Test Case must have a unique `test_case_id`.
* Every Test Case must have a clear expected answer and expected action.
* All referenced IDs must point to existing records.
* Ground Truth must come from actual synthetic records, trusted policies, or known authority rules.
* The expected answer must not depend on information that does not exist.
* Tests must include normal and failure situations.
* Some tests must check whether the AI refuses unauthorised actions.
* Some tests must require human handoff.
* Critical tests should cover safety, authority, privacy, hallucination, or incorrect business actions.
* Test cases must be deterministic and repeatable.

## Why Test Cases have direct record links

A Test Case should point directly to the record that proves its answer whenever practical.

Examples:

```text
Delayed shipment test
→ shipment_id

Out-of-stock test
→ inventory_id

Hardware diagnostic test
→ test_record_id

Return-policy test
→ required_knowledge_id
```

This makes later evaluation more reliable and easier to debug.

---

# 15. Relationship Map

The dataset must maintain clear links between related records.

## Core business relationships

```text
Customer
   │
   ├──< Order
   │      │
   │      ├──< Order Item >── Product
   │      │                    │
   │      │                    └──< Inventory
   │      │
   │      └──< Shipment
   │
   └──< Support Ticket
```

## Support relationships

```text
Customer
   │
   └── Support Ticket
          │
          ├──< Support Message
          │
          ├── Order       (optional)
          ├── Shipment    (optional)
          ├── Product     (optional)
          │
          └──< Technician Test Record
```

## Ground Truth relationships

```text
Test Case / Ground Truth
   │
   ├── Customer              (optional)
   ├── Order                 (optional)
   ├── Shipment              (optional)
   ├── Product               (optional)
   ├── Inventory             (optional)
   ├── Support Ticket        (optional)
   ├── Technician Test       (optional)
   └── Policy / Knowledge    (optional)
```

---

# 16. Relationship Rules

## Customer → Order

```text
Customer.customer_id
        ↓
Order.customer_id
```

One Customer can have many Orders.

Every Order belongs to exactly one Customer.

---

## Customer → Support Ticket

```text
Customer.customer_id
        ↓
Support Ticket.customer_id
```

One Customer can have many Support Tickets.

Every Support Ticket belongs to one Customer.

---

## Order → Order Item

```text
Order.order_id
      ↓
Order Item.order_id
```

One Order contains one or more Order Items.

---

## Product → Order Item

```text
Product.product_id
        ↓
Order Item.product_id
```

One Product can appear in many Order Items.

---

## Product → Inventory

```text
Product.product_id
        ↓
Inventory.product_id
```

One Product can have one or more Inventory records.

---

## Order → Shipment

```text
Order.order_id
      ↓
Shipment.order_id
```

One Order may have one or more Shipments.

---

## Support Ticket optional links

A Ticket may optionally point to:

```text
Order.order_id
Shipment.shipment_id
Product.product_id
```

The linked records must belong to a consistent support situation.

---

## Support Ticket → Support Message

```text
Support Ticket.ticket_id
        ↓
Support Message.ticket_id
```

One Ticket can contain many Messages.

---

## Technician Test relationships

A Technician Test can link to:

```text
Support Ticket.ticket_id
Customer.customer_id
Product.product_id
Order.order_id
```

`ticket_id`, `customer_id`, and `product_id` are required.

`order_id` is optional.

---

## Test Case relationships

A Test Case may directly reference:

```text
Customer.customer_id
Order.order_id
Shipment.shipment_id
Product.product_id
Inventory.inventory_id
Support Ticket.ticket_id
Technician Test Record.test_record_id
Policy / Knowledge Record.knowledge_id
```

Every non-null linked ID must point to an existing record.

---

# 17. Relationship Integrity Rules

* IDs must remain consistent throughout the dataset.
* A linked ID must always point to an existing record.
* No orphan foreign-key references are allowed.
* Records must not point to missing Customers, Products, Orders, Shipments, Tickets, Inventory records, Technician Tests, or Knowledge records.
* Connected records must make sense together.
* Connected dates must make sense chronologically.
* Ticket links should refer to records belonging to the same support case.
* Test Cases must use the exact records needed to establish Ground Truth.

---

# 18. ID Format Rules

| Record type      | Format        | Example       |
| ---------------- | ------------- | ------------- |
| Customer         | `CUST-####`   | `CUST-0001`   |
| Product          | `PROD-####`   | `PROD-0001`   |
| Order            | `ORDER-####`  | `ORDER-0001`  |
| Order Item       | `ITEM-####`   | `ITEM-0001`   |
| Inventory        | `INV-####`    | `INV-0001`    |
| Shipment         | `SHIP-####`   | `SHIP-0001`   |
| Support Ticket   | `TICKET-####` | `TICKET-0001` |
| Support Message  | `MSG-####`    | `MSG-0001`    |
| Technician Test  | `TEST-####`   | `TEST-0001`   |
| Knowledge Record | `KB-####`     | `KB-0001`     |
| Test Case        | `CASE-####`   | `CASE-0001`   |
| Technician       | `TECH-###`    | `TECH-001`    |
| Agent            | `AGENT-###`   | `AGENT-001`   |

## ID rules

* IDs must be unique within their record type.
* IDs must not change between deterministic generation runs.
* Related records must use the exact same ID when linking.
* IDs should be easy for learners to read and search.
* IDs must not contain real customer information.
* Deleted or unused IDs should not be silently reassigned to a different logical record within the same deterministic dataset version.

---

# 19. Date and Time Rules

Connected dates must follow a realistic sequence.

Example:

```text
Customer account created
        ↓
Order placed
        ↓
Order processed
        ↓
Shipment shipped
        ↓
Shipment delivered / delayed / lost
        ↓
Support Ticket created
        ↓
Support Messages
        ↓
Technician Test if needed
```

Rules:

* An Order cannot be placed before the Customer account exists.
* A Shipment cannot be shipped before its Order exists.
* A delivery cannot occur before `shipped_at`.
* A Support Ticket about an Order must occur after the Order exists.
* A delivery-problem Ticket should normally occur after shipment activity exists.
* A Technician Test must occur after the related support problem exists.
* `updated_at` cannot be earlier than `created_at`.
* `effective_to` cannot be earlier than `effective_from`.
* All generated timestamps must use a consistent format.

Preferred timestamp:

```text
2026-03-15T10:20:00Z
```

---

# 20. Data Consistency Rules

The generated dataset must be internally consistent.

## Inventory

```text
quantity_available =
quantity_on_hand - quantity_reserved
```

## Order Item

```text
line_total =
quantity × unit_price
```

## Order totals

```text
subtotal =
sum(all related line_total values)
```

```text
total_amount =
subtotal + shipping_amount + tax_amount
```

## Shipment

* Delivered Shipments must have `delivered_at`.
* Non-delivered Shipments should normally have `delivered_at = null`.
* Cancelled Orders must not later appear as successfully delivered without an explicitly modelled correction.

## Support

* Tickets must refer only to records that exist.
* Ticket Customer, Order, Shipment, and Product relationships must be consistent.
* Technician Test findings must agree with test results.
* Recommendations must make sense for the diagnostic result.

## Ground Truth

Ground Truth must match:

* the actual Customer;
* the actual Order;
* the actual Shipment;
* the actual Inventory state;
* the actual Technician Test;
* the applicable Policy / Knowledge record;
* known authority rules.

The purpose is to create a dataset that can be trusted during later AI testing.

---

# 21. Support Situation Coverage

The dataset must include both simple and difficult support cases.

## Order situations

* asking for Order status;
* Order still processing;
* successfully delivered Order;
* cancelled Order;
* returned Order;
* customer cannot provide enough identifying information.

## Shipping situations

* Shipment in transit;
* delayed Shipment;
* lost Shipment;
* out for delivery;
* successfully delivered Shipment;
* customer asks for tracking information.

## Product situations

* Product works normally;
* wrong Product reportedly received;
* damaged Product;
* Product does not power on;
* troubleshooting request;
* warranty question;
* technician diagnostic passes;
* technician diagnostic fails;
* technician result is inconclusive.

## Inventory situations

* normal stock;
* low inventory;
* out of stock.

## Returns and refunds

* return request inside allowed period;
* return request outside allowed period;
* refund eligibility question;
* request for the AI to issue or promise a refund when it has no authority to do so.

## Account and general support

* account question;
* general product question;
* missing information;
* ambiguous customer request.

## Safety and authority

* issue requiring human handoff;
* request for an action the AI is not allowed to perform;
* case where policy must be consulted;
* case where the AI should refuse to guess;
* case where the correct answer requires an exact Order or Shipment lookup;
* case where the AI must not expose another Customer's information.

---

# 22. Important v1 Scope Boundaries

The v1 dataset deliberately does **not** model every possible ecommerce system.

This must be understood when interpreting Ground Truth.

## Payments

There is no Payment or Refund Transaction entity in S02.

Therefore the dataset can test:

* refund eligibility;
* refund-policy questions;
* whether the AI improperly promises or issues a refund.

It cannot truthfully claim that a real payment processor completed a refund unless a payment/refund entity is added in a future version.

---

## Wrong product received

There is no separate warehouse Fulfilment Item entity in v1.

A wrong-product case may therefore be represented by:

* the Customer's report;
* the original Order Item;
* the Support Ticket;
* related Support Messages.

The dataset should not pretend to have independent warehouse proof unless such an entity is added later.

---

## Human agents and technicians

Agent and Technician IDs are fictional stable identifiers.

Full Agent and Technician profile tables are outside the current S02 scope.

---

# 23. Ground Truth Rules

Ground Truth is the correct result that the AI system is expected to reach.

Ground Truth may come from:

* Customer records;
* Product records;
* Order records;
* Order Item records;
* Shipment records;
* Inventory records;
* Technician Test records;
* Support Ticket history;
* Policy / Knowledge records;
* authority rules.

A Ground Truth test should make it possible to answer questions such as:

* Did the AI identify the correct Customer?
* Did it find the correct Order?
* Did it report the actual Shipment status?
* Did it report the correct Inventory state?
* Did it use the correct Product?
* Did it use the relevant diagnostic result?
* Did it use the applicable policy?
* Did it avoid inventing information?
* Did it refuse an unauthorised action?
* Did it request missing information when necessary?
* Did it hand the case to a human when required?

A response must not pass merely because it sounds helpful.

It must also be:

* factually correct;
* grounded in the synthetic records;
* consistent with policy;
* consistent with authority rules;
* operationally safe.

---

# 24. Synthetic Data Safety Rules

* Use fictional PixelVault Retro data only.
* Do not copy real Customer records.
* Do not copy real Support Tickets.
* Do not use real employee records.
* Do not use real payment information.
* Do not use real passwords.
* Do not use real API keys.
* Do not use real authentication tokens.
* Do not use real private addresses or phone numbers.
* Use safe test email domains such as `example.test`.
* Tracking numbers must be fictional.
* Product serial numbers must be fictional.
* Technician and Agent identifiers must be fictional.
* Generated data must be safe to publish in the public GitHub repository.

---

# 25. S03 Deterministic Generation Rules

These rules apply when S03 begins.

Do not implement them during S02.

The generator must:

* use a fixed random seed;
* produce the same logical records on repeated runs;
* preserve stable IDs;
* generate records in dependency order;
* generate only valid foreign-key relationships;
* follow all allowed enum values;
* follow all date rules;
* satisfy all consistency equations;
* create both normal and deliberately difficult support cases;
* generate Ground Truth from actual generated records;
* never use real personal information;
* fail validation if generated records violate this specification.

Recommended dependency order:

```text
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
```

After generation, validation should confirm:

```text
IDs valid
foreign keys valid
dates valid
money totals valid
inventory math valid
shipment states valid
support relationships valid
ground truth valid
synthetic-data safety valid
```

---

# 26. S02 Definition of Done

S02 is complete when:

* [x] customer structure is defined
* [x] product structure is defined
* [x] order structure is defined
* [x] order item structure is defined
* [x] inventory structure is defined
* [x] shipment structure is defined
* [x] support ticket structure is defined
* [x] support message structure is defined
* [x] technician test structure is defined
* [x] policy and knowledge structure is defined
* [x] test case and ground truth structure is defined
* [x] relationships are defined
* [x] ID formats are defined
* [x] date and consistency rules are defined
* [x] support situation coverage is defined
* [x] synthetic data safety rules are defined
* [x] v1 scope boundaries are documented
* [x] deterministic S03 generation rules are documented
* [x] the specification has been reviewed
* [x] the specification has been committed and pushed to GitHub

---

# 27. Final S02 Gate

**Do not generate the dataset until this specification has been reviewed.**

After review:

1. mark the review checkbox complete;
2. save the file;
3. inspect the Git diff;
4. stage the specification;
5. commit it;
6. push it to GitHub;
7. confirm the working tree is clean;
8. update the project status so S03 becomes current.

Only then begin:

**S03 — Generate the deterministic synthetic PixelVault dataset.**
