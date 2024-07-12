# a = input()

# b = a[::-1]
# lst = []
# lst_new = []

# for char in b:
#     lst.append(char)

# n = 1

# if len(lst) <= 3:
#     print(a)
# else:
#     for i in range(len(lst)):
#         if n % 3 != 0:
#             lst_new.append(lst[i])
#             n += 1
#         else:
#             lst_new.append(lst[i])
#             lst_new.append(',')
#             n += 1

#     c = ''

#     for i in range(len(lst_new)):
#         c = c + lst_new[i]

#     c = c[::-1]
#     if c[0] == ',':
#         print(c[1:])
#     else:
#         print(c)


n = int(input())
print(f'{n:,}')
