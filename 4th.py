#python

#чтение файла и преобразование его в двумерный масив
with open("astronaut_time.csv", encoding="UTF-8") as fin:
    data = list(map(lambda x: x.split(","), fin.read().split("\n")))
    keys = data[0]
    data = data[1:]


#итерирую по элементам и записываю их записываю их в словарь
dct = {}
for elem in data:
    if elem[1] not in dct.keys():
        dct[elem[1]] = int(elem[-1])
    else:
        dct[elem[1]] += int(elem[-1])


# Запись списка в файл
with open("list.txt", "w") as fout:
    # вывод всех станций с временем простоя 9
    for (key, value) in dct.items():
        if value == 9:
            fout.write(str(key)+"\n")

#Запись списка в файл
with open("station_max_downtime.csv.", "w") as fout:
    # итерирую по элементам и записываю их в файл в нужном формате
    fout.write("numberStation,downtime\n")
    for (key, value) in dct.items():
        fout.write(f"{key},{value}\n")