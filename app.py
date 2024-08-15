import os

id_cadastrado = 0
id_ativo = []
restaurantes_cadastrados = []
telefones_cadastrados = []
responsaveis_cadastrados = []
restaurantes_ativos = []
telefones_ativos = []
responsaveis_ativos = []


def exibir_nome_do_programa():
    print(
        """
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█ 
"""
    )


def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Desativar restaurante")
    print("5. Sair\n")


def opcao_invalida():
    print("A opção escolhida é invalida")
    retorna_menu_principal()


def retorna_menu_principal():
    input("\nPressione ENTER para voltar ao menu principal ")
    main()


def exibir_subtitulo(texto):
    os.system("cls")
    linha = "*" * (len(texto) + 1)
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_restaurante():
    global id_cadastrado
    exibir_subtitulo("--- Cadastro de novos restaurantes ---")
    nome_inserido = input("Informe o nome do restaurante: ")
    telefone_inserido = input("Informe o telefone do restaurante: ")
    responsavel_inserido = input("Informe o nome do responsável pelo restaurante: ")
    id_cadastrado = id_cadastrado + 1
    dados_restaurante = {
        "ID": id_cadastrado,
        "Nome": nome_inserido,
        "Telefone": telefone_inserido,
        "Responsável": responsavel_inserido,
        "Ativo": False,
    }
    restaurantes_cadastrados.append(dados_restaurante)
    # id_inserido = len(id_cadastrado) + 1
    # id_cadastrado.append(id_inserido)
    print("Restaurante cadastrado com sucesso")
    retorna_menu_principal()


def listar_restaurantes():
    exibir_subtitulo("-------Restaurantes Cadastrados------")
    if id_cadastrado == 0:
        print("Não há restaurantes cadastrados")
        retorna_menu_principal()
    else:
        for restaurante in restaurantes_cadastrados:
            id = restaurante["ID"]
            nome_restaurante = restaurante["Nome"]
            telefone = restaurante["Telefone"]
            responsavel = restaurante["Responsável"]
            if restaurante["Ativo"] == False:
                ativo = "Inativo"
            else:
                ativo = "Ativo"
            print(
                f"- ID:{id.ljust(5)} | Nome: {nome_restaurante.ljust(25)} | Tel: {telefone.ljust(25)} | Resp: {responsavel.ljust(25)} | {ativo}"
            )
        retorna_menu_principal()


def ativar_restaurantes():
    exibir_subtitulo("-------Restaurantes disponíveis para Ativação------")
    try:
        if any(not restaurante["Ativo"] for restaurante in restaurantes_cadastrados):
            for restaurante in restaurantes_cadastrados:
                id = restaurante["ID"]
                nome_restaurante = restaurante["Nome"]
                telefone = restaurante["Telefone"]
                responsavel = restaurante["Responsável"]
                ativo = "Ativo" if restaurante["Ativo"] else "Inativo"
                print(
                    f"- ID:{id} | Nome: {nome_restaurante} | Tel: {telefone} | Resp: {responsavel} | {ativo}"
                )

            opcao_escolhida = int(
                input("Informe o ID do restaurante que deseja ativar: ")
            )
            if any(
                restaurante["ID"] == opcao_escolhida
                for restaurante in restaurantes_cadastrados
            ):
                restaurante["Ativo"] = True
                print("Restaurante ativado com sucesso")
                retorna_menu_principal()
            else:
                input("ID não encontrado, pressione ENTER para tentar novamente")
                ativar_restaurantes()
        else:
            print("Não há restaurantes disponíveis para ativação")
            retorna_menu_principal()
    except:
        input("Apenas número. Tecle ENTER para tentar novamente")
        ativar_restaurantes()


def desativar_restaurantes():
    exibir_subtitulo("-------Restaurantes disponíveis para Desativação------")
    try:
        if any(restaurante["Ativo"] for restaurante in restaurantes_cadastrados):
            for restaurante in restaurantes_cadastrados:
                id = restaurante["ID"]
                nome_restaurante = restaurante["Nome"]
                telefone = restaurante["Telefone"]
                responsavel = restaurante["Responsável"]
                ativo = "Ativo" if restaurante["Ativo"] else "Inativo"
                print(
                    f"- ID:{id} | Nome: {nome_restaurante} | Tel: {telefone} | Resp: {responsavel} | {ativo}"
                )

            opcao_escolhida = int(
                input("Informe o ID do restaurante que deseja desativar: ")
            )
            if any(
                restaurante["ID"] == opcao_escolhida
                for restaurante in restaurantes_cadastrados
            ):
                restaurante["Ativo"] = False
                print("Restaurante desativado com sucesso")
                retorna_menu_principal()
            else:
                input("ID não encontrado, pressione ENTER para tentar novamente")
                desativar_restaurantes()
        else:
            print("Não há restaurantes disponíveis para desativação")
            retorna_menu_principal()
    except:
        input("Apenas número. Tecle ENTER para tentar novamente")
        desativar_restaurantes()


def escolher_opcoes():
    # try:
    opcao_escolhida = int(input("Escolha uma das opções acima:"))
    match opcao_escolhida:
        case 1:
            cadastrar_restaurante()
        case 2:
            listar_restaurantes()
        case 3:
            ativar_restaurantes()
        case 4:
            desativar_restaurantes()
        case 5:
            # flag = 0
            exibir_subtitulo("O aplicativo foi encerrado")
        case _:
            opcao_invalida()


# except:
#         opcao_invalida()


if __name__ == "__main__":
    main()
