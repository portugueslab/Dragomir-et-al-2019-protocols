import numpy as np
from stytra.stimulation import Protocol
import pandas as pd

from lightparam import Param
from stytra.stimulation.stimuli import RandomDotKinematogram
from stytra import Stytra


class Exp26Protocol(Protocol):
    name = "exp_26"

    def __init__(self):
        super().__init__()
        self.velocity = Param(5.5, (0, 40))
        self.max_coherent_for = Param(0.4, (0, 10))
        self.dot_density = Param(0.113, (0.01, 1.0))
        self.stimulus_duration = Param(20, (1, 100))
        self.theta = Param(90, (-180, 180))
        self.dot_radius = Param(0.6, (0, 1))

    def get_stim_sequence(self):
        choices = [
            None,
            0.8,
            0.3,
            0.8,
            -0.8,
            0.8,
            -0.3,
            0.8,
            0,
            0.8,
            None,
            0.3,
            -0.8,
            0.3,
            -0.3,
            0.3,
            0,
            0.3,
            None,
            -0.8,
            -0.3,
            -0.8,
            0,
            -0.8,
            None,
            -0.3,
            0,
            -0.3,
            None,
        ]  # none is static dots; choices has 29 stimuli in a fixed order
        d = self.stimulus_duration

        t = []
        coh = []
        frozen = []

        for j, c in enumerate(choices):
            if c is None:
                coh.extend([0, 0])
                frozen.extend([1, 1])
            else:
                coh.extend([c, c])
                frozen.extend([0, 0])

            t.extend([j * d, (j + 1) * d])

        coherence_df = pd.DataFrame(dict(t=t, coherence=coh, frozen=frozen))

        return [
            RandomDotKinematogram(
                df_param=coherence_df,
                theta=self.theta * (np.pi / 180),
                dot_radius=self.dot_radius,
                color_dots=(0, 0, 0),
                color_bg=(255, 255, 255),
                velocity=self.velocity,
                max_coherent_for=self.max_coherent_for,
                dot_density=self.dot_density,
            )
        ]


if __name__ == "__main__":
    stytra = Stytra(protocol=Exp26Protocol())
