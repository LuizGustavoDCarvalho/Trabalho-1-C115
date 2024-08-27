def opcoes():
    print("Bom dia! Bem-vindo ao atendimento da nossa empresa de telefonia.")
    print("Por favor, escolha uma das opções a seguir:")
    print("1 - Telefone")
    print("2 - Internet")
    print("3 - Encerrar")

def opcoesTelefone():
    print("Você escolheu Telefone.")
    print("Por favor, escolha uma das opções a seguir:")
    print("1 - Recarga")
    print("2 - Saldo")
    print("3 - Voltar")
    
def opcoesInternet():
    print("Você escolheu Internet.")
    print("Por favor, escolha uma das opções a seguir:")
    print("1 - Planos")
    print("2 - Consumo")
    print("3 - Valor da fatura")
    print("4 - Quantidade de internet")
    print("5 - voltar")
    
def planosInternet():
    print("Você escolheu a opção Planos")
    print("1 - 20$ 1GB")
    print("2 - 30$ 2GB")
    print("3 - 50$ 4GB")


def chatbot():
    saldo = 0
    internet = 0
    consumo = 0
    fatura = 0
    
    opcoes()

    escolha = input("Digite a opção desejada: ")
    
    while escolha != "3":
        if escolha == "1":
            opcoesTelefone()
            sub_escolha = input("Digite a opção desejada: ")
            
            while sub_escolha != "3":
                if sub_escolha == "1":
                    print("Você escolheu Recarga.")
                    recarga = input("Digite quanto você deseja recarregar: ")
                    saldo =+ int(recarga)
                    opcoesTelefone()
                    sub_escolha = input("Digite a opção desejada: ")
                elif sub_escolha == "2":
                    print("Você escolheu quantidade de saldo.")
                    print("Seu saldo é: " + str(saldo))
                    opcoesTelefone()
                    sub_escolha = input("Digite a opção desejada: ")
                elif sub_escolha == "3":
                    print("Encerrando a conexão. Obrigado por usar o nosso serviço.")
                else:
                    print("Opção inválida. Tente novamente.")
                    opcoesTelefone()
                    sub_escolha = input("Digite a opção desejada: ")
                    
            opcoes()
            escolha = input("Digite a opção desejada: ")
            
            
        elif escolha == "2":
            opcoesInternet()

            sub_escolha = input("Digite a opção desejada: ")
            
            while sub_escolha != "5":
                if sub_escolha == "1":
                    planosInternet()
                    planos = input("Escolha uma das opções de planos: ")
                    if planos == "1":
                        internet =+ int(1000)
                        fatura = 20
                        print("Plano Contratado")
                    elif planos == "2":
                        internet =+ int(2000)
                        fatura = 30
                        print("Plano Contratado")
                    elif planos == "3":
                        internet =+ int(4000)
                        fatura = 50
                        print("Plano Contratado")
                    opcoesInternet()
                    sub_escolha = input("Digite a opção desejada: ")
                    
                elif sub_escolha == "2":
                    print("Você escolheu Consumo.")
                    print("Seu consumo foi de: " + str(consumo))
                    opcoesInternet()
                    sub_escolha = input("Digite a opção desejada: ")
                elif sub_escolha == "3":
                    print("Você escolheu Valor da fatura.")
                    print("A sua fatura é de " + str(fatura) + " reais.")
                    opcoesInternet()
                    sub_escolha = input("Digite a opção desejada: ")
                elif sub_escolha == "4":
                    print("Você escolheu quantidade de internet.")
                    print("Voce ainda tem: " + str(internet) + " mb de intenet")
                    opcoesInternet()
                    sub_escolha = input("Digite a opção desejada: ")
                elif sub_escolha == "5":
                    print("Encerrando a conexão. Obrigado por usar o nosso serviço.")
                else:
                    print("Opção inválida. Tente novamente.")
                    sub_escolha = input("Digite a opção desejada: ")
            opcoes()
            escolha = input("Digite a opção desejada: ")
            
        else:
            print("Opção inválida. Tente novamente.")
            opcoes()
            escolha = input("Digite a opção desejada: ")

    print("Conexão encerrada. Tenha um bom dia!")

# Executar o chatbot
chatbot()
