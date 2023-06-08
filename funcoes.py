import json
# Funções que iram se repetir
    # Verificador de Erros
def verificador_dicionario(dicionario):
    if len(dicionario) == 0:
        print('===========================')
        print("Dicionario Vazio ❌.")
        print()
        print("Cadastre pelo menos um professor e um aluno")
        print('===========================')
        return False
    else:
        return True

    # Função de Carregar
def salvar_dicionarios(dicionario, nome_do_arquivo):
    with open(f'{nome_do_arquivo}.json', 'w') as file:
        json.dump(dicionario, file)

def pegar_dicionario(nome_do_arquivo):
    with open(f'{nome_do_arquivo}.json', 'r') as file:
        return json.load(file)
    
def pesquisa_nomes(dicionario, nome):
    lista_nomes = nome.split()
    dicionario_nomes = {}
    if nome == 'sair':
        print('Tchau😢.')
        pass
    else:
        for sobrenome in lista_nomes:
            for matricula, nomes in dicionario.items():
                if not matricula in dicionario_nomes:
                    for palavras in nomes.split():
                        if sobrenome.lower() == palavras.lower():
                            dicionario_nomes[matricula] = nomes
                        else:
                            pass
        if len(dicionario_nomes) == 0:
            print(f"'{nome}' não encontrado ❌.")
            print('-'*55+"\n"'Tente novamente🔄.\n')
            nome = input('-'*55+'\n'"Digite o nome novamente:\n 🔦 ")
            pesquisa_nomes(dicionario, nome)

        else:
            print("="*16+'>PESQUISA<'+"="*16)
            print(f'|{"MATRICULA":^11}{"NOME":^29}|')
            for matricula, nome in dicionario_nomes.items():
                print('|'+'-'*40+'|')
                print(f'|{matricula:^11}-{nome:^28}|')
            print('='*42)
        
def verificador_matricula(matricula, dicionario):
    if matricula in dicionario.keys():
        return matricula
    else:
        print(f'Matricula "{matricula}" não existi.\n'+"-"*55)
        matricula = input('-'*55+'\n'"Digite novamente a matricula:\n 🔦 ")
        verificador_matricula(matricula, dicionario)
        return False
    
def verificador_nome(matricula, nome, dicionario, nome_aplicacao):
    if dicionario[matricula].lower() == nome.lower():
        return nome
    else:
        print(f'"{nome}" não existi.\n'+"="*55)
        nome = input('-'*55+'\n'f"Digite novamente o nome do {nome_aplicacao}:\n 🔦 ")
        verificador_nome(matricula, nome, dicionario, nome_aplicacao)
        return False
    

def nome_conposto(nome, nome_aplicação):
    if nome.replace(' ','').isalpha() == False:
        print('-'*61+'\n\n'"\nA senha deve conter somente letras e sem acento.\n EX: 'Thomaz maia'\n")
        nome = input('-'*61+'\n'f"Digite novamente o nome do {nome_aplicação}:\n 🔦 ")
        nome_conposto(nome, nome_aplicação)
    else:
        lista_nome = nome.split()
        if len(lista_nome) == 2:
            print('oi')
            return nome
        else:
            print('-'*61+'\n\n'"A o nome do professor só tem que ter nome composto e sem acento.\n EX: 'Thomaz maia'\n")
            nome = input('-'*61+'\n\n'f"Digite novamente o nome do {nome_aplicação}:\n 🔦 ")
            nome_conposto(nome, nome_aplicação)

# ------------------------------------------------------------------------
# Opções do menu das Turmas.
    # Opçao [1]
def criar_turma(dicionario_turma, dicionario_alunos, dicionario_professores):
    verificador_professor = verificador_dicionario(dicionario_professores)
    verificador_aluno = verificador_dicionario(dicionario_alunos)
    lista_alunos = dicionario_alunos.get('Materia')
    if verificador_aluno == True and verificador_professor == True:
        for alunos in lista_alunos:
            print() 
        return True
    else:
        return False
    # Opçao [2]
def editar_turma():
    pass
    # Opçao [3]
def ver_turma():
    pass
    # Opçao [4]
def apagar_turma():
    pass

# ------------------------------------------------------------------------
# Opções do menu dos Professores.
    # Opçao [1]
def cadastrar_professor(nome_professor, dicionario):
    dicionario = pegar_dicionario('dicionario_professor')
    matricula = 1
    for matricula_chave in dicionario.keys():
        matricula = int(matricula_chave) + 1
    dicionario[matricula] = nome_professor
    salvar_dicionarios(dicionario,'dicionario_professor')
    
    # Opçao [2]
def editar_professor(matricula_professor, nome_professor, dicionario_professores):
    nome_professor_novo = input(f'-'*55+'\n'"Digite o nome novo do professor '{nome_professor}':\n 🔦 ")
    dicionario_professores[matricula_professor] = nome_professor_novo
    salvar_dicionarios(dicionario_professores, 'dicionario_professor')
    print('-'*55+'\nEditador com sucesso✅.')

    # Opçao [3]
def ver_dados_professor(dicionario):
    nome_professor = input("Digite o nome do professor que deseja vê os dados: ")
    matricula = 0
    professores = []
    for nome_professor in dicionario.values():
        professores.append(nome_professor)


    # Opçao [4]
def apagar_professor():
    pass
    # Opçao [5]
def visualizar_turmas_professor():
    pass
    # Opçao [6]
def visualizar_alunos_turma_professor():
    pass

# ------------------------------------------------------------------------
# Opções do Menu dos Alunos.
    # Opçao [1]
def cadastrar_aluno(dicionario,lista_ids):
    print('===========================')
    nome_aluno = input("Digite o nome do aluno: ")

    lista_ids.append()
    dicionario[id] = nome_aluno
    print('===========================')

    # Opçao [2]
def editar_aluno():
    pass
    # Opçao [3]
def visualizar_aluno():
    pass
    # Opçao [4]
def apagar_aluno():
    pass