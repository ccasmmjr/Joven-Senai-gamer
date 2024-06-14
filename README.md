# Joven-Senai-gamer

Requisto
python
xmlrpc
tinker

para install tinker e so 
sudo apt install python3-tk

comando para usar
primeiro no terminal do visual studio
abra outro terminal pararelo e escreva cd cadastrologin para ir para o ditretorio
apos isso nele execute os ocmandos abaixos

sudo docker build -t cadastro .

sudo docker run -it -p 8000:8000 cadastro

dentro do container user
apt update

python3 CadastroeLogin.py

apos isso o seu servico cadastro e login estara em pe

agora abra outro terminal no visual studio sem fechar aquele que vc usou

e use os seguintes comandos

sudo docker build -t hub .

sudo docker run -it -p 8080:8080 cadastro

dentro do container user
apt update

python3 hub.py

apos isso o seu servico hub estara em pe

agora tu pode executar a main

lista do que falta
-criar o login
-criar o cadastro
-criar o hub(local que vai mostra o que tem no firebase)
-criar o main onde ele vai fazer os requsitos para os outros
-criar um dockefile para o hub
