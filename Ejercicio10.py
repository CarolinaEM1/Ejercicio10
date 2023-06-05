#multiplicar una lista con el número que el usuario digite

lista = list(range(1,11))

print("La lista original es: ")
for i in lista:
    print(i, end="-")

numero = int(input("\nDigite un número a multiplicar -> "))

print(f"\nLista multiplicada por {numero} -> ")
indice = 0
for i in lista:
    lista[indice] *= numero
    indice += 1

for i in lista:
    print(i, end="-")

#Carolina EM