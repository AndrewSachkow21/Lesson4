def middle_mark(b):
    result = 0
    for i in b:
        result += int(i)
    return round(result/len(b),2)
def ocinka(d,*b):
    list = [b[i].split() for i in range(d)]
    dict_marks={middle_mark(v[1: ]) for v in list}
    return dict_marks
print(ocinka(2,"ivadov 5 4 1","danichkin 3 4 5"))