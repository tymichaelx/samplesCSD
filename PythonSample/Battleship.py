import time

GRID_SIZE = 13
turn_num = 30


def game_intro(turn_num):
    print("\t" + 6 * "*" + " BATTLESHIP " + "*" * 6 + "\t\n")
    print("Rules:")
    print("Player 1 gets to place the ships.")
    print("Player 2 gets to call in the missile strikes")
    print(f"Player 2 has {turn_num} turns to win the game\n")
    print("\t" + "*" * 22 + "\t\n")


def game_board():
    global GRID_SIZE
    grid = [[' ' if j == 0 else str(j) for j in range(GRID_SIZE)]]

    for i in range(GRID_SIZE - 1):
        row = [' ' for _ in range(GRID_SIZE)]
        row[0] = chr(ord('A') + i)
        grid.append(row)

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            print(grid[i][j], end='\t')
        print()

    return grid


def test_game_board():
    global GRID_SIZE
    grid = [[' ' if j == 0 else str(j) for j in range(GRID_SIZE)]]

    for i in range(GRID_SIZE - 1):
        row = [' ' for _ in range(GRID_SIZE)]
        row[0] = chr(ord('A') + i)
        grid.append(row)

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            print(grid[i][j], end='\t')
        print()

    # place the destroyer's positions (increment column number)
    for i in range(2):
        grid[1][i + 1] = "D"

        # place the battleship's positions (increment row number)
    for i in range(3):
        grid[i + 2][2] = "B"

        # place the submarine's positions (increment column number)
    for i in range(3):
        grid[i + 5][1] = "S"

        # place the cruiser's positions (increment row number)
    for i in range(3):
        grid[4][i + 4] = "C"

        # place the carrier's positions (increment column number)
    for i in range(5):
        grid[5][i + 5] = "A"

    return grid


def get_ship(dict_ships) -> str:
    while True:
        ship = input("Type the name of the ship you would like to place. ").lower()
        if ship in dict_ships:
            return ship
        else:
            print("Invalid ship type, please choose from " + ", ".join(dict_ships))


# def build_ship(ship, dict_ships):
#     return dict_ships.get(ship)

def validate_ship_location(grid, built_ship) -> bool:
    ship_length = len(built_ship)
    # Check if ship can be placed based on the length
    if start_row + 1 > len(grid) or start_column + ship_length > len(grid[0]):
        print("Out of boundary, please try again")
        return False

    # Check if a ship is overlapping another ship
    for i in range(ship_length):
        if grid[start_row + 1][start_column + i] != ' ':
            print("Overlapping with another ship, please try again")
            return False
    return True


def place_ship(grid, built_ship, start_row, start_column):
    ship_length = len(built_ship)

    for i in range(ship_length):
        grid[start_row + 1][start_column + i] = built_ship[i]

    return grid


def print_game_board(grid):
    global GRID_SIZE

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            print(grid[i][j], end='\t')
        print()


def hit_or_miss(grid, missile_row, missile_column):
    if grid[missile_row + 1][missile_column] == ' ':
        print("MISS!!!!\n")
        time.sleep(2)
        return ' '
    elif grid[missile_row + 1][missile_column] != ' ':
        print("HIT!!!!\n")
        time.sleep(2)
        if grid[missile_row + 1][missile_column] == 'D':
            return 'D'
        elif grid[missile_row + 1][missile_column] == 'B':
            return 'B'
        elif grid[missile_row + 1][missile_column] == 'S':
            return 'S'
        elif grid[missile_row + 1][missile_column] == 'C':
            return 'C'
        elif grid[missile_row + 1][missile_column] == 'A':
            return 'A'
        elif grid[missile_row + 1][missile_column] == 'X':
            return 'X'
        else:
            return 'O'


if __name__ == '__main__':
    dict_ships = {"destroyer": ["D", "D"],
                  "battleship": ["B", "B", "B"],
                  "sub": ["S", "S", "S"],
                  "cruiser": ["C", "C", "C"],
                  "carrier": ["A", "A", "A", "A", "A"]
                  }

    game_intro(turn_num)
    grid = test_game_board()
    grid_player2 = game_board()
    # grid = game_board()
    # print()

    # Player 1 places ships on the board until there are no ships to place
    # while dict_ships:
    #     ship_placement_success = False
    #
    #     # Print dict of ships left to be placed for user reference
    #     for key, val in dict_ships.items():
    #         print(key, val)
    #
    #     # Get user input as to which ship they want to place.
    #     ship = get_ship(dict_ships)
    #     # Get list of characters to be placed on the board based on ship selection
    #     built_ship = dict_ships.get(ship)
    #
    #     start_row = ''
    #     while not 'A' <= start_row <= 'L':  # Ensure user input for start_row is on the grid
    #         try:
    #             start_row = input("What row would you like to place the ship (A - L)? ").upper()
    #             if not ('A' <= start_row.upper() <= 'L'):
    #                 print("Placement row must be between A and L.")
    #         except TypeError:
    #             print("Invalid input. Enter an alphabetic character between A and L.")
    #
    #     start_row = ord(start_row) - ord('A')
    #
    #     start_column = 0
    #     while not 1 <= start_column < 12:  # Ensure user input for start_column is on the grid
    #         try:
    #             start_column = int(input("What column would you like to place the ship (1 - 11)? "))
    #             if not (1 <= start_column < 12):
    #                 print("Placement column must be between 1 and 10. Allow for the length of the ship.")
    #         except TypeError:
    #             print("Invalid input. Enter a number between 1 and 10.")
    #
    #     ship_placement_success = validate_ship_location(grid, built_ship)
    #
    #     if ship_placement_success:
    #         grid = place_ship(grid, built_ship, start_row, start_column)
    #         dict_ships.pop(ship)
    #         print_game_board(grid)
    #         print()

    # First player's board is set
    print("*** Player 1's ship are in position ***")
    # Other player gets to send missile strikes at the ships
    print(".", end=' ')
    time.sleep(1)
    print(".", end=' ')
    time.sleep(1)
    print(".")
    time.sleep(3)
    print(f"Player 2 gets {turn_num} turns to sink all ships.")

    ships_afloat = {"destroyer": ["D", "D"],
                    "battleship": ["B", "B", "B"],
                    "sub": ["S", "S", "S"],
                    "cruiser": ["C", "C", "C"],
                    "carrier": ["A", "A", "A", "A", "A"]
                    }

    while turn_num > 0:
        print(f"Turn number {turn_num}\n")
        print("**Call in a missile strike**\n")
        print("Ships still floating:")
        # Print dict of ships left to be placed for user reference
        for key, val in ships_afloat.items():
            print(key, val)

        missile_row = ''
        while not 'A' <= missile_row <= 'L':  # Ensure user input for start_row is on the grid
            try:
                missile_row = input("\nEnter a row to strike (A - L). ").upper()
                if not ('A' <= missile_row.upper() <= 'L'):
                    print("Placement row must be between A and L")
            except TypeError:
                print("Invalid input. Enter an alphabetic character between A and L.")

        missile_row = ord(missile_row[0]) - ord('A')

        missile_column = 0
        while not 1 <= missile_column <= 12:  # Ensure user input for start_column is on the grid
            try:
                missile_column = int(input("Enter a column to strike (1 - 12)."))
                if not (1 <= missile_column <= 12):
                    print("Place column must be between 1 and 12")
            except TypeError:
                print("Invalid input. Enter a number between 1 and 12.")

        # Check for hit or miss and return the ship if hit or return 0 if miss
        hit_miss_result = hit_or_miss(grid, missile_row, missile_column)
        # Update game boards if there's a hit or miss
        ship_letters = ['D', 'B', 'S', 'C', 'A']
        if hit_miss_result in ship_letters:
            grid[missile_row + 1][missile_column] = 'X'
            grid_player2[missile_row + 1][missile_column] = 'X'
        elif hit_miss_result == ' ':
            grid[missile_row + 1][missile_column] = 'O'
            grid_player2[missile_row + 1][missile_column] = 'O'

        if hit_miss_result == 'D':
            ships_afloat['destroyer'].remove(hit_miss_result)
            if not ships_afloat.get('destroyer'):
                print("You sunk the destroyer!!!")
        elif hit_miss_result == 'B':
            ships_afloat['battleship'].remove(hit_miss_result)
            if not ships_afloat.get('battleship'):
                print("You sunk the battleship!!!")
        elif hit_miss_result == 'C':
            ships_afloat['cruiser'].remove(hit_miss_result)
            if not ships_afloat.get('cruiser'):
                print("You sunk the cruiser!!!")
        elif hit_miss_result == 'S':
            ships_afloat['sub'].remove(hit_miss_result)
            if not ships_afloat.get('sub'):
                print("You sunk the submarine!!!")
        elif hit_miss_result == 'A':
            ships_afloat['carrier'].remove(hit_miss_result)
            if not ships_afloat.get('carrier'):
                print("You sunk the carrier!!!")
        elif hit_miss_result == 'X' or hit_miss_result == 'O':
            print("You already called a strike on that location.")

        time.sleep(2)
        # Check if any ships are still floating
        if all(not value for value in ships_afloat.values()):
            print("Player 2 sunk all battleships! Congratulations player 2 wins!")
            print_game_board(grid)
            time.sleep(3)
            exit(0)
        print_game_board(grid_player2)
        turn_num -= 1

    print("Player 2 ran out of turns. Congratulations player 1 wins!")
    print_game_board(grid)
    print(f"Player 1 still has {ships_afloat}")
    time.sleep(3)
