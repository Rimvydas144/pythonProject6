from random import randint, random

print("---1.1---")
def sumos_skaiciavimas (a,b) :
    suma = (a + b)
    print(suma)
a = 2
b = 5
sumos_skaiciavimas(a,b)

#ARBA
def sumos_skaiciavimas (a,b) :
    suma = (a + b)
    print(suma)
sumos_skaiciavimas(2,5)

#ARBA
def sumos_skaiciavimas (a,b) :
    print(a + b)
sumos_skaiciavimas(2,5)

print("---1.2---")
def PISq ():
    return 9.8596
print(PISq())

print("---1.3---")
def sandaugos_skaiciavimas (a,b) :
    sandauga = (a * b)
    print(sandauga)
a = 2
b = 5
sandaugos_skaiciavimas(a,b)

#ARBA
def multiply (a,b):
    return a*b
print(multiply(2, 5))


print("---1.4---")
def skaiciai_masyve (masyvas):
    return masyvas
masyvas = [7,4,8,9,1]
print(skaiciai_masyve (masyvas))

#ARBA
def printArr(arr):
    line = ""
    for i in  arr:
        line += str(i) + ", "
    print(line[:-2] + ";")
printArr([1,4,10])

print("---1.5---")
def numeriai (a,b):
    if a > b:
        print(f' skaicius {a} max, skaicius {b} min')
    elif a == b:
        print(f'skaiciai {b} yra {a} lygus')
    else:
        print(f'skaicius {b} max, skaicius {a} min')
a = randint(1,10)
b = randint(1, 10)
numeriai(a,b)

#ARBA (nuo cia viskas pagal paskaita)
def rndNum(min,max):
    return randint(min,max)

print("---1.6---")
def rndNumArr(min,max,length):
    arr = []
    for i in range (length):
        arr.append(rndNum(min, max))
    return arr
rndArr = rndNumArr(1,10,4)
print(rndArr)

print("---1.7---")
def sumNumArr(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
print(sumNumArr(rndArr))

print("---1.8---")
def avgNumArr(arr):
    return sumNumArr(arr)/ len(arr)
print(avgNumArr(rndArr))

print("---1.10---")
def countStrSymbols(str):
    print(f'simboliu yra {len(str.replace(" ", ""))}, tarpu yra {len(str) - len(str.replace(" ", ""))}')
countStrSymbols("Siandien labai grazi diena")

print("---1.11---")
def UltraSmartTextCodingSystem(str):
    return str[::-1]
print(UltraSmartTextCodingSystem("labas"))

