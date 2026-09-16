// Jordan Fitzgerald
//  2/23/2026
// Program: Dog Class with Methods

#include <iostream>
#include <string>
using namespace std;

// Dog class defintion 
class Dog
{
private:
    string name;
    string breed;
    int age;

public:
    //Contsructor
    Dog(string n, string b, int a)
    {
        name = n;
        breed = b;
        age = a;
    }
    // Method: Make the dog bark
    void bark()
    {
        cout << name << " says: Woof! Woof!" << endl;
    }

    // Method: Display dog info
    void displayInfo()
    {
        cout << "\n--- Dog Profile ---" << endl;
        cout << "Name: " << name << endl;
        cout << "Breed: " << breed << endl;
        cout << "Age: " << age << endl;
    }

    // Method: haveBirthday increases age
    void haveBirthday()
    {
        age++;
        cout << name << " just turned " << age << " years old!" << endl;
    }


};

int main()
{
    cout << "=== Dog Class Demo ===\n";
    // Create dog object
    Dog myDog("Buddy", "Pitbull", 3);

    // Call methods 
    myDog.displayInfo();
    myDog.bark();
    myDog.haveBirthday();
    myDog.displayInfo();
    
    return 0;
}