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

test  = """233313312141413140212"""

# UNCOMMENT TO TEST
# data = test

if int(puzzle_id) == 1:
    parsed = []
    
    for i in range(int(len(data)/2+1)):
        
        for _ in range(int(data[2*i])):
            parsed.append(str(i)) 
        for _ in range(int(data[2*i+1])):
            parsed.append(None) 

    # print(parsed)

    i = 0
    while not all(parsed):
        if not parsed[i]:
            parsed[i] = parsed[-1]
            parsed = parsed[:-1]
        else:
            i += 1
        print(i)
        print(len(parsed))

    res = sum([i * int(p) for i, p in enumerate(parsed)]) 
    print(res)



if int(puzzle_id) == 2:
    parsed = []
    
    for i in range(int(len(data)/2+1)):
        
        parsed.append((int(data[2*i]), str(i))) 
        if 2*i + 1 < len(data):
            parsed.append((int(data[2*i+1]), None)) 

    # print(parsed)
    n = 0
    while True:
        i = 0
        while i < len(parsed):
            while parsed[i][1]:
                i += 1
                
            j = len(parsed) - 1
            
            while parsed[j][0] > parsed[i][0] or not parsed[j][1] and j >= 0:
                j -= 1
            
            if j <= i:
                i += 1
            else:
                break
        print(len(parsed))
        print(i)
        if i == len(parsed): break
        # print(parsed[i])
        # print(parsed[j])
        
        file = parsed[j]
        parsed[j] = (parsed[j][0], None)

        if parsed[i][0] - file[0] > 0:
            parsed[i] = (parsed[i][0] - file[0], None)
            parsed.insert(i, file)
        else:
            parsed[i] = file

        # print(parsed)
        
        # print()

    # parsed_text = ""
    # for p in parsed:
    #     if not p[1]:
    #         parsed_text += "." * p[0]
    #     else:
    #         parsed_text += p[1] * p[0]
            
    # print(parsed_text)
    res = 0
    count = 0
    for p in parsed:
        for _ in range(p[0]):
            
            if p[1]: res += count * int(p[1])
            count += 1


    print(res)

