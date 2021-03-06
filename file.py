def surname():
    return input('Введіть ваше прізвище: ')
with open('2.txt', 'w', encoding='utf-8') as file:
    file.write(surname())
with open('2.txt', 'r', encoding='utf-8') as file:
    content = file.readline()
    print(content)
    for i in range(len(content)):
        print(content[i])