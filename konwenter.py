def konwenter(summa, kurs):
    return summa * kurs

while True:
    print('-----------')
    print('1. Конвертація\n2. Вихід\n')
    command = input('Виберіть команду: ')
    if command == '1':
        summa = float(input('Введіть сумму: '))
        if summa > 10000:
            print('Перевищенний ліміт(10.000)')
            continue
        else:
            kurs = float(input('Введіть курс: '))
            print("{0:.2f}".format(konwenter(summa, kurs)))
    elif command == '2':
        break
    else:
        print('Невідома коианда')
print('Бувай')