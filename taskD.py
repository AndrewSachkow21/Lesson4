def middle_mark(b):
    result = 0
    for i in b:
        result += int(i)
    return result/len(b)
def ocinka(d,*b):
    list = []
    for i in range(d):
        list.append(b[i].split())
    dict_marks={v[0]:middle_mark(v[1: ]) for v in list}
ocinka(2,"ivanov 5 4 6","danichkin 3 4 5")
