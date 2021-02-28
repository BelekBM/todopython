lst = ["92", "91", "49", '87', '74', '20', '94', '12', '64', '36', '97', '2', '96', '40', '97', '36', '32', '22', '80', '83', '49', '52', '62', '31',
'55', '86', '84', '1', '22', '15', '52', '18', '78', '92', '21', '9', '85', '89', '54', '99', '80', '7', '4', '31', '30', '28', '59', '35', '72', '33']
{i: j for i,j in enumerate(lst)}

import random
guessesTaken = 5

myName = input()
number = random.randint(1,20)

while guessesTaken < 6:
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken+1
    if guess < number:
        print('слишком мало')
    if guess > number:
        print("слишком много")
    if guess == number:
        break
if guess == number:
    print("Класс вы угадали")
if guess != number and guessesTaken == 0:
    print("Все, вы не выиграли. игра завершилась")

a = 'bloomberg'
a[3, 4, 5]

from itertools import zip_longest
a = 'Aidana'
b = 'Adilet'
l = []
for i in list(zip_longest(a,b)):
    l.extend(i)
print([i for i in l if i])
