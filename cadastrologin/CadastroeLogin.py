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
    def add_user(self, nome, senha, adm):
        if adm == 1:
            ref.child('admin').child(nome).set({
                'senha': senha
            })
        else:
             ref.child('users').child(nome).set({
                'senha': senha
             })
        
    def check_user_credentials(self, nome, senha, adm):
        if adm == 1:
             user_ref = ref.child('admin').child(nome)
             user_data = user_ref.get()
             if user_data is not None and user_data.get('senha') == senha:
                return True
             else:
                return False
        else:
             user_ref = ref.child('users').child(nome)
             user_data = user_ref.get()
             if user_data is not None and user_data.get('senha') == senha:
                return True
             else:
                return False
    
server = xmlrpc.server.SimpleXMLRPCServer(("0.0.0.0",8000), allow_none=True)
server.register_instance(MyserverCL)
server.serve_forever()
