marka_spisok = []
dvig_spisok = []
shin_spisok = []
color_spisok = []
tonirowka_spisok = []
dveri_far_spisok = []

file_sohr = open('sohr', encoding='utf-8')
file_sohr = file_sohr.read()

if len(file_sohr) != 0:
    file_sohr = file_sohr.split(';')
    print(file_sohr)
    file_sohr0 = (file_sohr[0])[:-1].split(',')
    file_sohr1 = (file_sohr[1])[:-1].split(',')
    file_sohr2 = (file_sohr[2])[:-1].split(',')
    file_sohr3 = (file_sohr[3])[:-1].split(',')
    file_sohr4 = (file_sohr[4])[:-1].split(',')
    file_sohr5 = (file_sohr[5:])[:-1]

    for i in range(len(file_sohr0)):
        marka_spisok.append(file_sohr0[i])
        dvig_spisok.append(file_sohr1[i])
        shin_spisok.append(file_sohr2[i])
        color_spisok.append(file_sohr3[i])
        tonirowka_spisok.append(file_sohr4[i])
    dveri_far_spisok = file_sohr5

file = open('name', encoding='utf-8')
file = file.read().split('\n')
file_mark = file[0].split(',')
file_dvig = file[1].split(',')
file_shin = file[2].split(',')
file_color = file[3].split(',')
file_tonirowka = file[4].split(',')

class Sozdanie_car:
    haracter = []
    j = []
    def marka_sozd(self):
        print("Выберите марку автомобиля")
        print("0. Назад")
        print(file_mark)
        for i in range(len(file_mark)):
            print(str(i + 1) + ')', file_mark[i])
        a = int(input())
        while (len(file_mark) < a) or (a < 0):
            print("Вы ввели некорректные данные")
            a = int(input())
        if a == 0:
            Menu().menu()
        if len(marka_spisok) == 0:
            self.haracter.append(file_mark[a - 1] + "(0)")
        else:
            for i in marka_spisok:
                self.j.append(int(i[-2]))
            self.haracter.append(file_mark[a-1]+"("+str(max(self.j)+1)+")")
        return ''

    def dvig_sozd(self):
        print("Выберите тип двигателя")
        print("0. Назад")
        print(file_dvig)
        for i in range(len(file_dvig)):
            print(str(i + 1) + ')', file_dvig[i])
        a = int(input())
        while (len(file_dvig) < a) or (a < 0):
            print("Вы ввели некорректные данные")
            a = int(input())
        if a == 0:
            Menu().menu()
        self.haracter.append(file_dvig[a - 1])
        return ''

    def shin_sozd(self):
        print("Выберите тип шин")
        print("0. Назад")
        print(file_shin)
        for i in range(len(file_shin)):
            print(str(i + 1) + ')', file_shin[i])
        a = int(input())
        while (len(file_shin) < a) or (a < 0):
            print("Вы ввели некорректные данные")
            a = int(input())
        if a == 0:
            Menu().menu()
        self.haracter.append(file_shin[a - 1])
        return ''

    def color_sozd(self):
        print("Выберите цвет автомобиля")
        print("0. Назад")
        print(file_color)
        for i in range(len(file_color)):
            print(str(i + 1) + ')', file_color[i])
        a = int(input())
        while (len(file_color) < a) or (a < 0):
            print("Вы ввели некорректные данные")
            a = int(input())
        if a == 0:
            Menu().menu()
        self.haracter.append(file_color[a - 1])
        return ''

    def toniriwka_sozd(self):
        print("Выберите тонировку")
        print("0. Назад")
        print(file_tonirowka)
        for i in range(len(file_tonirowka)):
            print(str(i + 1) + ')', file_tonirowka[i])
        a = int(input())
        while (len(file_tonirowka) < a) or (a < 0):
            print("Вы ввели некорректные данные")
            a = int(input())
        if a == 0:
             Menu().menu()
        self.haracter.append(file_tonirowka[a - 1])
        return ''

class Prosmotr_car(Sozdanie_car):
    def prosmotr_car(self):
        j = 0
        print("Выберите автомобиль")
        print("0. Назад")
        for i in range(0, len(marka_spisok)):
            j += 1
            print(str(j) + ".", marka_spisok[i])
        if len(marka_spisok) == 0:
            print("Нету созданных автомобилей")
        a = int(input())
        while a < 0 or a > len(marka_spisok):
            print("Вы ввели некорректные данные")
            a = int(input())
        if a == 0:
            Menu().menu()
        else:
            print("0. Вернуться к списку созданных автомобилей")
            print("1. Войти в режим редактирования")
            print('Марка:', (marka_spisok[a - 1])[:-3])
            print('Двигатель:', dvig_spisok[a - 1])
            print('Шины:', shin_spisok[a - 1])
            print('Цвет:', color_spisok[a - 1])
            print('Тонировка:', tonirowka_spisok[a - 1])
            print('Дверь справа спереди:', dveri_far_spisok[0 + (a - 1) * 6])
            print('Дверь слева спереди:', dveri_far_spisok[1 + (a - 1) * 6])
            print('Дверь слева сзади:', dveri_far_spisok[2 + (a - 1) * 6])
            print('Дверь справа сзади:', dveri_far_spisok[3 + (a - 1) * 6])
            print('Передние фары:', dveri_far_spisok[4+(a-1)*6])
            print('Задние фары:', dveri_far_spisok[5+(a-1)*6])
            a1 = int(input())
            while a1 < 0 or a1 > 1:
                print("Вы ввели некорректные данные")
                a1 = int(input())
            if a1 == 0:
                Prosmotr_car().prosmotr_car()
            if a1 == 1:
                print("0. Вернуться к списку созданных автомобилей")
                print(" 1. Изменить марку")
                print(" 2. Изменить двигатель")
                print(" 3. Изменнить шины")
                print(" 4. Изменить цвет")
                print(" 5. Изменить тонировку")
                print(" 6. Открыть/закрыть двери")
                print(" 7. Вкл./выкл. фыры ")
                a1 = int(input())
                while a1 < 0 or a1 > 7:
                    print("Вы ввели некорректные данные")
                    a1 = int(input())
                if a1 == 0:
                    Prosmotr_car().prosmotr_car()
                elif a1 == 1:
                    Sozdanie_car().marka_sozd()
                    marka_spisok[a-1] = self.haracter[-1]
                    self.haracter.clear()
                    print("Вы изменили марку")
                    print("Для продолжения введите любую клавишу")
                    a = input()
                    Prosmotr_car().prosmotr_car()

                elif a1 == 2:
                    Sozdanie_car().dvig_sozd()
                    dvig_spisok[a-1] = self.haracter[-1]
                    self.haracter.clear()
                    print("Вы изменили двигатель")
                    print("Для продолжения введите любую клавишу")
                    a = input()
                    Prosmotr_car().prosmotr_car()

                elif a1 == 3:
                    Sozdanie_car().shin_sozd()
                    shin_spisok[a-1] = self.haracter[-1]
                    self.haracter.clear()
                    print("Вы изменили шины")
                    print("Для продолжения введите любую клавишу")
                    a = input()
                    Prosmotr_car().prosmotr_car()

                elif a1 == 4:
                    Sozdanie_car().color_sozd()
                    color_spisok[a-1] = self.haracter[-1]
                    self.haracter.clear()
                    print("Вы изменили цвет")
                    print("Для продолжения введите любую клавишу")
                    a = input()
                    Prosmotr_car().prosmotr_car()

                elif a1 == 5:
                    Sozdanie_car().toniriwka_sozd()
                    tonirowka_spisok[a-1] = self.haracter[-1]
                    self.haracter.clear()
                    print("Вы изменили тонировку")
                    print("Для продолжения введите любую клавишу")
                    a = input()
                    Prosmotr_car().prosmotr_car()

                elif a1 == 6:
                    print("Выберите дверь")
                    print("0. Вернуться к списку созданных автомобилей")
                    print(" 1. Справа спереди")
                    print(" 2. Слева спереди")
                    print(" 3. Слева сзади")
                    print(" 4. Справа сзади")
                    a5 = int(input())
                    while a5 < 0 or a5 > 4:
                        print("Вы ввели некорректные данные")
                        a5 = int(input())
                    if a5 == 0:
                        Prosmotr_car().prosmotr_car()
                    if dveri_far_spisok[(a5 - 1) + 6 * (a - 1)] == "close":
                        dveri_far_spisok[(a5 - 1) + 6 * (a - 1)] = "open"
                        print("Вы открыли дверь")
                        print("Для продолжения введите любую клавишу")
                        a5 = input()
                        Prosmotr_car().prosmotr_car()
                    else:
                        dveri_far_spisok[(a5 - 1) + 6 * (a - 1)] = "close"
                        print("Вы закрыли дверь")
                        print("Для продолжения введите любую клавишу")
                        a5 = input()
                        Prosmotr_car().prosmotr_car()

                elif a1 == 7:
                    print("Выберите фары")
                    print("0. Вернуться к списку созданных автомобилей")
                    print(" 1. Передние фары")
                    print(" 2. Задние фары")
                    a6 = int(input())
                    while a6 < 0 or a6 > 2:
                        print("Вы ввели некорректные данные")
                        a6 = int(input())
                    if a6 == 0:
                        Prosmotr_car().prosmotr_car()
                    elif dveri_far_spisok[4 + (a6 - 1) + 6 * (a - 1)] == "off":
                        dveri_far_spisok[4 + (a6 - 1) + 6 * (a - 1)] = "on"
                        print("Вы включили фары")
                        print("Для продолжения введите любую клавишу")
                        a6 = input()
                        Prosmotr_car().prosmotr_car()
                    else:
                        dveri_far_spisok[4 + (a6 - 1) + 6 * (a - 1)] = "off"
                        print("Вы выключили фары")
                        print("Для продолжения введите любую клавишу")
                        a6 = input()
                        Prosmotr_car().prosmotr_car()
        return ''


class Delete():
    def car_del(self):
        print("Введите номер автомобиля, который нужно удалить")
        print("0. Назад")
        j = 0
        for i in range(0, len(marka_spisok)):
            j += 1
            print(str(j) + ".", marka_spisok[i])
        if len(marka_spisok) == 0:
            print("Нету автомобилей для удаления")
        a = int(input())
        while a < 0 or a > len(marka_spisok):
            print("Вы ввели некорректные данные")
            a = int(input())
        if a == 0:
            Menu().menu()
        marka_spisok.pop(a - 1)
        dvig_spisok.pop(a - 1)
        shin_spisok.pop(a - 1)
        color_spisok.pop(a - 1)
        tonirowka_spisok.pop(a - 1)
        del dveri_far_spisok[0 + (a - 1) * 6:6 + (a - 1) * 6]
        print("Вы удалили автомобиль")
        print("Для продолжения введите любую клавишу")
        a = input()
        Menu().menu()
        return ''

class Sohranenie:
    def Sohr(self):
        if len(marka_spisok) == 0:
            file_sohr = open('sohr', 'w', encoding='utf-8')
            file_sohr.write('')
            file_sohr.close()
        else:
            file_sohr = open('sohr', 'w', encoding='utf-8')
            file_sohr.write('')
            file_sohr.close()

            file_sohr = open('sohr', 'a', encoding='utf-8')
            for i in marka_spisok:
                file_sohr.write(i + ',')
            file_sohr.write(';')

            for i in dvig_spisok:
                file_sohr.write(i + ',')
            file_sohr.write(';')

            for i in shin_spisok:
                file_sohr.write(i + ',')
            file_sohr.write(';')

            for i in color_spisok:
                file_sohr.write(i + ',')
            file_sohr.write(';')

            for i in tonirowka_spisok:
                file_sohr.write(i + ',')
            file_sohr.write(';')

            for i in dveri_far_spisok:
                file_sohr.write(i+';')
            file_sohr.close()
        return ''

class Car():
    def __init__(self, m, d, s, c, t):
        self.marka = m
        self.dvig = d
        self.shin = s
        self.color = c
        self.tonirowka = t

    def car_dobavlenie(self):
        marka_spisok.append(self.marka)
        dvig_spisok.append(self.dvig)
        shin_spisok.append(self.shin)
        color_spisok.append(self.color)
        tonirowka_spisok.append(self.tonirowka)
        return ''

class Menu(Sozdanie_car,Sohranenie,Delete):
    def menu(self):
        print(marka_spisok) #
        print(dvig_spisok)  #
        print(shin_spisok)  #
        print(color_spisok) #
        print(tonirowka_spisok)
        print(dveri_far_spisok)
        print("1. Просмотр списка и редактирование созданных автомобилей")
        print("2. Создать автомобиль")
        print("3. Удалить автомобиль")
        print("4. Сохранить и выйти")
        a = input()
        while ("1" > a) or ("4" <  a):
            print("Вы ввели некорректные данные")
            a = input()
        if a == "1":
            print(Prosmotr_car().prosmotr_car())
        if a == "2":
            print(Sozdanie_car().marka_sozd())
            print(Sozdanie_car().dvig_sozd())
            print(Sozdanie_car().shin_sozd())
            print(Sozdanie_car().color_sozd())
            print(Sozdanie_car().toniriwka_sozd())
            print(Car(Sozdanie_car().haracter[0], Sozdanie_car().haracter[1], Sozdanie_car().haracter[2],Sozdanie_car().haracter[3],Sozdanie_car().haracter[4]).car_dobavlenie())
            self.haracter.clear()
            dveri_far = ["close", "close", "close", "close", "off", "off"]
            for i in dveri_far:
                dveri_far_spisok.append(i)
            print("Вы создали автомобиль")
            print("Для продолжения введите любую клавишу")
            a = input()
            return Menu().menu()
        if a == "3":
            print(Delete().car_del())
        if a == "4":
            print(Sohranenie().Sohr())
        return ''
print(Menu().menu())



