import pygame

class Node:
    def __init__(self, name="Node"):
        self.name = name
        self.parent = None
        self.children = []
        self.active = True
        self.visible = True
        self.signals = {}

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def remove_child(self, child):
        self.children.remove(child)
        child.parent = None
    
    def get_children(self):
        return self.children
    
    def _update_tree(self, dt):
        if not self.active:
            return
        self.update(dt)
        for child in self.children:
            child._update_tree(dt)

    def connect(self, signal_name, func):
        #creates/gets list from dict: appends function to list
        self.signals.setdefault(signal_name, []).append(func)

    def emit(self, signal_name, *args):
        for func in self.signals.get(signal_name, []):
            func(*args)

    def get_root(self):
        node = self
        while node.parent:
            node = node.parent
        return node

    def find(self, name):
        if self.name == name:
            return self
        for child in self.children:
            result = child.find(name)
            if result:
                return result
        return None
    
    def ready(self):
        """Called once when added to the scene"""
        pass

    def update(self):
        """Called every frame"""
        pass

    def physics_update(self, dt): # fixed timestep
        pass

    def draw(self, screen):
        """Called every frame"""
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        result = self.__class__.__name__ + ": " + self.name + "\n"
        for child in self.children:
            result += (" "+str(child))
        return result