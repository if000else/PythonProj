import os,hashlib,json
with open("users.db",'w',encoding='utf-8') as f:
    admin = dict(admin='123456',alex='123456')
    json.dump(admin,f)
# os.makedirs("D:/myProject/SimpleFTP/new")