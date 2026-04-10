// Jordan Fitzgerald
// 4/10/2026
// Rectangle Project - Main File
#include <iostream>
#include "Rectangle.h"
using namespace std;

int main()
{
    Square sq;

    int side;
    cout << "Enter the side length of the square: ";
    cin >> side;
    sq.set(side);
    sq.displayInfo();

    return 0;
}
