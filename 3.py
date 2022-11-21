def mirrorseries(n):
    validrefl = ["0","1","2","5","6","8","9"]
    firstint=n//7
    diff=n-(firstint*7)
    secondint=validrefl[diff]
    return (int(firstint*10+int(secondint)))
n=int(input())
print(mirrorseries(n))
