#########1
# print("Это приложение позволяет узнать кратно или некратно n число от 1 до 100.")
# a = float(input('Введите число от 1 до 100:'))
# if a < 1:
#     print("Ошибка")
# if a > 100:
#     print("Ошибка")
# elif a % 3 == 0 and a % 5 == 0:
#     print("Fizz Buzz")
# elif a % 3 == 0:
#     print("Fizz")
# elif a % 5 == 0:
#     print("Buzz")
# else:
#     print(a)
#####2
# print("Это приложение позволяет узнать степень от 0 до 7 .")
# a = int(input('введите число:'))
# for i in range(8):
#      print(f"{a} ^ {i} = {a ** i}")
##############3
# print("Это приложение позволяет определить стоимость оператора MTS Билайн Мегафон.")
#
# oper = str(input('выберете любой оператор Летай, Билайн или Мегафон :'))
# a = float(input('ВВедите стоимость оператора:'))
# if oper == "Летай":
#     print(f'Резултат вычесления минута разговора 1руб : {a * 1}')
# elif oper == "Билайн":
#     print(f'Резултат вычесления минута разговора 2руб: {a * 2}')
# elif oper == "Мегафон":
#     print(f'Резултат вычесления минута разговора 3руб: {a * 3}')
############################4

man = 200

man2 = 200

man3 = 200
print("Это приложение позволет узнать работника месяца ")
a = int(input("уровень продаж 1 менеджера:"))

b = int(input("уровень продаж 2 менеджера:"))

c = int(input("уровень продаж 3 менеджера:"))

def sales_verification(manager, sales):

   if sales <= 500:

       temp = sales * 0.03

       manager += temp

   elif a <= 1000:

       temp = sales * 0.05

       manager += temp

   else:

       temp = sales * 0.08

       manager += temp

   return manager

man = sales_verification(man, a)

man2 = sales_verification(man2, b)

man3 = sales_verification(man3, c)

num = [man, man2, man3]

temp = max(num)

for a in range(0,3):

   if num[a] == temp:

       num[a] += 200

   print(num[a], "мененджер", a+1)



man = 200

man2 = 200

man3 = 200

a = int(input(" премия 1 мененджер:"))

b = int(input(" премия 2 мененджер:"))

c = int(input(" премия 3 мененджер:"))

if a <= 500:

   temp = a * 0.03

   man += temp

elif a <= 1000:

   temp = a * 0.05

   man += temp

else:

   temp = a * 0.08

   man += temp

if b <= 500:

   temp = b*0.03

   man2+= temp

elif b <= 1000:

   temp = b * 0.05

   man2 += temp

else:

   temp = b * 0.08

   man2 += temp

if c <= 500:

   temp = c * 0.03

   man3 += temp

elif c <= 1000:

   temp = c * 0.05

   man3 += temp

else:

   temp = c * 0.08

   man3 += temp

# Проверка у кого больше зарплата

if man > man2:

   if man > man3:

       man += 200

   elif man < man3:

       man3 += 200

else:

   if man2 > man3:

       man2+= 200

   elif man2 < man3:

       man3 += 200

print(man, "1 мененджер\n")

print(man2, "2 мененджер\n")

print(man3, "3 мененджер\n")







