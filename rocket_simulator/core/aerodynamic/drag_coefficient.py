from dataclasses import dataclass

from ui.models.rocket_model import RocketModel

@dataclass
class DragCoefficient:
    rocket: RocketModel
    mach: float = 0.0
    reynolds: float = 0.0

    def update_parameters(self, mach: float,
                                reynolds: float) -> None:
        self.mach = mach
        self.reynolds = reynolds
        return

    def cd(self) -> float:
        return 0.1
