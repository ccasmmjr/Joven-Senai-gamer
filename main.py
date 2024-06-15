import xmlrpc.client
import hubuser
import hubadmin
import tkinter as tk
from tkinter import messagebox

serverCL = xmlrpc.client.ServerProxy("http://localhost:8000")

def fazer_login():
    username = username_entry.get()
    senha = senha_entry.get()
    adm = admin_var.get()
    if admin_var.get() == 1:
        tipo_usuario = "Administrador"
        if serverCL.check_user_credentials(senha, username, senha, adm):
            print("A senha está correta para o usuário.")
            hubadmin.abrir_outra_janela(janela)
            janela.withdraw()
        else:
            print("A senha está incorreta ou o usuário não existe.")
    else:
        if serverCL.check_user_credentials(senha, username, senha, adm):
            print("A senha está correta para o usuário.")
            hubuser.abrir_outra_janela(janela)
            janela.withdraw()
        else:
            print("A senha está incorreta ou o usuário não existe.")
        tipo_usuario = "Usuário normal"
    messagebox.showinfo("Login", f"Username: {username}\nSenha: {senha}\nTipo de usuário: {tipo_usuario}")

def fazer_cadastro():
    username = username_entry.get()
    senha = senha_entry.get()
    adm=admin_var.get()
    if admin_var.get() == 1:
        tipo_usuario = "Administrador"
        serverCL.add_user(senha, username, senha, adm)
    else:
        serverCL.add_user(senha, username, senha, adm)
        tipo_usuario = "Usuário normal"
    messagebox.showinfo("Cadastro", f"Cadastro realizado!\nUsername: {username}\nSenha: {senha}\nTipo de usuário: {tipo_usuario}")





# Cria a janela principal
janela = tk.Tk()
janela.title("Login e Cadastro")

# Cria os widgets
username_label = tk.Label(janela, text="Username:")
username_entry = tk.Entry(janela)

senha_label = tk.Label(janela, text="Senha:")
senha_entry = tk.Entry(janela, show="*")

admin_var = tk.IntVar()
admin_checkbox = tk.Checkbutton(janela, text="Administrador", variable=admin_var)

login_button = tk.Button(janela, text="Login", command=fazer_login)
cadastro_button = tk.Button(janela, text="Cadastro", command=fazer_cadastro)

# Coloca os widgets na janela
username_label.grid(row=0, column=0, sticky="e")
username_entry.grid(row=0, column=1)
senha_label.grid(row=1, column=0, sticky="e")
senha_entry.grid(row=1, column=1)
admin_checkbox.grid(row=2, columnspan=2)
login_button.grid(row=3, column=0, pady=10)
cadastro_button.grid(row=3, column=1, pady=10)

# Inicia o loop da aplicação
janela.mainloop()



