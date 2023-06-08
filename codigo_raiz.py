# Importando todas as outras pastas.
from funcoes import *
from menus import *

# Dicionario das Turmas.
dicionario_turmas = pegar_dicionario('dicionario_turmas')
# Dicionario dos Professores.
dicionario_professores = pegar_dicionario('dicionario_professor')
# Dicionario dos Alunos.
dicionario_alunos = pegar_dicionario('dicionario_alunos')

# Logica raiz do programa.
while True:
    op = menu_inicial()
    if op == '1':
        
        while True:
            op = menu_turmas()
            if op == '1':
                criar_turma(dicionario_turmas, dicionario_alunos, dicionario_professores)

            elif op == '2':
                editar_turma()
            elif op == '3':
                ver_turma()
            elif op == '4':
                apagar_aluno()
                
            elif op == 'voltar':
                break
            else:
                print()
                print(f"Opção '{op}' invalida ❌.")
                print()

    elif op == '2':
        while True:
            op = menu_professores()
            # Menu [1]
            if op == '1':
                nome_professor = input("\nDigite o nome do professor que irar cadastrar:\n 🔦 ")
                nome_professor = nome_conposto(nome_professor, 'professor')
                cadastrar_professor(nome_professor, dicionario_professores)

            # Menu [2]
            elif op == '2':
                nome = input('-'*55+'\n'"Digite o nome do professor que voçê deseja procurar:\n 🔦 ")
                print('-'*25)
                pesquisa_nomes(dicionario_professores, nome)
                matricula = input('-'*55+'\n'"--Digite a matricula do professor:\n 🔦 ")
                matricula = verificador_matricula(matricula, dicionario_professores)
                nome_professor = input('-'*55+"\n"'Digite o nome do professor que queira editar:\n 🔦 ')
                nome_professor = verificador_nome(matricula, nome_professor, dicionario_professores, 'professor')
                editar_professor(matricula, nome_professor, dicionario_professores)


            elif op == '3':
                ver_dados_professor()
            elif op == '4':
                apagar_professor()
            elif op == '5':
                visualizar_turmas_professor()
            elif op == '6':
                visualizar_alunos_turma_professor()
                
            elif op == 'voltar':
                break
            else:
                print()
                print(f"Opção '{op}' invalida ❌.")
                print()

    elif op == '3':
        while True:
            op = menu_alunos()
            if op == '1':
                cadastrar_aluno()
            elif op == '2':
                editar_aluno
            elif op == '3':
                visualizar_aluno()
            elif op == '4':
                apagar_aluno()
                
            elif op == 'voltar':
                break
            else:
                print()
                print(f"Opção '{op}' invalida ❌.")
                print()      

    elif op == 'sair':
        print("Programa Encerrado!😪")
        break
    else:
        print()
        print(f"Opção '{op}' invalida ❌.")
        print()