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

test  = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

# UNCOMMENT TO TEST
# data = test

def check_distances(digits):
        print(digits)
        for i in range(len(digits)-1):
            dif = abs(digits[i] - digits[i+1])
            if dif > 3 or dif < 1: return False 
        return True

if int(puzzle_id) ==  1:

    res = 0
    for line in data.split("\n"):
        digits = [int(l) for l in line.split(" ")]
        
        if digits == sorted(digits) or digits == sorted(digits, reverse=True): 
            if check_distances(digits): res += 1
        
    print(res)
    
if int(puzzle_id) == 2:
    
    res = 0
    for line in data.split("\n"):
        digits = [int(l) for l in line.split(" ")]
        all_digits = [digits]
        for i in range(len(digits)):
            all_digits.append([digits[j] for j in range(len(digits)) if i != j])

        for d in all_digits:
            if d == sorted(d) or d == sorted(d, reverse=True): 
                if check_distances(d): 
                    res += 1
                    break
    print(res)
