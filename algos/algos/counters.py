class Counters:

    def __init__(self, numbers):
        self._numbers = numbers
        self._inversions = 0

    def count_inversions(self):
        self._merge_and_count(self._numbers)
        return self._inversions

    def _merge_and_count(self, a):
        if (len(a) == 1):
            return a

        a1 = self._merge_and_count(a[0:len(a)/2])
        a2 = self._merge_and_count(a[len(a)/2:len(a)])
        return self._merge(a1, a2)

    def _merge(self, b, c):
        i = 0
        j = 0
        d = []

        for k in range(0, len(b) + len(c)):
            if (i < len(b) and j < len(c)):
                if (b[i] < c[j]):
                    d.append(b[i])
                    i = i + 1
                else:
                    self._inversions = self._inversions + len(b[i:len(b)])
                    d.append(c[j])
                    j = j + 1

            else:
                if (i < len(b)):
                    d.append(b[i])
                    i = i + 1
                else:
                    d.append(c[j])
                    j = j + 1

        return d
