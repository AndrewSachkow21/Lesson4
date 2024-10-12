def list_remove(N,list,P):
    list2 = []
    d = ""
    for b in list:
        if b != " ":
            d += b
        elif b == " ":
            list2.append(d)
            d = ""
    print(list2)
    output = list2.copy()
    for i in list2:
        print(int(i) == P,P,i)
        if int(i) == P:
            output.remove(i)
    return output
print(list_remove(input("1"),input("2"),int(input("3"))))
