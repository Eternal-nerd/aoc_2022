

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    dict = {'win':0,'tie':0,'lose':0}

    total1=0
    for line in lines:

        spl = line.split()

        if spl[1]=='X':
            #print('lose')
            dict['lose'] = dict['lose']+1
            total1+=0

            if spl[0]=='A':
                total1+=3
            if spl[0]=='B':
                total1+=1
            if spl[0]=='C':
                total1+=2

        if spl[1]=='Y':
            #print('tie')
            dict['tie'] = dict['tie']+1
            total1+=3

            if spl[0]=='A':
                total1+=1
            if spl[0]=='B':
                total1+=2
            if spl[0]=='C':
                total1+=3

        if spl[1]=='Z':
            #print('win')
            dict['win'] = dict['win']+1
            total1+=6

            if spl[0]=='A':
                total1+=2
            if spl[0]=='B':
                total1+=3
            if spl[0]=='C':
                total1+=1

    print(total1)
    print(dict)

if __name__ == "__main__":
    main()