
def countTriplets(arr, r):
    potential = {}
    count = {}
    total = 0

    for val in arr:
        if val in count:
            total += count[val]
        
        if val in potential:
            if val * r in count:
                count[val * r] += potential[val]
            else:
                count[val * r] = potential[val]
        
        if val * r in potential:
            potential[val * r] += 1
        else:
            potential[val * r] = 1

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
