def kontrol(kullanici,sifre):
    if kullanici=="admin" and sifre=="123456":
        return True
    else:
        return False
kullanici=input("Kullanıcı Adınızı Giriniz:")
sifre=input("Şifreniz:")
sonuc=kontrol(kullanici,sifre)
if sonuc==True:
    print("Doğru Girdiniz")
else:
    print("Kullanıcı adı veya şifre hatalı")