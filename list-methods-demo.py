names=['Ali','Yağmur','Belinay','Ahmet']
years=[1998,2006,2006,1981]
print(names)
print(years)

names.append('Cenk')
print(names)

names.insert(0,'Sena')
print(names)
names.remove('Yağmur')
print(names)
names.index('Belinay')
print (names)

names.sort()
print(names)
names.reverse()
print(names)

val=sorted(names)
print(val)

val=sorted(years)
print(val)
val=min(years)
print(val)
val=max(years)
print(val)

print(years.count(2006))