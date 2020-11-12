# string constants
name_month = [JAN, FAB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC]
QUESTION = 'Доход: '
annual_income = 0
for month in range(12):
    print('{} {}:'.format(QUESTION, name_month[month], end ='')
    income = float(input())
    annual_income += income
print(annual_income)
nalv = float(input())
d = annual_income - nalv

n1 = s1 * (d - d1)
n2 = s1 * (d2 - d1) + s2 * (d - d2)
n3 = s1 * (d2 - d1) + s2 * (d3 - d2) + s3 * (d - d3)
n4 = s1 * (d2 - d1) + s2 * (d3 - d2) + s3 * (d4 - d3) + s4 * (d - d4)
n5 = s1 * (d2 - d1) + s2 * (d3 - d2) + s3 * (d4 - d3) + s4 * (d5 - d4) + s5 * (d - d5)
n6 = s1 * (d2 - d1) + s2 * (d3 - d2) + s3 * (d4 - d3) + s4 * (d5 - d4) + s5 * (d6 - d5) + s6 * (d - d6)
n7 = s1 * (d2 - d1) + s2 * (d3 - d2) + s3 * (d4 - d3) + s4 * (d5 - d4) + s5 * (d6 - d5) + s6 * (d7 - d6) + s7 * (d - d7)
#для супружеской пары
d1 = 0
d2 = 18151
d3 = 73801
d4 = 148851
d5 = 226851
d6 = 405101
d7 = 457601

if d1 < d < d2 - 1:
    print(n1)
elif d2 < d < d3 - 1:
    print(n2)
elif d3 < d < d4 - 1:
    print(n3)
elif d4 < d < d5 - 1:
    print(n4)
elif d5 < d < d6 - 1:
    print(n5)
elif d6 < d < d7 - 1:
    print(n6)
elif d7 < d:
    print(n7)