from flask import Flask
app = Flask(__name__)


contacts = [
    { 'id' : '1', 'name' : 'Shaun', 'phone': '123-456-7890'},
    { 'id' : '2','name' : 'Joel', 'phone': '353-486-2852'},
    { 'id' : '3','name' : 'Mina', 'phone': '832-536-9347'},
    { 'id' : '4','name' : 'Heather', 'phone': '349-716-2212'},
]

@app.route('/hello')

@app.get('/contacts')
def listContacts():
    return contacts

@app.get('/contacts/<id>')
def readSingleContact(id):
    for contact in contacts:
        if contact['id'] == id:
            return contact
    return "Contact doesn't exist"

if __name__ == "__main__":
    app.run(debug = True)