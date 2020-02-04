def multiplicativePersistence(num):
    str_num = str(num)
    multiplicative = 0

    while len(str_num) > 1:
        num = int(str_num[0]) * int(str_num[1])
        str_num = str(num)
        multiplicative += 1
    else:
        return multiplicative


test = multiplicativePersistence(39)
print(test)
