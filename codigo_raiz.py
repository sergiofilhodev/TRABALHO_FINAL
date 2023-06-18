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
    op = menu_inicial()
    # 🔄🔄🔄🔄🔄🔄🔄🔄
    if op == '1':
        while True:
            op = menu_turmas()
            # menu [1] Turmas [1]✅
            if op == '1':
                dicionario_turmas = carregar_dicionario('dicionario_turmas')
                dicionario_professores = carregar_dicionario('dicionario_professor')
                dicionario_alunos = carregar_dicionario('dicionario_alunos')
                if verificador_dicionario(dicionario_professores, 'professor') == True and verificador_dicionario(dicionario_alunos, 'aluno') == True:
                    nome_disciplina = input('-'*55+'\n'+"Digite o nome da disciplina ou digite '[F]' para cancelar a operação:\n 🔦 ").title()
                    if nome_disciplina == 'F':
                        print("Tchau 😢.")
                        continue
                    else:
                        criar_turma(dicionario_turmas, dicionario_alunos, dicionario_professores, nome_disciplina)

            # menu [1] Turmas [2] ✅
            elif op == '2':
                if verificador_dicionario(dicionario_professores, 'professor') == True and verificador_dicionario(dicionario_alunos, 'aluno') == True:
                    lista_materia = ver_todas_turmas(dicionario_turmas)
                    if lista_materia == False:
                        pass
                    else:
                        opcao = input('-'*55+'\n'+"Digite o numero da materia que deseja mostrar os alunos e e fazer as operações seguintes ou digite '[F]' para cancelar a operação:\n 🔦 ")
                        if opcao == 'f' or opcao == 'F':
                            pass
                        else:
                            mostrar_tudo(opcao, dicionario_turmas, lista_materia)
                            while True:
                                op = menu_edita_turma()
                                if op == 's' or op == 'S':
                                    print("Tchau 😢.")
                                    break
                                elif op == '1':
                                    dicionario_turmas = carregar_dicionario('dicionario_turmas')
                                    if verificador_dicionario(dicionario_turmas, 'turmas') == False:
                                        continue
                                    else:
                                        for nome_disciplina, resto in dicionario_turmas.items():
                                            if nome_disciplina == lista_materia[int(opcao)-1]:
                                                lista_materia.append(nome_disciplina)
                                                for matricula_professor, resto in resto.items():
                                                    for nome_professor, lista_alunos in resto.items():
                                                        alunos = lista_alunos
                                        ver_dicionario(dicionario_professores, 'Lista dos professores')
                                        matricula_professor = input("Digite a matricula do novo professor ou digite '[F]' para cancelar a troca:\n 🔦 ")
                                        if matricula_professor == 'F' or matricula_professor == 'f':
                                            print('Operação Cancelada.')
                                        else:
                                            matricula_professor = verificador_matricula(matricula_professor, dicionario_professores)
                                            if matricula_professor == False:
                                                continue
                                            else:
                                                editar_turma(lista_materia[int(opcao)-1], dicionario_turmas, matricula_professor, False, alunos, False, False, dicionario_professores)

                                elif op == '2':
                                    dicionario_turmas = carregar_dicionario('dicionario_turmas')
                                    if verificador_dicionario(dicionario_turmas, 'turmas') == False:
                                        continue
                                    else:
                                        dicionario = {}
                                        for nome_disciplina, resto in dicionario_turmas.items():
                                            if nome_disciplina == lista_materia[int(opcao)-1]:
                                                for matricula_professor, resto in resto.items():
                                                    for nome_professor, resto in resto.items():
                                                        for lista_alunos in resto:
                                                            for matricula_aluno, nome_aluno in lista_alunos.items():
                                                                dicionario[matricula_aluno] = nome_aluno
                                        if len(dicionario) == 0:
                                            print("Não existe nenhum aluno na turma para remover ❌.")
                                        else:
                                            ver_dicionario(dicionario, 'lista dos alunos')
                                            matricula_remover = input("Digite a matricula do aluno que desejas remover ou digite '[F]' para cancelar a operação:\n🔦 ")
                                            if matricula_remover == 'f' or matricula_remover == 'F':
                                                print("Tchau 😢.")
                                            else:
                                                matricula_remover = verificador_matricula(matricula_remover, dicionario)
                                                if matricula_remover == False:
                                                    continue
                                                else:
                                                    editar_turma(lista_materia[int(opcao)-1], dicionario_turmas, matricula_professor, nome_professor, False, False, matricula_remover, False, False)

                                elif op == '3':
                                    dicionario_turmas = carregar_dicionario('dicionario_turmas')
                                    if verificador_dicionario(dicionario_turmas, 'turmas') == False:
                                        continue
                                    else:
                                        dicionario = {}
                                        for nome_disciplina, resto in dicionario_turmas.items():
                                            if nome_disciplina == lista_materia[int(opcao)-1]:
                                                for matricula_professor, resto in resto.items():
                                                    for nome_professor, lista_alunos in resto.items():
                                                            for alunos in lista_alunos:
                                                                for matricula_aluno, nome_aluno in alunos.items():
                                                                    dicionario[matricula_aluno] = nome_aluno
                                        ver_dicionario(dicionario_alunos, 'lista dos alunos')
                                        matricula_aluno_novo = input("Digite a matricula do aluno que desejas aicionar ou digite '[F]' para cancelar a operação:\n🔦 ")
                                        if matricula_aluno_novo == 'f' or matricula_aluno_novo == 'F':
                                            print("Tchau 😢.")
                                            continue
                                        else:
                                            matricula_aluno_novo = verificador_matricula(matricula_aluno_novo, dicionario_alunos)
                                            if matricula_aluno_novo == False:
                                                continue
                                            else:
                                                editar_turma(nome_disciplina, dicionario_turmas, matricula_professor, nome_professor, lista_alunos, matricula_aluno_novo, dicionario_alunos, False)

                                elif op == 'f' or op == 'F':
                                    break
                                else:
                                    print('\n\n'+f"Opção '{op}' invalida ❌."+'\n\n')
            
            # menu [1] Turmas [3]
            elif op == '3':
                dicionario_turmas = carregar_dicionario('dicionario_turmas')
                if verificador_dicionario(dicionario_turmas, 'turma') == False:
                    continue
                else:
                    lista_materia = ver_todas_turmas(dicionario_turmas)
                    if lista_materia == False:
                        continue
                    else:
                        opcao = input('-'*55+'\n'+"Digite o numero da materia desejada ou digite digite '[F]' para cancelar a operação:\n 🔦 ")
                        if opcao == 'f' or opcao == 'F':
                            pass
                        else:
                            ver_dicionario(dicionario_professores, 'Lista dos professores')
                            ver_dicionario(dicionario_alunos, 'Lista dos alunos')

            # menu [1] Turmas [4] ✅
            elif op == '4':
                dicionario_turmas = carregar_dicionario('dicionario_turmas')
                if verificador_dicionario(dicionario_turmas, 'turma') == False:
                    continue
                else:
                    dicionario_turmas = carregar_dicionario('dicionario_turmas')
                    lista_turmas = ver_todas_turmas(dicionario_turmas)
                    if lista_turmas == False:
                        continue
                    else:
                        opcao = input('-'*55+'\n'+"Digite o numero da materia que deseja apagar ou digite digite '[F]' para cancelar a operação:\n 🔦 ")
                        if opcao == 'f' or opcao =='F':
                            print("Tchau 😢.")
                            continue
                        else:
                            apagar_turma(dicionario_turmas, lista_turmas[int(opcao)-1])

            elif op == 'V' or op == 'v':
                break
            else:
                print(f"\nOpção '{op}' invalida ❌.\n")


    # ✅✅✅✅✅✅✅✅
    elif op == '2':
        while True:
            op = menu_professores()


            # Menu [2] Professores [1] ✅
            if op == '1':
                dicionario_professores = carregar_dicionario('dicionario_professor')
                nome_professor = input('-'*55+'\n'+"\nDigite o nome do professor que irar cadastrar ou digite '[F]' para deixar operação:\n 🔦 ")
                if nome_professor == 'f' or nome_professor == 'F':
                    print("Tchau 😢.")
                    continue
                else:
                    nome_professor = nome_composto(nome_professor, 'professor')
                    cadastrar_professor(nome_professor, dicionario_professores)


            # Menu [2] Professores [2] ✅
            elif op == '2':
                dicionario_professores = carregar_dicionario('dicionario_professor')
                if verificador_dicionario(dicionario_professores, 'professor') == False:
                    continue
                else:
                    if ver_todos(dicionario_professores, False) == False:
                        continue
                    else:
                        aux = False
                        matricula = input('-'*55+'\n'"--Digite a matricula do professor ou digite '[F]' para cancelar a operação:\n 🔦 ")
                        if matricula == 'f' or matricula == 'F':
                            print('Tchau 😢.')
                        else:
                            matricula = verificador_matricula(matricula, dicionario_professores)
                            if matricula == False:
                                print("Tchau 😢.")
                            else:
                                nome_professor = input("Digite o novo nome do professor '[F]' para cancelar a operação:\n 🔦 ")
                                if nome_professor == 'f' or nome_professor == 'F':
                                    print('tchau 😢.')
                                else:
                                    nome_professor = nome_composto(nome_professor, 'professor')
                                    if nome_professor == False:
                                        continue
                                    else:
                                        for nome_disciplina, resto in dicionario_turmas.items():
                                            for matricula_professor, resto in resto.items():
                                                if matricula_professor ==  matricula:
                                                    aux = True
                                        if aux:
                                            for nome_disciplina, resto in dicionario_turmas.items():
                                                for matricula_professor, resto in resto.items():
                                                    if matricula_professor == matricula:
                                                        for nome, lista_aluno in resto.items():
                                                            print(lista_aluno)
                                                            dicionario_turmas[nome_disciplina][matricula] = {nome_professor: lista_aluno}
                                            dicionario_professores[matricula] = nome_professor
                                            salvar_dicionarios(dicionario_turmas, 'dicionario_turmas')
                                            salvar_dicionarios(dicionario_professores, 'dicionario_professor')
                                        else:
                                            dicionario_professores[matricula] = nome_professor
                                            salvar_dicionarios(dicionario_professores, 'dicionario_professor')
                                    # editar_professor(matricula, dicionario_professores)


            # menu [2] Professores [3] ✅
            elif op == '3':
                dicionario_professores = carregar_dicionario('dicionario_professor')
                if  verificador_dicionario(dicionario_professores, 'professor') == False:
                    continue
                else:
                    carregar_dicionario('dicionario_professor')
                    ver_dados_professor(dicionario_professores)


            # menu [2] Professores [4] ✅
            elif op == '4':
                apagar_professor(dicionario_professores)


            # menu [2] Professores [5] ✅
            elif op == '5':
                dicionario_professores = carregar_dicionario('dicionario_professor')
                if verificador_dicionario(dicionario_turmas, 'turma') == False:
                    continue
                else:
                    nome_pesquisa = input('-'*55+'\n'"Digite o nome do professor que voçe queira procurar ou digite 'sair':\n 🔦 ")
                    if pesquisa_nomes(dicionario_professores, nome_pesquisa) == False:
                        continue
                    else:
                        aux = False
                        matricula_digitada = input("Digite a matricula do professor que deseja visualizar as turmas ou digite '[S]'air:\n 🔦 ")
                        for nome_disciplina, resto in dicionario_turmas.items():
                            for matricula_professor in resto.keys():
                                if matricula_professor ==  matricula_digitada:
                                    aux = True
                        if matricula_digitada == 'S' or matricula_digitada == 's':
                            continue
                        else:
                            matricula_digitada = verificador_matricula(matricula_digitada, dicionario_professores)
                            if matricula_digitada == False:
                                continue
                            else:
                                visualizar_turmas_professor(dicionario_turmas, 'Turmas do professor:', matricula_digitada)

            # menu [2] Professores [6] ✅               
            elif op == '6':
                dicionario_professores = carregar_dicionario('dicionario_professor')
                verificador_dicionario(dicionario_turmas, 'turma')
                lista_materia = ver_todas_turmas(dicionario_turmas)
                if lista_materia == False:
                    continue
                else:
                    opcao = input('-'*55+'\n'+"Digite o id da materia desejada ou digite '[S]'air: ")
                    if opcao == "S" or opcao == 's':
                        pass
                    else:
                        mostrar_tudo(opcao, dicionario_turmas, lista_materia)
                
            elif op == 'v' or op == 'V':
                break
            else:
                print(f"\nOpção '{op}' invalida ❌.\n")

    # ✅✅✅✅✅✅✅✅
    elif op == '3':
        while True:
            op = menu_alunos()

            # menu [3] Alunos [1] ✅
            if op == '1':
                dicionario_alunos = carregar_dicionario('dicionario_alunos')
                nome_aluno = input('-'*55+'\n'+"Digite o nome do aluno que deseja cadastrar ou digite '[F]' para cancelar a operação:\n 🔦 ")
                if nome_aluno == 'f' or nome_aluno == 'F':
                    print("Tchau 😢.")
                    continue
                nome_aluno = nome_composto(nome_aluno, 'aluno')
                if nome_aluno == False:
                    continue
                else:
                    cadastrar_aluno(nome_aluno, dicionario_alunos)


            # menu [3] Alunos [2] ✅
            elif op == '2':
                dicionario_alunos = carregar_dicionario('dicionario_alunos')
                if verificador_dicionario(dicionario_alunos, 'aluno') == False:
                    continue
                else:
                    dicionario_alunos = carregar_dicionario('dicionario_alunos')
                    ver_todos(dicionario_alunos, False)
                    matricula_aluno = input('-'*55+'\n'+"Digite a matricula do aluno que deseja editar:\n 🔦 ")
                    matricula_aluno = verificador_matricula(matricula_aluno, dicionario_alunos)
                    if matricula_aluno == False:
                        continue
                    else:    
                        editar_aluno(matricula_aluno, dicionario_alunos)

            # menu [3] Alunos [3] ✅
            elif op == '3':
                dicionario_alunos = carregar_dicionario('dicionario_alunos')
                if verificador_dicionario(dicionario_alunos, 'aluno') == False:
                    continue
                else:
                    visualizar_aluno(dicionario_alunos)

            # menu [4] Alunos [4] ✅
            elif op == '4':
                dicionario_alunos = carregar_dicionario('dicionario_alunos')
                if verificador_dicionario(dicionario_alunos, 'aluno') == False:
                    continue
                else:
                    dicionario_alunos = carregar_dicionario('dicionario_alunos')
                    ver_todos(dicionario_alunos, False)
                    matricula_aluno = input("Digite o numero da matricula do aluno que deseja apagar ou digite '[F]' para cancelar a operação:\n 🔦 ")
                    if matricula_aluno == 'f' or matricula_aluno == 'F':
                        print("Tchau 😢.")
                    else:
                        matricula_aluno = verificador_matricula(matricula_aluno, dicionario_alunos)
                        if matricula_aluno == False:
                            continue
                        else:
                            apagar_aluno(dicionario_alunos, matricula_aluno)

            elif op == 'V' or op == 'v':
                break
            else:
                print(f"\nOpção '{op}' invalida ❌.\n")

    elif op == 'F' or op == 'f':
        print("\nPrograma Encerrado!😪\n")
        break
    else:
        print(f"\nOpção '{op}' invalida ❌.\n")