import logging
from conf import settings
from logging.handlers import RotatingFileHandler
def setlog():

    hander = RotatingFileHandler('%s/ftp.log'%settings.LOG_PATH,maxBytes=20*1024*1024,backupCount=100)
    hander.setLevel(logging.INFO)
    formate = logging.Formatter('[%(asctime)s] [%(filename)s:%(lineno)d] <%(levelname)s> %(message)s')
    hander.setFormatter(formate)
    logging.basicConfig(format='%(asctime)s [%(filename)s:%(lineno)d] <%(levelname)s> '
                               '%(message)s',datefmt='%Y-%m-%d %H:%M:%S',level=logging.INFO)
    logger = logging.getLogger()
    logger.addHandler(hander)
