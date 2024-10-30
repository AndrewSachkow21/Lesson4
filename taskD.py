def middle_mark(b):
    result = 0
    for i in b:
        result += int(i)
    return round(result/len(b),2)
def ocinka(d,*b):
    dict_marks={v[0]:middle_mark(v[1: ]) for v in [b[i].split() for i in range(d)]}
    print(dict_marks)
    return dict_marks
print(ocinka(2,"ivadov 5 4 3","danichkin 3 4 5"))
