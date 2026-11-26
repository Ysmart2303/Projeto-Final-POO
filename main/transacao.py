class Transacao:

    def __init__(self, descricao, valor, tipo):
        self.__descricao = descricao
        self.__valor = valor
        self.__tipo = tipo

    def get_descricao(self):
        return self.__descricao

    def get_valor(self):
        return self.__valor

    def get_tipo(self):
        return self.__tipo

    def alterar_valor(self, novo_valor):
        if novo_valor > 0:
            self.__valor += novo_valor
        else:
            print("Insira o um saldo maior que 0 (zero)")

    def exibir_transacao(self):
        print(f"""Descrição: {self.get_descricao()}
Valor: R$ {self.get_valor()}
Tipo: {self.get_tipo()}""")

a = Transacao("Alimentação", 100, "Despesa")
b= Transacao("Alimentação", 200, "Despesa")
c = Transacao("Alimentação", 300, "Despesa")

transacoes = [a, b, c]

for itens in transacoes:
    a.exibir_transacao()
    itens.alterar_valor(250)
    itens.exibir_transacao()
    print("")