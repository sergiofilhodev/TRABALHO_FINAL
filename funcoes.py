import json
# Funções Globais
# ------------------------------------------------------------------------
# Verificador de Erros.
def verificador_dicionario(dicionario, nome_aplicação):
    if not len(dicionario) >= 1:
        print('===========================\n')
        print("Dicionario Vazio ❌.\n")
        print(f"Cadastre pelo menos um(a) {nome_aplicação}.\n")
        print('===========================')
        return False
    else:
        return True

# Função de salvar.
def salvar_dicionarios(dicionario, nome_do_arquivo):
    with open(f'{nome_do_arquivo}.json', 'w') as file:
        json.dump(dicionario, file)

# Função de Carregar.
def carregar_dicionario(nome_do_arquivo):
    with open(f'{nome_do_arquivo}.json', 'r') as file:
        return json.load(file)

# Função de pesquisa nomes.
def pesquisa_nomes(dicionario, nome):
    lista_nome = nome.split()
    if nome in 'fF':
        print('Tchau😢.')
        return False
    else:
        ver_todos(dicionario, lista_nome)

# Função que serve para duas coisas.
def ver_todos(dicionario, lista_nome):
    # Para a pesquisa.
    if lista_nome != False:
        dicionario_nomes = {}
        for sobrenome in lista_nome:
            for matricula, nomes in dicionario.items():
                if not matricula in dicionario_nomes:
                    for palavras in nomes.split():
                        if sobrenome.lower() == palavras.lower():
                            dicionario_nomes[matricula] = nomes
                        else:
                            pass
        if len(dicionario_nomes) == 0:
            print(f"'{nome}' não encontrado ❌.\n")
            print('-'*55+"\n\n"'Tente novamente🔄.\n')
            nome = input('-'*55+'\n'"Digite o nome novamente ou digite '[F]' para cancelar a operação:\n 🔦 ")
            if nome in 'fF':
                print('Tchau 😢.')
                return False
            else:
                pesquisa_nomes(dicionario, nome)
        else:
            print("="*16+'>PESQUISA<'+"="*16)
            print(f'|{"MATRICULA:":^11}{"NOME:":^29}|')
            for matricula, nome in dicionario_nomes.items():
                print('|'+'-'*40+'|')
                print(f'|{matricula:^11}-{nome:^28}|')
            print('='*42)
    # Para visualiza so o dicionario.
    else:
        dicionario_nomes = {}
        for matricula_professor, nome_professor in dicionario.items():
            dicionario_nomes[matricula_professor] = nome_professor
        print("="*16+'>PESQUISA<'+"="*16)
        print(f'|{"MATRICULA:":^11}{"NOME:":^29}|')
        for matricula, nome in dicionario_nomes.items():
            print('|'+'-'*40+'|')
            print(f'|{matricula:^11}-{nome:^28}|')
        print('='*42)

# Função de verificar se a matricula existi no dicionario.
def verificador_matricula(matricula, dicionario):
    if matricula in dicionario.keys():
        print(matricula)
        return matricula
    else:
        print(f'Matricula "{matricula}" não existe.\n'+"-"*55)
        matricula_novamente = input('-'*55+'\n'"Digite novamente a matricula ou digite '[F]' para cancelar a operação:\n 🔦 ")
        if matricula_novamente in 'fF':
            print("Tchau 😢.")
            return False
        else:
            return verificador_matricula(matricula_novamente, dicionario)

# Função de verificar se o nome existi no dicionario
def verificador_nome(matricula, nome, dicionario, nome_aplicacao):
    if dicionario[matricula].lower() == nome.lower():
        return nome
    else:
        print(f'"{nome}" não existi.\n'+"="*55)
        nome = input('-'*55+'\n'f"Digite novamente o nome do {nome_aplicacao} ou digite '[F]' para cancelar a operação:\n 🔦 ")
        if nome in 'fF':
            print('Tchau 😢.')
            return False
        else:
            verificador_nome(matricula, nome, dicionario, nome_aplicacao)

# Função de verificação de nome é composto.
def nome_composto(nome, nome_aplicação):
    if nome.replace(' ','').isalpha() == False:
        print('-'*61+'\n\n'"\nA senha deve conter somente letras e sem acento.\n EX: 'Thomaz maia'\n")
        nome = input('-'*61+'\n'f"Digite novamente o nome do {nome_aplicação} ou digite '[F]' para cancelar a operação:\n 🔦 ")
        if nome in 'fF':
            print('Tchau 😢.')
            return False
        else:
            return nome_composto(nome, nome_aplicação)
    else:
        lista_nome = nome.split()
        if len(lista_nome) == 2:
            return nome
        else:
            print('-'*61+'\n\n'"A o nome do professor só tem que ter nome composto e sem acento.\n EX: 'Thomaz maia'\n")
            nome = input('-'*61+'\n\n'f"Digite novamente o nome do {nome_aplicação} ou digite '[F]' para cancelar a operação:\n 🔦 ")
            if nome in 'fF':
                print('Tchau 😢.')
                return False
            else:
                return nome_composto(nome, nome_aplicação)

# Função de ver a lista de qualquer dicionario.
def ver_dicionario(dicionario, nome_aplicacao):
    print('\n'+"="*16+'>PESQUISA<'+"="*16)
    print(f"|{nome_aplicacao:=^40}|")
    print(f'|{"MATRICULA:":^11}{"NOME:":^29}|')
    for matricula, nome in dicionario.items():
        print('|'+'-'*40+'|')
        print(f'|{matricula:^11}-{nome:^28}|')
    print('='*42)

# Mostra o professor e os alunos do dicionario das turmas.
def mostrar_tudo(pergunta, dicionario, lista_materia):
    print('|'+'='*41+'|')
    print(f'|{"Matricula":^15}|{"Nome":^25}|')
    for matricula_professor, nome in dicionario[lista_materia[int(pergunta)-1]].items():
        for nome_professor, alunos in nome.items():
            print('|'+'-'*41+'|')
            print(f"|{'Professor':=^41}|")
            print('|'+'-'*41+'|')
            print(f'|{matricula_professor:^15}|{nome_professor:^25}|')
            print('|'+'-'*41+'|')
            print(f"|{'Aluno(s)':=^41}|")
            print('|'+'-'*41+'|')
            for lista_aluno in alunos:
                for matricula_alunos, nomes_alunos in lista_aluno.items():
                    print('|'+'-'*41+'|')
                    print(f'|{matricula_alunos:^15}|{nomes_alunos:^25}|')
                    print('|'+'-'*41+'|')
    print('|'+'='*41+'|')

# ------------------------------------------------------------------------
    # Opções do menu das Turmas.
# Cria a turma tem as verificações.
def criar_turma(dicionario_turma, dicionario_alunos, dicionario_professores, nome_disciplina):
    lista_alunos = []
    if nome_disciplina in dicionario_turma:
        print("Essa disciplina já foi cadastrada 🔄.")
        nome_disciplina = input("Digite o nome da disciplina novamente ou digite '[F]' para cancelar a operação:\n 🔦 ").title()
        if nome_disciplina in 'F':
            print("Tchau 😢.")
            return False
        elif not nome_disciplina in 'F':
            criar_turma(dicionario_turma, dicionario_alunos, dicionario_professores, nome_disciplina)
        else:
            print("Opção invalida.")
            nome_disciplina = input("Digite o nome da disciplina novamente ou digite '[F]' para cancelar a operação:\n 🔦 ").title()
            if nome_disciplina in 'F':
                print("Tchau 😢.")
                pass
            else:
                criar_turma(dicionario_turma, dicionario_alunos, dicionario_professores, nome_disciplina)
    else:
        ver_dicionario(dicionario_professores, 'Lista dos professores')
        ver_dicionario(dicionario_alunos, 'Lista dos alunos')
        matricula_professor = input("Digite a matricula do professor para adicionar a disciplina ou digite '[F]' para cancelar a operação:\n 🔦 ")
        if matricula_professor in 'fF':
            print("Tchau 😢.")
        else:
            matricula_professor = verificador_matricula(matricula_professor, dicionario_professores)
            if matricula_professor == False:
                pass
            else:
                aux = True
                while aux:
                    matricula_aluno = input("Digite a matricula do aluno que deseja adicionar ou digite '[F]' pra parar de adicionar:\n 🔦 ")
                    if matricula_aluno in 'fF':
                        aux = False
                        break
                    else:
                        matricula_aluno = verificador_matricula(matricula_aluno, dicionario_alunos)
                        if matricula_aluno in lista_alunos:
                            print(f"\nO aluno '{dicionario_alunos[matricula_aluno]}' já está cadastrado.")
                        else:
                            flag = True
                            for alunos in lista_alunos:
                                for matricula in alunos.keys():
                                    if matricula == matricula_aluno:
                                        print("\nAluno já está na turma ❌.\n")
                                        flag = False
                            if flag:
                                if matricula_aluno != False:
                                    lista_alunos.append({matricula_aluno: dicionario_alunos[matricula_aluno]})
                                else:
                                    print("\nAlgo deu errado")
                if not aux and len(lista_alunos) >= 1:
                    dicionario_turma[nome_disciplina] = {matricula_professor: {dicionario_professores[matricula_professor]: lista_alunos}}
                    print('\n--- Matéria cadastrada com sucesso ✅---')
                    salvar_dicionarios(dicionario_turma, 'dicionario_turmas')
                    return True
                else:
                    print("\nNão foi possivel cadastrar uma turma ❌.")

# Somente edita a turma que contem 3 subfunções escolhida.
def editar_turma(nome_turma, dicionario, matricula_professor, nome_professor, lista_alunos, matricula_aluno, dicionario_aluno, dicionario_professor):
    if matricula_aluno == False and nome_professor == False and dicionario_aluno == False:
        troca_professor_turma(nome_turma, dicionario, matricula_professor, lista_alunos, dicionario_professor)
    elif lista_alunos == False and dicionario_aluno == False and dicionario_professor == False:
        remover_aluno_turma(nome_turma, matricula_professor, nome_professor, matricula_aluno, dicionario)
    else:
        inserir_aluno(nome_turma, matricula_professor, nome_professor, lista_alunos, matricula_aluno, dicionario, dicionario_aluno)

# Primeira Subfunção de editar turma: Função para troca a turma de professor.
def troca_professor_turma(nome_turma, dicionario, matricula_professor, lista_alunos, dicionario_professor):
    dicionario[nome_turma] = {matricula_professor:{dicionario_professor[matricula_professor]:lista_alunos}}
    print("\nProfessor trocado com sucesso ✅.")
    salvar_dicionarios(dicionario, 'dicionario_turmas')

# Segunda subfunção de editar turma: Função para remove um aluno expecifico da turma escoliha.
def remover_aluno_turma(nome_turma, matricula_professor, nome_professor, matricula_aluno, dicionario):
    lista_alunos = dicionario[nome_turma][matricula_professor][nome_professor]
    for aluno in lista_alunos:
        if matricula_aluno in aluno.keys():
            lista_alunos.remove(aluno)
            break
    dicionario[nome_turma][matricula_professor][nome_professor] = lista_alunos
    print("\nAluno removido com sucesso ✅.")
    salvar_dicionarios(dicionario, 'dicionario_turmas')

# Terceira subfunção de editar turma: Função para inserir um aluno na turma.
def inserir_aluno(nome_turma, matricula_professor, nome_professor, lista_aluno, matricula_aluno, dicionario, dicionario_aluno):
    dicionario_aluno_novo = {}
    dicionario_aluno_novo[matricula_aluno] = dicionario_aluno[matricula_aluno]
    print(lista_aluno)
    lista_aluno.append(dicionario_aluno_novo)
    dicionario[nome_turma][matricula_professor][nome_professor] = lista_aluno
    salvar_dicionarios(dicionario, 'dicionario_turmas')

# Função para chama a função de mostrar os professores e os aluno de uma turma expecifica.
def ver_turma(nome_turma, dicionario, opcao):
    mostrar_tudo(nome_turma, dicionario, opcao)

# Função para apagar uma turma expecifica.
def apagar_turma(dicionario, nome_turma):
    del dicionario[nome_turma]
    salvar_dicionarios(dicionario, 'dicionario_turmas')
    print("\n Turma apagada com sucesso ✅.")

# Função para ver todas as turmas do dicionario das turmas/Função Global.
def ver_todas_turmas(dicionario):
    lista_disciplinas = []
    for nome_disciplinas in dicionario.keys():
        lista_disciplinas.append(nome_disciplinas)
    if len(lista_disciplinas) == 0:
        print(f"\n{'Não existe Turmas':^36}\n\n"+'='*36)
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
# Função para cadastrar um professor.
def cadastrar_professor(nome_professor, dicionario):
    dicionario = carregar_dicionario('dicionario_professor')
    matricula = 1
    for matricula_chave in dicionario.keys():
        matricula = int(matricula_chave) + 1
    dicionario[matricula] = nome_professor
    print("\nProfessor cadastrado com sucesso ✅.")
    salvar_dicionarios(dicionario,'dicionario_professor')

# Função para ver a matricula dos professores e os nomes.
def ver_dados_professor(dicionario):
    dicionario = carregar_dicionario('dicionario_professor')
    ver_todos(dicionario, False)

# Função para apagar um Professor.
def apagar_professor(dicionario_professor, dicionario_turma, matricula_digitada):
    aux = False
    contador = 0
    dicionario_novo = {}
    # Percore o dicionario das turmas verificando se o professor tem alguma turma e adiciona em outro dicionario.
    for nome_turma, resto_turma in dicionario_turma.items():
        for matricula_professor, lista in resto_turma.items():
            if matricula_professor == matricula_digitada:
                aux = True
                contador += 1
                dicionario_novo[contador] = nome_turma
    # Apaga e salva o dicionario turma e apaga o professor do dicionario professor.
    if aux:
        for numero_contador, nome_disciplina in dicionario_novo.items():
            del dicionario_turma[nome_disciplina]
        del dicionario_professor[matricula_digitada]
        salvar_dicionarios(dicionario_turma, 'dicionario_turmas')
        salvar_dicionarios(dicionario_professor, 'dicionario_professor')
        print("Professor apagado com sucesso ✅.")
    # Apaga e salva o dicionario dos professores caso o professor não ter nenhuma turma.
    else:
        del dicionario_professor[matricula_digitada]
        salvar_dicionarios(dicionario_professor, 'dicionario_professor')
        print("Professor apagado com successo ✅.")

# Função para visualizar as turmas que o professor tem.
def visualizar_turmas_professor(dicionario_turma, nome_lista, matricula_digitada):
    print('\n'+"="*17+'>Turmas<'+"="*17)
    print(f"|{nome_lista:=^42}|")
    for nome_disciplina in dicionario_turma.keys():
        for matricula_professor in dicionario_turma[nome_disciplina].keys():
            if matricula_professor == matricula_digitada:
                print('='*44+'\n'f'|{nome_disciplina:^42}|'+'\n'+'='*44)

# ------------------------------------------------------------------------
# Opções do Menu dos Alunos.
# Função para cadastrar um aluno.
def cadastrar_aluno(nome_aluno, dicionario):
    dicionario = carregar_dicionario('dicionario_alunos')
    matricula = 1
    for matricula_chave in dicionario.keys():
        matricula = int(matricula_chave) + 1
    dicionario[matricula] = nome_aluno
    if matricula in dicionario:
        print(f"\nAluno(a) '{nome_aluno}' cadastrado(a) ✅.")
    salvar_dicionarios(dicionario,'dicionario_alunos')

# Função para editar um aluno.
def editar_aluno(matricula_digitada, dicionario_alunos, dicionario_turma):
    dicionario_alunos = carregar_dicionario('dicionario_alunos')
    nome_aluno_novo = input('-'*55+'\n'f"Digite o nome novo do Aluno ou digite '[f]' para cancelar a operação:\n 🔦 ")
    if nome_aluno_novo in 'fF':
        print("Tchau 😢.")
        pass
    else:
        aux = False
        # Verificando se a matricula digitada tem na turma.
        for nome_disciplina, resto_turma in dicionario_turma.items():
            for matricula_professor, resto in resto_turma.items():
                for nome_professor, lista_alunos in resto.items():
                    for alunos in lista_alunos:
                        for matricula, nome_aluno in alunos.items():
                            if matricula_digitada == matricula:
                                aux = True
        # Entra aqui quando a matricula digitada estiver em alguma turma.
        if aux:
            # Trocando o nome aluno para um novo na turma.
            for nome_disciplina, resto_turma in dicionario_turma.items():
                for matricula_professor, resto in resto_turma.items():
                    for nome_professor, lista_alunos in resto.items():
                        for alunos in lista_alunos:
                            for matricula, nome_aluno in alunos.items():
                                if matricula_digitada == matricula:
                                    aux = True
                                    alunos[matricula] = nome_aluno_novo
            # Salva o dicionario das turmas e depois o dicionario dos alunos.
            salvar_dicionarios(dicionario_turma,'dicionario_turmas')
            dicionario_alunos[matricula_digitada] = nome_aluno_novo
            salvar_dicionarios(dicionario_alunos, 'dicionario_alunos')
            print('-'*55+'\n\nEditador com sucesso✅.\n'+'\n'+'-'*55)

        # Entra aqui se ele não estiver em nenhum turma.
        else:
            # Troca o nome do aluno.
            dicionario_alunos[matricula_digitada] = nome_aluno_novo
            # Salva o dicionario dos alunos.
            salvar_dicionarios(dicionario_alunos, 'dicionario_alunos')
            print('-'*55+'\n\nEditador com sucesso✅.\n'+'\n'+'-'*55)

# Função para chamar outra função que ver todos os alunos no dicionario.
def visualizar_aluno(dicionario):
    dicionario = carregar_dicionario('dicionario_alunos')
    ver_todos(dicionario, False)

# Função para apagar um aluno.
def apagar_aluno(dicionario, matricula_digitada, dicionario_turma):
    aux = False
    # Verificando se a matricula digitada está na disciplina.
    for nome_disciplina, resto_turma in dicionario_turma.items():
        for matricula_professor, resto in resto_turma.items():
            for nome_professor, lista_alunos in resto.items():
                for alunos in lista_alunos:
                    for matricula_aluno, nome_aluno in alunos.items():
                        if matricula_aluno == matricula_digitada:
                            aux = True
    # Entra aqui se o aluno estiver em alguma turma.
    if aux:
        # remove aluno na disciplina.
        for nome_disciplina, resto_turma in dicionario_turma.items():
            for matricula_professor, resto in resto_turma.items():
                for nome_professor, lista_alunos in resto.items():
                    for alunos in lista_alunos:
                        for matricula, nome_aluno in alunos.items():
                            if matricula_digitada == matricula:
                                aux = True
                                lista_alunos.remove(alunos)
        # Salva no dicionario das turmas.
        salvar_dicionarios(dicionario_turma,'dicionario_turmas')
        # deleta o usuario do dicionario das turmas.
        del dicionario[matricula_digitada]
        # Salva no dicionario dos alunos.
        salvar_dicionarios(dicionario, 'dicionario_alunos')
        print('-'*55+'\n\nEditador com sucesso✅.\n'+'\n'+'-'*55)

    # Entra aqui se o aluno não tiver nenhuma turma.
    else:
        # Deleta o aluno no dicionario dos alunos.
        del dicionario[matricula_digitada]
        # Salva o dicionario dos alunos.
        salvar_dicionarios(dicionario, 'dicionario_alunos')
        print('-'*55+'\n\nEditador com sucesso✅.\n'+'\n'+'-'*55)