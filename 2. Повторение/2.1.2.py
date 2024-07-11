weight = float(input())
height = float(input())

index = weight / (height * height)
# print(index)

if 18.5 <= index <= 25:
    print('Оптимальная масса')
elif index < 18.5:
    print('Недостаточная масса')
elif index > 25:
    print('Избыточная масса')
