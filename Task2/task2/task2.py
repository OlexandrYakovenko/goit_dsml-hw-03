import json
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def fill_db(db):
    with open("authors.json","r", encoding='utf-8') as fi:
        obj_authors=json.load(fi)
        db.authors.insert_many(obj_authors)
        
    with open("quotes.json","r", encoding='utf-8') as fi:
        obj_quotes=json.load(fi)
        db.qoutes.insert_many(obj_quotes)
def read_all(db):
    print( list(db.authors.find()) )
    print( list(db.qoutes.find()) )
    
def delete_all(db):
    db.authors.delete_many({})   
    db.qoutes.delete_many({})  

if __name__=="__main__":
    
    
    uri = "mongodb+srv://user:mysecretpassword@cluster0.bb7cstx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"    
    
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    db = client.scrapy_db
    try:
        #fill_db(db)
        read_all(db)
        #delete_all(db)
        q=0
    except Exception as e:
        print(e)     
        
