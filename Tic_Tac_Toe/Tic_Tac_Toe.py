# Project Tic Tac Toe

#Function to construct a matrix
def matrix_maker(n,matrix):
	for i in range(0,n):
		 new=[]
		 for j in range(0,n):
		        new.append(empty)
		 matrix.append(new)  
	for i in range(x,n,x+1):
	             for j in range(0,n):
	             	matrix[i][j]="-"
	             	matrix[j][i]="|"
	for i in range (x,n,x+1):
	               for j in range(x,n,x+1):
	               	matrix[i][j]="+"
	               	
#Funtion to map Index
def index_mapper(n,pos):
	a=[int(n/6),int(n/2),int((5*n)/6)]
	index_1=int(pos/3)
	index_2=pos%3
	return a[index_1],a[index_2]

#Function to Print Matrix	
def print_matrix():
    for x in range (0,n):
        for y in range(0,n):
        	print(matrix[x][y], end =" ")
        print()		 

#Function to change Player
def next_player_name(player_name):
	if(player_name=='X'):
		return 'O'
	else:
		return 'X'

#Function to tell if a block is empty
def isempty(a):
	return a==empty

#Function to tell if a block is not empty	
def isnonempty(a):
	return not isempty(a)

#Function to check equality
def equality_checker(a,b,c):
	flag=isnonempty(a) and isnonempty(b) and isnonempty(c)
	return flag and a==c and a==b
	
#Function to tell if row elements are same
def row_check(x):
	col_index=[int(n/6),int(n/2),int((5*n)/6)]
	return equality_checker(matrix[x][col_index[0]],  matrix[x][col_index[1]], matrix[x][col_index[2]])

#Function to tell if column elements are same
def col_check(y):
	row_index=[int(n/6),int(n/2),int((5*n)/6)]
	return equality_checker(matrix[row_index[0]][y],matrix[row_index[1]][y],matrix[row_index[2]][y])
	
#Function to check if diagonals are same
def diagonal_check(a,b):
	index=[int(n/6),int(n/2),int((5*n)/6)]
	if(a==b):
		return equality_checker(matrix[index[0]][index[0]],matrix[index[1]][index[1]],matrix[index[2]][index[2]])
	else:
		return equality_checker(matrix[index[2]][index[0]],matrix[index[1]][index[1]],matrix[index[0]][index[2]])

#Function to check if someone has won
def checker(position,row,col,player_name):
	if(position%2==0):
				if(row_check(row) or col_check(col)):
					print("Game over!")
					print("Player ",player_name," Wins!")
					return 1
	else:
				if(row_check(row)or col_check(col) or diagonal_check(row,col)):
					print("Player ",player_name," Wins!")
					return 1
	return 0
					
#Main Function
def tic_tac_toe():
	player_name='X'
	matrix_maker(n,matrix)
	i=0
	flag=0
	for i in range(9):
		
		print("Hey ",player_name,", Its your turn. Enter your position ",end="")
		position=int(input())
		row,col=index_mapper(n,position-1)
		
		if(isempty(matrix[row][col])):
			matrix[row][col]=player_name
			print_matrix()				
		else:
			print("Oops that's Occupied! ",player_name," Try another empty space\n")
			i=i-1
			continue
			
		if(i>=4 and checker(position,row,col,player_name)):
			break
			
		player_name=next_player_name(player_name)
		if(i==8):
			flag=1
	if(flag):
		print("Tie!")
		print("Intresting game guys")	
		
num=int(input("Enter Grid Spacing Level "))
print()
x=2*num-1
n=(x-1)*3+5
empty=" "
matrix=[]

tic_tac_toe()