def list_remove(N,list,P):
    list2 = []
    for b in str(list):
        if b != " ":
            list2.append(b)
    output = list2.copy()
    for i in list2:
        if int(i) == P:
            output.remove(i)
    return output
print(list_remove(3,2333333,2))
