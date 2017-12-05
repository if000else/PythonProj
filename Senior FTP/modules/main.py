import socket,os,time
from conf import settings
from modules import funcs
from modules import display
from modules import log

login_tool = dict(name=None,passwd=None,role='0')

def run():
    main_flag=True
    while main_flag:
        print(display.welcome)
        if not login_tool['name']:
            data = funcs.login()
            if data:
                login_tool['name'] = data["name"]
                login_tool['passwd'] = data["passwd"]
                login_tool['role'] = data["role"]
        user = User(login_tool['name'], login_tool['passwd'], login_tool['role'])
        flag = True
        while flag:
            command = funcs.ck_command()
            if command == 'useradd':
                user.adduser()
            elif command == "ls -c":
                user.ls_c()
            elif command == 'ls -s':
                user.ls_s()
            elif command.startswith("upload"):
                split = command.split(" ")
                command = split[0]
                filename = split[1]
                files = os.listdir(user.path)
                if filename in files:
                    user.upload(command,filename)
                else:
                    print("No such file!")
            elif command.startswith("download"):
                split = command.split(" ")
                command = split[0]
                filename = split[1]
                files = os.listdir(settings.F_SERVER)
                if filename in files:
                    user.download(command,filename)
                else:
                    print("No such file!")
            elif command == 'help':
                print(display.help_menu)

            elif command == 'logout':
                stat = user.switch # get sk stat and shutdown
                login_tool['name'] = None
                login_tool['passwd'] = None
                login_tool['role'] = '0'
                flag = False
            else:
                print("Invalid input!")

class User(object):
    def __init__(self,username,passwd,role='0'):
        '''
        initialize ,include path,socket
        :param username:
        :param passwd:
        :param role:
        '''
        self.username=username
        self.passwd=passwd
        self.role=role
        self.service=True #turn on service
        self.sk = socket.socket()
        self.path =''
        self.initdir()# initialize dir

        ###connect to server
        ip_port = (settings.ADDR, settings.PORT)
        self.sk.connect(ip_port)
        data = self.sk.recv(settings.MAXSIZE)
        print("\033[1;34;1mConnected to socket!\033[0m",)
        log.logger("services").info("User %s connect to socket." % self.username)

    @property
    def switch(self):
        '''
        close/open socket,run when open ,service closed
        :return:
        '''
        self.sk.sendall("quit".encode()) # quit request
        self.sk.close()#close sk
        log.logger("services").info("User %s disconnect to socket." % self.username)
        self.service = not self.service
        return self.service
    def adduser(self):
        '''
        add user
        :return:
        '''
        user = input("Input username:").strip()
        psd = input("Input password:").strip()
        role =input("Set as root?y/n:")
        if role == 'y':
            role = '1'
        else:
            role ='0'
        funcs.sign_up(user,psd,role)
    def upload(self,command,filename):
        '''
        excute upload command
        :param command:
        :return:
        '''
        self.sk.sendall(command.encode())#send command
        self.sk.sendall(filename.encode())#send filename
        with open("%s/%s"%(self.path,filename),"r") as f:
            data = f.read()
        self.sk.sendall(data.encode())##send data
        log.logger("clients").info("User %s upload." % self.username)
    def download(self,command,filename):
        '''
        :param command:
        :return:
        '''
        self.sk.sendall(command.encode())#send request
        self.sk.sendall(filename.encode())#send filname
        data = self.sk.recv(settings.MAXSIZE).decode()#receive file
        with open("%s/%s"%(self.path,filename),"w") as f:
            f.write(data)
            log.logger("clients").info("User %s upload." % self.username)
    def ls_c(self):
        '''
        show directory of users,if does not exist,create
        :return:
        '''
        print("Your home directory:")
        dirs = os.listdir(self.path)
        if not dirs:
            print("Empty!")
        else:
            for i in dirs:
                print(i)


    def ls_s(self):
        dirs = os.listdir("%s/server"%settings.DATABASE)
        print("Files in server:")
        if not dirs:
            print("Empty!")
        else:
            for i in dirs:
                print(i)
    def initdir(self):
        '''
        init users dir
        :return:
        '''
        path = "%s/client/%s"%(settings.DATABASE,self.username)
        if os.path.exists(path):
            self.path = path
        else:
            os.makedirs(path)
            print("Created dir for user!")
            self.path = path
