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
class MyserverHUB:
    def add_game(self, nome, detalhes):
        
            ref.child('game').child(nome).set({
                'detalhes': detalhes
            })
            
    def view_game(self, nome):
        
             user_ref = ref.child('game').child(nome)
             user_data = user_ref.get()
             if user_data is not None:
                return user_data.get('senha')
             else:
                return None
      
    
server = xmlrpc.server.SimpleXMLRPCServer(("0.0.0.0",8080), allow_none=True)
server.register_instance(MyserverHUB)
server.serve_forever()
