import transacao as tran
class GerenciadorFinanceiro:

    def __init__(self):
        self.transacoes = []

    def adicionar_transicao(self, transacao):
        self.transacoes.append(transacao)

    def listar_transacoes(self):
        for transacao in self.transacoes:
            transacao.tran_ex

