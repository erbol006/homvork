ee = 0
while ee < 12:
    print('Кто вы по знаку зодиака?')
    mesas = int(input('Введите месяц рождения (1-12): '))
    dea = int(input('Введите день рождения: '))
    time = input('сколько')
    if time == 'все':
        break
    if (mesas == 1 and dea >= 20) or (mesas == 2 and dea <= 18):
         print('Водолей')
    elif (mesas == 2 and dea >= 19) or (mesas == 3 and dea <= 20):
        print('Рыбы')
    elif (mesas == 3 and dea >= 21) or (mesas == 4 and dea <= 19):
        print('Овен')
    elif (mesas == 4 and dea >= 20) or (mesas == 5 and dea <= 20):
        print('Телец')
    elif (mesas == 5 and dea >= 21) or (mesas == 6 and dea <= 20):
        print('Близнецы')
    elif (mesas == 6 and dea >= 21) or (mesas == 7 and dea <= 22):
        print('Рак')
    elif (mesas == 7 and dea >= 23) or (mesas == 8 and dea <= 22):
        print('Лев')
    elif (mesas == 8 and dea >= 23) or (mesas == 9 and dea <= 22):
        print('Дева')
    elif (mesas == 9 and dea >= 23) or (mesas == 10 and dea <= 22):
        print('Весы')
    elif (mesas == 10 and dea >= 23) or (mesas == 11 and dea <= 21):
        print('Скорпион')
    elif (mesas == 11 and dea >= 22) or (mesas == 12 and dea <= 21):
        print('Стрелец')
    elif (mesas == 12 and dea >= 22) or (mesas == 1 and dea <= 19):
        print('Козерог')
    else:
        print('Неверная дата рождения')
round -= 1