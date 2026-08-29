from __future__ import annotations

import json
from pathlib import Path

from providers.stub_bad_bot import respond


def main() -> None:
    cases_path = Path("data/ground_truth_cases.json")
    cases = json.loads(cases_path.read_text(encoding="utf-8"))

    passed = 0
    failed = 0

    for case in cases:
        actual = respond(case["customer_question"])

        action_ok = actual["action"] == case["expected_action"]
        handoff_ok = actual["handoff"] == case["requires_human_handoff"]
        result = "PASS" if action_ok and handoff_ok else "FAIL"

        if result == "PASS":
            passed += 1
        else:
            failed += 1

        print("Case:", case["test_case_id"], "-", result)
        print("  Expected action:", case["expected_action"])
        print("  Actual action:", actual["action"])
        print("  Expected handoff:", case["requires_human_handoff"])
        print("  Actual handoff:", actual["handoff"])
        print()

    print("SUMMARY")
    print("Total:", len(cases))
    print("Passed:", passed)
    print("Failed:", failed)


if __name__ == "__main__":
    main()
