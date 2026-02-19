import unittest
import ctypes
import os
from pathlib import Path
from gradescope_utils.autograder_utils.decorators import weight

# Load the compiled shared library
ROOT_DIR = Path(__file__).resolve().parent.parent
LIB_PATH = ROOT_DIR / "banking.so"
lib = ctypes.CDLL(str(LIB_PATH))

libc = ctypes.CDLL(None)
libc.fflush.argtypes = [ctypes.c_void_p]
libc.fflush.restype = ctypes.c_int

# Define function prototypes for pass-by-reference changes
lib.displayBalance.argtypes = [ctypes.c_double]
lib.displayBalance.restype = None

lib.deposit.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_double]
lib.deposit.restype = None  # No return value since balance is modified directly

lib.withdraw.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_double]
lib.withdraw.restype = None  # No return value since balance is modified directly

lib.calculateCompoundInterest.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]
lib.calculateCompoundInterest.restype = ctypes.c_double  # Still returns a value


def capture_c_stdout(func, *args):
    """Capture stdout emitted by C code called through ctypes."""
    stdout_fd = 1
    saved_stdout_fd = os.dup(stdout_fd)
    read_fd, write_fd = os.pipe()

    try:
        libc.fflush(None)
        os.dup2(write_fd, stdout_fd)
        func(*args)
        libc.fflush(None)
    finally:
        os.close(write_fd)
        os.dup2(saved_stdout_fd, stdout_fd)
        os.close(saved_stdout_fd)

    output = os.read(read_fd, 8192).decode("utf-8", errors="replace")
    os.close(read_fd)
    return output


class TestBankingSystem(unittest.TestCase):

    @weight(5)
    def test_display_balance_output(self):
        """displayBalance should print the numeric balance with 2 decimal places."""
        output = capture_c_stdout(lib.displayBalance, 1000.00)
        self.assertIn("1000.00", output, msg="displayBalance should print the current balance.")

    @weight(5)
    def test_deposit(self):
        """Deposit $500 should update balance to $1500.00."""
        balance = ctypes.c_double(1000.00)
        lib.deposit(ctypes.byref(balance), 500.00)  # Pass balance by reference
        self.assertAlmostEqual(balance.value, 1500.00, places=2, msg="Deposit function failed!")

    @weight(5)
    def test_withdraw(self):
        """Withdraw $200 should update balance to $800.00."""
        balance = ctypes.c_double(1000.00)
        lib.withdraw(ctypes.byref(balance), 200.00)  # Pass balance by reference
        self.assertAlmostEqual(balance.value, 800.00, places=2, msg="Withdraw function failed!")

    @weight(5)
    def test_insufficient_funds(self):
        """Withdrawal of more than balance should leave balance unchanged."""
        balance = ctypes.c_double(1000.00)
        lib.withdraw(ctypes.byref(balance), 2000.00)  # Attempt to withdraw more than balance
        self.assertAlmostEqual(balance.value, 1000.00, places=2, msg="Balance should remain unchanged!")

    @weight(5)
    def test_compound_interest(self):
        """Calculate compound interest for $1000 at 5% for 2 years (compounded yearly)."""
        result = lib.calculateCompoundInterest(1000.00, 0.05, 2, 1)
        self.assertAlmostEqual(result, 1102.50, places=2, msg="Compound interest calculation incorrect!")

    @weight(5)
    def test_compound_interest_higher_frequency(self):
        """More frequent compounding should match the standard formula."""
        principal = 1000.00
        rate = 0.05
        years = 2
        compounds = 12
        expected = principal * ((1 + (rate / compounds)) ** (compounds * years))
        result = lib.calculateCompoundInterest(principal, rate, years, compounds)
        self.assertAlmostEqual(result, expected, places=2, msg="Compounding frequency is not handled correctly.")

if __name__ == "__main__":
    unittest.main()
