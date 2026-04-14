// Jordan Fitzgerald
// 4/14/2026
// Template Min and Max Function - Main File

#include <iostream>
#include <string>
using namespace std;

// Template Functions for Min and Max
template <typename T>
T minimum(T a, T b)
{
    if (a < b)
        return a;
    else
        return b;
}
template <typename T>
T maximum(T a, T b)
{
    if (a > b)
        return a;
    else
        return b;
}

int main()
{
    // INT Test
    cout << "Min Test (int): " << minimum(5, 10) << endl;
    cout << "Max Test (int): " << maximum(5, 10) << endl;

    // FLOAT Test
    cout << "Min Test (float): " << minimum(5.5f, 10.1f) << endl;
    cout << "Max Test (float): " << maximum(5.5f, 10.1f) << endl;

    // STRING Test
    cout << "Min Test (string): " << minimum(string("apple"), string("banana")) << endl;
    cout << "Max Test (string): " << maximum(string("apple"), string("banana")) << endl;

    return 0;
}
