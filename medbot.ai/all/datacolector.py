import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
        'databaseURL': 'url'
    })
ref = db.reference('/')
all_data = ref.get()
# Initialize the Firebase app with your credentials
def verify(user_chat_id):
    # Extract the nested dictionary under the 'messages' key
    messages = all_data['messages']
    values=[]
    # Iterate over the messages and print the fields separately
    for message_id, message_data in messages.items():
        for key, value in message_data.items():
           # print(f"{key}: {value}")
            values.append(value)    
        if user_chat_id in values:
            msg="Congratulations! Your account has been successfully verified. 🎉\n''Thank you for completing the verification process."
            return(msg)
        else:
            emsg="verify first"
            return(emsg)
user_chat_id ='5581857026'

print(verify(user_chat_id))

