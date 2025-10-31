thislist = ["apple", "banana", "cherry"]#LİSTELEME TÜRLERİ
print(thislist[1])# 0 dan başlar 1 ikinci olur

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])#SONDAN GERİYE DOĞRU SAYAR

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])#2 VE 5 DAHİL O SAYILARIN ARASINDAKİ İTEMLERİ YAZDIRIYOR

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])#SIFIRDAN 4 TANESİNİ YAZDIRIYOR

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])#iKİDEN İTİBAREN YAZDIRIYOR

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])#SONDAN GERİYE DOĞRU 1. VE 4. DAHİL İKİ İTEM ARASINI YAZDIRIYOR

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")#LİSTENİN İÇİNDE APPLE VARSA EVET VAR YAZDIRIYOR ÖYLEYSE DEĞİLSE GİBİ

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)#YERİNE YAZDIRMA BANANA YERİNE BLACKCURRANT YAZDIRIYOR

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)# İKİ İTEMİ YERİNE YAZDIRMA

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)# İKİ İTEMİ YERİNE YAZDIRMA

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)#FAZLA YAZDIRMAK İSTESENDE EĞER LİSTEDE YETERLİ İTEM YOKSA YAZDIRMIYOR

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)#BU DA YERİNE YAZDIRIYOR

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)#LİSTEYE EKLEME SONUNA EKLİYOR AMA

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)#1. OLARAK LİSTEYE YAZDIRIYOR(LİSTE 0 DAN BAŞLAR İLK İTEM 0 LA BAŞLAR)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)#İKİ LİSTENİN BİRLEŞTİRME SONDAN EKLİYOR

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)#YİNE LİSTEYE EKLEME

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)#LİSTEDEN SİLME

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)#BİR TANESİNİ SİLİYOR

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)#İKİNCİSİNİ SİLDİRİYOR

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)#SON İTEMİ LİSİYOR

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)#İLK İTEMİ SİLİYOR

thislist = ["apple", "banana", "cherry"]
del thislist#LİSTEYİ KOMPLE SİLİYOR

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)#İÇİNİ BOŞ BIRAKIYOR [] BUNU YAZDIRIYOR

thislist = ["apple", "banana", "cherry"]