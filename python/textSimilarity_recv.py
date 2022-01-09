from multiprocessing.connection import Listener, Client
import sys

address = ('localhost', 6000)

def getTS(input_text = "갑자기 배가 아파요"):
    with Listener(address, authkey=b'secret password') as listener:
        with listener.accept() as conn:
            print('connection accepted from', listener.last_accepted)
            conn.send(input_text)

    with Client(address, authkey=b'secret password') as conn:
        print(conn.recv())                  # => [2.25, None, 'junk', float]

if __name__ == '__main__':
    getTS(sys.argv[1]) if len(sys.argv) >= 2 else getTS()