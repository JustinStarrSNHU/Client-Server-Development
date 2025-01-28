from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for animal collection in MongoDB """


    def __init__(self, username, userpass):
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
        USER = username
        PASS = userpass
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32435
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD
    
# Inserts a single document into the specified MongoDB database and collection using the passed
# in data (dictionary) if it is not of type None. Using a try/catch block,
# True is returned if the document is added successfully. 
# An exception is thrown if the document is not added succesfully and False is returned. 
# If the data passed in is empty an exception is raised.
    
    def create(self, data):
        if data is not None:
            try:
                insert_result = self.database.animals.insert_one(data) # data should be dictionary
                return True  
            except Exception:
                return False   
                
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
# Read method to implement the R in CRUD

# Queries the specified MongoDB database and collection using the passed in data (dictionary)
# if the passed in data is not of type None. If the passed in data is empty an exception is raised. Matching
# query reults are returned to the user. If no matches are found an empty list is returned.

    def read(self, readData):
    	if readData is not None:
    	    data = self.database.animals.find(readData)  
    	else:
    	    raise Exception("Nothing to read, because data parameter is empty")
    	return data    
    	    
# Update method to implement the U in CRUD

# Queries the specified MongoDB database and collection using the passed in data parameters (dictionaries)
# if the passed in searchData and updateData is not of type None. If the passed in data parameters are empty,
# an exception is raised. If the searchData is found, any documents matching the searchData is updated with the
# passed in updateData. The number of documents updated is returned to the user. If no documents are updated
# zero is returned to the user.

    def update(self, searchData, updateData):
        if searchData and updateData is not None:
            data = self.database.animals.update_many(searchData, { "$set": updateData } )
        else:
            raise Exception("Nothing to update, because one of the data parameters is empty")
        return data.modified_count
        
# Delete method to implement the D in CRUD

# Queries the specified MongoDB database and collection using the passed in data (dictionary)
# if the passed in data is not of type None. If the pass3ed in data is empty an exception is raised.
# If the deleteData is found, any documents matching the deleteData will be deleted from the specified
# MongoDB database and collection. The number of documents deleted is returned to the user.
# If no documents are deleted, zero is returned to the user.

    def delete(self, deleteData):
        if deleteData is not None:
            data = self.database.animals.delete_many(deleteData)
        else:
            raise Exception("Nothing to delete, because the data parameter is empty")
        return data.deleted_count           	    
    	
        
