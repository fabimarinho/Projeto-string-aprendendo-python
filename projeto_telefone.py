print('Valida e corrige número de telefone')

tel = input('Telefone: ')
tel = tel.replace('-', '')
if len(tel) == 7:
    print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
    tel = '3' + tel
    print(f'Telefone corrigido sem formatação: {tel}')
    print(f'Telefone corrigido com formatação: {tel[:4]}-{tel[4:]}')
else:
    print('O telefone não tem 7 dígitos.')
