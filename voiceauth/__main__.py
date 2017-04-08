import struct
from typing import List


from . import gfx, audio


def chunks(data: bytes, chunk_size: int) -> List[bytes]:
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]


def stream_to_ints(stream: bytes) -> List[int]:
    if len(stream) % 2 != 0:
        raise ValueError('Illegal frame size: {}'.format(len(stream)))
    return [struct.unpack('<h', c)[0] for c in chunks(stream,  2)]


def main() -> None:
    stream = audio.Stream()
    buff = stream.record(1.5)
    stream.save_stream_to('output.wav', buff)

    gfx.plot_vector(stream_to_ints(buff))


main()
