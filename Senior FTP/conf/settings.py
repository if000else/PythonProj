from bin import ftp
####LOG
LOG_LEVEL = 10 #INFO
LOG_PATH = str(ftp.BASEDIR / "logs")

###USER
USER_DATA = str(ftp.BASEDIR / "database" / "users")

###database
DATABASE = str(ftp.BASEDIR / "database")


###SEVER
HomeOfServer =  str(ftp.BASEDIR / "database" / "server")

###socket
ADDR = '127.0.0.1'
PORT = 1212
MAXSIZE = 10240  #10M
TMOUT = 600 #10min
MAXCONN = 5 # max connecting amount
