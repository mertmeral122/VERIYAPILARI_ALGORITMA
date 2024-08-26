# len () = bir değişkenin uzunluğunu ele almaktadır.
# type() = bir değişkenin veri tipini vermektedir.
# print()= belirtilen değeri veya değerleri ekrana yazdırır.
# capitalized () = bir dizeyi alır ve sadece ilk harfini büyük harf yapar ,geri kalan harfleri küçük yapar.
# split () = bir dizeyi belirler bir ayırıcıya göre böler ve her bir parçayı liste elemanı olarak döner
# upper () = bir dizedeki bütün harfleri büyük yazdırır.
# input () = Kullanıcıdan veri almak için kullanılır .
# float () = bir değeri ondalıklı sayı tipine dönüştürmek için kullanılır
# int () = bir değeri tam sayı tipine dönüştürmek için kullanılır.
# abs () = negatif sayıların mutlak değerini alır..



#degisken_1=10
#Degisken2=20

#degisken3 =30




x=5
y= "Merhaba Dünya"

print(x)
print(y)

a=10
print(type(a)) #parantez içindeki type paranteze alınmaz.Veri tipini öğrenmek istediğin değişkenini type dan sonra parantez içinde yazmalısın..


b=20.5 # b atanmış bir deger

print(type(b)) # b'nin veri tipini ekrana yazdır.


x=10 #x 10' atanmış bir deger
y=float(x) # y ; x'in float olarak değişim yapması için atanmış bir deger

print(y,type(y)) # y yi yazdır ve y nin veri tipini yazdır

a=12.34 #a atanmış bir deger
b=int(a) # b ataması a atamasının sadece integer'a çevrilmesini istiyor

print(b,type(b)) #b'yi yazdır ve b'nin veri tipini göster

c="Python Programlama"
print(c) #c yi yazdır
print(type(c)) # c' nin veri tipini göster

d=True
e= False
print(d) #d ye tekabül eden ifadeyi yazdır
print(type(e)) # e ye tekabül edenin veri tipini göster



liste=[1,2,3,4,5] #liste atanmış bir deger

print(type(liste)) #liste nin veri tipini göster
print(liste) #liste yi yazdır



demet = (1,2,3,4,5) # demet atanmış bir deger 
print(type(demet)) # Demetin veri tipini göster
print(demet) # demet'i yazdır

notlar ={ #notlar diye bir sözlük oluştuyoruz.NOT:pythonda bir sözlük oluşturuken ilk süslü parantez , eşittirden sonrasına denk gelmeli.
    
    "Ali" : 85, #Alinin notu oluşturuldu
    "Veli": 90, #Veli nin Notu oluşturuldu.
    "Ayşe": 78  #Ayşenin notu oluşturuldu.
}

notlar["Fatma"]=92 #notlar dizisine fatmanın adı ve notu eklendi
notlar["Ali"]=88 # Alinin notu güncellemesi
print(notlar)

print(notlar.keys()) #Bu kodun çıktısı :: 'Ali' , 'Veli' , 'Ayse' , 'Fatma' ##KEYS  string ifadeler
print(notlar.values())#Bu kodun çıktısı :: 88,       90,      78,      92 ##VALUES SAYISAL DEĞERLER
print(notlar.items()) #Bu kodun çıktısı :: ('Ali', 88), ('Veli', 90), ('Ayşe', 78), ('Fatma', 92) ##ITEMS = VALUES + KEYS 

kodyazanlar={"Ahmet","Mehmet","Ayşe"} #Atanmış Bir Liste
kodyazmayanlar={"Ayşe","Fatma","Veli"}#Atanmış Bir Liste

ortak=kodyazanlar.intersection(kodyazmayanlar)#Atanmış kaç liste var ise ; o listelerdeki aynı değeri bulup yazdırmak için "intersection" kullanılır
print("Kafasına göre takılan öğrencilerin Listesi :",ortak)#Her 2 listede aynı değere karşılık gelen kişiyi yazdır


kod_yazmayan = kodyazmayanlar.difference(kodyazanlar) #difference::farklılığı bulur
print("Kod çalışması yapmayan öğrenci Listesi :",kod_yazmayan)

imza_liste=kodyazanlar.union(kodyazmayanlar)#union:2 listenin toplam elemanlarını yazdırır.
print("İmza Atacak Öğrenci Listesi :.",imza_liste)


giris =input("Bir Sayı Giriniz : ")

try:
     num =float(giris)
     print(f"Girilen sayı : {num}, tipi : {type(num)}," , abs(num))

except ValueError:
     print("Geçersiz Veri Girdiniz.")    





import random

rastgele_float =random.random()
print("Rastgele Deger :",rastgele_float)


import random

rastgele_sayi = random.randint(1,100)
print("Rastgele Deger :",rastgele_sayi)
"""
"""
x=10
if x>5:
     print("x , 5'ten büyüktür")

x=3
if x >5:
     print("x,5ten büyüktür")
else :
     print("x,5 ten Küçüktür")     
"""

"""
x=8

if x > 10 :
   print("x,10'dan büyüktür")

elif x > 5 :
   print("x,5ten büyüktür ama 10 dan küçük veya eşittir") 

else :
   print("x,5ten  küçük veya eşittir")




yas =20 

if yas < 18:
   print("Reşit Değilsiniz ")

elif yas < 21:
   print("Reşitsiniz ama İçecek Alamazsınız")

else :
   print("İçecek Satın Alabilirsiniz")   



sayi = int(input("Bir sayı gir::"))


if sayi > 0 :
   print("Sayı Pozitiftir")

elif sayi < 0 :
   print("Sayı Negatiftir")

else :
   print("Sayı Sıfıra Eşittir")   
"""

   #while ketil mantığı gibidir.Ketıllarda ısı azaldıkça otomatik sistem çalışmaya başlar
   #for uzay mekiği mantığı gibidir.Belirtilen hedefe odaklanıp belirlenen artış-azalış doğrultusunda çalışır.


"""
for i in range(5): #for i in python'da döngünün yazlış biçimidir.

   print(i)


liste=["elma","ekmek","süt","peynir"]

for alinacaklar in liste:
      print(alinacaklar)




notlar = [85,92,78,90,88]

toplam=0
for sayi in notlar: 
 toplam+=sayi

ortalama=toplam/len(notlar) # len komutu; "NOTLAR adındaki dizinin kaç elemanı var ise..." demektir.
print(f"Not  ORTALAMASI ::",ortalama)


 #while dögüsü örneği
i=0

while i < 5:
    print(i)
    i+=1



kullanici_girdisi=int(input("Bir sayı giriniz"))

i=0
while i <= kullanici_girdisi :
   print(i)
   i+=1




for i in range(5):
    if i==3:  
        break
    print(i)
    
for i in range(5):
    if i==3:  
        continue
    print(i)

    
    

matris=[
    [1,2,3],
    [4,5,6],
    [7,8,9],

]
for x in matris:
    for y in x:
        print(y)
        

    



while True:
    try: 
        gelenbilgi=int(input("Bir sayı Girin:"))
        break
    except ValueError:
        print("Lütfen Geçerli Bir sayı Giriniz !")

i=0
while i<=gelenbilgi:
    print(i)
    i+=1




toplam_ucret = 1000
while toplam_ucret > 0:
    try:
        cekilen_tutar = int(input("Çekmek istenilen miktarı Girin:"))
        if cekilen_tutar > toplam_ucret:
            print("Yetersiz Bakiye! ")
            bilgi=input("İşleme Devam etmek ister misiniz ? (e/h)").lower()
            if bilgi == "h":
                print("İşlem Sonlandırıldı.")
                break
        else:
             toplam_ucret -= cekilen_tutar
             print(f"Kalan Bakiye::", {toplam_ucret})
        if toplam_ucret == 0:
             print("Bakiye Tükendi.")
             break
    except ValueError:
        print("Lütfen geçerli bir sayı Girin !")   
      


"""
