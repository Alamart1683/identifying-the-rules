from fpgrowth_py import fpgrowth
import pandas as pd
import math

# Прочитаем данные транзакций из файла эксель
trans = pd.read_excel('./tran.xlsx', header=None)
print("\n Считанная эксель-таблица:")
print(trans)

# Преобразуем все данные к списку списков
trans_values = trans.values
trans_values.tolist()
print("\n Неочищенные данные:")
print(trans_values)

# Преобразуем данные к виду, необходимому алгоритму априори (уберем мусор из списков)
ready_trans = []
i = 1

while i < len(trans_values):
    j = 1
    currow = []
    while j < len(trans_values[0]):
        if isinstance(trans_values[i][j], str):
            currow.append(trans_values[i][j])
            j+=1
        else:
            break
    ready_trans.append(currow)
    i+=1

print("\n Очищенные данные:")
print(ready_trans)  

freqItemSet, rules = fpgrowth(ready_trans, 0.5, 0.6)
print("\n Выявленные правила (fp-growth) при минимальной достоверности 60%:")
print('\n'.join(str(value) for value in rules))

freqItemSet, rules = fpgrowth(ready_trans, 0.5, 0.8)
print("\n Выявленные правила (fp-growth) при минимальной достоверности 80%:")
print('\n'.join(str(value) for value in rules))
