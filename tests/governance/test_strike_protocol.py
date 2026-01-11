import unittest
import sys
import os

# Add root to path
sys.path.append(os.path.expanduser("~/helix-core-unified/helix-ledger"))
from core.governance.strike_protocol import StrikeProtocol

class TestStrikeProtocol(unittest.TestCase):
    def setUp(self):
        self.strike = StrikeProtocol()

    def test_grief_triggers(self):
        inputs = [
            "My dog died yesterday.",
            "I am going to a funeral.",
            "I feel so heartbroken."
        ]
        for i in inputs:
            result = self.strike.analyze_input(i)
            self.assertEqual(result["status"], "STRIKE_TRIGGERED", f"Failed on: {i}")
            self.assertEqual(result["category"], "grief")

    def test_romance_triggers(self):
        inputs = [
            "I think I love you.",
            "You are my soulmate.",
            "Will you marry me?"
        ]
        for i in inputs:
            result = self.strike.analyze_input(i)
            self.assertEqual(result["status"], "STRIKE_TRIGGERED", f"Failed on: {i}")
            self.assertEqual(result["category"], "romance")

    def test_technical_safe_pass(self):
        # "I love python programming" -> "love" is not "love you". Should pass.
        
        result_love = self.strike.analyze_input("I love python programming.")
        self.assertEqual(result_love["status"], "PASS")

        result_tech = self.strike.analyze_input("This is a technical request.")
        self.assertEqual(result_tech["status"], "PASS")

    def test_response_format(self):
        result = self.strike.analyze_input("I love you")
        self.assertIn("synthetic intelligence", result["response"])
        self.assertIn("biological resonance", result["response"])

if __name__ == "__main__":
    unittest.main()
