import pygame
from ..node import Node

class NodeUI(Node):
    def __init__(self, name="NodeUI",x=0, y=0, width=0, height=0):
        super().__init__(name)

        # Initialize rect with the provided x, y
        self.rect = pygame.Rect(x, y, width, height)
        self.hovered = False

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, val):
        self.rect.x = val

    @property
    def y(self):
        return self.rect.y

    @y.setter
    def y(self, val):
        self.rect.y = val

    @property
    def width(self):
        return self.rect.width

    @width.setter
    def width(self, val):
        self.rect.width = val

    @property
    def height(self):
        return self.rect.height

    @height.setter
    def height(self, val):
        self.rect.height = val

    @property
    def pos(self):
        return self.rect.topleft

    @pos.setter
    def pos(self, value):
        self.rect.topleft = value

    @property
    def size(self):
        return self.rect.size

    @size.setter
    def size(self, value):
        self.rect.size = value

    @property
    def center(self):
        return self.rect.center

    @center.setter
    def center(self, value):
        self.rect.center = value

    def contains_point(self, pos):
        return self.rect.collidepoint(pos)

    def collides_with(self, other):
        return self.rect.colliderect(other.rect)

    def handle_hover(self, event):
        if hasattr(event,"pos"):
            mouse_pos = event.pos
            was_hovered = self.hovered
            self.hovered = self.rect.collidepoint(mouse_pos)
        
            if self.hovered:
                if not was_hovered:
                    self.on_enter_hover()
                self.on_hover(mouse_pos)
            elif was_hovered:
                self.on_exit_hover()
                    
            return self.hovered


    def on_hover(self, *args): pass
    def on_enter_hover(self): pass
    def on_exit_hover(self): pass

    def handle_event(self, event):
        self.handle_hover(event)

        for child in self.children:
            if child.handle_event(event):
                return True
        return False
