funcionarios = []

def carregar_dados():
    """Carrega os dados de funcionários do arquivo ao iniciar o sistema."""
    try:
        with open("funcionarios.txt", "r") as arquivo:
            for linha in arquivo:
                nome, idade, cargo = linha.strip().split(",")
                funcionarios.append({"nome": nome, "idade": int(idade), "cargo": cargo})
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Nenhum arquivo encontrado. Começando com lista vazia.")

def salvar_dados():
    """Salva os dados de funcionários no arquivo ao finalizar o sistema."""
    with open("funcionarios.txt", "w") as arquivo:
        for f in funcionarios:
            arquivo.write(f"{f['nome']},{f['idade']},{f['cargo']}\n")
    print("Dados salvos com sucesso!")

def adicionar_funcionario():
    """Adiciona um novo funcionário à lista."""
    nome = input("Digite o nome: ")
    try:
        idade = int(input("Digite a idade: "))
    except ValueError:
        print("Idade inválida! Tente novamente.")
        return
    cargo = input("Digite o cargo: ")
    funcionarios.append({"nome": nome, "idade": idade, "cargo": cargo})
    print("Funcionário adicionado com sucesso!")

def listar_funcionarios():
    """Exibe a lista de todos os funcionários cadastrados."""
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    for f in funcionarios:
        print(f"Nome: {f['nome']}, Idade: {f['idade']}, Cargo: {f['cargo']}")

def buscar_funcionario():
    """Busca um funcionário pelo nome."""
    nome = input("Digite o nome do funcionário: ")
    for f in funcionarios:
        if f["nome"].lower() == nome.lower():
            print(f"Nome: {f['nome']}, Idade: {f['idade']}, Cargo: {f['cargo']}")
            return
    print("Funcionário não encontrado.")

def atualizar_funcionario():
    """Atualiza os dados de um funcionário existente."""
    nome = input("Digite o nome do funcionário a ser atualizado: ")
    for f in funcionarios:
        if f["nome"].lower() == nome.lower():
            try:
                nova_idade = int(input("Digite a nova idade: "))
            except ValueError:
                print("Idade inválida!")
                return
            novo_cargo = input("Digite o novo cargo: ")
            f["idade"] = nova_idade
            f["cargo"] = novo_cargo
            print("Dados atualizados com sucesso!")
            return
    print("Funcionário não encontrado.")

def gerar_relatorio():
    """Gera um relatório com os dados dos funcionários em um arquivo."""
    if not funcionarios:
        print("Nenhum funcionário cadastrado para gerar relatório.")
        return
    with open("relatorio_funcionarios.txt", "w") as arquivo:
        for f in funcionarios:
            arquivo.write(f"Nome: {f['nome']}, Idade: {f['idade']}, Cargo: {f['cargo']}\n")
    print("Relatório gerado: relatorio_funcionarios.txt")
