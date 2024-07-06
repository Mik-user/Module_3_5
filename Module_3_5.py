def get_multiplied_digits (number):
    x = str(number)
    rez = 1
    for i in x:
        if int(i) > 0:
            rez = int(i) * rez
    return rez
while 1>0:
    str_number = input('Введите число:')
    if str_number.isnumeric():
        if len(str_number) == 1:
            print(int(str_number))
        else:
                first = int(str_number[0])
                print(first * get_multiplied_digits(int(str_number[1:])))
        break
    else:
        print ('Я ж просил число, а оно состоит из цифр, а не букв')
        continue