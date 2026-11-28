
import tkinter as tk
from tkinter import ttk

aba = tk.Tk()
aba.title("Gerenciador Financeiro")
aba.geometry("700x600")


# TÍTULO

tk.Label(
    aba,
    text="GERENCIADOR FINANCEIRO",
    font=("Arial", 16, "bold")
).pack(pady=15)


# CAMPOS

frame_campos = tk.Frame(aba)
frame_campos.pack(pady=5)

tk.Label(frame_campos, text="Descrição:").pack()
entrada_descricao = tk.Entry(frame_campos, width=35)
entrada_descricao.pack(pady=3)

tk.Label(frame_campos, text="Valor:").pack()
entrada_valor = tk.Entry(frame_campos, width=35)
entrada_valor.pack(pady=3)

tk.Label(frame_campos, text="Tipo:").pack()
combo_tipo = ttk.Combobox(
    frame_campos,
    values=["Receita", "Despesa"],
    state="readonly",
    width=32
)
combo_tipo.pack(pady=3)


# BOTÕES

frame_botoes = tk.Frame(aba)
frame_botoes.pack(pady=12)

tk.Button(
    frame_botoes,
    text="Adicionar",
    width=15
).pack(side="left", padx=5)

tk.Button(
    frame_botoes,
    text="Alterar valor",
    width=15
).pack(side="left", padx=5)

tk.Button(
    frame_botoes,
    text="Excluir",
    width=15
).pack(side="left", padx=5)


# TABELA

frame_tabela = tk.Frame(aba)
frame_tabela.pack(pady=10)

tabela = ttk.Treeview(
    frame_tabela,
    columns=("descricao", "valor", "tipo"),
    show="headings",
    height=10
)

tabela.heading("descricao", text="Descrição")
tabela.heading("valor", text="Valor")
tabela.heading("tipo", text="Tipo")

tabela.column("descricao", width=200)
tabela.column("valor", width=150)
tabela.column("tipo", width=150)

tabela.pack()


# RESUMO FINANCEIRO

frame_resumo = tk.Frame(aba)
frame_resumo.pack(pady=15)

lbl_receitas = tk.Label(
    frame_resumo,
    text="Receitas: R$ 0.00"
)
lbl_receitas.pack(pady=3)

lbl_despesas = tk.Label(
    frame_resumo,
    text="Despesas: R$ 0.00"
)
lbl_despesas.pack(pady=3)

lbl_saldo = tk.Label(
    frame_resumo,
    text="Saldo: R$ 0.00",
    font=("Arial", 11, "bold")
)
lbl_saldo.pack(pady=3)


aba.mainloop()
