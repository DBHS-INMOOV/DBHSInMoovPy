class ObjectTemplate():
    def __init__(self, name="Object", x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def getName(self):
        return self.name
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y