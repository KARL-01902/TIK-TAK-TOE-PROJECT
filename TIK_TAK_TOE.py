import random

def rand(): # generates any random number bwn 1-9
    return random.randint(1, 9)

def print_board(List):
    i = 0
    while(i < 9):
        for j in range(i,i+3):
            if(j!=i+2):
                if(List[j] == '\0'):
                    print("   |",end ="")
                else:
                    print(" "+List[j]+" |",end ="")
            else:
                if(List[j] == '\0') :
                    print("   ",end ="")
                else:
                    print(" "+List[j]+" ",end ="")
        print("")
        if(i!=6):
            print("---|---|---")
        i+=3
    print("")

def wincheck(v):
    i = 0
    while(i<9):
        if((v[0+i] == 'X' and v[1+i] == 'X' and v[2+i] == 'X') or (v[0+i] == 'O' and v[1+i] == 'O' and v[2+i] == 'O')):
           return True
        else:
            i+=3
    i = 0
    while(i<3):
        if((v[0+i] == 'X' and v[3+i] == 'X' and v[6+i] == 'X') or (v[0+i] == 'O' and v[3+i] == 'O' and v[6+i] == 'O')):
            return True
        else:
            i+=1
    if((v[0] == 'X' and v[4] == 'X' and v[8] == 'X') or (v[0] == 'O' and v[4] == 'O' and v[8] == 'O')):
        return True
    if((v[2] == 'X' and v[4] == 'X' and v[6] == 'X') or (v[2] == 'O' and v[4] == 'O' and v[6] == 'O')):
        return True
    return False

def main():
    List = ['\0','\0','\0','\0','\0','\0','\0','\0','\0']
    x = 0;
    flag1 = False;
    flag2 = True;
    while(x<9):
        if(flag2 == True):  # player 1
            print_board(List)
            x+=1
            pos = 10
            while(pos<1 or pos>9 or List[pos-1] != '\0'):
                try:
                    pos = int(input("Player please enter valid position of O between (1-9) : "))
                except:
                    print("NO INPUT, input again")
            List[pos-1] = 'O'
            if(wincheck(List)):
                print_board(List)
                print("Player wins!!", end ="")
                flag1 = True
                break
            else:
                flag2 = False

        else:   # player 2 @ computer
            print_board(List)
            x+=1
            pos = int(rand())
            while(List[pos-1] != '\0'):
                pos = int(rand())
            print("Computer enter position of X as : ", pos)
            List[pos-1] = 'X'
            if(wincheck(List)):
                print_board(List)
                print("Computer wins!!", end="")
                flag1 = True
                break
            else:
                flag2 = True

    if(flag1):
        print("\nGame ENDS!!")
    else:
        print_board(List)
        print("\nIt's a tie!")

main()