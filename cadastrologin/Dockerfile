# Use a imagem oficial do Python como imagem base
FROM python:3.9

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo local 'file1' para o diretório '/app' dentro do contêiner
COPY  jovemsenai-2fbc6-firebase-adminsdk-wlzwy-50db1941db.json /app/jovemsenai-2fbc6-firebase-adminsdk-wlzwy-50db1941db.json

# Instala a biblioteca Python 'biblioteca1' usando pip
RUN pip install firebase-admin

# Copia o script Python local 'script1.py' para o diretório '/app' dentro do contêiner
COPY CadastroeLogin.py /app/CadastroeLogin.py
#Expor a porta
EXPOSE 8000

# Define o comando padrão a ser executado quando o contêiner for iniciado
CMD ["python", "CadastroeLogin.py"]
