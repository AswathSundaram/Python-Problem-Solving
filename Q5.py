
def countInversions(arr):
    # Write your code here
    n=len(arr)
    if n==1:
        return 0
    n1=n//2
    n2=n-n1
    arr1=arr[:n1]
    arr2=arr[n1:]
    ans =countInversions(arr1)+countInversions(arr2)
    
    i1,i2=0,0
    for i in range(n):
        if i1<n1 and(i2>=n2 or arr1[i1]<=arr2[i2]):
            arr[i]=arr1[i1]
            ans+=i2
            i1+=1
        elif i2<n2:
            arr[i]=arr2[i2]
            i2+=1
    return ans
    
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
