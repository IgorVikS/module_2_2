first = int(input('Введите число в "first": '))
second = int(input('Введите число в "second": '))
third = int(input('Введите число в "third": '))
if first == second and first == third and second == third:
    print('Число совпадений = 3')
elif first == second or second == third or third == first:
    print('Число совпадений = 2')
else:
    print('Число совпадений = 0')