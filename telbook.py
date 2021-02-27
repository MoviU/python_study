tel_book = {
    'max': '012309128'
}
# Пошук за іменем
def seacrh_by_name(name):
    if name in tel_book.keys():
        return print(f"У контакта {name} номер телефону: {tel_book[name]}")
    return print('Такого контакта немає')
# Пошук за номером
def seacrh_by_phone(number):
    if number in tel_book.values():
        for key, val in tel_book.items():
            if val == number:
                return print(f"Номер {number} є у користувача {key}")
    return print('Контакта з таким номером телефону немає')
# Перегля словника
def view():
    if len(tel_book) == 0:
        return print('Записник пустий')
    print('Всі номера телефонів: ')
    for key, val in tel_book.items():
        print(f'\t{key}: {val}')
# Додавання
def add(name):
    if name in tel_book.keys():
        return print("Такий контакт вже є")
    number = input('Введіть номер телефону: ')
    tel_book.setdefault(name, number)
# Оновлення
def update(name):
    if name not in tel_book.keys():
        return print("Такого контакта немає")
    phone = input("Введіть новий номер телефону: ")
    tel_book[name] = phone
# Видалленя
def delete(name):
    if name not in tel_book.keys():
        return print("Такого контакта немає")
    del tel_book[name]
    return print(f"Контакт {name} був успішно видаленний")

def ui():
    try:
        # об'явлення словаря
        print('--------------')
        # Виведення команд для користувача
        commands = ['Пошук елемента за іменем', "Пошук елемента за номером", "Виведення значень записника", "Додавання нового запису", "Оновлення телефону абонента", "Видалення абонента", "Вихід з програми"]
        print('Всі команди: ')
        for i in range(len(commands)):
            print(f'\t{i + 1} - {commands[i]}')
        command = input('Виберіть команду: ')
        print()
        # Описання роботи команд
        if command == '7':
            print('Кінець програми')
            exit()
        elif command == '1':
            seacrh_by_name(input("Введіть ім'я контакта: "))
        elif command == '2':
            seacrh_by_phone(input("Введіть номер контакта: "))
        elif command == '3':
            view()
        elif command == '4':
            add(input("Введіть ім'я контакта: "))
        elif command == '5':
            update(input("Введіть ім'я контакта: "))
        elif command == '6':
            delete(input("Введіть ім'я контакта: "))
        print()
    except ValueError:
        print('Ви ввели неправильні значення. Попробуйте ще раз')
    ui()

if __name__ == "__main__":
    ui()