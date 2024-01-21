#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <windows.h>

#define BOARD_SIZE 10

static int roll_dice(void);
void displayBoard(int positionPlayer1, int positionPlayer2);
int check_chutes(int positionPlayer);
int check_ladder(int positionPlayer);

typedef struct Chutes {
    int start;
    int end;
} Chutes;

Chutes chutes[] = {
        {99, 1},
        {65, 40},
        {27, 3},
        {70, 51},
        {-1, -1} // end
};

typedef struct Ladders {
    int start;
    int end;
} Ladders;

Ladders ladders[] = {
        {13, 42},
        {60, 83},
        {70, 90},
        {4, 21},
        {-1, -1} // end
};

int main() {
    char input;
    int ch;
    int dice_value;
    int positionPlayer1 = 0;
    int positionPlayer2 = 0;

    printf("-----------------------------CHUTES AND LADDERS-----------------------------\n\n");
    printf("Rules:\n");
    printf("\tFirst player to 100 wins.\n");
    printf("\tSelect a player and roll the dice.\n\n");

    do {

        printf("The chutes are from:\n");
        for (int i = 0; chutes[i].start != -1; i++) {
            if (i == 0 || i == 2) {
                printf("\t%d to %d\t", chutes[i].start, chutes[i].end);
            } else {
                printf("\t%d to %d", chutes[i].start, chutes[i].end);
            }
        }
        printf("\n");
        printf("The ladders are from:\n");
        for (int i = 0; ladders[i].start != -1; i++) {
            printf("\t%d to %d", ladders[i].start, ladders[i].end);
        }
        printf("\n\n");
        printf("Enter an option:\n");
        printf("\t1. Player 1's turn\n");
        printf("\t2. Player 2's turn\n");
        printf("\t3. Quit Game\n");
        scanf("%s", &input);


        switch(input) {
            case '1':
                printf("Player 1's turn.\n");
                dice_value = roll_dice();
                positionPlayer1 += dice_value;
                if (positionPlayer1 < 100) {
                    positionPlayer1 = check_chutes(positionPlayer1);
                    positionPlayer1 = check_ladder(positionPlayer1);
                } else {
                    printf("Congratulations Player 1 wins!\n");
                    Sleep(1500);
                    exit(0);
                }
                break;
            case '2':
                dice_value = roll_dice();
                positionPlayer2 += dice_value;
                if (positionPlayer2 < 100) {
                    positionPlayer2 = check_chutes(positionPlayer2);
                    positionPlayer2 = check_ladder(positionPlayer2);
                } else {
                    printf("Congratulations Player 2 wins!\n");
                    Sleep(1500);
                    exit(0);
                }
                break;
            case '3':
                printf("Good bye.\n");
                return 0;
            default:
                printf("Incorrect menu choice. Try again.\n");
        }
        displayBoard(positionPlayer1, positionPlayer2);
        Sleep(2000);
    } while (1);

}

static int roll_dice(void) {
    int dice_value_total = 0;
    int dice_value;
    char input;
    int ch;

    do {
        printf("Press enter to roll the dice.");
        // Clear the input buffer
        while ((ch = getchar()) != '\n' && ch != EOF);

        input = getchar();

        if(input != '\n') {
            continue;
        }
        srand(time(0));
        dice_value = rand() % 6 + 1; // generate random number between 1 and 6
        dice_value_total += dice_value;
        printf("You rolled a %i!\n\n", dice_value);
        if (dice_value == 6) {
            printf("You get to roll again.\n\n");
        }
        else {
            break;
        }
    } while (1);

    Sleep(1500);
    return dice_value_total;
}

void displayBoard(int positionPlayer1, int positionPlayer2){
    int board[BOARD_SIZE][BOARD_SIZE];

    // Create the board with numbers.
    for (int i = 0; i < BOARD_SIZE; ++i) {
        for (int j = 0; j < BOARD_SIZE; ++j) {
            if (i % 2 == 0) {
                board[i][j] = i * BOARD_SIZE + j + 1;
            } else {
                board[i][BOARD_SIZE - j - 1] = i * BOARD_SIZE + j + 1;
            }
        }
    }
    printf("----------------------------------------------------------------------------\n");
    // Display the board.
    for (int i = BOARD_SIZE - 1; i >= 0; --i) {
        for (int j = 0; j < BOARD_SIZE; ++j) {
            if (board[i][j] == positionPlayer1) {
                printf("|P1|\t");
            } else if (board[i][j] == positionPlayer2) {
                printf("|P2|\t");
            } else {
                printf("%d\t", board[i][j]);
            }
        }
        printf("\n\n");
    }
    printf("Player 1's position: %i\n", positionPlayer1);
    printf("Player 2's position: %i\n\n", positionPlayer2);
    printf("-----------------------------CHUTES AND LADDERS-----------------------------\n");
}

int check_chutes(int positionPlayer) {
    char chuteMsg[] = "You landed on a chute! :'(\n";
    for (int i = 0; chutes[i].start != -1; i++) {
        if (positionPlayer == chutes[i].start) {
            printf("%s", chuteMsg);
            return chutes[i].end;
        }
    }

    return positionPlayer;
}

int check_ladder(int positionPlayer) {
    char ladderMsg[] = "You landed on a ladder! :D\n";
    for (int i = 0; ladders[i].start != -1; i++) {
        if (positionPlayer == ladders[i].start) {
            printf("%s", ladderMsg);
            return ladders[i].end;
        }
    }
    return positionPlayer;
}
