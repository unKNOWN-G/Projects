# Project Tic Tac Toe

# Function to construct a matrix
def matrix_maker(number):
    for a in range(0, number):
        new = []
        for b in range(0, number):
            new.append(empty)
        matrix.append(new)
    for a in range(x, number, x + 1):
        for b in range(0, number):
            matrix[a][b] = "-"
            matrix[b][a] = "|"
    for a in range(x, number, x + 1):
        for b in range(x, number, x + 1):
            matrix[a][b] = "+"


# Function to map Index
def index_mapper(number, pos):
    a = [int(number / 6), int(number / 2), int((5 * number) / 6)]
    index_1 = int(pos / 3)
    index_2 = pos % 3
    return a[index_1], a[index_2]


# Function to Print Matrix
def print_matrix():
    for a in range(0, n):
        for b in range(0, n):
            print(matrix[a][b], end=" ")
        print()


# Function to change Player
def next_player_name(player_name):
    if player_name == 'X':
        return 'O'
    else:
        return 'X'


# Function to tell if a block is empty
def isempty(a):
    return a == empty


# Function to tell if a block is not empty
def isnonempty(a):
    return not isempty(a)


# Function to check equality
def equality_checker(a, b, c):
    flag = isnonempty(a) and isnonempty(b) and isnonempty(c)
    return flag and a == c and a == b


# Function to tell if row elements are same
def row_check(row_num):
    col_index = [int(n / 6), int(n / 2), int((5 * n) / 6)]
    return equality_checker(matrix[row_num][col_index[0]], matrix[row_num][col_index[1]], matrix[row_num][col_index[2]])


# Function to tell if column elements are same
def col_check(y):
    row_index = [int(n / 6), int(n / 2), int((5 * n) / 6)]
    return equality_checker(matrix[row_index[0]][y], matrix[row_index[1]][y], matrix[row_index[2]][y])


# Function to check if diagonals are same
def diagonal_check(a, b):
    index = [int(n / 6), int(n / 2), int((5 * n) / 6)]
    if a == b:
        return equality_checker(matrix[index[0]][index[0]], matrix[index[1]][index[1]], matrix[index[2]][index[2]])
    else:
        return equality_checker(matrix[index[2]][index[0]], matrix[index[1]][index[1]], matrix[index[0]][index[2]])


# Function to check if someone has won
def checker(position, row, col, player_name, players):
    if position % 2 == 0:
        if row_check(row) or col_check(col):
            print("Game over!")
            print(players[player_name], " Wins!")
            scores[players[player_name]] += 1
            return 1
    else:
        if row_check(row) or col_check(col) or diagonal_check(row, col):
            print(players[player_name], " Wins!")
            scores[players[player_name]] += 1
            return 1
    return 0


# Input Number Exceptional Handling

def input_number_exceptional_handling(num_input):
    while not num_input.isdigit():
        print("Please Enter a Number")
        num_input = input()
    return int(num_input)


# Exceptional Handling
def exceptional_handling(player_name):
    check_input = input()
    check_input = input_number_exceptional_handling(check_input)
    if not (9 >= check_input >= 1):
        print("Please Enter an Index from 1-9")
        return exceptional_handling(player_name)

    return check_input


# Main Function
def tic_tac_toe(player_a, player_b):
    player_1_name = input("\nHey! Who wanna Play X?")
    while not (player_1_name == player_a or player_1_name == player_b):
        player_1_name = input("Please Enter the Player Name")
    if player_1_name == player_a:
        player_a = player_1_name
        player_b = player_b
    else:
        player_b = player_a
        player_a = player_1_name
    players = {'X': player_a, 'O': player_b}
    player_name = 'X'
    matrix_maker(n)
    flag = 0
    turn = 0
    while turn < 9:
        # Input and Exceptional Handling
        print("Hey ", players[player_name], ", Its your turn. Enter your position ", end="")
        position = exceptional_handling(player_name)

        row, col = index_mapper(n, position - 1)

        if isempty(matrix[row][col]):
            matrix[row][col] = player_name
            print_matrix()
        else:
            print("Oops that's Occupied ", players[player_name], "! Try another empty space\n")
            continue

        if turn >= 4 and checker(position, row, col, player_name, players):
            break

        player_name = next_player_name(player_name)
        if turn == 8:
            flag = 1
        turn = turn + 1
    if flag:
        print("Tie!")
        print("Interesting game guys")


num = input("Enter Grid Spacing Level ")
num = input_number_exceptional_handling(num)

num = int(num)
x = 2 * num - 1
n = (x - 1) * 3 + 5

player_1 = input("\nEnter the name of Player 1 ")
player_2 = input("Enter the name of Player 2 ")

scores = {player_1: 0, player_2: 0}

number_of_games = input("How many Games do you want to Play? ")
number_of_games = input_number_exceptional_handling(number_of_games)

for i in range(number_of_games):
    empty = " "
    matrix = []
    tic_tac_toe(player_1, player_2)
if scores[player_1] == scores[player_2]:
    print("Match ended and its a Tie!\n\tGreat Competitors")
else:
    print(player_1 if (scores[player_1] > scores[player_2]) else player_2, "Wins the total Game!")
