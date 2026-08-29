from __future__ import annotations


def judge_answer_content(case: dict[str, object], response_text: str) -> bool | None:
    case_id = str(case.get("test_case_id", ""))
    text = response_text.lower()

    if case_id == "CASE-0008":
        has_ten_day_rule = "10 working days" in text
        has_last_scan = "last carrier scan" in text or "last scan" in text
        return has_ten_day_rule and has_last_scan

    return None
