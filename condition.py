txt = "The best things in life are free!"
print("free" in txt) #CÜMLENİN İÇİNDE O KELİMELER VARMI YOKMU DİYE KONTROL ETTİRİYOR

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")#FREE KELİMESİ İÇİNDE VARSA YES YAZDIR DEDİLER

  txt = "The best things in life are free!"
print("expensive" not in txt)#YİNE KELİME KONTROL ETTTİRİYOR EĞER KELİME İÇİNDE VARSA TRUE YOKSA FALSE ONA GÖRE İF ELSE DENKLEMİ

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")#EĞR VARSA VAR YOKSA YOK YAZDIRIYOR

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

a = 33
b = 200

if b > a:
  pass

day = 7
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

day = 4
match day:#günleri de haftaya entegre
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")

i = 1 #1 DEN 5 E KADAR TEKER TEKER ARTAN SİSTEM
while i < 6:
  print(i)
  i += 1
'''
i = 1 # 6 YI YAZDIRMIYOR 5 TEN SONRA BİRDAHA BAŞTAN BAŞLATIRYOR BU SEFER 3 E KADAR
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

  i = 0
while i < 6:
  i += 1
  if i == 3:
    break
  print(i)
 '''
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

def greet():
  print("Hello from a function")

def my_function():
  print("Hello from a function")

my_function()