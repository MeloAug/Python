import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Contador de produtos
quantidade = 0

# Função para adicionar produto
def adicionar_produto():
    global quantidade

    produto = campo_produto.get()
    preco = campo_preco.get()

    # Verifica se os campos estão vazios
    if produto == "" or preco == "":
        messagebox.showwarning("Erro", "Preencha todos os campos")

    else:
        # Adiciona os dados na tabela
        tabela.insert("", tk.END, values=(produto, preco))

        # Atualiza quantidade de produtos
        quantidade += 1
        texto_quantidade.config(
            text=f"Produtos cadastrados: {quantidade}"
        )

        # Limpa os campos
        campo_produto.delete(0, tk.END)
        campo_preco.delete(0, tk.END)

# Criação da janela
janela = tk.Tk()
janela.title("Controle de Produtos")
janela.geometry("500x350")

# Título
titulo = tk.Label(
    janela,
    text="Sistema de Produtos",
    font=("Arial", 14)
)
titulo.pack(pady=10)

# Campo produto
label_produto = tk.Label(janela, text="Produto")
label_produto.pack()

campo_produto = tk.Entry(janela, width=35)
campo_produto.pack(pady=5)

# Campo preço
label_preco = tk.Label(janela, text="Preço")
label_preco.pack()

campo_preco = tk.Entry(janela, width=35)
campo_preco.pack(pady=5)

# Botão
botao = tk.Button(
    janela,
    text="Adicionar Produto",
    command=adicionar_produto
)
botao.pack(pady=10)

# Texto quantidade
texto_quantidade = tk.Label(
    janela,
    text="Produtos cadastrados: 0"
)
texto_quantidade.pack()

# Tabela
colunas = ("Produto", "Preço")

tabela = ttk.Treeview(
    janela,
    columns=colunas,
    show="headings"
)

# Cabeçalhos
tabela.heading("Produto", text="Produto")
tabela.heading("Preço", text="Preço")

# Exibe tabela
tabela.pack(expand=True, fill=tk.BOTH, pady=10)

# Mantém a janela aberta
janela.mainloop()