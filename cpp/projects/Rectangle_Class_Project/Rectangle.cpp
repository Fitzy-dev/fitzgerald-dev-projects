// Jordan Fitzgerald
// 4/10/2026
// Rectangle Project - Function File
#include "Rectangle.h"

// Rectangle Functions
Rectangle::Rectangle()
{
    length = 0;
    width = 0;

}

int Rectangle::get_Area() const
{
    return length * width;
}

int Rectangle::get_Length() const
{
    return length;
}

int Rectangle::get_Width() const
{
    return width;
}

void Rectangle::set(int l, int w)
{
    length = l;
    width = w;
}

void Rectangle::displayInfo() const
{
    cout << "Length: " << length << endl;
    cout << "Width: " << width << endl;
    cout << "Area: " << get_Area() << endl;
}

// Square Functions
void Square::set(int s)
{
    Rectangle::set(s, s);
}

int Square::get_Perimeter() const
{
    return 4 * get_Length();
}
