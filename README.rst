=====
About
=====

Only works on python >= 3.4.

System requirements::

    $ apt install libportaudio-dev
    $ cd libs/portaudio-v190600-20161030 && configure && make && sudo make install

Python requirements::

    $ make pyenv

Run demo application::

    $ pyenv/bin/python -m voiceauth

.. rubric:: References

.. [#f1] http://www.portaudio.com/
.. [#f2] http://people.csail.mit.edu/hubert/pyaudio
