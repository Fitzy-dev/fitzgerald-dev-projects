// Jordan Fitzgerald
// 3/28/2026
// Reverse Array Project

#include <iostream>
using namespace std;

void reverseArray(int* arr, int size)
{
    int* start = arr;
    int* end = arr + size - 1;

    while (start < end)
    {
        int temp = *start;
        *start = *end;
        *end = temp;

        start++;
        end--;
    }
}

int main()
{
    int arr[5] = {10, 20, 30, 40, 50};
    cout << "Original array: ";
    for (int i = 0; i < 5; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;

    reverseArray(arr, 5);

    cout << "Reversed array: ";
    for (int i = 0; i < 5; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
