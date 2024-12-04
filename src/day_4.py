import sys

import numpy as np

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

test  = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

# UNCOMMENT TO TEST
# data = test

if int(puzzle_id) ==  1:
    res = 0
    grid = [[c for c in d] for d in data.split("\n")]
    # print(grid)

    # vertical
    verticals = ["".join(g) for g in grid]
    for v in verticals:
        res += v.count("XMAS") + v.count("SAMX")
    
    print(res)
    horizontal = ["".join(g) for g in np.transpose(grid)]
    for h in horizontal:
        res += h.count("XMAS") + h.count("SAMX")
    
    print(res)
    
    crossed = [[] for _ in range(len(grid) + len(grid[0]))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            crossed[i+j].append(grid[i][j])
    
    for c in ["".join(c) for c in crossed]:
        res += c.count("XMAS") + c.count("SAMX")
    print(res)
    # for c in crossed: print(c)

    crossed = [[] for _ in range(len(grid) + len(grid[0])-1)]
    
    for i in range(len(grid)):
        for j in range(len(grid[len(grid)-i-1])):
            crossed[i+j].append(grid[len(grid)-i-1][j])
    
    for c in ["".join(c) for c in crossed]:
        res += c.count("XMAS") + c.count("SAMX")

    # for c in crossed: print(c)
    print(res)


if int(puzzle_id) ==  2:
    res = 0
    grid = [[c for c in d] for d in data.split("\n")]
    # print(grid)

    for I in range(len(grid)-2):
        for J in range(len(grid[0])-2):
            i = I + 1
            j = J + 1
            if grid[i][j] == "A":
                if (grid[i-1][j-1] == "M" and grid[i+1][j+1] == "S") or (grid[i-1][j-1] == "S" and grid[i+1][j+1] == "M"):
                    if (grid[i-1][j+1] == "M" and grid[i+1][j-1] == "S") or (grid[i-1][j+1] == "S" and grid[i+1][j-1] == "M"):
                        res += 1
                
     
    print(res)