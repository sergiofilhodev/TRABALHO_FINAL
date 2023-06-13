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
                nome_disciplina = input('-'*55+'\n'+"Digite o nome da disciplina:\n 🔦 ").title()
                criar_turma(dicionario_turmas, dicionario_alunos, dicionario_professores, nome_disciplina)

            elif op == '2':
                editar_turma()
            elif op == '3':
                ver_turma()
            elif op == '4':
                apagar_aluno()


            # menu [5] ✅
            elif op == '5':
                lista_materia = ver_todas_turmas(dicionario_turmas)
                if lista_materia == False:
                    continue
                else:
                    opcao = int(input('-'*55+'\n'+"Digite a opção desejada ou '[S]'air: "))-1
                    if opcao == "S" or opcao == 's':
                        pass
                    else:
                        print('|'+'='*40+'|')
                        print(f'|{"Matricula":^20}{"Nome":^20}|')
                        for matricula_professor, nome in dicionario_turmas[lista_materia[int(opcao)-1]].items():
                            for nome_professor, alunos in nome.items():
                                for lista in alunos:
                                    for matricula_alunos, nomes_alunos in lista.items():
                                        print('|'+'-'*40+'|')
                                        print(f'|{matricula_alunos:^20}{nomes_alunos:^20}|')
                                        print('|'+'-'*40+'|')
                        print('|'+'='*40+'|')


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