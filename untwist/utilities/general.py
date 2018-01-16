from __future__ import division, print_function
import wave
import shutil
import tempfile
import numpy as np


class TemporaryDirectory(object):
    """
    Context manager for tempfile.mkdtemp().
    This class is available in python +v3.2.
    From: https://gist.github.com/cpelley/10e2eeaf60dacc7956bb
    """
    def __enter__(self):
        self.dir_name = tempfile.mkdtemp()
        return self.dir_name

    def __exit__(self, exc_type, exc_value, traceback):
        shutil.rmtree(self.dir_name)


def get_duration(wav_file):
    with wave.open(wav_file, 'rb') as f:
        return f.getnframes() / f.getframerate()


def calc_num_frames(signal_length,
                    window_size,
                    hop_size,
                    pad_start,
                    pad_end):

    half_window = int(window_size // 2)

    if pad_end:

        if pad_start:

            num_frames = np.ceil(
                (signal_length + half_window) /
                hop_size)
        else:

            num_frames = np.ceil(signal_length / hop_size)

    elif pad_start:

        num_frames = np.floor(
            (signal_length + half_window - window_size) /
            hop_size) + 1
    else:

        num_frames = np.floor(
            (signal_length - window_size) /
            hop_size) + 1

    return int(num_frames)
