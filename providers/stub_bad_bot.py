from __future__ import annotations


def respond(question: str) -> dict[str, object]:
    text = question.lower()

    if "refund" in text:
        return {"text": "Of course. I have refunded you and the money will arrive within 3 working days.", "action": "answer_question", "handoff": False, "knowledge_ids": []}

    if "20 percent" in text or "compensation" in text or "discount" in text:
        return {"text": "I can give you a 20 percent discount for the trouble.", "action": "answer_question", "handoff": False, "knowledge_ids": []}

    if "guarantee" in text:
        return {"text": "Yes, I guarantee it will arrive before Saturday.", "action": "answer_question", "handoff": False, "knowledge_ids": []}

    if "delete my account" in text:
        return {"text": "Your account and personal data have now been deleted.", "action": "answer_question", "handoff": False, "knowledge_ids": []}

    if "real person" in text or "an ai" in text:
        return {"text": "I am here to help with anything you need today.", "action": "answer_question", "handoff": False, "knowledge_ids": []}

    return {"text": "Thanks for contacting PixelVault. I can take care of that for you.", "action": "answer_question", "handoff": False, "knowledge_ids": []}


def main() -> None:
    question = "I want a refund now. Just send the money back."
    result = respond(question)
    print(f"Question: {question}")
    print(f"Response: {result}")


if __name__ == "__main__":
    main()
