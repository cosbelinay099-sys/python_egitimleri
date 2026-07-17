#"BMW,Mercedes,Opel,Mazda"elemanlarına sahip bir liste oluşturunuz ve ekrana yazdırınız.
car_brands=['BMW','Mercedes','Opel','Mazda']
print(car_brands)
#liste kaç elemanlıdır?
print(len(car_brands)) 
print(car_brands[0]) #listenin 0. indexindeki elemanı verir
print(car_brands[3]) 
car_brands[3]='Toyota'
print(car_brands)
car_brands[2]='Audi'
car_brands[3]='Nissan'
print(car_brands)
del car_brands[-1]
print(car_brands)


#örnek 2
studentA=['Belinay','Coşkun',2006,[70,60,70]]
studentB=['Ahmet','Yılmaz',2005,[80,90,100]]
studentC=['Ayşe','Demir',2006,[90,80,70]]
result=studentA[0]
result=studentB[1]
result=studentC[3][1] #Ayşe'nin 2. notu

print(result)