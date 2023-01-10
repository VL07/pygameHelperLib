############################
# IMPORT
############################

from typing import Callable
import pygame
from pygame import Vector2
from datetime import datetime
import traceback
from .scene import SceneManager
from .debuginfo import DebugInfo
from dataclasses import fields

############################
# GAME
############################


class Game:
    def __init__(
            self,
            productionMode: bool,
            gameName: str,
            screenSize: Vector2 = Vector2(100, 100),
            canvasSize: Vector2 | None = None,
            screenInitMethod: Callable[[], pygame.surface.Surface] | None = None,
            fps: int = 30):
        self.display: pygame.surface.Surface

        if screenInitMethod:
            self.display = screenInitMethod()
        else:
            self.display = pygame.display.set_mode(screenSize)

        pygame.init()

        # Vars
        self.run: bool = True
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.fps: int = fps
        self.canvasSize: Vector2 = canvasSize if canvasSize else screenSize
        self.productionMode: bool = productionMode
        self.gameName = gameName
        self.sceneManager = SceneManager()
        self.showDebugInfo: bool = False

        if not self.productionMode:
            self.debugInfo: DebugInfo = DebugInfo()
            self.debugFont = pygame.font.SysFont("arial", 24)

        # Funcs
        if self.productionMode:
            try:
                self.init()
                self.loop()
            except Exception as err:
                self._error(err)
        else:
            print("Use [F1] to show/hide the debug info menu")

            self.init()
            self.loop()

    def _error(self, err: Exception):
        pygame.quit()
        self.run = False

        fileName: str = f"error-log-{datetime.now().strftime('%m-%d-%-y_%h-%m-%s')}.txt"

        with open(fileName, "w") as f:
            f.write(traceback.format_exc())

    def _drawDebugInfo(self, surface: pygame.surface.Surface):
        texts = [f"{field.name}: {getattr(self.debugInfo, field.name)}" for field in fields(self.debugInfo)]

        for index, text in enumerate(texts):
            textSuface = self.debugFont.render(text, False, (0, 0, 0))
            surface.blit(textSuface, Vector2(10, 10 + index * 30))

    def init(self):
        pass

    def loop(self):
        while self.run:
            dt: float = self.clock.tick(self.fps) / 1000

            # Update debuger info data
            if not self.productionMode:
                self.debugInfo.dt = dt
                self.debugInfo.fps = self.clock.get_fps()
                self.debugInfo.scenes = len(self.sceneManager.scenes)
                self.debugInfo.activeScene = self.sceneManager.currentScene.name \
                    if self.sceneManager.currentScene else "Default"

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                    self.showDebugInfo = not self.showDebugInfo

            self.updateMain(pygame.event.get(), dt)

            self.sceneManager.update(pygame.event.get(), dt)
            self.update(pygame.event.get(), dt)

            canvasSize = self.canvasSize if self.canvasSize else self.display.get_size()
            canvas = pygame.surface.Surface(canvasSize)
            if self.sceneManager.hasActiveScene():
                self.sceneManager.draw(canvas)
            else:
                self.draw(canvas)

            if canvasSize != self.display.get_size():
                canvas = pygame.transform.scale(canvas, self.display.get_size())

            if self.showDebugInfo:
                self._drawDebugInfo(canvas)

            self.display.blit(canvas, Vector2(0, 0))

            pygame.display.update()

    def updateMain(self, events: list[pygame.event.Event], dt: float):
        pass

    def update(self, events: list[pygame.event.Event], dt: float):
        pass

    def draw(self, surface: pygame.surface.Surface):
        pass
