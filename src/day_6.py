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

test  = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

# UNCOMMENT TO TEST
data = test

if int(puzzle_id) ==  1:
    def flip(grid):
        new_grid = [[] for g in grid[0]]
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                new_grid[len(new_grid) - j - 1].append(grid[i][j])
    
        return new_grid
    
    grid = [[c for c in d] for d in data.split("\n")]
    
    for g in grid: print(g) 
    print() 
    # for g in flip(grid): print(g) 
    
    # exit()
    res = 0
    coords = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                
                coords = (i, j)
    while True:

        blocked = None
        for i in range(coords[0]):
            if grid[i][coords[1]] == "#":
                blocked = (i, coords[1])
        # print(blocked)
        if blocked:
            for i in range(coords[0] - blocked[0]):
                grid[i+blocked[0]+1][coords[1]] = "X"
            # grid[coords[0]][coords[1]] = str(res)
            # res += coords[0] - blocked[0]
            coords = (len(grid[0]) - blocked[1] -1, blocked[0] + 1)
            # print(coords)
            
            grid = flip(grid)
            # grid[coords[0]][coords[1]] = "^"
            # for g in grid: print(g)
        else:   
            for i in range(coords[0] + 1):
                grid[i][coords[1]] = "X"        
            break
        
        t = "".join(["".join(g) for g in grid])
        print(t.count("X"))

    # grid = flip(grid)    
    # grid = flip(grid)
    
    # for g in grid: print(g)    
    t = "".join(["".join(g) for g in grid])
    print(t.count("X"))


if int(puzzle_id) ==  2:
    def flip(grid):
        new_grid = [[] for g in grid[0]]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                x = grid[i][j]
                if x == "^": x = "<"
                elif x == "<": x = "v"
                elif x == "v": x = ">"
                elif x == ">": x = "^"

                new_grid[len(new_grid) - j - 1].append(x)
    
        return new_grid
    
    def has_loop(grid):
        
        res = 0
        coords = None
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "^":
                    
                    coords = (i, j)

        for g in grid: print(g)
        print()
        while True:

            blocked = None
            for i in range(coords[0]):
                if grid[i][coords[1]] == "#":
                    blocked = (i, coords[1])
            # print(blocked)
            if blocked:
                for i in range(coords[0] - blocked[0]):
                    if grid[i+blocked[0]+1][coords[1]] == "^": return True 
                    grid[i+blocked[0]+1][coords[1]] = "^"
                
                coords = (len(grid[0]) - blocked[1] -1, blocked[0] + 1)
                # print(coords)
                
                grid = flip(grid)
                # grid[coords[0]][coords[1]] = "^"
                # for g in grid: print(g)
            else:   
                for i in range(coords[0] + 1):
                    grid[i][coords[1]] = "^"        
                return False    
    
    grid = [[c for c in d] for d in data.split("\n")]
    grid_copy = [[c for c in d] for d in data.split("\n")]
    
    res = 0
    coords = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                
                coords = (i, j)
    while True:

        blocked = None
        for i in range(coords[0]):
            if grid[i][coords[1]] == "#":
                blocked = (i, coords[1])
        # print(blocked)
        if blocked:
            for i in range(coords[0] - blocked[0]):
                grid[i+blocked[0]+1][coords[1]] = "^"
                if has_loop([[grid_copy[j][k] if (j, k) != (i+blocked[0]+2, coords[1]) else "#" for k in range(len(grid_copy[j]))] for j in range(len(grid_copy))]): res += 1
            # res += coords[0] - blocked[0]
            coords = (len(grid[0]) - blocked[1] -1, blocked[0] + 1)
            # print(coords)
            
            grid = flip(grid)
            grid[coords[0]][coords[1]] = "^"
            for g in grid: print(g)
        else:   
            for i in range(coords[0] + 1):
                grid[i][coords[1]] = "^"        
            break
    
    grid = flip(grid)
    grid = flip(grid)
    print()
    for g in grid: print(g)

    print(res)

