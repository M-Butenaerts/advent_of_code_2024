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

test  = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

# UNCOMMENT TO TEST
# data = test

if int(puzzle_id) ==  1: 
    rules = {}
    for r in data.split("\n\n")[0].split("\n"):
        
        if r.split("|")[0] in rules.keys():
            rules[r.split("|")[0]].append(r.split("|")[1])
        else:
            rules[r.split("|")[0]] = [r.split("|")[1]]
    sequences = [s.split(",") for s in data.split("\n\n")[1].split("\n")]
    
    res = 0
    
    for seq in sequences:
        valid = True
        for i in range(len(seq)):
            if valid:
                for j in range(i):
                    if seq[i] in rules.keys() and seq[j] in rules[seq[i]]:
                        valid = False
                        break 


        if valid:
            res += int(seq[int((len(seq)-1)/2)])

    print(res)


if int(puzzle_id) ==  2: 
    rules = {}
    for r in data.split("\n\n")[0].split("\n"):
        
        if r.split("|")[0] in rules.keys():
            rules[r.split("|")[0]].append(r.split("|")[1])
        else:
            rules[r.split("|")[0]] = [r.split("|")[1]]
    sequences = [s.split(",") for s in data.split("\n\n")[1].split("\n")]
    
    res = 0
    
    for seq in sequences:
        valid = True
        for i in range(len(seq)):
            if valid:
                for j in range(i):
                    if seq[i] in rules.keys() and seq[j] in rules[seq[i]]:
                        valid = False
                        break 

            
        if valid: pass
            # print(seq)
            # res += int(seq[int((len(seq)-1)/2)])
        
        else:
            ordered_list = []
            
            for s in seq:
                index = len(ordered_list)
                for i, o in enumerate(ordered_list): 
                    if s in rules.keys() and o in rules[s]:
                        index = i
                        break
                ordered_list.insert(index, s)
                
            res += int(ordered_list[int((len(ordered_list)-1)/2)])
                
    print(res)