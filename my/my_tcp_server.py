from socket import *
from threading import Thread
import os,time

HOST='0.0.0.0'
PORT=8888
ADDR=(HOST,PORT)
FTP='/home/tarena/FTP/'
class FTPServer(Thread):
    def __init__(self,connfd):
        self.connfd=connfd
        super().__init__()
    def do_list(self):
        file_list=os.listdir(FTP)
        if not file_list:
            self.connfd.send(b'FALL')
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.01)
            data='\n'.join(file_list)
            self.connfd.send(data.encode())



    def run(self):
        while True:
            data,addr=self.connfd.recv(1024).decode()
            if data=='list':
                self.do_list()

def main():
    s=socket()
    s.bind(ADDR)
    s.listen(5)
    print("listen from the %s"%PORT)

    while True:
        try:
            connfd,addr=s.accept()
        except KeyboardInterrupt:
            s.close()
            return

    t=FTPServer(connfd)
    t.start()

if __name__ == '__main__':
    main()
