# bot de atendimento automatico
import time

def exibir_menu():
    print("BOT DE ATENDIMENTO AUTOMATICO")
    print("digite 1 para ver catalogo de produtos")
    print("digite 2 para falar com um de nossos atendentes")
    print("digite 3 para falar ver o status de seu pedido")
    print("digite 4 para sair")
    return input("\ndigite a opção desejada: ")

def processar_atendimento():
    print("olá, eu sou assistente virtual, como posso te ajudar?")
    time.sleep(1)

    while True:
        opção = exibir_menu()
        if opção == "1":
            print("catalogo atualizado:")
            print("pizza de calabresa, R$ 45,99")
            print("pizza de frango c/catupiry, R$ 49,99")
            print("pizza de queijo, R$ 39,99")
            print("pizza de bauru, R$ 42,99")
            break
        elif opção == "2":
            print("te direcionando para um de nossos atendentes...")
            break
        elif opção == "3":
            print("verificando seu pedido no banco de dados...")
            time.sleep(2)
            print("seu pedido ja saiu para entrega")
            break
        elif opção == "4":
            print("obrigado por entrar em contato, até logo!")
            break
        else:
            print("opção invalida. tente novamente!")

if __name__ == "__main__":
    processar_atendimento()