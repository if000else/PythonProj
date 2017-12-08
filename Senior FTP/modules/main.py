import socket,os,time
from conf import settings
from modules import funcs
from modules import display
from modules import log


Home = ''
FlagLogin = False
User = ''
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
                sk.send(command.encode())
                data = sk.recv(1024).decode()
                if data == 'rz': # upload signal
                    pass
                elif data == 'sz': # download signal
                    pass
                elif data == 'logout':
                    FlagLogin = False
                    break
                print(data)
        except Exception:
            print("exist exception!!!")
    else:
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
        ###connect to server
        # ip_port = (settings.ADDR, settings.PORT)
        # self.sk.connect(ip_port)
        # print("\033[1;34;1mConnected to socket!\033[0m",)
    # def ls_s(self):
    #     dirs = os.listdir("%s/server"%settings.DATABASE)
    #     print("Files in server:")
    #     if not dirs:
    #         print("Empty!")
    #     else:
    #         for i in dirs:
    #             print(i)




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

# def login():
#     import json
#     global FlagLogin
#     global User
#     while True:
#         user = input("username:").strip()
#         psd = input("passwod:").strip()
#         with open('%s/users/users.db','r') as f:
#             users = json.load(f)
#             if user in users:
#                 if psd == users[user]:
#                     print("login successful!")
#                     FlagLogin = True
#                     User = user
#
#                 else:
#                     print("Incorrect password!")
#             else:
#                 print("No such user!")

