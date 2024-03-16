#python
def Calc_time(current_timed, should_be_added):
    """ Функция считает актуальное время и возвращает его

        Описание аргументов:
        current_timed – значение при остановке времени
        should_be_added – посчитаное значение в часах

       """
    time = current_timed.split(":")
    return str((int(time[0]) + int(should_be_added)) % 24) + ":" + ":".join(time[1:])


def my_sort(data):
    """ Функция сортирует значения и возвращает их

        Описание аргументов:
        data - массив, который нужно отсортировать

       """
    should_be_returned = [min(data, key= lambda x: x[2]), max(data, key= lambda x: x[2])]
    data.remove(min(data, key= lambda x: x[2]))
    data.remove(max(data, key= lambda x: x[2]))
    for elem in data:
        for i in range(1, len(should_be_returned)):
            if should_be_returned[i - 1][2] <= elem[2] and elem[2] <= should_be_returned[i][2]:
                should_be_returned.insert(i, elem)
                break
    return should_be_returned

#чтение файла и преобразование его в двумерный масив
with open("astronaut_time.csv", encoding="UTF-8") as fin:
    data = list(map(lambda x: x.split(","), fin.read().split("\n")))
    keys = data[0]
    data = data[1:]


#Сортировка файла
data = my_sort(data)

# Запись нужного файла
with open("sorted.txt", "w") as fout:
    #итерирую по элементам и записываю их в файл в нужном формате
    for elem in data:
        fout.write(f"На станции {elem[1]} в каюте {elem[2]} восстановлено время. Актуальное время: {Calc_time(elem[-2], elem[-1])}\n")
        pass
