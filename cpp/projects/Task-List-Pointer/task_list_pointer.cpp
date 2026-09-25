// Jordan Fitzgerald
// 9/8/2026
// Task List (Pointer) Program

#include <iostream>
using namespace std;

//---------------------------------------------------------
// Node Structure
//---------------------------------------------------------
struct Node
{
    string task;
    Node* next;
};

//---------------------------------------------------------
// Function Prototypes
//---------------------------------------------------------
void displayMenu();
void addTask(Node*& head, int& numTasks);
void deleteTask(Node*& head, int& numTasks);
void printTaskCount(int numTasks);
void printForward(Node* head);
void printReverse(Node* current, int position);
void deleteList(Node*& head);

//---------------------------------------------------------
// Main Function 
//---------------------------------------------------------
int main()
{
    Node* head = nullptr;
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
                addTask(head, numTasks);
                break;

            case 2:
                deleteTask(head, numTasks);
                break;

            case 3:
                printTaskCount(numTasks);
                break;

            case 4:
                printForward(head);
                break;

            case 5:
                printReverse(head, numTasks);
                break;

            case 6:
                cout << "Exit Program" << endl;
                break;

            default:
                cout << "Invalid choice. Please try again." << endl;
            
        }

    } while (choice != 6);

    // Clean up memory before exiting
    deleteList(head);

    return 0;
}

//---------------------------------------------------------
// Display Menu Function
//---------------------------------------------------------
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
// Add Function to add a task at a specific position in the linked list 
//---------------------------------------------------------
void addTask(Node*& head, int& numTasks)
{
    string taskName;
    int position;

    cout << "Enter task name and its position -> ";
    cin >> taskName >> position;

    if (position < 1 || position > numTasks + 1)
    {
        cout << "Invalid position." << endl;
        return;
    }

    if (taskName.length() != 2)
    {
        cout << "Invalid task name." << endl;
        return;
    }

    // Create a new node
    Node* newNode = new Node;

    newNode->task = taskName;
    newNode->next = nullptr;

    // Insert the new node at the specified position
    if (position == 1)
    {
        newNode->next = head;
        head = newNode;
    } else 
    {
        Node* current = head;

        for(int i = 1; i < position - 1; i++)
        {
            current = current->next;
        }

        newNode->next = current->next;
        current->next = newNode;

    }

    numTasks++;

    //Display Updated Task List
    printTaskCount(numTasks);
    printForward(head);
    printReverse(head, numTasks);
}

//---------------------------------------------------------
// Delete Function to delete a task at a specific position in the linked list
//---------------------------------------------------------
void deleteTask(Node*& head, int& numTasks)
{
    int position;

    if (numTasks == 0)
    {
        cout << "Task List is empty." << endl;
        return;
    }

    cout << "Enter task position -> ";
    cin >> position;

    if (position < 1 || position > numTasks)
    {
        cout << "Invalid position." << endl;
        return;
    }

    Node* deleteNode;

    if (position == 1)
    {
        deleteNode = head;
        head = head->next;
    } else
    {
        Node* current = head;

        // Move to the node before the node being deleted
        for (int i = 1; i < position - 1; i++)
        {
            current = current->next;
        }

        deleteNode = current->next;
        current->next = deleteNode->next;
    }
    
    // Save the deleted task name
    string deletedTask = deleteNode->task;

    delete deleteNode;

    numTasks--;

    cout << "Deleted task = " << deletedTask << endl;
    cout << "Number of remaining tasks = " << numTasks << endl;

    printForward(head);
    printReverse(head, 1);
}

//---------------------------------------------------------
// Print number of tasks in the linked list
//---------------------------------------------------------
void printTaskCount(int numTasks)
{
    cout << "Number of tasks = " << numTasks << endl;
}

//---------------------------------------------------------
// Print tasks in current order
//---------------------------------------------------------
void printForward(Node* head)
{
    Node* current = head;
    int position = 1;

    while (current != nullptr)
    {
        cout << position << ":" << current->task << " ";

        current = current->next;
        position++;
    }

    cout << endl;
}

//---------------------------------------------------------
// Print tasks in reverse order
//---------------------------------------------------------
void printReverse(Node* head, int numTasks)
{
    if (head == nullptr)
    {
        return;
    }

    // Recursively call the function with the next node
    printReverse(head->next, numTasks);

    // Print the current node's task
    cout << numTasks << ":" << head->task << " ";
    numTasks--;
}


//---------------------------------------------------------
// Delete the entire linked list to free memory
//---------------------------------------------------------
void deleteList(Node*& head)
{
    Node* current = head;

    while (current != nullptr)
    {
        current = head;
        head = head->next;

        delete current;
    }

}