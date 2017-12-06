import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        try:
            while True:
                self.data = self.request.recv(1024)
                print(self.client_address[0])
                print("client %s wrote:" % self.request.__dic__, self.data.decode())
        except Exception:
            print("disconnect...")
            server.server_close()


if __name__ == "__main__":
    ip,addr="127.0.0.1",9999
    server=socketserver.ThreadingTCPServer((ip,addr),MyTCPHandler)
    server.serve_forever(poll_interval=15)
    print("finish")