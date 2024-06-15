# Jovem-Senai-gamer

### Requistos
python
xml-rpc
tkinter

### Para install tkinter e so 
sudo apt install python3-tk

# Passos para executar o serviço de Cadastro e Login

## Abrir o terminal no VS Code
Abra um novo terminal no Visual Studio Code e navegue até o diretório cadastrologin com o comando:
cd cadastrologin

sudo docker build -t cadastro .

## Construir e executar o container
No terminal, execute os seguintes comandos para construir e executar o container Docker:
sudo docker build -t cadastro .
sudo docker run -it -p 8000:8000 cadastro

## Atualizar o Container e Executar o Serviço
Dentro do container, atualize o sistema e execute o script CadastroeLogin.py:
apt update
python3 CadastroeLogin.py

Após esses passos, o serviço de cadastro e login estará ativo.

# Passos para executar o Service Hub
## Abrir um novo terminal no VS Code
Abra um novo terminal no Visual Studio Code sem fechar o terminal anterior.

## Construir e executar o container Docker

No novo terminal, execute os seguintes comandos para construir e executar o container Docker para o serviço Hub:
sudo docker build -t hub .
sudo docker run -it -p 8080:8080 cadastro

## Atualizar o Container e Executar o Serviço
Dentro do container, atualize o sistema e execute o script hub.py:
apt update
python3 hub.py

Após esses passos, o serviço Hub estará ativo.

# Executar o Script Principal
Agora você pode executar o script principal conforme necessário.
