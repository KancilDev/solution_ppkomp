n=int(input(""))

M = [int(x) for x in input("").split()] #list comprehension to accept as many numbers in 1 line 

M.sort(reverse=True)#sort number largest-->smallest
print(M)
sum=M[0]+M[1]+M[2]+M[3]+M[4]

print(sum)