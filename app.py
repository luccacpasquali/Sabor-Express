import os

restaurantes = [{'Nome':'Praça', 'Categoria':'Japonesa','Ativo':False},
                {'Nome':'Lucca', 'Categoria':'Café','Ativo':True},
                {'Nome':'Livia\'s', 'Categoria':'Caseiro','Ativo':False}
                ]

def main():

    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['Nome']
        categoria = restaurante['Categoria']
        ativo = restaurante['Ativo']
        print(f'-{nome_restaurante} | {categoria} | {ativo}')
    voltar_menu()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de Restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria,ativo:False}

    restaurantes.append(dados_do_restaurante) 
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    voltar_menu()

def alternar_estado_restaurante():error: failed to push some refs to 'https://github.com/luccacpasquali/Sabor-Express.git'
    print ("teste")
    

def voltar_menu():
    input('\nDigite qualquer tecla para voltar ao menu principal: ')
    os.system('cls')
    main()

def opcao_invalida():
    print('Opção invalida\n')
    voltar_menu()

def finalizar_app():
    listar_restaurantes('Finalizando')

def exibir_nome_programa():
    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    ''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

if __name__ == '__main__':
    main()

