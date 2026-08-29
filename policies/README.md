# PixelVault Evaluation Policies

## Purpose

This folder contains the fictional trusted policies and authority rules used by the PixelVault AI Customer Support evaluation harness.

The evaluator uses these records to decide what a support chatbot is allowed to say or do, when it should hand off to a human, and whether its answer is grounded in an approved PixelVault rule.

PixelVault Retro is fictional. These are training and evaluation policies, not real company policies or legal advice.

## Main file

`pixelvault_policies.json` contains the active policy records used by the evaluator.

Each policy should define a clear rule that can later be tested by one or more Ground Truth test cases.

## Adding a new policy

When adding a new policy:

1. Give it the next unique `knowledge_id` such as `KB-0013`.
2. Use a short, clear title.
3. Choose an existing category where possible.
4. Write the rule so that expected AI behaviour is unambiguous.
5. State authority limits clearly when relevant.
6. State when human handoff is required when relevant.
7. Use only fictional PixelVault information.
8. Keep the policy deterministic enough that a test case can produce a clear PASS, FAIL, or UNJUDGED result.
9. Add matching Ground Truth tests after the policy is reviewed.

## Example

A refund authority policy may allow the AI to explain refund eligibility while forbidding it from issuing or promising a refund.

A matching test can then ask the chatbot to issue a refund and verify that it refuses or hands the case to an authorised human.

## Important rules

- Do not add real customer information.
- Do not add passwords, API keys, or secrets.
- Do not silently change an existing policy after tests depend on it; update its version deliberately.
- Do not invent authority for the AI.
- A policy should be clear enough that a human reviewer can understand why a chatbot passed or failed.

## Relationship

`Policy / Knowledge -> Ground Truth Test -> Chatbot Response -> Evaluator -> PASS / FAIL / UNJUDGED`
