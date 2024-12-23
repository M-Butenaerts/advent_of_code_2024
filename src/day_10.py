import sys

# SETUP

puzzle_id = None
filename = None

try:
        
    puzzle_id = sys.argv[1]
    filename = sys.argv[2]

except:
    print("invalid command. See documentation")
    exit()

data = None 


try:
    with open(filename, "r") as f:
        data = f.read()

except:

    print("file not found. See documentation")
    exit()

# SOLUTION

test  = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

# UNCOMMENT TO TEST
# data = test

if int(puzzle_id) == 1:
    def find_nines(coords, grid):
        nines = []
        coords_list = [(0, coords)]
        
        while len(coords_list) > 0:
            digit, c = coords_list.pop()
            x, y = c
            
            if digit == 9: nines.append((x, y))

            else:
                if x > 0 and grid[x-1][y] == digit + 1: coords_list.append((digit + 1, (x-1, y)))
                if y > 0 and grid[x][y-1] == digit + 1: coords_list.append((digit + 1, (x, y-1)))
                if x < len(grid) - 1 and grid[x + 1][y] == digit + 1: coords_list.append((digit + 1, (x+1, y)))
                if y < len(grid[x])-1 and grid[x][y+1] == digit + 1: coords_list.append((digit + 1, (x, y+1)))

        return nines
    

    grid = [[int(c) for c in d] for d in data.split("\n")]

    print(grid)
    zeros = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                zeros.append((i, j))

    print(zeros)
    res = 0
    for coords in zeros:
        res += len(set(find_nines(coords, grid)))

    print(res)
    
    

if int(puzzle_id) == 2:
    def find_paths(c_0, c_9, grid):
        
        coords_list = [(0, c_0)]
        nines = []
        while len(coords_list) > 0:
            digit, c = coords_list.pop()
            x, y = c
            
            if digit == 9: nines.append((x, y))

            else:
                if x > 0 and grid[x-1][y] == digit + 1: coords_list.append((digit + 1, (x-1, y)))
                if y > 0 and grid[x][y-1] == digit + 1: coords_list.append((digit + 1, (x, y-1)))
                if x < len(grid) - 1 and grid[x + 1][y] == digit + 1: coords_list.append((digit + 1, (x+1, y)))
                if y < len(grid[x])-1 and grid[x][y + 1] == digit + 1: coords_list.append((digit + 1, (x, y+1)))
            
        return nines.count(c_9)
    

    grid = [[int(c) for c in d] for d in data.split("\n")]

    print(grid)
    zeros = []
    nines = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                zeros.append((i, j))
            if grid[i][j] == 9:
                nines.append((i, j))
    print(zeros)
    print(nines)
    res = 0
    for i in range(len(zeros)):
        for j in range(len(nines)):
            res += find_paths(zeros[i], nines[j], grid)
            
            
    print(res)