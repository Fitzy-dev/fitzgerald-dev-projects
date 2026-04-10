// Jordan Fitzgerald
// 4/10/2026
// School Class Project - Header File

#ifndef SCHOOL_H
#define SCHOOL_H

#include <iostream>
#include <string>
using namespace std;

// Base class for School
class School 
{
    private:
        string name;
        string location;
    protected:
        float tuition;
    public:
        School(string n);
        void setLocation(string loc);
        void setTuition(float t);
        string getName() const;
        string getLocation() const;
        float getTuition() const;
        void displayInfo() const;
};

// Derived class for Division
class Division : public School
{
    private:
        string divisionName;
    public:
        Division(string n, string d);
        string getDivisionName() const;
        void displayDivisionInfo() const;

};

// Derived class for Department
class Department : public Division
{
    private:
        string departmentName;
        int numFaculty;
        int numStudents;
    public:
        Department(string n, string d, string dept);
        void setNumFaculty(int faculty);
        void setNumStudents(int students);
        string getDepartmentName() const;
        int getNumFaculty() const;
        int getNumStudents() const;
        void displayDepartmentInfo() const;


};

#endif
