#Criação do treeview TABELA
import tkinter as tk
from tkinter import ttk

#Configuração da janela principal
janela = tk.Tk()
janela.title("Exemplo de Tabela")
janela.geometry("400x200")

#Criançao do Treeview
colunas = ("Nome", "Idade")
tabela = ttk.Treeview(janela, columns=colunas, show="headings")

#Definição dos cabeçalhos
tabela.heading("Nome", text="Nome")
tabela.heading("Idade", text="Idade")

#Inserção de dados
tabela.insert("", tk.END, values=("  Ana", "   28"))
tabela.insert("", tk.END, values=("  Bruna", "   35"))
tabela.insert("", tk.END, values=("  Carla", "   22"))

tabela.pack(expand=True, fill=tk.BOTH)

janela.mainloop()