import pygame
from .scene import Scene
from .event_handler import EventHandler

class App:
    def __init__(self, scene=None, width=800, height=600, title="Game"):
        self.setup_app(scene,width,height,title)

    def setup_app(self, scene=None,width=800, height=600, title="Game"):
        pygame.init()

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()
        self.running = True

        self.set_scene(scene)

        self.bg_color = (30, 30, 30)

    def run(self):
        while self.running:
            self.handle_events()
            self.render()
            self.clock.tick(60)

        pygame.quit()

    def set_scene(self,scene:Scene):
        self.scene = scene
        self.event_handler = EventHandler(self.scene)

    def update():
        pass

    def render(self):
        # if self.scene.background != None:
        #     self.scene.background.draw(self.screen)
        # else:
        #     self.screen.fill(self.bg_color)
        self.scene.draw(self.screen)
        pygame.display.flip()

        
    def handle_events(self):
        if self.event_handler:
            self.running = self.event_handler.process_events()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False