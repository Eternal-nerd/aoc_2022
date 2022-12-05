
def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    
    total = 0
    for line in lines:
        spl = line.split(',')
        o1 = spl[0].split('-')
        o2 = spl[1].split('-')

        o1set = set(range(int(o1[0]),(int(o1[1])+1)))
        o2set = set(range(int(o2[0]),(int(o2[1])+1)))
        
        #issubset() for part 1
        if (len(o1set.intersection(o2set)) != 0) or (len(o2set.intersection(o1set)) != 0):
            total+=1

    print(total)

if __name__ == "__main__":
    main()