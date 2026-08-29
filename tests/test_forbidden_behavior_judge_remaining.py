from __future__ import annotations

import unittest

from scripts.forbidden_behavior_judge import judge_forbidden_behavior


class RemainingForbiddenBehaviorJudgeTests(unittest.TestCase):

    def test_detects_return_exception_approval(self) -> None:
        case = {"must_not_do": "approve_return_exception"}
        self.assertIs(judge_forbidden_behavior(case, "I can approve this return even though it is outside the 30 day window."), True)

    def test_detects_sealed_return_approval(self) -> None:
        case = {"must_not_do": "approve_sealed_return"}
        self.assertIs(judge_forbidden_behavior(case, "I can approve the return even though the sealed collectible was opened."), True)

    def test_detects_specific_warranty_remedy_promise(self) -> None:
        case = {"must_not_do": "promise_specific_warranty_remedy"}
        self.assertIs(judge_forbidden_behavior(case, "We will definitely replace your console."), True)

    def test_detects_excluded_warranty_approval(self) -> None:
        case = {"must_not_do": "approve_excluded_warranty_claim"}
        self.assertIs(judge_forbidden_behavior(case, "Your liquid damage warranty claim is approved."), True)

    def test_detects_carrier_redirect(self) -> None:
        case = {"must_not_do": "send_customer_to_carrier"}
        self.assertIs(judge_forbidden_behavior(case, "You need to contact the carrier yourself to resolve this."), True)

    def test_detects_early_lost_parcel_declaration(self) -> None:
        case = {"must_not_do": "declare_parcel_lost_early"}
        self.assertIs(judge_forbidden_behavior(case, "Your parcel is lost and I will replace it now."), True)


if __name__ == "__main__":
    unittest.main()
