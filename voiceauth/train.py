import os

from . import audio


def next_file_name(target_dir: str) -> str:
    return '{}/{}.wav'.format(target_dir, len(os.listdir(target_dir)) + 1)


def ensure_dir_exists(target_dir: str) -> None:
    os.makedirs(target_dir, exist_ok=True)


def main() -> None:
    name = input('Whats your name: ')

    target_dir = 'data/{}'.format(name)
    ensure_dir_exists(target_dir)

    stream = audio.Stream()
    for i in range(10):
        print('Recording #{} sample...'.format(i))

        buff = stream.record(1.5)
        stream.save_to(next_file_name(target_dir), buff)


main()
