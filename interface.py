import tkinter as tk
from tkinter import messagebox

# Função que será chamada quando o botão for clicado
def mostrar_mensagem():
    messagebox.showinfo("Informação", "Você clicou no botão!")

# Criando a janela principal
janela = tk.Tk()
janela.title("Minha primeira GUI")
janela.geometry("300x200")

# Criando um botão
botao = tk.Button(janela, text="Clique aqui", command=mostrar_mensagem)
botao.pack(pady=50)

# Iniciando o loop da interface
janela.mainloop()
