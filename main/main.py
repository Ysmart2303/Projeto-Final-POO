import tkinter as tk
from tkinter import ttk

aba = tk.Tk()
aba.title("Gerenciador Financeiro")
aba.geometry("600x500")
aba.minsize(300, 250)
aba.configure(bg = "#F0F2F5")


# ESTILO DA TABELA

estilo = ttk.Style()
estilo.theme_use("clam")

estilo.configure(
    "Treeview.Heading",
    font = ("Arial", 10, "bold"),
    background = "#263B5E",
    foreground = "white"
)

estilo.configure(
    "Treeview",
    font = ("Arial", 10),
    rowheight = 28
)


# TÍTULO

tk.Label(
    aba,
    text = "GERENCIADOR FINANCEIRO",
    font = ("Arial", 18, "bold"),
    bg = "#F0F2F5",
    fg = "#263B5E"
).pack(pady = 5)


# CAMPOS

frame_campos = tk.Frame(
    aba,
    bg = "white",
    padx = 20,
    pady = 12
)
frame_campos.pack(fill = "x", padx = 20)

tk.Label(
    frame_campos,
    text = "Descrição:",
    font = ("Arial", 10, "bold"),
    bg = "white"
).pack(anchor = "w")

entrada_descricao = tk.Entry(
    frame_campos,
    width = 40,
    font = ("Arial", 10)
)
entrada_descricao.pack(fill = "x", pady = 4)

tk.Label(
    frame_campos,
    text = "Valor (R$):",
    font = ("Arial", 10, "bold"),
    bg = "white"
).pack(anchor = "w")

entrada_valor = tk.Entry(
    frame_campos,
    width = 40,
    font = ("Arial", 10)
)
entrada_valor.pack(fill = "x", pady = 4)

tk.Label(
    frame_campos,
    text = "Tipo:",
    font = ("Arial", 10, "bold"),
    bg = "white"
).pack(anchor = "w")

combo_tipo = ttk.Combobox(
    frame_campos,
    values = ["Receita", "Despesa"],
    state = "readonly",
    width = 37
)
combo_tipo.pack(fill = "x", pady = 4)


# BOTÕES

frame_botoes = tk.Frame(aba, bg  ="#F0F2F5")
frame_botoes.pack(fill = "x", padx = 20, pady = 12)
frame_botoes.columnconfigure(0, weight = 1)
frame_botoes.columnconfigure(1, weight = 1)
frame_botoes.columnconfigure(2, weight = 1)

botao_adicionar = tk.Button(
    frame_botoes,
    text = "Adicionar",
    bg = "#198754",
    fg = "white",
    font = ("Arial", 9, "bold")
)
botao_adicionar.grid(
    row = 0, column = 0, sticky = "ew", padx = 5
)

botao_alterar = tk.Button(
    frame_botoes,
    text = "Alterar valor",
    bg = "#E0A800",
    fg = "black",
    font = ("Arial", 9, "bold")
)
botao_alterar.grid(
    row = 0, column = 1, sticky = "ew", padx = 5
)

botao_excluir = tk.Button(
    frame_botoes,
    text = "Excluir",
    bg = "#DC3545",
    fg = "white",
    font = ("Arial", 9, "bold")
)
botao_excluir.grid(
    row = 0, column = 2, sticky = "ew", padx = 5
)

def responsividade(event):

    if event.widget != aba:
        return

    if event.width < 450:
        # TELA VERTICAL

        botao_adicionar.grid(
            row = 0, column = 0, sticky = "ew", pady = 3
        )

        botao_alterar.grid(
            row = 1, column = 0, sticky = "ew", pady = 3
        )

        botao_excluir.grid(
            row = 2, column = 0, sticky = "ew", pady = 3
        )

    else:
        # MODO HORIZONTAL

        botao_adicionar.grid(
            row = 0, column = 0, sticky = "ew", padx = 5
        )

        botao_alterar.grid(
            row = 0, column = 1, sticky = "ew", padx = 5
        )

        botao_excluir.grid(
            row = 0, column = 2, sticky = "ew", padx = 5
        )

aba.bind("<Configure>", responsividade)


# TABELA

frame_tabela = tk.Frame(aba)
frame_tabela.pack(fill = "both", expand = True, padx = 20, pady = 10)

tabela = ttk.Treeview(
    frame_tabela,
    columns = ("descricao", "valor", "tipo"),
    show = "headings",
    height = 8
)

tabela.heading("descricao", text = "Descrição")
tabela.heading("valor", text = "Valor")
tabela.heading("tipo", text = "Tipo")

tabela.column("descricao", width = 200, stretch = True)
tabela.column("valor", width = 150, stretch = True)
tabela.column("tipo", width = 150, stretch = True)

tabela.pack(fill = "both", expand = True)


# RESUMO FINANCEIRO

frame_resumo = tk.Frame(
    aba,
    bg = "white",
    padx = 25,
    pady = 10
)
frame_resumo.pack(fill = "x", padx = 20, pady = 12)

lbl_receitas = tk.Label(
    frame_resumo,
    text = "Receitas: R$ 0.00",
    font = ("Arial", 10),
    bg = "white",
    fg = "#198754"
)
lbl_receitas.pack(pady = 3)

lbl_despesas = tk.Label(
    frame_resumo,
    text = "Despesas: R$ 0.00",
    font = ("Arial", 10),
    bg = "white",
    fg = "#DC3545"
)
lbl_despesas.pack(pady=3)

lbl_saldo = tk.Label(
    frame_resumo,
    text = "Saldo: R$ 0.00",
    font = ("Arial", 12, "bold"),
    bg = "white",
    fg = "#263B5E"
)
lbl_saldo.pack(pady = 3)


aba.mainloop()