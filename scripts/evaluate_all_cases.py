from __future__ import annotations

import json
from pathlib import Path

from providers.stub_bad_bot import respond
from scripts.answer_content_judge import judge_answer_content
from scripts.forbidden_behavior_judge import judge_forbidden_behavior


def main() -> None:
    cases_path = Path("data/ground_truth_cases.json")
    cases = json.loads(cases_path.read_text(encoding="utf-8"))

    passed = 0
    failed = 0
    unjudged = 0

    for case in cases:
        actual = respond(case["customer_question"])

        action_ok = actual["action"] == case["expected_action"]
        handoff_ok = actual["handoff"] == case["requires_human_handoff"]
        forbidden = judge_forbidden_behavior(case, str(actual["text"]))
        answer_content = judge_answer_content(case, str(actual["text"]))

        if not action_ok or not handoff_ok or forbidden is True or answer_content is False:
            result = "FAIL"
            failed += 1
        elif forbidden is None or answer_content is None:
            result = "UNJUDGED"
            unjudged += 1
        else:
            result = "PASS"
            passed += 1

        print("Case:", case["test_case_id"], "-", result)
        print("  Expected action:", case["expected_action"])
        print("  Actual action:", actual["action"])
        print("  Expected handoff:", case["requires_human_handoff"])
        print("  Actual handoff:", actual["handoff"])
        print("  Forbidden rule:", case["must_not_do"])
        print("  Forbidden detected:", forbidden)
        print("  Required answer content:", answer_content)
        print()

    print("SUMMARY")
    print("Total:", len(cases))
    print("Passed:", passed)
    print("Failed:", failed)
    print("Unjudged:", unjudged)


if __name__ == "__main__":
    main()
