fila_um = []
fila_dois = []

ultimo_cont_um = 0
ultimo_cont_dois = 0

print("A -Atendimento fila 1")
print("B - Atendimento fila 2\n\n\n\n")
while True:
    escolha = input("Escolha uma fila ")
    if escolha != "A" and escolha != "B":
      break
    acao = input("escolha uma letra")
    if escolha == "B":
      for letra in acao:
        if acao == "S":
          print(fila_dois)
          break
        elif acao == "F":
          ultimo_cont_dois = ultimo_cont_dois + 1
          fila_dois.append(ultimo_cont_dois)
          print(fila_dois)
        elif acao == "T":
          fila_dois.pop(0)
    elif escolha == "A":
      for letra in acao:
        if acao == "S":
          print(fila_um)
          break
        elif acao == "F":
          ultimo_cont_um = ultimo_cont_um + 1
          fila_um.append(ultimo_cont_um)
          print(fila_um)
        elif acao == "T":
          fila_um.pop(0)
          
