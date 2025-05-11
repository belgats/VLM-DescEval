import unittest
from src.evaluation.vqascore import VQAScore

class TestVQAScore(unittest.TestCase):

    def setUp(self):
        self.vqa = VQAScore()

    def test_score_calculation(self):
        # Example input for testing
        description = "A dog playing in the park."
        question = "What is the animal doing?"
        expected_score = 0.85  # Hypothetical expected score

        score = self.vqa.calculate_score(description, question)
        self.assertAlmostEqual(score, expected_score, places=2)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.vqa.calculate_score("", "What is this?")

if __name__ == '__main__':
    unittest.main()