#module_9_3.py

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x)-len(y) for x,y in zip(first, second) if len(x) != len(y))
second_result = (len(second[i]) == len(first[i]) for i in range(len(second)))

print(list(first_result))
print(list(second_result))
