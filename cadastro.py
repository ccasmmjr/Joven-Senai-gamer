from firebase_admin import firestore

# Acesse o Cloud Firestore
db = firestore.client()

# Referencie o seu banco de dados em tempo real
ref = db.reference('/')

# Escreva dados no banco de dados
ref.set({
    'message': 'Hello, Firebase!'
})


