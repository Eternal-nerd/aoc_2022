
def get_prio(str):
    if (str.isupper()):
        return(ord(str)-38)
    else:
        return(ord(str)-96)

def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    

    threes = [lines[x:x+3] for x in range(0, len(lines), 3)]

    total=0
    for line in threes:
        o1 = set(line[0])
        o2 = set(line[1])
        o3 = set(line[2])

        inter1 = o1.intersection(o2)
        inter2 = inter1.intersection(o3)

        total+=get_prio(list(inter2)[0])


        '''mid = int(len(line)/2)
        one = line[:mid]
        two = line[mid:]


        inter = list(set(one).intersection(two))[0]
        total += get_prio(inter)'''



    print(total)

    #print(get_prio("L"))

    

if __name__ == "__main__":
    main()