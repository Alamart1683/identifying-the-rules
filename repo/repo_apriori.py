from apriori_python import apriori
import time

# Получим датасет
raw_data = open("BreadBasket_DMS.csv", "r")
# raw_data = open("cut.csv", "r")
# raw_data = open("BreadBasket5k.csv", "r")

ready_trans = []
curr_tran = []
prev_tran_index = '1'
curr_tran_index = '1'

# Приведем данные к нужному виду
line = raw_data.readline()  # Опустим строку с заголовками
while True:
    line = raw_data.readline()
    if not line:
        break
    split_line = line.split(",")
    curr_tran_index = split_line[2]
    if curr_tran_index != prev_tran_index:
        ready_trans.append(curr_tran)
        # print(curr_tran)
        curr_tran = []
        prev_tran_index = curr_tran_index
    if split_line[3].replace('\n', '') != "NONE":
        curr_tran.append(split_line[3].replace('\n', ''))

ready_trans.append(curr_tran)
raw_data.close()

# print(ready_trans)
t0 = time.perf_counter()
freqItemSet, rules = apriori(ready_trans, minSup=0.005, minConf=0.6)
print("\n Выявленные правила (apriori) для минимальной достоверности 60%:")
print('\n'.join(str(value) for value in rules))
t1 = time.perf_counter() - t0

freqItemSet, rules = apriori(ready_trans, minSup=0.005, minConf=0.8)
print("\n Выявленные правила (apriori) для минимальной достоверности 80%:")
print('\n'.join(str(value) for value in rules))

print("\n Алгоритм apriori выполнился за ", t1, "секунд")
