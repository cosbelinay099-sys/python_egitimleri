numbers = [1,19,4,5,10,7,16,3]
letters = ['a','b','c','d','e','f','g','h']

val = min(numbers)
print(val)
val = max(numbers)
print(val)
val = sum(numbers)
print(val)
val = len(numbers)
print(val)
val = sorted(numbers)
print(val)

val = max(letters)
print(val)
val = numbers[3:6]
print(val)

numbers[4]=141
numbers.append(49) #en sona yazılan sayı eklenir
print(numbers)
numbers.insert(2, 100) #index 2 numaralı yere yazılan sayı eklenir
print(numbers)
numbers.remove(19)  #yazılan sayı silinir
print(numbers)
numbers.pop() #sondaki eleman silinir
print(numbers)


numbers.sort()     #elemanları sıralar
letters.sort()
numbers.reverse()    #tersten sıralar
letters.reverse()

print(numbers)
print(letters)

print(numbers.count(10))#içine yazılan elemandan kaç tane olduğunu söyler

numbers.clear()
print(numbers)


