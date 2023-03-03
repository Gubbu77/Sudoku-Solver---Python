grid = [[0, 6, 4, 0, 0, 8, 0, 0, 0],
        [5, 0, 0, 0, 9, 1, 6, 4, 8],
        [0, 0, 1, 6, 0, 5, 7, 0, 0],
        [0, 0, 0, 9, 3, 0, 0, 6, 0],
        [1, 4, 0, 5, 2, 0, 0, 0, 9],
        [0, 9, 0, 8, 1, 7, 5, 0, 0],
        [0, 0, 0, 4, 8, 2, 9, 0, 0],
        [4, 7, 8, 0, 5, 9, 0, 0, 0],
        [2, 5, 9, 7, 0, 3, 0, 0, 0]]

# main program to solve the sudoku
def solve(a):
    find = find_empty(a)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(a, i, (row, col)):
            a[row][col] = i

            if solve(a):
                return True
            a[row][col] = 0
    return False
# finding the valid row and column
def valid(a, num, pos):
    #check row
    for i in range(len(a[0])):
        if a[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(a)):
        if a[i][pos[1]] == num and pos[0] != i:
            return False
    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if a[i][j] == num and (i, j) != pos:
                return False
    return True

# making puzzle for better understanding
def puzzle(a):
    for i in range(len(a)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(a[0])):
            if j % 3 == 0 and j != 0 :
                print(" | ", end= " ")
            if j == 8 :
                print(a[i][j])
            else :
                print(str(a[i][j]) + " ", end="")

#  finding empty cells which have 0
def find_empty(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 0:
                return (i, j)
    return None

puzzle(grid)
solve(grid)
print(" ")
print("Solved -----------------------------------------------", "\n")
puzzle(grid)
