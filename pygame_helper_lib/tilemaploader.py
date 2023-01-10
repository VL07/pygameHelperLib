############################
# IMPORT
############################

import pygame

############################
# SCENE
############################

def loadTileMap(image: pygame.surface.Surface, tileSize: pygame.Vector2) -> list[pygame.surface.Surface]:
	if image.get_width() % tileSize.x != 0:
		raise Exception("The width of the provided image dose not match the tile width")
	elif image.get_height() % tileSize.y != 0:
		raise Exception("The height of the provided image dose not match the tile height")

	tiles: list[pygame.surface.Surface] = []

	for y in range(int(image.get_height() / tileSize.y)):
		for x in range(int(image.get_width() / tileSize.x)):
			tiles.append(image.subsurface(pygame.rect.Rect(x * tileSize.x, y * tileSize.y, tileSize.x, tileSize.y)))

	return tiles