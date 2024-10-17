# w -- write (переапись апись)
# a -- add (доп папись)
# x -- сосдаёт и провер ест ли другая сапись

file = open('new_file.txt', 'w')
file.write('текс на латынь')
file.close()

with open('new_file.txt','a') as new_file:
    new_file.write('\nвтроряя страка')
# with open('other.txt', 'x') as file:
#     file.write('новый')
# from time import sleep
#
# with open('new_file.txt', 'r') as file:
#     for i in file.read():
#        # sleep(1)
#         print(i, end='')
#
#

