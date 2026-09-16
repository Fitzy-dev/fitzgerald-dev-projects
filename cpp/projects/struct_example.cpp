// Jordan Fitzgerald
// 2/19/26
// Structs Assignment: Player ADT 

#include <iostream>
#include <string>
using namespace std;
// Create an ADT called "Player" with memebrs name, number, and age
struct Player 
{
    string name;
    int number;
    int age;
};


// Main Function 
int main()
{
    
    string names[5] = {"Sonya","Luke","John","Kim","Tela"};
    int numbers[5] = {45,10,23,27,99};
    int ages[5] = {23,18, 30, 17, 21};

    Player team[5];
    // Use for loop to place data in the parallel arrays into Player array
    for(int i = 0; i < 5; i++)
    {
        team[i].name = names[i];
        team[i].number = numbers[i];
        team[i].age = ages[i];
    }
    // Print out the contents of Players array using a for loop
    cout << "---- All Players ----" << endl;
    for(int i = 0; i < 5; i++)
    {
        cout << "Name: " << team[i].name << ", Jersey #: " << team[i].number << ", Age: " << team[i].age << endl;
    }
    
    // Using a while loop, search through the array and print players between the ages of 20 and 25
    
    cout << "\n---- Players Age 20 to 25 ----" << endl;
    int i = 0;
    bool found = false;
    
    while (i < 5)
    {
        if(team[i].age >= 20 and team[i].age <= 25)
        {
            cout << team[i].name << " - Jersey #: " << team[i].number << endl;
            found = true;
        }
        i++;
    }
    
    if (!found)
    {
        cout << "No Players found between ages 20 and 25." << endl;
    }
    return 0;
}

