
import tkinter as tk
from tkinter import ttk

aba = tk.Tk()
aba.title("Gerenciador Financeiro")
aba.geometry("700x600")


# TÍTULO

tk.Label(
    aba,
    text="GERENCIADOR FINANCEIRO"
).pack()


# CAMPOS

frame_campos = tk.Frame(aba)
frame_campos.pack()

tk.Label(frame_campos, text="Descrição:").pack()

entrada_descricao = tk.Entry(frame_campos)
entrada_descricao.pack()

tk.Label(frame_campos, text="Valor:").pack()

entrada_valor = tk.Entry(frame_campos)
entrada_valor.pack()

tk.Label(frame_campos, text="Tipo:").pack()

combo_tipo = ttk.Combobox(
    frame_campos,
    values=["Receita", "Despesa"],
    state="readonly"
)
combo_tipo.pack()


# BOTÕES

frame_botoes = tk.Frame(aba)
frame_botoes.pack()

tk.Button(
    frame_botoes,
    text="Adicionar"
).pack()

tk.Button(
    frame_botoes,
    text="Alterar valor"
).pack()

tk.Button(
    frame_botoes,
    text="Excluir"
).pack()


# TABELA

frame_tabela = tk.Frame(aba)
frame_tabela.pack()

tabela = ttk.Treeview(
    frame_tabela,
    columns=("descricao", "valor", "tipo"),
    show="headings",
    height=10
)

tabela.heading("descricao", text="Descrição")
tabela.heading("valor", text="Valor")
tabela.heading("tipo", text="Tipo")

tabela.pack()


# RESUMO FINANCEIRO

frame_resumo = tk.Frame(aba)
frame_resumo.pack()

lbl_receitas = tk.Label(frame_resumo, text="Receitas: R$ 0.00")
lbl_receitas.pack()

lbl_despesas = tk.Label(frame_resumo, text="Despesas: R$ 0.00")
lbl_despesas.pack()

lbl_saldo = tk.Label(frame_resumo, text="Saldo: R$ 0.00")
lbl_saldo.pack()


aba.mainloop()
