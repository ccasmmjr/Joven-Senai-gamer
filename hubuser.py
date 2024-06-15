import xmlrpc.client
import tkinter as tk
from tkinter import scrolledtext

# Cria uma instância do servidor proxy
serverHUB = xmlrpc.client.ServerProxy("http://localhost:8080")

def abrir_outra_janela(janela):
    # Cria uma nova janela
    outra_janela = tk.Toplevel(janela)
    outra_janela.title("Outra Janela")
    label = tk.Label(outra_janela, text="Você fez login com sucesso!")
    label.pack()
    
    # Obtém os dados do servidor
    data = serverHUB.view_game("a")
    
    # Cria uma caixa de texto rolável
    global scroll_text
    scroll_text = scrolledtext.ScrolledText(outra_janela, wrap=tk.WORD, width=50, height=20)
    scroll_text.pack(padx=10, pady=10)
    
    # Formata e insere os dados na caixa de texto
    formatted_data = format_data(data)
    newformatted_data = formatar_string(formatted_data)
    scroll_text.insert(tk.END, newformatted_data)
    scroll_text.config(state=tk.DISABLED)
    
    # Cria um botão para atualizar os dados
    botao_atualizar = tk.Button(outra_janela, text="Atualizar", command=atualizar_scrolled_text)
    botao_atualizar.pack()

def format_data(data):
    # Formata os dados em um string legível
    formatted_data = ""
    for key, value in data.items():
        formatted_data += f"{key}: {value}\n"
    return formatted_data

def atualizar_scrolled_text():
    # Obtém novos dados do servidor
    newdata = serverHUB.view_game("a")
    
    # Habilita a edição da caixa de texto, limpa a caixa de texto e insere os novos dados formatados
    scroll_text.config(state=tk.NORMAL)
    scroll_text.delete("1.0", tk.END)
    formatted_newdata = format_data(newdata)
    newformatted_newdata = formatar_string(formatted_newdata)
    scroll_text.insert(tk.END, newformatted_newdata)
    scroll_text.config(state=tk.DISABLED)

def formatar_string(texto):
    # Formata a string para remover caracteres indesejados e melhorar a legibilidade
    texto_formatado = texto.replace('{', '\n').replace('}', '').replace("'", "")
    return texto_formatado

# Cria a janela principal do Tkinter
def main():
    janela = tk.Tk()
    janela.title("Login")
    
    label_usuario = tk.Label(janela, text="Usuário:")
    label_usuario.pack()
    
    entrada_usuario = tk.Entry(janela)
    entrada_usuario.pack()
    
    label_senha = tk.Label(janela, text="Senha:")
    label_senha.pack()
    
    entrada_senha = tk.Entry(janela, show="*")
    entrada_senha.pack()
    
    botao_login = tk.Button(janela, text="Login", command=lambda: abrir_outra_janela(janela))
    botao_login.pack()
    
    janela.mainloop()

if __name__ == "__main__":
    main()
