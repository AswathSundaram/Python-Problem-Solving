
def minimumBribes(q):
    bribe = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2: 
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i): 
            if q[j] > q[i]:
                bribe += 1
    print(bribe)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

