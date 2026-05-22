import qrcode
from tkinter import *
from tkinter import messagebox

window = Tk()

label = Label(window, text="Olá", font=("Arial", 12))
label.pack(pady=10)
website_entry = Entry(window)
website_entry.pack()
window.geometry("300x200")

def gera_qr_code():
    url = website_entry.get()
    
    if len(url) == 0:
        messagebox.showinfo(
            title="Erro!",
            message="Favor insira uma URL válida")
    else:
        opcao_escolhida = messagebox.askokcancel(
            title=url,
            message=f"O endereço URL é: \n "
                    f"Endereço: {url} \n"
                    f"Pronto para salvar?")
                   
        
        if opcao_escolhida:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black', back_color='white')
            img.save('qrExporte.png')

window.mainloop()