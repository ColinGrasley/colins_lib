from .node_ui import NodeUI
import pygame

class VBox(NodeUI):
    def __init__(self, x, y,name="VBox", spacing=10, border_color=(255,0,0), bg_color=None, border_width=0, padding=5):
        super().__init__(name,x, y)
        self.spacing = spacing
        self.border_color = border_color
        self.bg_color = bg_color
        self.border_width = border_width
        self.padding = padding

    def add(self, element):
        element.parent = self
        self.add_child(element)
        self.update_layout()

    def update_layout(self):
        current_y = self.padding
        max_width = 0

        for child in self.children:
            # Position child inside padded area
            child.x = self.x + self.padding + self.border_width
            child.y = self.y + current_y + self.border_width

            current_y += child.height + self.spacing

            if child.width > max_width:
                max_width = child.width

        # Total height of content
        total_height = current_y - self.spacing + self.padding

        # Update VBox size to fit children + padding + border
        self.width = max_width + 2 * self.padding + 2 * self.border_width
        self.height = total_height + 2 * self.border_width

    def draw(self, screen):
        # Draw background
        if self.bg_color:
            pygame.draw.rect(screen, self.bg_color, self.rect)

        # Draw children
        for child in self.children:
            child.draw(screen)

        # Draw border
        if self.border_width > 0:
            pygame.draw.rect(screen, self.border_color, self.rect, self.border_width)

    def handle_event(self, event):
        if not self.handle_hover(event):
            return False
    
        for child in self.children:
            if child.handle_event(event):
                return True
        return False