import random

# Classe que representa um território
class Territorio:
    def __init__(self, nome, cor, tropas):
        self.nome = nome
        self.cor = cor
        self.tropas = tropas

# Função para cadastrar territórios
def cadastrar_territorios():
    n = int(input("Quantos territórios deseja cadastrar? "))
    mapa = []

    for i in range(n):
        print(f"\n=== Cadastro do Território {i + 1} ===")
        nome = input("Nome: ")
        cor = input("Cor (ex: Vermelho, Azul, Verde): ")
        tropas = int(input("Quantidade de tropas: "))
        mapa.append(Territorio(nome, cor, tropas))

    return mapa

# Exibir territórios cadastrados
def exibir_territorios(mapa):
    print("\n===== LISTA DE TERRITÓRIOS =====")
    for i, t in enumerate(mapa):
        print(f"{i + 1} - {t.nome} | Cor: {t.cor} | Tropas: {t.tropas}")

# Função de ataque entre dois territórios
def atacar(atacante, defensor):
    if atacante.cor == defensor.cor:
        print("\n⚠️  Você não pode atacar um território da mesma cor!")
        return

    print(f"\n🎯 {atacante.nome} ({atacante.cor}) está atacando {defensor.nome} ({defensor.cor})!")

    dado_atacante = random.randint(1, 6)
    dado_defensor = random.randint(1, 6)

    print(f"🎲 Dado atacante: {dado_atacante}")
    print(f"🎲 Dado defensor: {dado_defensor}")

    if dado_atacante > dado_defensor:
        print(f"\n🔥 Ataque bem-sucedido! {atacante.nome} conquistou {defensor.nome}!")
        defensor.cor = atacante.cor
        defensor.tropas = atacante.tropas // 2
        print(f"Novo dono: {defensor.cor} | Tropas transferidas: {defensor.tropas}")
    else:
        print(f"\n💥 Ataque falhou! {defensor.nome} resistiu ao ataque!")
        if atacante.tropas > 0:
            atacante.tropas -= 1

# Programa principal
def main():
    random.seed()  # Garante aleatoriedade
    mapa = cadastrar_territorios()
    exibir_territorios(mapa)

    atacante_idx = int(input("\nEscolha o número do território atacante: ")) - 1
    defensor_idx = int(input("Escolha o número do território defensor: ")) - 1

    if atacante_idx < 0 or defensor_idx < 0 or atacante_idx >= len(mapa) or defensor_idx >= len(mapa):
        print("⚠️  Território inválido!")
    else:
        atacar(mapa[atacante_idx], mapa[defensor_idx])

    print("\n=== Estado final dos territórios ===")
    exibir_territorios(mapa)

if __name__ == "__main__":
    main()
