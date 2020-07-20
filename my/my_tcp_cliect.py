from socket import *



ADDR=("0.0.0.0",8888)

class FTPClient:
    def __init__(self,s):
        self.s=s
    def do_list(self):
        self.s.senf(b'list')
        res=self.s.recv(128).decode()
        if res =='OK':
            file =self.s.recv(1024*1024).decode()
            print(file)
        else:
            print("文件空的哦")





def main():
    s=socket()
    s.connect(ADDR)
    ftp=FTPClient(s)
    while True:
        print("============ 命令选项==============")
        print("***           list           ***")
        print("***         get  file        ***")
        print("***         put  file        ***")
        print("***           exit           ***")
        print("==================================")

        cmd=input('请输入命令')
        if cmd=='list':
            ftp.do_list()




