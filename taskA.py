def list_remove(N,list,P):
    list2 = list.split()
    output = list2.copy()
    for i in list2:
        if int(i) == P:
            output.remove(i)
    return output
print(list_remove(input("1"),input("2"),int(input("3"))))
