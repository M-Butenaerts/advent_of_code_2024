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

test  = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

# UNCOMMENT TO TEST
# data = test

if int(puzzle_id) ==  1: 
    res = 0
    def solve(eq, els):
        if eq < 0: return False
        if len(els) == 0:
            return eq == 0
        else:
            return solve(eq - els[-1], els[:-1]) or (eq % els[-1] == 0 and solve(eq / els[-1], els[:-1]))

    equations = [(int(d.split(": ")[0]), [int(i) for i in d.split(": ")[1].split(" ")]) for d in data.split("\n")]
    
    for eq, els in equations:
        print(els)
        if solve(eq, els): 
            res += eq 
    print(res)

if int(puzzle_id) ==  2: 
    res = 0
    def solve(eq, els):
        # print(eq)
        # print(els)
        if eq < 0: return False
        if len(els) == 0:
            return eq == 0
        else:
            return solve(eq - els[-1], els[:-1]) or (eq % els[-1] == 0 and solve(int(eq / els[-1]), els[:-1])) or ( str(eq)[-len(str(els[-1])):] == str(els[-1]) and solve(int(str(eq)[:-len(str(els[-1]))]), els[:-1]) )

    equations = [(int(d.split(": ")[0]), [int(i) for i in d.split(": ")[1].split(" ")]) for d in data.split("\n")]
    
    for eq, els in equations:
        if solve(eq, els): 
            res += eq 

    print(res)