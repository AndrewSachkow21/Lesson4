d = lambda b,*d: [s*b for s in d] 
print(d(2,3,3,4,2,4))
G=input("3")
print([x for x in input("2").split() if int(x) != int(G)]) 