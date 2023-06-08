# ------------------------------------------------------------------------
# Menu inicial do Coordenador
def menu_inicial():
    print('''
======>Menu<======
 [1] - Turmas.
 [2] - Professor.
 [3] - Alunos.
==================
    ''')
    op = input("Digite a opção desejada ou escreva 'sair': ")
    print()
    print('==================')
    return op

# ------------------------------------------------------------------------
# Menu que da acesso ao CRUD das Turmas.
def menu_turmas():
    print('''
=====>Menu das Turmas<=====

 [1] - Criar turma.
 [2] - Editar turma.
 [3] - Ver turma.
 [4] - Apagar turma.

===========================
    ''')
    op = input("Digite a opção desejada ou escreva 'voltar': ")
    print()
    print('===========================')
    return op

# ------------------------------------------------------------------------
# Menu que da acesso ao CRUD dos Professores.
def menu_professores():
    print('''
===================>Menu dos Professores<===================

 [1] - Cadastrar Professor.
 [2] - Editar Professsor.
 [3] - Ver dados do professor.
 [4] - Apagar um professor.
 [5] - Visualizar as turmas do professor.
 [6] - Visualizar os alunos da turma de um professsor.

=============================================================
    ''')
    op = input("Digite a opção desejada ou escreva 'voltar': ")
    print()
    print('=============================================================')
    return op

# ------------------------------------------------------------------------
# Menu que da acesso ao CRUD dos Alunos.
def menu_alunos():
    print('''
==========>Menu dos Alunos<==========

 [1] - Cadastrar Aluno.
 [2] - Editar Aluno.
 [3] - Visualizar Alunos.
 [4] - Apagar Aluno.

=====================================
    ''')
    op = input("Digite a opção desejada ou escreva 'voltar': ")
    print()
    print('=====================================')
    return op