


from threading import Thread
from time import sleep
import socket
import json


UDP_IP = "127.0.0.1"
UDP_PORT = 8080
MESSAGE = b"Hello, World!"

class Divisas:
    def __init__(self,dir):
        self.dirDivisas=dir

    def get_lista(self):
        try:
            with open(self.dirDivisas, "r") as f:
                path=f.read()
                texto=path.split('\n')
        except:
            print("Error lectura "+self.dirDivisas)

        try:
            with open(texto[0], "r") as f:
                archivo=f.read()
        except:
            print("Error lectura "+archivo)
        lista=archivo.split('\n')
        return lista
    
    def get_json(self):
        lista=self.get_lista()
        item=[]
        for i in range(len(lista)):
            if i==0:
                llave=lista[0].split(',')
            else:
                dic=dict()
                r=lista[i].split(',')
                dic[llave[0]]=int(r[0])
                dic["value1"]=float(r[2])
                dic["value2"]=float(r[3])
                dic["name"]=r[1]
                item.append(dic)
        return json.dumps(item)
        
       
        



    
        




class hiloPrueba(Thread):
    def __init__(self,nomb):
        super().__init__() 
        self.nombre=nomb
    def run(self):
        print('hola mundo')
        sleep(0.5)

#print(li)

ob=Divisas("config.txt")
while True:
    a=ob.get_json()
    print(a)
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
    sock.sendto(bytes(a, "utf-8"), (UDP_IP, UDP_PORT))
    sleep(30)
    