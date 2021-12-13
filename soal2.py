def huruf_muncul(kata):
    dict = {}
    for i in kata:
        dict[i] = kata.count(i)
    for i, v in dict.items():
        a = i,':', v
        print(i + ' = ' + str(v))
    return a
 

a = input().split()
huruf_muncul(a)
