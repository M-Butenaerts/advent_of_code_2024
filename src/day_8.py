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

test  = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

# UNCOMMENT TO TEST
# data = test

if int(puzzle_id) ==  1: 

    grid = [[c for c in d] for d in data.split("\n")]

    antennas = {}

    for i, g in enumerate(grid):
        for j, a in enumerate(g):
            if a != ".":
                if a not in antennas.keys():
                    antennas[a] = [(i, j)]

                else:
                    antennas[a].append((i, j)) 

    print(antennas)

    blocks = []
    
    for a in antennas:
        for i in range(len(antennas[a])):
            for j in range(len(antennas[a])):
                if j != i:
                    coords_1 = antennas[a][i]
                    coords_2 = antennas[a][j]

                    blocks.append((coords_2[0] + (coords_2[0] - coords_1[0]), coords_2[1] + (coords_2[1] - coords_1[1])))
    
    blocks = [c for c in blocks if c[0] >= 0 and c[0] < len(grid) and c[1] >= 0 and c[1] < len(grid[0]) ]
    print(blocks)
    print(len(set(blocks)))

    for b in blocks: grid[b[0]][b[1]] = "#"

    for g in grid: print(g)
    
    
    
    
if int(puzzle_id) ==  2: 

    grid = [[c for c in d] for d in data.split("\n")]

    antennas = {}

    for i, g in enumerate(grid):
        for j, a in enumerate(g):
            if a != ".":
                if a not in antennas.keys():
                    antennas[a] = [(i, j)]

                else:
                    antennas[a].append((i, j)) 

    print(antennas)

    blocks = []
    
    for a in antennas:
        for i in range(len(antennas[a])):
            for j in range(len(antennas[a])):
                if j != i:
                    coords_1 = antennas[a][i]
                    coords_2 = antennas[a][j]
                    
                    dif = (coords_2[0] - coords_1[0], coords_2[1] - coords_1[1])
                    c = (coords_2[0] + dif[0], coords_2[1] + dif[1])
                    
                    while c[0] >= 0 and c[0] < len(grid) and c[1] >= 0 and c[1] < len(grid[0]):
                        blocks.append(c)
                        c = (c[0] + dif[0], c[1] + dif[1])
                        print(c)

    for a in [a for a in antennas.keys() if len(antennas[a]) >  1]: 
        for b in antennas[a]:
            
            blocks.append(b)
    
    print(blocks)
    
    print(len(set(blocks)))

    for b in blocks: 
        grid[b[0]][b[1]] = "#"

    for g in grid: print(g)