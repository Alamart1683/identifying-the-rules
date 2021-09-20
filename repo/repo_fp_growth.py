from fpgrowth_py import fpgrowth

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
    curr_tran.append(split_line[3].replace('\n', ''))

ready_trans.append(curr_tran)
raw_data.close()

# print(ready_trans)

itemsets, rules = fpgrowth(ready_trans, 0.03, 0.03)
print("\n Выявленные правила (fp-growth):")
print('\n'.join(str(value) for value in rules))
