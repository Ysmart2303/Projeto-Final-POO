import tkinter as tk
from tkinter import ttk
import transacao as tsc
from tkinter import messagebox

aba = tk.Tk()
aba.title("Gerenciador Financeiro")
aba.geometry("500x450")
aba.minsize(300, 250)
aba.configure(bg = "#F0F2F5")

# CRIACAO DO GERENCIADOR

gerenciador = tsc.GerenciadorFinanceiro()

def adicionar_transacao():

    # ATRIBUICAO DOS VALORES
    descricao = entrada_descricao.get()
    valor = entrada_valor.get()
    tipo = combo_tipo.get()

    if not descricao or not valor or not tipo:
        messagebox.showerror("Erro na criação de cadastro", "Preencha todos os campos!")
        return

    try:
        valor = float(valor.replace(",", "."))
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido!")
        return

    if valor <= 0:
        messagebox.showerror("Erro", "O valor deve ser maior que zero!")
        return


    # COLOCANDO AS TRANSACOES NA LISTA
    nova_transacao = tsc.Transacao(descricao, valor, tipo)
    gerenciador.adicionar_transacao(nova_transacao)
    atualizar_tela()
    atualizar_resumo()


    # LIMPAR CAMPOS
    entrada_descricao.delete(0, tk.END)
    entrada_valor.delete(0, tk.END)
    combo_tipo.set("")

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

titulo = tk.Label(
    aba,
    text = "GERENCIADOR FINANCEIRO",
    font = ("Arial", 18, "bold"),
    bg = "#F0F2F5",
    fg = "#263B5E"
)
titulo.pack(pady = 5)


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
    font = ("Arial", 9, "bold"),
    command = adicionar_transacao
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

# ATUALIZAR TABELA APOS ADD VALORES
def atualizar_tela():

    tabela.delete(*tabela.get_children())

    for transacao in gerenciador.transacoes:

        descricao = transacao.get_descricao()
        valor = transacao.get_valor()
        tipo = transacao.get_tipo()

        tabela.insert(
            "",
            "end",
            values = (descricao, valor, tipo)
        )


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

# ATT O RESUMO ABAIXO DA TABELA
def atualizar_resumo():

    receitas = gerenciador.calcular_receitas()
    despesas = gerenciador.calcular_despesas()
    saldo = gerenciador.calcular_saldo()

    lbl_receitas.configure(
        text = f"Receitas: R$ {receitas:.2f}"
    )

    lbl_despesas.configure(
        text = f"Despesas: R$ {despesas:.2f}"
    )

    lbl_saldo.configure(
        text = f"Saldo: R$ {saldo:.2f}"
    )


# AJUSTAR TAMANHO DA TELA
def tamanho_tela(largura):

    if largura < 400:
        return "pequena"

    elif largura < 500:
        return "media"

    else:
        return "grande"

def responsividade(event):

    if event.widget != aba:
        return

    tamanho = tamanho_tela(event.width)


    # AJUSTAR TITULO

    if tamanho == "pequena":
        titulo.configure(font = ("Arial", 10, "bold"))

    elif tamanho == "media":
        titulo.configure(font = ("Arial", 14, "bold"))

    else:
        titulo.configure(font = ("Arial", 18, "bold"))

    # AJUSTAR CAMPOS

    if tamanho == "pequena":
        frame_campos.configure(padx = 8)

    else:
        frame_campos.configure(padx = 20)

    # AJUSTAR RESUMO

    if tamanho == "pequena":
        frame_resumo.configure(padx = 10)

    else:
        frame_resumo.configure(padx = 25)

    # AJUSTAR TABELA

    if tamanho == "pequena":
        tabela.column("descricao", width = 100)
        tabela.column("valor", width = 70)
        tabela.column("tipo", width = 70)

    else:
        tabela.column("descricao", width = 200)
        tabela.column("valor", width = 150)
        tabela.column("tipo", width = 150)

    # AJUSTAR FONTE TABELA

    if tamanho == "pequena":
        estilo.configure("Treeview", font = ("Arial", 8))

    else:
        estilo.configure("Treeview", font = ("Arial", 10))

    # AJUSTAR FONTE DOS CABEÇALHOS

    if tamanho == "pequena":
        estilo.configure(
            "Treeview.Heading",
            font = ("Arial", 8, "bold")
        )

    else:
        estilo.configure(
            "Treeview.Heading",
            font = ("Arial", 10, "bold")
        )

    # AJUSTAR INFORMACOES ABAIXO DA TABELA

    if tamanho == "pequena":
        lbl_receitas.configure(font = ("Arial", 8))
        lbl_despesas.configure(font = ("Arial", 8))
        lbl_saldo.configure(font = ("Arial", 10, "bold"))

    else:
        lbl_receitas.configure(font = ("Arial", 10))
        lbl_despesas.configure(font = ("Arial", 10))
        lbl_saldo.configure(font = ("Arial", 12, "bold"))



    if tamanho == "pequena":
        # TELA VERTICAL

        botao_adicionar.grid(
            row = 0, column = 0, sticky = "", pady = 3
        )

        botao_alterar.grid(
            row = 1, column = 0, sticky = "", pady = 3
        )

        botao_excluir.grid(
            row = 2, column = 0, sticky = "", pady = 3
        )

        frame_botoes.columnconfigure(
            0, weight = 1
        )
        
        frame_botoes.columnconfigure(
            1, weight = 0
        )

        frame_botoes.columnconfigure(
            2, weight = 0
        )

    else:
        # TELA HORIZONTAL

        for coluna in range(3):
            frame_botoes.columnconfigure(coluna, weight = 1)

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
aba.mainloop()