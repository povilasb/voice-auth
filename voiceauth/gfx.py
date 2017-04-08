from typing import List

import matplotlib.pyplot as plt


def plot_vector(v: List[int]) -> None:
    plt.plot(v)
    plt.ylabel('some numbers')
    plt.show()
