a = input()
len_a = len(a)

cost = len(a) * 60
b = cost // 100
c = cost - b * 100

print(f'{b} р. {c} коп.')
