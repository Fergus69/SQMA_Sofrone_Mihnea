import unittest

class TestSuiteTwo(unittest.TestCase):
    def test_string_logic(self):
        print("\n[Exec] Running Test Suite Two: String Check")
        name = "Mihnea"
        self.assertTrue(name.startswith("M"))