n=int(input())
arr=[1]
i=0
current_n=0
while i<n:
    arr[i]+(current_n+1)
    arr.append(arr[i]+(current_n+1))
    current_n+=1
    i+=1
print(arr[n-1])