// Jordan Fitzgerald
// 2/18/26

// Hospital Management System Assignment

#include <iostream>
using namespace std;

// Enum and Structs Usage

// Enum for Patient Status
enum Status {Admitted, Discharged, Evaluated};

// Nested Struct: Date
struct Date
{
    int day;
    int month;
    int year;
};

struct Patient
{
    int id;
    string name;
    int age;
    Status currentStatus;
    Date admitDate;
};

// Function returning a structure
Patient makePatient(int id, string name, int age, int d, int m, int y)
{
    Patient newPatient;
    newPatient.id = id;
    newPatient.name = name;
    newPatient.age = age;
    newPatient.currentStatus = Admitted;
    newPatient.admitDate.day = d;
    newPatient.admitDate.month = m;
    newPatient.admitDate.year = y;
    return newPatient;
}

// Function to display the data
void display(Patient p)
{
    string statusText[] = {"Admitted", "Discharged", "Evaluated"};
    cout << "ID: " << p.id << endl;
    cout << "Name: " << p.name << endl;
    cout << "Status: " << statusText[p.currentStatus] << endl;
    cout << "Admitted on: " << p.admitDate.month << "/"  <<  p.admitDate.day;
    cout << "/" << p.admitDate.year << endl;
}

// Function taking a pointer
void updateStatus(Patient *p, Status newStatus)
{
    if (p != nullptr)
    {
        p->currentStatus = newStatus;
    }
}

// Main Function 
int main()
{
    // Array for structs
    const int MAX_P = 2;
    Patient patientList[MAX_P];
    
    // Initialize patients
    patientList[0] = makePatient(101, "Mary Jane", 25, 10, 2, 2026);
    patientList[1] = makePatient(105, "Harry Osborne", 35, 8, 15, 2026);
    
    cout << "*** Initial Patient records ***" << endl;
    for(int i=0; i < MAX_P; i++)
    {
        display(patientList[i]);
    }
    // Using Pointer to structure 
    cout << "Updating the status " << endl;
    updateStatus(&patientList[0], Evaluated);
    
    cout << "***Updated Record ***" << endl;
    display(patientList[0]);
    
    return 0;
}

