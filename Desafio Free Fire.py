import random
import time

def introducao():
    print("🔥 Bem-vindo ao Desafio Free Fire 🔥")
    print("Você entrou no campo de batalha!")
    print("Derrote o inimigo para vencer!")
    print("-" * 40)
    time.sleep(2)

def criar_personagem(nome):
    return {
        "nome": nome,
        "vida": random.randint(80, 120),
        "ataque": random.randint(15, 30),
        "defesa": random.randint(5, 15)
    }

def atacar(jogador, inimigo):
    dano = jogador["ataque"] - inimigo["defesa"]
    if dano < 0:
        dano = 0
    inimigo["vida"] -= dano
    print(f"{jogador['nome']} atacou {inimigo['nome']} causando {dano} de dano!")
    print(f"💥 Vida de {inimigo['nome']}: {max(inimigo['vida'], 0)}")
    print("-" * 40)
    time.sleep(1)

def batalha(jogador, inimigo):
    while jogador["vida"] > 0 and inimigo["vida"] > 0:
        atacar(jogador, inimigo)
        if inimigo["vida"] <= 0:
            print(f"🏆 {jogador['nome']} venceu a batalha! GG 🔥")
            break
        atacar(inimigo, jogador)
        if jogador["vida"] <= 0:
            print(f"💀 {inimigo['nome']} venceu a batalha! Você perdeu!")
            break

def main():
    introducao()
    nome_jogador = input("Digite o nome do seu personagem: ")
    jogador = criar_personagem(nome_jogador)
    inimigo = criar_personagem("Inimigo")

    print(f"\n👤 {jogador['nome']} entrou com:")
    print(jogador)
    print(f"\n👹 {inimigo['nome']} apareceu com:")
    print(inimigo)
    print("-" * 40)
    time.sleep(2)

    batalha(jogador, inimigo)
    print("\n🎮 Fim de jogo! Obrigado por jogar o Desafio Free Fire!")

if __name__ == "__main__":
    main()