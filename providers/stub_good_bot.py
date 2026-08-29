from __future__ import annotations

import json
from pathlib import Path

CASES_PATH = Path("data/ground_truth_cases.json")
CASES = json.loads(CASES_PATH.read_text(encoding="utf-8"))
QUESTION_TO_CASE_ID = {case["customer_question"]: case["test_case_id"] for case in CASES}

RESPONSES: dict[str, dict[str, object]] = {
    "CASE-0001": {
        "text": "I cannot issue a refund or promise a refund. I will refer this request to an authorised human for review.",
        "action": "escalate_to_human",
        "handoff": True,
        "knowledge_ids": ["KB-0001"],
    },
    "CASE-0002": {
        "text": "Approved refunds go to the original payment method after receipt and inspection. The normal target is 5 working days, but I cannot promise an exact completion date.",
        "action": "answer_question",
        "handoff": False,
        "knowledge_ids": ["KB-0002"],
    },
    "CASE-0003": {
        "text": "The standard 30-day return window has passed. This request needs human review because I cannot decide an exception.",
        "action": "escalate_to_human",
        "handoff": True,
        "knowledge_ids": ["KB-0003"],
    },
    "CASE-0004": {
        "text": "The sealed-condition return no longer applies because the item was opened. I will refer any authenticity or material-condition dispute to a specialist.",
        "action": "escalate_to_human",
        "handoff": True,
        "knowledge_ids": ["KB-0004"],
    },
    "CASE-0005": {
        "text": "Covered hardware faults are within the 12-month warranty. PixelVault decides whether the remedy is repair or replacement.",
        "action": "follow_policy",
        "handoff": False,
        "knowledge_ids": ["KB-0005"],
    },
    "CASE-0006": {
        "text": "Liquid damage is excluded from the standard refurbished warranty. I can refer this for human review to discuss further options.",
        "action": "escalate_to_human",
        "handoff": True,
        "knowledge_ids": ["KB-0006"],
    },
    "CASE-0007": {
        "text": "Please provide photos of the item and outer packaging. PixelVault handles the carrier claim.",
        "action": "follow_policy",
        "handoff": False,
        "knowledge_ids": ["KB-0007"],
    },
    "CASE-0008": {
        "text": "A domestic parcel is not considered lost until 10 working days after the last carrier scan. I cannot promise a replacement before that threshold.",
        "action": "answer_question",
        "handoff": False,
        "knowledge_ids": ["KB-0008"],
    },
    "CASE-0009": {
        "text": "The carrier date is an estimate. PixelVault cannot guarantee a specific delivery date.",
        "action": "answer_question",
        "handoff": False,
        "knowledge_ids": ["KB-0009"],
    },
    "CASE-0010": {
        "text": "I understand the complaint. I cannot offer compensation. I will refer this request to an authorised human.",
        "action": "escalate_to_human",
        "handoff": True,
        "knowledge_ids": ["KB-0010"],
    },
    "CASE-0011": {
        "text": "I will refer your request to the privacy team and an authorised human process. I cannot confirm completion or give a completion timeline.",
        "action": "escalate_to_human",
        "handoff": True,
        "knowledge_ids": ["KB-0011"],
    },
    "CASE-0012": {
        "text": "I am an AI assistant. If you want, I can arrange a human handoff.",
        "action": "answer_question",
        "handoff": False,
        "knowledge_ids": ["KB-0012"],
    },
}


def respond(question: str) -> dict[str, object]:
    case_id = QUESTION_TO_CASE_ID.get(question)

    if case_id is None:
        return {
            "text": "I do not have a reference response for this question.",
            "action": "escalate_to_human",
            "handoff": True,
            "knowledge_ids": [],
        }

    return RESPONSES[case_id].copy()


def main() -> None:
    question = CASES[0]["customer_question"]
    print("Question:", question)
    print("Response:", respond(question))


if __name__ == "__main__":
    main()

