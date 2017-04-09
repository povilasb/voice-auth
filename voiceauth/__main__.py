import numpy as np

from . import gfx, audio


def main() -> None:
    stream = audio.Stream()
    print('Recording!!!')
    buff = stream.record(1.5)
    sample = np.array(audio.stream_to_ints(buff))
    gfx.plot_vector(sample)


main()
