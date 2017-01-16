class player:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print("Hello {}!".format(self.name))
        return '{}'.format(self.name)