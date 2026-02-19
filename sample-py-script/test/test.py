import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from unittest.mock import patch
from io import StringIO
import sys
from unittest.mock import patch


# Import functions from the student's script
from lab1 import (
    twinkle_twinkle,
    display_statement,
    display_two_methods,
    pyramid_pattern,
    box_border_pattern,
    stair_step_pattern,
    alphabetic_pyramid,
)

class TestPatterns(unittest.TestCase):

    def setUp(self):
        """Redirect stdout to capture print statements."""
        self.held_output = StringIO()
        self.original_stdout = sys.stdout  # Save original stdout
        sys.stdout = self.held_output

    def tearDown(self):
        """Reset stdout after the test."""
        sys.stdout = self.original_stdout  # Restore original stdout
        self.held_output.close()

    @weight(5)
    @number("1.1")
    def test_twinkle_twinkle(self):
        """Test Case 1.1: Twinkle Twinkle in Specific Format"""
        twinkle_twinkle()
        output_lines = self.held_output.getvalue().split('\n')

        expected_output = [
            "Twinkle, twinkle, little star,",
            "    How I wonder what you are!",
            "        Up above the world so high,",
            "        Like a diamond in the sky.",
            "Twinkle, twinkle, little star,",
            "    How I wonder what you are",
        ]
        
        # Count the leading spaces of the line with "Twinkle, twinkle, little star,"
        target_line = "Twinkle, twinkle, little star,"
        leading_spaces = None
        for line in output_lines:
            if line.strip() == target_line:
                leading_spaces = len(line) - len(line.lstrip())
                break
        
        # Remove the same number of leading spaces from all lines
        if leading_spaces is not None:
            output_lines = [line[leading_spaces:] if len(line) >= leading_spaces else line for line in output_lines]
        
        # Normalize tabs to spaces
        output_lines = [line.replace('\t', '    ') for line in output_lines]

        # Check each line, ignoring trailing spaces
        for line, expected in zip(output_lines, expected_output):
            self.assertEqual(line.rstrip(), expected)
        
    @weight(5)
    @number("1.2")
    def test_display_statement(self):
        """Test Case 1.2: Display Statement Across Two Lines"""
        ## strip whitespaces
        display_statement()
        output_lines = self.held_output.getvalue().split('\n')

        expected_output = [
            "I am using Python",
            "It's my First Assignment",
        ]

        output_lines = [line.replace("’", "'") for line in output_lines]

        # Strip all leading and trailing spaces from each line
        output_lines = [line.strip() for line in output_lines]
        
        # Check each line, ignoring trailing spaces
        for line, expected in zip(output_lines, expected_output):
            self.assertEqual(line, expected)


    @weight(5)
    @number("1.3")
    def test_display_two_methods(self):
        """Test Case 1.3: Statement with Two Methods"""
        display_two_methods()
        output_lines = self.held_output.getvalue().split('\n')
        expected_output = [
            "ohhh!!!",
            "Python is so fun!!! && It is Easy! Get Started",
        ]
        # Strip all leading and trailing spaces from each line
        output_lines = [line.strip() for line in output_lines]
        
        # Check each line, ignoring trailing spaces
        for line, expected in zip(output_lines, expected_output):
            self.assertEqual(line, expected)



    @weight(5)
    @number("1.4")
    def test_pyramid_pattern(self):
        """Test Case 1.4: Pyramid Pattern"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            pyramid_pattern()
            output_lines = mock_stdout.getvalue().split('\n')

        expected_output = [
            "    A",
            "   A A",
            "  A A A",
            " A A A A",
            "A A A A A",
        ]
        
        # Count the leading spaces of the line with "A A A A A"
        target_line = "A A A A A"
        leading_spaces = None
        for line in output_lines:
            if line.strip() == target_line:
                leading_spaces = len(line) - len(line.lstrip())
                break
        
        # Remove the same number of leading spaces from all lines
        if leading_spaces is not None:
            output_lines = [line[leading_spaces:] if len(line) >= leading_spaces else line for line in output_lines]
        
        # Check each line, ignoring trailing spaces
        for line, expected in zip(output_lines, expected_output):
            self.assertEqual(line.rstrip(), expected)

        


    @weight(5)
    @number("1.5")
    def test_box_border_pattern(self):
        """Test Case 1.5: Box Border Pattern"""
        box_border_pattern()
        output_lines = self.held_output.getvalue().split('\n')

        expected_output = [
            "O O O O O",
            "O       O",
            "O       O",
            "O       O",
            "O O O O O",
        ]
        
        # Count the leading spaces of the line with "O O O O O"
        target_line = "O O O O O"
        leading_spaces = None
        for line in output_lines:
            if line.strip() == target_line:
                leading_spaces = len(line) - len(line.lstrip())
                break
        
        # Remove the same number of leading spaces from all lines
        if leading_spaces is not None:
            output_lines = [line[leading_spaces:] if len(line) >= leading_spaces else line for line in output_lines]
        
        # Normalize tabs to spaces
        output_lines = [line.replace('\t', '       ') for line in output_lines]

        # Replace all lowercase 'o' with uppercase 'O'
        output_lines = [line.replace('o', 'O') for line in output_lines]

        # Replace all number 0 with uppercase 'O'
        output_lines = [line.replace('0', 'O') for line in output_lines]
    
        # Check each line, ignoring trailing spaces
        for line, expected in zip(output_lines, expected_output):
            self.assertEqual(line.rstrip(), expected)

            



    @weight(5)
    @number("1.6")
    def test_stair_step_pattern(self):
        """Test Case 1.6: Stair-Step Pattern"""
        stair_step_pattern()
        output_lines = self.held_output.getvalue().split('\n')

        expected_output = [
            "*",
            "* *",
            "* * *",
            "* * * *",
            "* * * * *",
        ]
        
        # Strip all leading and trailing spaces from each line
        output_lines = [line.strip() for line in output_lines]
        
        # Check each line
        for line, expected in zip(output_lines, expected_output):
            self.assertEqual(line, expected)


    @weight(5)
    @number("1.7")
    def test_alphabetic_pyramid(self):
        """Test Case 1.7: Alphabetic Pyramid"""
        alphabetic_pyramid()
        output_lines = self.held_output.getvalue().split('\n')

        expected_output = [
            "A",
            "B C",
            "D E F",
            "G H I J",
            "K L M N O",
        ]
        
        # Strip all leading and trailing spaces from each line
        output_lines = [line.strip() for line in output_lines]
        
        # Check each line
        for line, expected in zip(output_lines, expected_output):
            self.assertEqual(line, expected)


if __name__ == "__main__":
    unittest.main()
