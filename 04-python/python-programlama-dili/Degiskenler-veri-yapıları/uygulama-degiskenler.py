musteriAd = "Yasin"
musteriSoyad = "Başer"
musteriTelefon = "09874562343"
musteriEmail = "sdflg@gmail.com"
musteriAdres = "Yozgat"

kdvOrani = 0.18

urun1Ad = "mouse"
urun1Fiyat = 550

urun2Ad = "klavye"
urun2Fiyat = 650

urun3Ad = "laptop"
urun3Fiyat = 55000

urunTop = urun1Fiyat + urun2Fiyat + urun3Fiyat

print("Toplam ücret:")
print(urunTop)
print("Toplam kdvli ücret: " + str(urunTop + (urunTop * kdvOrani)))
