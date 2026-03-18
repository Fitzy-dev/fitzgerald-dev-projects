// Jordan Fitzgerald
// 3/18/2026
// Car Class

#include <iostream>
#include <string>
using namespace std;
#ifndef CAR_H
#define CAR_H
class Car
{
    private:
        string make;
        string model;
        int year;
    public:
        // Constructor
        Car(string m, string mo, int yr)
        {
            make = m;
            model = mo;
            year = yr;
        }
        // Mutators - Settors
        void setMake(string m)
        {
            make = m;
        }
        void setModel(string mo)
        {
            model = mo;
        }
        void setYear(int yr)
        {
            year = yr;
        }
        // Getters - Accessors
        string getMake() const
        {
            return make;
        }
        string getModel() const
        {
            return model;
        }
        int getYear() const
        {
            return year;
        }
        // Display Function
        void display()
        {
            cout << "--------- Car ---------" << endl;
            cout << "Make: " << make << endl;
            cout << "Model: " << model << endl;
            cout << "Year: " << year << endl;
        }
#endif
};

int main()
{   
    // Creating Car Variables
    Car a = {"Mercedes", "AMG", 2018};
    Car b = {"Honda", "Accord", 2023};
    Car c = {"Telsa", "Model Y", 2020};
    // Displaying Them in the console
    a.display();
    b.display();
    c.display();

    return 0;
};
