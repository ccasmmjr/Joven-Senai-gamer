import xmlrpc.client
import sys
import tkinter as tk
from tkinter import scrolledtext

scroll_text = None
serverHUB = xmlrpc.client.ServerProxy("http://localhost:8080")
def abrir_outra_janela(janela):
    outra_janela = tk.Toplevel(janela)
    outra_janela.title("Outra Janela")
    label = tk.Label(outra_janela, text="Você fez login com sucesso!")
    label.pack()
    data = serverHUB.view_game("a")
    global scroll_text
    scroll_text = scrolledtext.ScrolledText(outra_janela, wrap=tk.WORD, width=50, height=20)
    scroll_text.pack(padx=10, pady=10)
    formatted_data = format_data(data)
    newformatted_data=formatar_string(formatted_data)
    scroll_text.insert(tk.END, newformatted_data)
    scroll_text.config(state=tk.DISABLED) 
    botao_atualizar = tk.Button(outra_janela, text="Update", command=atualizar_scrolled_text)
    botao_atualizar.pack()

def format_data(data):
    formatted_data = ""
    for key, value in data.items():
        formatted_data += f"{key}: {value}\n"
    return formatted_data

def atualizar_scrolled_text():
    newdata = serverHUB.view_game("a")
    scroll_text.config(state=tk.NORMAL) 
    scroll_text.delete("1.0", tk.END)   
    formatted_newdata = format_data(newdata)
    newformatted_newdata = formatar_string(formatted_newdata)
    scroll_text.insert(tk.END, newformatted_newdata)
    scroll_text.config(state=tk.DISABLED) 

def formatar_string(texto):
    texto_formatado = texto.replace('{', '\n').replace('}', '').replace("'", "")
    return texto_formatado