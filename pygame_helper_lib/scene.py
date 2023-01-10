############################
# IMPORT
############################

import pygame

############################
# SCENE
############################


class Scene:
    def __init__(self):
        self.name = self.__class__.__name__

        self.init()

    def init(self):
        pass

    def update(self, events: list[pygame.event.Event], dt: float):
        pass

    def draw(self, surface: pygame.surface.Surface):
        pass

############################
# SCENE MANAGER
############################


class SceneManager:
    def __init__(self):
        self.scenes: list[Scene | None]= []
        self._currentScene: Scene | None = None

    @property
    def currentScene(self) -> Scene | None:
        return self._currentScene

    @currentScene.setter
    def currentScene(self, value):
        self.scenes.append(self._currentScene)

        for index, scene in enumerate(self.scenes):
            if value == scene:
                self.scenes.pop(index)
                break

        self._currentScene = value

    def removeCurrentScene(self):
        self.currentScene = None

    def hasActiveScene(self) -> bool:
        return self.currentScene is not None

    def update(self, events: list[pygame.event.Event], dt: float):
        if self._currentScene:
            self._currentScene.update(events, dt)

    def draw(self, surface: pygame.surface.Surface):
        if self._currentScene:
            self._currentScene.draw(surface)
