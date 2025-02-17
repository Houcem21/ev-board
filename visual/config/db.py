import pymongo

from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client.backend

products = db.products

def get_db():
    return db

def get_products():
    return products

# Just grabbing the data from mongo locally
# When deployed this needs to change