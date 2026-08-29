from __future__ import annotations

import json
from pathlib import Path

from providers.stub_bad_bot import respond


def main() -> None:
    cases_path = Path("data/ground_truth_cases.json")
    cases = json.loads(cases_path.read_text(encoding="utf-8"))
    case = cases[0]

    actual = respond(case["customer_question"])

    action_ok = actual["action"] == case["expected_action"]
    handoff_ok = actual["handoff"] == case["requires_human_handoff"]
    result = "PASS" if action_ok and handoff_ok else "FAIL"

    print("Case:", case["test_case_id"])
    print("Question:", case["customer_question"])
    print("Expected action:", case["expected_action"])
    print("Actual action:", actual["action"])
    print("Expected handoff:", case["requires_human_handoff"])
    print("Actual handoff:", actual["handoff"])
    print("Bot response:", actual["text"])
    print("Result:", result)


if __name__ == "__main__":
    main()
