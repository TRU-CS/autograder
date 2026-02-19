# 1. Twinkle Twinkle in a Specific Format
def twinkle_twinkle():
    output = """
        Twinkle, twinkle, little star,
            How I wonder what you are!
                Up above the world so high,
                Like a diamond in the sky.
        Twinkle, twinkle, little star,
            How I wonder what you are
        """
    print(output)

# 2. Display a Statement Across Two Lines
def display_statement():
    print("I am using Python")
    print("It’s my First Assignment")

# 3. Statement with Two Methods
def display_two_methods():
    # Method 1: Using a single print with \n
    print("ohhh!!!\nPython is so fun!!! && It is Easy! Get Started")
    
    # Method 2: Using two separate print statements
    print("ohhh!!!")
    print("Python is so fun!!! && It is Easy! Get Started")

# 4.1 Pyramid Pattern
def pyramid_pattern():
    rows = 5
    for i in range(1, rows + 1):
        line = " " * (rows - i) + " ".join(["A"] * i)
        print(line)
        # print(f"Row {i}: '{line}'")  # Debugging output



def box_border_pattern():
    rows = 5
    columns = 5
    for i in range(rows):
        if i == 0 or i == rows - 1:
            # Top or bottom border
            print(" ".join(["O"] * columns))
        else:
            # Inner rows: correct spacing between border Os
            spaces_between = " " * ((columns - 2) * 2 + 1)
            print(f"O{spaces_between}O")


# 4.3 Stair-Step Pattern
def stair_step_pattern():
    rows = 5
    for i in range(1, rows + 1):
        print("* " * i)

# 4.4 Alphabetic Pyramid
def alphabetic_pyramid():
    rows = 5
    char = 65  # ASCII for 'A'
    for i in range(1, rows + 1):
        for j in range(i):
            print(chr(char), end=" ")
            char += 1
        print()

# Main execution to demonstrate the solutions
if __name__ == "__main__":
    print("1. Twinkle Twinkle in Specific Format:")
    twinkle_twinkle()
    print("\n2. Display Statement Across Two Lines:")
    display_statement()
    print("\n3. Statement with Two Methods:")
    display_two_methods()
    print("\n4.1 Pyramid Pattern:")
    pyramid_pattern()
    print("\n4.2 Box Border Pattern:")
    box_border_pattern()
    print("\n4.3 Stair-Step Pattern:")
    stair_step_pattern()
    print("\n4.4 Alphabetic Pyramid:")
    alphabetic_pyramid()
