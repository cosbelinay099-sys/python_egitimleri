# 1-kullanıcıdan isim ,yaş ve eğitim bilgilerini isteyip ehliyet alıp alamayacağını kontrol eden bir program yazınız.ehliyet alma koşulu 18 yaşından büyük ve eğitim durumu lise veya üniversite olmalıdır.

#2- trafiğe çıkış tarihi alınan bir servis zamanını aşağıdaki bilgilere göre hesaplayınız
#1.bakım => 1 yıl
#2.bakım => 2 yıl   
#3.bakım => 3 yıl

import datetime


name = input("Lütfen isminizi giriniz: ")
age = int(input("Lütfen yaşınızı giriniz: "))
eğitim = input("Lütfen eğitim durumunuzu giriniz (lise/üniversite): ")

if age >= 18 and (eğitim == "lise" or eğitim == "üniversite"):
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet alamazsınız.")







tarih = input("Lütfen trafiğe çıkış tarihinizi giriniz (YYYY-AA-GG formatında): ")
tarih = tarih.split("/")

trafigeCikis=datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
simdi=datetime.datetime.now()
fark=simdi-trafigeCikis
print(fark)
days=fark.days

if days <= 365:
    print("1. servis aralığı.")
elif days>365 and days <= 730:
    print("2. servis aralığı.")
elif days>730 and days <= 1095:
    print("3. servis aralığı.")
else:
    print("Geçersiz tarih.")