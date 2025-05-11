# FILE: /Eval-VLM-Image-Desc/tests/test_clipscore.py

import unittest
from src.evaluation.clipscore import compute_clipscore
from src.utils.image_loader import load_image
from src.utils.text_loader import load_descriptions

class TestClipscore(unittest.TestCase):

    def setUp(self):
        # Load a sample image and description for testing
        self.image = load_image('data/images/sample_image.jpg')
        self.descriptions = load_descriptions('data/descriptions/descriptions.json')

    def test_clipscore_validity(self):
        # Test the Clipscore computation
        score = compute_clipscore(self.image, self.descriptions[0])
        self.assertIsInstance(score, float, "Clipscore should be a float value.")
        self.assertGreaterEqual(score, 0, "Clipscore should be non-negative.")

    def test_clipscore_with_invalid_input(self):
        # Test Clipscore with invalid image input
        with self.assertRaises(ValueError):
            compute_clipscore(None, self.descriptions[0])

        # Test Clipscore with invalid description input
        with self.assertRaises(ValueError):
            compute_clipscore(self.image, None)

if __name__ == '__main__':
    unittest.main()