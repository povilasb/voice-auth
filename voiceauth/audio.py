from typing import List
import struct

import pyaudio
import wave


class Stream:
    def __init__(self) -> None:
        self._rate = 44100
        self._channels = 1
        self._format = pyaudio.paInt16
        self._p = pyaudio.PyAudio()

    def __del__(self) -> None:
        self._p.terminate()

    def record(self, seconds: float) -> bytes:
        stream = self._p.open(format=self._format, channels=self._channels,
                              rate=self._rate, input=True,
                              frames_per_buffer=1024)
        audio_stream = b''
        for i in range(0, int(self._rate / 1024 * seconds)):
            audio_stream += stream.read(1024)

        stream.stop_stream()
        stream.close()

        return audio_stream

    def save_to(self, fname: List[str], stream: bytes) -> None:
        wf = wave.open(fname, 'wb')
        wf.setnchannels(self._channels)
        wf.setsampwidth(self._p.get_sample_size(self._format))
        wf.setframerate(self._rate)
        wf.writeframes(stream)
        wf.close()

    def read_from(self, fname: str) -> bytes:
        wf = wave.open(fname, 'rb')
        data = wf.readframes(1024)
        buff = data
        while data != b'':
            data = wf.readframes(1024)
            buff += data

        return buff


def chunks(data: bytes, chunk_size: int) -> List[bytes]:
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]


def stream_to_ints(stream: bytes) -> List[int]:
    if len(stream) % 2 != 0:
        raise ValueError('Illegal frame size: {}'.format(len(stream)))
    return [struct.unpack('<h', c)[0] for c in chunks(stream,  2)]
