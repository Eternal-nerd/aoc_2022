
import re

def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    
    cargo = lines[:8] #7 lines
    nums = lines[8]
    lines = lines[10:]
    #cargo = [list(i) for i in cargo]
    #print(cargo[0])
    #print(f"ind: {cargo[0].index('B')}")
    
    valdict = {}
    for i in range(1,10):
        valdict[nums.index(str(i))] = i
    #print(valdict)

    master = {}
    for j in range(1,10):
        master[j] = []

    for row in reversed(cargo):
        dict = {}
        res = re.findall(r'[A-Z]', row)
        res = set(res)
        for i in res:
            for indx, val in enumerate(row):
                if val == i:
                    if i not in dict.keys():
                        dict[i] = [indx]
                    else:
                        dict[i] = dict[i]+[indx]
        
        for key in dict.keys():
            for index in dict[key]:
                mainind = valdict[index]
                master[mainind] = master[mainind] + [key]

    for line in lines:
        line = line.split()
        amt = line[1]
        src = line[3]
        dst = line[5]
        temp = []

        for n in range(int(amt)):
            temp = temp + [master[int(src)].pop()]
            #print(f"before: src: {master[int(src)]},  dst:  {master[int(dst)]}")
            #master[int(dst)] = master[int(dst)] + [(master[int(src)].pop())]
            #print(f"aftser: src: {master[int(src)]},  dst:  {master[int(dst)]}")

        
        for k in reversed(temp):
            master[int(dst)] = master[int(dst)] + [k]


    temp1 = []
    for key1 in master.keys():
        temp1 += [master[key1][-1]]

    print(''.join(temp1))



if __name__ == "__main__":
    main()