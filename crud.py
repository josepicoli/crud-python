from os import system

def add_aluno(list):
    system('clear')
    print('< ADICIONANDO ALUNO >')
    aluno = dict()
    aluno['nome'] = str(input('Nome: ')).strip()
    aluno['matricula'] = str(input('Matrícula: ')).strip()
    aluno['curso'] = str(input('Curso: ')).strip()
    aluno['data_nasc'] = str(input('Data de Nascimento (DD/MM/AA): ')).strip()

    list.append(aluno.copy())
    print(f'Aluno {aluno["nome"]} registrado com sucesso')
    input('...')

def search_aluno(list):
    system('clear')
    print('< PESQUISAR ALUNO POR NOME >')
    nome = str(input('Digite o nome completo do aluno: ')).strip()
    for i in list:
        if i['nome'] == nome:
            print('-' * 30)
            print(f"Nome: {i['nome']}")
            print(f"Matrícula: {i['matricula']}")
            print(f"Curso: {i['curso']}")
            print(f"Data de Nascimento: {i['data_nasc']}")
            print('-' * 30)
            input('...')
            return
    print('Aluno não encontrado.')
    input('...')

def del_aluno(list):
    system('clear')
    print('< DELETA ALUNO POR NOME OU MATRÍCULA >')
    nome_matricula = str(input('Digite o nome completo ou a matrícula do aluno: ')).strip()
    for i, aluno in enumerate(list):
        if nome_matricula in [aluno['nome'], aluno['matricula']]:
            print(f'Aluno {aluno["nome"]} deletado com sucesso.')
            list.pop(i)
            input('...')
            return
    print('Aluno não encontrado.')
    input('...')

def all_alunos(list):
    system('clear')
    print('< LISTA TODOS OS ALUNOS >')
    for i in list:
        print('-' * 30)
        print(f"Nome: {i['nome']}")
        print(f"Matrícula: {i['matricula']}")
        print(f"Curso: {i['curso']}")
        print(f"Data de Nascimento: {i['data_nasc']}")
        print('-' * 30)
    input('...')

def edit_aluno(list):
    system('clear')
    print('< EDITA ALUNO POR NOME OU MATRÍCULA >')
    nome_matricula = str(input('Digite o nome completo ou a matrícula do aluno: ')).strip()
    for i in list:
        if nome_matricula in [i['nome'], i['matricula']]:
            print('-' * 30)
            print(f"Nome: {i['nome']}")
            print(f"Matrícula: {i['matricula']}")
            print(f"Curso: {i['curso']}")
            print(f"Data de Nascimento: {i['data_nasc']}")
            print('-' * 30)

            i['nome'] = str(input('Novo Nome: ')).strip()
            i['curso'] = str(input('Novo Curso: ')).strip()
            i['data_nasc'] = str(input('Nova Data de Nascimento (DD/MM/AA): ')).strip()
            print('Dados editados com sucesso.')
            input('...')
            return
    print('Aluno não encontrado.')
    input('...')

def erro(list):
    system('clear')
    print('< OPÇÃO INVÁLIDA TENTE NOVAMENTE >')
    input('...')

def menu():
    alunos = list()
    while True:
        system('clear')
        print('1. Adicionar um novo aluno.')
        print('2. Buscar aluno por nome.')
        print('3. Excluir aluno.')
        print('4. Listar todos os alunos.')
        print('5. Editar dados de um aluno.')
        print('6. Sair do programa.')

        menu_op = {
            1: add_aluno,
            2: search_aluno,
            3: del_aluno,
            4: all_alunos,
            5: edit_aluno
        }

        op = int(input('>>> '))

        if op == 6:
            system('clear')
            break

        menu_op.get(op, erro)(alunos)

menu()
