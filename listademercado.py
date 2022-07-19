listagem = []

while True:
  try:
    item = input('Qual o item cadastrado? \n')
    quantidade = int(input('Quantas unidades de {} serão cadastradas? \n'.format(item)))
    valor = float(input('qual o valor unitario de {}? \n'.format(item)))
    tabela = {'item': item,
              'quantidade': quantidade,
              'valor': valor}
    listagem.append(tabela.copy())

  except:
    print('Erro de digitação, tente novamente') 
    continue
  mais_item = input('Cadastrar mais itens? (s/n) ')
  if mais_item == 's':
    continue
  elif mais_item =='n':
    break
  else:
    print('opção invalida')
    continue

for i in listagem:
   for e,j in i.items():
    print('{} : {}'.format(e,j))

    
  
