# 1-) girilen 2 sayıdan hangisi büyüktür
#kullanıcıdan 2 vize ve final  notu alıp ortalamasını hesaplayın ve 
# ve ort 50den büyükse geçti yazdırın değilse kaldı yazdırın

#parola ve email bilgisini isteyip doğruluğunu kontrol edin. doğru ise giriş başarılı yazdırın yanlış ise giriş başarısız yazdırın


input1 = int(input("Birinci sayıyı girin: "))
input2 = int(input("İkinci sayıyı girin: "))

if input1 > input2:
   print("Birinci sayı daha büyüktür.")
elif input2 > input1:
  print("İkinci sayı daha büyüktür.")
else:
    print("İki sayı eşittir.")

vize=float(input("Vize notunu girin: "))
final=float(input("Final notunu girin: "))
ortalama=(vize*0.4)+(final*0.6)
if ortalama>=50:
    print("Geçti")
else:
        print("Kaldı")






parola = input("Parolanızı girin: ")
email = input("Email adresinizi girin: ")
if parola == "1234" and email == "abcd@gnail.com":
    print("Giriş başarılı")
else:
    print("Giriş başarısız")