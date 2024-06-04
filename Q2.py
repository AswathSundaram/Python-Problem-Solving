
def arrayManipulation(n, queries):                               
    # Write your code here
    l=[]
    for i in range(n):
        l.append(0)
    l1=len(queries)
    for query in queries:
        a, b, k = query
        for q in range(a-1,b):
            l[q]+=k
    qq=max(l)
    return qq
  
# but for large data its not working and the correct solution seems to be:
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for query in queries:
        a, b, k = query
        arr[a - 1] += k
        if b < n:
            arr[b] -= k
    max_value = 0
    current_value = 0
    for i in range(n):
        current_value += arr[i]
        if current_value > max_value:
            max_value = current_value
    return max_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    fptr.write(str(result) + '\n')
    fptr.close()
