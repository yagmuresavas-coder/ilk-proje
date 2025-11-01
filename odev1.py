
kullanici_adi = input("Kullanıcı Adı Giriniz:")
if not kullanici_adi: 
    print("Kullanıcı adı boş bırakılamaz.")
elif len(kullanici_adi) < 5:
    print("Kullanıcı Adı En Az 5 Karakter Olmalı")
else:  
    ilk_harf = kullanici_adi[0] 
    if ilk_harf == '?' or ilk_harf == '!' or ilk_harf == ',' or ilk_harf == '*':
        print(f"Kullanıcı adı '{ilk_harf}' karakteri ile başlayamaz.")
    else:
        print("Kullanıcı Adı Geçerli")
        sifre=input("Şifre Giriniz:")
        if len(sifre)<6:
            print("Şifre En Az 6 Karkter Olmalı")
        else:
            sifre_ilk_harf=sifre[0]
            sifre_son_harf=sifre[-1]
            if sifre_ilk_harf==sifre_son_harf:
                print("Şifrenin ilk ve son harfleri aynı olamaz.")
            else:
                if sifre in '@':
                    print ("Şifreniz Geçerli")
                else:
                    print("Şifreniz Geçersiz @ karakteri içermelidir.")