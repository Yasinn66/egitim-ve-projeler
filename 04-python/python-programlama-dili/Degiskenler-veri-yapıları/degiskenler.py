mesaj = input("isiminizi giriniz: ")
print("merhaba " + mesaj)


#   DEGISKEN TANIMLAMA
urunAFiyat = 100
urunBFiyat = 200
kdvOrani = 0.18
print(urunAFiyat + (urunAFiyat * kdvOrani))
print(urunBFiyat + (urunBFiyat * kdvOrani))

urunTop = urunAFiyat + urunBFiyat
print(urunTop + (urunTop * kdvOrani))


#   DEGISKEN TANIMLAMA KURALLARI
sayi1 = 10
sayi2 = 30
# 3sayi = 50  degiskenler sayi ile baslayamaz
sayi3 = 50
# sayi@ = 60 degiskenlerde sadece "_" kullanilabilir
sayi_ = 60

# komut isimleri kullanılmaz örn: True

x, y, z = 1, 2, 3   # tek satırda birden çok degisken atanabilir
a, b, c = 66    # hepsine birden tek degerde atanabilir
