print("Iniciando os estudos")

var1 = 12
var2 = 30
var3 = var1 + var2

print(var3)

var3 = var3 / 2

print(var3)

num1 = int(input("Digite um número a seguir: "))
dobro = 2*num1

print(dobro)

x = 10
y = 4.2

num = float(input("Digite um número a seguir: "))

# Fazendo com que o output seja o mesmo nos dois casos
print(num > x*y, num <= x + y, num*y != x*y)
print(num == x*y, num*y == x*y, y > x + num)

x = 4.2

y = 10

z = "42"

not (((x * y == z) and not (x < y)) or y % 2 == 0)