#python
def Calc_time(current_timed, should_be_added):
    """ Функция считает актуальное время и возвращает его

        Описание аргументов:
        current_timed – значение при остановке времени
        should_be_added – посчитаное значение в часах

       """
    time = current_timed.split(":")
    return str((int(time[0]) + int(should_be_added)) % 24) + ":" + ":".join(time[1:])


#чтение файла и преобразование его в двумерный масив
with open("astronaut_time.csv", encoding="UTF-8") as fin:
    data = list(map(lambda x: x.split(","), fin.read().split("\n")))
    keys = data[0]
    data = data[1:]

# Запись нужного файла
while True:
    # запрос номера станции
    tmp = input()
    if tmp == "stop":
        break

    for elem in data:
        if elem[1] == tmp:
            print(f"На станции {elem[1]} восстановлено время (время остановки: {elem[-2]}). Актуальное время: {Calc_time(elem[-2], elem[-1])}")
            break
    else:
        print("На этой станции все хорошо")