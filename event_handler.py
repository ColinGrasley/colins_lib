import pygame
from .ui.button import Button

class EventHandler:
    def __init__(self,scene):
        self.scene = scene
        #maybe event filtering for a certain objects. 
        #if event.type not in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION):
            #return False

    def process_events(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                return False
            #print("handling events")
            self.scene.handle_event(event)
        return True
