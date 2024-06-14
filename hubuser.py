import xmlrpc.client
import sys
import tkinter as tk
from tkinter import messagebox
serverHUB = xmlrpc.client.ServerProxy("http://localhost:8080")
def abrir_outra_janela(janela):
    outra_janela = tk.Toplevel(janela)
    outra_janela.title("Outra Janela")
    label = tk.Label(outra_janela, text="Você fez login com sucesso!")
    label.pack()