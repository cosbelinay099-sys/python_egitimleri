
#kişinin ad,kilo ve boy bilgilerini alarak vücut kitle indeksini hesaplayan ve kişinin hangi gruba girdiğini belirleyen bir program yazınız.
#formül:(kilo/(boy*boy))
# aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#0-18.4  =>zayıf
#18.5 - 24.9 =>normal
#25.0 - 29.9 =>fazla kilolu
#30.0 - 34.9 =>obez

name = input("Adınızı giriniz: ")
kg= float(input("Kilonuzu giriniz: "))
hg = float(input("Boyunuzu giriniz: "))

indeks = kg / (hg ** 2)
zayıf= (indeks >= 0) and (indeks <= 18.4)
normal = (indeks >= 18.5) and (indeks <= 24.9)
fazla_kilolu = (indeks >= 25.0) and (indeks <= 29.9)
obez = (indeks >= 30.0) and (indeks <= 34.9)
print(f'{name} kilo indeksiniz: {indeks} ve kilo durumunuz zayıf: {zayıf}')
print(f'{name} kilo indeksiniz: {indeks} ve kilo durumunuz normal: {normal}')
print(f'{name} kilo indeksiniz: {indeks} ve kilo durumunuz fazla kilolu: {fazla_kilolu}')
print(f'{name} kilo indeksiniz: {indeks} ve kilo durumunuz obez: {obez}')

#girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
input_number = float(input("Bir sayı giriniz: "))
print("Girilen sayı 0-100 arasında mı?", 0 <= input_number <= 100)


#girilen 3 sayıyı büyüklük olarak sıralayan bir program yazınız.
sayi1=int(input("Birinci sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))  
sayi3=int(input("Üçüncü sayıyı giriniz: "))
print("Sıralama: ", sorted([sayi1, sayi2, sayi3], reverse=True))