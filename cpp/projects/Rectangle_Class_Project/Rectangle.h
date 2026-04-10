// Jordan Fitzgerald
// 4/10/2026
// Rectangle Project - Header File
#ifndef RECTANGLE_H
#define RECTANGLE_H

#include <iostream>
#include <string>
using namespace std;

class Rectangle
{
    private:
        int length;
        int width;
    public:
        Rectangle();
        void set(int l, int w);
        int get_Area() const;
        int get_Length() const;
        int get_Width() const;
        void displayInfo() const;

};

class Square : public Rectangle
{
    public:
        void set(int s);
        int get_Perimeter() const;

    
};

#endif
