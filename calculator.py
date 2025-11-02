sayi=(input("Bir sayı giriniz: "))
sayi=float(sayi)
sayi1=(input("İkinci Sayıyı Giriniz: "))
sayi1=float(sayi1)
islem=input("Yapmak İstediğiniz işlemi seçiniz(+,-,*,/,^):")
while islem not in ['+','-','*','/','^']:
    print("Geçersiz işlem Seçtniz.Lütfen Tekrara Deneyiniz")
    islem=input("Yapmak İstediğiniz işlemi seçiniz(+,-,*,/,^):")
if islem=='+':
    sonuc =sayi+sayi1
    print(f"{sayi}+{sayi1}={sonuc}")
elif islem=='-':
    sonuc=sayi-sayi1
    print(f"{sayi}-{sayi1}={sonuc}")
elif islem=='*':
    sonuc=sayi*sayi1
    print(f"{sayi}*{sayi1}={sonuc}")
elif islem=='/':
    if sayi1==0:
        print("Sonuç Tanımsızdır(Syntax Error)")
    else:
        sonuc=sayi/sayi1
        print(f"{sayi}/{sayi1}={sonuc}")
elif islem=='^':
    sonuc=sayi**sayi1
    print(f"{sayi}**{sayi1}={sonuc}")
