import socket,os,time,hashlib
from conf import settings
from modules import display
from modules import log


Home = ''
FlagLogin = False
User = ''
Command = []
sk = None
def run():
    print('Welcome!')
    print(display.HelpMenu)
    login()
    init()
    while not FlagLogin:
        print(Home)
        print(FlagLogin)
        print(User)
        print(sk)
        try:
            while True:
                command = input("[server@%s]:"%User).strip()
                Command = command.split()
                if Command[0].startswith('rz'): # upload file request
                    file_path = "%s/%s"%(Home,Command[1])
                    if os.path.isfile(file_path):
                        sk.send(command.encode())
                        data = sk.recv(1024)
                        FileSize = os.stat(file_path).st_size
                        sk.send(str(FileSize).encode()) # send file size
                        m5 = hashlib.md5()
                        with open(file_path, 'rb') as f:
                            SentSize = 0
                            for line in f:
                                sk.send(line)
                                m5.update(line)
                                SentSize += len(line)
                                print("Transfer:%s%%"%(100*SentSize/FileSize),end='\r')
                        print('\rCompletely!')
                        # md5 = m5.encode()
                        sk.send(m5.hexdigest()) # send md5 value after finish
                    else:
                        print("Invalid file!")
                elif Command[0].startswith('sz'): #download files,continu when receive 'sz'
                    sk.send(command.encode())
                    data = sk.recv(1024)
                    if data.decode() == 'sz':
                        UpName = time.strftime("%Y%m%d%H%M%S:", time.localtime()) + 'upload'
                        FileSize = int(sk.recv(1024).decode())
                        RecvSize = 0
                        m5 = hashlib.md5()
                        with open('%s/%s' % (Home, UpName), 'w') as f:
                            while RecvSize < FileSize:
                                size = FileSize - RecvSize
                                if size < 1024:
                                    data = sk.recv(size)
                                else:
                                    data = sk.recv(1024)
                                m5.update(data)
                                f.write(data)
                                RecvSize += len(data)
                                print("Transfer:%s%%" % (100*RecvSize/FileSize), end='\r')
                            else:
                                print('\rCompletely!')
                        md5_recv = sk.recv(1024).decode()  # receive md5 check
                        if md5_recv == m5.hexdigest():
                            os.rename("%s/%s" % (Home, UpName),
                                      "%s/%s" % (Home, Command[1]))  # rename filename
                            print("File check passed!")
                        else:
                            sk.send(b'file crash!!!')
                            os.remove("%s/%s" % (Home, UpName))
                            print("Remove file because check failed...")
                    else:
                        print("Invalid filename!")

                elif data == 'logout':
                    FlagLogin = False
                    break
                print(data)
        except Exception:
            print("exist exception!!!")
    else:
        print("offline, use 'login' to connect server!")
        print(Home)
        print(FlagLogin)
        print(User)
        print("Disconnect to server...")


def login():
    import json
    # global FlagLogin
    # global User
    while True:
        user = input("username:").strip()
        psd = input("passwod:").strip()
        with open('%s/users/users.db', 'r') as f:
            users = json.load(f)
            if user in users:
                if psd == users[user]:
                    print("login successful!")
                    FlagLogin = True
                    User = user

                else:
                    print("Incorrect password!")
            else:
                print("No such user!")

def init():
    '''
    init users dir,socket
    :return:
    '''
    # global Home
    sk = socket.socket()
    sk.connect((settings.ADDR,settings.PORT))
    print("\033[1;34;1mConnected to socket!\033[0m", )
    path = "%s/client/%s"%(settings.DATABASE,User)
    if not os.path.exists(path):
        os.makedirs(path)
        print("Created new dir for user!")
    Home = path



