# Importando todas as outras pastas.
from funcoes import*
from menus import*

# Dicionario das Turmas.
dicionario_turmas = carregar_dicionario('dicionario_turmas')
# Dicionario dos Professores.
dicionario_professores = carregar_dicionario('dicionario_professor')
# Dicionario dos Alunos.
dicionario_alunos = carregar_dicionario('dicionario_alunos')

# Logica raiz do programa.
while True:
    op = menu_inicial() # Chama a função do menu inicial.
    #✅
    if op == '1':
        while True: # Chama a função infinitamente até uma forção maior lhe parar.
            op = menu_turmas() # Chama a função do Menu de turmas.
            # menu [1] Turmas [1]✅.
            if op == '1':
                # Carrega o arquivo json do diretorio.
                dicionario_turmas = carregar_dicionario('dicionario_turmas')
                dicionario_professores = carregar_dicionario('dicionario_professor')
                dicionario_alunos = carregar_dicionario('dicionario_alunos')
                # ------------------------------------------------------
                if verificador_dicionario(dicionario_professores, 'professor') == True and verificador_dicionario(dicionario_alunos, 'aluno') == True: # Verifica se os dicionario estão vazios.
                    nome_disciplina = input('-'*55+'\n'+"Digite o nome da disciplina ou digite '[F]' para cancelar a operação:\n 🔦 ").title()
                    if nome_disciplina in 'F':
                        print("Tchau 😢.")
                        continue
                    else:
                        criar_turma(dicionario_turmas, dicionario_alunos, dicionario_professores, nome_disciplina) # Chama a função de criar turma.

            # menu [1] Turmas [2] ✅.
            elif op == '2':
                if verificador_dicionario(dicionario_professores, 'professor') == True and verificador_dicionario(dicionario_alunos, 'aluno') == True: # verifica se os dicionario estão vazios.
                    lista_materia = ver_todas_turmas(dicionario_turmas) # Chama a função para ver todas as disciplinas que existe no dicionario turma.
                    if lista_materia == False:
                        pass
                    else:
                        opcao = input('-'*55+'\n'+"Digite o numero da materia que deseja mostrar os alunos e e fazer as operações seguintes ou digite '[F]' para cancelar a operação:\n 🔦 ")
                        if opcao in 'fF':
                            pass
                        else:
                            mostrar_tudo(opcao, dicionario_turmas, lista_materia) # Chama a função de mostrar dos os alunos e professores que existe em uma turma especifica.
                            while True:
                                op = menu_edita_turma() # Chama a função do menu de editar somente uma turma por vez.
                                if op in 'fF':
                                    print("Tchau 😢.")
                                    break
                                elif op == '1': #✅
                                    dicionario_turmas = carregar_dicionario('dicionario_turmas') # Carrega o arquivo json para ser o dicionario_turmas.
                                    if verificador_dicionario(dicionario_turmas, 'turmas') == False: # Verifica se o dicionario está vazio.
                                        continue
                                    else:
                                        # Percorre todo o dicionario que tem armazena as turmas
                                        for nome_disciplina, resto in dicionario_turmas.items():
                                            if nome_disciplina == lista_materia[int(opcao)-1]: # Compara se o nome da disciplina/turma e igual a materia que o usuário.
                                                lista_materia.append(nome_disciplina) # Coloca o nome da disciplina dentro de uma lista.
                                                for matricula_professor, resto in resto.items(): # percorre o resto do dicionario.
                                                    for nome_professor, lista_alunos in resto.items(): # Percorre uma lista que contem todos os alunos da displina.
                                                        alunos = lista_alunos # Cria outra lista pra não da comflito.
                                        ver_dicionario(dicionario_professores, 'Lista dos professores') # Chama a função para aparecer todos os professores do dicionario dos professores.
                                        matricula_professor = input("Digite a matricula do novo professor ou digite '[F]' para cancelar a troca:\n 🔦 ")
                                        if matricula_professor in 'fF':
                                            print('Operação Cancelada.')
                                        else:
                                            matricula_professor = verificador_matricula(matricula_professor, dicionario_professores) # Verifica se a matricula digitada existe no dicionario dos professores.
                                            if matricula_professor == False:
                                                continue
                                            else:
                                                editar_turma(lista_materia[int(opcao)-1], dicionario_turmas, matricula_professor, False, alunos, False, False, dicionario_professores) # Chama a função para editar a turmas onde nesse tem subfunções.
                                elif op == '2': #✅
                                    dicionario_turmas = carregar_dicionario('dicionario_turmas') # Carrega o arquivo json para ser o dicionario_turmas.
                                    if verificador_dicionario(dicionario_turmas, 'turmas') == False: # Verifica se o dicinario não está vazio.
                                        continue
                                    else:
                                        dicionario = {} # Dicionario auxiliar.
                                        for nome_disciplina, resto in dicionario_turmas.items(): # Percorre o dicionario das turmas.
                                            if nome_disciplina == lista_materia[int(opcao)-1]: # Compara se o nome da disciplina é igual a opção que o usuário digitou lá em cima.
                                                for matricula_professor, resto in resto.items(): # Percorre o resto do dicionario.
                                                    for nome_professor, resto in resto.items(): # Percorre novamente o resto do dicionario.
                                                        for lista_alunos in resto: # Percorre a lista.
                                                            for matricula_aluno, nome_aluno in lista_alunos.items(): # Percorre as informações dos aluno que está na turma.
                                                                dicionario[matricula_aluno] = nome_aluno # Adiciona esse alunos da materia no dicionario auxiliar.
                                        # Verifica se o dicionario auxiliar está vazio.
                                        if len(dicionario) == 0:
                                            print("Não existe nenhum aluno na turma para remover ❌.")
                                        else:
                                            ver_dicionario(dicionario, 'lista dos alunos') # Chama a função para ver todos os alunos da turma.
                                            matricula_remover = input("Digite a matricula do aluno que desejas remover ou digite '[F]' para cancelar a operação:\n🔦 ")
                                            if matricula_remover in 'fF':
                                                print("Tchau 😢.")
                                            else:
                                                matricula_remover = verificador_matricula(matricula_remover, dicionario) #  Chama a função para verificar se a matricula exite no dicionario auxiliar
                                                if matricula_remover == False:
                                                    continue
                                                else:
                                                    editar_turma(lista_materia[int(opcao)-1], dicionario_turmas, matricula_professor, nome_professor, False, matricula_remover, False, False) # Chama a função para editar a turmas onde nesse tem subfunções.
                                elif op == '3': #✅
                                    dicionario_turmas = carregar_dicionario('dicionario_turmas') # Carrega o arquivo json para ser o dicionario_turmas.
                                    if verificador_dicionario(dicionario_turmas, 'turmas') == False:
                                        continue
                                    else:
                                        dicionario = {} # Dicionario auxiliar.
                                        # Percorre o dicionario da turma digitada para adicionar em outro dicionario.
                                        for nome_disciplina, resto in dicionario_turmas.items(): # Percorre o dicionario das turmas.
                                            if nome_disciplina == lista_materia[int(opcao)-1]: # Compara se o nome da disciplina é igual a opção que o usuário digitou lá em cima.
                                                for matricula_professor, resto in resto.items(): # Percorre o resto do dicionario.
                                                    for nome_professor, lista_alunos in resto.items(): # Percorre novamente o resto do dicionario.
                                                        for alunos in lista_alunos: # Percorre a lista.
                                                            for matricula_aluno, nome_aluno in alunos.items(): # Percorre as informações dos aluno que está na turma.
                                                                dicionario[matricula_aluno] = nome_aluno # Adiciona os alunos da materia no dicionario auxiliar.

                                        ver_dicionario(dicionario_alunos, 'lista dos alunos') # Chama a função para ver todos os alunos do dicionario dos alunos para escolher o aluno.
                                        matricula_aluno_novo = input("Digite a matricula do aluno que desejas adicionar ou digite '[F]' para cancelar a operação:\n🔦 ")
                                        aux = True # Uma flag para auxiliar na logica.
                                        # Percorre o dicionario novamente verificando se o aluno já está na turma.
                                        for nome_disciplina, resto in dicionario_turmas.items(): # Percorre o dicionario das turmas.
                                            if nome_disciplina == lista_materia[int(opcao)-1]: # Compara se o nome da disciplina é igual a opção que o usuário digitou lá em cima.
                                                for matricula_professor, resto in resto.items(): # Percorre o resto do dicionario.
                                                    for nome_professor, lista_alunos in resto.items(): # Percorre novamente o resto do dicionario.
                                                        for alunos in lista_alunos: # Percorre a lista.
                                                            for matricula_aluno, nome_aluno in alunos.items(): # Percorre as informações dos aluno que está na turma.
                                                                if matricula_aluno == matricula_aluno_novo: # Compara se a matricula do aluno que está na turma e igual a matricula do aluno que foi digitado.
                                                                    print("Aluno já está na turma ❌.")
                                                                    aux = False
                                                                else:
                                                                    dicionario[matricula_aluno] = nome_aluno # Adiciona os alunos que não estão na turma.
                                        if aux:
                                            if matricula_aluno_novo in 'fF':
                                                print("Tchau 😢.")
                                                continue
                                            else:
                                                matricula_aluno_novo = verificador_matricula(matricula_aluno_novo, dicionario_alunos) # Verifica se a matricula do aluno que vai entrar na turma existe no dicionario dos alunos.
                                                if matricula_aluno_novo == False:
                                                    continue
                                                else:
                                                    editar_turma(nome_disciplina, dicionario_turmas, matricula_professor, nome_professor, lista_alunos, matricula_aluno_novo, dicionario_alunos, False) # Chama a função para editar a turmas onde nesse tem subfunções.
                                elif op == 'f' or op == 'F':
                                    break
                                else:
                                    print('\n\n'+f"Opção '{op}' invalida ❌."+'\n\n')
            # menu [1] Turmas [3] ✅
            elif op == '3':
                dicionario_turmas = carregar_dicionario('dicionario_turmas') # Carrega o arquivo json para ser o dicionario_turmas.
                if verificador_dicionario(dicionario_turmas, 'turma') == False: # Verifica se o dicionario das turmas está vazia.
                    continue
                else:
                    lista_materia = ver_todas_turmas(dicionario_turmas) # Chama a função de ver todas as turmas que exite no dicionario das turmas.
                    if lista_materia == False:
                        continue
                    else:
                        opcao = input('-'*55+'\n'+"Digite o numero da materia desejada ou digite digite '[F]' para cancelar a operação:\n 🔦 ")
                        if opcao in 'fF':
                            pass
                        else:
                            mostrar_tudo(opcao, dicionario_turmas, lista_materia) # Chama a função para mostrar professor e os alunos da turma escolhida.
            # menu [1] Turmas [4] ✅
            elif op == '4':
                dicionario_turmas = carregar_dicionario('dicionario_turmas') # Carrega o arquivo json para ser o dicionario_turmas.
                if verificador_dicionario(dicionario_turmas, 'turma') == False: # Verifica se o dicionario das turmas está vazia.
                    continue
                else:
                    lista_turmas = ver_todas_turmas(dicionario_turmas) # Chama função de ver todas as turmas que existe no dicionario das turmas.
                    if lista_turmas == False:
                        continue
                    else:
                        opcao = input('-'*55+'\n'+"Digite o numero da materia que deseja apagar ou digite digite '[F]' para cancelar a operação:\n 🔦 ")
                        if opcao in 'fF':
                            print("Tchau 😢.")
                            continue
                        else:
                            apagar_turma(dicionario_turmas, lista_turmas[int(opcao)-1]) # Chama a função a para apagar a turma que foi escolhida.
            elif op == 'V' or op == 'v':
                break
            else:
                print(f"\nOpção '{op}' invalida ❌.\n")
    # ✅
    elif op == '2':
        while True:
            op = menu_professores()
            # Menu [2] Professores [1] ✅
            if op == '1':
                dicionario_professores = carregar_dicionario('dicionario_professor') # Carrega o arquivo json para ser o dicionario_turmas.
                nome_professor = input('-'*55+'\n'+"\nDigite o nome do professor que irar cadastrar ou digite '[F]' para deixar operação:\n 🔦 ")
                if nome_professor in 'fF':
                    print("Tchau 😢.")
                    continue
                else:
                    nome_professor = nome_composto(nome_professor, 'professor') # Chama a função de verificar se o nome digitado é composto ou não.
                    if nome_professor == False:
                        continue
                    else:
                        cadastrar_professor(nome_professor, dicionario_professores) # Chama a função para cadastrar o professor.
            # Menu [2] Professores [2] ✅
            elif op == '2':
                dicionario_professores = carregar_dicionario('dicionario_professor') # Carrega o arquivo json para ser o dicionario_turmas.
                if verificador_dicionario(dicionario_professores, 'professor') == False: # Verifica se o dicionario das turmas está vazia.
                    continue
                else:
                    if ver_todos(dicionario_professores, False) == False: # Chama a função de ver dos os professore que existe no dicionario dos professores.
                        continue
                    else:
                        aux = False
                        matricula = input('-'*55+'\n'"--Digite a matricula do professor ou digite '[F]' para cancelar a operação:\n 🔦 ")
                        if matricula in 'fF':
                            print('Tchau 😢.')
                        else:
                            matricula = verificador_matricula(matricula, dicionario_professores) # Verifica se a matricula digitada existe.
                            if matricula == False:
                                print("Tchau 😢.")
                            else:
                                nome_professor = input("Digite o novo nome do professor '[F]' para cancelar a operação:\n 🔦 ")
                                if nome_professor in 'fF':
                                    print('tchau 😢.')
                                else:
                                    nome_professor = nome_composto(nome_professor, 'professor') # Verifica se o novo nome do professor é composto.
                                    if nome_professor == False:
                                        continue
                                    else:
                                        # Percorre o dicionario das turmas para verifica se o professor existe na turma.
                                        for nome_disciplina, resto in dicionario_turmas.items():
                                            for matricula_professor, resto in resto.items():
                                                if matricula_professor ==  matricula:
                                                    aux = True
                                        # Se o professor estiver em alguma turma ele ver pra cá:
                                        if aux:
                                            # Percorre o dicionario das turmas novamente para editar o o nome do professor.
                                            for nome_disciplina, resto in dicionario_turmas.items():
                                                for matricula_professor, resto in resto.items():
                                                    if matricula_professor == matricula:
                                                        for nome, lista_aluno in resto.items():
                                                            dicionario_turmas[nome_disciplina][matricula] = {nome_professor: lista_aluno}
                                            # Altera 
                                            dicionario_professores[matricula] = nome_professor
                                            # Chama a função para salvar as alterações feitas até agora.
                                            salvar_dicionarios(dicionario_turmas, 'dicionario_turmas')
                                            salvar_dicionarios(dicionario_professores, 'dicionario_professor')
                                        # Se o professor tiver nenhuma turma ele entra aqui:
                                        else:
                                            dicionario_professores[matricula] = nome_professor
                                            salvar_dicionarios(dicionario_professores, 'dicionario_professor') # Chama a função para salvar as alterações feitas até agora.
            # menu [2] Professores [3] ✅
            elif op == '3':
                dicionario_professores = carregar_dicionario('dicionario_professor') # Carrega o arquivo json para ser o dicionario_professores.
                if  verificador_dicionario(dicionario_professores, 'professor') == False: # Verifica se o dicionario das turmas está vazia.
                    continue
                else:
                    ver_dados_professor(dicionario_professores) # Chama a função de ver todos os professores.
            # menu [2] Professores [4] ✅
            elif op == '4':
                dicionario_professores = carregar_dicionario('dicionario_professor') # Carrega o arquivo json para ser o dicionario_professores.
                dicionario_turmas = carregar_dicionario('dicionario_turmas') # Carrega o arquivo json para ser o dicionario_turmas.
                if verificador_dicionario(dicionario_professores, 'professor') == False: # Verifica se o dicionario dos professores está vazio.
                    continue
                else:
                    ver_todos(dicionario_professores, False) # chama a função de ver todos os professores.
                    matricula = input("Digite o numero da matricula do professor que deseja apagar ou digite '[F]' para cancelar a operação:\n 🔦 ")
                    if matricula in 'fF':
                        print("Tchau 😢.")
                    else:
                        matricula = verificador_matricula(matricula, dicionario_professores) # Verifica se a matricula digitada está existe.
                        if matricula == False:
                            print("Tchau 😢.")
                        else:
                            apagar_professor(dicionario_professores, dicionario_turmas, matricula) # Chama a função para apagar o professor.
            # menu [2] Professores [5] ✅
            elif op == '5':
                dicionario_professores = carregar_dicionario('dicionario_professor') # Carrega o arquivo json para ser o dicionario_professores.
                if verificador_dicionario(dicionario_turmas, 'turma') == False: #  Verifica se o dicionario dos professosres está vazio.
                    continue
                else:
                    ver_todos(dicionario_professores, False) # Chama a função de ver todos os professores
                    aux = False
                    matricula_digitada = input("Digite a matricula do professor que deseja visualizar as turmas ou digite '[F]' para cancelar a operação:\n 🔦 ")
                    if matricula_digitada in 'fF':
                        print("Tchau 😢.")
                    else:
                        # Percorre o dicionario das turmas para verificar se o professor existe na turma.
                        for nome_disciplina, resto in dicionario_turmas.items():
                            for matricula_professor in resto.keys():
                                if matricula_professor ==  matricula_digitada:
                                    aux = True
                        if aux:
                            matricula_digitada = verificador_matricula(matricula_digitada, dicionario_professores) # Verifica se a matricula digitada existe.
                            if matricula_digitada == False:
                                continue
                            else:
                                visualizar_turmas_professor(dicionario_turmas, 'Turmas do professor:', matricula_digitada) # Chama a função para ver as turmas do professor escolhido.
                        else:
                            print("Professor não tem nenhuma turma ❌.")
            # menu [2] Professores [6] ✅               
            elif op == '6':
                dicionario_professores = carregar_dicionario('dicionario_professor') # Carrega o arquivo json para ser o dicionario_professores.
                if verificador_dicionario(dicionario_turmas, 'turma') == False: # Verifica se o dicionario dos professores está vazio.
                    continue
                else:
                    lista_materia = ver_todas_turmas(dicionario_turmas) # Chama a função para mostrar todas as turmas que existem e pergunta qual turma que ver os alunos e professores.
                    if lista_materia == False:
                        continue
                    else:
                        opcao = input('-'*55+'\n'+"Digite o id da materia desejada ou digite '[F]' para cancelar a operação: ")
                        if opcao in 'fF':
                            pass
                        else:
                            mostrar_tudo(opcao, dicionario_turmas, lista_materia) # Chama a função para mostrar os alunos da turma escolinhada.
            elif op == 'v' or op == 'V':
                break
            else:
                print(f"\nOpção '{op}' invalida ❌.\n")
    # ✅
    elif op == '3':
        while True:
            op = menu_alunos()
            # menu [3] Alunos [1] ✅
            if op == '1':
                dicionario_alunos = carregar_dicionario('dicionario_alunos') # Carrega o arquivo json para ser o dicionario_alunos,
                nome_aluno = input('-'*55+'\n'+"Digite o nome do aluno que deseja cadastrar ou digite '[F]' para cancelar a operação:\n 🔦 ")
                if nome_aluno in 'fF':
                    print("Tchau 😢.")
                    continue
                nome_aluno = nome_composto(nome_aluno, 'aluno') # Verifica se o nome digitado é composto.
                if nome_aluno == False:
                    continue
                else:
                    cadastrar_aluno(nome_aluno, dicionario_alunos) # Chama a Função para cadastrar o aluno.


            # menu [3] Alunos [2] ✅
            elif op == '2':
                dicionario_alunos = carregar_dicionario('dicionario_alunos') # Carrega o arquivo json para ser o dicionario_alunos.
                if verificador_dicionario(dicionario_alunos, 'aluno') == False: # Verifica se o dicionario dos alunos está vazio.
                    continue
                else:
                    ver_todos(dicionario_alunos, False) # Mostra os alunos que existem.
                    matricula_aluno = input('-'*55+'\n'+"Digite a matricula do aluno que deseja editar ou digite '[F]' para cancelar a operação:\n 🔦 ")
                    if matricula_aluno in 'fF':
                        print("Tchau 😢.")
                    else:
                        matricula_aluno = verificador_matricula(matricula_aluno, dicionario_alunos) # Verifica se a matricula digitada existe.
                        if matricula_aluno == False:
                            continue
                        else:
                            editar_aluno(matricula_aluno, dicionario_alunos, dicionario_turmas) # Chama a função para editar o aluno.
            # menu [3] Alunos [3] ✅
            elif op == '3':
                dicionario_alunos = carregar_dicionario('dicionario_alunos') # Carrega o arquivo json para ser o dicionario_alunos.
                if verificador_dicionario(dicionario_alunos, 'aluno') == False: # Verifica se o dicionario dos alunos está vazio.
                    continue
                else:
                    visualizar_aluno(dicionario_alunos) # Chama a função para ver todos os aluno que existem.

            # menu [4] Alunos [4] ✅
            elif op == '4':
                dicionario_alunos = carregar_dicionario('dicionario_alunos') # Carrega o arquivo json para ser o dicioanario_alinos.
                if verificador_dicionario(dicionario_alunos, 'aluno') == False: # Verifica se o dicionario dos alunos está vazio.
                    continue
                else:
                    ver_todos(dicionario_alunos, False) # Chama a função para ver todos os alunos que existem.
                    matricula_aluno = input("Digite o numero da matricula do aluno que deseja apagar ou digite '[F]' para cancelar a operação:\n 🔦 ")
                    if matricula_aluno in 'fF':
                        print("Tchau 😢.")
                    else:
                        matricula_aluno = verificador_matricula(matricula_aluno, dicionario_alunos) # Verifica se a matricula digitada existe.
                        if matricula_aluno == False:
                            continue
                        else:
                            apagar_aluno(dicionario_alunos, matricula_aluno, dicionario_turmas) # Chama a função para apagar um aluno escolhido.

            elif op in 'vV':
                break
            else:
                print(f"\nOpção '{op}' invalida ❌.\n")

    elif op in 'fF':
        print("\nPrograma Encerrado!😪\n")
        break
    else:
        print(f"\nOpção '{op}' invalida ❌.\n")