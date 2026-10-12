// Jordan Fitzgerald 
// 10/12/26
// Radix Sort Program

#include <iostream>
#include <vector>

using namespace std;

// Function to get the maximum value in the array
int getMax(const vector<int>& arr) 
{
    int maxVal = arr[0];
    for (int num : arr) 
    {
        if (num > maxVal) 
        {
            maxVal = num;
        }
    }
    return maxVal;
}

// Function to print the array
void printArray(const vector<int>& arr) 
{
    for (int num : arr) 
    {
        cout << num << " ";
    }
    cout << endl;
}
// Counting sort function used by radix sort
void countingSort(vector<int>& arr, int exp) 
{
    int n = arr.size();
    vector<int> output(n);
    int count[10] = {0};

    for (int i = 0; i < n; i++) 
    {
        count[(arr[i] / exp) % 10]++;
    }

    for (int i = 1; i < 10; i++) 
    {
        count[i] += count[i - 1];
    }

    for (int i = n - 1; i >= 0; i--) 
    {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }

    for (int i = 0; i < n; i++) 
    {
        arr[i] = output[i];
    }
}

// Radix sort function
void radixSort(vector<int>& arr) 
{
    int maxVal = getMax(arr);

    for (int exp = 1; maxVal / exp > 0; exp *= 10) {
        countingSort(arr, exp);
        cout << "After sorting with exponent " << exp << ": ";
        printArray(arr);
    }
}
// Main function
int main() 
{
    vector<int> arr = {170, 45, 75, 90, 802, 24, 2, 66};

    cout << "Original array: ";
    printArray(arr);

    radixSort(arr);

    cout << "Sorted array: ";
    printArray(arr);

    return 0;
}

