import json as js
from firebase import firebase as fb

firebase = fb.FirebaseApplication('https://d-t-script.firebaseio.com', None)
result = firebase.get('/users', None)
print (result)
