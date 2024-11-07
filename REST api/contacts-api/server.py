from flask import Flask, request
app = Flask(__name__)

nextID = 5

contacts = [
    { 'id' : '1', 'name' : 'Shaun', 'phone': '123-456-7890'},
    { 'id' : '2','name' : 'Joel', 'phone': '353-486-2852'},
    { 'id' : '3','name' : 'Mina', 'phone': '832-536-9347'},
    { 'id' : '4','name' : 'Heather', 'phone': '349-716-2212'},
]

@app.route('/hello')

def hello_route():
    print('I have recevied a request on the /hello endpoint')
    return '<h1>Hello!</h1>'


@app.get('/contacts')
def listContacts():
    return contacts


@app.get('/contacts/<id>')
def readSingleContact(id):
    for contact in contacts:
        if contact['id'] == id:
            return contact
    return "Contact doesn't exist"

@app.post('/contacts/')
def create_contact():
    global nextID 

    newContact = {
        "id" : f'{nextID}',
        "name" : request.json['name'],
        "phone" : request.json['phone'],
    }

    contacts.append(newContact)

    nextId += 1

    return newContact

@app.put('/contacts/<id>')
def update_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            contact['name'] = request.json['name'] if 'name' in request.json else contact['name']
            contact['phone'] = request.json['phone'] if 'phone' in request.json else contact['phone']
            return contact
    return 'No contact with that ID'


@app.delete('/contacts/<id>')
def delete_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            contacts.remove(contact)
            return contact
    
    return 'There is no contact with that id'

if __name__ == "__main__":
    app.run(debug = True)