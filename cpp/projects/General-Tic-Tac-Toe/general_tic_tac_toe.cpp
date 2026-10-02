// Jordan Fitzgerald
// General Tic Tac Toe
// 9/24/26

#include <iostream>
#include <string>
using namespace std;

//---------------------------------------------------------
// Constants
//---------------------------------------------------------
const int MIN_PLAYERS = 2;
const int MAX_PLAYERS = 7;

const int MIN_ROWS = 3;
const int MAX_ROWS = 9;

const int MIN_COLS = 3;
const int MAX_COLS = 12;

//---------------------------------------------------------
// Player Structure
//---------------------------------------------------------
struct Player
{
    string firstName;
    string lastName;
    char piece;
    int wins;
    int losses;
    int draws;
};

//---------------------------------------------------------
// Function Prototypes
//---------------------------------------------------------
void getPlayers(Player players[], int& numPlayers);
bool validName(string name);
void formatName(string& name);

void getBoardSize(int& rows, int& cols);
void initializeBoard(char board[][MAX_COLS], int rows, int cols);
void displayBoard(char board[][MAX_COLS], int rows, int cols);

void getMove(char board[][MAX_COLS], int rows, int cols, Player players[], int currentPlayer);
bool validMove(string move, char board[][MAX_COLS], int rows, int cols, int& row, int& col);

bool checkWinner(char board[][MAX_COLS], int rows, int cols, char piece);
bool boardFull(char board[][MAX_COLS], int rows, int cols);
void markWinningPieces(char board[][MAX_COLS], int rows, int cols, char piece);
int nextPlayer(int currentPlayer, int numPlayers);

void updateStatistics(Player players[], int numPlayers, int winner);
void displayStatistics(Player players[], int numPlayers, int gamesPlayed);

int playGame(Player players[], int numPlayers, int startingPlayer);

//---------------------------------------------------------
// Main Function
//---------------------------------------------------------
int main()
{
    Player players[MAX_PLAYERS];

    int numPlayers;
    int gamesPlayed = 0;
    int startingPlayer = 1;
    int winner;
    char playAgain = 'y';

    getPlayers(players, numPlayers);

    while (playAgain == 'y' || playAgain == 'Y')
    {
        winner = playGame(players, numPlayers, startingPlayer);
        gamesPlayed++;

        updateStatistics(players, numPlayers, winner);
        displayStatistics(players, numPlayers, gamesPlayed);

        if (winner != -1)
        {
            startingPlayer = nextPlayer(winner, numPlayers);
        } 
        else 
        {
            startingPlayer = nextPlayer(startingPlayer, numPlayers);
        }

        cout << "\nWould you like to play again? (y/n): ";
        cin >> playAgain;

        while (playAgain != 'y' && playAgain != 'Y' && playAgain != 'n' && playAgain != 'N')
        {
            cout << "Invalid input. Please enter 'y' or 'n': ";
            cin >> playAgain;
        }
    }
    cout << "Thanks for playing!" << endl;

    return 0;
}

//---------------------------------------------------------
// Get Players Function to get player information
//---------------------------------------------------------
void getPlayers(Player players[], int& numPlayers)
{
    cout << "Enter number of players (2-7): ";
    cin >> numPlayers;

    while (numPlayers < MIN_PLAYERS || numPlayers > MAX_PLAYERS)
    {
        cout << "Invalid number of players. " << endl;
        cout << "Please enter a number between 2 and 7:";
        cin >> numPlayers;   
    }

    for (int i = 0; i < numPlayers; i++)
    {
        cout << "\nEnter Player " << (i + 1) << " First Name: ";
        cin >> players[i].firstName;

        while (!validName(players[i].firstName))
        {
            cout << "Invalid name." << endl;
            cout << "Enter Player " << (i + 1) << " First Name: "; 
            cin >> players[i].firstName;
        }

        cout << "Enter Player " << (i + 1) << " Last Name: ";
        cin >> players[i].lastName;

        while (!validName(players[i].lastName))
        {
            cout << "Invalid name." << endl;
            cout << "Enter Player " << (i + 1) << " Last Name: ";
            cin >> players[i].lastName;
        }

        formatName(players[i].firstName);
        formatName(players[i].lastName);

        switch (i)
        {
            case 0:
                players[i].piece = 'a';
                break;
            case 1:
                players[i].piece = 'b';
                break;
            case 2:
                players[i].piece = 'c';
                break;
            case 3:
                players[i].piece = 'd';
                break;
            case 4:
                players[i].piece = 'e';
                break;
            case 5:
                players[i].piece = 'f';
                break;
            case 6:
                players[i].piece = 'g';
                break;
        }

        players[i].wins = 0;
        players[i].losses = 0;
        players[i].draws = 0;

        cout << "Player " << (i + 1) << ": " << players[i].firstName << " " << players[i].lastName 
        << ", will use piece: " << players[i].piece << '.' << endl;


    }
}


//---------------------------------------------------------
// Name Validation Function
//---------------------------------------------------------
bool validName(string name)
{
    if (name.length() == 0)
    {
        return false;
    }

    for (int i = 0; i < name.length(); i++)
    {
        if (!(name[i] >= 'A' && name[i] <= 'Z') && !(name[i] >= 'a' && name[i] <= 'z'))
        {
            return false;
        }
    }
    return true;
}

//---------------------------------------------------------
// Format Name Function to capitalize the first letter and make the rest lowercase
//---------------------------------------------------------
void formatName(string& name)
{
    if (name[0] >= 'a' && name[0] <= 'z')
    {
        name[0] = name[0] - 'a' + 'A';
    }

    for (int i = 1; i < name.length(); i++)
    {
        if (name[i] >= 'A' && name[i] <= 'Z')
        {
            name[i] = name[i] - 'A' + 'a';
        }
    }
}

//---------------------------------------------------------
// Board Size Function to get the number of rows and columns for the game board
//---------------------------------------------------------
void getBoardSize(int& rows, int& cols)
{
    cout << "\nEnter number of rows (3-9): ";
    cin >> rows;

    while (rows < MIN_ROWS || rows > MAX_ROWS)
    {
        cout << "Invalid number of rows. " << endl;
        cout << "Please enter a number between 3 and 9: ";
        cin >> rows;
    }

    cout << "Enter number of columns (3-12): ";
    cin >> cols;

    while (cols < MIN_COLS || cols > MAX_COLS)
    {
        cout << "Invalid number of columns. " << endl;
        cout << "Please enter a number between 3 and 12: ";
        cin >> cols;
    }
}

//---------------------------------------------------------
// Initialize Board Function to set all positions on the board to a space character
//---------------------------------------------------------
void initializeBoard(char board[][MAX_COLS], int rows, int cols)
{
    for (int row = 0; row < rows; row++)
    {
        for (int col = 0; col < cols; col++)
        {
            board[row][col] = ' ';
        }
    }   
}

//---------------------------------------------------------
// Display Board Function to print the current state of the game board
//---------------------------------------------------------
void displayBoard(char board[][MAX_COLS], int rows, int cols)
{
    cout << "    ";

    for (int col = 0; col < cols; col++)
    {
        cout << col + 1;

        if (col + 1 < 10)
        {
            cout << "   ";
        }
        else
        {
            cout << "  ";
        }
    }

    cout << endl;

    cout << "  ";
    for (int col = 0; col < cols; col++)
    {
        cout << "----";
    }

    cout << endl;

    for (int row = 0; row < rows; row++)
    {   
        char rowLetter;

        switch (row)
        {
            case 0:
                rowLetter = 'A';
                break;
            case 1:
                rowLetter = 'B';
                break;
            case 2:
                rowLetter = 'C';
                break;
            case 3:
                rowLetter = 'D';
                break;
            case 4:
                rowLetter = 'E';
                break;
            case 5:
                rowLetter = 'F';
                break;
            case 6:
                rowLetter = 'G';
                break;
            case 7:
                rowLetter = 'H';
                break;
            case 8:
                rowLetter = 'I';
                break;
        }

        cout << rowLetter << " |";

        for (int col = 0; col < cols; col++)
        {
            cout << " " << board[row][col] << " |";
        }

        cout << " " << rowLetter << endl;

        cout << "  ";

        for (int col = 0; col < cols; col++)
        {
            cout << "----";
        }

        cout << endl;
    }

    cout << "    ";

    for (int col = 0; col < cols; col++)
    {
        cout << col + 1;

        if (col + 1 < 10)
        {
            cout << "   ";
        }
        else
        {
            cout << "  ";
        }
    }

    cout << endl;

}

//---------------------------------------------------------
// Valid Move Function to check if the move entered by the player is valid
//---------------------------------------------------------
bool validMove(string move, char board[][MAX_COLS], int rows, int cols, int& row, int& col)
{
    if (move.length() < 2 || move.length() > 3)
    {
        return false;
    }

    char rowLetter = move[0];

    if (rowLetter >= 'a' && rowLetter <= 'i')
    {
        rowLetter = rowLetter - 'a' + 'A';
    }

    if (rowLetter < 'A' || rowLetter >= 'A' + rows)
    {
        return false;
    }

    row = rowLetter - 'A';

    if (move.length() == 2)
    {
        if (move[1] < '1' || move[1] > '9')
        {
            return false;
        }

        col = move[1] - '1';
    }
    else
    {
        if (move[1] < '0' || move[1] > '9' || move[2] < '0' || move[2] > '9')
        {
            return false;
        }

        col = (move[1] - '0') * 10 + (move[2] - '0') - 1;
    }

    if (col < 0 || col >= cols)
    {
        return false;
    }

    if (board[row][col] != ' ')
    {
        return false;
    }

    return true;
}

//---------------------------------------------------------
// Get Move Function to prompt the current player for their move and validate it
//---------------------------------------------------------
void getMove(char board[][MAX_COLS], int rows, int cols, Player players[], int currentPlayer)
{
    string move;
    int row;
    int col;

    cout << players[currentPlayer].firstName << ", enter your move: ";
    cin >> move;

    while (!validMove(move, board, rows, cols, row, col))
    {
        cout << "Invalid move. Please try again: " << endl;

        cout << players[currentPlayer].firstName << ", enter your move: ";
        cin >> move; 
    }

    board[row][col] = players[currentPlayer].piece;
}

//---------------------------------------------------------
// Check Winner Function to determine if the current player has won the game in either horizontal, vertical, or diagnoal
//---------------------------------------------------------
bool checkWinner(char board[][MAX_COLS], int rows, int cols, char piece)
{
    for (int row = 0; row < rows; row++)
    {
        for (int col = 0; col < cols - 2; col++)
        {
            if (board[row][col] == piece && board[row][col + 1] == piece && board[row][col + 2] == piece)
            {
                return true;
            }
        }
    }

    for (int row = 0; row < rows - 2; row++)
    {
        for (int col = 0; col < cols; col++)
        {
            if (board[row][col] == piece && board[row + 1][col] == piece && board[row + 2][col] == piece)
            {
                return true;
            }
        }
    }

    for (int row = 0; row < rows - 2; row++)
    {
        for (int col = 0; col < cols - 2; col++)
        {
            if (board[row][col] == piece &&
                board[row + 1][col + 1] == piece &&
                board[row + 2][col + 2] == piece)
            {
                return true;
            }
        }
    }

    for (int row = 0; row < rows - 2; row++)
    {
        for (int col = 2; col < cols; col++)
        {
            if (board[row][col] == piece &&
                board[row + 1][col - 1] == piece &&
                board[row + 2][col - 2] == piece)
            {
                return true;
            }
        }
    }

    return false;
}

//---------------------------------------------------------
// Mark Winning Pieces Function to mark the winning players pieces to uppercase
//---------------------------------------------------------
void markWinningPieces(char board[][MAX_COLS], int rows, int cols, char piece)
{
    char winningPiece = piece - 'a' + 'A';

    for (int row = 0; row < rows; row++)
    {
        for (int col = 0; col < cols - 2; col++)
        {
            if ((board[row][col] == piece || board[row][col] == winningPiece) && 
            (board[row][col + 1] == piece || board[row][col + 1] == winningPiece) && 
            (board[row][col + 2] == piece ||board[row][col + 2] == winningPiece))
            {
                board[row][col] = winningPiece;
                board[row][col + 1] = winningPiece;
                board[row][col + 2] = winningPiece;
            }
        }
    }

    for (int row = 0; row < rows - 2; row++)
    {
        for (int col = 0; col < cols; col++)
        {
            if ((board[row][col] == piece || board[row][col] == winningPiece) && 
            (board[row + 1][col] == piece || board[row + 1][col] == winningPiece) && 
            (board[row + 2][col] == piece ||board[row + 2][col] == winningPiece))
            {
                board[row][col] = winningPiece;
                board[row + 1][col] = winningPiece;
                board[row + 2][col] = winningPiece;
            }
        }
    }

    for (int row = 0; row < rows - 2; row++)
    {
        for (int col = 0; col < cols - 2; col++)
        {
            if ((board[row][col] == piece || board[row][col] == winningPiece) && 
            (board[row + 1][col + 1] == piece || board[row + 1][col + 1] == winningPiece) && 
            (board[row + 2][col + 2] == piece ||board[row + 2][col + 2] == winningPiece))
            {
                board[row][col] = winningPiece;
                board[row + 1][col + 1] = winningPiece;
                board[row + 2][col + 2] = winningPiece;
            }
        }
    }

    for (int row = 0; row < rows - 2; row++)
    {
        for (int col = 2; col < cols; col++)
        {
            if ((board[row][col] == piece || board[row][col] == winningPiece) && 
            (board[row + 1][col - 1] == piece || board[row + 1][col - 1] == winningPiece) && 
            (board[row + 2][col - 2] == piece ||board[row + 2][col - 2] == winningPiece))
            {
                board[row][col] = winningPiece;
                board[row + 1][col - 1] = winningPiece;
                board[row + 2][col - 2] = winningPiece;
            }
        }
    }

}

//---------------------------------------------------------
// Is Board Full Function to check if the game board is full
//---------------------------------------------------------
bool boardFull(char board[][MAX_COLS], int rows, int cols)
{
    for (int row = 0; row < rows; row++)
    {
        for (int col = 0; col < cols; col++)
        {
            if (board[row][col] == ' ')
            {
                return false;
            }
        }
    }

    return true;
}

//---------------------------------------------------------
// Next Player Function to determine the next player in the game
//---------------------------------------------------------
int nextPlayer(int currentPlayer, int numPlayers)
{
    currentPlayer++;

    if (currentPlayer >= numPlayers)
    {
        currentPlayer = 0;
    }

    return currentPlayer;
}

//---------------------------------------------------------
// Update Statistics Function to update the wins, losses, and draws for each player
//---------------------------------------------------------
void updateStatistics(Player players[], int numPlayers, int winner)
{
    if (winner == -1)
    {
        for (int i = 0; i < numPlayers; i++)
        {
            players[i].draws++;
        }
    } 
    else 
    {
        for (int i = 0; i < numPlayers; i++)
        {
            if (i == winner)
            {
                players[i].wins++;
            } 
            else 
            {
                players[i].losses++;
            }
        }
    }
}

//---------------------------------------------------------
// Display Statistics Function to display the wins, losses, and draws for each player
//---------------------------------------------------------
void displayStatistics(Player players[], int numPlayers, int gamesPlayed)
{
    cout << "Total games played: " << gamesPlayed << endl;
    cout << endl;

    cout << "                     ------- ------- -------" << endl;
    cout << "                     |  WIN  | LOSS  | DRAW  |" << endl;
    cout << "                     ------- ------- -------" << endl;

    for (int i = 0; i < numPlayers; i++)
    {
        string fullName = players[i].firstName + " " + players[i].lastName;

        for (int space = fullName.length(); space < 20; space++)
        {
            cout << " ";
        }

        cout << fullName << " |";
        cout << "     " << players[i].wins << " |";
        cout << "     " << players[i].losses << " |";
        cout << "     " << players[i].draws << " |" << endl;

        cout << "                     ------- ------- -------" << endl;
    }
}

//---------------------------------------------------------
// Play Game Function to play a single game of Tic Tac Toe
//---------------------------------------------------------
int playGame(Player players[], int numPlayers, int startingPlayer)
{
    char board[MAX_ROWS][MAX_COLS];

    int rows;
    int cols;
    int currentPlayer = startingPlayer;

    getBoardSize(rows, cols);
    initializeBoard(board, rows, cols);
    displayBoard(board, rows, cols);

    while (true)
    {
        getMove(board, rows, cols, players, currentPlayer);

        if (checkWinner(board, rows, cols, players[currentPlayer].piece))
        {
            cout << players[currentPlayer].firstName << " " << players[currentPlayer].lastName << " wins!" << endl;
            markWinningPieces(board, rows, cols, players[currentPlayer].piece);
            displayBoard(board, rows, cols);
            return currentPlayer;
        }

        displayBoard(board, rows, cols);

        if (boardFull(board, rows, cols))
        {
            cout << "The game is a draw!" << endl;
            return -1;
        }

        currentPlayer = nextPlayer(currentPlayer, numPlayers);
    }

}