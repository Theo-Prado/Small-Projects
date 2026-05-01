preto = "⬛"
branco = "⬜"
tamanho = 8

for linha in range(tamanho):
  tabuleiro_linha = ""
  coluna = 0
  while coluna < tamanho:
    if (linha + coluna) % 2 == 0:
      tabuleiro_linha = tabuleiro_linha + branco
    else:
      tabuleiro_linha = tabuleiro_linha + preto
    coluna = coluna + 1

  print(tabuleiro_linha)
