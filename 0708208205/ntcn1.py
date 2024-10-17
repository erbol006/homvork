while True:
    eee = (input("ведитн свет светофора""'зелёный'""'жолтый'""'красный' ")).lower()
    if eee =='стоп':
        break
    if eee == 'зелёный' or set(eee).issubset('зелёный'):
        print('ежайте')
    elif eee == 'жолтый' or set(eee).issubset('жолтый'):
        print('приготовтесь к остоновки')
    elif eee == 'красный' or set(eee).issubset('красный'):
        print('остоновитесь')

    else:
        print('не правельно вили ')
