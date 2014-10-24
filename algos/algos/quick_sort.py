class QuickSort:

    def __init__(self, array):
        self._array = array

    def sort(self):
        self._sort(0, self._array)
        return self._array

    def _sort(self, start, array):
        if (len(array) <= 1):
            return array

        p = self.partition(start, len(array) - 1)
        self._sort(start, array[start:p -1])
        self._sort(p + 1, array[p + 1:len(array)])

    def partition(self, i, j):
        pos = i
        i = i + 1

        while (i <= j):
            if (self._array[i] < self._array[pos]):
                i = i + 1
            elif (self._array[j] > self._array[pos]):
                j = j - 1
            else:
                temp = self._array[i]
                self._array[i] = self._array[j]
                self._array[j] = temp
                i = i + 1
                j = j - 1

        pivot = self._array[pos]
        self._array[pos] = self._array[i - 1]
        self._array[i - 1] = pivot

        return i - 1