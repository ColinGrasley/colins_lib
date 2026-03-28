import pygame
from .node_ui import NodeUI

class TextBox(NodeUI):
    def __init__(self,name="TextBox", width=200, height=40):
        super().__init__(name,0,0,width,height)

        self.text = ""
        self.font = pygame.font.Font(None, 32)

        self.active = False

        # styles
        self.bg_color = (40, 40, 40)
        self.border_color_inactive = (150, 150, 150)
        self.border_color_active = (255, 255, 255)
        self.text_color = (255, 255, 255)

        self.text_surface = self.font.render("", True, self.text_color)

    def update(self):
        # sync rect position with VBox layout
        self.rect.topleft = (self.x, self.y)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                print("Entered:", self.text)
            else:
                self.text += event.unicode

            self.text_surface = self.font.render(self.text, True, self.text_color)

    def draw(self, screen):
        # background
        pygame.draw.rect(screen, self.bg_color, self.rect)

        # border
        border_color = self.border_color_active if self.active else self.border_color_inactive
        pygame.draw.rect(screen, border_color, self.rect, 2)

        # text
        screen.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5))