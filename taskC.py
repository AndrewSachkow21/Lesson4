
def list_remove(N,list,P,Q):
    list2 = [int(x) for x in list.split()]
    d = []
    order = [int(x) for x in Q.split()]
    try:
        list2[P-1:P+1]=[list2[P]]
    except:
        list2[P-2:int(N)]=[list2[P-2]]
    list2[order[0]-1]=order[1],list2[order[0]-1]
    for i in list2:
        if type(i) != tuple:
            d.append(i)
        else:
            d.append(i[0])
            d.append(i[1])
    return d
print(list_remove(input("1"),input("2"),int(input("3")),input("4")))
