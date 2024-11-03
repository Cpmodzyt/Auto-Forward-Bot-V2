from os import environ 

class Config:
    API_ID = environ.get("API_ID", "23023343")
    API_HASH = environ.get("API_HASH", "2b79fd2d2c83173807a039325e7e166f")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7771987608:AAFpA0l29fsIPyvQx174n0Krhgtd2-pMiTU") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://AnimeFlix:Itzmecp@cluster0.qxdxy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7717701360').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
