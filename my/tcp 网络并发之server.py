from socket import *
from multiprocessing import Process
from signal import *

HOST='127.0.0.0'
PORT=8888
ADDR=(HOST,PORT)


def handle(connfd):
    pass



def main():
    s = socket()
    s.bind(ADDR)
    s.listen(4)
    print("Listen the post %s"%PORT)
    signal(SIGCHLD,SIG_IGN)
    #循环连接客户端
    while True:
        try:
            connfd,addr=s.accept()
            print('come from',addr)
        except KeyboardInterrupt:
            s.close()
            return

        p=Process(target=handle,args=(connfd,))
        p.daemon =  True
        p.start()

if __name__ == '__main__':
    main()







