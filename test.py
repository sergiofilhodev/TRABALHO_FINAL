def pesquisa(dicionario):
    nome = input('Digite o nome do professor que deseja editar ou digite "sair": ')
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
            print('Tente novamente🔄.\n')
            pesquisa(dicionario)
            return False

        else:
            print("="*16+'>PESQUISA<'+"="*16)
            print(f'|{"MATRICULA":^11}{"NOME":^29}|')
            for matricula, nome in dicionario_nomes.items():
                print('|'+'-'*40+'|')
                print(f'|{matricula:^11}-{nome:^28}|')
            print('='*42)
            return True
            
dic = {
    '1':'Sergio filho',
    '2':'Sergio Sousa',
    '3':'Thomaz filho',
    '4':'Assys Sousa'
}
pesquisa(dic)