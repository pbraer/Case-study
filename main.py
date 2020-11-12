# Case-study #2
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Vasily N. (%)
s1=0.1
s2=0.15
s3=0.25
s4=0.28
s5=0.33
s6=0.35
s7=0.396
nalv=input("Налоговый вычет: ")
# string constants
name_month = ['JAN', 'FAB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
question='Доход:'
annual_income = 0
for month in range(12):
    print('{} {}:'.format(question,name_month[month], end ='' ))
    income = float(input())
    annual_income += income
print(annual_income)
n1 = s1 * (d - d1)
n2 = s1 * (d2 - d1) + s2 * (d - d2)
n3 = s1 * (d2 - d1) + s2 * (d3 - d2) + s3 * (d - d3)
n4 = s1 * (d2 - d1) + s2 * (d3 - d2) + s3 * (d4 - d3) + s4 * (d - d4)
n5 = s1 * (d2 - d1) + s2 * (d3 - d2) + s3 * (d4 - d3) + s4 * (d5 - d4) + s5 * (d - d5)
n6 = s1 * (d2 - d1) + s2 * (d3 - d2) + s3 * (d4 - d3) + s4 * (d5 - d4) + s5 * (d6 - d5) + s6 * (d - d6)
n7 = s1 * (d2 - d1) + s2 * (d3 - d2) + s3 * (d4 - d3) + s4 * (d5 - d4) + s5 * (d6 - d5) + s6 * (d7 - d6) + s7 * (d - d7)
subject=input('Семейный статус? ').lower()
#для одного субъекта
if subject=='один субъект' :
    ////////=='семейная пара' :
    ////////////
elif subject=='родитель-одиночка' :
    /////////