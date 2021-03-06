def name(name, surname):
    return f"Ім'я: {name}. Прізвище: {surname}\n"

def birth(year, month):
    return f"Рік народження: {year}\nМісяць народження: {month}"

with open('1.txt', 'w', encoding='utf-8') as file:
    
    file.write(name(input('Введіть імя: '), input('Введіть прізвище: ')))
    file.write(birth(input('Введіть рік народження: '), input('Введіть місяць народження: ')))

print('-----------\nУ файл було записано: ')

with open('1.txt', 'r', encoding='utf-8') as file:
    array = file.readlines()
    
    for i in range(len(array)):
        print('\t' + array[i], end='')

print('Кінець програми')