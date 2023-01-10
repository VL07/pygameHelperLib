############################
# IMPORT
############################

import pygame

############################
# OBJECT
############################

class Object:
	def __init__(self) -> None:
		self.init()

	def init(self) -> None:
		pass

	def update(self, events: list[pygame.event.Event], dt: float) -> None:
		pass

	def draw(self, surface: pygame.surface.Surface) -> None:
		pass