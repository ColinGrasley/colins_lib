import pygame
from .node_ui import NodeUI

class Button(NodeUI):
    def __init__(self, text,
                 x=0, y=0,
                 width=200, height=50,
                 name="Button",
                 on_click=None,on_hover=None):
        super().__init__(name,x,y,width,height)
        self.text = text
        self.on_click = on_click
        if on_hover is not None:
            self.on_hover = on_hover

        # default styles
        self.bg_color = (70, 130, 180)
        self.hover_color = (100, 160, 210)
        self.text_color = (255, 255, 255)

        self.font = pygame.font.Font(None, 36)

        self.rect = pygame.Rect(x, y, width, height)


    def draw(self, screen):
        color = self.hover_color if self.hovered else self.bg_color
        pygame.draw.rect(screen, color, self.rect, border_radius=8)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)

        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        super().handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered and self.on_click:
                self.on_click(event)
                return True
        return False
