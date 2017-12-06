import os,hashlib,json
with open("date.db",'w',encoding='utf-8') as f:
    psd = hashlib.md5(('admin+123456').encode('utf-8')).hexdigest()
    print(psd)
    admin = dict(admin=psd)
    json.dump(admin,f)
# os.makedirs("D:/myProject/SimpleFTP/new")