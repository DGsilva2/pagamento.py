print('\033[31m{:*^40}\033[m'.format('RDSIMPORTS'))
preço = float(input('preço das compras R$: '))
print(''' formas de pagamento 
[1] à vista dinheiro/cheque
[2] à vista cartao
[3] 2x no cartao 
[4] 3x ou mais no cartão ''')
opçao = int(input('Qual é a opção de pagamento? '))
if opçao == 1:
    total = preço - (preço * 10 / 100)
elif opçao == 2:
    total = preço - (preço * 5 / 100)
elif opçao == 3:
    total = preço
    parcela = total / 2
    print('Sera parcelado em 2x de R$ {:.2f} SEM JUROS'.format(parcela))
elif opçao == 4:
    total = preço + (preço * 20 / 100)
    tparc = int(input('quantas parcelas ? '))
    parcelas = total / tparc
    print('sera parcelado em {}x de R${:.2f} COM JUROS'.format(tparc, parcelas))
else:
    total = preço
    print('opçao INVALIDA. Tente novamente!')
print('seu valor total é de {:.2f}'.format(total))


