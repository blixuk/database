#!/usr/bin/env python3
import database
import client

db = database.DB("client")

def main():
	newClient = client.Client('0001', 'bob', 'smith')
	db.add(newClient.idNumber, newClient.__dict__)
	print(db.show())
	print(db.show()[newClient.idNumber])
	print(db.show()[newClient.idNumber]['firstName'])

	print(db.listAll('0001'))
	print(db.listKeys('0001'))
	print(db.listValues('0001'))
	print(db.listAll('0001')['firstName'])

	print()

	db.add('Key', ['Value1', 'Value2'])
	print(db.show()['Key'])
	db.append('Key', 'Value3')
	print(db.show()['Key'])

	db.save()

if __name__ == "__main__":
	main()
