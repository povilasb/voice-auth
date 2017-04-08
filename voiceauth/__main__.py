from sklearn.neighbors import KNeighborsClassifier

from . import gfx, audio, train



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
