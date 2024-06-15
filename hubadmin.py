import xmlrpc.client
import sys
import tkinter as tk
from tkinter import messagebox
import tkinter as tk
from tkinter import scrolledtext
#falta testa a funcao de ver o game
entry_nome_jogo = None
scrolled_text_descricao = None

serverHUB = xmlrpc.client.ServerProxy("http://localhost:8080")
def abrir_outra_janela(janela):
    outra_janela = tk.Toplevel(janela)
    outra_janela.title("Outra Janela")
    label = tk.Label(outra_janela, text="Você fez login com sucesso!")
    label.pack()
    label_nome_jogo = tk.Label(outra_janela, text="Nome do Jogo:")
    label_nome_jogo.pack()
    global entry_nome_jogo
    entry_nome_jogo = tk.Entry(outra_janela, width=50)
    entry_nome_jogo.pack()
    label_descricao_jogo = tk.Label(outra_janela, text="Descrição do Jogo:")
    label_descricao_jogo.pack()
    global scrolled_text_descricao
    scrolled_text_descricao = scrolledtext.ScrolledText(outra_janela, width=50, height=10)
    scrolled_text_descricao.pack()
    botao_cadastrar = tk.Button(outra_janela, text="Cadastrar", command=cadastrar_jogo)
    botao_cadastrar.pack()

    
def cadastrar_jogo():
    nome_jogo = entry_nome_jogo.get()
    descricao_jogo = scrolled_text_descricao.get("1.0", tk.END)
    serverHUB.add_game(nome_jogo, nome_jogo, descricao_jogo)
    # Aqui você pode inserir o código para cadastrar o jogo
    print(f"Jogo cadastrado:\nNome: {nome_jogo}\nDescrição:\n{descricao_jogo}")
