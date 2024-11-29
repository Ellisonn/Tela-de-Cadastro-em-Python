import tkinter as tk
from tkinter import messagebox

def salvar_cadastro():
    nome = entry_nome.get()
    sobrenome = entry_sobrenome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    endereco = entry_endereco.get()

    if not all([nome, sobrenome, telefone, email, endereco]):
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        return

    with open("cadastro.txt", "a") as file:
        file.write(f"Nome: {nome}\n")
        file.write(f"Sobrenome: {sobrenome}\n")
        file.write(f"Telefone: {telefone}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Endereço: {endereco}\n")
        file.write("="*40 + "\n")

    messagebox.showinfo("Sucesso", "Cadastro salvo com sucesso!")
    limpar_campos()

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_sobrenome.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)

# Criar a janela principal
root = tk.Tk()
root.title("Tela de Cadastro")
root.geometry("400x400")

# Adicionar os campos e rótulos
tk.Label(root, text="Nome:").pack(pady=5)
entry_nome = tk.Entry(root)
entry_nome.pack(pady=5)

tk.Label(root, text="Sobrenome:").pack(pady=5)
entry_sobrenome = tk.Entry(root)
entry_sobrenome.pack(pady=5)

tk.Label(root, text="Telefone:").pack(pady=5)
entry_telefone = tk.Entry(root)
entry_telefone.pack(pady=5)

tk.Label(root, text="Email:").pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack(pady=5)

tk.Label(root, text="Endereço:").pack(pady=5)
entry_endereco = tk.Entry(root)
entry_endereco.pack(pady=5)

# Adicionar o botão de envio
tk.Button(root, text="Enviar", command=salvar_cadastro).pack(pady=20)

# Iniciar o loop principal da interface
root.mainloop()
