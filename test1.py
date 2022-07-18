import pymongo as pm
client = pm.MongoClient("mongodb+srv://miqbalatif:7Nq2s7w3IFQZOq5Y@cluster0.w6whugs.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={'name':'ali', 'age':20, 'job':'student', 'marital':'single', 'education':'highschool'}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)