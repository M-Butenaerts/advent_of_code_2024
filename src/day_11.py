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

test  = """2 77706 5847 9258441 0 741 883933 12"""

# UNCOMMENT TO TEST
data = test

if int(puzzle_id) == 1:

    stones = [int(d) for d in data.split(" ")]
    print(stones)

    for i in range(25):
        print(i)
        new_stones = []

        for stone in stones:
            if stone == 0: new_stones.append(1)
            elif len(str(stone)) % 2 == 0: 
                new_stones.append(int(str(stone)[:int(len(str(stone))/2)]))
                new_stones.append(int(str(stone)[int(len(str(stone))/2):]))
        
            else: new_stones.append(stone*2024) 
        # print(new_stones)
        stones = new_stones
        
    print(len(stones))


if int(puzzle_id) == 2:
    pass            
    