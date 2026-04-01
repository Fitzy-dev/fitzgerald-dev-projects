// Jordan Fitzgerald
// 4/1/2026
// School Project

#include <iostream>
#include <string>
using namespace std;

class Student
{
    protected:
        string name;
        int age;
    public:
        Student(string n, int a)
        {
            name = n;
            age = a;
        }


};

class HighSchoolStudent : public Student
{
    private:
        double gpa;
    public:
        HighSchoolStudent(string n, int a, double g) : Student(n, a)
        {
            name = n;
            age = a;
            gpa = g;
        }
        void displayInfo()
        {
            cout << "Name: " << name << endl;
            cout << "Age: " << age << endl;
            cout << "GPA: " << gpa << endl;
        }
};

int main()
{
    HighSchoolStudent student1("Jordan Fitzgerald", 25, 3.8);
    student1.displayInfo();

    return 0;
}
