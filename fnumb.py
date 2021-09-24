import random
a = random.randint(0, 30)
print('Я загадал число от 0 до 30, попробуй отгадай')
numb = int(input('Напиши предполагаемое число: '))
pop = 1
while numb != a:
    if numb > a:
        print('Загаданное число меньше')
    else:
        print('Загаданное число больше')
    numb = int(input('Напиши предполагаемое число: '))
    pop += 1
print('Вы угдали число, это правда: ' + str(a))
print('Вы справились за: ' + str(pop) + ' попыт(ок/ки/ку)')
