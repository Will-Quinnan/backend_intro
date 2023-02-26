import pymongo
import certifi

con_str = "mongodb+srv://willq:123qwe@cluster0.xkpeovp.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("onlinestore_ch34")