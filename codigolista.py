
import getpass
import os

print('\n            --- LISTA DE COMPRAS ---  \n')
carrinho = []

while True:
       
       try:
              escolher_acao = getpass.getpass('\n [A] anotar | [D] deletar | [V] visualizar | [S] sair \n \n ')

              if escolher_acao.lower() != 'a' and escolher_acao.lower() != 'd' and escolher_acao.lower() != 'v' and escolher_acao.lower() != 's':
                     print('Escolha umas das opções.')

              elif escolher_acao.lower() == 'a':
                     anotar = input('Anotar: ')
                     os.system('cls')
                     carrinho.append(anotar.lower())
                     print(f'{anotar} Anotado.')
                     
              elif escolher_acao.lower() == 'd':
                     deletar = input('Deletar: ')
                     os.system('cls')
                     carrinho.remove(deletar.lower())
                     print(f'{deletar} Deletado.')
                     
              elif escolher_acao.lower() == 'v':
                     os.system('cls')
                     print('Lista completa:')
                     for i,ordenar in enumerate(carrinho):
                            print(f'{i} - {ordenar}')
                     
              elif escolher_acao.lower() == 's':
                     os.system('cls')
                     print('Lista finalizada.')
                     for i,ordenar in enumerate(carrinho):
                            print(f'{i} - {ordenar}')
                     print('\n Saindo do Programa. \n','Boas Compras!\U0001f600 \n')
                     break 
       except:
              print('Erro desconhecido ou o produto descrito não está no carrinho.')