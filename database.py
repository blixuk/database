#!/usr/bin/env python3

###########################################
## File:     database.py                 ##
## Author:   Graham 'Blix' Winchester    ##
## Email:    blixuk@gmail.com            ##
## Date:     21/11/18                    ##
###########################################

# Imports
import os
import uuid
import shelve

class DB:
	
	def __init__(self, name): # Set the database file and the data holders
		self.DATASET = shelve.open(f'{os.getcwd()}/db/{name}.db')
		self.DATA = {}
		self.KEYS = []
		self.VALUES = []

	def load(self, name): # Load any database file into the data holder
		self.DATASET = shelve.open(f'{os.getcwd()}/db/{name}.db')

	def save(self): # Save the database file and clear the cache
		self.DATASET.sync()
		self.DATASET.close()

	def uuid(self): # Return a UUID
		return uuid.uuid4().hex

	def show(self): # Return all data stored in the database
		return self.DATASET

	def add(self, key, object): # Add a new entry to the database
		self.DATASET[key] = object

	def remove(self, key): # Remove an entry from the database
		del self.DATASET[key]

	def keys(self): # Return a List of all keys in the database
		self.KEYS = list(self.DATASET.keys())
		return self.KEYS

	def count(self): # Return the number of entries in the database
		return len(self.DATASET)

	def check(self, key): # Return a check if an entry is in the database
		return key in self.DATASET

	def append(self, key, object): # Append new entries to the database
		self.DATA = self.DATASET[key]
		self.DATA.append(object)
		self.DATASET[key] = self.DATA

	def update(self, key, object): # Update the value of an entry
		self.DATASET[key] = object
	
	def reform(self, key, keys, object): # Update the value of an entries dictionary value
		self.DATASET[key][keys] = object

	def listAll(self, key): # Return a dictionary of all key pairs to an entries dictionary
		self.DATA = dict(self.DATASET[key])
		return self.DATA

	def listKeys(self, key): # Return a list of all keys in an entries dictionary
		return list(self.DATASET[key])

	def listValues(self, key): # Return a list of all values in an entries dictionary
		for keys in self.listKeys(key):
			self.VALUES.append(self.DATASET[key][keys])
		return self.VALUES
