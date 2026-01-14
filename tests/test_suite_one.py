import unittest

class TestSuiteOne(unittest.TestCase):
    def test_math_operations(self):
        print("\n[Exec] Running Test Suite One: Math Check")
        self.assertEqual(10 + 10, 20)