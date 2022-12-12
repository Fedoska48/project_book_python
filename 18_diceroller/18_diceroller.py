import random, sys

# Приветственное сообщение с инструкцией
print('''Программа бросающие игральные кости.
Примеры:
3d6 - это три шестигранных кости,
2d12+4 - две двенадцатигранных кости с бонусными 4 очками,
Введите Q для того, чтобы покинуть игру.
''')

# Основной цикл
while True:
    try:
        # Ввод заначения
        diceStr = input('> ')
        # Выход из игры
        if diceStr.upper() == "Q":
            print('Спасибо за игру!')
            sys.exit()

        # Подготовка полученного значения для обработки
        diceStr = diceStr.lower().replace(' ', '')

        # Ищем d
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Забыли ввести значение "d".')

        # Ищем количество костей
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('Не введено количество костей.')
        numberOfDice = int(numberOfDice)

        # Поиск модификатора плюс или минус
        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')

        # Страница 106 строка 46

        # Поиск количества сторон в костях
        # если модификатор отсутствует - стороны след. за d до конца
        if modIndex == -1:
            numbersOfSides = diceStr[dIndex + 1:]
        # если модифик есть - стороны след. за d и до модификатора
        else:
            numbersOfSides = diceStr[dIndex + 1: modIndex]
        if not numbersOfSides.isdecimal():
            raise Exception('Пропущено значение количества сторон')
        numbersOfSides = int(numbersOfSides)

        # Выясняем сколько добовляет модификатор
        # если модифика нет - добавляем ноль
        if modIndex == -1:
            modAmount = 0
        # в другом случае добавляем значение за знаком модификации
        else:
            modAmount = int(diceStr[modIndex + 1:])
            if diceStr[modIndex] == '-':
                modAmount = -modAmount

        # Моделируем броски
        rolls = []
        for i in range(numberOfDice):
            rollResult = random.randint(1, numbersOfSides)
            rolls.append(rollResult)

        print(
            'Всего очков:', sum(rolls) + modAmount, '(Каждая кость: ', end=''
        )

        # Выводим значения бросков из rolls
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        # Выводим бонусы модификатора
        if modAmount != 0:
            modSign = diceStr[modIndex]
            print(', {}{}'.format(modSign, abs(modAmount)), end='')
        print(')')

    except Exception as exc:
        print(
            'Неравильный ввод. Введите значение в формате "3d6" или "4d10+1".'
        )
        print('Ввод неправильный из-за ошибки ' + str(exc))
        continue
