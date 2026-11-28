import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import transacao as tsc

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

# ALTERAR TRANSACAO

def alterar_valor():

    selecao = tabela.selection()

    if not selecao:
        messagebox.showwarning(
            "Aviso",
            "Selecione uma transação para alterar!"
        )
        return

    dados = tabela.item(selecao[0])
    valores = dados["values"]

    for transacao in gerenciador.transacoes:

        # RECUPERA OS DADOS 
        if (
            transacao.get_descricao() == valores[0]
            and transacao.get_valor() == float(valores[1])
            and transacao.get_tipo() == valores[2]
        ):

            # CANTO PARA ALTERAR O VALOR
            novo_valor = simpledialog.askfloat(
                "Alterar valor",
                "Digite o novo valor:"
            )

            if novo_valor is None:
                return

            if novo_valor <= 0:
                messagebox.showerror(
                    "Erro",
                    "O valor deve ser maior que zero!"
                )
                return

            transacao.alterar_valor(novo_valor)
            break

    atualizar_tela()
    atualizar_resumo()


# APAGAR TRANSACAO

def excluir_transacao():

    selecao = tabela.selection()

    if not selecao:
        messagebox.showwarning(
            "Aviso",
            "Selecione uma transação para excluir!"
        )
        return

    # RECUPERAR DADOS DA LINHA

    dados = tabela.item(selecao[0])
    valores = dados["values"]

    # ENCONTRAR E EXCLUIR A TRANSAÇÃO

    for transacao in gerenciador.transacoes:

        if (
            transacao.get_descricao() == valores[0]
            and transacao.get_valor() == float(valores[1])
            and transacao.get_tipo() == valores[2]
        ):

            gerenciador.excluir_transacao(transacao)
            break

    # ATUALIZAR INTERFACE

    atualizar_tela()
    atualizar_resumo()

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

frame_botoes = tk.Frame(aba, bg = "#F0F2F5")
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
    font = ("Arial", 9, "bold"),
    command = alterar_valor
)
botao_alterar.grid(
    row = 0, column = 1, sticky = "ew", padx = 5
)

botao_excluir = tk.Button(
    frame_botoes,
    text = "Excluir",
    bg = "#DC3545",
    fg = "white",
    font = ("Arial", 9, "bold"),
    command = excluir_transacao
)
botao_excluir.grid(
    row = 0, column = 2, sticky = "ew", padx = 5
)

# TABELA

frame_tabela = tk.Frame(aba)
frame_tabela.pack(fill = "x", padx = 20, pady = 10)

tabela = ttk.Treeview(
    frame_tabela,
    columns = ("descricao", "valor", "tipo"),
    show = "headings",
    height = 1
)

# CONFIGURAÇÃO DAS COLUNAS

tabela.heading("descricao", text = "Descrição")
tabela.heading("valor", text = "Valor")
tabela.heading("tipo", text = "Tipo")

tabela.column("descricao", width = 200)
tabela.column("valor", width = 150)
tabela.column("tipo", width = 150)

# BARRA DE ROLAGEM

scroll = ttk.Scrollbar(
    frame_tabela,
    orient = "vertical",
    command = tabela.yview
)

tabela.configure(yscrollcommand = scroll.set)

# POSICIONAMENTO

tabela.pack(side = "left", fill = "x", expand = True)
scroll.pack(side = "right", fill = "y")

# AJUSTAR ALTURA DA TABELA

def ajustar_altura_tabela():

    quantidade = len(gerenciador.transacoes)

    altura_maxima = 5

    nova_altura = min(max(quantidade, 1), altura_maxima)

    tabela.configure(height = nova_altura)



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

    ajustar_altura_tabela()

# ROLAGEM DA TABELA PELO MOUSE

def rolar_tabela(event):

    tabela.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )

tabela.bind("<MouseWheel>", rolar_tabela)


# RESUMO FINANCEIRO

# FRAME PARA OS CARDS
frame_cards = tk.Frame(
    aba,
    bg = "#F0F2F5"
)

frame_cards.pack(
    fill = "x",
    padx = 20,
    pady = 10
)

frame_cards.columnconfigure(0, weight = 1)
frame_cards.columnconfigure(1, weight = 1)
frame_cards.columnconfigure(2, weight = 1)


# CARD DE RECEITAS
card_receitas = tk.Frame(
    frame_cards,
    bg = "white",
    padx = 15,
    pady = 15
)

card_receitas.grid(
    row = 0,
    column = 0,
    padx = 5,
    sticky = "ew"
)


# CARD DE DESPESAS
card_despesas = tk.Frame(
    frame_cards,
    bg = "white",
    padx = 15,
    pady = 15
)

card_despesas.grid(
    row = 0,
    column = 1,
    padx = 5,
    sticky = "ew"
)


# CARD DE SALDO
card_saldo = tk.Frame(
    frame_cards,
    bg = "white",
    padx = 15,
    pady = 15
)

card_saldo.grid(
    row = 0,
    column = 2,
    padx = 5,
    sticky = "ew"
)


# LABEL DE RECEITAS

tk.Label(
    card_receitas,
    text = "RECEITAS",
    font = ("Arial", 10, "bold"),
    bg = "white",
    fg = "#263B5E"
).pack()

lbl_receitas = tk.Label(
    card_receitas,
    text = "R$ 0,00",
    font = ("Arial", 15, "bold"),
    bg = "white",
    fg = "#198754"
)

lbl_receitas.pack(pady = 5)


# LABEL DE DESPESAS

tk.Label(
    card_despesas,
    text = "DESPESAS",
    font = ("Arial", 10, "bold"),
    bg = "white",
    fg = "#263B5E"
).pack()

lbl_despesas = tk.Label(
    card_despesas,
    text = "R$ 0,00",
    font = ("Arial", 15, "bold"),
    bg = "white",
    fg = "#DC3545"
)

lbl_despesas.pack(pady = 5)


# LABEL DE SALDO

tk.Label(
    card_saldo,
    text = "SALDO",
    font = ("Arial", 10, "bold"),
    bg = "white",
    fg = "#263B5E"
).pack()

lbl_saldo = tk.Label(
    card_saldo,
    text = "R$ 0,00",
    font = ("Arial", 15, "bold"),
    bg = "white",
    fg = "#263B5E"
)

lbl_saldo.pack(pady = 5)

# ATT O RESUMO ABAIXO DA TABELA

def atualizar_resumo():

    receitas = gerenciador.calcular_receitas()
    despesas = gerenciador.calcular_despesas()
    saldo = gerenciador.calcular_saldo()

    lbl_receitas.configure(
        text = f"R$ {receitas:.2f}"
    )

    lbl_despesas.configure(
        text = f"R$ {despesas:.2f}"
    )

    lbl_saldo.configure(
        text = f"R$ {saldo:.2f}"
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
        frame_cards.configure(padx = 10)

    else:
        frame_cards.configure(padx = 25)

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
