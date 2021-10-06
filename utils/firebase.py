import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class Firebase:
    def __init__(self, cert_path):
        cred = credentials.Certificate(cert_path)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        pass

    def store(self, person):
        doc_ref = self.db.collection(u'person').document(person['id'])
        doc_ref.set({
            u'id': person['id'],
            u'image_base64': person['image_base64'],
            u'people_in': person['people_in'],
            u'people_out': person['people_out'],
            u'created_at': person['created_at'],
        })
