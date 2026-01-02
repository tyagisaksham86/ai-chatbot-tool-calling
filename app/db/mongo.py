from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGODB_URI"))
db = client[os.getenv("DB_NAME")]

sales_collection = db["sales"]
admin_collection = db["admin"]
chat_history = db["chat_history"]
