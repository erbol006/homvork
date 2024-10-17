#cлова - dict
#славрь {key: value}
#eee = {'neim': 'erbol' , "vozrast": 18 }
#
"""доступ к лючам"""
# print(eee['neim'])
# print(eee.get("nam", ' нет токого ключа'))
# #дабавление
# eee['sorneim'] = 'soronbaev'#добавляеттодну
# eee.update({'rrr':12, 'www': 34})#дабавляет много и можно заменить
""""удаление"""
#eee.pop('www')#стирает только одну
#del eee ['rrr']#стирает полностю
#
# eee['vozrast'] = 22
# eee.pop('neim')#удаляет
# del eee['vozrast']
#
#
#
# print(eee)
#
"""монжество set"""
# e1 = [1, 2, 3, 4, 5, 1, 2, 3]
# e2 = (1, 2, 3, 4, 5, 1, 2, 3)
# e3 = {1, 2, 3, 4, 5, 1, 2, 3}
# print(e1)
# print(e2)
# print(e3)

# for i in eee:
#     sleer(2)#секунда вывидения
#     print((f'{i}: {eee[i]}'))
# print(eee.keys())#вазврашяет только ключи
# print(eee.values())#возварашает только значения
# print(eee.items())#приврошяет в картеж и делит по парам (ключ: значеиние)
#
# for cc, vvv in eee.items():
#     print(f'{cc} _ {vvv}')

# behbarmak = {"лапша", "мяса", "лук"}
# plov = {"рис", "морковь", "мяса"}
#
#
#
# print(behbarmak.union(plov))#скаладывает похожие значениия
# print(behbarmak | plov)#токойже как и сверху
#
# print(behbarmak.difference(plov))#что есть у бешбармака от плова
# print(behbarmak - plov)#токойже как и сверху
#
# print(behbarmak.intersection(plov))#что у еих есть похожего
# print(behbarmak & plov)#токойже как и сверху
#
# print(behbarmak.symmetric_difference(plov))#что у них не похожего похожое уберает
# print(behbarmak ^ plov)#токойже как и сверху

""""""""""""""""""""".issubset"""""""""""""""""""""""""""""
