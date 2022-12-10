

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    line = [x for x in lines[0]]

    que = []
    index = 0
    for i in line:
        print(f"Current que: {que},  index = {index}, i={i}")

        if (len(que) < 14):
            que.append(i)
        
        else:
        
            if (i in que):
                que.pop(0)
                que.append(i)
            else:
                if (len(set(que)) == len(que)):
                    print(index)
                    return(0)
                else:
                    que.pop(0)
                    que.append(i)


        index+=1





if __name__ == "__main__":
    main()