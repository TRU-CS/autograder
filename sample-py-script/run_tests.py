# run_tests.py
import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

if __name__ == '__main__':
    # Discover and load all test cases from the 'tests' directory
    suite = unittest.defaultTestLoader.discover('test')
    
    # Run the test suite and save results in JSON format for Gradescope
    with open('/autograder/results/results.json', 'w') as f:
        JSONTestRunner(visibility='visible', stream=f).run(suite)
