import couchdb  # importing couchdb

# Connecting with couchdb Server
# couch = couchdb.Server()
couch = couchdb.Server('http://localhost:5984')
# Creating Database
db = couch.create('dftest')
print("Database created")
# Creating document
doc = {'name': 'Employee'}
db.save(doc)  # Saving document
print("Document created")
# Fetching document from the database
print("Name is: " + doc['name'])
