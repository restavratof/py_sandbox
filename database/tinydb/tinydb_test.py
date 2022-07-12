from tinydb import TinyDB

dbpath = "/home/dfashchanka/PycharmProjects/py_sandbox/database/tinydb/testdb.json"
db = TinyDB(dbpath)
db.insert({'int': 1, 'char': 'a'})
db.insert({'int': 1, 'char': 'b'})
