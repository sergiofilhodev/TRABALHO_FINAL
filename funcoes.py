import json
# Funções Globais
# ------------------------------------------------------------------------
# Verificador de Erros
def verificador_dicionario(dicionario, nome_aplicação):
    if not len(dicionario) >= 1:
        print('===========================')
        print("Dicionario Vazio ❌.\n\n")
        print(f"Cadastre pelo menos um(a) {nome_aplicação}.")
        print('===========================')
        return False
    else:
        return True

# Função de salvar
def salvar_dicionarios(dicionario, nome_do_arquivo):
    with open(f'{nome_do_arquivo}.json', 'w') as file:
        json.dump(dicionario, file)

# Função de Carregar
def pegar_dicionario(nome_do_arquivo):
    with open(f'{nome_do_arquivo}.json', 'r') as file:
        return json.load(file)

# Função de pesquisa nomes
def pesquisa_nomes(dicionario, nome):
    lista_nome = nome.split()
    if nome == 'sair':
        print('Tchau😢.')
        return False
    else:
        ver_todos(dicionario, lista_nome)

# Função de verificar se a matricula existi no dicionario
def verificador_matricula(matricula, dicionario):
    if matricula in dicionario.keys():
        return matricula
    else:
        print(f'Matricula "{matricula}" não existi.\n'+"-"*55)
        matricula = input('-'*55+'\n'"Digite novamente a matricula ou digite 'sair':\n 🔦 ")
        if matricula != 'sair':
            verificador_matricula(matricula, dicionario)
        else:
            print("Tchau 😢.")
            return False

# Função de verificar se o nome existi no dicionario
def verificador_nome(matricula, nome, dicionario, nome_aplicacao):
    if dicionario[matricula].lower() == nome.lower():
        return nome
    else:
        print(f'"{nome}" não existi.\n'+"="*55)
        nome = input('-'*55+'\n'f"Digite novamente o nome do {nome_aplicacao} ou digite 'sair':\n 🔦 ")
        if not nome == 'sair':
            verificador_nome(matricula, nome, dicionario, nome_aplicacao)
        else:
            print('Tchau 😢.')
            return False

# Função de verificação de nome segui a regra do sistema
def nome_composto(nome, nome_aplicação):
    if nome.replace(' ','').isalpha() == False:
        print('-'*61+'\n\n'"\nA senha deve conter somente letras e sem acento.\n EX: 'Thomaz maia'\n")
        nome = input('-'*61+'\n'f"Digite novamente o nome do {nome_aplicação} ou digite 'sair':\n 🔦 ")
        if nome == 'sair':
            print('Tchau 😢.')
            return False
        else:
            nome_composto(nome, nome_aplicação)
    else:
        lista_nome = nome.split()
        if len(lista_nome) == 2:
            return nome
        else:
            print('-'*61+'\n\n'"A o nome do professor só tem que ter nome composto e sem acento.\n EX: 'Thomaz maia'\n")
            nome = input('-'*61+'\n\n'f"Digite novamente o nome do {nome_aplicação} ou digite 'sair':\n 🔦 ")
            if nome == 'sair':
                print('Tchau 😢.')
                return False
            else:
                nome_composto(nome, nome_aplicação)


# Função de ver a lista de qualquer dicionario
def ver_lista(dicionario, nome_lista):
    print('\n'+"="*16+'>PESQUISA<'+"="*16)
    print(f"|{nome_lista:=^40}|")
    print(f'|{"MATRICULA:":^11}{"NOME:":^29}|')
    for matricula, nome in dicionario.items():
        print('|'+'-'*40+'|')
        print(f'|{matricula:^11}-{nome:^28}|')
    print('='*42)

def mostrar_tudo(pergunta, dicionario, lista_materia):
    print('|'+'='*41+'|')
    print(f'|{"Matricula":^20}|{"Nome":^20}|')
    for matricula_professor, nome in dicionario[lista_materia[int(pergunta)-1]].items():
        for nome_professor, alunos in nome.items():
            print(f"|{'Professor':^41}|")
            print(f'|{matricula_professor:^20}|{nome_professor:^20}|')
            print(f"|{'Aluno(s)':^41}|")
            for lista in alunos:
                for matricula_alunos, nomes_alunos in lista.items():
                    print('|'+'-'*41+'|')
                    print(f'|{matricula_alunos:^20}|{nomes_alunos:^20}|')
                    print('|'+'-'*41+'|')
    print('|'+'='*41+'|')


def ver_todos(dicionario, lista_nome, matricula_digitada=False):
    if lista_nome != False and matricula_digitada == False:
        dicionario_nomes = {}
        for sobrenome in lista_nome:
            for matricula, nomes in dicionario.items():
                if not matricula in dicionario_nomes:
                    for palavras in nomes.split():
                        if sobrenome.lower() == palavras.lower():
                            dicionario_nomes[matricula] = nomes
                        else:
                            pass
    else:
        dicionario_nomes = {}
        for nome_disciplina, valores in dicionario.items():
            for matricula_professor , valores in valores.items():
                if not matricula_professor in dicionario_nomes:
                    for nome_professor, lista_alunos in valores.items():
                        for aluno in lista_alunos:
                            for matricula_aluno, nome_aluno in aluno.items():
                                dicionario_nomes[matricula_aluno] = nome_aluno
        if len(dicionario_nomes) == 0:
            print(f"'{nome}' não encontrado ❌.")
            print('-'*55+"\n\n"'Tente novamente🔄.\n')
            nome = input('-'*55+'\n'"Digite o nome novamente ou digite '[S]air':\n 🔦 ")
            if nome != 'sair':
                if not lista_nome == False:
                    pesquisa_nomes(dicionario, nome)
                else:
                    ver_todos(dicionario)
            else:
                print('Tchau 😢.')
                return False
        else:
            if matricula_professor != False:
                print(f"|{nome_disciplina:=^40}|")
            print("="*16+'>PESQUISA<'+"="*16)
            print(f'|{"MATRICULA:":^11}{"NOME:":^29}|')
            for matricula, nome in dicionario_nomes.items():
                print('|'+'-'*40+'|')
                print(f'|{matricula:^11}-{nome:^28}|')
            print('='*42)


# ------------------------------------------------------------------------

# Opções do menu das Turmas.
    # Opçao [1] ✅
def criar_turma(dicionario_turma, dicionario_alunos, dicionario_professores, nome_disciplina):
    lista_alunos = []
    verificador_professor = verificador_dicionario(dicionario_professores, 'professor')
    verificador_aluno = verificador_dicionario(dicionario_alunos, 'aluno')
    if verificador_professor == True and verificador_aluno == True:
        ver_lista(dicionario_professores, 'Lista dos professores')
        ver_lista(dicionario_alunos, 'Lista dos alunos')
        if nome_disciplina in dicionario_turma:
            print("Essa disciplina já foi cadastrada 🔄.")
            nome_disciplina = input("Digite o nome da disciplina novamente ou digite '[S]'air:\n 🔦 ").title()
            if nome_disciplina == 'S':
                print("Tchau 😢.")
                return False
            elif not nome_disciplina == 'S':
                criar_turma(dicionario_turma, dicionario_alunos, dicionario_professores, nome_disciplina)
            else:
                print("Opção invalida.")
                nome_disciplina = input("Digite o nome da disciplina novamente ou digite '[S]'air:\n 🔦 ").title()
                criar_turma(dicionario_turma, dicionario_alunos, dicionario_professores, nome_disciplina)
        else:
            matricula_professor = input("Digite a matricula do professor para adicionar a disciplina ou digite 'sair':\n 🔦 ")
            if matricula_professor == 'sair':
                print("Tchau 😢.")
            else:
                matricula_professor = verificador_matricula(matricula_professor, dicionario_professores)
                aux = True
                while aux:
                    matricula_aluno = input("Digite a matricula do aluno que deseja adicionar ou digite 'sair' pra parar de adicionar:\n 🔦 ")
                    if matricula_aluno == 'sair':
                        aux = False
                        break
                    else:
                        matricula_aluno = verificador_matricula(matricula_aluno, dicionario_alunos)
                        if matricula_aluno in lista_alunos:
                            print(f"O aluno '{dicionario_alunos[matricula_aluno]}' já está cadastrado.")
                        else:
                            if matricula_aluno != False:
                                lista_alunos.append({matricula_aluno:dicionario_alunos[matricula_aluno]})
                            else:
                                print("Algo deu errado")
                if aux == False and len(lista_alunos) >= 1:
                    dicionario_turma[nome_disciplina] = {matricula_professor: {dicionario_professores[matricula_professor]: lista_alunos}}
                    print('\n--- Materia cadastrada com sucesso ---')
                    salvar_dicionarios(dicionario_turma, 'dicionario_turmas')
                    return True


    # Opçao [2]
def editar_turma(nome_turma, dicionario, matricula_professor, novo_professor, lista_alunos):
    dicionario[nome_turma] = {matricula_professor:{novo_professor:lista_alunos}}
    if nome_turma in dicionario:
        print("\nProfessor trocado com sucesso ✅.")
        salvar_dicionarios(dicionario, 'dicionario_turmas')

    # Opçao [3]
def ver_turma(nome_turma, dicionario, opcao):
    mostrar_tudo(nome_turma, dicionario, opcao)
    # Opçao [4]
def apagar_turma(dicionario, nome_turma):
    del dicionario[nome_turma]

    pass
    # Opção [5]
def ver_todas_turmas(dicionario):
    lista_disciplinas = []
    for nome_disciplinas in dicionario.keys():
        lista_disciplinas.append(nome_disciplinas)
    if len(lista_disciplinas) == 0:
        print("Não existe Turmas")
        return False
    else:
        aux = 0
        print('='*11+"=>Disciplinas<"+'='*11)
        for nome_disciplinas in lista_disciplinas:
            aux += 1
            print('-'*36+'\n'+f'|{aux:^5}|{nome_disciplinas:^28}|'+'\n'+'-'*36)
        print('='*36)
        return lista_disciplinas

# ------------------------------------------------------------------------
# Opções do menu dos Professores.
    # Opçao [1] ✅
def cadastrar_professor(nome_professor, dicionario):
    dicionario = pegar_dicionario('dicionario_professor')
    matricula = 1
    for matricula_chave in dicionario.keys():
        matricula = int(matricula_chave) + 1
    dicionario[matricula] = nome_professor
    salvar_dicionarios(dicionario,'dicionario_professor')
    
    # Opçao [2] ✅
def editar_professor(matricula_professor, nome_professor, dicionario_professores):
    nome_professor_novo = input(f'-'*55+'\n'"Digite o nome novo do professor '{nome_professor}' ou digite '[s]'air:\n 🔦 ")
    if nome_professor_novo != 's' or nome_professor_novo != 'S':
        dicionario_professores[matricula_professor] = nome_professor_novo
        salvar_dicionarios(dicionario_professores, 'dicionario_professor')
        print('-'*55+'\n\nEditador com sucesso✅.'+'\n'+'-'*55)
    elif nome_professor_novo == 's' or nome_professor_novo == 'S':
        print("Tchau 😢.")
    else:
        print("Opção invalida.")
        editar_professor(matricula_professor, nome_professor, dicionario_professores)


    # Opçao [3] ✅
def ver_dados_professor(dicionario):
    pegar_dicionario('dicionario_professor')
    verificador_dicionario(dicionario, 'professor')
    nome_professor = input("Digite o nome do professor que deseja vê os dados ou digite '[s]'air:\n 🔦 ")
    if nome_professor != 's' or nome_professor != 'S':
        pesquisa_nomes(dicionario, nome_professor)
    elif nome_professor == 's' or nome_professor == 'S':
        print("Tchau 😢.")
    else:
        print("Opção invalida.")
        ver_dados_professor(dicionario)


    # Opçao [4] ✅
def apagar_professor(dicionario):
    matricula = input("Digite o numero da matricula do professor que deseja apagar:\n 🔦 ")
    matricula = verificador_matricula(matricula, dicionario)
    if matricula == False:
        print("Tchau 😢.")
    else:
        nome_professor = input("Digite o nome do professor que deseja apagar:\n 🔦 ")
        nome_professor = verificador_nome(matricula, nome_professor, dicionario, 'professor')
        if nome_professor == False:
            print("Tchau 😢.")
        else:
            del dicionario[matricula]
            salvar_dicionarios(dicionario, 'dicionario_professor')
            print("Professor apagado com sucesso ✅.")

    # Opçao [5] ✅
def visualizar_turmas_professor(dicionario_turma, nome_lista, matricula_digitada):
    if matricula_digitada == False:
        pass
    else:
        print('\n'+"="*17+'>Turmas<'+"="*17)
        print(f"|{nome_lista:=^42}|")
        if matricula_digitada == False:
            print("Tchau 😢.")
        else:
            aux = False
            for nome_disciplina in dicionario_turma.keys():
                for matricula_professor in dicionario_turma[nome_disciplina].keys():
                    if matricula_professor == matricula_digitada:
                        print('='*44+'\n'f'|{nome_disciplina:^42}|'+'\n'+'='*44)
                        aux = True

            if aux == False:
                print('='*44+'\n'f"|{'Esse professor não possui turma.':^42}|"'\n'+'='*44)


    # Opçao [6] 
# def visualizar_alunos_turma_professor(matricula_professor, dicionario):
#     if matricula_professor == False:
#         pass
#     else:
#         for nome_turmas, valores in dicionario.items():
#             if valores == matricula_professor:
#                 ver_todos(dicionario, False, matricula_professor)


# ------------------------------------------------------------------------
# Opções do Menu dos Alunos.
    # Opçao [1]
def cadastrar_aluno(nome_aluno, dicionario):
    dicionario = pegar_dicionario('dicionario_alunos')
    matricula = 1
    for matricula_chave in dicionario.keys():
        matricula = int(matricula_chave) + 1
    dicionario[matricula] = nome_aluno
    if matricula in dicionario:
        print(f"Alunos '{nome_aluno}' cadastrado")
    salvar_dicionarios(dicionario,'dicionario_alunos')

    # Opçao [2]
def editar_aluno(matricula_aluno, nome_aluno, dicionario_alunos):
    nome_aluno_novo = input(f'-'*55+'\n'"Digite o nome novo do Aluno '{nome_aluno}' ou digite '[s]'air:\n 🔦 ")
    if nome_aluno_novo != 's' or nome_aluno_novo != 'S':
        dicionario_alunos[matricula_aluno] = nome_aluno_novo
        salvar_dicionarios(dicionario_alunos, 'dicionario_alunos')
        print('-'*55+'\n\nEditador com sucesso✅.'+'\n'+'-'*55)
    elif nome_aluno_novo == 's' or nome_aluno_novo == 'S':
        print("Tchau 😢.")
    else:
        print("Opção invalida.")
        editar_aluno(matricula_aluno, nome_aluno, dicionario_alunos)


    # Opçao [3]
def visualizar_aluno(dicionario, nome_aluno):
    pegar_dicionario('dicionario_alunos')
    if nome_aluno != 's' or nome_aluno != 'S':
        pesquisa_nomes(dicionario, nome_aluno)
    elif nome_aluno == 's' or nome_aluno == 'S':
        print("Tchau 😢.")
    else:
        print("Opção invalida.")
        visualizar_aluno(dicionario)



    # Opçao [4]
def apagar_aluno(dicionario, matricula):
    del dicionario[matricula]
    salvar_dicionarios(dicionario, 'dicionario_alunos')
    print("Aluno apagado com sucesso ✅.")