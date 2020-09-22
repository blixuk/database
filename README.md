# database
Python Database using shelve to store data.

- init(  name )
- load ( name )
- save
- uuid
- show
- add ( key, object )
- remove ( key )
- keys
- count
- check ( key )
- append ( key, object )
- update ( key, object )
- reform ( key, keys, object)
- listAll ( key )
- listKeys ( key )
- listValues (key)

sample code
```
newClient = client.Client('0001', 'bob', 'smith')
db.add(newClient.idNumber, newClient.__dict__)
print(db.show())
print(db.show()[newClient.idNumber])
print(db.show()[newClient.idNumber]['firstName'])
print(db.listAll('0001'))
print(db.listKeys('0001'))
print(db.listValues('0001'))
print(db.listAll('0001')['firstName'])
```
output
```
db.show() -> <shelve.DbfilenameShelf object at 0x7f2e5b72e2e8>
db.show()[newClient.idNumber] -> {'idNumber': '0001', 'firstName': 'bob', 'lastName': 'smith'}
db.show()[newClient.idNumber]['firstName'] -> bob
db.listAll('0001') -> {'idNumber': '0001', 'firstName': 'bob', 'lastName': 'smith'}
db.listKeys('0001') -> ['idNumber', 'firstName', 'lastName']
db.listValues('0001') -> ['0001', 'bob', 'smith']
db.listAll('0001')['firstName'] -> bob
```