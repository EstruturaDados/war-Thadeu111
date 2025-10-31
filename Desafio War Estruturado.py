import random

def mostrar_mensagem_inicial():
    print("🌍 Bem-vindo ao Desafio War Estruturado!")
    print("Você irá comandar um exército e tentar conquistar o inimigo.\n")

def criar_jogadores():
    jogador = {"nome": "Jogador", "tropas": 10}
    inimigo = {"nome": "Inimigo", "tropas": 10}
    return jogador, inimigo

def batalha(jogador, inimigo):
    print("A guerra começou!\n")

    while jogador["tropas"] > 0 and inimigo["tropas"] > 0:
        ataque_jogador = random.randint(1, 6)
        ataque_inimigo = random.randint(1, 6)

        print(f"{jogador['nome']} atacou com {ataque_jogador}")
        print(f"{inimigo['nome']} atacou com {ataque_inimigo}")

        if ataque_jogador > ataque_inimigo:
            inimigo["tropas"] -= 1
            print("✅ Você venceu a rodada!")
        elif ataque_inimigo > ataque_jogador:
            jogador["tropas"] -= 1
            print("❌ Você perdeu a rodada!")
        else:
            print("⚔️ Empate! Nenhuma tropa perdida.")

        print(f"Tropas restantes -> Você: {jogador['tropas']} | Inimigo: {inimigo['tropas']}\n")

    if jogador["tropas"] > 0:
        print("🎉 Parabéns! Você conquistou a vitória!")
    else:
        print("💀 Seu exército foi derrotado!")

def main():
    mostrar_mensagem_inicial()
    jogador, inimigo = criar_jogadores()
    batalha(jogador, inimigo)

if __name__ == "__main__":
    main()