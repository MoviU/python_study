def name(name, surname):
    return f"Ім'я: {name}. Прізвище: {surname}\n"

def birth(year, month):
    return f"Рік народження: {year}\nМісяць народження: {month}"

with open('1.txt', 'w', encoding='utf-8') as file:
    
    file.write(name(input('Введіть імя: ').title(), input('Введіть прізвище: ').title()))
    file.write(birth(input('Введіть рік народження: '), input('Введіть місяць народження: ').title()))

print('-----------\nУ файл було записано: ')

with open('1.txt', 'r', encoding='utf-8') as file:
    content_array = file.read().splitlines()
    for i in range(len(content_array)):
        print('\t' + content_array[i])
        
print('Кінець програми')