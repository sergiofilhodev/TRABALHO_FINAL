# # def pesquisa(dicionario):
# #     nome = input('Digite o nome do professor que deseja editar ou digite "sair": ')
# #     lista_nomes = nome.split()
# #     dicionario_nomes = {}
# #     if nome == 'sair':
# #         print('Tchau😢.')
# #         pass
# #     else:
# #         for sobrenome in lista_nomes:
# #             for matricula, nomes in dicionario.items():
# #                 if not matricula in dicionario_nomes:
# #                     for palavras in nomes.split():
# #                         if sobrenome.lower() == palavras.lower():
# #                             dicionario_nomes[matricula] = nomes
# #                         else:
# #                             pass
# #         if len(dicionario_nomes) == 0:
# #             print(f"'{nome}' não encontrado ❌.")
# #             print('Tente novamente🔄.\n')
# #             pesquisa(dicionario)
# #             return False

# #         else:
# #             print("="*16+'>PESQUISA<'+"="*16)
# #             print(f'|{"MATRICULA":^11}{"NOME":^29}|')
# #             for matricula, nome in dicionario_nomes.items():
# #                 print('|'+'-'*40+'|')
# #                 print(f'|{matricula:^11}-{nome:^28}|')
# #             print('='*42)
# #             return True
            
# # dic = {
# #     '1':'Sergio filho',
# #     '2':'Sergio Sousa',
# #     '3':'Thomaz filho',
# #     '4':'Assys Sousa'
# # }
# # pesquisa(dic)

# lista_alunos = [{'1':"sergio filho", "2":'sergio'}]
# dicionario_professores = {"1":"Sergio filho"}
# matricula_professor = "1"
# dic = {}
# dic[(matricula_professor,dicionario_professores[matricula_professor])] = lista_alunos
# print(dic)
# for nome_disciplina, matricula_professor in dicionario_turma.items():
#     if matricula_professor in matricula_digitada:
#         print(dicionario_turma)

# for nome_disciplina in dicionario_turma.keys():
#     for matricula_prof in dicionario_turmas[nome_disciplina].keys():
#         if matricula_prof == matricula_digitada:
#             print(dicionario_turma.keys())


# def ver_todas_turmas(dicionario):
#     lista_disciplinas = []
#     for nome_disciplinas in dicionario.keys():
#         lista_disciplinas.append(nome_disciplinas)
#     if len(lista_disciplinas) == 0:
#         return
#     aux = 0
#     for nome_disciplinas in lista_disciplinas:
#         aux += 1
#         print(f'|{aux:^5}{nome_disciplinas:^29}|')
#     return lista_disciplinas    


# dicionario_turmas = {"Matematica": {"2": {"S\u00e9rgio Filho": [{"1": "sergio filho"},{"2": "Vitoria Matos"}]}}, "Historia": {"2": {"S\u00e9rgio Filho": [{"1": "sergio filho"}, {"2": "Vitoria Matos"}]}}}
# lista_materia = ver_todas_turmas(dicionario_turmas)

# opcao = input("Digite a opção desejada ou '[S]'air: ")
# if opcao == "S" or opcao == 's':
#     pass
# else:
#     print('|'+'='*40+'|')
#     print(f'|{"Matricula":^20}{"Nome":^20}|')
#     for matricula_professor, nome in dicionario_turmas[lista_materia[int(opcao)-1]].items():
#         for nome_professor, alunos in nome.items():
#             for lista in alunos:
#                 for matricula_alunos, nomes_alunos in lista.items():
#                     print('|'+'-'*40+'|')
#                     print(f'|{matricula_alunos:^20}{nomes_alunos:^20}|')
#                     print('|'+'-'*40+'|')
#     print('|'+'='*40+'|')
dicionario_aluno = {"1": "Kauan Emanuel", "2": "Anderson Lucas", "3": "Yasmim Moura"}
dicionario_professor = {"1": "Thomaz maia", "3": "Cataryna Fontenele"}
dicionario_turma = {"Matematica": {"3": {"Cataryna Fontenele": [{"1": "Kauan Emanuel"}, {"2": "Anderson Lucas"}]}}}

def menu_edita_turma():
    print('''
==========>Menu da edição<==========
[1] - Trocar professor.
[2] - Deletar aluno.
[3] - Inserir aluno.
====================================
    ''')
    op = input("Digite um opção ou digite '[F]' para sair:\n 🔦 ")
    print("\n====================================")
    return op
