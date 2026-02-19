"""Lab 1 student template.

Implement each function below. The autograder imports these exact function names,
so do not rename functions or change their signatures.
"""


def twinkle_twinkle():
    """Print the Twinkle Twinkle nursery rhyme in the required format."""
    # TODO: Replace `pass` with your implementation.
    pass


def display_statement():
    """Print the two-line statement exactly as required."""
    # TODO: Replace `pass` with your implementation.
    pass


def display_two_methods():
    """Print the target message (this question asks for two methods)."""
    # TODO: Replace `pass` with your implementation.
    pass


def pyramid_pattern():
    """Print the A pyramid pattern."""
    # TODO: Replace `pass` with your implementation.
    pass


def box_border_pattern():
    """Print the O box-border pattern."""
    # TODO: Replace `pass` with your implementation.
    pass


def stair_step_pattern():
    """Print the stair-step star pattern."""
    # TODO: Replace `pass` with your implementation.
    pass


def alphabetic_pyramid():
    """Print the alphabetic pyramid pattern."""
    # TODO: Replace `pass` with your implementation.
    pass


if __name__ == "__main__":
    # Local smoke test runner (not used by Gradescope autograder).
    demos = [
        ("1. Twinkle Twinkle in Specific Format", twinkle_twinkle),
        ("2. Display Statement Across Two Lines", display_statement),
        ("3. Statement with Two Methods", display_two_methods),
        ("4.1 Pyramid Pattern", pyramid_pattern),
        ("4.2 Box Border Pattern", box_border_pattern),
        ("4.3 Stair-Step Pattern", stair_step_pattern),
        ("4.4 Alphabetic Pyramid", alphabetic_pyramid),
    ]

    for idx, (title, fn) in enumerate(demos):
        if idx:
            print()
        print(f"{title}:")
        fn()
