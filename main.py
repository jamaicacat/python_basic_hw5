tuple_a = (1, 2, 3, 4, 5)
tuple_b = (4, 5, 6, 7, 8)
tuple_c = (4, 5, 6, 7, 8, 9, 10, 11)

# TUPLES

# 1. Використовуючи tuple_a і tuple_b і tuple_c зробити загальний кортеж tuple_d
# Очікуваний результат:
# tuple_d = (1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 9, 10, 11)
tuple_d = tuple_a + tuple_b + tuple_c

print('tuple_d', tuple_d)

# 2.  Використовуючи tuple_d згенерувати кортеж res, де буде кожен елемент це кортеж в якому:
# - першим елементом буде елемент з кортежу tuple_d
# - другим буде кількість елементів, що зустрічаються в кортежі tuple_d,
# за умови що кількість елементів, що зустрічаються > 1
# Очікуваний результат:
# res = ((4, 3), (5, 3), (4, 3), (5, 3), (6, 2), (7, 2), (8, 2), (4, 3) , (5, 3), (6, 2), (7, 2), (8, 2))

res_1 = ()

for item in tuple_d:
    total_count = tuple_a.count(item) + tuple_b.count(item) + tuple_c.count(item)

    if total_count > 1:
        res_1 = (*res_1, (item, total_count))

print('res_1', res_1)

# Задача 3. Використовуючи tuple_d згенерувати кортеж res,
# де буде кожен елемент це кортеж в якому:
# - першим елементом буде елемент з кортежу tuple_d
# - другим буде кортеж з індексами елементів які повторюється
# Очікуваний результат:
# res = ((4, (3, 5, 10)), (5, (4, 6, 11)), (6, (7, 12)), (7, (8, 13)), (8, (9, 14)))

res_2 = ()

for item in tuple_d:

    if len(res_2) and item <= res_2[-1][0]:
        # более элегантного способа провести фильтрацию на дублирование без введения доп. переменных не придумал
        continue

    duplicate_indexes = []

    for index in range(0, len(tuple_d)):
        if tuple_d[index] == item:
            duplicate_indexes.append(index)

    if len(duplicate_indexes) > 1:
        res_2 = (*res_2, (item, tuple(duplicate_indexes)))

print('res_2', res_2)

# LIST

list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
list_f = [9, 3, 4, 1, 8, 6, 5, 2, 0, 7]

# Задача 1. Зробити з двох списків list_a та list_b один
# Очікуваний результат:
# list_c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_c = list_a + list_b  # либо использовать метод extend, но тогда он изменит один из массивов
print('list_c', list_c)

# Задача 2. Зробити з двох списків один, елементи двох списком повинні чергуватися
# Очікуваний результат:
# list_с = [1, 6, 2, 7, 3, 8, 4, 9, 5, 10]

list_c_2 = []

for index in range(0, len(list_a)):
    list_c_2.append(list_a[index])
    list_c_2.append(list_b[index])

print('list_c_2', list_c_2)

# Задача 3. З першого списку зробити список тільки з парними, з другого тільки з непарними
# Очікуваний результат:
# list_с_a = [2, 4]
# list_c_b = [7, 9]

list_c_a = []
list_c_b = []

for item in list_a:
    if item % 2 == 0:
        list_c_a.append(item)

for item in list_b:
    if item % 2 == 1:
        list_c_b.append(item)

print('list_c_a', list_c_a)
print('list_c_b', list_c_b)

# Задача 4. Використовуючи список list_c завдання 1 "розгорнути" список, що б перший елемент став останнім,
# а останній першим
# Очікуваний результат:
# list_d = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

list_d = list_c[:]  # создал копию списка, чтобы не изменять изначальный массив
list_d.reverse()

print('list_d', list_d)

# Задача 5. Використовуючи список list_с і list_d отримати суму елементів попарно
# Очікуваний результат:
# res = [11, 11, 11, 11, 11, 11, 11, 11, 11, 11]

list_res = []

for index in range(0, len(list_c)):
    list_res.append(list_c[index] + list_d[index])

print('list_res', list_res)

# Задача 6. Використовуючи список list_f отримати два списки один відсортований по зростанню, а один по спаданню
# res1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

res1 = list_f[:]  # attention!: list_f не содержит цифру 10, как того требует результат
res1.sort()
print('res1', res1)

res2 = list_f[:]
res2.sort(reverse=True)
print('res2', res2)

# Задача 7. Використовуючи список list_с і list_d отримати список "кортежів" елементів попарно
# Очікуваний результат:
# res = [(1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3), (9, 2), (10, 1)]

res3 = []

for index in range(0, len(list_c)):
    res3.append((list_c[index], list_d[index]))

print('res3', res3)
