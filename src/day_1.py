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

test  = """3   4
4   3
2   5
1   3
3   9
3   3"""

# UNCOMMENT TO TEST
# data = test

if int(puzzle_id) == 1:
    
    left = []
    right = []
    
    for line in data.split("\n"):
        
    
        left.append(int(line.split("   ")[0]))
        right.append(int(line.split("   ")[1]))

    left.sort()
    right.sort()

    res = sum([abs(left[i] - right[i]) for i in range(len(left))])
    print(res)


if int(puzzle_id) == 2:
    left = []
    right = []
    
    for line in data.split("\n"):
        
    
        left.append(int(line.split("   ")[0]))
        right.append(int(line.split("   ")[1]))
    
    res = 0
    for l in left:
        res += l * len([r for r in right if r == l])

    print(res)