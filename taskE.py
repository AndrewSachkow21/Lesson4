def middle_mark(b):
    result = 0
    for i in b:
        result += int(i)
    return round(result/len(b),2)
def ocinka(d,*b):
    ans=[]
    retuern = []
    for x in range(3):
        for i in [x[1: ] for x in [b[i].split() for i in range(d)]]:
            ans.append(int(i[x]))
        retuern.append(middle_mark(ans))
    return retuern 
print(ocinka(2,"ivadov 5 4 1","danichkin 3 4 5"))
