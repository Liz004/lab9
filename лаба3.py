word = []
while(word1 := str(input())) !='стоп':
    word.append(word1)
print(''.join(word))

def z2():
    word = []
while(word := str(input())) !='стоп':
    if "ф" in word or "Ф" in word:
        print('Ого! Это редкое слово!')
    else:
        print('Эх, это не очень редкое слово...')

def z3():
    pass
from random import randint

count = 0
while True:
    a = randint(1, 100)
    b = randint(1, 100)
    print (f"{a}+{b} =", end = "")
    num = input()
    while not num.isdigit() and num !='стоп':
        print('Ответ неверный')
        break
    if num == 'стоп':
        break
    num = int(num)
    if a + b == num:
        print('Ответ правильный!')
    else:
        count: count + 1
        print('Ответ неверный')
    if count == 3:
        print('Игра окончена. Правильных ответов: 1')
        break