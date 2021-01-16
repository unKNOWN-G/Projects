# Project Tic Tac Toe

# Function to construct a matrix
def matrix_maker(number):
    for i in range(0, number):
        new = []
        for j in range(0, number):
            new.append(empty)
        matrix.append(new)
    for i in range(x, number, x + 1):
        for j in range(0, number):
            matrix[i][j] = "-"
            matrix[j][i] = "|"
    for i in range(x, number, x + 1):
        for j in range(x, number, x + 1):
            matrix[i][j] = "+"


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
def checker(position, row, col, player_name):
    if position % 2 == 0:
        if row_check(row) or col_check(col):
            print("Game over!")
            print(players[player_name], " Wins!")
            return 1
    else:
        if row_check(row) or col_check(col) or diagonal_check(row, col):
            print("Player ", player_name, " Wins!")
            return 1
    return 0


# Exceptional Handling
def exceptional_handling(player_name):
    check_input = input()
    if not check_input.isdigit():
        print("Enter a Valid Position Number")
        return exceptional_handling(player_name)
    check_input = int(check_input)
    if not (9 >= check_input >= 1):
        print("Please Enter an Index from 1-9")
        return exceptional_handling(player_name)

    return check_input


# Main Function
def tic_tac_toe():
    player_name = 'X'
    matrix_maker(n)
    flag = 0
    for i in range(9):
        # Input and Exceptional Handling
        print("Hey ", players[player_name], ", Its your turn. Enter your position ", end="")
        position = exceptional_handling(player_name)

        row, col = index_mapper(n, position - 1)

        if isempty(matrix[row][col]):
            matrix[row][col] = player_name
            print_matrix()
        else:
            print("Oops that's Occupied! ", players[player_name], " Try another empty space\n")
            i = i - 1
            continue

        if i >= 4 and checker(position, row, col, player_name):
            break

        player_name = next_player_name(player_name)
        if i == 8:
            flag = 1
    if flag:
        print("Tie!")
        print("Interesting game guys")


num = input("Enter Grid Spacing Level ")
while not num.isdigit():
    print("Please Enter a Number")
    num = input("Enter Grid Spacing Level ")

num = int(num)
x = 2 * num - 1
n = (x - 1) * 3 + 5

player_X = input("Hey! Who wanna Play X? X plays the First Turn :p")
player_O = input("So Who is choosing O?")
players = {'X': player_X, 'O': player_O}

empty = " "
matrix = []

tic_tac_toe()
