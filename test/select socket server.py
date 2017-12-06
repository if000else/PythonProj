import socket,select,queue
server = socket.socket()
server.bind(("localhost",8080))
server.listen(1000)
server.setblocking(False)#不阻塞

inputs = [server]
outputs = []
messages = {}
while True:
    readable,writable,exception = select.select(inputs,outputs,inputs)#开始监视
    for r in readable:
        if r is server:#有新客户端连接
            conn, addr = r.accept()#创建连接
            conn.setblocking(False)#不阻塞
            print("A client has connected in:",addr)
            inputs.append(conn)#添加连接到监听列表
            messages[conn] = queue.Queue()#为连接创建一个发送数据的缓存队列,
        else:#收到之前连接过的客户端请求
            data = r.recv(1024)
            if data:
                messages[r].put(data)#将数据保存在缓存队列，等待下次循环发送
                if r not in outputs:
                    outputs.append(r)
            else:
                print("A cliend has disconnected!",r)
                inputs.remove(r)
    for w in writable:#监测客户端数据请求
        try:
            text = messages[w].get_nowait()
        except queue.Empty:
            outputs.remove(w)
        else:
            w.send(text)
            print("send text to client...", text.decode())
    for e in exception:#报错列表中存在客户端连接
        if e in outputs:
            outputs.remove(e)#删除请求接受数据的此客户端
        inputs.remove(e)#删除监控的此客户端
        del messages[e]#删除此客户端队列
        e.closed()#关掉此连接
