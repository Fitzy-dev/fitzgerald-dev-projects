// Jordan Fitzgerald
// 3/18/2026
// Class Date Project

#include <iostream>
using namespace std;
class Date
{
    private:
        int month;
        int day;
        int year;
    // Constructor
    public:
        Date(int m, int d, int y)
        {
            month = m;
            day = d;
            year = y;
        }
        // Functions to display the date
        void displayDate1()
        {
            cout << month << "/" << day << "/" << year;
        }
        void displayDate2()
        {

            if (month == 1)
            {
                cout << "January" << " " << day << ", " << year;
            }
            else if (month == 2)
            {
                cout << "February" << " " << day << ", " << year;
            }
            else if (month == 3)
            {
                cout << "March" << " " << day << ", " << year;
            }
            else if (month == 4)
            {
                cout << "April" << " " << day << ", " << year;
            }
            else if (month == 5)
            {
                cout << "May" << " " << day << ", " << year;
            }
            else if (month == 6)
            {
                cout << "June" << " " << day << ", " << year;
            }
            else if (month == 7)
            {
                cout << "July" << " " << day << ", " << year;
            }
            else if (month == 8)
            {
                cout << "August" << " " << day << ", " << year;
            }
            else if (month == 9)
            {
                cout << "September" << " " << day << ", " << year;
            }
            else if (month == 10)
            {
                cout << "October" << " " << day << ", " << year;
            }
            else if (month == 11)
            {
                cout << "November" << " " << day << ", " << year;
            }
            else if (month == 12)
            {
                cout << "December" << " " << day<< ", "<< year;
            }else
            {
                cout << "Invalid month";
            }
        }
        void displayDate3()
        {   
            if (month == 1)
            {
                cout << day << " " << "January" << " " << year;
            }
            else if (month == 2)
            {
                cout << day << " " << "February" << " " << year;
            }
            else if (month == 3)
            {
                cout << day << " " << "March" << " " << year;
            }
            else if (month == 4)
            {
                cout << day << " " << "April" << " "<< year;
            }
            else if (month == 5)
            {
                cout << day << " "<< "May" << " "<< year;
            }
             else if (month == 6)
             {
                cout << day<< " "<< "June" << " "<< year;
             }
             else if (month == 7)
             {
                cout << day<< " "<< "July" << " "<< year;
             }
             else if (month == 8)
             {
                cout << day<< " "<< "August" << " "<< year;
             }
             else if (month == 9)
             {
                cout << day<< " "<< "September" << " "<< year;
             }
             else if (month == 10)
             {
                cout << day<< " "<< "October" << " "<< year;
             }
             else if (month == 11)
             {
                cout << day<< " "<< "November" << " "<< year;
             }
             else if (month == 12)
             {
                cout << day<< " "<< "December" << ", "<< year;
             }else
             {
                cout <<"Invalid month";
             }
        }
        // Setters
        void setDate(int m, int d, int y)   
        {
            month = m;
            day = d;
            year = y;
        }
        

};
int main() 
{
    Date date(3, 18, 2026);
    Date date2(5, 31, 2007);
    Date date3(12, 25, 2020);
    cout << "Date 1: ";
    date.displayDate1();
    cout << "\nDate 2: ";
    date2.displayDate2();
    cout << "\nDate 3: ";
    date3.displayDate3();
    date3.setDate(4, 1, 2021);
    cout << "\nDate 3 after setting new date: ";
    date3.displayDate1();
    return 0;

}
