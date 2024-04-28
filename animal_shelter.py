"""
Name: Tatiana Case
Date: April 7th, 2024
CS-340
Project One
"""
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER='aacuser', PASS='SNHU1234'):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30294
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insertData = self.database.animals.insert_one(data)  # data should be dictionary
            #Check insertData for operation
            if insertData != 0:
                return True
        else:
            return False

# Create method to implement the R in CRUD.
    def read(self, searchData):
        if searchData:
            data = self.database.animals.find(searchData,{'_id': False})
        else:
            data = self.database.animals.find({},{'_id': False})
        # Return the dataset else display error
        return data
    
# Create a method to implement the U in CRUD.
    def update(self,searchData, updateData):
        if searchData is not None:
            result = self.database.animals.update_many(searchData, {'$set': updateData})
        else:
            return '{}'
        # Return the dataset else display error
        return result.raw_result

# Create a method to implement the D in CRUD.
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else:
            return '{}'
        # Return the dataset seld display error
        return result.raw_result
