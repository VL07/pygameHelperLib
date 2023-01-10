############################
# IMPORTS
############################

from dataclasses import dataclass

############################
# DEBUG INFO
############################


@dataclass
class DebugInfo:
    fps: float = 0
    dt: float = 0
    scenes: int = 0
    activeScene: str = "Default"
