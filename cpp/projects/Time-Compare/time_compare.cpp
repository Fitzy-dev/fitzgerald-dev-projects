// Jordan Fitzgerald
// 3/28/2026
// Time Comparison Project

#include <iostream>
using namespace std;

struct Time 
{
    int hour;
    int minute;
    int second;
};

bool isEarlier(const Time& t1, const Time& t2) 
{
    if (t1.hour < t2.hour) return true;
    if (t1.hour > t2.hour) return false;

    if (t1.minute < t2.minute) return true;
    if (t1.minute > t2.minute) return false;

    return t1.second < t2.second;
}

int main()
{
    Time a = {9, 30, 0};
    Time b = {12, 15, 0};

    if (isEarlier(a, b)) {
        cout << "Time A is earlier than Time B." << endl;
    } else {
        cout << "Time A is not earlier than Time B." << endl;
    }

    return 0;
}
