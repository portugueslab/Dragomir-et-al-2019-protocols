# Protocols for the Dragomir et al 2019 manuscript


## Exp 20
Motion of coherence 0.0, 0.3, 0.6 and 1.0 are displayed in both directions in a randomized order

exp_20.py

## Exp 26
All transitions between displaying motion of coherences of 0.0, 0.3 and 0.8 and 1.0 in both directions are examined

exp_26.py

## Running
Both protocols can be run as python scripts after installing a new version of Stytra `pip install stytra`
For closed-loop freely-swimming experiments, stimuli have to be adjusted, and fish tracking has to be enabled in the Stytra configuration:

```python

from stytra.stimulation.stimuli import CenteringWrapper, FishTrackingStimulus, RandomDotKinematogram

class ClosedLoopKinematogram(FishTrackingStimulus, RandomDotKinematogram):
    pass


stimulus = CenteringWrapper(
                ClosedLoopKinematogram(
                    # stimulus parameters go here
                ),
                pause_stimulus=True,
                reset_phase=1,
            )


```

Please refer to the Stytra ![documentation](http://portugueslab.com/stytra) for more details. 