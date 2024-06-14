import xmlrpc.client
import sys
import tkinter as tk
from tkinter import scrolledtext

serverHUB = xmlrpc.client.ServerProxy("http://localhost:8080")
def abrir_outra_janela(janela):
    outra_janela = tk.Toplevel(janela)
    outra_janela.title("Outra Janela")
    label = tk.Label(outra_janela, text="Você fez login com sucesso!")
    label.pack()
    data = serverHUB.view_game("a")
    scroll_text = scrolledtext.ScrolledText(outra_janela, wrap=tk.WORD, width=50, height=20)
    scroll_text.pack(padx=10, pady=10)
    formatted_data = format_data(data)
    scroll_text.insert(tk.END, formatted_data)


def format_data(data):
    formatted_data = ""
    for key, value in data.items():
        formatted_data += f"{key}: {value}\n"
    return formatted_data



