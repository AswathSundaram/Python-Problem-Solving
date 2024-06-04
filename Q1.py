
def minimumBribes(q):
    bribe = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2: 
            print("Too chaotic") #if the movement is >2 it is chaotic
            return
        for j in range(max(0, q[i] - 2), i): #it checks if the previous 2 values(if not exist then possible previous values either 0 or 1)is > than present
            if q[j] > q[i]:
                bribe += 1
    print(bribe)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

