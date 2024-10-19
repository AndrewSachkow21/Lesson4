def middle_mark(b):
    result = 0
    for i in b:
        result += int(i)
    return result/len(b)
def ocinka(d,*b):
    list = [b[i].split() for i in range(d)]
    dict_marks={v[0]:middle_mark(v[1: ]) for v in list}
    return dict_marks
print(ocinka(2,"ivanov 5 4 6","danichkin 3 4 5"))
