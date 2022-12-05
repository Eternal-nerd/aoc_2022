


def main():
    with open("input.txt") as f:
        lines = f.readlines()
    
    currentmax = 0
    count = 0
    maxlist = []
    sumlist = []
    for num in lines:
        num = num.strip()
        if (num != ''):
            count+=int(num)
        else:
            sumlist+=[count]
            if (count > currentmax):
                currentmax=count
                #print(f"CURRENTMAX: {currentmax}")
                maxlist += [currentmax]
            count = 0

    maxlist = maxlist[-3:]

    sumlist.sort()

    top3 = sumlist[-3:]

    

    print(f"top: {sum(top3)}")

    #print(f"MAXLIST: {maxlist}, SUM: {sum(maxlist)}")

    #print(f"FINAL MAX: {currentmax}")
        



if __name__ == "__main__":
    main()