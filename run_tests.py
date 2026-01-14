import unittest
import sys
import xmlrunner
from tests.test_suite_one import TestSuiteOne
from tests.test_suite_two import TestSuiteTwo

def run_tests(choice):
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Logic to map Jenkins parameter to Test Classes
    if choice == "TestOne":
        print(f"--> Jenkins selected: {choice}")
        suite.addTests(loader.loadTestsFromTestCase(TestSuiteOne))
    elif choice == "TestTwo":
        print(f"--> Jenkins selected: {choice}")
        suite.addTests(loader.loadTestsFromTestCase(TestSuiteTwo))
    elif choice == "All":
        print("--> Jenkins selected: All Tests")
        suite.addTests(loader.loadTestsFromTestCase(TestSuiteOne))
        suite.addTests(loader.loadTestsFromTestCase(TestSuiteTwo))
    else:
        print(f"Error: Invalid selection '{choice}'. Use 'TestOne', 'TestTwo', or 'All'")
        sys.exit(1)

    # --- UPDATED RUNNER ---
    # This generates XML files in the 'test-reports' folder
    runner = xmlrunner.XMLTestRunner(output='test-reports', verbosity=2)
    result = runner.run(suite)

    # Exit with failure code if tests fail
    if not result.wasSuccessful():
        sys.exit(1)

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "All"
    run_tests(arg)