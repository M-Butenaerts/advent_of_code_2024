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

test  = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

# UNCOMMENT TO TEST
# data = test

if int(puzzle_id) == 1: 
    grid = [[c for c in d] for d in data.split("\n")]
    regions = {}
    
    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         perimeter = 4
    #         if i > 0 and grid[i-1][j] == grid[i][j]: perimeter -= 1 
    #         if j > 0 and grid[i][j-1] == grid[i][j]: perimeter -= 1 
    #         if i < len(grid)-1 and grid[i+1][j] == grid[i][j]: perimeter -= 1 
    #         if j < len(grid[i])-1 and grid[i][j+1] == grid[i][j]: perimeter -= 1 
            
    #         if grid[i][j] in regions.keys():
    #             regions[grid[i][j]] = {"area": regions[grid[i][j]]["area"]+1, "perimeter": regions[grid[i][j]]["perimeter"]+perimeter}
    #         else:
    #             regions[grid[i][j]] = {"area": 1, "perimeter": perimeter} 
    res = 0

    while any([any(g) for g in grid]):

        flower_at = None
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    flower_at = (i, j)
                    break
            if flower_at: break
        
        flower = grid[flower_at[0]][flower_at[1]]
        patch = set([flower_at])
        visited = set([])
        area = 0
        perimeter = 0
        
        while len(patch) > 0:
            i, j = patch.pop()
            grid[i][j] = None
            visited.add((i, j))
            print((i, j))
            area += 1
            perimeter += 4
            
            if i > 0: 
                if (i-1, j) in visited or grid[i-1][j] == flower: perimeter -= 1
                if grid[i-1][j] == flower: patch.add((i-1, j))
            if j > 0: 
                if (i, j-1) in visited or grid[i][j-1] == flower: perimeter -= 1
                if grid[i][j-1] == flower: patch.add((i, j-1))

            if i < len(grid)-1: 
                print(grid[i+1])
                if (i+1, j) in visited or grid[i+1][j] == flower: perimeter -= 1
                if grid[i+1][j] == flower: patch.add((i+1, j))

            if j < len(grid[i])-1: 
                if (i, j+1) in visited or grid[i][j+1] == flower: perimeter -= 1
                if grid[i][j+1] == flower: patch.add((i, j+1))
            print(patch)
            print(perimeter)

        res += area * perimeter
        print(area)
        print(perimeter)
        for g in grid: print(g)
        print()


    print(res)

