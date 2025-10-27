#include  <stdio.h>

def introducao():
    print("🕵️‍♂️ Bem-vindo ao Detective Quest!")
    print("Você é um detetive e precisa resolver um misterioso caso.")
    print("Preste atenção nas pistas e faça escolhas inteligentes!\n")

def escolher_local():
    while True:
        print("Escolha onde investigar primeiro:")
        print("1 - Biblioteca")
        print("2 - Cozinha")
        print("3 - Jardim")
        escolha = input("Digite o número da sua escolha: ")
        if escolha in ["1", "2", "3"]:
            return escolha
        else:
            print("❌ Escolha inválida! Tente novamente.\n")

def analisar_pista(escolha):
    if escolha == "1":
        print("\nVocê encontrou uma pista: um livro aberto com anotações suspeitas.")
        print("Parece que alguém deixou um recado secreto aqui.\n")
        return "livro"
    elif escolha == "2":
        print("\nVocê encontrou um utensílio sujo de tinta vermelha.")
        print("Pode estar relacionado ao crime!\n")
        return "utensilio"
    elif escolha == "3":
        print("\nVocê encontrou pegadas perto da árvore antiga.")
        print("Talvez elas levem até o culpado!\n")
        return "pegadas"

def decidir_final(pista):
    while True:
        print("Hora de tomar uma decisão final para resolver o caso!")
        print("Escolha quem você acha que é o culpado:")
        print("1 - O mordomo")
        print("2 - A governanta")
        print("3 - O jardineiro")
        final = input("Digite o número da sua escolha: ")
        
        if final not in ["1", "2", "3"]:
            print("❌ Escolha inválida! Tente novamente.\n")
            continue

        if pista == "livro" and final == "2":
            print("\n🎉 Parabéns! Você resolveu o caso corretamente!")
        elif pista == "utensilio" and final == "1":
            print("\n🎉 Parabéns! Você resolveu o caso corretamente!")
        elif pista == "pegadas" and final == "3":
            print("\n🎉 Parabéns! Você resolveu o caso corretamente!")
        else:
            print("\n❌ Ops! Você escolheu a pessoa errada. O caso continua misterioso!")
        break

def main():
    introducao()
    escolha = escolher_local()
    pista = analisar_pista(escolha)
    decidir_final(pista)
    print("\nObrigado por jogar Detective Quest! Até a próxima!")

if __name__ == "__main__":
    main()
