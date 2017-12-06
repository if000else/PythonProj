import socketserver,os,sys,json
from pathlib import Path
BASEDIR = Path(__file__).parent.parent
sys.path.append(str(BASEDIR))
from conf import settings
from modules import log



class MyTCPHandler(socketserver.BaseRequestHandler):
    LoginUsers = []  ### logined users
    PATH=settings.HomeOfServer### home dir
    def handle(self):
        print("client [%s] in.." % self.client_address[0])
        while True:
            comm = self.request.recv(1024)
            if comm.decode() == 'login':
                self.request.send(b'Please input username:')
                user=self.request.recv(1024).decode()
                if user =='quit':
                    self.request.send(b'quit')
                self.request.send(b'Please input password:')
                psd=self.request.recv(1024).decode()
                with open('%s/date.db'%settings.USER_DATA,'r') as f:
                    date = json.load(f)
                    if date.get(user):
                        if psd == date[user]:
                            print("client [%s] has login..."%self.client_address[0])
                            self.request.send(b'Welcome!')
                            self.LoginUsers.append(user)
                            self.operate()
                        else:
                            self.request.send(b'Incorrect user or password!')
                    else:
                        self.request.send(b'No such user!')

    def operate(self):
        try:
            while True:
                # self.request.send(b'welcome!')
                data=self.request.recv(1024).decode()
                if data == 'ls':
                    pass
                elif data == 'rz':
                    pass
                elif data == 'sz':
                    pass
                elif data == 'cd':
                    pass
                elif data == 'useradd':
                    pass
                elif data == 'logout':
                    pass
                else:
                    self.request.send(b'')
        except Exception :
            print("Exist error!!!")

if __name__ == "__main__":
    server=socketserver.ThreadingTCPServer((settings.PORT,settings.ADDR),MyTCPHandler)
    server.serve_forever(poll_interval=0.5)
    server.server_close()




###send big size files

# server=socket.socket()
# server.bind(("127.0.0.1",8888))
# server.listen(5)
# flag1=True
# flag2=True
# while flag1:
#     conn,addr=server.accept()
#     print("A client has connect in...")
#     while flag2:
#         data=conn.recv(1024).decode()
#         if not data:
#             flag2=False
#         if data.startswith("get"):
#             comm,filename=data.split()
#             print("comm,filename",comm,filename)
#             if os.path.isfile(filename):
#                 size=os.stat(filename).st_size
#                 print("size:",size)
#                 conn.send(str(size).encode()) #send size
#                 m5_obj=hashlib.md5()
#                 conn.recv(1024)# recv ack
#                 with open(filename,"rb") as f:
#                     for line in f:
#                         conn.send(line)
#                         m5=m5_obj.update(line)
#                 m5_str=m5_obj.hexdigest()
#                 print("Send finished!md5:\n",m5_str)
#                 conn.send(m5_str.encode())
#         else:
#             flag2=False
#     else:
#         pass