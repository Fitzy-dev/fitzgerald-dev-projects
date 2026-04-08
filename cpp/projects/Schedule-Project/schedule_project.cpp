// Jordan Fitzgerald
// 4/8/2026
// Schedule Project

#include <iostream>
#include <string>
#include <vector>
#include <limits>
using namespace std;

class Schedule
{
    private:
        string name;
        int time;
        string loc;
        double crhour;
    public:
        Schedule()
        {
            name = "";
            time = 0;
            loc = "";
            crhour = 0.0;
        }
        Schedule(string n, int t, string l, double c)
        {
            name = n;
            time = t;
            loc = l;
            crhour = c;
        }

        string getName()
        {
            return name;
        }
        int getTime()
        {
            return time;
        }
        string getLoc()
        {
            return loc;
        }
        double getCrHour()        
        {
            return crhour;
        }

        void setName(string n)
        {
            name = n;
        }
        void setTime(int t)
        {
            time = t;
        }
        void setLoc(string l)
        {
            loc = l;
        }
        void setCrHour(double c)
        {
            crhour = c;
        }

        void displayInfo()
        {
            cout << "\nCourse Information:";
            cout << "\nCourse Name: " << name;
            cout << "\nTime: " << time;
            cout << "\nLocation: " << loc;
            cout << "\nCredit Hours: " << crhour << endl;
        }
};

int main()
{
    int numCourses;

    cout << "Enter the number of courses: ";
    cin >> numCourses;

    while (numCourses < 3)
    {
        cout << "Please enter at least 3 courses: ";
        cin >> numCourses;
    }

    vector<Schedule> courses(numCourses);

    for (int i = 0; i < numCourses; i++)
    {
        string name, loc;
        int time;
        double crhour;

        cout << "Enter course name: ";
        cin.ignore(); // Clear the input buffer
        getline(cin, name);

        cout << "Enter course time (e.g., 900 for 9:00 AM): ";
        cin >> time;

        cout << "Enter course location: ";
        cin.ignore(); // Clear the input buffer
        getline(cin, loc);

        cout << "Enter credit hours: ";
        cin >> crhour;

        courses[i] = Schedule(name, time, loc, crhour);
    }

    cout << "\nYour Schedule:\n";
    for (int i = 0; i < numCourses; i++)
    {
        courses[i].displayInfo();
    }

    return 0;


}
        
