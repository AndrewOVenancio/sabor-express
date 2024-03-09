import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Eragom', 'categoria':'Chinesa', 'ativo':True},
                {'nome':'Mucho', 'categoria':'Mexicana', 'ativo':False}]


def exibir_nome_do_programa():    
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    '''Essa função é responsavel por exbir as opçoes disponiveis no programa'''
    print('1. Cadastrar restaurante')
    print('2. Lista restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Função utilizada para exibir a mensagem de Finalizando app'''
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    '''Função criada para voltar ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    '''Função de informa que a opção esta incorreta'''
    print('Opção invalida')
    voltar_ao_menu_principal()
    
def exibir_subtitulo(texto):
    '''Função  que apresenta subtitulos'''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()
    
def cadastrar_novo_restaurante():
        '''Essa função é resposavel por cadastrar um novo restaurante'''
        exibir_subtitulo('Cadastrar novo restaurante: ')
        nome_do_restaurante = input('Nome do Restaurante: ')
        categoria = input(f'Tipo de categoria {nome_do_restaurante}: ')
        dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
        restaurantes.append(dados_do_restaurante)
        print(f'Cadastrado com sucesso {nome_do_restaurante}')
        
        voltar_ao_menu_principal()

def listar_restaurantes():
    '''Função criada para exibir a lista de restaurantes cadastrado'''
    exibir_subtitulo('Listando os restaurantes')
     
    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
                       
    voltar_ao_menu_principal()   
   
def alternar_estado_restaurante():
    '''Função criada para muda o status/estado do restaurante'''
    exibir_subtitulo('Alterando estado do restaurante')  
    nome_restaurante = input('Digite o nome do restaurante que desja alterar o estado: ')
    restaurante_econtrado = False
     
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_econtrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print (mensagem)
    if not restaurante_econtrado:
        print ('O restaurante não foi encontrado')           
    
    
    voltar_ao_menu_principal() 
          
def escolher_opcao():
    '''Função criada para escolher o que desejar realizar no menu'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes() 
        elif opcao_escolhida == 3:
            alternar_estado_restaurante() 
        elif opcao_escolhida == 4:
            finalizar_app()    
        else:
            opcao_invalida( )
    except:
        opcao_invalida()
    
def main(): 
        os.system('cls')
        exibir_nome_do_programa()
        exibir_opcoes()
        escolher_opcao()
    
if __name__ == '__main__':
    main()