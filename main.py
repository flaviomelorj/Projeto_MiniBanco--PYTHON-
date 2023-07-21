import os
class Conta():
    def __init__(self,nome,cpf,endereco,senha):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.senha = senha
        self.num_conta = 5555
        self.saldo = 0

    def opcoes(self):
        print("VOCÊ ESTÁ DENTRO DO BANCO!")
        print("O QUE VOCÊ DESEJA?")
        print("1 - MEUS DADOS COMPLETOS")
        print("2 - VERIFICAR SEU SALDO")
        print("3 - SACAR DINHEIRO")
        print("4 - EFETUAR UM DEPOSITO")
        print("5 - ALTERAR SUA SENHA")
        print("6 - SAIR")
        op = input("INFORME -->  ")
        os.system('cls') or None

        if (op == "1"):
            senha = input("INFORME SUA SENHA -->  ")
            if (senha == self.senha):
                self.apresentacao()
            else:
                print("********************************")
                print("SENHA INVÁLIDA")
                print("********************************")
                self.opcoes()


        if (op == "2"):
            senha = input("INFORME SUA SENHA -->  ")
            if (senha == self.senha):
                self.mostrarSaldo()
            else:
                print("*********************************")
                print("SENHA INVÁLIDA")
                print("*********************************")
                self.opcoes()
        if (op == "3"):
            senha = input("INFORME SUA SENHA -->  ")
            if (senha == self.senha):
                valor = input("INFORME O VALOR DO SAQUE -->  ")
                self.sacar(valor)
            else:
                print("*********************************")
                print("SENHA INVÁLIDA")
                print("*********************************")
                self.opcoes()

        if (op == "4"):
            senha = input("INFORME SUA SENHA -->  ")
            if (senha == self.senha):
                valor = input("INFORME O VALOR DO DEPÓSITO -->  ")
                self.deposito(valor)
            else:
                print("*********************************")
                print("SENHA INVÁLIDA")
                print("*********************************")
                self.opcoes()

        if (op == "5"):
            senha = input("INFORME SUA SENHA -->  ")
            if (senha == self.senha):
                nova = input("INFORME SUA NOVA SENHA -->  ")
                self.mudarSenha(nova)
            else:
                print("*********************************")
                print("SENHA INVÁLIDA")
                print("*********************************")
                self.opcoes()
    def apresentacao(self):
        print(f"Olá {self.nome}, tudo bem? O numero da sua conta é {self.num_conta}"
              f" seu endereço é {self.endereco}, seu cpf é {self.cpf}!")
        print("Caso tenha dados incorretos alterar imediatamente")
        print("*********************************")
        print("*********************************")
        print("*********************************")

        self.opcoes()

    def mostrarSaldo(self):
        print("*********************************")
        print("*********************************")
        print(f"Seu saldo atual é de R${self.saldo} reais")
        print("*********************************")
        print("*********************************")
        self.opcoes()

    def sacar(self,valor):
        valor = int(valor)
        if(self.saldo < valor):
            print("*********************************")
            print("*********************************")
            print("SALDO INSUFICIENTE")
            print("*********************************")
            print("*********************************")
            self.opcoes()
        else:
            self.saldo = self.saldo - valor
            print("*********************************")
            print("*********************************")
            print(f"SAQUE NO VALOR DE R$ {valor} reais")
            print("*********************************")
            print("*********************************")
            self.opcoes()

    def deposito(self,valor):
        valor = int(valor)
        self.saldo = self.saldo + valor
        print("*********************************")
        print("*********************************")
        print("VALOR DEPOSITADO COM SUCESSO")
        print("*********************************")
        print("*********************************")
        self.opcoes()
    def mudarSenha(self,nova):
        nova = int(nova)
        self.senha = nova
        print("*********************************")
        print("*********************************")
        print("Senha alterada com sucesso")
        print("*********************************")
        print("*********************************")
        self.opcoes()

print("Digite o numero para a opção desejada")
print("1 - ABRIR CONTA")
print("2 - SAIR")
op = input("INFORME -->  ")

if(op == "1"):
    print("Para abrir a conta vamos precisar de alguns dados:")
    nome = input("INFORME SEU NOME -->  ")
    cpf = input("INFORME SEU CPF -->  ")
    endereco = input("INFORME SEU ENDEREÇO -->  ")
    senha = input("CRIE SUA SENHA -->  ")
    c1 = Conta(nome,cpf,endereco,senha)
    print(f"Olá {c1.nome}, tudo bem? Sua conta foi aberta com sucesso, o numero da sua conta {c1.num_conta}"
          f" e esse sera seu primeiro acesso ao banco")
    c1.opcoes()



















