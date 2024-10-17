#lambda фуексия. обработка искулючениии
def first(wort: str) -> str:
    return wort.title()

def shov(come_, some):
    for element in come_:
        print(come_(element))


gorod = ['tokmok', 'bihkek', 'darhan']
soor = sorted(gorod, key=lambda word: word[1])
print(gorod)

lambda_r = lambda  n1, n2: n1 + n2
print(lambda_r(2, 3))

try:
    print(2 * 'ry')
except:
    print('error ')
else:
    print('ok')
finally:
    print('ошибка устранене')


#for = перебирает

cc = 5
while cc != 0:
    print('sdfghjk')
    cc -=1