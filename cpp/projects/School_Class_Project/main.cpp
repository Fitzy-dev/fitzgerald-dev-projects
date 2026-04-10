// Jordan Fitzgerald
// 4/10/2026
// School Class Project - Main File

#include <iostream>
#include "School.h"
using namespace std;

int main()
{
    // Create a Department Object
    Department dept("Morhouse College", "Math and Science", "Computer Science");
    dept.setLocation("830 Westview Drive");
    dept.setTuition(5000.00);
    dept.setNumFaculty(5);
    dept.setNumStudents(130);
    dept.displayDepartmentInfo();
    return 0;
}
