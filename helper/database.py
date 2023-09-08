# Copyright (C) 2023 DX_MODS
#Licensed under the  AGPL-3.0 License;
#you may not use this file except in compliance with the License.
#Author ZIYAN"

import motor.motor_asyncio
from config import Config
from .utils import send_log

class Database:

    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.user

    def new_user(self, id):
        return dict(
            _id=int(id),                                   
            file_id=None,
            caption=None
        )

    #Total User 

def total_user():
      user = self.col.count_documents({})
      return user
      
#insert bot Data 
def botdata(chat_id):
	bot_id = int(chat_id)
	try:
		bot_data = {"_id":bot_id,"total_rename":0,"total_size":0}
		dbcol.insert_one(bot_data)
	except:
		pass


def total_rename(chat_id,renamed_file):
	now = int(renamed_file) + 1
	self.col.update_one({"_id":chat_id},{"$set":{"total_rename":str(now)}})
	
def total_size(chat_id,total_size,now_file_size):
	now = int(total_size) + now_file_size
	self.col.update_one({"_id":chat_id},{"$set":{"total_size":str(now)}})

	
#insert user data 
def insert(chat_id):
            user_id = int(chat_id)
            user_det = {"_id":user_id,"file_id":None ,"caption":None ,"daily":0 ,"date":0 , "uploadlimit" :2147483648,"used_limit":0,"usertype":"Free","prexdate" : None}
            try:
            	self.col.insert_one(user_det)
            except:
            	return True
            	pass

def addthumb(chat_id, file_id):
	self.col.update_one({"_id":chat_id},{"$set":{"file_id":file_id}})
	
def delthumb(chat_id):
	self.col.update_one({"_id":chat_id},{"$set":{"file_id":None}})

def addcaption(chat_id, caption):
       self.col.update_one({"_id": chat_id},{"$set":{"caption": caption}})
	
def delcaption(chat_id): 
        self.col.update_one({"_id": chat_id},{"$set":{"caption":None}})
	
def dateupdate(chat_id,date):
	self.col.update_one({"_id":chat_id},{"$set":{"date":date}})

def used_limit(chat_id,used):
	self.col.update_one({"_id":chat_id},{"$set":{"used_limit":used}})
	
def usertype(chat_id,type):
	self.col.update_one({"_id":chat_id},{"$set":{"usertype":type}})
	
def uploadlimit(chat_id,limit):
	self.col.update_one({"_id":chat_id},{"$set":{"uploadlimit":limit}})

def backpre(chat_id):
    self.col.update_one({"_id":chat_id},{"$set":{"prexdate":None}})
    
def addpre(chat_id):
    date = add_date()
    self.col.update_one({"_id":chat_id},{"$set":{"prexdate":date[0]}})

def addpredata(chat_id):
    self.col.update_one({"_id":chat_id},{"$set":{"prexdate":None}})
    
  
def daily(chat_id,date):
	  self.col.update_one({"_id":chat_id},{"$set":{"daily":date}})
	  
def find(chat_id):
	id =  {"_id":chat_id}
	x = self.col.find(id)
	for i in x:
             file = i["file_id"]
             try:
                 caption = i["caption"]
             except:
                 caption = None
                 
             return [file, caption]

def getid():
    values = []
    for key  in self.col.find():
         id = key["_id"]
         values.append((id)) 
    return values

def delete(id):
	self.col.delete_one(id)
	
def find_one(id):
	return self.col.find_one({"_id":id})

db = Database(Config.DB_URL, Config.DB_NAME)



