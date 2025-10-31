#değişken tanımlamanın 3 yolu var
#1.YOL bu düz olan
x=5
y="YAGMUR"
print(x)
print(y)

#2.YOL
a=str(3) #yazı olarak atadık 3 ü
b=int(3) #sayı olarak atadık3 ü
c=float(3) #küsüratlı olarak atadık 3 ü

#3.YOL bu değişken tanımlamaıyo da değişkenin türünü yazdırıyor
e=5
f="YAĞMUR"
print(type(e))
print(type(f))

# string tütünde tanımlarken tek çift tırnakta sıkıntı yok ancakk python 
#case-sensetive olduğu için büyük a ve küçük a farklı değişkenler oluyorrr
#nasıl deiğşen tanımlanabilir nasıl tanımlanamaz
degisken="YAGMUR"
degi_sken="YAGMUR"

# SİTE BUNU KABUL EDİYOR AMA VS CODE ETMİYOR O YÜZDEDN KULLANMIYORUZ_degi_sken="YAGMUR" 
degiSken="YAGMUR"
DEGİSKEN="YAGMUR"
degisken5448="YAGMUR"
#BİR KOD SATIRINDA BİRDEN FAZLA DEĞİŞKEN TANIMLAMA

#1.YOL
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#2.YOL 3 FARKLI DEĞİŞKENE AYNI DEĞERE ATAMA
x = y = z = "Orange"
print(x)
print(y)
print(z)

#3. YOL LİSTELEMME YÖNTEMİ
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#EKRANA DEĞİŞKEN YAZDIRMA
x="AAAAAAAA"
print(x)
x="GEÇMİŞ"
y="ŞİMDİ"
z="GELECEK"
A=5
C=4
print(x,y,z)#bu boşluklu yazdırıyor
print(x+y+z)#bu bitişik yazdırıyor
print(A+C)#matematik hesabı ama değerler int türündeyse yoksa biri string ve int olursa hata veriyor
x = "Hello World"	                            #str	
x = 20	                                        #int	
x = 20.5	                                    #float	
x = 1j	                                        #complex	
x = ["apple", "banana", "cherry"]	            #list	
x = ("apple", "banana", "cherry")	            #tuple	
x = range(6)	                                #range	
x = {"name" : "John", "age" : 36}           	#dict	
x = {"apple", "banana", "cherry"}	            #set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	                                    #bool	
x = b"Hello"	                                #bytes	
x = bytearray(5)	                            #bytearray	
x = memoryview(bytes(5))	                    #memoryview	
x = None	                                    #NoneType	

x = str("Hello World")	                        #str	
x = int(20)	                                    #int	
x = float(20.5)	                                #float	
x = complex(1j)	                                #complex	
x = list(("apple", "banana", "cherry"))	        #list	
x = tuple(("apple", "banana", "cherry"))	    #tuple	
x = range(6)	                                #range	
x = dict(name="John", age=36)	                #dict	
x = set(("apple", "banana", "cherry"))	        #set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	                                    #bool	
x = bytes(5)	                                #bytes	
x = bytearray(5)	                            #bytearray	
x = memoryview(bytes(5))	                    #memoryview
import random

print(random.randrange(1, 146450))#bu iki değer arasında rastgele bir değer belirliyor

x = int(1)   
y = int(2.8) 
z = int("3")
#BÜTÜN DEĞERLERİ İNTE ÇEVİRİYOR

x = float(1)    
y = float(2.8)   
z = float("3")   
w = float("4.2")
#BÜTÜN DEĞERLERİ FLOATA ÇEVİRİR

x = str("s1") 
y = str(2)    
z = str(3.0)
#BÜTÜN DEĞERLERİ STRİNGE ÇEVİRİR