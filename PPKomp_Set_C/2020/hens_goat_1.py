K,M=map(int,input().split())

n_animal=M/2


n_goat=int( (K-M)/2 )
n_hen=int(n_animal-n_goat)

print(f"{n_hen} {n_goat}")