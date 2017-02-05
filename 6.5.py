total = 40
lista = list(range(1,41))
cont = 1
x = 0

choice = input("digite a sua escolha: ")

for letra in choice:
    if letra == "A":
        lista.append(total + cont)
        cont = cont + 1
    elif letra == "I":
        lista.pop(0)
print(lista)