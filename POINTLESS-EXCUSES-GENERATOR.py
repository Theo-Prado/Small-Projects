import random

nomes = ["O meu cachorro", "A minha gata", "O filho da vizinha","Meu primo"]
verbos = ["comeu o", "destruiu o", "roubou o","ateou fogo no"]
coisas = ["meu dever de casa.","meu documento.", "meu compromisso.","meu trabalho."]

print("Gerador de Desculpas Fúteis")
print()

ciclo = True

while ciclo:
  print("1 - Gerar desculpa")
  print("2 - Sair")
  print()
  try:
    escolha = int(input("Digite sua escolha:"))
    print()
    if escolha == 1:
     aleatorio1 = random.randint(0,3)
     aleatorio2 = random.randint(0,3)
     aleatorio3 = random.randint(0,3)
     aleatorio4 = random.randint(0,100)
     print(nomes[aleatorio1], verbos[aleatorio2], coisas[aleatorio3])
     print()
     print(f"Credibilidade da desculpa de {aleatorio4}%")
     print()
     if aleatorio4 < 30:
      print("Resposta: Para de mentir!")
     elif aleatorio4 < 70:
      print("Resposta: Sei sei...")
     else:
      print("Resposta: Sério?! Eu sinto muito!")
     print()
    elif escolha == 2:
     ciclo = False
     print("Obrigado por usar o sistema!")
    else:
      print("Digito inválido.")
  except ValueError:
    print("Digito inválido.")
    print()
