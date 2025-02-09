import sys
import copy
import time
# Running script: given code can be run with the command:
# python file.py, ./path/to/init_state.txt ./output/output.txt
class Sudoku(object):
	def __init__(self, puzzle):
		# you may add more attributes if you need
		self.puzzle = puzzle # self.puzzle is a list of lists
		self.ans = copy.deepcopy(puzzle) # self.ans is a list of lists
		
	def find_empty_pos(self, list):
		for i in range(9):
			for j in range(9):
				if self.puzzle[i][j] == 0:
					list[0] = i
					list[1] = j
					return True
		return False
					

	def check_col(self, number, col):
		for i in range(9):
			if self.puzzle[i][col] == number:
				return False
		return True
	
	def check_row(self, number, row):
		for i in range(9):
			if self.puzzle[row][i] == number:
				return False
		return True
	
	def check_square(self, number, row, col):
		row_start = row - row % 3
		col_start = col - col % 3
		
		for i in range(3):
			for j in range(3):
				if self.puzzle[row_start + i][col_start + j] == number:
					return False
		return True

	
	def check_validation(self, number, row, col):
		return self.check_col(number, col) and self.check_row(number, row) and self.check_square(number, row, col)


	def find_solution(self):
		list = [0,0]
		if self.find_empty_pos(list) is False:
			#no more empty space
			return True
			
		row = list[0]
		col = list[1]
		
		for number in range(1,10):
			#print(number)
			if self.check_validation(number, row, col):
				#print('success')
				self.puzzle[row][col] = number

				if self.find_solution():
					return True

			self.puzzle[row][col] = 0
		
		#print('backtrack')
		return False

	def solve(self):
		# TODO: Write your code here
		start = time.time()
		self.find_solution()
		end = time.time()
		print(end - start)
		self.ans = copy.deepcopy(puzzle)
		# self.ans is a list of lists
		
		return self.ans

	# you may add more classes/functions if you think is useful
	# However, ensure all the classes/functions are in this file ONLY
	# Note that our evaluation scripts only call the solve method.
	# Any other methods that you write should be used within the solve() method.

if __name__ == "__main__":
	# STRICTLY do NOT modify the code in the main function here
	if len(sys.argv) != 3:
		print ("\nUsage: python CS3243_P2_Sudoku_XX.py input.txt output.txt\n")
		raise ValueError("Wrong number of arguments!")

	try:
		f = open(sys.argv[1], 'r')
	except IOError:
		print ("\nUsage: python CS3243_P2_Sudoku_XX.py input.txt output.txt\n")
		raise IOError("Input file not found!")

	puzzle = [[0 for i in range(9)] for j in range(9)]
	lines = f.readlines()

	i, j = 0, 0
	for line in lines:
		for number in line:
			if '0' <= number <= '9':
				puzzle[i][j] = int(number)
				j += 1
				if j == 9:
					i += 1
					j = 0

	sudoku = Sudoku(puzzle)
	ans = sudoku.solve()

	with open(sys.argv[2], 'a') as f:
		for i in range(9):
			for j in range(9):
				f.write(str(ans[i][j]) + " ")
			f.write("\n")
