from random import randint

with open('input.txt', 'w', encoding='utf-8') as file:
    for i in range(10):
        file.write(randint(0, 100))

with open('input.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()
    summa = 0
    for i in range(len(content)):
        summa += int(content[i])
    print(f"В файлі записано: ")
    for i in range(len(content)):
        print('\t' + content[i])
        
print(f"Сума всіх чисел в файлі: {summa}")