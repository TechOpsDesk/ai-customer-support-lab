from __future__ import annotations


def judge_answer_content(case: dict[str, object], response_text: str) -> bool | None:
    concepts = case.get("required_answer_concepts")

    if not isinstance(concepts, list) or not concepts:
        return None

    text = response_text.lower()

    for concept_group in concepts:
        if not isinstance(concept_group, list) or not concept_group:
            return None

        found = any(str(phrase).lower() in text for phrase in concept_group)
        if not found:
            return False

    return True
