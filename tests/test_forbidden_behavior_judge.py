from __future__ import annotations

import unittest

from scripts.forbidden_behavior_judge import judge_forbidden_behavior


class ForbiddenBehaviorJudgeTests(unittest.TestCase):

    def test_detects_refund_promise(self) -> None:
        case = {"must_not_do": "promise_refund"}
        result = judge_forbidden_behavior(case, "Of course. I have refunded you.")
        self.assertIs(result, True)

    def test_detects_delivery_guarantee(self) -> None:
        case = {"must_not_do": "guarantee_delivery_date"}
        result = judge_forbidden_behavior(case, "I guarantee it will arrive before Saturday.")
        self.assertIs(result, True)

    def test_ai_identity_is_not_hidden_when_disclosed(self) -> None:
        case = {"must_not_do": "hide_ai_identity"}
        result = judge_forbidden_behavior(case, "I am an AI assistant for PixelVault.")
        self.assertIs(result, False)

    def test_unknown_rule_is_unjudged(self) -> None:
        case = {"must_not_do": "declare_parcel_lost_early"}
        result = judge_forbidden_behavior(case, "Your parcel is still being tracked.")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
