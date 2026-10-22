import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.evaluate import load_questions, load_prompts, search_questions, get_dialectical_structure

class TestSocraticEvaluator(unittest.TestCase):

    def setUp(self):
        self.questions = load_questions()
        self.prompts = load_prompts()

    def test_questions_loaded(self):
        self.assertEqual(len(self.questions), 85)

    def test_search_kant(self):
        matches = search_questions("Kant", self.questions)
        self.assertGreaterEqual(len(matches), 5)

    def test_search_sartre(self):
        matches = search_questions("Sartre", self.questions)
        self.assertGreaterEqual(len(matches), 2)

    def test_outline_generation(self):
        res = get_dialectical_structure("La liberté consiste-t-elle à faire ce que l'on veut ?")
        self.assertEqual(len(res["steps"]), 3)
        self.assertIn("Thèse", res["steps"][0]["part"])
        self.assertIn("Antithèse", res["steps"][1]["part"])
        self.assertIn("Synthèse", res["steps"][2]["part"])

if __name__ == "__main__":
    unittest.main()
