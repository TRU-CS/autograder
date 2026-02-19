import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner
import sys


if __name__ == '__main__':
   


    suite = unittest.defaultTestLoader.discover('tests')
    # sys.stdout = open("/autograder/results/log.txt", "w")
    # sys.stderr = sys.stdout  # Capture any errors too


     # Run the test suite and save results in JSON format for Gradescope
    with open('/autograder/results/results.json', 'w') as f:
        JSONTestRunner(visibility='visible', stream=f).run(suite)
    # JSONTestRunner(visibility='visible').run(suite)