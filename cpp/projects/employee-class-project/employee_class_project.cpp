// Jordan Fitzgerald
// 2/25/2026
/* Write a class named Employee that has the following: name(string), idnum(int), dept(string), pos(string)
3 constructors: 1: Default, 2: name and id 3:, all member variables include accessors/mutators
*/

#include <iostream>
#include <string>
using namespace std;

class Employee
{
private:
    string name;
    int idNum;
    string dept;
    string pos;
    
public:
    // Constructor
    Employee();   // #1
    Employee(string, int); // #2
    Employee(string, int, string, string); // #3
    void display();
    
    // Mutators
    void setName(string n)
    {
        name = n;
    }
    
    void setIdNum(int i)
    {
        idNum = i;
    }
    
    void setDept(string d)
    {
        dept = d;
    }
    
    void setPos(string p)
    {
        pos = p;
    }
    
    // Accessors
    string getName()
    {
        return name;
    }
    
    int getIdNum()
    {
        return idNum;
    }
    
    string getDept()
    {
        return dept;
    }
    
    string getPos()
    {
        return pos;
    }
    
    
    
};

//Contructor #1
    Employee::Employee()
    {
        name = "";
        idNum = 0;
        dept = "";
        pos = "";
    }
    //Contructor #2
    Employee::Employee(string n, int i)
    {
        name = n;
        idNum = i;
        dept = "";
        pos = "";
    }
    //Contructor #3
    Employee::Employee(string n, int i, string d, string p)
    {
        name = n;
        idNum = i;
        dept = d;
        pos = p;
    }
    
 // Function prototype display the employee data
    void Employee::display()
    {
        cout << "Name: " << name << endl;
        cout << "ID: " << idNum << endl;
        cout << "Department: " << dept << endl;
        cout << "Position: " << pos << endl;
        cout << "---------------------- " << endl;
    }
// Main program
int main()
{
    // Create 3 different object using the 3 constructors 
    Employee e1; // default
    
    Employee e2("Joshua", 123); // name + id
    
    Employee e3("Taylor", 456, "IT", "Manager"); // all members variables
    
    // Display the data
    
    e1.display();
    e2.display();
    e3.display();
    
    return 0;
}
