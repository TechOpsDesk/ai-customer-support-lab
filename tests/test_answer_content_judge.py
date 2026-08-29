from __future__ import annotations

import unittest

from scripts.answer_content_judge import judge_answer_content


class AnswerContentJudgeTests(unittest.TestCase):

    def test_accepts_required_content(self) -> None:
        case = {"required_answer_concepts": [["10 working days", "ten working days"], ["last carrier scan", "last scan"]]}
        response = "A domestic parcel is not considered lost until 10 working days after the last carrier scan."
        self.assertIs(judge_answer_content(case, response), True)

    def test_rejects_vague_answer(self) -> None:
        case = {"required_answer_concepts": [["10 working days", "ten working days"], ["last carrier scan", "last scan"]]}
        response = "Thanks for contacting PixelVault. I can take care of that for you."
        self.assertIs(judge_answer_content(case, response), False)

    def test_case_without_required_concepts_is_unjudged(self) -> None:
        case = {"test_case_id": "CASE-9999"}
        self.assertIsNone(judge_answer_content(case, "Example response"))


if __name__ == "__main__":
    unittest.main()
