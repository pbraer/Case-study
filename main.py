# Case-study #2
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Novoselov V. (%)

subject = input('Семейный статус? ').lower()

if subject == 'один субъект' or 'субъект':
    d1 = 0
    d2 = 9076
    d3 = 36901
    d4 = 89351
    d5 = 186351
    d6 = 405101
    d7 = 406751

elif subject == 'супружеская пара' or 'семейная пара':
    d1 = 0
    d2 = 18151
    d3 = 73801
    d4 = 148851
    d5 = 226851
    d6 = 405101
    d7 = 457601

elif subject == 'родитель-одиночка' or 'родитель одиночка':
    d1 = 0
    d2 = 12951
    d3 = 49401
    d4 = 127551
    d5 = 206601
    d6 = 405101
    d7 = 432201

name_month = ['JAN', 'FAB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
question = 'Revenue for'
annual_income = 0
for month in range(12):
    print('{} {}:'.format(question,name_month[month], end=''))
    income = float(input())
    annual_income += income
annual_income = int(annual_income)
nalv = int(input("Налоговый вычет: "))
d = annual_income-nalv

s1 = 0.1
s2 = 0.15
s3 = 0.25
s4 = 0.28
s5 = 0.33
s6 = 0.35
s7 = 0.396

n1 = s1 * (d - d1)
n2 = s1 * (d2 - d1) + s2 * (d - d2)
n3 = s1 * (d2 - d1) + s2 * (d3 - d2) + s3 * (d - d3)
n4 = s1 * (d2 - d1) + s2 * (d3 - d2) + s3 * (d4 - d3) + s4 * (d - d4)
n5 = s1 * (d2 - d1) + s2 * (d3 - d2) + s3 * (d4 - d3) + s4 * (d5 - d4) + s5 * (d - d5)
n6 = s1 * (d2 - d1) + s2 * (d3 - d2) + s3 * (d4 - d3) + s4 * (d5 - d4) + s5 * (d6 - d5) + s6 * (d - d6)
n7 = s1 * (d2 - d1) + s2 * (d3 - d2) + s3 * (d4 - d3) + s4 * (d5 - d4) + s5 * (d6 - d5) + s6 * (d7 - d6) + s7 * (d - d7)

if d1 < d < d2-1:
    print(round(n1,2))
elif d2 < d < d3 - 1:
    print(round(n2,2))
elif d3 < d < d4 - 1:
    print(round(n3, 2))
elif d4 < d < d5 - 1:
    print(round(n4, 2))
elif d5 < d < d6 - 1:
    print(round(n5, 2))
elif d6 < d < d7 - 1:
    print(round(n6, 2))
elif d7 < d:
    print(round(n7, 2))