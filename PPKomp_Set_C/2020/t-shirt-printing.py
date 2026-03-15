N=float(input())
K=str(input(""))

if K=="ahli":
    if N>=200:
        price=8
    elif N>50:
        price=10
    elif N>20:
        price=13
    else:
        price=16
else:
    if N>=200:
        price=9
    elif N>=50:
        price=12
    elif N>=20:
        price=15
    else:
        price=18

print("{:.2f}".format(N*price))

