import pygame
from .node_ui import NodeUI
class Label(NodeUI):
    def __init__(self, text,
                 x=0, y=0,
                 name="Label",
                 font=None,
                 color=(255, 255, 255),
                 bg_color=None):
        super().__init__(name,x,y,0,0)

        self.text = text
        self.font = font or pygame.font.Font(None, 36)
        self.color = color
        self.bg_color = bg_color

        self._render_text()

    def _render_text(self):
        self.text_surface = self.font.render(self.text, True, self.color)

        self.width = self.text_surface.get_width()
        self.height = self.text_surface.get_height()

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def set_text(self, new_text):
        self.text = new_text
        self._render_text()

    def update(self):
        self.rect.topleft = (self.x, self.y)

    def handle_event(self, event):
        pass

    def draw(self, screen):
        if self.bg_color:
            pygame.draw.rect(screen, self.bg_color, self.rect)

        screen.blit(self.text_surface, (self.x, self.y))


