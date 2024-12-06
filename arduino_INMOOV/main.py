from board import Board

if __name__ =="__main__":
    try:
        board = Board()
        print("RUNNING MAIN")
        board.run()
    except Exception:
        print("ERROR: "+Exception)