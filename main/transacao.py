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
            self.__valor = novo_valor
        else:
            print("Insira um valor maior que 0 (zero)")

    def exibir_transacao(self):
        print(f"""Descrição: {self.get_descricao()}
Valor: R$ {self.get_valor()}
Tipo: {self.get_tipo()}""")


class GerenciadorFinanceiro:

    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def listar_transacoes(self):
        for transacao in self.transacoes:
            transacao.exibir_transacao()

    def calcular_receitas(self):
        total_receitas = 0

        for transacao in self.transacoes:
            if transacao.get_tipo() == "Receita":
                total_receitas += transacao.get_valor()

        return total_receitas

    def calcular_despesas(self):
        total_despesas = 0

        for transacao in self.transacoes:
            if transacao.get_tipo() == "Despesa":
                total_despesas += transacao.get_valor()

        return total_despesas

    def calcular_saldo(self):
        receitas = self.calcular_receitas()
        despesas = self.calcular_despesas()

        saldo = receitas - despesas

        return saldo


# Criando transações
a = Transacao("Salário", 5000, "Receita")
b = Transacao("Alimentação", 400, "Despesa")
c = Transacao("Transporte", 200, "Despesa")


# Criando gerenciador
gerenciador = GerenciadorFinanceiro()

gerenciador.adicionar_transacao(a)
gerenciador.adicionar_transacao(b)
gerenciador.adicionar_transacao(c)


# Exibindo resultados
print("=== TRANSAÇÕES ===")
gerenciador.listar_transacoes()

print("\n=== RESUMO FINANCEIRO ===")
print(f"Receitas: R$ {gerenciador.calcular_receitas()}")
print(f"Despesas: R$ {gerenciador.calcular_despesas()}")
print(f"Saldo: R$ {gerenciador.calcular_saldo()}")
