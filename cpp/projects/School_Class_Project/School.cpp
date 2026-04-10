// Jordan Fitzgerald
// 4/10/2026
// School Class Project - Function Definitions

#include "School.h"

// School Class Function Definitions
School::School(string n)
{
    name = n;
    location = "";
    tuition = 0.0;
}

void School::setLocation(string loc)
{
    location = loc;
}

void School::setTuition(float t)
{
    tuition = t;
}

string School::getName() const
{
    return name;
}

string School::getLocation() const
{
    return location;
}

float School::getTuition() const
{
    return tuition;
}

void School::displayInfo() const
{
    cout << "School Name: " << name << endl;
    cout << "Location: " << location << endl;
    cout << "Tuition: $" << tuition << endl;
}

// Division Class Function Definitions
Division::Division(string n, string d) : School(n)
{
    divisionName = d;
}

string Division::getDivisionName() const
{
    return divisionName;
}

void Division::displayDivisionInfo() const
{
    displayInfo();
    cout << "Division Name: " << divisionName << endl;
}

// Department Class Function Definitions
Department::Department(string n, string d, string dept) : Division(n, d)
{
    departmentName = dept;
}

void Department::setNumFaculty(int faculty)
{
    numFaculty = faculty;
}

void Department::setNumStudents(int students)
{
    numStudents = students;
}

string Department::getDepartmentName() const
{
    return departmentName;
}

int Department::getNumFaculty() const
{
    return numFaculty;
}

int Department::getNumStudents() const
{
    return numStudents;
}

void Department::displayDepartmentInfo() const
{
    displayDivisionInfo();
    cout << "Department Name: " << departmentName << endl;
    cout << "Number of Faculty: " << numFaculty << endl;
    cout << "Number of Students: " << numStudents << endl;
}
