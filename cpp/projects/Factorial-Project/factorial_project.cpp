// Jordan Fitzgerald 
// 4/15/2026
// Factorial Question Game - Main File

#include <iostream>
using namespace std;

int factorial(int n) {
    if (n == 0 || n == 1)
        return 1;
    else
        return n * factorial(n - 1);
}

int main() 
{
    srand(time(0)); // Seed for random number generation

    string playAgain = "yes";
    while (playAgain == "yes")
    {
        int score = 0;
        cout << "Welcome to the Factorial Question Game!" << endl;
        for (int round = 1; round <=3; round++)
        {
            int num = rand() % 11; // Random number between 0 and 10
            int guess;
            cout << "Round " << round << ": What is " << num << "! ? ";
            cin >> guess;

            int answer = factorial(num);
            if (guess == answer)
            {
                cout << "Correct!" << endl;
                score++;
            }
            else
            {
                cout << "Wrong! The correct answer is " << answer << "." << endl;
            }

            cout << "Current Score: " << score << endl;

        }
        cout << "Game Over! Your final score is: " << score << "/3" << endl;

        if (score == 3)
            cout << "Excellent! You got all questions right!" << endl;
        else if (score == 2)
            cout << "Great job! You got 2 out of 3 correct!" << endl;
        else if (score == 1)
            cout << "Not bad! You got 1 out of 3 correct!" << endl;
        else
            cout << "Better luck next time! You got all questions wrong!" << endl;

        cout << "Do you want to play again? (yes/no): ";
        cin >> playAgain;
    }

    cout << "Thanks for playing the Factorial Question Game! Goodbye!" << endl;
    

    return 0;
}
