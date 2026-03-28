from .event_handler import EventHandler
from .ui.node_ui import NodeUI
from .node_2D import Node2D

class Scene:
    def __init__(self,name="Scene",root=None):
        self.root = root
        self.name = name

    def draw(self, screen, camera=None):
        # Draw layers bottom → top
        self.root.draw(screen)

    def update(self, dt):
        # Update all layers (game → UI is fine)
        self.root.update()

    def handle_event(self, event):
        # Route events to top layers first (UI gets priority)
            # Top-most first: UI, then game
        for child in self.root.children[::-1]:
            if self.root.handle_event(event):
                return True
        return False

    def __str__(self):
        result = self.__class__.__name__ + ": " + self.name + "\n"
        result += str(self.root)
        return result

    def add(self, node):
        if self.root is None:
            self.root = node
            return self
        self.root.add_child(node)
        return self