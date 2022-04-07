zero = '   1  2  3'
first = ['1','  -','  -','  -']
second = ['2','  -','  -','  -']
third = ['3','  -','  -','  -']
list = [zero,first,second,third]

# Сделали матрицу для игры

def tape(a,s = 0.06):
    import time
    for i in a:
        print(i, end = "")
        time.sleep(s)
    time.sleep(3)
    print("\n")

# Сделали функцию для красивого вывода приветствия


def out(list):
    print(zero)
    for i in list[1:]:
        for j in i:
            print(j,end="")
        print("")
    print('\n')

# Сделали функцию вывода игрового поля

def turn(a,t,list = list):
    a = (a.replace(" ",''))
    a = (a.replace(",", ''))
    a = (a.replace(".", ''))
    a = (a.replace(":", ''))
    if len(a) == 2 and a.isdigit() and 0 < int(a[0]) < 4 and 0 < int(a[1]) < 4 and list[int(a[1])][int(a[0])]=='  -':
        # проверка введеного игроком значения
        b = "x" if t else "o"  # Если t истина, то крестик, иначе нолик
        list[int(a[1])][int(a[0])]='  %s' %b
        out(list)
    else:
        print("Ошибка хода, пожалуйста схоите еще раз")
        turn(input(),t)

#сделали функцию, которая показывает куда поставлен символ

def check(list = list):
    for i in list[1:]:
        if all([j == '  x' for j in i[1:]]):
            print("x выиграл!")
            return True
        elif all([j == '  o' for j in i[1:]]):
            print("o выиграл!")
            return True
    for i in range(1, 4):
        if all([j[i] == '  x' for j in list[1:]]):
            print("x выиграл!")
            return True
        elif all([j[i] == '  o' for j in list[1:]]):
            print("o выиграл!")
            return True
    if list[2][2] == '  x' and (list[2][2] == list[1][3] == list[3][1] or list[2][2] == list[1][1] == list[3][3]):
        print("x выиграл!")
        return True
    if list[2][2] == '  o' and (list[2][2] == list[1][3] == list[3][1] or list[2][2] == list[1][1] == list[3][3]):
        print("o выиграл!")
        return True
# функция для проверки выигрыша
# не смог придумать как укоротить, нужно над этим подумать

tape("Приветствую!\nЭто игра 'Крестики - нолики'!\nДля хода нужно указать ячейку, указав кординаты по вертикали и горизонтали\nПервые ходят 'х'")

out(list)

y = False
while True:
    y = False if y else True
    turn(input(),y)
    if check():
        print("Поздравляем !")
        break