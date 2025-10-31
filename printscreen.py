print("Hello")#TEK ÇİFT TIRNAK FARKETMİYOR
print('Hello')

print("It's alright")#TIRNAKLA İLGİLİ BİR SIKINTI YOK
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)#TIRNAĞI YAZDIRMIYOR

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)#ÜÇ TIRNAK KULLANINCA TIRNAKLARI YAZDIRMIYOR

a =''' Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)#ÜÇ TEK TIRNAK KULLANINCA TIRNAKLARI YAZDIRMIYOR

a = "Hello, World!"
print(a[1])#h=0 e=1 birinci harfi yazdırıyor
b="YAĞMUR"
print(b[3])# 0 dan başlıyorrrr

b = "Hello, World!"
print(b[2:5])#2. ve 5. harfleri yazdırıyor

b = "Hello, World!"
print(b[:5])#5 harfi yazdırıyor

b = "Hello, World!"
print(b[2:])#2. harften itibaren başlıyor yazdırmaya 

b = "Hello, World!"
print(b[-5:-2])# - LERİ TERSTEN SÖYLE

a = "Hello, World!"
print(a.upper())#CAPSLOCKLU YAZDIRIYOR

a = "Hello, World!"
print(a.lower())#HEPSİNİ KÜÇÜK HARFLİ YAZDIRIYOR

a = " Hello, World! "
print(a.strip()) #DÜZELTİYOR

a = "Hello, World!"
print(a.replace("H", "J"))#HARFLERİN YERİNİ DEĞİŞTİRİYOR

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] KÖŞELİ PARANTEZLİ YAZDIRIYOR