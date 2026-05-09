class Item:
    def _init_(self, nome, tipo, valor):
        self.nome = nome
        self.tipo = tipo
        self.valor = valor

    def usar(self, personagem):
        if self.tipo == "cura":
            personagem.hp += self.valor
            print(f"{personagem.nome} curou {self.valor} HP!")
        elif self.tipo == "ataque":
            personagem.ataque += self.valor
            print(f"{personagem.nome} ganhou {self.valor} de ataque!")

class Personagem:
    def _init_(self, nome, hp, ataque):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
        self.inventario = [] # Adiciona um inventário para o personagem

    def atacar(self, alvo):
        alvo.hp -= self.ataque
        print(f"{self.nome} → {alvo.nome}: -{self.ataque} HP")

    def usar_item(self, indice):
        if 0 <= indice < len(self.inventario):
            item_a_usar = self.inventario.pop(indice) # Remove o item do inventário
            item_a_usar.usar(self) # O item usa seu efeito no próprio personagem
            return True
        else:
            print("Você não tem esse item ou o inventário está vazio.")
            return False

class Mago(Personagem):
    def _init_(self, nome):
        super()._init_(nome, 70, 30)

    def magia(self, alvo):
        alvo.hp -= 40
        print(f"{self.nome} → MAGIA! -40 HP")

def combate(jogador, inimigo):
    while jogador.hp > 0 and inimigo.hp > 0:
        print(f"\n{jogador.nome}: {jogador.hp} | {inimigo.nome}: {inimigo.hp}")
        escolha = input("[1] Atacar [2] Item [3] Fugir: ")
        if escolha == "1":
            jogador.atacar(inimigo)
        elif escolha == "2":
            # Tenta usar o primeiro item do inventário
            if not jogador.usar_item(0):
                print("Não foi possível usar o item. Escolha outra opção.")

        elif escolha == "3":
            print("Fugiu!"); return
        if inimigo.hp > 0:
            inimigo.atacar(jogador)
    print(f"{'Vitória!' if jogador.hp > 0 else 'Derrota...'}")

# Testando o combate:
heroi_teste = Personagem("Arthur", 100, 20)
vilao_teste = Personagem("Goblin", 100, 20)

# Adiciona um item ao inventário do herói para poder testar a opção [2] Item
pocao_cura = Item("Poção de Cura Menor", "cura", 25)
heroi_teste.inventario.append(pocao_cura)

print("\n--- Início do Combate ---")
combate(heroi_teste, vilao_teste)
print("--- Fim do Combate ---")
