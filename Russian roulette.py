import random
import time
def func():
    print("---------------------------")
    print("1 раунд")
    time.sleep(3)
    print("---------------------------")
    print("2 холостых - 3 заряженых")
    time.sleep(4)
    print("Шанс выпадения холостого составляет 40% | Шанс выпадения заряженого составляет 60%")
    time.sleep(5)
    n_1 = random.randrange(1,6)
    if(n_1 < 4):
        print("Вам выпал заряжений!")
        time.sleep(3)
        print("Вы погибли(")
        x = str(input("Вы хотите начать новую игру Y/N: "))
        print(x)
        if(x=="Y"):
            print("Колесо Сансары снова вращается")
            time.sleep(3)
            func()
        elif(x=="N"):
            print("Хорошо!")
        else:
            print("Ошибка!")
            time.sleep(1)
            print("Перезагрузка Игры.")
            time.sleep(1.5)
            print("Перезагрузка Игры..")
            time.sleep(2)
            print("Перезагрузка Игры...")
            time.sleep(2.5)
            print("Перезагрузка Игры....")
            time.sleep(3)
            func()
    elif(n_1 == 4,5):
        print("Вам выпал холостой! Вам повезло...")
        time.sleep(2.5)
        print("Вы проходите на следующий раунд")
        m = str(input("Нажмите Y для продолжения игры: "))
        if(m=="Y"):
            print(

                # Empty
            )
            print("---------------------------")
            print("2 раунд")
            time.sleep(3)
            print("---------------------------")
            print("3 холостых - 3 заряженых")
            time.sleep(4)
            print("Шанс выпадения холостого составляет 50% | Шанс выпадения заряженого составляет 50%")
            time.sleep(5)
            p_1 = random.randrange(1,7)
            if(p_1 == 4,5,6):
                print("Вам выпал заряжений!")
                time.sleep(3)
                print("Вы погибли(")
                x_1 = str(input("Вы хотите начать новую игру Y/N: "))
                print(x_1)
                if(x_1=="Y"):
                    print("Колесо Сансары снова вращается")
                    time.sleep(3)
                    func()
                elif(x_1=="N"):
                    print("Хорошо!")
                else:
                    print("Ошибка!")
                    time.sleep(1)
                    print("Перезагрузка Игры.")
                    time.sleep(1.5)
                    print("Перезагрузка Игры..")
                    time.sleep(2)
                    print("Перезагрузка Игры...")
                    time.sleep(2.5)
                    print("Перезагрузка Игры....")
                    time.sleep(3)
                    func()
            elif(p_1 < 4):
                print("Вам выпал холостой! Вам повезло...")
                time.sleep(2.5)
                print("Вы проходите на следующий раунд")
                print(

                    # Empty
                )
                print("---------------------------")
                print("3 раунд")
                time.sleep(3)
                print("---------------------------")
                print("2 холостых - 1 заряженый")
                time.sleep(4)
                print("Шанс выпадения холостого составляет 67% | Шанс выпадения заряженого составляет 33%")
                time.sleep(5)
                b_1 = random.randrange(1, 4)
                if (b_1 == 3):
                    print(b_1)
                    print("Вам выпал зараженный!")
                    time.sleep(3)
                    print("Вы погибли(")
                    x_1 = str(input("Вы хотите начать новую игру Y/N: "))
                    if (x_1 == "Y"):
                        print("hello World!")
                    elif (x_1 == "N"):
                        print("Хорошо!")
                    else:
                        print("Ошибка!")
                        print("Ошибка!")
                        time.sleep(1)
                        print("Перезагрузка Игры.")
                        time.sleep(1.5)
                        print("Перезагрузка Игры..")
                        time.sleep(2)
                        print("Перезагрузка Игры...")
                        time.sleep(2.5)
                        print("Перезагрузка Игры....")
                        time.sleep(3)
                elif (b_1 < 3):
                    print(b_1)
                    print("Вам выпал холостой! Вам повезло...")
                    time.sleep(2.5)
                    print("Вы проходите на следующий раунд")
                    m = str(input("Нажмите Y для продолжения игры: "))
                    if (m == "Y"):
                        print(

                            # Empty
                        )
            else:
                print("Ошибка!")
                func()
            print("---------------------------")
    else:
        print("Ошибка!")
        func()
    print("---------------------------")
# func()