import pygame

from .event_handler import EventHandler
from .ui import *
from . import *
from .app import App
from .scene import Scene
from .logger import Logger
from .state import State
from .node import Node

def init():
    pygame.init()
    State()
    Logger()
