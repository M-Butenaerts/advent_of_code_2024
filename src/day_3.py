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

test  = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+don'tmul(32,64](mul(11,8)undo()?mul(8,5))"""

# UNCOMMENT TO TEST
# data = test

if int(puzzle_id) ==  1:
    res = 0
    
    for d in data.split("mul(")[1:]:
        if len(d.split(",")) > 1:
            i_1 = d.split(",")[0]
            i_2 = d.split(",")[1].split(")")[0]
            if i_2.isnumeric() and i_1.isnumeric() and len(i_1) < 4 and len(i_2) < 4 and " " not in i_1 and " " not in i_2 and f"mul({i_1},{i_2})" in data:
                res += int(i_2) * int(i_1)
                
    print(res)

if int(puzzle_id) == 2:
    res = 0
    
    filtered_data = ""
    for i, d in enumerate(data.split("don't()")):
        if i == 0:
            filtered_data += d
        elif "do()" in d:
                filtered_data += "".join(d.split("do()")[1:])

    print(filtered_data)
    for d in filtered_data.split("mul(")[1:]:
        if len(d.split(",")) > 1:
            i_1 = d.split(",")[0]
            i_2 = d.split(",")[1].split(")")[0]
            if i_2.isnumeric() and i_1.isnumeric() and len(i_1) < 4 and len(i_2) < 4 and " " not in i_1 and " " not in i_2 and f"mul({i_1},{i_2})" in filtered_data:
                res += int(i_2) * int(i_1)
                
    print(res)