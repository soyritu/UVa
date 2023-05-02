def PRINT():
    for i in range(3):
        if len(pegs[i]) == 0:
            print(f"{names[i]}=>")
        else:
            print(f"{names[i]}=>",end="   ")
            print(*(pegs[i]))
    print()

def move(Disks,From,Buffer,To):
    if steps[0]==steps[1]:
        return
    if Disks > 0:
        move(Disks-1,From,To,Buffer)
        if steps[0]==steps[1]:
            return
        steps[0]+=1
        pegs[To].append(pegs[From].pop())
        PRINT()
        move(Disks-1,Buffer,From,To)


problem = 0
while True:
    problem +=1
    n,m = map(int,input().split())
    if n == m == 0:
        break
    names = ['A','B','C']
    A = [i for i in range(n,0,-1)]
    B = []
    C = []
    pegs =[A,B,C]
    steps = [0,m]
    print(f"Problem #{problem}")
    print()
    PRINT()
    move(n,0,1,2)
    
