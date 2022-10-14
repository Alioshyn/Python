def tribonachi_generator(val):
    num1 = 0
    num2 = 0
    num3 = 1
    counter = 0
    while counter <= val:
        counter += 1
        if counter == 1 or counter == 2:
            yield num1
        elif counter == 3:
            yield num3
        else:
            sum_num =  num1 + num2 + num3
            num1 = num2
            num2 = num3
            num3 = sum_num
            yield sum_num


val = int(input('Введите длину ряда Трибоначчи: '))
iter = tribonachi_generator(val)

trib_list = []
for i in iter:
    trib_list.append(i)
print(trib_list)