import tkinter as tk
from tkinter import ttk

aba = tk.Tk()
aba.title("Gerenciador Financeiro")
aba.geometry("700x650")
aba.configure(bg="#F0F2F5")


# ESTILO DA TABELA

estilo = ttk.Style()
estilo.theme_use("clam")

estilo.configure(
    "Treeview.Heading",
    font=("Arial", 10, "bold"),
    background="#263B5E",
    foreground="white"
)

estilo.configure(
    "Treeview",
    font=("Arial", 10),
    rowheight=28
)


# TÍTULO

tk.Label(
    aba,
    text="GERENCIADOR FINANCEIRO",
    font=("Arial", 18, "bold"),
    bg="#F0F2F5",
    fg="#263B5E"
).pack(pady=18)


# CAMPOS

frame_campos = tk.Frame(
    aba,
    bg="white",
    padx=20,
    pady=12
)
frame_campos.pack(pady=5)

tk.Label(
    frame_campos,
    text="Descrição:",
    font=("Arial", 10, "bold"),
    bg="white"
).pack(anchor="w")

entrada_descricao = tk.Entry(
    frame_campos,
    width=40,
    font=("Arial", 10)
)
entrada_descricao.pack(pady=4)

tk.Label(
    frame_campos,
    text="Valor (R$):",
    font=("Arial", 10, "bold"),
    bg="white"
).pack(anchor="w")

entrada_valor = tk.Entry(
    frame_campos,
    width=40,
    font=("Arial", 10)
)
entrada_valor.pack(pady=4)

tk.Label(
    frame_campos,
    text="Tipo:",
    font=("Arial", 10, "bold"),
    bg="white"
).pack(anchor="w")

combo_tipo = ttk.Combobox(
    frame_campos,
    values=["Receita", "Despesa"],
    state="readonly",
    width=37
)
combo_tipo.pack(pady=4)


# BOTÕES

frame_botoes = tk.Frame(aba, bg="#F0F2F5")
frame_botoes.pack(pady=12)

tk.Button(
    frame_botoes,
    text="Adicionar",
    width=15,
    bg="#198754",
    fg="white",
    font=("Arial", 9, "bold")
).pack(side="left", padx=5)

tk.Button(
    frame_botoes,
    text="Alterar valor",
    width=15,
    bg="#E0A800",
    fg="black",
    font=("Arial", 9, "bold")
).pack(side="left", padx=5)

tk.Button(
    frame_botoes,
    text="Excluir",
    width=15,
    bg="#DC3545",
    fg="white",
    font=("Arial", 9, "bold")
).pack(side="left", padx=5)


# TABELA

frame_tabela = tk.Frame(aba)
frame_tabela.pack(pady=10)

tabela = ttk.Treeview(
    frame_tabela,
    columns=("descricao", "valor", "tipo"),
    show="headings",
    height=8
)

tabela.heading("descricao", text="Descrição")
tabela.heading("valor", text="Valor")
tabela.heading("tipo", text="Tipo")

tabela.column("descricao", width=200)
tabela.column("valor", width=150)
tabela.column("tipo", width=150)

tabela.pack()


# RESUMO FINANCEIRO

frame_resumo = tk.Frame(
    aba,
    bg="white",
    padx=25,
    pady=10
)
frame_resumo.pack(pady=12)

lbl_receitas = tk.Label(
    frame_resumo,
    text="Receitas: R$ 0.00",
    font=("Arial", 10),
    bg="white",
    fg="#198754"
)
lbl_receitas.pack(pady=3)

lbl_despesas = tk.Label(
    frame_resumo,
    text="Despesas: R$ 0.00",
    font=("Arial", 10),
    bg="white",
    fg="#DC3545"
)
lbl_despesas.pack(pady=3)

lbl_saldo = tk.Label(
    frame_resumo,
    text="Saldo: R$ 0.00",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#263B5E"
)
lbl_saldo.pack(pady=3)


aba.mainloop()