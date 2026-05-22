import tkinter as tk

# Função que será chamada ao clicar no botão
def acao_botao():
    label.config(text="Botão clicado! 🌟")
    print("O botão foi clicado.")

#1. Criação da janela principal
janela = tk.Tk()
janela.title("Exemplo GUI Python")
janela.geometry("300x200") #largura x altura

#2. Adicionando componetes (Wingets)
label =tk.Label(janela, text="Olá, usuário!", font=("Arial", 12))
label.pack(pady=20) # pack organiza o widget na janela

botao = tk.Button(janela, text="Clique Aqui", command=acao_botao)
botao.pack()

#3. Inicia o loop principal (mantem a janela aberta)
janela.mainloop()