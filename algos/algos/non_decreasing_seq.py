import sys


class NonDecreasingSeq:

    def __init__(self):
        self._seq = []

    def get_seq(self, numbers):
        seq = self._init_seq(len(numbers))
        _max = sys.maxint * -1

        for i in range(0, len(numbers)):
            for j in range(0, i):
                if (numbers[j] <= numbers[i] and seq[j] + 1 > seq[i]):
                    seq[i] = seq[j] + 1

            if (seq[i] >= _max):
                _max = seq[i]

        return _max

    def _init_seq(self, size):
        return [1 for i in range(0, size)]