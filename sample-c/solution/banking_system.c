#include <stdio.h>
#include <math.h>

// Function prototypes
void displayBalance(double balance);
void deposit(double *balance, double amount);
void withdraw(double *balance, double amount);
double calculateCompoundInterest(double principal, double rate, int years, int compounds);
static double calculateCompoundInterestPeriods(double principal, double rate, int periods, int compounds);

// Function implementations

// Function to display balance
void displayBalance(double balance) {
    printf("Your current balance is: $%.2f\n", balance);
}

// Function to deposit money (Pass-by-Reference)
void deposit(double *balance, double amount) {
    *balance += amount;  // Updates the balance directly
    printf("Deposit successful! Your updated balance is: $%.2f\n", *balance);
}

// Function to withdraw money (Pass-by-Reference)
void withdraw(double *balance, double amount) {
    if (*balance >= amount) {
        *balance -= amount;  // Updates the balance directly
        printf("Withdrawal successful! Your updated balance is: $%.2f\n", *balance);
    } else {
        printf("Insufficient funds! Your current balance is: $%.2f\n", *balance);
    }
}

// Recursive function to calculate compound interest
static double calculateCompoundInterestPeriods(double principal, double rate, int periods, int compounds) {
    if (periods == 0) {
        return principal;
    }

    principal = principal * (1 + rate / compounds);
    return calculateCompoundInterestPeriods(principal, rate, periods - 1, compounds);
}

double calculateCompoundInterest(double principal, double rate, int years, int compounds) {
    if (years <= 0 || compounds <= 0) {
        return principal;
    }

    return calculateCompoundInterestPeriods(principal, rate, years * compounds, compounds);
}

// Main function for user interaction
int main() {
    double balance = 1000.00;
    int choice;

    printf("Welcome to the Banking System!\n");

    do {
        printf("\n1. Check Balance\n");
        printf("2. Deposit Money\n");
        printf("3. Withdraw Money\n");
        printf("4. Calculate Compound Interest\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                displayBalance(balance);
                break;
            case 2: {
                double amount;
                printf("Enter amount to deposit: $");
                scanf("%lf", &amount);
                deposit(&balance, amount);  // Pass-by-Reference
                break;
            }
            case 3: {
                double amount;
                printf("Enter amount to withdraw: $");
                scanf("%lf", &amount);
                withdraw(&balance, amount);  // Pass-by-Reference
                break;
            }
            case 4: {
                double principal, rate;
                int years, compounds;
                printf("Enter the principal amount: $");
                scanf("%lf", &principal);
                printf("Enter the annual interest rate (in %%): ");
                scanf("%lf", &rate);
                printf("Enter the number of years: ");
                scanf("%d", &years);
                printf("Enter the compounding frequency per year: ");
                scanf("%d", &compounds);

                rate /= 100;  // Convert rate to decimal
                double finalAmount = calculateCompoundInterest(principal, rate, years, compounds);
                printf("Final amount after %d years: $%.2f\n", years, finalAmount);
                break;
            }
            case 5:
                printf("Thank you for using the Banking System!\n");
                break;
            default:
                printf("Invalid choice, try again.\n");
                break;
        }
    } while (choice != 5);

    return 0;
}
