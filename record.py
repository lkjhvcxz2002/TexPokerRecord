from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

# connection
conn = MongoClient("mongodb://user:admin000@ds239911.mlab.com:39911/texpoker") # 如果你只想連本機端的server你可以忽略，遠端的url填入: mongodb://<user_name>:<user_password>@ds<xxxxxx>.mlab.com:<xxxxx>/<database_name>，請務必既的把腳括號的內容代換成自己的資料。
db = conn.texpoker
collection = db.record

# test if connection success
print("Begin find")
cursor = collection.find().sort("_id", -1)
lastRecord = cursor.next()
gameNo = 10
roundNo = lastRecord["RoundNo"] + 1

print("Begin insert")
insert_dict = {"GameNo": gameNo, "RoundNo": roundNo, "Chips": 5000, "Hands": "7A,6H", "Table": "1A,1H,1D", 
"Bet": 300, "IsWinner": False, "UpdateTime": datetime.now()}
collection.insert_one(insert_dict)