import  socket
import pickle
from threading import Thread
import  DH_code
from  random import randint
import json









def send_server():


    g = 3
    p = 17

    data = json.dumps({"g": g, "p": p})
    print("Шя отправлю")
    client.send(data.encode("utf-8"))
    print("Отпрвил")

    #A_private = randint(0, 100000)
    #Alica = DH_code.DH_Endpoint(g, p, A_private)
    A_secret = randint(0, 100000)
    A_public = (g ** A_secret) % p
    data_A = json.dumps({"Alica": A_public})
    client.send(data_A.encode("utf-8"))
    listen_thred = Thread(target=lissten_server)
    listen_thred.start()

    Bob = client.recv(1024)
    Bob1 = json.loads(Bob.decode())
    Bob_a = Bob1.get("Bob")
    print("Bob public", Bob_a)


    A_key=(Bob_a**A_secret)%p
    print("key = ",A_key)


    while True:
        client.send(input("Вы: ").encode("utf-8"))




def lissten_server():

    while True:
        data = client.recv(1024)
        print(data.decode("utf-8"))



client =socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)
client.connect(

    ("127.0.0.1",700)

)


if __name__=='__main__':

    send_server()
