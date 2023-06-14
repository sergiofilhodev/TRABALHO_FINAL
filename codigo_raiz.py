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

            # menu [1] ✅
            if op == '1':
                nome_disciplina = input('-'*55+'\n'+"Digite o nome da disciplina ou digite '[S]'air:\n 🔦 ").title()
                if nome_disciplina == 'S' or nome_disciplina.lower() == 's':
                    print("Tchau 😢.")
                    continue
                else:
                    criar_turma(dicionario_turmas, dicionario_alunos, dicionario_professores, nome_disciplina)

            elif op == '2':
                lista_materia = ver_todas_turmas(dicionario_turmas)
                if lista_materia == False:
                    pass
                else:
                    opcao = input('-'*55+'\n'+"Digite o numero da materia que deseja mostrar os alunos editar ou digite '[S]'air:\n 🔦 ")
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
                                    for nome_disciplina, matricula_professor in dicionario_turmas.items():
                                        if nome_disciplina == dicionario_turmas[lista_materia[int(opcao)-1]]:
                                            lista_materia.append()
                                            for nome_professor, lista_alunos in matricula_professor.items():
                                                lista_alunos = lista_alunos
                                    matricula_professor = input("Digite a matricula do professor novo ou digite '[F]' para cancelar a troca:\n 🔦 ")
                                    if matricula_professor == 'F' or matricula_professor == 'f':
                                        print('Operação Cancelada.')
                                    else:
                                        matricula_professor = verificador_matricula(matricula_professor, dicionario_professores)
                                        if matricula_professor == False:
                                            continue
                                        else:
                                                ver_lista(dicionario_professores, 'Lista dos professores')
                                                matricula_professor = input("Digite a matricula do professor:\n 🔦 ")
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
                                                            editar_turma(lista_materia[int(opcao)-1], dicionario_turmas, matricula_professor, novo_professor, lista_alunos)
            elif op == '3':
                ver_turma()
            elif op == '4':
                apagar_aluno()


            # menu [5] ✅
            elif op == '5':
                verificador_dicionario(dicionario_turmas, 'turma')
                lista_materia = ver_todas_turmas(dicionario_turmas)
                if lista_materia == False:
                    continue
                else:
                    opcao = input('-'*55+'\n'+"Digite a materia desejada ou digite '[S]'air: ")
                    if opcao == "S" or opcao == 's':
                        pass
                    else:
                        mostrar_tudo(opcao, dicionario_turmas, lista_materia)


            elif op == 'voltar':
                break
            else:
                print('\n\n'+f"Opção '{op}' invalida ❌."+'\n\n')


    # ✅✅✅✅✅✅✅✅
    elif op == '2':
        while True:
            op = menu_professores()


            # Menu [1] ✅
            if op == '1':
                nome_professor = input('-'*55+'\n'+"\nDigite o nome do professor que irar cadastrar ou digite 'sair':\n 🔦 ")
                if nome_professor != 'sair':
                    nome_professor = nome_conposto(nome_professor, 'professor')
                    cadastrar_professor(nome_professor, dicionario_professores)
                else:
                    print("Tchau 😢.")
                    continue


            # Menu [2] ✅
            elif op == '2':
                nome = input('-'*55+'\n'"Digite o nome do professor que voçê deseja procurar ou digite 'sair':\n 🔦 ")
                print('-'*25)
                if nome != 'sair':
                    pesquisa_nomes(dicionario_professores, nome)
                    matricula = input('-'*55+'\n'"--Digite a matricula do professor ou digite 'sair':\n 🔦 ")
                    if matricula != 'sair':
                        matricula = verificador_matricula(matricula, dicionario_professores)
                        nome_professor = input('-'*55+"\n"'Digite o nome do professor que queira editar ou digite "sair":\n 🔦 ')
                        if nome_professor != 'sair':
                            nome_professor = verificador_nome(matricula, nome_professor, dicionario_professores, 'professor')
                            editar_professor(matricula, nome_professor, dicionario_professores)
                        else:
                            print('Tchau 😢.')
                    else:
                        print('Tchau 😢.')
                else:
                    print('Tchau 😢.')
                    continue


            # menu [3] ✅
            elif op == '3':
                ver_dados_professor(dicionario_professores)


            # menu [4] ✅
            elif op == '4':
                apagar_professor(dicionario_professores)


            # menu [5] ✅    
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
                                            
            elif op == '6':
                visualizar_alunos_turma_professor()
                
            elif op == 'voltar':
                break
            else:
                print()
                print(f"Opção '{op}' invalida ❌.")
                print()

    # ✅✅✅✅✅✅✅✅
    elif op == '3':
        while True:
            op = menu_alunos()


            # menu [1] ✅
            if op == '1':
                nome_aluno = input('-'*55+'\n'+"Digite o nome do aluno que deseja cadastrar:\n 🔦 ")
                nome_aluno = nome_conposto(nome_aluno, 'aluno')
                if nome_aluno == False:
                    continue
                else:
                    cadastrar_aluno(nome_aluno, dicionario_alunos)


            # menu [2] ✅
            elif op == '2':
                if verificador_dicionario(dicionario_alunos, 'aluno') == False:
                    continue
                else:
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


            # menu [3] ✅
            elif op == '3':
                nome_aluno = input("Digite o nome do aluno que deseja vê os dados ou digite '[s]'air:\n 🔦 ")
                visualizar_aluno(dicionario_alunos, nome_aluno)


            # menu [4] ✅
            elif op == '4':
                if verificador_dicionario(dicionario_alunos, 'aluno') == False:
                    continue
                else:
                    matricula_aluno = input("Digite o numero da matricula do aluno que deseja apagar ou digite '[S]'air:\n 🔦 ")
                    if matricula_aluno == 'S' or matricula_aluno == 's':
                        print("Tchau 😢.")
                    else:
                        matricula_aluno = verificador_matricula(matricula_aluno, dicionario_alunos)
                        if matricula_aluno == False:
                            continue
                        else:
                            nome_aluno = input("Digite o nome do aluno que deseja apagar ou digite '[S]'air:\n 🔦 ")
                            if nome_aluno == "S" or nome_aluno == "s":
                                print("Tchau 😢.")
                            else:
                                nome_aluno = verificador_nome(matricula, nome_aluno, dicionario_alunos, 'aluno')
                                if nome_aluno == False:
                                    continue
                                else:
                                    apagar_aluno(dicionario_alunos, matricula_aluno)


            elif op == 'voltar':
                break
            else:
                print(f"\nOpção '{op}' invalida ❌.\n")
                

    elif op == 'sair':
        print("\nPrograma Encerrado!😪")
        break
    else:
        print(f"\nOpção '{op}' invalida ❌.\n")