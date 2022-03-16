#problem 1
#a = 8
#b = 9

a = 2**3
b = 3**2
if a > b:
	print("а больше чем б")


if a < b:
	print("б бьольше чем а")

#problem 2
a = 100
b = 150
c = 200

if a < b:
	print("c > a")
if b < a:
	print("b < c")
if c > a:
	print("a < b")

#problem 3
#поделить каждое число на 17 по модулю и узнать где остаток меньше

a = 17391 % 17
b = 546 % 17
c = 934 % 17

if a < b < c:
	print("a")
if a > b > c:
	print("c")
if c > a > b:
	print("b")


#Problem 4
x = 13**2

if x < 172:
	x = x**2
	print(x)


#problem 5

a = 20

if a % 2 == 0:
	print("четное")
else:
	print("нечетное")


if a % 3 == 0:
	print ("без остаткам")
else: 
	print ("с остатком")

if a*a <=1000:
	print ("нет")
else: print ("да")







