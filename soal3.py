def angka(list):
    target = list[-1]
    for i in list:
        for j in list:
            if int(i) + int(j) == int(target):
                return [list.index(i), list.index(j)]
                            
a = input().split()
print(angka(a))
