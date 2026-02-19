# from io import StringIO
# import sys
# from unittest import TestCase, main

# def generate_pattern():
#     # print("          A")
#     # print("         A A")
#     # print("        A A A")
#     # print("       A A A A")
#     # print("      A A A A A")

#     print("    A") 
#     print("   A A")
#     print("  A A A")
#     print(" A A A A")
#     print("A A A A A")
#     # print("    A\n   A A\n  A A A\n A A A A\nA A A A A")
# class TestPatternGeneration(TestCase):
#     def test_generate_pattern(self):
#         expected_output = [
#             "    A",
#             "   A A",
#             "  A A A",
#             " A A A A",
#             "A A A A A",
#         ]
        
#         # Capture the output of the function
#         captured_output = StringIO()
#         sys.stdout = captured_output
#         generate_pattern()
#         sys.stdout = sys.__stdout__
        
#         # Split the captured output into lines
#         output_lines = captured_output.getvalue().split('\n')
        
#         # Count the leading spaces of the line with "A A A A A"
#         target_line = "A A A A A"
#         leading_spaces = None
#         for line in output_lines:
#             if line.strip() == target_line:
#                 leading_spaces = len(line) - len(line.lstrip())
#                 break
        
#         # Remove the same number of leading spaces from all lines
#         if leading_spaces is not None:
#             output_lines = [line[leading_spaces:] if len(line) >= leading_spaces else line for line in output_lines]
        
#         # Check each line, ignoring trailing spaces
#         for line, expected in zip(output_lines, expected_output):
#             self.assertEqual(line.rstrip(), expected)


# # if __name__ == '__main__':
# #     main()

# from io import StringIO
# import sys
# from unittest import TestCase, main

# def print_pattern():
#     print("O O O O O\nO\tO\nO\tO\nO\tO\nO O O O O")

# class TestPatternGeneration(TestCase):
#     def test_print_pattern(self):
#         expected_output = [
#             "O O O O O",
#             "O       O",
#             "O       O",
#             "O       O",
#             "O O O O O",
#         ]
        
#         # Capture the output of the function
#         captured_output = StringIO()
#         sys.stdout = captured_output
#         print_pattern()
#         sys.stdout = sys.__stdout__
        
#         # Split the captured output into lines
#         output_lines = captured_output.getvalue().split('\n')
        
#         # Count the leading spaces of the line with "O O O O O"
#         target_line = "O O O O O"
#         leading_spaces = None
#         for line in output_lines:
#             if line.strip() == target_line:
#                 leading_spaces = len(line) - len(line.lstrip())
#                 break
        
#         # Remove the same number of leading spaces from all lines
#         if leading_spaces is not None:
#             output_lines = [line[leading_spaces:] if len(line) >= leading_spaces else line for line in output_lines]
        
#         # Normalize tabs to spaces
#         output_lines = [line.replace('\t', '       ') for line in output_lines]
        
#         # Check each line, ignoring trailing spaces
#         for line, expected in zip(output_lines, expected_output):
#             self.assertEqual(line.rstrip(), expected)

# if __name__ == '__main__':
#     main()

# from io import StringIO
# import sys
# from unittest import TestCase, main

# def print_pattern():
    
#     print("A ") 
#     print("B C  ")
#     print("D E F  ")
#     print("G H I J  ")
#     print("K L M N O")
# class TestPatternGeneration(TestCase):
#     def test_print_pattern(self):
#         expected_output = [
#             "A",
#             "B C",
#             "D E F",
#             "G H I J",
#             "K L M N O",
#         ]
        
#         # Capture the output of the function
#         captured_output = StringIO()
#         sys.stdout = captured_output
#         print_pattern()
#         sys.stdout = sys.__stdout__
        
#         # Split the captured output into lines
#         output_lines = captured_output.getvalue().split('\n')
        
#         # Strip all leading and trailing spaces from each line
#         output_lines = [line.strip() for line in output_lines]
        
#         # Check each line
#         for line, expected in zip(output_lines, expected_output):
#             self.assertEqual(line, expected)

# if __name__ == '__main__':
#     main()

# import unittest
# from io import StringIO
# import sys
# from unittest.mock import patch

# def print_poem():
#     # print("        Twinkle, twinkle, little star,")
#     # print("            How I wonder what you are!")
#     # print("                Up above the world so high,")
#     # print("                Like a diamond in the sky.")
#     # print("        Twinkle, twinkle, little star,")
#     # print("            How I wonder what you are")
#     print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are ")
# print_poem()
# class TestPoemOutput(unittest.TestCase):
#     def test_print_poem(self):
#         """Test Case: Poem Output"""
#         with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
#             print_poem()
#             output_lines = mock_stdout.getvalue().split('\n')

#         expected_output = [
#             "Twinkle, twinkle, little star,",
#             "    How I wonder what you are!",
#             "        Up above the world so high,",
#             "        Like a diamond in the sky.",
#             "Twinkle, twinkle, little star,",
#             "    How I wonder what you are",
#         ]
        
#         # Count the leading spaces of the line with "Twinkle, twinkle, little star,"
#         target_line = "Twinkle, twinkle, little star,"
#         leading_spaces = None
#         for line in output_lines:
#             if line.strip() == target_line:
#                 leading_spaces = len(line) - len(line.lstrip())
#                 break
        
#         # Remove the same number of leading spaces from all lines
#         if leading_spaces is not None:
#             output_lines = [line[leading_spaces:] if len(line) >= leading_spaces else line for line in output_lines]
        
#         # Normalize tabs to spaces
#         output_lines = [line.replace('\t', '    ') for line in output_lines]

#         # Check each line, ignoring trailing spaces
#         for line, expected in zip(output_lines, expected_output):
#             self.assertEqual(line.rstrip(), expected)

# if __name__ == '__main__':
#     unittest.main()

import unittest
from io import StringIO
import sys
from unittest.mock import patch

def display_statement():
    print("I am using Python\nIt’s my First Assignment")

class TestStatementOutput(unittest.TestCase):
    def test_display_statement(self):
        """Test Case: Display Statement"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            display_statement()
            output_lines = mock_stdout.getvalue().split('\n')

        expected_output = [
            "I am using Python",
            "It’s my First Assignment",
        ]
        
        # Check each line, ignoring trailing spaces
        for line, expected in zip(output_lines, expected_output):
            self.assertEqual(line.strip(), expected)

if __name__ == '__main__':
    unittest.main()