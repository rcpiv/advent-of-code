# Part 1
dic = {'A': 1,'B': 2,'C': 3, 'X': 1, 'Y': 2, 'Z' : 3}
r = []
with open("adventofcode\\advent-of-code\\2022\\input_files\\day2.txt", 'r') as f:
    data = f.read().split('\n')
    for i in data:
        mine = i.split()[1]
        yours = i.split()[0]
        
        if mine == 'Z' and yours == 'A':
            result = dic[mine]
        elif mine == 'X' and yours == 'C':
            result = dic[mine] + 6
        else:
            if dic[mine] < dic[yours]: # Loss
                result = dic[mine]
            elif dic[mine] > dic[yours]: # Win
                result = dic[mine] + 6
            else:
                result = dic[mine] + 3
        
        r.append(result)

print(sum(r))

# Part 2
dic2 = {'A': 1,'B': 2,'C': 3, 'X': 1, 'Y': 3, 'Z' : 6}
l = ['A','B','C']
r = 0
with open("adventofcode\\advent-of-code\\2022\\input_files\\day2.txt", 'r') as f:
    data = f.read().split('\n') 
    for i in data:
        result = i.split()[1]
        yours = i.split()[0]
        
        if result == 'Y': # Draw
            mine = dic2[yours]
            r += (mine + 3)
        elif result == 'X': # Loss
            mine = dic2[l[l.index(yours) - 1]]
            r += mine
        else: # Win
            if yours == 'C':
                mine = dic2['A']
            else:
                mine =  dic2[l[l.index(yours) +  1]]
            r += (mine + 6)

print(r)