

# Liste tanımlama
dizi = [2, 3, 5, 6, 8, 11, 14]

# Çift sayıları tutmak için boş liste
numaralistesi = []

# For ve if ile çift sayıları bulma
for i in dizi:
    if i % 2 == 0:
        numaralistesi.append(i)

print(f"Listede bulunan çift sayılar: {numaralistesi}")
print("Adet çift sayı", len(numaralistesi), "bulunmaktadır !!!")





dizi = ["elma", "muz", "çilek", "su", "cikolata"] # Malzeme Listesi

aranacak_urun = "muz" # Aranacak eleman

if aranacak_urun in dizi:
    print(aranacak_urun, "liste içerisinde mevcut.")
else:
    print(aranacak_urun, "liste içerisinde mevcut değil.")



"""


    
dizi = ["elma", "muz", "çilek", "su", "cikolata"] # Malzeme Listesi

aranacak_urun = input("Aranacak Ürün Nedir? ") # Aranacak eleman

if aranacak_urun in dizi:
    print(aranacak_urun, "liste içerisinde mevcut.")
else:
    print(aranacak_urun, "liste içerisinde mevcut değil.")


"""


    # Matematiksel Toplama İşlemi

def toplama(a, b):
    return a + b

# Fonksiyonu çağırarak kullanma
sonuc = toplama(5, 3)
print(f"Toplama sonucu: {sonuc}")
print("Toplama sonucu: ",sonuc)




# Liste Elemanlarını Toplama
sayilar = [1, 2, 3, 4, 5]

def liste_toplam(liste):
    toplam = 0
    for eleman in liste:
        toplam += eleman
    return toplam

# Fonksiyonu çağırarak kullanma
sonuc = liste_toplam(sayilar)
print("Toplama sonucu: ",sonuc)     



# Fibonacci Dizisi Hesaplama

def fibonacci(n):
    if n <= 0:
        return "Geçersiz giriş"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Fonksiyonu çağırarak kullanma
n = 7
sonuc = fibonacci(n)
print(f"Fibonacci dizisinin {n}. elemanı: {sonuc}")





# EBOB be EKOK Bulma

def ebob(a, b):
    while b:
        a, b = b, a % b
    return a

def ekok(a, b):
    return a * b // ebob(a, b)

# Kullanıcıdan iki sayı al
Bir_Sayi = int(input("Birinci sayıyı girin: "))
iki_Sayi = int(input("İkinci sayıyı girin: "))

# EBOB ve EKOK hesapla
ebob_sonuc = ebob(Bir_Sayi, iki_Sayi)
ekok_sonuc = ekok(Bir_Sayi, iki_Sayi)

# Sonuçları göster
print("Sayılarının EBOB'u: ", ebob_sonuc)
print("Sayılarının EKOK'u: ", ekok_sonuc)





# Asal Sayı Kontrolü ve Asal Sayılar Listesi
def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    return True

def asal_sayilar(aralik):
    asal_listesi = []
    for sayi in range(2, aralik + 1):
        if asal_mi(sayi):
            asal_listesi.append(sayi)
    return asal_listesi

# Fonksiyonları çağırarak kullanma
aralik = 50
sonuc = asal_sayilar(aralik)
print("1 ile", aralik, " arasındaki asal sayılar: ", sonuc) 




buzdolabi = { # Buzdolabındaki meyveler ve miktarlarını tutan sözlük
    "elma": 5,    # 5 kilo elma
    "muz": 3,     # 3 kilo muz
    "kiraz": 2,   # 2 kilo kiraz
    "hurma": 4    # 4 kilo hurma
}

def buzdolabi_durumu_yazdir(): # Mevcut buzdolabı durumunu yazdıran fonksiyon
    print("Buzdolabındaki meyve miktarları:")
    for meyve, miktar in buzdolabi.items():
        print(f"{meyve}: {miktar} kilo")
    print("\n")


def meyve_tuket(meyve, miktar): # Meyveden belirtilen miktarı düşen fonksiyon
    if meyve in buzdolabi:
        if buzdolabi[meyve] >= miktar:
            buzdolabi[meyve] -= miktar
            print(f"{miktar} kilo {meyve} tüketildi.")
            if buzdolabi[meyve] == 0:
                print(f"{meyve} kalmadı. {meyve} almalısın!")
                yeni_miktar = float(input(f"Kaç kilo {meyve} almak istersiniz?: "))
                buzdolabi[meyve] = yeni_miktar
                print(f"{meyve} buzdolabına {yeni_miktar} kilo olarak eklendi.")
        else:
            print(f"Buzdolabında yeterli {meyve} yok. Mevcut miktar: {buzdolabi[meyve]} kilo.")
    else:
        print(f"Buzdolabında {meyve} bulunmuyor.")

print("Buzdolabı Uygulaması") # Uygulama başlangıc noktası
buzdolabi_durumu_yazdir()

while True: #Ana döngü tanımlaması
    # Kullanıcıdan meyve ve miktar bilgisi alma
    meyve = input("Hangi meyveyi tüketmek istersiniz? (Çıkmak için 'exit' yazın): ").lower()

    if meyve == 'exit':
        print("Uygulama sonlandırılıyor.")
        break

    miktar = float(input(f"Kaç kilo {meyve} tüketmek istersiniz?: "))

    meyve_tuket(meyve, miktar)     # Meyve tüketme işlemi

    buzdolabi_durumu_yazdir()  # Güncellenmiş buzdolabı durumunu yazdırma



    
# Diyet listesindeki besinler ve kalorilerini tutan sözlük (Adet başına kalori)
diyet_listesi = {
    "elma": {"miktar": 5, "kalori": 52},    # 1 adet elma: 52 kalori
    "muz": {"miktar": 3, "kalori": 89},     # 1 adet muz: 89 kalori
    "kiraz": {"miktar": 2, "kalori": 50},   # 1 adet kiraz: 50 kalori
    "hurma": {"miktar": 4, "kalori": 282}   # 1 adet hurma: 282 kalori
}

# Mevcut diyet listesini yazdıran fonksiyon
def diyet_listesi_yazdir():
    print("Diyet listesindeki besin miktarları ve kalorileri:")
    for besin, bilgi in diyet_listesi.items():
        print(f"{besin}: {bilgi['miktar']} Adet, Toplam Kalori: {bilgi['miktar'] * bilgi['kalori']} kalori")
    print("\n")

# Besinden belirtilen miktarı düşen ve kalori hesaplayan fonksiyon
def besin_tuket(besin, miktar):
    if besin in diyet_listesi:
        if diyet_listesi[besin]["miktar"] >= miktar:
            diyet_listesi[besin]["miktar"] -= miktar
            tuketilen_kalori = miktar * diyet_listesi[besin]["kalori"]
            print(f"{miktar} kilo {besin} tüketildi. Alınan kalori: {tuketilen_kalori} kalori.")
            if diyet_listesi[besin]["miktar"] == 0:
                print(f"{besin} kalmadı. {besin} almalısın!")
                yeni_miktar = float(input(f"Kaç kilo {besin} almak istersiniz?: "))
                diyet_listesi[besin]["miktar"] = yeni_miktar
                print(f"{besin} diyet listesine {yeni_miktar} kilo olarak eklendi.")
        else:
            print(f"Diyet listesinde yeterli {besin} yok. Mevcut miktar: {diyet_listesi[besin]['miktar']} kilo.")
    else:
        print(f"Diyet listesinde {besin} bulunmuyor.")

print("Diyet Uygulaması") # Uygulama başlangıcı
diyet_listesi_yazdir()

while True:     # Kullanıcıdan besin ve miktar bilgisi alma

    besin = input("Hangi besini tüketmek istersiniz? (Çıkmak için 'exit' yazın): ").lower()

    if besin == 'exit':
        print("Uygulama sonlandırılıyor.")
        break

    miktar = float(input(f"Kaç kilo {besin} tüketmek istersiniz?: "))

    besin_tuket(besin, miktar)     # Besin tüketme işlemi

    diyet_listesi_yazdir()     # Güncellenmiş diyet listesini yazdırma
     
     
"""
