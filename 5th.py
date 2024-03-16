#python
def get_group(data):
    """ Функция находит группу и возвращает её

        Описание аргументов:
        data = массив элементов

       """
    return data[1].split("-")[0]

#чтение файла и преобразование его в двумерный масив
with open("astronaut_time.csv", encoding="UTF-8") as fin:
    data = list(map(lambda x: x.split(","), fin.read().split("\n")))
    keys = data[0]
    data = data[1:]

#итерирую по элементам и записываю их записываю их в словарь и запоминаю ноиера групп
groups = set()

kauti = {}
for elem in data:
    if get_group(elem) not in kauti.keys():
        groups.add(get_group(elem))
        kauti[get_group(elem)] = [elem[2]]
    else:
        kauti[get_group(elem)].append(elem[2])

prostoi = {}
for elem in data:
    if get_group(elem) not in prostoi.keys():
        prostoi[get_group(elem)] = [int(elem[-1])]
    else:
        prostoi[get_group(elem)].append(int(elem[-1]))


# Запись списка в файл
with open("table.txt", "w") as fout:
    # вывод всех станций с временем простоя 9
    for key in list(groups):
        fout.write(f"Номер группы: {key}. Каюты: {', '.join(kauti[key])}. Время простоя: {sum(prostoi[key]) / len(prostoi[key])}")