import numpy as np
from stytra.stimulation import Protocol
import pandas as pd

from lightparam import Param
from stytra import Stytra
from stytra.stimulation.stimuli import (
    CenteringWrapper,
    RadialSineStimulus,
    FishTrackingStimulus,
    RandomDotKinematogram,
)


class Exp20Protocol(Protocol):
    name = "exp_20"

    def __init__(self):
        super().__init__()
        self.velocity = Param(5.5, (0, 40))
        self.max_coherent_for = Param(0.4, (0, 10))
        self.dot_density = Param(0.113, (0.01, 1.0))
        self.n_trials = Param(30, (1, 100))
        self.stimulus_duration = Param(12, (1, 100))
        self.pause_duration = Param(3, (1, 100))

    def get_stim_sequence(self):
        choices = np.array([1.0, 0.6, 0.3, 0.0, -0.3, -0.6, -1.0])

        order = np.concatenate(
            [np.random.permutation(len(choices)) for _ in range(self.n_trials)]
        )

        current_t = 0
        t = []
        coh_df = []
        frozen_df = []
        for i_coh in order:
            coherence = choices[i_coh]
            t.extend([current_t, current_t + self.pause_duration])
            frozen_df.extend([1, 1])
            coh_df.extend([0, 0])
            current_t += self.pause_duration
            t.extend([current_t, current_t + self.stimulus_duration])
            frozen_df.extend([0, 0])
            coh_df.extend([coherence, coherence])
            current_t += self.stimulus_duration

        coherence_df = pd.DataFrame(dict(t=t, coherence=coh_df, frozen=frozen_df))

        return [
            RandomDotKinematogram(
                df_param=coherence_df,
                dot_radius=0.6,
                color_dots=(0, 0, 0),
                color_bg=(255, 255, 255),
                velocity=self.velocity,
                max_coherent_for=self.max_coherent_for,
                dot_density=self.dot_density,
                theta=np.pi / 2,
            )
        ]


if __name__ == "__main__":
    stytra = Stytra(protocol=Exp20Protocol())
