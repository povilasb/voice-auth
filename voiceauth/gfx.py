from typing import List

import matplotlib.pyplot as plt
from scipy import signal
from skimage import io
import numpy as np


def plot_vector(v: List[int]) -> None:
    plt.plot(v)
    plt.ylabel('some numbers')
    plt.show()


def make_spectrogram(stream: bytes) -> np.array:
    f, t, Sxx = signal.spectrogram(stream, 44100)
    plt.pcolormesh(t, f, Sxx)
    plt.axis('off')

    img_file = '/tmp/spectrogram.png'
    plt.savefig(img_file)
    return io.imread(img_file)
