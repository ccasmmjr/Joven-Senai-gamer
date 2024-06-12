import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import xmlrpc.server
# Inicialize o aplicativo do Firebase com suas credenciais
cred = credentials.Certificate("/app/jovemsenai-2fbc6-firebase-adminsdk-wlzwy-50db1941db.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://jovemsenai-2fbc6-default-rtdb.firebaseio.com'
})
ref = db.reference('/')

# Escreva dados no banco de dados
class MyserverCL:
    def add_user(self, nome, senha):
        ref.child('users').child(nome).set({
        'senha': senha
    })
server = xmlrpc.server.SimpleXMLRPCServer(("0.0.0.0",8000), allow_none=True)
server.register_instance(MyserverCL)
server.serve_forever()
