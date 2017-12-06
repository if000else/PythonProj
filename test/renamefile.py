import os,sys
print(sys.path)
path = 'D:/PythonProj/test/rename'
count = 1
for item in os.listdir(path):
    new_name = '%s/wallpaper%s.jpg'%(path,count)
    old_name = '%s/%s'%(path,item)
    os.rename(old_name,new_name)
    count += 1
    print("successful!")

