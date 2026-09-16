// Jordan Fitzgerald
// 3/28/2026
// Bank Account Project

#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

class BankAccount
{
    private:
        double balance = 0.0;
        std::string accountHolder;
    public:
        BankAccount(const std::string& name, double initialBalance)
        {
            accountHolder = name;
            if (initialBalance >= 0)
            {
                balance = initialBalance;
            }
            else
            {
                balance = 0.0;
            }
        }
        void deposit(double amount)
        {
            if (amount > 0)
            {
                balance += amount;
            }
        }

        bool withdraw(double amount)
        {
            if (amount > 0 && amount <= balance)
            {
                balance -= amount;
                return true;
            }
            return false;
        }

        double getBalance() const
        {
            return balance;
        }

        void displayInfo() const 
        {
            cout << "Account Holder: " << accountHolder << endl;
            cout << "Current Balance: $" <<  balance << endl;
        }

        

};

int main()
{
    BankAccount account("John Doe", 1000.0);
    account.displayInfo();

    account.deposit(500.0);
    cout << "After deposit of $500:" << endl;
    account.displayInfo();

    account.withdraw(200.0);
    cout << "After withdrawal of $200:" << endl;
    account.displayInfo();

    account.deposit(700.0);
    cout << "After deposit of $700:" << endl;
    account.displayInfo();

    account.withdraw(400.0);
    cout << "After withdrawal of $400:" << endl;
    account.displayInfo();

    cout << "Final Balance: $" << account.getBalance() << endl;

    return 0;
}

