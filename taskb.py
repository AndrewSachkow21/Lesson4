def list_remove(N,list,P):
    list2 = list.split()
    Count = 0 
    the_r=int(list2.copy()[P-1])
    for i in list2:
        list2[Count]=int(i)
        Count+=1    
    try:
        list2[P-1:P+1]=[list2[P]]
    except:
        list2[P-2:int(N)]=[list2[P-2]]
    return [the_r]+list2
print(list_remove(input("1"),input("2"),int(input("3"))))
