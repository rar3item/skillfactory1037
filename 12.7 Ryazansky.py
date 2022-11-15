per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposits = []
money = int(input())
for each in per_cent:
    deposits.append(int(per_cent[each] * money * 0.01))
print(deposits)
print('Максимальная сумма которую вы можете заработать - ' + str(max(deposits)))
