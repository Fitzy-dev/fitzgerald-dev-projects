// Jordan Fitzgerald
// 8/24/26
// Task List (ARRAY) Program 


#include <iostream>
using namespace std;

const int MAX_TASKS = 7;


// Function Prototypes
void displayMenu();
void addTask(string tasks[], int& numTasks);
void deleteTask(string tasks[], int& numTasks);
void printTaskCount(int numTasks);
void printForward(string tasks[], int numTasks);
void printReverse(string tasks[], int numTasks);

int main()
{
    string tasks[MAX_TASKS];
    int numTasks = 0;
    int choice;
    
    do 
    {
        displayMenu();
        
        cout << "Enter a choice: ";
        cin >> choice;

        // Switch statement to handle user choices
        switch (choice)
        {
            case 1:
                addTask(tasks, numTasks);
                break;

            case 2:
                deleteTask(tasks, numTasks);
                break;

            case 3:
            
                printTaskCount(numTasks);
                break;

            case 4:
                printForward(tasks, numTasks);
                break;
                
            case 5:
                printReverse(tasks, numTasks);
                break
                ;
            case 6:
                cout << "Exit Program" << endl;
                break;

            default:
                cout << "Invalid choice. Please try again." << endl;
            
        }

    } while (choice != 6);

    return 0;
}

// Function Definitions


// Display Function to give user options
void displayMenu()
{
    cout << "\n------- Task List Menu -------" << endl;
    cout << "1). Add Task at Specific Position" << endl;
    cout << "2). Delete Task at Specific Position" << endl;
    cout << "3). Print Number of Task in Task List" << endl;
    cout << "4). Print Tasks in Current Order" << endl;
    cout << "5). Print Tasks in Reverse Order" << endl;
    cout << "6). Quit" << endl;
}


//---------------------------------------------------------
// Add Task Function
void addTask(string tasks[], int& numTasks)
{
    string taskName;
    int position;
    // Check if the task list is full
    if (numTasks >= MAX_TASKS)
    {
        cout << "Task List is full." << endl;
        return;
    }

    // User Prompt for task name and position
    cout << "Enter task name and its position -> ";
    cin >> taskName >> position;

    // Check if the position is valid
    if (position < 1 || position > numTasks + 1)
    {
        cout << "Invalid position." << endl;
        return;
    }

    // Check task name length
    if (taskName.length() !=  2)
    {
        cout << "Invalid Task Name." << endl;
        return;
    }

    // Shift Tasks to the right to make space for the new task
    for (int i = numTasks; i > position - 1; i--)
    {
        tasks[i] = tasks[i - 1];
    }

    // Insert new task at the specified position
    tasks[position - 1] = taskName;
    numTasks++;

    // Display number of tasks
    printTaskCount(numTasks);

    // Display tasks in current order
    printForward(tasks, numTasks);

    // Display tasks in reverse order
    printReverse(tasks, numTasks);
}


//---------------------------------------------------------
// Delete Task Function
//---------------------------------------------------------

void deleteTask(string tasks[], int& numTasks)
{
    int position;

    // Check if the task list is empty
    if (numTasks == 0)
    {
        cout << "Task List is empty." << endl;
        return;
    }

    // User Prompt for task position
    cout << "Enter task position -> ";
    cin >> position;

    // Check if the position is valid
    if (position < 1 || position > numTasks)
    {
        cout << "Invalid position." << endl;
        return;
    }

    // Save the deleted task name
    string deletedTask = tasks[position - 1];

    // Shift tasks to the left
    for (int i = position - 1; i < numTasks - 1; i++)
    {
        tasks[i] = tasks[i + 1];
    }

    // Decrease the number of tasks
    numTasks--;

    // Display deleted task
    cout << "Deleted task = " << deletedTask << endl;

    // Display remaining tasks
    cout << "Number of remaining tasks = " << numTasks << endl;

    // Display tasks in current order
    printForward(tasks, numTasks);

    // Display tasks in reverse order
    printReverse(tasks, numTasks);

}

// Print Task Count Function
void printTaskCount(int numTasks)
{
    cout << "Number of tasks = " << numTasks << endl;
}

// Print Tasks in Current Order Function
void printForward(string tasks[], int numTasks)
{
    for (int i = 0; i < numTasks; i++)
    {
        cout << i + 1 << ":"  << tasks[i] << " ";
    }
    cout << endl;
}

// Print Tasks in Reverse Order Function
void printReverse(string tasks[], int numTasks)
{
    for (int i = numTasks - 1; i >= 0; i--)
    {
        cout << i + 1 << ":" << tasks[i] << " ";
    }
    cout << endl;
}