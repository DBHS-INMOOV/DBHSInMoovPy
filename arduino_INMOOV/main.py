import threading
from board import Board

activeThreads = []

if __name__ =="__main__":
    board = Board()

    boardThread = threading.Thread(target=board.run(),args=())
    activeThreads.append(boardThread)

    for i in activeThreads:
        i.start()
    
    for i in activeThreads:
        i.join()