import os

class State:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        self.screen_size = (800,600)
        self.rescources = {}
        self.debug = False
        self.assets_path = os.getcwd()