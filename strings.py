name='Belinay'
surname='Coşkun'
age=20

greeting='My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old'
#greeting=türkçede selamlamadır.
#print(greeting)
print(greeting[3])  #cümledeki 3.karakteri temsil eder boşluklar da sayılıyor
print(greeting[8])
print(len(greeting))  #cümledeki karakter sayısını verir
print(greeting[0:10])  #cümledeki 0-10 arasındaki karakterleri verir
print(greeting[10:])  #cümledeki 10. karakterden sonrasını verir
print(greeting[:10])  #cümledeki 0-10 arasındaki karakterleri verir
print(greeting[-10:])  #cümledeki sondan 10. karakterden sonrasını verir
print(greeting[-10:-1])  #cümledeki sondan 10. karakterden sondan 1. karaktere kadar olan kısmı verir
print(greeting[2:20:2])  #cümledeki 2. karakterden 20. karaktere kadar olan kısmı 2'şer atlayarak verir