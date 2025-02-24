from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['movie_db']  # Your database name

# Collections
movies_collection = db['movies']
reviews_collection = db['reviews']