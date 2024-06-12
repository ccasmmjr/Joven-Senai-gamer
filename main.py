import xmlrpc.client
import sys

nome = "oi"
senha = "2"
serverCL = xmlrpc.client.ServerProxy("http://localhost:8000")
serverCL.add_user(senha, nome, senha)
