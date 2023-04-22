
import getpass
import os

print('\n            --- LISTA DE COMPRAS ---  \n')

listing = []

while True:
       
       try:
              choose_action = getpass.getpass('\n [A] anotar | [D] deletar | [V] visualizar | [S] sair \n \n ')

              if choose_action.lower() != 'a' and choose_action.lower() != 'd' and choose_action.lower() != 'v' and choose_action.lower() != 's':
                     print('Erro de digitação, escolha umas das opções.')

              elif choose_action.lower() == 'a':
                     note = input('Anotar: ')
                     os.system('cls')
                     listing.append(note.lower())
                     print(f'{note} Anotado.')
                     
              elif choose_action.lower() == 'd':
                     delete = input('Deletar: ')
                     os.system('cls')
                     listing.remove(delete.lower())
                     print(f'{delete} Deletado.')
                     
              elif choose_action.lower() == 'v':
                     os.system('cls')
                     print('Lista completa:')
                     for index, order in enumerate(listing):
                            print(f'{index} - {order}')
                     
              elif choose_action.lower() == 's':
                     os.system('cls')
                     print('Lista finalizada.')
                     for index, order in enumerate(listing):
                            print(f'{index} - {order}')
                     print('\n Saindo do Programa. \n','Boas Compras!\U0001f600 \n')
                     break 
       except Exception:
              print('Erro desconhecido.')
       except:
              print('Produto descrito não está no carrinho.')