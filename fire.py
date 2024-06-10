import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Inicialize o aplicativo do Firebase com suas credenciais
cred = credentials.Certificate("/app/jovemsenai-2fbc6-firebase-adminsdk-wlzwy-50db1941db.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://jovemsenai-2fbc6-default-rtdb.firebaseio.com'
})
ref = db.reference('/')

# Escreva dados no banco de dados
ref.set({
    'message': 'Hello, Firebase!'
})
