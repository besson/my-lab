class MaxSeq:

    def __init__(self, array):
        self._seq = array
        self._start = 0
        self._end = 0

    def run(self):
        wR = 1
        wL = 0
        window = -1

        while (wR < len(self._seq)):

            if ((self._seq[wR] - self._seq[wR - 1]) != 1):
                wL = wR

            if ((wR - wL) > window):
                window = (wR - wL)
                self._start = wL
                self._end = wR

            wR = wR + 1

    def start(self):
        return self._start

    def end(self):
        return self._end