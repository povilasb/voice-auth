import os
from typing import Tuple, List

from . import audio


def next_file_name(target_dir: str) -> str:
    return '{}/{}.wav'.format(target_dir, len(os.listdir(target_dir)) + 1)


def ensure_dir_exists(target_dir: str) -> None:
    os.makedirs(target_dir, exist_ok=True)


def training_labels(training_dir: str) -> List[str]:
    return os.listdir(training_dir)


def load_data(training_dir: str) -> Tuple[list, list]:
    stream = audio.Stream()
    data = []
    labels = []
    for label in training_labels(training_dir):
        training_files = os.listdir('{}/{}'.format(training_dir, label))
        for f in training_files:
            buff = stream.read_from('{}/{}/{}'.format(training_dir, label, f))
            data.append(audio.stream_to_ints(buff))
            labels.append(label)
    return data, labels


def main() -> None:
    name = input('Whats your name: ')

    target_dir = 'data/{}'.format(name)
    ensure_dir_exists(target_dir)

    stream = audio.Stream()
    for i in range(10):
        print('Recording #{} sample...'.format(i))

        buff = stream.record(1.5)
        stream.save_to(next_file_name(target_dir), buff)


if __name__ == '__main__':
    main()
