# Importando todas as outras pastas.
from funcoes import*
from menus import*

# Dicionario das Turmas.
dicionario_turmas = pegar_dicionario('dicionario_turmas')
# Dicionario dos Professores.
dicionario_professores = pegar_dicionario('dicionario_professor')
# Dicionario dos Alunos.
dicionario_alunos = pegar_dicionario('dicionario_alunos')

# Logica raiz do programa.
while True:
    op = menu_inicial()
    # 🔄🔄🔄🔄🔄🔄🔄🔄
    if op == '1':
        while True:
            op = menu_turmas()

            # menu [1] Turmas [1]✅
            if op == '1':
                verificador_dicionario(dicionario_professores, 'professor')
                verificador_dicionario(dicionario_alunos, 'aluno')
                if verificador_dicionario(dicionario_professores, 'professor') == True and verificador_dicionario(dicionario_alunos, 'aluno') == True:
                    nome_disciplina = input('-'*55+'\n'+"Digite o nome da disciplina ou digite '[F]' para cancelar a operação:\n 🔦 ").title()
                    if nome_disciplina == 'F':
                        print("Tchau 😢.")
                        continue
                    else:
                        criar_turma(dicionario_turmas, dicionario_alunos, dicionario_professores, nome_disciplina)

            # menu [1] Turmas [2] ✅
            elif op == '2':
                lista_materia = ver_todas_turmas(dicionario_turmas)
                if lista_materia == False:
                    pass
                else:
                    opcao = input('-'*55+'\n'+"Digite o numero da materia que deseja mostrar os alunos e editar ou digite '[S]'air:\n 🔦 ")
                    if opcao == "S":
                        pass
                    else:
                        mostrar_tudo(opcao, dicionario_turmas, lista_materia)
                        while True:
                            op = menu_edita_turma()
                            if op == 'S' or op == 's':
                                print("Tchau 😢.")
                                break
                            elif op == '1':
                                if verificador_dicionario(dicionario_turmas, 'turmas') == False:
                                    continue
                                else:
                                    alunos = []
                                    for nome_disciplina, matricula_professor in dicionario_turmas.items():
                                        if nome_disciplina == dicionario_turmas[lista_materia[int(opcao)-1]]:
                                            lista_materia.append(nome_disciplina)
                                            for nome_professor, lista_alunos in matricula_professor.items():
                                                alunos.append(lista_alunos)
                                                
                                    ver_lista(dicionario_professores, 'Lista dos professores')
                                    matricula_professor = input("Digite a matricula do novo professor ou digite '[F]' para cancelar a troca:\n 🔦 ")
                                    if matricula_professor == 'F' or matricula_professor == 'f':
                                        print('Operação Cancelada.')
                                    else:
                                        matricula_professor = verificador_matricula(matricula_professor, dicionario_professores)
                                        if matricula_professor == False:
                                            continue
                                        else:
                                            novo_professor = input("Digite o novo nome do professor ou digite '[F]' para cancelar a troca:\n 🔦 ")
                                            if novo_professor == "F" or novo_professor == 'f':
                                                print('Operação Cancelada.')
                                            else:
                                                novo_professor = verificador_nome(matricula_professor, novo_professor, dicionario_professores, 'professor')
                                                if novo_professor == False:
                                                    continue
                                                else:
                                                    editar_turma(lista_materia[int(opcao)-1], dicionario_turmas, matricula_professor, novo_professor, alunos)
                            elif op == 'f' or op == 'F':
                                break
                            else:
                                print('\n\n'+f"Opção '{op}' invalida ❌."+'\n\n')
            
            # menu [1] Turmas [3]
            elif op == '3':
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
                            mostrar_tudo(opcao, dicionario_turmas, lista_materia)

            # menu [1] Turmas [4] ✅
            elif op == '4':
                if verificador_dicionario(dicionario_turmas, 'turmas') == False:
                    continue
                else:
                    dicionario_turmas = pegar_dicionario('dicionario_turmas')
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
                nome_professor = input('-'*55+'\n'+"\nDigite o nome do professor que irar cadastrar ou digite '[F]' para deixar operação:\n 🔦 ")
                if nome_professor == 'f' or nome_professor == 'F':
                    print("Tchau 😢.")
                    continue
                else:
                    nome_professor = nome_composto(nome_professor, 'professor')
                    cadastrar_professor(nome_professor, dicionario_professores)


            # Menu [2] Professores [2] ✅
            elif op == '2':
                if ver_todos(dicionario_professores, False) == False:
                    continue
                else:
                    matricula = input('-'*55+'\n'"--Digite a matricula do professor ou digite '[F]' para cancelar a operação:\n 🔦 ")
                    if matricula == 'f' or matricula == 'F':
                        print('Tchau 😢.')
                    else:
                        matricula = verificador_matricula(matricula, dicionario_professores)
                        if matricula == False:
                            print("Tchau 😢.")
                        else:
                            nome_professor = input('-'*55+"\n""Digite o nome do professor que queira editar ou digite '[F]' para cancelar a operação:\n 🔦 ")
                            if nome_professor == 'f' or nome_professor == 'F':
                                print('Tchau 😢.')
                            else:
                                nome_professor = verificador_nome(matricula, nome_professor, dicionario_professores, 'professor')
                                if nome_professor == False:
                                    print("Tchau 😢.")
                                else:
                                    editar_professor(matricula, nome_professor, dicionario_professores)


            # menu [2] Professores [3] ✅
            elif op == '3':
                if  verificador_dicionario(dicionario_professores, 'professor') == False:
                    continue
                else:
                    pegar_dicionario('dicionario_professor')
                    ver_dados_professor(dicionario_professores)


            # menu [2] Professores [4] ✅
            elif op == '4':
                apagar_professor(dicionario_professores)


            # menu [2] Professores [5] ✅
            elif op == '5':
                if verificador_dicionario(dicionario_turmas, 'turma') == False:
                    continue
                else:
                    nome_pesquisa = input('-'*55+'\n'"Digite o nome do professor que voçe queira procurar ou digite 'sair':\n 🔦 ")
                    if pesquisa_nomes(dicionario_professores, nome_pesquisa) == False:
                        continue
                    else:
                        matricula_digitada = input("Digite a matricula do professor que deseja visualizar as turmas ou digite '[S]'air:\n 🔦 ")
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
                if verificador_dicionario(dicionario_alunos, 'aluno') == False:
                    continue
                else:
                    dicionario_alunos = pegar_dicionario('dicionario_alunos')
                    ver_todos(dicionario_alunos, False)
                    matricula_aluno = input('-'*55+'\n'+"Digite a matricula do aluno que deseja editar:\n 🔦 ")
                    matricula_aluno = verificador_matricula(matricula_aluno, dicionario_alunos)
                    if matricula_aluno == False:
                        continue
                    else:
                        nome_aluno = input('-'*55+'\n'+f"Digite o nome do aluno '{matricula_aluno}' que deseja editar:\n 🔦 ")
                        nome_aluno = verificador_nome(matricula_aluno, nome_aluno, dicionario_alunos, 'aluno')
                        if verificador_nome(matricula_aluno, nome_aluno, dicionario_alunos, 'aluno') == False:
                            continue
                        else:
                            editar_aluno(matricula_aluno, nome_aluno, dicionario_alunos)

            # menu [3] Alunos [3] ✅
            elif op == '3':
                visualizar_aluno(dicionario_alunos)

            # menu [4] Alunos [4] ✅
            elif op == '4':
                if verificador_dicionario(dicionario_alunos, 'aluno') == False:
                    continue
                else:
                    dicionario_alunos = pegar_dicionario('dicionario_alunos')
                    ver_todos(dicionario_alunos, False)
                    matricula_aluno = input("Digite o numero da matricula do aluno que deseja apagar ou digite '[F]' para cancelar a operação:\n 🔦 ")
                    if matricula_aluno == 'f' or matricula_aluno == 'F':
                        print("Tchau 😢.")
                    else:
                        matricula_aluno = verificador_matricula(matricula_aluno, dicionario_alunos)
                        if matricula_aluno == False:
                            continue
                        else:
                            nome_aluno = input("Digite o nome do aluno que deseja apagar ou digite '[F]' para cancelar a operação:\n 🔦 ")
                            if nome_aluno == 'F' or nome_aluno == 'F':
                                print("Tchau 😢.")
                            else:
                                nome_aluno = verificador_nome(matricula_aluno, nome_aluno, dicionario_alunos, 'aluno')
                                if nome_aluno == False:
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