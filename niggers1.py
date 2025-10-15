"""
a = list(map(int, input("Ввелите числа: ").split()))
print(sum(a))

b = list(map(str, input("Введите строку: ").split()))
print(b[1], b[-1])

c = list(map(int, input("Введите числа: ").split()))
c1 = []
for i in c:
    if i % 2 == 0:
       c1.append(i)
print(c1)

d = list(map(int, input("Введите числа: ").split()))
d_odd = [i for i in d if i % 2 != 0]
d_even = [i for i in d if i % 2 == 0]
print(d_even, d_odd, sep='\n')
"""
"""
e = list(map(str, input("Введите что угодно: ").split()))
thing = ''
for i in e:
    thing = i
    while e.count(i)>0:
        e.remove(i)
    e.append(thing)
print(e)

f = list(map(str, input("Введите что угодно: ").split()))
f1 = list(map(str, input("Введите что угодно: ").split()))
f_intersection = []


for i in f:
    for j in f1:
        if i == j:
            f_intersection.append(i)
print(f_intersection)
"""
countries = {
    'Россия':'Москва',
    'Франция':'Париж',
    'Япония':'Токио',
}
g = input("Введите название страны: ")
for i in countries.keys():
    if g == i:
        print(f'Столица {g} - {countries[i]}')

grades = {
    'Алгебра':'5',
    'Геометрия':'3',
    'Русский':'4',
    'Информатика':'2',
    'Физра':'69',
}

print(f'Оценка по информатике - {grades['Информатика']}')
for k, v in grades.items():
    print(f'{k} - {v}')