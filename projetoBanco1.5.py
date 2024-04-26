import time
import os
import textwrap
def menu():
    menu = '''
    
    ========== MENU ==========
    [d] Deposito
    [s] Saque
    [e] Extrato
    [nc] Nova conta
    [lc] Listar conta
    [nu] Novo usuario
    [sa] Sair
    ==> '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}'
        print('\n=== Depósito realizado com sucesso ===')
    else:
        print('### A operação falhou! O valor informado é inválido. ###')
    time.sleep(1.5)
    os.system('cls')
    return saldo, extrato
    

def sacar(*, saldo, valor, extrato, limite, numero_saques, limites_saques):
    valor = float(input('  (Limite de saque de R$500,00.)\n  Digite o valor do saque:  '))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limites_saques 
    if excedeu_saldo:
        print('### A operação falhou! O valor informado é inválido. ###')
    if excedeu_limite:
        print('### A operação falhou! O valor informado é inválido. ###')
    if excedeu_saques:
        print('### A operação falhou! O valor informado é inválido. ###')
    else:
        valor -= saldo
        extrato += f'Saque:\tR$ {valor:.2f} \n'
        numeros_saques += 1
        print('\n=== Saque realizado com sucesso ===')

def exibir_extrato(saldo, /, extrato):
    
        print('========== EXTRATO ==========')
        print('Não foram realizadas movimentações!' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f} ')
        print('=============================')
        

def criar_usuario(usuarios):
    cpf = int(input(' Digite seu CPF (somente números): '))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n### CPF já existente! ###')
        return
    nome = input('Digite seu nome completo: ')
    data_nascimento = int(input('Digite sua data de nascimento (dd-mm-aaaa): '))
    endereco = input('Digite seu endereco (logradouro, nro - bairro - cidade/sigla estado): ')
    usuarios.append({'nome':nome,'data_nascimento':data_nascimento,'cpf':cpf,'endereco':endereco})

    print('=== Usuario criado com sucesso! ===')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [ usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('\n=== Contra criada com sucesso! ===')
        return {'agencia':agencia,'numero_conta':numero_conta,'usuario':usuario}
    print('\n### Usuário não encontrado, fluxo de criação de conta encerrado! ###')


def listar_contas(contas):
    for conta in contas:
        linha = f'''\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        '''
        print('=' * 100)
        print(textwrap.dedent(linha))




def main():
    saldo = 0
    limite = 500
    extrato = ''
    numeros_saques = 0
    usuarios = []
    contas = []

    LIMITES_SAQUES = 3
    AGENCIA = '0001'
    while True:
        opcao = menu()
        if opcao == 'd':
            valor = float(input(' Digite o valor do depósito: '))

            saldo, extrato = depositar(saldo,valor,extrato)
        elif opcao == 's':
            valor = float(input(' Digite o valor do saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numeros_saques=numeros_saques,
                limites_saques=LIMITES_SAQUES,
                )
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                conta.append(contas)
        elif opcao == 'lc':
            listar_contas(contas)
        
        elif opcao == 'sa':
            break
main()    


    




