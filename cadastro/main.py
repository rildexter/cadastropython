from menu import menu
from funcoes import adicionar_funcionario, listar_funcionarios, buscar_funcionario, atualizar_funcionario, gerar_relatorio, carregar_dados, salvar_dados

def main():
    carregar_dados()
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_funcionario()
        elif opcao == "2":
            listar_funcionarios()
        elif opcao == "3":
            buscar_funcionario()
        elif opcao == "4":
            atualizar_funcionario()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "6":
            salvar_dados()
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
