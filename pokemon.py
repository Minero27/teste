import random

class Pokemon:
    def __init__(self, nome, tipo, hp, ataque, defesa):
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, outro):
        print(self.nome + " atacou " + outro.nome)
        dano = self.ataque - outro.defesa
        if dano < 1:
            dano = 1
        outro.hp = outro.hp - dano
        print("Causou", dano, "de dano!")

    def especial(self, outro):
        print(self.nome + " usou golpe especial!")
        if self.nome == "Roger":
            dano = self.ataque + 10
            outro.hp = outro.hp - dano
            print("Dano especial de", dano)
        elif self.nome == "Ricardão":
            cura = 15
            self.hp = self.hp + cura
            print("Curou", cura, "de HP")
        else:
            print("Nada aconteceu.")

    def status(self):
        print(self.nome, "HP:", self.hp)

def batalha(p1, p2):
    turno = 1
    while p1.hp > 0 and p2.hp > 0:
        print("\nTurno", turno)
        p1.status()
        p2.status()
        acao = input("1 - Ataque normal\n2 - Golpe especial\nEscolha: ")
        if acao == "2":
            p1.especial(p2)
        else:
            p1.atacar(p2)
        if p2.hp <= 0:
            break
        p2.atacar(p1)
        turno += 1
    print("\nFim da batalha!")
    if p1.hp > 0:
        print(p1.nome, "venceu!")
    else:
        print(p2.nome, "venceu!")

roger = Pokemon("Roger", "Torneiro", 35, 12, 6)
ricardao = Pokemon("Ricardão", "Mamada", 39, 10, 5)

batalha(roger, ricardao)