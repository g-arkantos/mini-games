board=[[0,0,0,0,0,0,2,0,0],			#   j j j
       [0,8,0,0,0,7,0,9,0],			# i[a,b,c]
       [6,0,2,0,0,0,5,0,0],			# i[a,b,c]
       [0,7,0,0,6,0,0,0,0],			# i[a,b,c]
       [0,0,0,9,0,1,0,0,0],
       [0,0,0,0,2,0,0,4,0],
       [0,0,5,0,0,0,6,0,3],
       [0,9,0,4,0,0,0,7,0],
       [0,0,6,0,0,0,0,0,0]]

def print_board(bo):
	for i in range(len(bo)):
		if i%3==0 and i!=0:
			print('------------------------')
		for j in range(len(bo[0])):
			if j % 3 == 0 and j != 0:
				print(" | ", end="")

			if j == 8:
				print(bo[i][j])
			else:
				print(str(bo[i][j]) + " ", end="")

def find_empty(bo):				#This funtion will find the empty box(represented by 0)
	for i in range(len(bo)):
		for j in range(len(bo[0])):
			if bo[i][j]==0:
				return (i,j)
	return None			

def solve(bo):
	find=find_empty(bo)
	if not find:
		return True
	else:
		row,col=find

	for i in range(1,10):
		if valid(bo,i,(row,col)):
			bo[row][col]=i
			if solve(bo):
				return True
			bo[row][col]=0
	return False						
						#  j
def valid(bo,num,pos):	#i[a,a] 		note: --> pos [0,1]
	#check row
	for i in range(len(bo[0])):
		if (bo[pos[0]][i]==num and pos[1]!=i):
			return False
	#check col
	for j in range(len(bo)):
		if (bo[j][pos[1]]==num and pos[0]!=j):
			return False
	#check box:
	box_r=pos[0]//3	
	box_col=pos[1]//3
	for i in range(box_r*3, box_r*3+3):
		for j in range(box_col*3, box_col*3+3):
			if bo[i][j]==num and pos!=(i,j):
				return False
	return True				

print_board(board)
solve(board)
print("_______________________________")
print_board(board)