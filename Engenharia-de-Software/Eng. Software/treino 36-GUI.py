import tkinter as tk
from tkinter import messagebox

#Função executada ao clicar no botão
def enviar_dados():
    nome = entry_nome.get()
    email = entry_email.get()

    if nome and email:
        #Exibe os dados (aqui você salvaria em um banco de dados)
        messagebox.showinfo("Sucesso", f"Dados salvos!\nNome: {nome}\nEmail: {email}")
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos")

#Configuração da janela principal
janela = tk.Tk()
janela.title("Formulário de Cadastro")
janela.geometry("300x250")

#Rotulo e campo de entrasda para nome
tk.Label(janela, text='Nome:').pack(pady=5)
entry_nome = tk.Entry(janela, width=30)
entry_nome.pack(pady=5)

#rotulo e campo de entrada para email
tk.Label(janela, text="e-mail:").pack(pady=5)
entry_email = tk.Entry(janela, width=30)
entry_email.pack(pady=5)
#Botão de envio
botao_enviar = tk.Button(janela, text="Enviar", command=enviar_dados)
botao_enviar.pack(pady=20)

#incializa o loop
janela.mainloop()