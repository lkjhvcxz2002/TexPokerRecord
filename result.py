from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

# connection
conn = MongoClient("mongodb://user:admin000@ds239911.mlab.com:39911/texpoker") # 如果你只想連本機端的server你可以忽略，遠端的url填入: mongodb://<user_name>:<user_password>@ds<xxxxxx>.mlab.com:<xxxxx>/<database_name>，請務必既的把腳括號的內容代換成自己的資料。
db = conn.texpoker
collection = db.result

# test if connection success
print("Begin find")
cursor = collection.find().sort("_id", -1)
lastRecord = cursor.next()
gameNo = lastRecord["GameNo"] + 1

print("Begin insert")
insert_dict = {"GameNo": gameNo, "Chips": 5000, "RoundCount": 33, "Duration(sec)": 600, 
"CallCount": 0, "RaiseCount": 0, "FoldCount": 0, "BetCount": 0, "AllInCount": 0, "LoseCount": 30, "WinCount": 0,
"UpdateTime": datetime.now()}
collection.insert_one(insert_dict)