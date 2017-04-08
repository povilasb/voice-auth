import struct
from typing import List

from sklearn.neighbors import KNeighborsClassifier

from . import gfx, audio, train


def chunks(data: bytes, chunk_size: int) -> List[bytes]:
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]


def stream_to_ints(stream: bytes) -> List[int]:
    if len(stream) % 2 != 0:
        raise ValueError('Illegal frame size: {}'.format(len(stream)))
    return [struct.unpack('<h', c)[0] for c in chunks(stream,  2)]


def main() -> None:
    clf = KNeighborsClassifier(3)
    clf.fit(*train.load_data('data'))

    stream = audio.Stream()
    print('Recording!!!')
    buff = stream.record(1.5)
    sample = stream_to_ints(buff)
    print(clf.predict([sample]))
    # gfx.plot_vector(stream_to_ints(buff))


main()
