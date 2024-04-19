import time
menu = ('[0] Deposito\n[1] Saque\n[2] Extrato\n[3] Sair\n')
saldo = 0
limite_saque_valor = 500
extrato = ''
numeros_saques = 0
LIMITES_SAQUES = 3

while True:
    print('')
    print('=== Aplicativo Bancario ===')
    time.sleep(0.5)
    print('')
    print(menu)
    op = int(input('--> '))
    
    if op == 0:
        valor = float(input('Digite o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += (f' Depósito: R${valor:.2f}\n')
        else:
            print('O valor não corresponde!')
    elif op == 1:
        valor = float(input(' Digite o valor do saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque_valor
        excedeu_saques = numeros_saques >= LIMITES_SAQUES        
        if excedeu_saldo:
            print(' Operação falhou! Você não tem saldo suficiente!')
        if excedeu_limite:
            print(' Operação falhou! O valor do saque excede o limite!')
        if excedeu_saques:
            print(' Operação falhou! O limite de saque foi excedido!')
        
        elif saldo > 0 and valor <= limite_saque_valor:
            saldo -= valor
            extrato += (f'\n O saque será de: {valor:.2f}')
            numeros_saques += 1
        
            
    elif op == 2:
        print('========== EXTRATO ==========')
        print('Não foram realizadas movimentações!' if not extrato else extrato)
        print(f'\n Saldo: R$ {saldo:.2f}')
        print('=============================')
    
    elif op == 3:
        print('Encerrando programa...')
        time.sleep(0.5)
        break

    